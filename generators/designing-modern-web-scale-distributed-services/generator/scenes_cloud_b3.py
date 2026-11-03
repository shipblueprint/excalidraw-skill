#!/usr/bin/env python3
"""Batch 3 (Cloud) — meaning-driven Excalidraw scenes.

Each function draws one course image and saves <basename>.excalidraw.
"""
from ekit import *


# ------------------------------------------------------------------ 1
def leader_node():
    new()
    title("Leader Node", 60, 40)
    subtitle("Every cluster elects one node as leader; it coordinates communication and drives "
             "consensus so all nodes share a consistent state.", 60, 96, width=820)

    person(110, 250, "User")
    arrow(150, 292, 216, 292)
    box(220, 248, 170, 88, "Load Balancer")

    dashed_group(430, 170, 700, 360, "Cluster (active-active)")
    arrow(390, 292, 470, 292)
    acc_box(470, 245, 190, 100, "Leader Node")
    text("coordination &\nconsensus", 565, 324, size=12, align="center", anchor="ct", color=MID)

    box(720, 225, 190, 90, "Follower Node 1")
    box(720, 350, 190, 90, "Follower Node 2")

    arrow_bidir(660, 275, 720, 270, color=ACC)
    arrow_bidir(660, 320, 720, 395, color=ACC)
    text("heartbeat", 692, 252, size=11, align="center", anchor="cb", color=ACC)

    text("A missed heartbeat marks a node offline — the leader keeps every node in consensus.",
         60, 565, size=13, color=MID)
    save("Leader Node")


# ------------------------------------------------------------------ 2
def sticky_sessions():
    new()
    title("Sticky Sessions", 60, 40)
    subtitle("The load balancer routes every request of a session to the same node that handled "
             "that session's first request.", 60, 96, width=860)

    person(100, 240, "User")
    arrow(140, 282, 206, 282)
    box(210, 238, 170, 88, "Load Balancer")

    dashed_group(440, 170, 560, 360, "Cluster")
    arrow(380, 268, 480, 262, color=ACC)
    text("Session A", 432, 250, size=12, align="center", anchor="cb", color=ACC)
    arrow(380, 298, 480, 400)
    text("Session B", 430, 366, size=12, align="center", anchor="cb", color=MID)

    box(480, 215, 190, 90, "Node A")
    box(480, 350, 190, 90, "Node B")

    database(790, 240, 170, 170, "Persistent\nSession Storage")
    arrow(670, 258, 790, 295, dash=True, color=MID)
    arrow(670, 395, 790, 375, dash=True, color=MID)
    text("session replication", 730, 440, size=11, align="center", anchor="ct", color=MID)

    text("All requests for Session A keep hitting Node A — required with asynchronous replication.",
         60, 565, size=13, color=MID)
    save("Sticky Sessions")


# ------------------------------------------------------------------ 3
def scalable_application():
    new()
    title("Scalable Application", 60, 40)
    subtitle("As concurrent users grow into the millions, the application scales horizontally so the "
             "response time stays the same.", 60, 96, width=880)

    dashed_group(60, 170, 600, 400, "Before — a single user")
    person(160, 250, "Single user")
    arrow(210, 295, 330, 295)
    text("Request", 270, 282, size=12, align="center", anchor="cb", color=MID)
    box(330, 250, 240, 95, "Application")
    arrow(330, 380, 210, 380)
    text("Response in X seconds", 270, 394, size=12, align="center", anchor="ct", color=MID)

    dashed_group(720, 170, 700, 400, "After — concurrent users (millions)")
    for i in range(5):
        person(790 + i * 46, 220, "", scale=0.6)
    text("Millions of concurrent users", 900, 300, size=13, align="center", anchor="ct", color=MID)
    arrow(1010, 300, 1080, 300)
    for i in range(4):
        box(1080 + i * 75, 255, 65, 80, "App")
    text("Application scales horizontally", 1210, 355, size=12, align="center", anchor="ct", color=MID)
    text("Response in X seconds — unchanged", 900, 480, size=13, align="center", anchor="cm", color=ACC)

    save("Scalable Application")


# ------------------------------------------------------------------ 4
def concurrent_updates():
    new()
    title("Concurrent Updates In A Distributed Application", 60, 40)
    subtitle("Two users update the same object in different regions at the same time; nodes hold "
             "conflicting values until the cluster reaches consensus.", 60, 96, width=940)

    dashed_group(150, 210, 560, 330, "Data Center — Japan")
    dashed_group(830, 210, 560, 330, "Data Center — America")

    person(80, 300, "User")
    arrow(112, 340, 150, 340)
    text("update X: 100 → 101", 150, 300, size=12, color=ACC)

    person(1440, 300, "User")
    arrow(1408, 340, 1370, 340)
    text("update X: 100 → 99", 1370, 300, size=12, align="right", anchor="rt", color=ACC)

    box(190, 275, 160, 85, "Node A")
    box(380, 275, 160, 85, "Node B")
    text("Object X = 101", 190, 372, size=13, color=ACC)
    text("Object X = 101", 380, 372, size=13, color=ACC)

    box(870, 275, 160, 85, "Node C")
    box(1060, 275, 160, 85, "Node D")
    text("Object X = 99", 870, 372, size=13, color=ACC)
    text("Object X = 99", 1060, 372, size=13, color=ACC)

    arrow_bidir(710, 420, 830, 420, dash=True, color=MID)
    text("replication across regions", 770, 440, size=11, align="center", anchor="ct", color=MID)

    acc_box(560, 590, 380, 80, "Consensus")
    text("all nodes agree on a single value for Object X", 750, 682, size=12,
         align="center", anchor="ct", color=MID)
    arrow(430, 540, 640, 590)
    arrow(1110, 540, 860, 590)

    text("Both regions start at Object X = 100; concurrent writes diverge them until consensus.",
         60, 700, size=12, color=MID)
    save("Concurrent Updates In A Distributed Application")


# ------------------------------------------------------------------ 5
def regions_azs_dcs():
    new()
    title("Regions, AZs & Data Centers", 60, 40)
    subtitle("A region is a geographic area holding multiple availability zones; each AZ is run by "
             "its own set of data centers. Regions stay physically isolated.", 60, 96, width=940)

    dashed_group(60, 180, 660, 400, "Ohio Region")
    for i in range(3):
        x = 80 + i * 200
        dashed_group(x, 230, 180, 330, "AZ " + str(i + 1))
        box(x + 20, 300, 140, 60, "Data Center")
        box(x + 20, 390, 140, 60, "Data Center")

    dashed_group(760, 180, 660, 400, "Tokyo Region")
    for i in range(4):
        x = 780 + i * 160
        dashed_group(x, 230, 150, 330, "AZ " + str(i + 1))
        box(x + 15, 300, 120, 60, "Data\nCenter")
        box(x + 15, 390, 120, 60, "Data\nCenter")

    acc_box(80, 605, 640, 70, "Local Zone (LZ) — extends a region near the end-user")
    text("Regions are isolated by power, water and hardware for fault tolerance.",
         760, 615, size=13, color=MID)
    save("Regions, AZs & Data Centers")


# ------------------------------------------------------------------ 6
def service_across_azs():
    new()
    title("Service Deployed On The Cloud Across Multiple AZs", 60, 40)
    subtitle("A regional load balancer spreads traffic across AZs; if a whole zone goes offline, its "
             "requests are routed to the surviving zones.", 60, 96, width=960)

    person(90, 200, "Users")
    arrow(140, 245, 560, 210)
    acc_box(560, 170, 380, 80, "Load Balancer (regional scope)")

    dashed_group(60, 300, 1360, 380, "Tokyo Region")
    for i in range(3):
        x = 90 + i * 450
        offline = (i == 2)
        dash = offline
        stroke = MID if offline else BDR
        dashed_group(x, 340, 400, 320, "AZ " + str(i + 1))
        box(x + 30, 390, 150, 70, "Service\nreplica", fill=CON, stroke=stroke, dash=dash,
            color=MID if offline else INK)
        box(x + 210, 390, 160, 70, "Data\nCenter", fill=CON, stroke=stroke, dash=dash,
            color=MID if offline else INK)
        box(x + 30, 500, 150, 60, "Data\nCenter", fill=CON, stroke=stroke, dash=dash,
            color=MID if offline else INK)
        box(x + 210, 500, 160, 60, "Data\nCenter", fill=CON, stroke=stroke, dash=dash,
            color=MID if offline else INK)

    arrow(700, 250, 290, 340)
    arrow(750, 250, 740, 340)
    arrow(800, 250, 1190, 340)
    text("AZ offline → traffic rerouted", 1190, 300, size=13, align="center", anchor="ct", color=ACC)

    text("Spanning AZs removes a single point of failure at the zonal level.",
         60, 705, size=13, color=MID)
    save("Service Deployed On The Cloud Across Multiple AZs")


# ------------------------------------------------------------------ 7
def multi_regional():
    new()
    title("Multi-Regional Cloud Deployment", 60, 40)
    subtitle("The same service is deployed in several regions; geo-aware routing sends each user to "
             "the nearest healthy region.", 60, 96, width=920)

    acc_box(560, 165, 380, 80, "Global Load Balancer (geo-aware routing)")

    person(125, 250, "Users worldwide")
    arrow(190, 285, 560, 205)

    for i, reg in enumerate(["Ohio Region", "Tokyo Region", "Europe Region"]):
        x = 70 + i * 490
        dashed_group(x, 320, 440, 330, reg)
        box(x + 30, 380, 170, 70, "Service")
        box(x + 230, 380, 170, 70, "Service")
        box(x + 30, 480, 170, 60, "Data Center")
        box(x + 230, 480, 170, 60, "Data Center")
        arrow(750, 245, x + 220, 320)

    arrow_bidir(510, 610, 560, 610, dash=True, color=MID)
    arrow_bidir(1000, 610, 1050, 610, dash=True, color=MID)
    text("inter-region replication", 780, 628, size=11, align="center", anchor="ct", color=MID)

    text("Nearest region → lowest latency, plus regional-level disaster safety.",
         60, 700, size=13, color=MID)
    save("Multi-Regional Cloud Deployment")


# ------------------------------------------------------------------ 8
def traditional_infra():
    new()
    title("Traditional Computing Infrastructure", 60, 40)
    subtitle("A monolithic application on bare-metal servers behind a load balancer in an in-house "
             "data center — everything provisioned by hand.", 60, 96, width=940)

    person(100, 260, "User")
    arrow(140, 300, 210, 300)
    box(210, 255, 180, 90, "Load Balancer")

    dashed_group(470, 180, 720, 380, "In-house / Rented Data Center")
    arrow(390, 300, 510, 300)
    for i in range(3):
        server(510 + i * 195, 245, 165, 120, "Bare-metal\nServer " + str(i + 1))

    database(700, 420, 220, 100, "Database")
    arrow(795, 365, 810, 420)
    text("Monolithic app", 800, 195, size=13, align="center", anchor="ct", color=ACC)

    text("• Manual resource provisioning\n• Hardware procurement & configuration\n"
         "• Scaling means replacing servers with bigger ones", 60, 585, size=13, color=MID)
    save("Traditional Computing Infrastructure")


# ------------------------------------------------------------------ 9
def cloud_infra():
    new()
    title("Cloud Computing Infrastructure", 60, 40)
    subtitle("Cloud services — compute, load balancing, messaging and database — are replicated "
             "horizontally across regions and zones.", 60, 96, width=940)

    cols = ["US-East\nZone 2", "US-West\nZone 3", "Europe\nZone 4"]
    rows = ["Compute Service", "Load Balancing Service", "Messaging Service", "Database Service"]
    cx = [300, 620, 940]
    for i, c in enumerate(cols):
        box(cx[i], 175, 260, 55, c, fill=WHITE, stroke=INK)

    for r, label in enumerate(rows):
        y = 260 + r * 100
        text(label, 250, y + 35, size=14, align="right", anchor="rm", color=INK)
        for i in range(3):
            fill = WHITE if (r == 0 and i == 0) else CON
            stroke = ACC if (r == 0 and i == 0) else BDR
            box(cx[i], y, 260, 70, "", fill=fill, stroke=stroke)
            text(label.split()[0], cx[i] + 130, y + 35, size=13, align="center",
                 anchor="cm", color=INK)

    text("Each service is deployed horizontally — it scales and fails independently of the others.",
         60, 680, size=13, color=MID)
    save("Cloud Computing Infrastructure")


# ------------------------------------------------------------------ 10
def commodity_hardware():
    new()
    title("Commodity Hardware", 60, 40)
    subtitle("Generic, open-standard servers from many vendors plug straight into the data center — "
             "interchangeable, cheap, no vendor lock-in.", 60, 96, width=920)

    box(60, 250, 180, 80, "Vendor A")
    box(60, 370, 180, 80, "Vendor B")
    text("same open standard", 150, 335, size=12, align="center", anchor="cm", color=MID)

    arrow(240, 285, 360, 300)
    arrow(240, 415, 360, 365)

    dashed_group(360, 180, 780, 400, "Cloud Data Center (powered by commodity hardware)")
    box(560, 205, 360, 60, "Workload")
    for i in range(4):
        box(400 + i * 180, 300, 150, 110, "Commodity\nServer")
        arrow(740, 265, 475 + i * 180, 300)
    text("Homogeneous, interchangeable servers built on open standards", 750, 445, size=13,
         align="center", anchor="cm", color=MID)

    text("• Buy off the shelf — no custom-manufacturing wait\n"
         "• Cheaper than custom hardware\n• Avoids hardware-specific vendor lock-in", 60, 610,
         size=13, color=MID)
    save("Commodity Hardware")


# ------------------------------------------------------------------ 11
def storage_google_dc():
    new()
    title("Storage In Warehouse-Scale Google Data Center", 60, 40)
    subtitle("Object storage is built on commodity servers: the API sits on Bigtable, which runs on "
             "the Google File System managing hard drives.", 60, 96, width=940)

    person(110, 200, "App")
    arrow(150, 240, 290, 220)
    acc_box(290, 185, 320, 80, "Object Storage API")

    arrow(450, 265, 450, 320)
    box(290, 320, 320, 80, "Google Bigtable")
    arrow(450, 400, 450, 455)
    box(290, 455, 320, 80, "Google File System (GFS)")

    box(700, 320, 260, 80, "MySQL (metadata)")
    arrow(610, 360, 700, 360, dash=True, color=MID)
    text("relationship\n& metadata", 680, 300, size=11, align="center", anchor="ct", color=MID)

    dashed_group(60, 565, 1080, 140, "Warehouse-Scale Google Data Center")
    for i in range(4):
        storage(90 + i * 260, 600, 150, 75, "Hard drives")
    arrow(450, 535, 450, 565)

    text("Read/write operations flow from the API down to the disk on commodity storage servers.",
         60, 720, size=12, color=MID)
    save("Storage In Warehouse-Scale Google Data Center")


# ------------------------------------------------------------------ 12
def edge_computing():
    new()
    title("Edge Computing", 60, 40)
    subtitle("Compute and cached content live at edge locations near users, so requests don't travel "
             "all the way to the origin data center.", 60, 96, width=920)

    person(120, 230, "End Users")
    text("IoT devices, phones, browsers", 165, 330, size=12, align="center", anchor="ct", color=MID)

    dashed_group(360, 180, 480, 400, "Edge Locations (global)")
    cache(400, 250, 180, 110, "CDN Cache\n(static content)")
    box(400, 400, 180, 90, "Edge Compute\n(FaaS, Lambda@Edge)")
    text("requests processed at the edge", 580, 560, size=12, align="center", anchor="ct", color=MID)

    dashed_group(920, 180, 500, 400, "Cloud Data Center (origin)")
    server(950, 250, 150, 110, "Origin\nServer")
    server(950, 400, 150, 110, "Origin\nServer")
    database(1160, 300, 210, 140, "Database")

    arrow(175, 270, 400, 300, color=ACC)
    text("low latency", 280, 262, size=12, align="center", anchor="cb", color=ACC)
    arrow(760, 330, 950, 300, dash=True, color=MID)
    text("cache miss / origin fetch", 850, 320, size=11, align="center", anchor="cb", color=MID)

    text("Edge nodes cut the load on the origin servers and improve user experience.",
         60, 620, size=13, color=MID)
    save("Edge Computing")


if __name__ == "__main__":
    leader_node()
    sticky_sessions()
    scalable_application()
    concurrent_updates()
    regions_azs_dcs()
    service_across_azs()
    multi_regional()
    traditional_infra()
    cloud_infra()
    commodity_hardware()
    storage_google_dc()
    edge_computing()
    print("wrote 12 batch-3 scenes")
