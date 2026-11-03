#!/usr/bin/env python3
"""Batch b7 scenes: databases, caching, message queues, real-time feeds, streaming APIs."""
from ekit import *


# ----------------------------------------------------------------- HBase
def hbase():
    new()
    title("HBase Architecture", 60, 40)
    subtitle("Modelled after Google BigTable: a master-slave design. Zookeeper coordinates the "
             "cluster; the Master manages the Region Servers; clients ask Zookeeper which "
             "Region Server holds their data.", 60, 96, width=920)

    person(110, 380, "Client", scale=0.9)

    acc_box(280, 180, 200, 80, "Zookeeper\n(coordinator)")
    box(580, 170, 210, 80, "Master Node", fill=WHITE, stroke=INK)

    dashed_group(460, 340, 980, 310, "HBase Cluster")
    regions = ["Region A", "Region B", "Region C"]
    for i, reg in enumerate(regions):
        x = 490 + i * 310
        server(x, 410, 200, 180, "Region Server " + str(i + 1))
        rect(x + 22, 490, 156, 72, fill=WHITE, stroke=BDR)
        text(reg, x + 100, 526, size=13, align="center", anchor="cm")

    # client asks Zookeeper where the data lives
    arrow(165, 400, 280, 250)
    text("lookup region", 180, 300, size=11, color=MID)
    # zookeeper coordinates the master
    arrow(480, 210, 580, 210, color=MID, dash=True)
    text("coordinate", 485, 190, size=11, color=MID)
    # master keeps an eye on the region servers
    for i in range(3):
        arrow(685, 250, 590 + i * 310, 410, color=MID, dash=True)
    text("monitor", 700, 330, size=11, color=MID)
    # client reads / writes the region server it was pointed to
    arrow(165, 445, 490, 470, color=ACC)
    text("read / write", 250, 475, size=11, color=ACC)

    save("HBase architecture")


# ----------------------------------------------------------------- Cassandra
def cassandra():
    new()
    title("Cassandra Peer-to-Peer Node Architecture", 60, 40)
    subtitle("Every node is identical and runs the same code — there is no master. Nodes gossip "
             "to share state, replicate data across peers, and can be added or removed on the fly.",
             60, 96, width=960)

    dashed_group(200, 140, 1000, 500, "Cassandra Cluster")

    # four identical nodes in a ring
    box(600, 180, 190, 80, "Cassandra Node")
    box(970, 340, 190, 80, "Cassandra Node")
    box(600, 510, 190, 80, "Cassandra Node")
    box(240, 340, 190, 80, "Cassandra Node")

    # peer links (bidirectional): replication + gossip
    arrow_bidir(790, 225, 965, 355, color=INK)
    arrow_bidir(1040, 420, 790, 520, color=INK)
    arrow_bidir(600, 545, 435, 420, color=INK)
    arrow_bidir(335, 340, 600, 245, color=INK)

    text("All nodes run\nthe same code", 700, 380, size=14, align="center", anchor="cm")
    text("No single point of failure", 700, 425, size=12, color=MID, align="center", anchor="cm")
    text("replication · gossip", 700, 465, size=12, color=ACC, align="center", anchor="cm")

    person(80, 360, "Client", scale=0.8)
    arrow(145, 400, 240, 390)
    text("read / write\n(any node)", 90, 445, size=11, color=MID)

    text("Gossip shares node state · data is replicated to peers · writes are rerouted if a node is offline",
         210, 655, size=12, color=MID)
    save("Cassandra peer-to-peer node architecture")


# ----------------------------------------------------------------- Caching
def caching():
    new()
    title("Caching", 60, 40)
    subtitle("Frequently accessed data is copied from disk-based storage into RAM, so repeated "
             "reads are answered from memory — low latency, high throughput, less load on the "
             "database.", 60, 96, width=940)

    person(100, 330, "User", scale=0.9)
    browser(250, 300, 210, 150, "App Server")
    cache(560, 270, 200, 140, "Cache", fill=WHITE, stroke=ACC)
    database(900, 260, 180, 180, "Database")

    arrow(165, 390, 250, 390)
    text("request", 175, 368, size=11, color=MID)
    arrow(460, 350, 560, 320)
    text("1. read", 465, 322, size=11, color=MID)
    arrow(560, 410, 460, 435, color=ACC)
    text("2. hit (fast)", 430, 448, size=11, color=ACC)
    arrow(760, 350, 900, 330, color=MID, dash=True)
    text("miss → fill from DB", 762, 320, size=11, color=MID)

    text("data lives in RAM", 560, 445, size=11, color=MID, align="center", anchor="ct")
    text("disk-based, slower", 900, 460, size=11, color=MID, align="center", anchor="ct")
    text("The cache intercepts every request before it reaches the database.", 250, 510,
         size=13, color=MID)
    save("Caching")


# ----------------------------------------------------------------- Caching in web apps
def caching_web():
    new()
    title("Caching In Web Applications", 60, 40)
    subtitle("A cache can sit at every layer — in the browser, in the API/backend, and in front "
             "of the database. Whenever the same data is requested repeatedly, cache it.", 60, 96,
             width=980)

    person(80, 340, "User", scale=0.8)
    browser(200, 300, 190, 150, "Client Browser")
    box(470, 300, 230, 150, "Backend Server\n(REST API)", fill=CON, stroke=BDR)
    cache(780, 300, 190, 150, "Cache Server", fill=WHITE, stroke=ACC)
    database(1050, 290, 170, 170, "Database")

    arrow(150, 390, 200, 390)
    text("request", 152, 368, size=11, color=MID)
    arrow(390, 375, 470, 375)
    text("HTTP", 405, 353, size=11, color=MID)
    arrow(700, 375, 780, 375)
    text("lookup", 705, 353, size=11, color=MID)
    arrow(780, 425, 700, 425, color=ACC)
    text("hit", 728, 443, size=11, color=ACC)
    arrow(970, 375, 1050, 375, color=MID, dash=True)
    text("miss", 985, 353, size=11, color=MID)

    text("Browser cache\n(static assets)", 295, 465, size=11, color=MID, align="center", anchor="ct")
    text("API / session cache", 585, 465, size=11, color=MID, align="center", anchor="ct")
    text("key-value store\n(Redis / Memcached)", 875, 465, size=11, color=MID, align="center", anchor="ct")
    text("source of truth", 1135, 470, size=11, color=MID, align="center", anchor="ct")
    text("Caching can be applied at any layer, with any component.", 80, 560, size=13)
    save("Caching in web applications")


# ----------------------------------------------------------------- Polyhaven
def polyhaven():
    new()
    title("Polyhaven Architecture", 60, 40)
    subtitle("A static 3D-asset library. A lean dynamic backend serves the site, while the heavy "
             "assets are pulled from object storage through a CDN and cached at the edge — cutting "
             "traffic costs dramatically.", 60, 96, width=1000)

    person(80, 350, "End User", scale=0.85)

    # dynamic path (left -> right)
    box(230, 195, 250, 90, "polyhaven.com\n(Next.js · Vercel)", size=13)
    box(530, 195, 190, 90, "Backend API")
    cache(770, 185, 170, 110, "Cache\n(Memcache)")
    database(990, 180, 170, 130, "Database")
    arrow(165, 330, 230, 255)
    text("HTTPS", 168, 285, size=11, color=MID)
    arrow(480, 240, 530, 240)
    arrow(720, 240, 770, 240)
    arrow(940, 240, 990, 240)

    # static asset path (right -> left, back to the user)
    box(990, 470, 220, 100, "3D Asset Storage\n(Backblaze B2)", size=13)
    box(740, 470, 210, 100, "CDN\n(Bunny.net)", size=13)
    box(490, 470, 210, 100, "Cloudflare\nEdge Nodes", size=13)
    arrow(990, 520, 950, 520)
    text("origin", 952, 498, size=11, color=MID)
    arrow(740, 520, 700, 520)
    arrow(490, 510, 165, 445, color=ACC)
    text("3D assets\nserved from edge", 250, 470, size=11, color=ACC)

    text("Cost: ~$400/month for 5M page views & 80TB of traffic — thanks to edge caching.",
         60, 630, size=13)
    save("Polyhaven architecture")


# ----------------------------------------------------------------- Message queue
def message_queue():
    new()
    title("Message Queue", 60, 40)
    subtitle("A queue routes messages from a producer to a consumer in FIFO order and stores them "
             "temporarily, so the two sides work asynchronously.", 60, 96, width=900)

    box(90, 300, 190, 110, "Producer", fill=WHITE, stroke=ACC)
    arrow_right(280, 355, 60, "publish")
    queue(350, 300, 240, 110, "Message Queue")

    # ordered messages sitting in the queue
    for i, m in enumerate(["M1", "M2", "M3", "M4"]):
        text(m, 379 + i * 55, 355, size=11, align="center", anchor="cm", color=MID)
    text("FIFO order", 470, 275, size=12, color=ACC, align="center", anchor="cm")

    arrow_right(590, 355, 60, "consume")
    box(650, 300, 190, 110, "Consumer")

    text("The producer keeps working — it does not wait for the consumer.", 90, 455,
         size=12, color=MID)
    text("Messages are held until a consumer is ready to process them.", 90, 480,
         size=12, color=MID)
    text("Priority queues deliver by assigned priority instead of arrival order.", 90, 520,
         size=12, color=MID)
    save("Message queue")


# ----------------------------------------------------------------- Publish subscribe
def pubsub():
    new()
    title("Publish Subscribe Pattern", 60, 40)
    subtitle("A single producer broadcasts a message to many subscribers — a one-to-many "
             "relationship, like a newspaper delivered to every reader.", 60, 96, width=940)

    box(80, 320, 190, 100, "Producer", fill=WHITE, stroke=ACC)
    arrow(270, 370, 360, 370)
    text("publish", 282, 350, size=11, color=MID)
    acc_box(360, 320, 200, 100, "Topic / Broker")

    for i in range(3):
        y = 190 + i * 150
        box(720, y, 200, 90, "Subscriber " + str(i + 1))
        arrow(560, 370, 720, y + 45)
    text("broadcast", 600, 300, size=12, color=ACC)

    text("One producer → many subscribers (one-to-many).", 80, 610, size=13)
    text("Every subscriber receives its own copy of the message.", 80, 640, size=12, color=MID)
    save("Publish subscribe pattern")


# ----------------------------------------------------------------- Pub-sub with exchange
def pubsub_exchange():
    new()
    title("Publish Subscribe Pattern With An Exchange", 60, 40)
    subtitle("The producer publishes to an exchange; bindings route the message to queues, and "
             "each queue's consumer receives a copy. A fanout exchange broadcasts to every bound "
             "queue.", 60, 96, width=1000)

    box(60, 320, 170, 100, "Producer", fill=WHITE, stroke=ACC)
    arrow(230, 370, 330, 370)
    text("publish", 240, 350, size=11, color=MID)
    acc_box(330, 320, 190, 100, "Exchange\n(fanout)")

    for i in range(3):
        y = 190 + i * 150
        queue(620, y, 190, 80, "Queue " + str(i + 1))
        box(880, y, 190, 80, "Consumer " + str(i + 1))
        arrow(520, 370, 620, y + 40, color=MID, dash=True)
        arrow(810, y + 40, 880, y + 40)
    text("binding", 545, 300, size=12, color=ACC)

    text("Exchange types: direct · topic · headers · fanout", 60, 620, size=12, color=MID)
    text("A fanout exchange broadcasts to every bound queue.", 60, 648, size=12, color=MID)
    save("Publish subscribe pattern with an exchange")


# ----------------------------------------------------------------- Point to point
def point_to_point():
    new()
    title("Point To Point Model", 60, 40)
    subtitle("Each message is delivered to exactly one consumer — a one-to-one relationship. "
             "Multiple consumers can share a queue, but every message is consumed only once "
             "(no broadcast).", 60, 96, width=1000)

    box(70, 220, 170, 90, "Producer 1", fill=WHITE, stroke=ACC)
    box(70, 380, 170, 90, "Producer 2")
    queue(360, 290, 240, 110, "Message Queue")

    arrow(240, 265, 360, 320)
    arrow(240, 425, 360, 380)

    box(720, 170, 190, 90, "Consumer 1")
    box(720, 320, 190, 90, "Consumer 2")
    box(720, 470, 190, 90, "Consumer 3")

    arrow(600, 320, 720, 215, color=ACC)
    text("M1", 645, 250, size=12, color=ACC)
    arrow(600, 360, 720, 365, color=ACC)
    text("M2", 645, 345, size=12, color=ACC)
    arrow(600, 375, 720, 515, color=MID, dash=True)
    text("waits", 645, 455, size=11, color=MID)

    text("Each message is consumed by exactly one consumer.", 70, 630, size=13)
    text("This is entity-to-entity communication, not a broadcast.", 70, 660, size=12, color=MID)
    save("Point to point model")


# ----------------------------------------------------------------- Graph data structure
def graph_data_structure():
    new()
    title("Graph Data Structure", 60, 40)
    subtitle("A social graph: people are vertices (nodes) and relationships — FOLLOWS, LIVES_IN, "
             "WORKS_AT — are edges. It captures many-to-many relationships that a flat table "
             "cannot.", 60, 96, width=1000)

    ellipse(220, 255, 160, 90, fill=WHITE, stroke=ACC)
    text("User A", 300, 300, size=15, align="center", anchor="cm")
    ellipse(560, 160, 160, 90, fill=CON, stroke=INK)
    text("User B", 640, 205, size=15, align="center", anchor="cm")
    ellipse(900, 300, 160, 90, fill=CON, stroke=INK)
    text("User C", 980, 345, size=15, align="center", anchor="cm")

    box(190, 440, 170, 70, "Boston", size=13)
    box(880, 460, 190, 70, "Acme Corp", size=13)

    arrow(590, 250, 385, 290, color=ACC)
    text("FOLLOWS", 455, 250, size=12, color=ACC)
    arrow(940, 300, 705, 240, color=ACC)
    text("FOLLOWS", 795, 250, size=12, color=ACC)
    arrow(295, 345, 278, 440)
    text("LIVES_IN", 300, 390, size=11, color=MID)
    arrow(985, 390, 988, 460)
    text("WORKS_AT", 1000, 425, size=11, color=MID)

    text("vertex (node)", 640, 132, size=11, color=MID, align="center", anchor="cm")
    text("Many-to-many: a user has many friends and followers — a social graph.", 60, 640,
         size=13)
    save("Graph data structure")


# ----------------------------------------------------------------- Polling
def notification_polling():
    new()
    title("Notification System & Real-Time Feed Via Polling", 60, 40)
    subtitle("Pull-based: the client repeatedly polls the backend, which scans every connection "
             "for new posts. Simple, but expensive and only near-real-time.", 60, 96, width=1020)

    # User A creates a post
    person(80, 170, "User A", scale=0.8)
    box(200, 165, 190, 90, "New Post\ncreated")
    arrow(150, 205, 200, 205)
    text("post", 152, 185, size=11, color=MID)

    database(950, 300, 190, 180, "Database\n(User & Post tables)")
    arrow(390, 210, 950, 320)
    text("persist post", 640, 250, size=11, color=MID)

    # User B polls the backend
    person(80, 470, "User B\n(follower)", scale=0.8)
    box(230, 450, 210, 100, "Backend Server")
    arrow(150, 510, 230, 505)
    text("poll", 152, 490, size=11, color=MID)
    curved(300, 448, [[0, 0], [40, -50], [120, -25]], color=ACC)
    text("every few seconds", 195, 430, size=11, color=ACC)
    text("User B follows User A", 60, 385, size=12, color=MID)

    arrow(440, 500, 950, 400)
    text("query all connections &\ncheck for new posts", 560, 445, size=11, color=MID)
    arrow(950, 440, 440, 540, color=MID, dash=True)
    text("updates + notify", 590, 545, size=11, color=MID)

    text("Downsides: frequent polling consumes bandwidth and loads the database; updates are "
         "not truly real-time.", 60, 640, size=13, color=ACC)
    save("Notification system and real-time feed via polling")


# ----------------------------------------------------------------- Streaming API
def streaming_api():
    new()
    title("Streaming API", 60, 40)
    subtitle("REST opens a fresh connection per request; a Streaming API keeps one persistent "
             "connection open so the server can push events to the client as they happen — a "
             "continuous conversation.", 60, 96, width=1020)

    # REST panel
    dashed_group(60, 180, 620, 380, "REST API — request / response")
    browser(110, 270, 180, 140, "Client")
    server(400, 270, 200, 140, "Server")
    arrow(290, 320, 400, 320)
    text("request", 300, 300, size=11, color=MID)
    arrow(400, 360, 290, 360)
    text("response", 300, 378, size=11, color=MID)
    text("Connection closes after each reply", 110, 450, size=12, color=MID)

    # Streaming panel
    dashed_group(740, 180, 620, 380, "Streaming API — persistent connection")
    browser(790, 270, 180, 140, "Client")
    server(1080, 270, 200, 140, "Server")
    line(970, 315, 1080, 315, color=ACC, w=3)
    line(970, 345, 1080, 345, color=ACC, w=3)
    text("persistent connection", 1025, 288, size=12, color=ACC, align="center", anchor="ct")
    arrow(1080, 375, 970, 375, color=ACC)
    text("events pushed", 985, 393, size=11, color=ACC)
    text("Connection stays open; the server pushes events", 790, 450, size=12, color=MID)

    text("A streaming API is like an ongoing conversation between the client and the server.",
         60, 610, size=13)
    save("Streaming API (2)")


if __name__ == "__main__":
    hbase()
    cassandra()
    caching()
    caching_web()
    polyhaven()
    message_queue()
    pubsub()
    pubsub_exchange()
    point_to_point()
    graph_data_structure()
    notification_polling()
    streaming_api()
    print("wrote 12 scenes for batch b7")
