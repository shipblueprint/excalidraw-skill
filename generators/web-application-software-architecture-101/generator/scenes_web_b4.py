#!/usr/bin/env python3
"""Meaning-driven Excalidraw scenes for the monolith / microservices chapter (batch web_b4)."""
from ekit import *


# ------------------------------------------------------------------ 1. DNS load balancing
def dns_load_balancing():
    new()
    title("DNS Load Balancing", 60, 40)
    subtitle("The authoritative nameserver hands clients the domain's IP addresses in "
             "round-robin order, spreading traffic across data centers.", 60, 96, width=880)

    person(130, 230, "Client 1", scale=0.85)
    person(130, 500, "Client 2", scale=0.85)

    acc_box(310, 280, 280, 120, "Authoritative\nNameserver")
    text("DNS load balancing\nhappens here", 450, 420, size=12, color=ACC,
         align="center", anchor="ct")

    arrow(190, 275, 310, 320, color=INK)
    text("DNS query\namazon.com", 248, 252, size=11, color=MID, align="center", anchor="cb")
    arrow(190, 545, 310, 385, color=INK)
    text("DNS query", 240, 470, size=11, color=MID, align="center", anchor="cb")

    # how round-robin works
    box(300, 460, 380, 210, "", fill=WHITE, stroke=BDR)
    text("Round-robin IP list", 322, 476, size=13, color=INK)
    text("Client 1 gets:\n  52.10.2.3 , 18.9.4.1 , 204.6.7.8\n\n"
         "Client 2 gets:\n  18.9.4.1 , 204.6.7.8 , 52.10.2.3\n\n"
         "Client hits the first IP and falls back\nto the next if it does not respond.",
         322, 504, size=11.5, color=MID)

    # data centers
    dashed_group(720, 160, 400, 230, "Data Center A")
    box(750, 195, 340, 55, "Load Balancer", size=13, fill=WHITE, stroke=ACC)
    server(760, 280, 150, 90, "App Server 1")
    server(940, 280, 150, 90, "App Server 2")

    dashed_group(720, 425, 400, 230, "Data Center B")
    box(750, 460, 340, 55, "Load Balancer", size=13, fill=WHITE, stroke=ACC)
    server(760, 545, 150, 90, "App Server 1")
    server(940, 545, 150, 90, "App Server 2")

    arrow(590, 320, 750, 245, color=ACC)
    text("IP address 1", 660, 258, size=11, color=ACC, align="center", anchor="cb")
    arrow(590, 360, 750, 500, color=MID)
    text("IP address 2", 660, 468, size=11, color=MID, align="center", anchor="cb")

    save("DNS load balancing")


# ------------------------------------------------------------------ 2. Monolithic architecture
def monolithic_architecture():
    new()
    title("Monolithic Architecture", 60, 40)
    subtitle("The whole application lives in a single codebase and ships as one deployable "
             "unit; every feature is tightly coupled to the rest.", 60, 96, width=900)

    person(120, 330, "User", scale=0.9)
    arrow(190, 375, 290, 375)
    text("HTTP", 240, 355, size=11, color=MID, align="center", anchor="cb")

    dashed_group(290, 170, 900, 420, "Single Codebase  ·  Single Deployment")
    feats = ["User Posts", "Comments", "Groups",
             "Marketplace", "Ads", "Photo Storage",
             "Live Streaming", "Recommendation", "Payments"]
    for i in range(3):
        for j in range(3):
            box(330 + j * 270, 210 + i * 115, 240, 80, feats[i * 3 + j],
                fill=WHITE, stroke=INK)

    # tight coupling between features
    arrow(570, 250, 600, 250, color=MID, dash=True)
    arrow(720, 290, 720, 325, color=MID, dash=True)
    arrow(720, 405, 720, 440, color=MID, dash=True)
    arrow(990, 290, 990, 325, color=MID, dash=True)
    text("tightly coupled — a change in one feature can break another", 330, 545,
         size=12, color=ACC)

    arrow(740, 590, 740, 650)
    text("SQL", 752, 618, size=11, color=MID)
    database(610, 650, 260, 100, "Single Database")

    save("Monolithic architecture")


# ------------------------------------------------------------------ 3. Microservice architecture
def microservice_architecture():
    new()
    title("Microservice Architecture", 60, 40)
    subtitle("Each feature runs as its own loosely coupled service with a single "
             "responsibility and (ideally) its own database.", 60, 96, width=940)

    person(120, 330, "User", scale=0.9)
    arrow(190, 375, 270, 375)
    text("HTTP", 228, 355, size=11, color=MID, align="center", anchor="cb")

    box(270, 330, 150, 90, "API Gateway", fill=WHITE, stroke=ACC)

    services = [("User\nService", 480), ("Post\nService", 720),
                ("Comment\nService", 960), ("Notification\nService", 1200)]
    for name, x in services:
        box(x, 180, 200, 90, name, fill=WHITE, stroke=INK)
        arrow(420, 375, x, 270)
        arrow(x + 100, 270, x + 100, 360)
        database(x + 30, 360, 140, 100, name.split("\n")[0] + "\nDB", size=12)
        dashed_group(x - 20, 155, 240, 330, "")

    text("Each service owns a single responsibility; scaling and failures are isolated.",
         480, 520, size=12, color=ACC)
    save("Microservice architecture (3)")


# ------------------------------------------------------------------ 4. Segment monolith architecture
def segment_monolith():
    new()
    title("Segment Monolith Architecture", 60, 40)
    subtitle("Every ingested event is forwarded to a single distributed message queue "
             "before reaching the destination APIs.", 60, 96, width=900)

    box(70, 300, 170, 110, "Event\nSources")
    arrow(240, 355, 340, 355)
    text("hundreds of\nthousands of\nevents / sec", 290, 305, size=11, color=MID,
         align="center", anchor="cb")

    acc_box(340, 300, 220, 110, "Segment API for\nIngesting Events")
    arrow(560, 355, 660, 355)
    text("forward", 610, 335, size=11, color=MID, align="center", anchor="cb")

    queue(660, 290, 200, 130, "Single Distributed\nMessage Queue")

    for i in range(4):
        y = 190 + i * 110
        box(1000, y, 210, 80, "Destination\nAPI " + str(i + 1), fill=WHITE, stroke=INK)
        arrow(860, 355, 1000, y + 40, color=INK)

    text("Failed events are retried by the same queue →\nit floods and delivery to every "
         "destination slows down.", 660, 470, size=12, color=ACC)
    save("Segment monolith architecture")


# ------------------------------------------------------------------ 5. Segment microservices architecture
def segment_microservices():
    new()
    title("Segment Microservices Architecture", 60, 40)
    subtitle("Split per destination: every destination gets its own service and its own "
             "message queue, isolating faults.", 60, 96, width=960)

    box(70, 320, 150, 110, "Event\nSources")
    arrow(220, 375, 310, 375)
    acc_box(310, 320, 180, 110, "Segment API\n(routing)")

    for i in range(4):
        y = 170 + i * 115
        dashed_group(550, y - 6, 520, 104, "")
        arrow(490, 375, 585, y + 40, color=INK)
        queue(585, y + 6, 150, 68, "Queue")
        box(805, y + 2, 215, 80, "Destination\nAPI " + str(i + 1), fill=WHITE, stroke=INK)

    text("One flooded queue no longer blocks the other destinations — fault isolation.",
         560, 660, size=12, color=ACC)
    save("Segment microservices architecture")


# ------------------------------------------------------------------ 6. The big ball of mud
def big_ball_of_mud():
    new()
    title("The Big Ball of Mud", 60, 40)
    subtitle("Spaghetti code: features with no layers, no interfaces and no structure, all "
             "tightly coupled together — versus clean lasagna code.", 60, 96, width=940)

    person(110, 330, "User", scale=0.85)

    # ---- tangled spaghetti side
    dashed_group(230, 170, 620, 420, "Spaghetti Code (no structure)")
    feats = [("Orders", 300, 215), ("Payment", 560, 205), ("Inventory", 660, 315),
             ("Routing", 420, 330), ("Membership", 300, 440), ("Notifications", 600, 460)]
    centers = []
    for name, x, y in feats:
        box(x, y, 160, 60, name, fill=WHITE, stroke=INK, size=13)
        centers.append((x + 80, y + 30))
    # criss-cross coupling
    criss = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (3, 4), (4, 5)]
    for a, b in criss:
        arrow(centers[a][0], centers[a][1], centers[b][0], centers[b][1],
              color=MID, dash=True, w=1)
    text("no layers · no interfaces · tightly coupled", 250, 555, size=12, color=ACC)

    # ---- clean lasagna side
    dashed_group(920, 170, 480, 420, "Layered (Lasagna) Code")
    for i, L in enumerate(["Controller Layer", "Service Layer", "Data Access Layer"]):
        box(960, 210 + i * 100, 400, 75, L, fill=WHITE if i == 1 else CON,
            stroke=ACC if i == 1 else BDR)
        if i < 2:
            arrow_bidir(1160, 285 + i * 100, 1160, 310 + i * 100, color=INK)
    database(1050, 510, 220, 90, "Database")
    arrow(1160, 485, 1160, 510, color=INK)
    text("clean separation · loosely coupled", 960, 630, size=12, color=MID)

    save("The big ball of mud")


# ------------------------------------------------------------------ 7. Layered architecture
def layered_architecture():
    new()
    title("Layered Architecture", 60, 40)
    subtitle("Also called lasagna code: controller, service and data access layers, each "
             "with a clear role, talking through interfaces.", 60, 96, width=960)

    person(120, 340, "User", scale=0.9)
    arrow(190, 385, 320, 385)
    text("request", 250, 365, size=11, color=MID, align="center", anchor="cb")

    layers = ["Controller Layer", "Service Layer", "Data Access Layer"]
    for i, name in enumerate(layers):
        hot = (i == 1)
        box(320, 210 + i * 100, 560, 80, name,
            fill=WHITE if hot else CON, stroke=ACC if hot else BDR)
    for i in range(2):
        arrow_bidir(600, 290 + i * 100, 600, 310 + i * 100, color=INK)

    text("Layers communicate\nonly through interfaces,\nkeeping them loosely\ncoupled and isolated.",
         910, 300, size=12.5, color=MID)

    database(700, 520, 240, 100, "Database")
    arrow_bidir(600, 490, 600, 520, color=INK)
    save("Layered architecture")


# ------------------------------------------------------------------ 8. Application layers
def application_layers():
    new()
    title("Application Layers", 60, 40)
    subtitle("Business features run as vertical slices across the layers — a request flows "
             "controller → service → DAO for its feature.", 60, 96, width=980)

    feats = ["Inventory", "Order Mgmt", "Payment"]
    x0, colw = 340, 300
    for j, f in enumerate(feats):
        acc_box(x0 + j * colw, 165, colw - 30, 60, f + " Feature")

    layers = ["Controller", "Service", "Data Access"]
    for i, L in enumerate(layers):
        text(L + " Layer", 60, 300 + i * 100, size=14, color=INK)
        for j in range(3):
            box(x0 + j * colw, 260 + i * 100, colw - 30, 70,
                feats[j] + " " + L, size=12.5, fill=CON, stroke=BDR)

    # vertical flow arrows per feature
    for j in range(3):
        cx = x0 + j * colw + (colw - 30) / 2
        arrow(cx, 225, cx, 260, color=INK)
        arrow(cx, 330, cx, 360, color=INK)
        arrow(cx, 430, cx, 460, color=INK)
        arrow(cx, 530, cx, 560, color=INK)

    database(560, 560, 260, 110, "Shared Database")
    text("A change to one feature stays inside its own vertical flow.", 340, 690,
         size=12, color=ACC)
    save("Application layers")


# ------------------------------------------------------------------ 9. Modular monolithic architecture
def modular_monolithic():
    new()
    title("Modular Monolithic Architecture", 60, 40)
    subtitle("One deployable monolith, split into loosely coupled modules by business "
             "feature — each module has its own layers and database.", 60, 96, width=980)

    dashed_group(180, 160, 1180, 470, "Modular Monolith  ·  single deployable unit")

    modules = ["Inventory", "Orders", "Payment", "Membership"]
    for j, m in enumerate(modules):
        x = 230 + j * 290
        box(x, 200, 250, 55, m + " Module", size=14, fill=WHITE, stroke=ACC)
        for i, L in enumerate(["Controller", "Service", "DAO"]):
            box(x + 20, 275 + i * 55, 210, 45, L, size=12, fill=CON, stroke=BDR)
        cx = x + 125
        arrow(cx, 255, cx, 275, color=INK)
        arrow(cx, 320, cx, 330, color=INK)
        arrow(cx, 375, cx, 385, color=INK)
        arrow(cx, 420, cx, 440, color=INK)
        database(x + 55, 440, 140, 90, m + "\nDB", size=11)

    text("Modules are logically separated (loosely coupled) but not independently "
         "deployable.", 230, 650, size=12, color=ACC)
    save("Modular monolithic architecture")


# ------------------------------------------------------------------ 10. Inter-module communication through interfaces
def intermodule_interfaces():
    new()
    title("Inter-Module Communication Through Interfaces", 60, 40)
    subtitle("Synchronous calls: a module talks to another only through its interface, "
             "with no knowledge of the implementation behind it.", 60, 96, width=1000)

    rect(180, 300, 250, 180, fill=CON, stroke=INK)
    text("Order Module", 305, 332, size=15, align="center", anchor="ct")
    text("business logic", 305, 410, size=12, color=MID, align="center", anchor="cm")

    hexagon(470, 350, 140, 90, "IInventory\nInterface", fill=WHITE, stroke=ACC, size=12)

    rect(650, 300, 280, 180, fill=CON, stroke=INK)
    text("Inventory Module", 790, 332, size=15, align="center", anchor="ct")
    rect(680, 360, 220, 90, fill=WHITE, stroke=BDR, dash=True)
    text("Implementation\n(hidden)", 790, 405, size=12, color=MID, align="center", anchor="cm")

    arrow(430, 390, 470, 395, color=INK)
    text("synchronous\ncall", 450, 360, size=11, color=MID, align="center", anchor="cb")
    arrow(610, 395, 650, 390, color=INK)

    text("The interface is the module's entry point — its implementation can be replaced "
         "without breaking callers.", 180, 530, size=12, color=ACC)
    save("Inter-module communication through interfaces")


# ------------------------------------------------------------------ 11. Inter-module communication through an event bus / message queue
def intermodule_eventbus():
    new()
    title("Inter-Module Communication Through an Event Bus / Message Queue", 60, 40)
    subtitle("Asynchronous, event-based (publish-subscribe): modules emit events to a central "
             "bus and subscribed modules react — no direct coupling.", 60, 96, width=1040)

    pubs = ["Order Module", "Inventory Module"]
    subs = ["Payment Module", "Membership Module"]
    for i, m in enumerate(pubs):
        box(220 + i * 500, 190, 300, 80, m, fill=WHITE, stroke=INK)
    for i, m in enumerate(subs):
        box(220 + i * 500, 560, 300, 80, m, fill=WHITE, stroke=INK)

    box(180, 385, 1080, 80, "Event Bus / Message Broker  (e.g. Kafka, Guava Event Bus)",
        fill=WHITE, stroke=ACC)

    for i in range(2):
        cx = 370 + i * 500
        arrow(cx, 270, cx, 385, color=INK)
        text("publish event", cx + 8, 320, size=11, color=MID, align="left", anchor="lm")
        arrow(cx, 465, cx, 560, color=INK)
        text("subscribe", cx + 8, 512, size=11, color=MID, align="left", anchor="lm")

    text("Publishers and subscribers never reference each other — the bus is their only "
         "point of contact.", 180, 680, size=12, color=ACC)
    save("Inter-module communication through an event bus or a message queue")


# ------------------------------------------------------------------ 12. Hexagonal architecture
def hexagonal_architecture():
    new()
    title("Hexagonal Architecture", 60, 40)
    subtitle("Ports and Adapters: the domain (business logic) sits at the core; every input "
             "and output passes through a port and its adapter.", 60, 96, width=1020)

    dashed_group(200, 200, 290, 440, "Inbound Adapters")
    dashed_group(1010, 200, 290, 440, "Outbound Adapters")

    box(230, 250, 230, 80, "Web UI /\nREST API Adapter", size=12.5, fill=WHITE, stroke=INK)
    box(230, 400, 230, 80, "Message Queue\nAdapter", size=12.5, fill=WHITE, stroke=INK)
    box(230, 550, 230, 80, "CLI / Test\nAdapter", size=12.5, fill=WHITE, stroke=INK)

    box(1040, 250, 230, 80, "Database\nAdapter", size=12.5, fill=WHITE, stroke=INK)
    box(1040, 400, 230, 80, "External API\nAdapter", size=12.5, fill=WHITE, stroke=INK)
    box(1040, 550, 230, 80, "Notifications\nAdapter", size=12.5, fill=WHITE, stroke=INK)

    hexagon(540, 300, 420, 320, "Domain\n(Business Logic)", fill=WHITE, stroke=ACC, size=16)

    # ports on the boundary
    ellipse(525, 445, 30, 30, fill=WHITE, stroke=ACC)
    ellipse(945, 445, 30, 30, fill=WHITE, stroke=ACC)
    text("Port", 505, 425, size=11, color=ACC, align="center", anchor="cb")
    text("Port", 970, 425, size=11, color=ACC, align="center", anchor="cb")

    # inbound (left) and outbound (right) adapters converge on the domain's ports
    arrow(460, 290, 545, 400, color=INK)
    arrow(460, 440, 543, 460, color=INK)
    arrow(460, 590, 545, 520, color=INK)
    arrow(955, 400, 1040, 290, color=INK)
    arrow(957, 460, 1040, 440, color=INK)
    arrow(955, 520, 1040, 590, color=INK)

    text("IO only happens at the edges; the domain never talks to external tools directly.",
         200, 670, size=12, color=ACC)
    save("Hexagonal architecture")


if __name__ == "__main__":
    dns_load_balancing()
    monolithic_architecture()
    microservice_architecture()
    segment_monolith()
    segment_microservices()
    big_ball_of_mud()
    layered_architecture()
    application_layers()
    modular_monolithic()
    intermodule_interfaces()
    intermodule_eventbus()
    hexagonal_architecture()
    print("wrote 12 scenes for web_b4")
