#!/usr/bin/env python3
"""Meaning-driven scenes for the "Introduction and types of data" /
database-model set (batch web_b6)."""
from ekit import *


# ------------------------------------------------------------------ helpers
def cell(x, y, w, h, label="", size=13, fill="transparent",
         stroke=BDR, color=INK, width=None):
    rect(x, y, w, h, fill=fill, stroke=stroke)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm",
             color=color, width=width if width else w - 8)


def table(x0, y0, col_ws, row_h, rows, size=13, head_fill=CON):
    """Simple grid: rows[0] is the header."""
    for r, row in enumerate(rows):
        x = x0
        for c, val in enumerate(row):
            w = col_ws[c]
            cell(x, y0 + r * row_h, w, row_h, val, size=size,
                 fill=head_fill if r == 0 else "transparent")
            x += w


def gnode(cx, cy, label, w=160, h=72, fill=WHITE, stroke=INK, color=INK, size=14):
    ellipse(cx - w / 2, cy - h / 2, w, h, fill=fill, stroke=stroke)
    text(label, cx, cy, size=size, align="center", anchor="cm", color=color, width=w - 14)


def edge(x1, y1, x2, y2, label="", color=INK, w=2, dash=False, size=12,
         lx=None, ly=None):
    line(x1, y1, x2, y2, color=color, w=w, dash=dash)
    if label:
        mx = (x1 + x2) / 2 if lx is None else lx
        my = (y1 + y2) / 2 if ly is None else ly
        text(label, mx, my, size=size, color=MID, align="center", anchor="cm")


def lock_icon(cx, cy, color=ACC, scale=1.0):
    r = 8 * scale
    ellipse(cx - r, cy - 16 * scale, 2 * r, 2 * r, stroke=color)
    rect(cx - 12 * scale, cy - 5 * scale, 24 * scale, 18 * scale,
         fill=WHITE, stroke=color)
    ellipse(cx - 2.5 * scale, cy + 1 * scale, 5 * scale, 5 * scale,
            fill=color, stroke=color)


# ------------------------------------------------------------------ 1
def web_application_architecture():
    new()
    title("Web Application Architecture", 60, 40)
    subtitle("A web application is a set of independent server-side components, "
             "each with a single clear responsibility.", 60, 96, width=900)

    person(120, 180, "User")
    browser(60, 300, 170, 130, "Web Browser\n(client)")
    arrow_right(230, 365, 100, "HTTP / HTTPS")

    box(340, 320, 190, 100, "Backend Server\n(application logic)",
        fill=WHITE, stroke=ACC)

    cache(650, 205, 180, 80, "Cache Server")
    queue(650, 360, 190, 80, "Messaging Server")
    database(670, 520, 170, 150, "Database\n(persistent data)")

    arrow(530, 345, 650, 245)
    arrow(530, 370, 650, 400)
    arrow(530, 395, 670, 555)

    text("reads / writes", 545, 250, size=11, color=MID)
    text("enqueue jobs", 545, 430, size=11, color=MID)
    text("no joins / low latency", 550, 610, size=11, color=MID)

    save("Web application architecture (3)")


# ------------------------------------------------------------------ 2
def data_ingestion():
    new()
    title("Data Ingestion", 60, 40)
    subtitle("Raw data streams in from many sources, is collected and prepared, then "
             "processed, analysed and visualised — resting in a data storage layer.",
             60, 96, width=1120)

    dashed_group(60, 210, 230, 300, "Data Sources")
    box(80, 250, 190, 55, "Social Media")
    box(80, 320, 190, 55, "Electronic Devices")
    box(80, 390, 190, 55, "Web Portals / Sensors")
    arrow_right(290, 360, 60, "streams in")

    dashed_group(360, 250, 1080, 330, "Data Security Layer")

    box(380, 290, 175, 95, "Data Collection\n& Preparation", fill=WHITE, stroke=ACC)
    arrow_right(555, 337, 40)
    box(600, 290, 140, 95, "Data\nProcessing")
    arrow_right(740, 337, 40)
    box(785, 290, 140, 95, "Data\nAnalytics")
    arrow_right(925, 337, 40)
    box(970, 290, 150, 95, "Data\nVisualization")
    arrow_right(1120, 337, 40)
    box(1165, 290, 150, 95, "Decision\nMaker")

    dashed_group(390, 440, 900, 110, "Data Storage Layer")
    box(410, 470, 180, 60, "Raw Data")
    box(610, 470, 180, 60, "Processed Data")
    box(810, 470, 200, 60, "Analytics Store")
    box(1030, 470, 240, 60, "Reports / Visuals")
    arrow_down(467, 385, 85, "store")

    save("Data ingestion")


# ------------------------------------------------------------------ 3
def polyglot_persistence():
    new()
    title("Polyglot Persistence", 60, 40)
    subtitle("One application, many databases — each store is chosen for a specific "
             "data need (the “social network / Facebook” example).", 60, 96, width=1050)

    box(560, 300, 300, 130, "Social Network\nApplication", fill=WHITE, stroke=ACC)

    box(180, 190, 250, 110, "Relational DB\nACID transactions,\nstrong consistency")
    box(960, 190, 250, 110, "Key-Value Store\ncaching,\nlow latency")
    box(100, 430, 250, 110, "Graph DB\nstoring relationships,\nrecommendations")
    box(960, 430, 260, 110, "Document Store\nwebsite search\n(Elasticsearch)")
    box(520, 580, 320, 100, "Wide-Column DB\nanalytics on big data\n(Cassandra / HBase)")

    arrow(710, 365, 305, 245)
    arrow(710, 365, 1085, 245)
    arrow(710, 365, 225, 485)
    arrow(710, 365, 1090, 485)
    arrow(710, 400, 680, 580)

    text("ACID", 500, 275, size=11, color=MID)
    text("cache", 900, 275, size=11, color=MID)
    text("relationships", 390, 445, size=11, color=MID)
    text("search", 920, 445, size=11, color=MID)
    text("analytics", 730, 525, size=11, color=MID)

    save("Polyglot persistence")


# ------------------------------------------------------------------ 4
def multi_model_database():
    new()
    title("Multi-model Database", 60, 40)
    subtitle("Instead of stitching many databases together, a single multi-model "
             "database serves several data models through one API.", 60, 96, width=1080)

    box(70, 330, 200, 120, "Social Network\nApplication")
    arrow_right(270, 390, 80, "single API")

    box(360, 300, 300, 160,
        "Multi-model Database\n(ArangoDB, CosmosDB,\nOrientDB, Couchbase)",
        fill=WHITE, stroke=ACC)

    dashed_group(740, 170, 240, 430, "Data models it supports")
    models = ["Relational", "Key-Value", "Document", "Graph", "Wide-Column"]
    for i, m in enumerate(models):
        box(760, 200 + i * 85, 200, 60, m)
        arrow(660, 380, 760, 230 + i * 85, color=MID)

    text("No need to manage multiple persistence technologies.",
         760, 620, size=12, color=MID)

    save("Multi-model database")


# ------------------------------------------------------------------ 5
def eventual_consistency():
    new()
    title("Eventual Consistency", 60, 40)
    subtitle("Across regions a write takes time to replicate. A reader may briefly see "
             "a stale value — eventually every node converges.", 60, 96, width=1050)

    dashed_group(60, 190, 470, 290, "Data Center — Japan")
    server(90, 250, 150, 120, "Node A\nlikes = 101")
    server(290, 250, 150, 120, "Node B\nlikes = 101")

    dashed_group(880, 190, 470, 290, "Data Center — America")
    server(910, 250, 150, 120, "Node C\nlikes = 100")
    server(1110, 250, 150, 120, "Node D\nlikes = 100")

    arrow_bidir(530, 315, 880, 315, color=MID, dash=True)
    text("Replication across geographic regions", 705, 300, size=12,
         color=MID, align="center", anchor="cb")

    person(170, 530, "User in Japan", scale=0.9)
    person(1210, 530, "User in America", scale=0.9)
    arrow(165, 522, 165, 482, color=ACC)
    text("likes:\n100 → 101", 190, 505, size=12, color=ACC)
    arrow(1205, 522, 1205, 482)
    text("sees old\nvalue 100", 1035, 505, size=12, color=MID)

    text("Temporarily inconsistent · converges to 101 everywhere in a few seconds",
         705, 660, size=13, color=MID, align="center", anchor="ct")

    save("Eventual consistency")


# ------------------------------------------------------------------ 6
def strong_consistency():
    new()
    title("Strong Consistency", 60, 40)
    subtitle("All nodes hold the same value at all times. While an update replicates the "
             "nodes are locked — only one writer acts at a time.", 60, 96, width=1080)

    dashed_group(60, 180, 470, 290, "Data Center — Japan")
    server(90, 240, 150, 120, "Node A\nlikes = 101")
    server(290, 240, 150, 120, "Node B\nlikes = 101")

    dashed_group(880, 180, 470, 290, "Data Center — America")
    server(910, 240, 150, 120, "Node C\nlikes = 101")
    server(1110, 240, 150, 120, "Node D\nlikes = 101")

    for cx in (222, 422, 1042, 1242):
        lock_icon(cx, 262, scale=0.9)

    arrow_bidir(530, 300, 880, 300, color=MID, dash=True)
    text("Replication across geographic regions", 705, 285, size=12,
         color=MID, align="center", anchor="cb")

    person(170, 540, "User A (writes)", scale=0.9)
    person(700, 560, "User B", scale=0.9)
    person(1240, 540, "User C (waits)", scale=0.9)
    arrow(165, 532, 165, 475, color=ACC)
    text("updates\n100 → 101", 190, 500, size=12, color=ACC)
    arrow(700, 545, 700, 470, color=MID, dash=True)
    text("access blocked until\nreplication completes", 835, 505, size=12, color=MID)

    text("Once all nodes reach consensus the locks are lifted and other users can write.",
         705, 670, size=13, color=MID, align="center", anchor="ct")

    save("Strong consistency")


# ------------------------------------------------------------------ 7
def graph_database():
    new()
    title("Graph Database", 60, 40)
    subtitle("Entities are nodes and relationships are edges stored in the database — "
             "so relationships are fetched, not computed with joins. e.g. Neo4J.",
             60, 96, width=1080)

    gnode(280, 300, "User A")
    gnode(620, 185, "User B")
    gnode(620, 470, "User C")
    gnode(1010, 320, "Boston")

    edge(349, 267, 551, 214, "follows")
    edge(620, 221, 620, 434, "follows", lx=650)
    edge(700, 470, 931, 356, "lives in")
    edge(700, 200, 940, 300, "works in")

    text("Vertex = entity (user, place)      Edge = relationship",
         120, 600, size=13, color=MID)
    text("Relationship traversal stays low-latency even as the graph grows.",
         120, 630, size=12, color=MID)

    save("Graph database")


# ------------------------------------------------------------------ 8
def nodes_in_a_graph():
    new()
    title("Nodes in a Graph", 60, 40)
    subtitle("Social connections represented as a graph: people are vertices, "
             "friendships and follows are edges.", 60, 96, width=1000)

    gnode(330, 300, "Meghan")
    gnode(650, 185, "Tom")
    gnode(650, 470, "Christie")
    gnode(970, 245, "Zach")
    gnode(990, 520, "Fred")
    gnode(120, 520, "Row")

    edge(400, 265, 570, 215, "friend")
    edge(400, 335, 570, 435, "friend")
    edge(730, 210, 890, 235, "follows")
    edge(730, 470, 910, 505, "follows")
    edge(250, 320, 195, 490, "follows")
    edge(1020, 280, 1000, 485, "friend")

    text("● Vertex — a user       ─ Edge — friendship / follows",
         120, 620, size=13, color=MID)

    save("Nodes in a graph")


# ------------------------------------------------------------------ 9
def nodes_in_a_graph_map():
    new()
    title("Nodes in a Graph", 60, 40)
    subtitle("Google Maps is one big graph: cities are nodes, roads are edges. "
             "Routing algorithms find the shortest path between two nodes.",
             60, 96, width=1080)

    gnode(210, 300, "San Francisco")
    gnode(520, 185, "Sacramento")
    gnode(520, 470, "Las Vegas")
    gnode(860, 310, "Phoenix")
    gnode(1180, 220, "Los Angeles")
    gnode(1180, 500, "San Diego")

    edge(290, 285, 440, 205, "90 mi")
    edge(520, 221, 520, 434, "430 mi", lx=555)
    edge(290, 315, 455, 445)
    edge(560, 500, 782, 350, "300 mi")
    edge(595, 440, 1105, 260, "270 mi", ly=360)
    edge(920, 340, 1115, 245, "370 mi")
    edge(1180, 256, 1180, 464, "120 mi", color=ACC, w=3)
    text("120 mi", 1205, 360, size=12, color=ACC)

    text("● Node — city       ─ Edge — road (distance in miles)",
         120, 630, size=13, color=MID)

    save("Nodes in a graph (2)")


# ------------------------------------------------------------------ 10
def row_oriented():
    new()
    title("Row-Oriented Data Storage", 60, 40)
    subtitle("Traditional relational databases (MySQL, PostgreSQL) keep a whole row "
             "together on disk — ideal for OLTP transactions.", 60, 96, width=1080)

    cols = [150, 160, 90, 150]
    table(80, 250, cols, 45, [
        ["Customer ID", "Name", "Age", "City"],
        ["1", "John", "55", "New York"],
        ["2", "Mary", "30", "Los Angeles"],
        ["3", "Alex", "42", "Chicago"],
    ])

    arrow(640, 365, 760, 365)
    text("each row stored\ncontiguously", 700, 335, size=11, color=MID,
         align="center", anchor="cb")

    rect(760, 250, 560, 280, fill="transparent", stroke=BDR, dash=True)
    text("On disk — one block per row", 770, 258, size=13, color=MID)
    rows_disk = [
        "Block 1 · 1, John, 55, New York",
        "Block 2 · 2, Mary, 30, Los Angeles",
        "Block 3 · 3, Alex, 42, Chicago",
    ]
    for i, r in enumerate(rows_disk):
        box(790, 300 + i * 70, 500, 55, r)

    text("Fetching or updating a customer touches a single block.", 80, 590, size=13, color=MID)

    save("Row-oriented data storage")


# ------------------------------------------------------------------ 11
def column_oriented():
    new()
    title("Column-Oriented Data Storage", 60, 40)
    subtitle("Columns are stored contiguously on disk, so an analytics query only scans "
             "the column it needs — ideal for OLAP. e.g. BigQuery, Redshift.",
             60, 96, width=1120)

    cols = [110, 100, 60, 110, 100, 120]
    table(60, 250, cols, 45, [
        ["Customer ID", "Name", "Age", "State", "Country", "City"],
        ["1", "John", "55", "California", "USA", "Los Angeles"],
        ["2", "Mary", "30", "Rajasthan", "India", "Jaipur"],
        ["3", "Alex", "42", "West Bengal", "India", "Darjeeling"],
    ])

    arrow(670, 365, 760, 365)
    text("columns stored\nseparately", 715, 335, size=11, color=MID,
         align="center", anchor="cb")

    rect(760, 250, 620, 300, fill="transparent", stroke=BDR, dash=True)
    text("On disk — one contiguous run per column", 770, 258, size=13, color=MID)
    col_blocks = [
        ("Customer ID column", False),
        ("Name column", False),
        ("Country column — only this is scanned", True),
        ("City column", False),
    ]
    for i, (lab, hot) in enumerate(col_blocks):
        if hot:
            box(790, 300 + i * 62, 560, 50, lab, fill=WHITE, stroke=ACC)
        else:
            box(790, 300 + i * 62, 560, 50, lab)

    text("Query “% of customers by country” skips the other columns entirely.", 60, 600, size=13, color=MID)

    save("Column-oriented data storage")


# ------------------------------------------------------------------ 12
def bigtable():
    new()
    title("Google Bigtable Data Model", 60, 40)
    subtitle("Rows are keyed by the reversed URL; columns carry timestamps and are grouped "
             "into column families (content, anchors). Newest version first.",
             60, 96, width=1150)

    x0 = 90
    rk = 330
    cw = 130
    y = 250
    hdr = 36
    dh = 64

    # column-family header row
    cell(x0, y, rk, hdr, "row key", fill=CON, size=14)
    cell(x0 + rk, y, cw * 3, hdr, "content", fill=CON, size=14)
    cell(x0 + rk + cw * 3, y, cw * 2, hdr, "anchors", fill=CON, size=14)

    # qualifier header row
    quals = ["content:t3", "content:t2", "content:t1", "anchor:wiki_t1", "anchor:sep_t1"]
    cell(x0, y + hdr, rk, hdr, "(reversed URL)", fill=CON, size=12, color=MID)
    for i, q in enumerate(quals):
        cell(x0 + rk + i * cw, y + hdr, cw, hdr, q, fill=CON, size=11)

    # data rows
    row1 = ["com.google.maps/\nindex.html", "<html>…\n(t3)", "<html>…\n(t2)",
            "<html>…\n(t1)", "wiki.com\n(t1)", "sep\n(t1)"]
    x = x0
    for i, v in enumerate(row1):
        w = rk if i == 0 else cw
        cell(x, y + 2 * hdr, w, dh, v, size=11,
             fill=WHITE if i == 2 else "transparent")
        x += w

    row2 = ["wiki.com", "<html>…\n(t1)", "", "", "… (t1)", "… (t1)"]
    x = x0
    for i, v in enumerate(row2):
        w = rk if i == 0 else cw
        cell(x, y + 2 * hdr + dh, w, dh, v, size=11)
        x += w

    text("Row key is the reversed URL, so pages of the same domain sit in contiguous rows.",
         90, 500, size=13, color=MID)
    text("Reads/writes under one row key are atomic · timestamps are 64-bit microseconds, newest first.",
         90, 528, size=13, color=MID)
    text("Column key syntax: column family : qualifier", 90, 556, size=13, color=ACC)

    save("Google Bigtable data model")


# ------------------------------------------------------------------ 13
def customer_column_family():
    new()
    title("Customer Data via Column-Family Model", 60, 40)
    subtitle("CustomerId is the row key; related columns are grouped into column families "
             "(CustomerInfo, Address), exactly as in Bigtable.", 60, 96, width=1120)

    x0 = 80
    rk = 200
    y = 280
    hdr = 38
    rh = 60

    # family header
    cell(x0, y, rk, hdr, "row key", fill=CON, size=14)
    cell(x0 + rk, y, 210, hdr, "CustomerInfo", fill=CON, size=14)
    cell(x0 + rk + 210, y, 390, hdr, "Address", fill=CON, size=14)

    # qualifier header
    quals = [("Name", 130), ("Age", 80), ("State", 130), ("Country", 120), ("City", 140)]
    cell(x0, y + hdr, rk, hdr, "CustomerId", fill=CON, size=13)
    x = x0 + rk
    for q, w in quals:
        cell(x, y + hdr, w, hdr, q, fill=CON, size=12)
        x += w

    data = [
        ["1", "John", "55", "California", "USA", "Los Angeles"],
        ["2", "Mary", "30", "Rajasthan", "India", "Jaipur"],
        ["3", "Alex", "42", "West Bengal", "India", "Darjeeling"],
    ]
    widths = [rk] + [w for _, w in quals]
    for r, row in enumerate(data):
        x = x0
        for i, v in enumerate(row):
            cell(x, y + 2 * hdr + r * rh, widths[i], rh, v, size=12)
            x += widths[i]

    text("Column families group related columns together; timestamps can be added per column.",
         80, 580, size=13, color=MID)

    save("Customer data stored via column-family data model")


# ------------------------------------------------------------------ run
if __name__ == "__main__":
    scenes = [
        web_application_architecture,
        data_ingestion,
        polyglot_persistence,
        multi_model_database,
        eventual_consistency,
        strong_consistency,
        graph_database,
        nodes_in_a_graph,
        nodes_in_a_graph_map,
        row_oriented,
        column_oriented,
        bigtable,
        customer_column_family,
    ]
    for fn in scenes:
        fn()
    print("wrote %d scenes" % len(scenes))
