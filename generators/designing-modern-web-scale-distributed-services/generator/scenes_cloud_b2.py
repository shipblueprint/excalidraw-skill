#!/usr/bin/env python3
"""Cloud Computing 101 — batch B2 scenes (meaning-driven, ekit).

Twelve diagrams: FaaS/BaaS evolution, cloud workloads, instance life cycle,
clusters, microservices, redundancy and replication.
"""
from ekit import *


# ---------------------------------------------------------------- FaaS / BaaS
def monolith_to_functions():
    new()
    title("Monolith to Microservices to Functions", 60, 40)
    subtitle("Architecture evolved from one monolith, to independently deployable microservices, "
             "to event-driven functions the cloud platform provisions and runs for us.",
             60, 96, width=1020)

    text("1 · Monolith", 200, 150, size=15, color=MID, anchor="ct", align="center")
    box(90, 180, 220, 340, "Monolith\n\nAll features in\none deployable\nunit")

    arrow(310, 350, 430, 350)
    text("split into\nmicroservices", 370, 300, size=12, color=MID, align="center", anchor="cb", width=150)

    text("2 · Microservices", 540, 150, size=15, color=MID, anchor="ct", align="center")
    box(430, 180, 220, 68, "Auth Service")
    box(430, 262, 220, 68, "Order Service")
    box(430, 344, 220, 68, "Catalog Service")
    box(430, 426, 220, 68, "Payment Service")

    arrow(650, 350, 880, 350)
    text("further split\ninto functions", 765, 300, size=12, color=MID, align="center", anchor="cb", width=170)

    text("3 · Functions", 1110, 140, size=15, color=MID, anchor="ct", align="center")
    dashed_group(880, 190, 460, 400, "FaaS — managed by the cloud platform")
    box(1010, 240, 200, 64, "Advertiser Fn", fill=WHITE, stroke=ACC)
    box(1010, 316, 200, 64, "Publisher Fn", fill=WHITE, stroke=ACC)
    box(1010, 392, 200, 64, "Login Fn", fill=WHITE, stroke=ACC)
    box(1010, 468, 200, 64, "Notify Fn", fill=WHITE, stroke=ACC)

    text("In FaaS the platform owns the servers — we supply only the function code, which runs "
         "only when an event fires.", 60, 620, size=13, color=MID, width=900)
    save("Monolith to Microservices to Functions")


def faas_architecture():
    new()
    title("Functions as a Service Architecture", 60, 40)
    subtitle("An API Gateway routes each request to the matching function; the function runs on "
             "demand and the cloud platform handles the backend services.", 60, 96, width=1000)

    person(170, 160, "User")
    browser(80, 290, 200, 150, "App Frontend")
    arrow(170, 255, 170, 290)

    acc_box(370, 300, 210, 110, "API Gateway\n(routing · auth · throttling)")
    arrow(280, 360, 370, 355)
    text("HTTPS request", 325, 330, size=11, color=MID, align="center", anchor="cb")

    dashed_group(650, 180, 520, 430, "FaaS — servers managed by the cloud platform")
    box(710, 250, 180, 90, "Advertiser\nFunction", fill=WHITE, stroke=ACC)
    box(920, 250, 180, 90, "Publisher\nFunction", fill=WHITE, stroke=ACC)
    database(710, 400, 170, 130, "Data\nPersistence")
    queue(920, 430, 180, 70, "Message Queue")

    arrow(580, 335, 710, 292)
    arrow(580, 375, 920, 292)
    text("route (event)", 640, 285, size=11, color=MID, align="center", anchor="cb")
    arrow(795, 340, 795, 400)
    arrow(1010, 340, 1010, 430)
    text("persist", 800, 372, size=11, color=MID)
    text("enqueue", 1015, 388, size=11, color=MID)

    text("When the event fires, the platform spins up a server, runs the function, and returns "
         "the response through the Gateway.", 60, 640, size=13, color=MID, width=920)
    save("Functions as a Service Architecture")


def mbaas():
    new()
    title("Mobile Backend as a Service", 60, 40)
    subtitle("MBaaS gives the app an API for every backend feature — authentication, database, "
             "notifications, storage, messaging and analytics — all managed for you.",
             60, 96, width=1040)

    person(200, 150, "User")
    mobile(110, 260, 180, 300, "Mobile App\n(Fat Client)\n\nAll business logic\nlives on the client")
    arrow(200, 232, 200, 260)

    dashed_group(420, 170, 780, 440, "MBaaS — managed backend (e.g., Firebase, AWS Amplify)")
    feats = [
        ("User\nAuthentication", 460, 250),
        ("Real-time\nDatabase", 690, 250),
        ("Push\nNotifications", 920, 250),
        ("Data Storage", 460, 400),
        ("Messaging\n& Chat", 690, 400),
        ("Analytics\n& Crash Reporting", 920, 400),
    ]
    for label, x, y in feats:
        box(x, y, 200, 100, label, size=13)

    arrow(290, 340, 460, 300)
    arrow(290, 430, 460, 450)
    text("API for every feature", 360, 320, size=11, color=MID, align="center", anchor="cb")

    text("MBaaS is ideal for mobile-only services: the client is a fat client and the platform "
         "exposes an API per feature.", 60, 650, size=13, color=MID, width=920)
    save("Mobile Backend as a Service")


def mbaas_and_custom_backend():
    new()
    title("MBaaS & A Custom Backend", 60, 40)
    subtitle("When the app must reach a legacy enterprise system or needs extra features, it "
             "talks to MBaaS and a custom backend side by side.", 60, 96, width=1000)

    person(190, 180, "User")
    mobile(100, 290, 180, 230, "Mobile App\n(Fat Client)")
    arrow(190, 262, 190, 290)

    dashed_group(390, 160, 760, 190, "MBaaS — managed backend")
    mfeats = [
        ("Authentication", 430, 200, 160, 60),
        ("Push Notifications", 610, 200, 160, 60),
        ("Real-time DB", 790, 200, 160, 60),
        ("Analytics", 970, 200, 160, 60),
    ]
    for label, x, y, w, h in mfeats:
        box(x, y, w, h, label, size=11)

    box(430, 470, 300, 130, "Custom Backend\n(legacy integration,\nadditional features)",
        fill=WHITE, stroke=ACC)
    database(830, 460, 220, 150, "Legacy Enterprise\nSystem")

    arrow(280, 350, 430, 235)
    text("API", 345, 300, size=11, color=MID, align="center", anchor="cb")
    arrow(280, 440, 430, 510)
    text("API", 345, 475, size=11, color=MID, align="center", anchor="cb")
    arrow(730, 535, 830, 535)
    text("cross-verify data", 780, 518, size=11, color=MID, align="center", anchor="cb")

    text("The app is a fat client; MBaaS provides managed features while the custom backend "
         "handles business logic and the legacy system.", 60, 650, size=13, color=MID, width=1000)
    save("MBaaS & A Custom Backend")


# ---------------------------------------------------------------- workloads
def cloud_workload():
    new()
    title("Cloud Workload", 60, 40)
    subtitle("A service deployed on the cloud is a workload — one monolith or hundreds of "
             "microservices — run by multiple cloud instances.", 60, 96, width=1000)

    acc_box(80, 250, 230, 120, "Workload\n(deployed service)")
    text("Portable: the same workload can move\nacross clouds or back on-prem.",
         80, 390, size=12, color=MID, width=280)

    arrow(310, 310, 450, 310)
    text("deploy", 380, 292, size=12, color=MID, align="center", anchor="cb")

    cloud(820, 300, 640, 320, "")
    server(600, 250, 140, 120, "Node A")
    server(780, 250, 140, 120, "Node B")
    server(960, 250, 140, 120, "Node C")
    text("Cloud instances running the workload", 820, 500, size=14, color=INK, align="center", anchor="ct")

    save("Cloud Workload")


def workload_google_cloud():
    new()
    title("Workload Deployed In Google Cloud", 60, 40)
    subtitle("Snapshot of a live service on Google Cloud: versions, status, traffic allocation, "
             "instances, runtime and size.", 60, 96, width=1000)

    rect(80, 160, 1340, 480, fill=WHITE, stroke=INK)
    line(80, 210, 1420, 210, color=INK)
    for i in range(3):
        ellipse(100 + i * 16, 178, 12, 12, stroke=INK)
    text("Google Cloud Platform  ·  App Engine  ·  Versions", 160, 176, size=15, color=INK)

    for i, b in enumerate(["REFRESH", "STOP", "START", "MIGRATE", "SPLIT TRAFFIC", "DIAGNOSE", "CONFIG"]):
        box(100 + i * 150, 230, 138, 40, b, size=11, fill=CON, stroke=BDR)

    rect(100, 290, 420, 36, fill=CON, stroke=BDR)
    text("Search resources and products", 116, 300, size=12, color=MID)
    text("Filter versions", 1240, 300, size=12, color=MID)

    rect(100, 350, 1300, 40, fill=CON, stroke=BDR)
    cols = [("Version", 120), ("Status", 320), ("Traffic Allocation", 470), ("Instances", 650),
            ("Runtime", 770), ("Environment", 880), ("Size", 1040), ("Deployed", 1130)]
    for name, x in cols:
        text(name, x, 362, size=12, color=INK)

    rect(100, 390, 1300, 60, fill=WHITE, stroke=BDR)
    text("2019020612-7", 120, 410, size=12)
    acc_box(320, 398, 120, 44, "Serving", size=12)
    text("100%", 470, 410, size=12)
    badge(700, 420, 2)
    text("java8", 770, 410, size=12)
    text("Standard", 880, 410, size=12)
    text("207MB", 1040, 410, size=12)
    text("6 Feb 20:12:56", 1130, 410, size=12)

    text("Every deployment creates a new version; traffic can be split between versions for A/B "
         "testing.", 80, 660, size=13, color=MID, width=1140)
    save("Workload Deployed In Google Cloud")


def instance_life_cycle():
    new()
    title("Instance Life Cycle", 60, 40)
    subtitle("From provisioning to termination, an instance passes through four stages — and a "
             "terminated instance can be spun up again.", 60, 96, width=1000)

    acc_box(120, 220, 240, 100, "Provisioned")
    box(600, 220, 240, 100, "Staged")
    box(600, 470, 240, 100, "Running")
    box(120, 470, 240, 100, "Terminated")

    arrow(360, 270, 600, 270)
    arrow(720, 320, 720, 470)
    arrow(600, 520, 360, 520)
    arrow(240, 470, 240, 320)

    text("allocated to a workload", 480, 250, size=11, color=MID, align="center", anchor="cb")
    text("resources assigned,\nprepped for launch", 730, 395, size=11, color=MID, anchor="lm")
    text("failure or manual stop", 480, 500, size=11, color=MID, align="center", anchor="cb")
    text("reset / restart", 250, 395, size=11, color=MID, anchor="lm")

    text("Not running yet; allocated\nbased on configuration.", 130, 335, size=11, color=MID)
    text("Cloud resources assigned\nto the instance.", 610, 335, size=11, color=MID)
    text("Hosts the workload and\nshares the cluster load.", 610, 585, size=11, color=MID)
    text("Down; can be reset,\nrestarted or deleted.", 130, 585, size=11, color=MID)

    dashed_group(870, 240, 460, 300, "Instance storage")
    text("Ephemeral: local disk, purged on terminate", 900, 290, size=12, color=MID)
    text("Persistent: spans the cluster and survives\ninstance swaps", 900, 360, size=12, color=MID, width=400)

    save("Instance Life Cycle")


# ---------------------------------------------------------------- clusters / HA
def server_cluster():
    new()
    title("Server Cluster", 60, 40)
    subtitle("A cluster is a group of servers working together for high availability, fault "
             "tolerance, scalability and parallel throughput.", 60, 96, width=1020)

    person(150, 300, "End User")
    acc_box(280, 290, 190, 100, "Load Balancer")
    arrow(185, 340, 280, 340)

    dashed_group(560, 170, 780, 380, "Cluster")
    server(600, 240, 160, 140, "Node 1")
    server(780, 240, 160, 140, "Node 2")
    server(960, 240, 160, 140, "Node 3")
    server(1140, 240, 160, 140, "Node 4")

    arrow(470, 340, 560, 340)
    text("distributes traffic", 515, 322, size=11, color=MID, align="center", anchor="cb")
    text("If a node fails, the remaining nodes keep serving the workload — the service stays up.",
         600, 420, size=12, color=MID, width=700)
    text("HA · Fault tolerant · Scalable · Parallel processing", 150, 520, size=13, color=MID, width=380)

    save("Server Cluster")


def microservice_architecture():
    new()
    title("Microservice Architecture", 60, 40)
    subtitle("A social network split into independent, separately deployable microservices — "
             "one failing feature does not bring down the rest (fail soft).", 60, 96, width=1040)

    person(165, 150, "User")
    browser(70, 270, 190, 140, "User Interface\n(Social Network)")
    arrow(165, 232, 165, 270)

    acc_box(290, 320, 150, 90, "API Gateway")
    arrow(260, 355, 290, 355)

    dashed_group(520, 150, 700, 540, "Microservices")
    svcs = [
        ("Authentication", 190, CON, BDR),
        ("Image Upload", 271, WHITE, ACC),
        ("Comment System", 352, CON, BDR),
        ("Instant Messaging", 433, CON, BDR),
        ("User Tagging", 514, CON, BDR),
        ("Live Streaming", 595, CON, BDR),
    ]
    for label, y, fill, stroke in svcs:
        box(580, y, 300, 70, label, fill=fill, stroke=stroke)

    for y in (225, 306, 387, 468, 549, 630):
        arrow(440, 365, 580, y, dash=True, color=MID, w=1)

    text("Each microservice is deployed and scaled independently.", 70, 470, size=12, color=MID, width=360)
    text("A bug in Image Upload does not affect the other services — fail soft.",
         520, 700, size=12, color=MID, width=700)
    save("Microservice Architecture")


def redundancy():
    new()
    title("Redundancy", 60, 40)
    subtitle("Active–passive HA: active instances serve live traffic while standby instances stay "
             "idle, ready to take over when an active node fails.", 60, 96, width=1060)

    box(90, 170, 240, 90, "Workload\n(Website)", fill=WHITE, stroke=ACC)
    arrow(210, 260, 210, 330)
    text("live traffic", 222, 295, size=11, color=MID, anchor="lm")

    dashed_group(80, 330, 520, 300, "Active Instance Fleet (serving)")
    server(120, 390, 140, 130, "Node A")
    server(290, 390, 140, 130, "Node B")
    server(460, 390, 140, 130, "Node C")
    text("Node C goes down →\nstandby takes over", 530, 535, size=11, color=ACC,
         align="center", anchor="ct", width=150)

    dashed_group(720, 330, 520, 300, "Passive Instances (standby, idle)")
    rect(760, 390, 140, 130, fill="transparent", stroke=BDR, dash=True)
    text("Node D\n(standby)", 830, 455, size=12, align="center", anchor="cm", color=MID)
    rect(930, 390, 140, 130, fill="transparent", stroke=BDR, dash=True)
    text("Node E\n(standby)", 1000, 455, size=12, align="center", anchor="cm", color=MID)

    arrow_bidir(600, 480, 720, 480, color=ACC)
    text("failover", 660, 462, size=12, color=ACC, align="center", anchor="cb")

    text("Active nodes are monitored; on failure a standby node takes over and the recovered node "
         "becomes passive.", 80, 670, size=13, color=MID, width=1120)
    save("Redundancy")


def replication():
    new()
    title("Replication", 60, 40)
    subtitle("Active–active HA: every node serves traffic and replicates data to stay in sync — "
             "no standby. If nodes fail, the rest share the load.", 60, 96, width=1060)

    box(80, 180, 240, 90, "Workload\n(Website)", fill=WHITE, stroke=ACC)
    arrow(200, 270, 200, 340)
    text("requests", 212, 305, size=11, color=MID, anchor="lm")

    dashed_group(80, 340, 1180, 300, "Active–Active Cluster (all nodes serving)")
    server(130, 400, 200, 150, "Node A")
    server(380, 400, 200, 150, "Node B")
    server(630, 400, 200, 150, "Node C")
    server(880, 400, 200, 150, "Node D")
    for x in (330, 580, 830):
        arrow_bidir(x, 475, x + 50, 475, color=ACC)
    text("replicate / stay in sync", 670, 392, size=11, color=ACC, align="center", anchor="cb")
    text("All nodes are active and share the load; each holds a replica and stays in sync.",
         670, 570, size=12, color=MID, align="center", anchor="ct", width=780)

    text("If a node goes down, the remaining nodes share its load and the service stays up.",
         80, 680, size=13, color=MID, width=1040)
    save("Replication")


def two_node_cluster():
    new()
    title("Two Node Cluster", 60, 40)
    subtitle("A load balancer spreads requests across two active nodes; heartbeats keep them aware "
             "of each other and session state is shared.", 60, 96, width=1060)

    person(150, 250, "End User")
    acc_box(280, 250, 190, 100, "Load Balancer")
    arrow(185, 300, 280, 300)
    text("request", 232, 282, size=11, color=MID, align="center", anchor="cb")

    dashed_group(560, 160, 780, 340, "Two-Node HA Cluster (Active–Active, replication)")
    server(620, 230, 200, 150, "Node A")
    server(900, 230, 200, 150, "Node B")
    arrow_bidir(820, 305, 900, 305, color=ACC)
    text("heartbeat (IP multicast)", 860, 285, size=11, color=ACC, align="center", anchor="cb", width=200)
    text("session US_1", 660, 400, size=12, color=ACC)

    arrow(470, 300, 560, 300)
    text("routes request", 515, 282, size=11, color=MID, align="center", anchor="cb")

    database(680, 540, 300, 150, "Persistent Session\nState Storage")
    arrow(720, 380, 760, 540, color=MID, dash=True)
    arrow(1000, 380, 940, 540, color=MID, dash=True)
    text("Persistent session state\nshared across the cluster", 1000, 545, size=12, color=MID, width=360)

    text("A missed heartbeat marks a node offline;\na leader handles consensus across the cluster.",
         60, 620, size=12, color=MID, width=520)
    save("Two Node Cluster")


if __name__ == "__main__":
    scenes = [
        monolith_to_functions,
        faas_architecture,
        mbaas,
        mbaas_and_custom_backend,
        cloud_workload,
        workload_google_cloud,
        instance_life_cycle,
        server_cluster,
        microservice_architecture,
        redundancy,
        replication,
        two_node_cluster,
    ]
    for fn in scenes:
        fn()
        print("wrote", fn.__name__)
    print("done:", len(scenes), "scenes")
