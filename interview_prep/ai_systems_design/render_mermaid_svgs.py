from __future__ import annotations

import html
import re
import textwrap
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "images"


@dataclass
class Node:
    id: str
    label: str
    shape: str = "rect"
    group: str | None = None
    order: int = 0
    lines: list[str] = field(default_factory=list)
    width: int = 0
    height: int = 0
    x: float = 0
    y: float = 0


@dataclass
class Edge:
    source: str
    target: str
    label: str = ""
    dashed: bool = False


@dataclass
class Group:
    id: str
    label: str
    order: int
    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0


@dataclass
class Diagram:
    direction: str
    nodes: dict[str, Node]
    edges: list[Edge]
    groups: dict[str, Group]
    original: str


def clean_label(label: str) -> str:
    label = label.strip().strip('"')
    label = re.sub(r"<br\s*/?>", "\n", label, flags=re.I)
    return label


def split_label(label: str, max_chars: int = 26) -> list[str]:
    pieces: list[str] = []
    for raw in clean_label(label).splitlines() or [""]:
        wrapped = textwrap.wrap(raw, width=max_chars, break_long_words=False)
        pieces.extend(wrapped or [""])
    return pieces


def ensure_node(nodes: dict[str, Node], node_id: str, label: str | None, shape: str, group: str | None) -> Node:
    if node_id not in nodes:
        nodes[node_id] = Node(
            id=node_id,
            label=clean_label(label or node_id),
            shape=shape,
            group=group,
            order=len(nodes),
        )
    elif label:
        nodes[node_id].label = clean_label(label)
        nodes[node_id].shape = shape
        if group and nodes[node_id].group is None:
            nodes[node_id].group = group
    return nodes[node_id]


def parse_endpoint(token: str, nodes: dict[str, Node], group: str | None, groups: dict[str, Group]) -> str:
    token = token.strip().rstrip(";")
    for pattern, shape in (
        (r"^([A-Za-z][\w-]*)\[(.*)\]$", "rect"),
        (r"^([A-Za-z][\w-]*)\{(.*)\}$", "diamond"),
        (r"^([A-Za-z][\w-]*)\((.*)\)$", "rect"),
    ):
        match = re.match(pattern, token)
        if match:
            node_id, label = match.groups()
            ensure_node(nodes, node_id, label, shape, group)
            return node_id
    if token in groups:
        return token
    match = re.match(r"^([A-Za-z][\w-]*)$", token)
    if match:
        node_id = match.group(1)
        if node_id not in groups:
            ensure_node(nodes, node_id, None, "rect", group)
        return node_id
    return token


def parse_edge(line: str) -> tuple[str, str, str, bool] | None:
    if "-." in line and ".->" in line:
        left, rest = line.split("-.", 1)
        label, right = rest.split(".->", 1)
        return left.strip(), right.strip(), label.strip(), True
    if "-->|" in line:
        left, rest = line.split("-->|", 1)
        label, right = rest.split("|", 1)
        return left.strip(), right.strip(), label.strip(), False
    if "-->" in line:
        left, right = line.split("-->", 1)
        return left.strip(), right.strip(), "", False
    return None


def parse_diagram(source: str) -> Diagram:
    nodes: dict[str, Node] = {}
    edges: list[Edge] = []
    groups: dict[str, Group] = {}
    direction = "LR"
    group_stack: list[str] = []

    for raw in source.splitlines():
        line = raw.strip()
        if not line:
            continue
        header = re.match(r"^flowchart\s+(\w+)", line)
        if header:
            direction = header.group(1)
            continue
        group_match = re.match(r"^subgraph\s+([A-Za-z][\w-]*)(?:\[(.*)\])?$", line)
        if group_match:
            group_id, label = group_match.groups()
            groups[group_id] = Group(group_id, clean_label(label or group_id), len(groups))
            group_stack.append(group_id)
            continue
        if line == "end":
            if group_stack:
                group_stack.pop()
            continue

        current_group = group_stack[-1] if group_stack else None
        parsed = parse_edge(line)
        if parsed:
            left, right, label, dashed = parsed
            source_id = parse_endpoint(left, nodes, current_group, groups)
            target_id = parse_endpoint(right, nodes, current_group, groups)
            edges.append(Edge(source_id, target_id, clean_label(label), dashed))
            continue
        parse_endpoint(line, nodes, current_group, groups)

    for node in nodes.values():
        node.lines = split_label(node.label)
        max_len = max((len(line) for line in node.lines), default=len(node.id))
        node.width = max(150, min(260, max_len * 8 + 34))
        node.height = max(54, len(node.lines) * 18 + 26)
        if node.shape == "diamond":
            node.width = max(node.width, 170)
            node.height = max(node.height, 88)

    return Diagram(direction=direction, nodes=nodes, edges=edges, groups=groups, original=source)


def forward_ranks(nodes: list[Node], edges: list[Edge], group_ids: set[str]) -> dict[str, int]:
    order = {node.id: node.order for node in nodes}
    ranks = {node.id: 0 for node in nodes}
    usable = [
        edge
        for edge in edges
        if edge.source in ranks
        and edge.target in ranks
        and edge.source not in group_ids
        and edge.target not in group_ids
        and order[edge.target] > order[edge.source]
    ]
    for _ in range(max(1, len(nodes))):
        changed = False
        for edge in usable:
            if ranks[edge.target] < ranks[edge.source] + 1:
                ranks[edge.target] = ranks[edge.source] + 1
                changed = True
        if not changed:
            break
    return ranks


def layout_nodes(diagram: Diagram) -> tuple[int, int]:
    margin = 34
    gap_x = 82
    gap_y = 62

    if diagram.groups:
        cursor_x = margin
        max_bottom = margin
        for group in sorted(diagram.groups.values(), key=lambda item: item.order):
            group_nodes = [node for node in diagram.nodes.values() if node.group == group.id]
            ranks = forward_ranks(group_nodes, diagram.edges, set(diagram.groups))
            by_rank: dict[int, list[Node]] = defaultdict(list)
            for node in group_nodes:
                by_rank[ranks.get(node.id, 0)].append(node)

            inner_x = cursor_x + 28
            inner_y = margin + 54
            if diagram.direction == "TB":
                group_width = max((node.width for node in group_nodes), default=180) + 56
                for rank in sorted(by_rank):
                    row = sorted(by_rank[rank], key=lambda node: node.order)
                    row_width = sum(node.width for node in row) + gap_x * max(0, len(row) - 1)
                    start_x = inner_x + max(0, (group_width - 56 - row_width) / 2)
                    max_h = max((node.height for node in row), default=54)
                    for node in row:
                        node.x = start_x
                        node.y = inner_y
                        start_x += node.width + gap_x
                    inner_y += max_h + gap_y
                group.width = max(group_width, max((node.x + node.width - cursor_x + 28 for node in group_nodes), default=220))
                group.height = max(140, inner_y - margin + 8)
            else:
                group_height = max((node.height for node in group_nodes), default=54) + 92
                for rank in sorted(by_rank):
                    col = sorted(by_rank[rank], key=lambda node: node.order)
                    max_w = max((node.width for node in col), default=150)
                    start_y = inner_y
                    for node in col:
                        node.x = inner_x
                        node.y = start_y
                        start_y += node.height + gap_y
                    inner_x += max_w + gap_x
                    group_height = max(group_height, start_y - margin + 8)
                group.width = max(220, inner_x - cursor_x + 2)
                group.height = group_height

            group.x = cursor_x
            group.y = margin
            cursor_x += group.width + 52
            max_bottom = max(max_bottom, group.y + group.height)

        loose_nodes = [node for node in diagram.nodes.values() if node.group is None]
        for idx, node in enumerate(sorted(loose_nodes, key=lambda item: item.order)):
            node.x = margin + idx * (node.width + gap_x)
            node.y = max_bottom + 40

        width = int(max([group.x + group.width for group in diagram.groups.values()] + [node.x + node.width for node in diagram.nodes.values()] + [0]) + margin)
        height = int(max([group.y + group.height for group in diagram.groups.values()] + [node.y + node.height for node in diagram.nodes.values()] + [0]) + margin)
        return width, height

    ranks = forward_ranks(list(diagram.nodes.values()), diagram.edges, set())
    by_rank: dict[int, list[Node]] = defaultdict(list)
    for node in diagram.nodes.values():
        by_rank[ranks.get(node.id, 0)].append(node)

    if diagram.direction == "TB":
        y = margin
        for rank in sorted(by_rank):
            row = sorted(by_rank[rank], key=lambda node: node.order)
            row_width = sum(node.width for node in row) + gap_x * max(0, len(row) - 1)
            x = margin
            if len(row) > 1:
                x = margin
            for node in row:
                node.x = x
                node.y = y
                x += node.width + gap_x
            y += max(node.height for node in row) + gap_y
    else:
        x = margin
        for rank in sorted(by_rank):
            col = sorted(by_rank[rank], key=lambda node: node.order)
            col_height = sum(node.height for node in col) + gap_y * max(0, len(col) - 1)
            y = margin
            if len(col) > 1:
                y = margin
            max_w = max(node.width for node in col)
            for node in col:
                node.x = x
                node.y = y
                y += node.height + gap_y
            x += max_w + gap_x

    width = int(max((node.x + node.width for node in diagram.nodes.values()), default=0) + margin)
    height = int(max((node.y + node.height for node in diagram.nodes.values()), default=0) + margin)
    return width, height


def center(node: Node) -> tuple[float, float]:
    return node.x + node.width / 2, node.y + node.height / 2


def anchor(item: Node | Group, toward: tuple[float, float]) -> tuple[float, float]:
    cx = item.x + item.width / 2
    cy = item.y + item.height / 2
    dx = toward[0] - cx
    dy = toward[1] - cy
    if abs(dx) / max(item.width, 1) > abs(dy) / max(item.height, 1):
        x = item.x + (item.width if dx >= 0 else 0)
        y = cy
    else:
        x = cx
        y = item.y + (item.height if dy >= 0 else 0)
    return x, y


def svg_text(lines: list[str], x: float, y: float, css_class: str = "node-text") -> str:
    parts = [f'<text class="{css_class}" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">']
    offset = -(len(lines) - 1) * 9
    for idx, line in enumerate(lines):
        parts.append(f'<tspan x="{x:.1f}" dy="{offset if idx == 0 else 18}">{html.escape(line)}</tspan>')
        offset = 18
    parts.append("</text>")
    return "".join(parts)


def render_svg(diagram: Diagram, title: str) -> str:
    width, height = layout_nodes(diagram)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title>{html.escape(title)}</title>",
        "<desc>Generated SVG rendering of a Mermaid flowchart.</desc>",
        "<defs>",
        '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#475569"/></marker>',
        "</defs>",
        "<style>",
        ".canvas{fill:#ffffff}.group{fill:#f8fafc;stroke:#cbd5e1;stroke-width:1.4}.group-title{font:600 14px Arial,sans-serif;fill:#334155}.node{fill:#eef6ff;stroke:#2563eb;stroke-width:1.5}.diamond{fill:#fff7ed;stroke:#ea580c;stroke-width:1.5}.node-text{font:13px Arial,sans-serif;fill:#0f172a}.edge{fill:none;stroke:#475569;stroke-width:1.45}.edge-label{font:12px Arial,sans-serif;fill:#475569}.label-bg{fill:#ffffff;opacity:.92}",
        "</style>",
        f'<rect class="canvas" x="0" y="0" width="{width}" height="{height}"/>',
    ]

    for group in sorted(diagram.groups.values(), key=lambda item: item.order):
        parts.append(f'<rect class="group" x="{group.x:.1f}" y="{group.y:.1f}" width="{group.width:.1f}" height="{group.height:.1f}" rx="10"/>')
        parts.append(f'<text class="group-title" x="{group.x + 18:.1f}" y="{group.y + 28:.1f}">{html.escape(group.label)}</text>')

    lookup: dict[str, Node | Group] = {**diagram.nodes, **diagram.groups}
    for edge in diagram.edges:
        source = lookup.get(edge.source)
        target = lookup.get(edge.target)
        if source is None or target is None:
            continue
        source_center = (source.x + source.width / 2, source.y + source.height / 2)
        target_center = (target.x + target.width / 2, target.y + target.height / 2)
        start = anchor(source, target_center)
        end = anchor(target, source_center)
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        dash = ' stroke-dasharray="6 5"' if edge.dashed else ""
        if abs(start[0] - end[0]) > 30 and abs(start[1] - end[1]) > 30:
            path = f"M {start[0]:.1f} {start[1]:.1f} C {mid_x:.1f} {start[1]:.1f}, {mid_x:.1f} {end[1]:.1f}, {end[0]:.1f} {end[1]:.1f}"
        else:
            path = f"M {start[0]:.1f} {start[1]:.1f} L {end[0]:.1f} {end[1]:.1f}"
        parts.append(f'<path class="edge" d="{path}" marker-end="url(#arrow)"{dash}/>')
        if edge.label:
            label = html.escape(edge.label)
            label_width = max(44, len(edge.label) * 7 + 12)
            parts.append(f'<rect class="label-bg" x="{mid_x - label_width / 2:.1f}" y="{mid_y - 14:.1f}" width="{label_width:.1f}" height="20" rx="4"/>')
            parts.append(f'<text class="edge-label" x="{mid_x:.1f}" y="{mid_y:.1f}" text-anchor="middle">{label}</text>')

    for node in sorted(diagram.nodes.values(), key=lambda item: item.order):
        if node.shape == "diamond":
            cx, cy = center(node)
            points = [
                (cx, node.y),
                (node.x + node.width, cy),
                (cx, node.y + node.height),
                (node.x, cy),
            ]
            point_text = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
            parts.append(f'<polygon class="diamond" points="{point_text}"/>')
        else:
            parts.append(f'<rect class="node" x="{node.x:.1f}" y="{node.y:.1f}" width="{node.width}" height="{node.height}" rx="8"/>')
        cx, cy = center(node)
        parts.append(svg_text(node.lines, cx, cy + 5))

    parts.append("</svg>\n")
    return "\n".join(parts)


def nearest_heading(text: str, pos: int) -> str:
    headings = re.findall(r"^#{1,4}\s+(.+)$", text[:pos], flags=re.M)
    return headings[-1].strip() if headings else "Diagram"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:60] or "diagram"


def update_markdown(path: Path) -> int:
    text = path.read_text()
    pattern = re.compile(r"```mermaid\n(.*?)\n```", re.S)
    matches = list(pattern.finditer(text))
    if not matches:
        return 0

    rendered = []
    last = 0
    for index, match in enumerate(matches, 1):
        heading = nearest_heading(text, match.start())
        filename = f"{path.stem}_diagram_{index}_{slug(heading)}.svg"
        relative = f"images/{filename}"
        title = f"{path.stem} diagram {index}: {heading}"
        diagram = parse_diagram(match.group(1))
        (IMAGES / filename).write_text(render_svg(diagram, title))
        rendered.append(text[last:match.start()])
        rendered.append(f"![{heading}]({relative})")
        last = match.end()
    rendered.append(text[last:])
    path.write_text("".join(rendered))
    return len(matches)


def main() -> None:
    IMAGES.mkdir(exist_ok=True)
    total = 0
    for path in sorted(ROOT.glob("*.md")):
        total += update_markdown(path)
    print(f"Rendered {total} Mermaid diagram(s) into {IMAGES.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
