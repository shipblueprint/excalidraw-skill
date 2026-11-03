#!/usr/bin/env python3
"""Batch b8 scenes — web architecture (message queues, data processing, P2P,
federation, and mapping-service case studies). Meaning-driven, ekit style."""
from ekit import *


# ---------------------------------------------------------------- batch b8
def notification_message_queue():
    new()
    title("Notification System & Real-time Feed via Message Queue", 60, 40)
    subtitle("Posts are pushed, not polled: a distributed transaction updates the DB and sends the "
             "payload to a message queue, which pushes it to online connections and stores it for "
             "offline ones until they return.", 60, 96, width=960)

    # publisher
    person(120, 240, "Publisher", scale=1.0)

    # distributed transaction manager
    acc_box(280, 230, 210, 100, "Transaction\nManager", size=15)
    arrow(165, 280, 280, 280, color=INK)
    text("create post", 222, 262, size=11, color=MID, align="center", anchor="cb")

    # posts database
    database(290, 470, 180, 150, "Posts DB")
    arrow(355, 330, 355, 470, color=INK)
    text("persist post", 362, 400, size=11, color=MID, align="left", anchor="lm")

    # message queue (highlighted)
    queue(560, 245, 220, 85, "", fill=WHITE, stroke=ACC)
    text("Message Queue", 670, 288, size=13, align="center", anchor="cm", color=INK)
    arrow(490, 280, 560, 280, color=INK)
    text("send payload", 525, 262, size=11, color=MID, align="center", anchor="cb")

    # online connections
    dashed_group(900, 190, 430, 210, "Online Connections (persistent connection)")
    person(1000, 250, "Connection 1", scale=0.8)
    person(1200, 250, "Connection 2", scale=0.8)
    arrow(780, 275, 900, 275, color=ACC, w=3)
    text("push updates", 840, 255, size=11, color=ACC, align="center", anchor="cb")

    # offline branch: temporary storage
    box(560, 430, 220, 90, "Temporary Storage\n(TTL)", size=13)
    arrow(610, 330, 610, 430, color=INK, dash=True)
    text("store updates for offline users", 618, 380, size=11, color=MID,
         align="left", anchor="lm")
    person(1230, 460, "Offline Connection", scale=0.8)
    arrow(780, 475, 1170, 475, color=MID, dash=True)
    text("delivered when back online", 980, 455, size=11, color=MID,
         align="center", anchor="cb")

    # connection list key-value store
    box(290, 650, 220, 80, "Connection List\n(Key-Value Store)", size=12,
        fill=WHITE, stroke=ACC)
    arrow(400, 620, 400, 650, color=ACC, dash=True)
    text("avoids polling the DB", 470, 660, size=11, color=MID, align="left", anchor="lm")

    save("Notification system and real-time feed via message queue")


def data_ingestion():
    new()
    title("Data Ingestion", 60, 40)
    subtitle("Heterogeneous data streams in from many sources and is standardized in the collection "
             "layer, then routed through processing and analytics to visualization — storage and "
             "security run underneath.", 60, 96, width=960)

    # sources
    box(60, 210, 170, 70, "Social Media")
    box(60, 300, 170, 70, "Electronic Devices")
    box(60, 390, 170, 70, "Web Services / IoT")
    text("Data streams in", 60, 480, size=12, color=MID)

    # pipeline
    acc_box(320, 210, 200, 100, "Data Collection\n& Preparation", size=14)
    box(560, 210, 200, 100, "Data\nProcessing", size=14)
    box(800, 210, 200, 100, "Data\nAnalytics", size=14)
    box(1040, 210, 200, 100, "Data\nVisualization", size=14)

    arrow(230, 245, 320, 250, color=INK)
    arrow(230, 335, 320, 258, color=INK)
    arrow(230, 425, 320, 266, color=INK)
    arrow(520, 260, 560, 260, color=INK)
    arrow(760, 260, 800, 260, color=INK)
    arrow(1000, 260, 1040, 260, color=INK)

    # decision maker / consumer
    person(1330, 215, "Decision Maker", scale=0.9)
    arrow(1240, 260, 1280, 260, color=INK)

    # lower layers
    database(320, 480, 220, 150, "Data Storage\nLayer")
    firewall(700, 490, 220, 150, "Data Security\nLayer")
    arrow(420, 310, 420, 480, color=MID, dash=True)
    text("standardize & archive", 470, 470, size=11, color=MID, align="left", anchor="lm")
    text("security applies to every layer", 700, 460, size=11, color=MID)

    save("Data ingestion (2)")


def distributed_data_processing():
    new()
    title("Distributed Data Processing", 60, 40)
    subtitle("Large data is split into blocks and processed in parallel by the cluster's nodes, "
             "coordinated by a node coordinator (Apache Zookeeper) with shared state across the cluster.",
             60, 96, width=960)

    document(60, 300, 170, 140, "Streaming\nData In")

    acc_box(430, 165, 320, 90, "Node Coordinator\n(Apache Zookeeper)", size=15)

    dashed_group(260, 330, 960, 305, "Cluster")

    for x, name in [(300, "Node A"), (620, "Node B"), (940, "Node C")]:
        server(x, 370, 220, 150, name)
        box(x + 35, 540, 150, 45, "Shared Memory", size=11, fill=WHITE, stroke=BDR)

    # task allocation downwards
    for x in (410, 730, 1050):
        arrow(590, 255, x, 370, color=MID, dash=True, w=1.5)
    text("assigns tasks in parallel", 810, 305, size=11, color=MID, align="center")

    # data blocks flowing in
    for y in (400, 450, 500):
        arrow(230, y, 300, y, color=INK)
    text("blocks of data", 235, 540, size=11, color=MID)

    # consistent shared state
    line(485, 585, 805, 585, color=ACC, w=2)
    line(805, 585, 1125, 585, color=ACC, w=2)
    text("consistent state replicated across the cluster", 690, 600, size=11,
         color=ACC, align="center", anchor="ct")

    save("Distributed data processing")


def lambda_architecture():
    new()
    title("Lambda Data Processing Architecture", 60, 40)
    subtitle("Batch processing (accurate but slow) and real-time stream processing (fast but "
             "approximate) run in parallel; the serving layer merges both results before the user "
             "sees them.", 60, 96, width=980)

    document(60, 300, 150, 130, "Incoming\nData")

    # batch branch
    box(330, 190, 250, 100, "Batch Processing\nLayer", size=14)
    database(650, 180, 170, 130, "Batch Views")
    text("accurate & comprehensive insights", 330, 300, size=11, color=MID)

    # speed branch
    box(330, 430, 250, 100, "Speed Layer\nReal-time Stream Processing", size=13)
    database(650, 420, 170, 130, "Real-time Views")
    text("quick (approximate) insights", 330, 540, size=11, color=MID)

    # serving layer (highlighted)
    box(920, 300, 240, 130, "Serving Layer\n(merges batch + real-time)",
        size=14, fill=WHITE, stroke=ACC)

    person(1330, 320, "End User", scale=0.9)

    arrow(210, 340, 330, 265, color=INK)
    arrow(210, 400, 330, 465, color=INK)
    arrow(580, 240, 650, 240, color=INK)
    arrow(580, 480, 650, 480, color=INK)
    arrow(820, 245, 920, 330, color=INK)
    arrow(820, 485, 920, 400, color=INK)
    arrow(1160, 365, 1270, 365, color=INK)
    text("merge", 1100, 345, size=11, color=MID, align="center", anchor="cb")

    save("Lambda data processing architecture")


def kappa_architecture():
    new()
    title("Kappa Data Processing Architecture", 60, 40)
    subtitle("All data — batch and real-time — flows through one streaming pipeline, so there are "
             "only two layers to manage: Speed and Serving.", 60, 96, width=900)

    box(80, 300, 200, 130, "Batch + Real-time\nData", size=14)
    arrow(280, 365, 360, 365, color=INK)
    text("single pipeline", 320, 345, size=11, color=MID, align="center", anchor="cb")

    box(360, 285, 320, 160, "Speed Layer\nSingle Streaming Pipeline", size=15,
        fill=WHITE, stroke=ACC)
    arrow(680, 365, 760, 365, color=INK)
    box(760, 300, 240, 130, "Serving Layer", size=15)
    arrow(1000, 365, 1080, 365, color=INK)
    box(1080, 320, 200, 90, "Query / Output", size=14)

    text("Same pipeline handles batch and streaming — no separate batch layer "
         "(unlike Lambda).", 80, 500, size=12, color=MID)

    save("Kappa data processing architecture")


def web_hook():
    new()
    title("Web Hook", 60, 40)
    subtitle("Consumers register an HTTP endpoint with an API key once; the service then fires an "
             "HTTP event (callback) whenever new data is available — no polling and no middleware.",
             60, 96, width=960)

    acc_box(360, 280, 300, 130, "Baseball API Service\n(event source)", size=15)

    box(920, 170, 250, 100, "Service B\n(consumer)", size=14)
    box(920, 400, 250, 100, "Service C\n(consumer)", size=14)

    # registration (dashed, one-time)
    curved(920, 210, [[0, 0], [-140, -40], [-260, 60]], color=MID, dash=True)
    text("register HTTP endpoint\n+ API key", 810, 175, size=11, color=MID,
         align="center", anchor="ct")
    curved(920, 455, [[0, 0], [-140, 40], [-260, -60]], color=MID, dash=True)

    # event push (solid accent callbacks)
    arrow(660, 320, 920, 245, color=ACC, w=3)
    text("HTTP event\n(callback)", 800, 300, size=11, color=ACC, align="center", anchor="ct")
    arrow(660, 372, 920, 425, color=ACC, w=3)

    # polling is no longer needed
    box(80, 300, 210, 100, "Polling every now\nand then", size=13, dash=True)
    line(95, 315, 275, 385, color=ACC, w=3)
    line(275, 315, 95, 385, color=ACC, w=3)
    text("no longer needed", 185, 420, size=11, color=MID, align="center")

    text("Consumers of third-party services", 950, 545, size=12, color=MID)
    save("Web hook")


def peer_to_peer_1():
    new()
    title("Peer-to-Peer Architecture", 60, 40)
    subtitle("Nodes connect directly to each other with no central server. Every node acts as both a "
             "seeder (uploads data) and a leecher (downloads data).", 60, 96, width=940)

    nodes = {"A": (280, 330), "B": (700, 260), "C": (1140, 330),
             "D": (950, 580), "E": (430, 590)}
    w, h = 180, 100
    for a in nodes:
        for b in nodes:
            if a < b:
                xa, ya = nodes[a]
                xb, yb = nodes[b]
                line(xa, ya, xb, yb, color=BDR, w=2)
    for name, (cx, cy) in nodes.items():
        stroke = ACC if name in ("A", "E") else INK
        server(cx - w / 2, cy - h / 2, w, h, "Node " + name, stroke=stroke)

    text("No central server — every node is equal", 700, 175, size=13, color=ACC,
         align="center")
    text("Seeder → uploads data to the network", 90, 690, size=12, color=ACC)
    text("Leecher → downloads data from the network", 560, 690, size=12, color=ACC)
    save("Peer-to-peer architecture")


def decentralized_architecture():
    new()
    title("Decentralized Architecture", 60, 40)
    subtitle("In a peer-to-peer network nobody owns the data: all nodes have equal rights, so there "
             "is no single point of failure and no one can delete your data.", 60, 96, width=960)

    # centralized for contrast
    dashed_group(80, 200, 500, 380, "Centralized")
    hexagon(300, 250, 120, 90, "Central\nServer", size=12, fill=WHITE, stroke=ACC)
    for x, y in [(160, 250), (160, 440), (420, 250), (420, 440)]:
        line(360, 295, x + 45, y + 35, color=MID, w=2)
        ellipse(x, y, 90, 70, fill=WHITE, stroke=INK)
    text("single owner • single point of failure", 330, 600, size=12, color=MID,
         align="center")

    # decentralized
    dashed_group(680, 180, 780, 420, "Decentralized (P2P)")
    dec = [(780, 270), (980, 220), (1160, 320), (820, 480), (1040, 500), (1260, 420)]
    for i in range(len(dec)):
        for j in range(i + 1, len(dec)):
            (x1, y1), (x2, y2) = dec[i], dec[j]
            line(x1, y1, x2, y2, color=BDR, w=2)
    for x, y in dec:
        ellipse(x - 55, y - 40, 110, 80, fill=WHITE, stroke=INK)
    text("equal rights • resilient • no single owner", 1070, 620, size=12, color=MID,
         align="center")

    save("Decentralized architecture")


def peer_to_peer_2():
    new()
    title("Peer-to-Peer Architecture", 60, 40)
    subtitle("Nodes take equal turns as client and server. A large file is split into chunks and "
             "transferred over TCP/IP across a P2P overlay network in non-sequential order.",
             60, 96, width=980)

    acc_box(80, 240, 240, 120, "Peer A (Seeder)\nhosts 75 GB file", size=14)

    chunks = ["C1", "C2", "C3", "C4", "C5", "C6"]
    for i, c in enumerate(chunks):
        rect(90 + i * 38, 385, 34, 34, fill=WHITE, stroke=INK, rx=False)
        text(c, 107 + i * 38, 402, size=10, align="center", anchor="cm")
    text("file split into equal-size chunks", 80, 430, size=11, color=MID)

    dashed_group(420, 200, 980, 340, "P2P Overlay Network over TCP/IP")

    for lab, cx, cy in [("Peer B\n(client + server)", 720, 260),
                        ("Peer C\n(client + server)", 1080, 240),
                        ("Peer D\n(client + server)", 900, 430)]:
        server(cx - 90, cy - 45, 180, 90, lab, size=12)

    # chunk transfers / re-hosting
    arrow(320, 340, 630, 280, color=INK, w=2)
    text("download chunks", 470, 290, size=11, color=MID, align="center", anchor="cb")
    arrow_bidir(320, 360, 990, 255, color=INK)
    arrow_bidir(320, 380, 810, 430, color=INK)
    arrow(630, 320, 320, 360, color=ACC, dash=True, w=2)
    text("re-host (upload) while leeching", 480, 375, size=11, color=ACC,
         align="left", anchor="lt")

    # network types
    box(80, 590, 190, 70, "Structured", size=13)
    box(320, 590, 190, 70, "Unstructured", size=13)
    box(560, 590, 190, 70, "Hybrid", size=13)
    text("Types of P2P networks", 80, 560, size=12, color=MID)

    save("Peer to peer architecture")


def federated_architecture():
    new()
    title("Federated Architecture", 60, 40)
    subtitle("Decentralized social networks run on pods: nodes subscribe to a pod, pods federate "
             "with each other, and the network keeps working even if some pod links break.",
             60, 96, width=980)

    def add_nodes(px, py, positions):
        for nx, ny in positions:
            line(px, py, nx, ny, color=BDR, w=2)
        for nx, ny in positions:
            ellipse(nx - 42, ny - 28, 84, 56, fill=WHITE, stroke=INK)
            text("node", nx, ny, size=10, align="center", anchor="cm", color=MID)

    dashed_group(60, 170, 1380, 420, "Federated Network (a network of pods)")

    # federation links between pods
    line(345, 330, 705, 285, color=ACC, w=3)
    text("pods federate / share info", 525, 285, size=11, color=ACC, align="center", anchor="cb")
    line(795, 295, 1125, 365, color=MID, w=3, dash=True)
    line(945, 300, 975, 340, color=ACC, w=3)
    line(985, 300, 955, 340, color=ACC, w=3)
    text("link down — network stays up", 960, 380, size=11, color=ACC, align="center")

    # pods
    hexagon(180, 260, 180, 120, "Pod / Server 1", size=13, fill=WHITE, stroke=INK)
    hexagon(620, 210, 180, 120, "Pod / Server 2", size=13, fill=WHITE, stroke=INK)
    hexagon(1060, 300, 180, 120, "Pod / Server 3", size=13, fill=WHITE, stroke=INK)

    # nodes subscribed to each pod
    add_nodes(270, 320, [(140, 210), (120, 440), (280, 520)])
    add_nodes(710, 270, [(560, 160), (540, 420), (720, 500)])
    add_nodes(1150, 360, [(1010, 220), (1320, 280), (1090, 530)])

    text("nodes subscribe to pods • pods enable node discovery", 60, 610,
         size=12, color=MID)
    save("Federated architecture")


def mapping_service():
    new()
    title("Mapping Service", 60, 40)
    subtitle("Built from many microservices — one per feature — so even if a few feature APIs go "
             "down, the core location search stays available.", 60, 96, width=940)

    browser(60, 300, 170, 140, "User Interface\n(JS, HTML5)", size=13)
    arrow(230, 370, 320, 370, color=INK)
    acc_box(320, 320, 180, 100, "API Gateway", size=15)

    dashed_group(580, 175, 800, 385, "Microservices (one per feature)")
    services = [
        ("Location Search\n(core)", 620, 230, True),
        ("Direction API", 860, 230, False),
        ("Geocoding API", 1100, 230, False),
        ("Distance Matrix", 620, 360, False),
        ("Elevation API", 860, 360, False),
        ("Gaming API", 1100, 360, False),
    ]
    for lab, x, y, core in services:
        if core:
            box(x, y, 220, 90, lab, size=13, fill=WHITE, stroke=ACC)
        else:
            box(x, y, 220, 90, lab, size=13)
    arrow(500, 370, 620, 278, color=INK)
    text("route by feature", 560, 345, size=11, color=MID, align="center", anchor="cb")

    # backing stores / renderers
    database(620, 600, 200, 130, "Location & Place\nDatabase")
    cache(900, 600, 180, 110, "Map Tile Cache")
    box(1140, 600, 200, 110, "Map Server\n(renders tiles)", size=13)
    arrow(720, 450, 720, 600, color=MID, dash=True)
    arrow(1000, 450, 990, 600, color=MID, dash=True)
    arrow(1300, 450, 1240, 600, color=MID, dash=True)

    save("Mapping service")


def web_based_map_service():
    new()
    title("Web-based Map Service", 60, 40)
    subtitle("The UI requests tiles; the tile cache serves pre-rendered tiles, and on a miss the map "
             "server fetches coordinates from the database and generates the tile.", 60, 96,
             width=960)

    browser(60, 300, 200, 150, "User Interface\n(JS, HTML5, OpenLayers)", size=13)
    arrow(260, 360, 330, 360, color=INK)
    text("tile request", 295, 342, size=11, color=MID, align="center", anchor="cb")

    cache(330, 300, 220, 120, "Tile Cache\n(pre-generated tiles)")

    # tile returns to the UI (cache hit, or after a miss)
    arrow(330, 400, 260, 400, color=ACC, dash=True)
    text("tile", 295, 420, size=11, color=ACC)

    arrow(550, 360, 650, 360, color=INK)
    text("cache miss", 600, 342, size=11, color=MID, align="center", anchor="cb")

    box(650, 300, 220, 120, "Map Server\n(renders map tiles)", size=14,
        fill=WHITE, stroke=ACC)

    arrow(870, 340, 1000, 340, color=INK)
    text("fetch coordinates", 935, 322, size=11, color=MID, align="center", anchor="cb")
    database(1000, 290, 200, 150, "Location DB\n(coordinates)")
    arrow(1000, 400, 870, 400, color=MID, dash=True)
    text("coordinates", 935, 420, size=11, color=MID, align="center")

    # generated tile flows back map server -> cache
    arrow(650, 400, 550, 400, color=ACC, dash=True)
    text("generated tile", 600, 420, size=11, color=ACC, align="center")

    # real-time persistent connection
    curved(180, 455, [[0, 0], [80, 150], [640, 140]], color=MID, dash=True,
           start="arrow", head="arrow")
    text("persistent connection (real-time)", 480, 610, size=11, color=MID,
         align="center")

    save("Web-based map service")


if __name__ == "__main__":
    notification_message_queue()
    data_ingestion()
    distributed_data_processing()
    lambda_architecture()
    kappa_architecture()
    web_hook()
    peer_to_peer_1()
    decentralized_architecture()
    peer_to_peer_2()
    federated_architecture()
    mapping_service()
    web_based_map_service()
    print("wrote 12 batch-b8 scenes")
