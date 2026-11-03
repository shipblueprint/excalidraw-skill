#!/usr/bin/env python3
"""Batch web-b5 scenes: layered/hexagonal architecture, inter-module + event-driven
communication, and micro frontends.  Meaning-driven diagrams drawn with ekit."""
from ekit import *


# ------------------------------------------------------------------ 1
def business_logic_layered():
    new()
    title("Business logic spread across the layered architecture", 60, 40)
    subtitle("In a layered architecture the domain rules leak into every layer — UI,\n"
             "controller, service, DAO and even the database (stored procedures) — so a\n"
             "single business change ripples through the whole stack.", 60, 96, width=820)

    layers = [
        ("Presentation / UI Layer", 180),
        ("Controller Layer", 254),
        ("Service Layer", 328),
        ("Data Access Layer (DAO)", 402),
    ]
    for name, y in layers:
        box(80, y, 340, 66, name, fill=CON, stroke=BDR)
        acc_box(262, y + 14, 146, 38, "business\nlogic", size=11)

    database(80, 500, 340, 130, "Database\n(stored procedures hold rules)")
    acc_box(262, 545, 146, 38, "business\nlogic", size=11)

    text("Lasagna code", 490, 190, size=18, color=INK)
    notes = [
        "• Domain logic is scattered, not in one place",
        "• UI and the database also carry rules",
        "• Layers are tightly coupled to their frameworks",
        "• Hard to test, refactor and extend",
        "• Adding a new entity touches many layers",
    ]
    for i, n in enumerate(notes):
        text(n, 490, 235 + i * 30, size=13, color=MID)

    text("Contrast: hexagonal architecture pulls all of this logic into one core.",
         490, 410, size=13, color=ACC, width=560)
    save("Business logic spread across the layered architecture")


# ------------------------------------------------------------------ 2
def hexagonal_use_case():
    new()
    title("Hexagonal architecture real-world use case", 60, 40)
    subtitle("A music subscription purchase from the mobile app flows through an inbound\n"
             "port/adapter into the isolated domain, then out through an outbound port/adapter\n"
             "to the database and messaging server.", 60, 96, width=820)

    person(62, 330, "User", scale=0.85)

    # application layer (outside)
    dashed_group(120, 175, 250, 400, "Application Layer")
    box(140, 225, 210, 85, "Mobile App / Web UI", size=13)
    box(140, 355, 210, 80, "REST Controller", size=13)
    arrow_down(245, 310, 45, "request")

    # domain core
    hexagon(430, 245, 340, 250, "Domain Layer\n\nBusiness Logic\n(Domain Model + Ports)",
            size=14, fill=WHITE, stroke=ACC)
    box(352, 342, 96, 56, "Inbound\nPort", size=11, fill=WHITE, stroke=INK)
    box(752, 342, 96, 56, "Outbound\nPort", size=11, fill=WHITE, stroke=INK)

    # infrastructure layer (outside)
    dashed_group(900, 175, 400, 420, "Infrastructure Layer")
    box(925, 225, 350, 80, "Outbound Adapter\n(implements the port)", size=13)
    database(925, 345, 155, 130, "Database")
    box(1115, 345, 160, 130, "Messaging\nServer", size=13)

    # flow
    arrow(245, 440, 352, 370, color=INK)
    arrow(448, 370, 430, 370, color=INK)
    arrow(770, 370, 925, 300, color=INK)
    arrow(1000, 305, 1000, 345, color=INK, dash=True)
    arrow(1080, 340, 1130, 340, color=INK, dash=True)
    text("persist purchase", 1015, 330, size=11, color=MID)
    text("send notification", 1120, 330, size=11, color=MID)

    text("Inbound ports/adapters take traffic from the app into the domain; outbound "
         "ports/adapters take traffic from the domain to infrastructure.",
         120, 600, size=12, color=MID, width=1150)
    save("Hexagonal architecture real-world use case")


# ------------------------------------------------------------------ 3
def inter_module_communication():
    new()
    title("Inter module communication", 60, 40)
    subtitle("Inside a modular monolith the modules talk asynchronously: they publish events\n"
             "into a shared in-memory event bus (or broker) and consume the events they\n"
             "care about — no direct module-to-module calls.", 60, 96, width=860)

    dashed_group(80, 160, 1200, 430, "Modular Monolith application")
    mods = ["Inventory", "Order", "Payment", "Membership"]
    for i, m in enumerate(mods):
        x = 110 + i * 290
        box(x, 220, 240, 170, "", fill="transparent", stroke=INK)
        text(m + " Module", x + 120, 245, size=15, align="center", anchor="cm")
        box(x + 20, 300, 200, 70, "Data Access Layer", size=12, fill=CON, stroke=BDR)

    acc_box(110, 470, 1080, 72, "Event Bus / Message Broker   (in-memory or external, e.g. Kafka)",
            size=14)
    for i in range(4):
        x = 110 + i * 290 + 120
        arrow_bidir(x, 392, x, 468, color=MID, dash=True)
    text("publish / consume events  (asynchronous)", 650, 560, size=13, color=MID,
         align="center", anchor="cm")
    save("Inter module communication")


# ------------------------------------------------------------------ 4
def inter_module_eventbus():
    new()
    title("Inter module communication via event bus/message queue", 60, 40)
    subtitle("Split into microservices: the modules that publish events are publishers, the\n"
             "ones that listen are consumers, and the broker in between is the event router.",
             60, 96, width=880)

    dashed_group(80, 175, 300, 380, "Publishers")
    box(110, 240, 240, 85, "Order Service", size=14)
    box(110, 355, 240, 85, "Payment Service", size=14)

    acc_box(470, 195, 320, 350, "Event Router\n\n(Message Broker / Queue)\n\nevents persisted")
    text("Kafka", 630, 505, size=12, color=MID, align="center", anchor="cm")

    dashed_group(980, 155, 400, 425, "Consumers")
    cons = ["Inventory Service", "Membership Service", "Notification Service"]
    for i, c in enumerate(cons):
        box(1010, 215 + i * 115, 340, 85, c, size=14)

    # publish (left -> router)
    arrow(350, 282, 470, 300, color=INK)
    arrow(350, 397, 470, 380, color=INK)
    text("publish", 405, 260, size=11, color=MID, align="center", anchor="cm")
    # consume (router -> right)
    arrow(790, 300, 980, 257, color=MID)
    arrow(790, 345, 980, 372, color=MID)
    arrow(790, 390, 980, 487, color=MID)
    text("consume", 895, 240, size=11, color=MID, align="center", anchor="cm")

    text("Events are persisted in the queue — a consumer that is down simply pulls them\n"
         "when it recovers, so scaling or failing a service does not affect the others.",
         80, 600, size=12, color=MID, width=1200)
    save("Inter module communication via event bus-message queue")


# ------------------------------------------------------------------ 5
def event_driven_architecture():
    new()
    title("Event-driven architecture", 60, 40)
    subtitle("At the system level the users are event producers and the microservices are\n"
             "event consumers; every event is routed through the event router (message\n"
             "broker), so services stay loosely coupled and process in parallel.", 60, 96,
             width=880)

    person(80, 300, "Customer", scale=0.9)
    browser(160, 235, 220, 150, "App / Web UI", size=13)
    arrow(105, 360, 160, 330)
    arrow_right(380, 310, 110, "events")
    acc_box(500, 230, 250, 230, "Event Router\n\n(Message Broker)")
    text("event producer", 270, 410, size=12, color=MID, align="center", anchor="cm")

    dashed_group(840, 150, 470, 420, "Event Consumers (microservices)")
    svc = [("Order Service", "Order Placed"),
           ("Payment Service", "Payment Made"),
           ("Inventory Service", "Stock Updated"),
           ("Membership Service", "Member Enrolled")]
    for i, (name, evt) in enumerate(svc):
        y = 190 + i * 90
        box(880, y, 300, 70, name, size=13)
        text(evt, 1200, y + 35, size=11, color=MID, anchor="lm")
        arrow(750, 320, 880, y + 35, color=MID, dash=True)

    text("Events are persisted and fanned out; if one service is down its events wait\n"
         "in the queue while the others keep running.", 500, 500, size=12, color=MID, width=320)
    save("Event-driven architecture")


# ------------------------------------------------------------------ 6
def online_game_store_monolith_frontend():
    new()
    title("Online game store with a monolith frontend", 60, 40)
    subtitle("Even with microservices on the backend, the whole user interface is one monolith\n"
             "built and owned by a dedicated frontend team.", 60, 96, width=820)

    person(80, 330, "End User", scale=0.85)
    dashed_group(155, 175, 335, 400, "Dedicated Frontend Dev Team")
    acc_box(175, 225, 295, 300,
            "Monolith\nFrontend\n\n(one codebase,\none UI team)")

    arrow(107, 360, 175, 360)
    arrow_right(490, 360, 65, "HTTPS")
    box(560, 315, 150, 90, "API\nGateway", size=14)

    dashed_group(800, 165, 660, 430, "Microservices Backend")
    micro = [("Product Service", 835, 215), ("Cart Service", 1145, 215),
             ("Payment Service", 835, 355), ("Order Service", 1145, 355)]
    for name, x, y in micro:
        box(x, y, 280, 80, name, size=13, fill=CON, stroke=BDR)
        database(x + 85, y + 95, 110, 80, "DB", size=11)
    arrow_right(710, 360, 90)
    save("Online game store with a monolith frontend")


# ------------------------------------------------------------------ 7
def full_stack_teams():
    new()
    title("Full stack teams with micro frontends", 60, 40)
    subtitle("The app is cut into vertical slices — each slice goes end to end from its UI\n"
             "component down to its database and is owned by one full-stack team.", 60, 96,
             width=840)

    text("Online Game Store UI (assembled from the team components)", 80, 148, size=13, color=MID)
    teams = [
        ("Team 1", "Product Search UI\n(React)", "Search Service", "Games DB"),
        ("Team 2", "Game Category UI\n(Vue)", "Catalog Service", "Catalog DB"),
        ("Team 3", "Cart & Checkout UI\n(Angular)", "Cart Service", "Cart DB"),
        ("Team 4", "Payment UI\n(plain JS)", "Payment Service", "Payments DB"),
    ]
    for i, (team, ui, svc, db) in enumerate(teams):
        x = 80 + i * 320
        dashed_group(x, 180, 300, 420, team)
        box(x + 20, 210, 260, 80, ui, size=13, fill=WHITE, stroke=ACC)
        arrow_down(x + 150, 290, 35)
        box(x + 20, 325, 260, 80, svc, size=13)
        arrow_down(x + 150, 405, 35)
        database(x + 45, 440, 210, 120, db)
        text("Frontend + Backend + DB devs", x + 150, 575, size=11, color=MID,
             align="center", anchor="cm")
    save("Full stack teams with micro frontends")


# ------------------------------------------------------------------ 8
def micro_frontends():
    new()
    title("Micro frontends", 60, 40)
    subtitle("A page is assembled from independently owned components: small fragments slot\n"
             "into other pages, while larger areas (checkout, payment) are full pages owned\n"
             "by their own team.", 60, 96, width=860)

    browser(80, 170, 560, 400, "")
    text("Home Page", 100, 200, size=13, color=MID)
    acc_box(100, 225, 520, 55, "Search Fragment  —  top of the home page", size=12)
    box(100, 305, 240, 240, "Game Category\nFragment", size=14)
    box(360, 305, 260, 110, "Cart Fragment", size=13)
    box(360, 440, 260, 105, "Upsell / Game\nRecommendations", size=12)

    box(690, 195, 320, 150, "Checkout Page\n(owned whole by one team)", size=14,
        fill=WHITE, stroke=ACC)
    box(690, 380, 320, 150, "Payment Page\n(owned whole by one team)", size=14,
        fill=WHITE, stroke=ACC)

    arrow(620, 370, 690, 280, color=MID)
    arrow_down(850, 345, 35, "navigate")
    text("Fragments integrate into other pages/components;", 690, 560, size=12, color=MID)
    text("larger areas are full pages.", 690, 582, size=12, color=MID)
    save("Micro frontends")


# ------------------------------------------------------------------ 9
def website_ui_micro_frontends():
    new()
    title("Website UI with micro frontends", 60, 40)
    subtitle("Because the components are loosely coupled, each one can be built with the right\n"
             "technology — and even on a different version of it — without rewriting the rest of\n"
             "the site.", 60, 96, width=860)

    browser(80, 170, 640, 405, "")
    text("Home Page", 100, 200, size=13, color=MID)
    acc_box(100, 225, 595, 60, "Product Search  —  built using React", size=13)
    box(100, 305, 285, 120, "City Building\nGames", size=14, fill=CON, stroke=BDR)
    box(410, 305, 285, 120, "First Person\nShooter Games", size=14, fill=CON, stroke=BDR)
    box(100, 450, 285, 105, "Cart  —  built using Angular", size=12)
    box(410, 450, 285, 105, "Deals  —  plain JS / HTML / CSS", size=12)

    text("Website UI built using micro frontends", 790, 220, size=16, color=INK)
    for i, t in enumerate([
        "• Each component picks its own tech stack",
        "• Teams can run different library versions",
        "• Upgrade one component without touching others",
        "• Use plain JS where a framework is overkill",
    ]):
        text(t, 790, 270 + i * 34, size=13, color=MID)
    save("Website UI with micro frontends")


# ------------------------------------------------------------------ 10
def client_side_integration():
    new()
    title("Client-side integration of micro frontends", 60, 40)
    subtitle("A basic (naive) client-side integration links the micro frontends directly. The two\n"
             "halves are hosted on different clouds, so the browser's address changes when the\n"
             "user navigates between them.", 60, 96, width=860)

    dashed_group(70, 165, 470, 380, "Micro Frontend — Checkout Page (hosted on AWS)")
    browser(90, 210, 430, 300, "")
    text("aws.amazon.com/onlinegamestore/checkout", 105, 240, size=11, color=MID)
    box(115, 280, 380, 100, "Checkout Page UI", size=14)
    acc_box(115, 410, 380, 55, "Link to the Payment Page", size=13)

    arrow(545, 435, 640, 435, color=ACC)
    text("click", 592, 415, size=11, color=ACC, align="center", anchor="cb")

    dashed_group(650, 165, 470, 380, "Micro Frontend — Payment Page (hosted on Google Cloud)")
    browser(670, 210, 430, 300, "")
    text("cloud.google.com/onlinegamestore/payment", 685, 240, size=11, color=MID)
    box(695, 280, 380, 100, "Payment Page UI", size=14)

    text("The visible URL changes  AWS  →  Google Cloud  as the user moves between pages.",
         70, 580, size=13, color=ACC, width=1000)
    text("Recommended instead: Web Components + a framework such as Single SPA.",
         70, 610, size=12, color=MID, width=900)
    save("Client-side integration of micro frontends")


# ------------------------------------------------------------------ 11
def iframe_integration():
    new()
    title("Integration of micro frontends with an Iframe", 60, 40)
    subtitle("A fragment can be embedded inside a host page with an iframe. It works, but it is\n"
             "the obsolete 90s approach — not bookmarkable, poor for SEO, and prone to stability\n"
             "and performance problems.", 60, 96, width=860)

    browser(80, 170, 650, 405, "")
    text("onlinegamestore.com/home", 100, 200, size=11, color=MID)

    rect(145, 250, 555, 295, fill="transparent", stroke=ACC, dash=True)
    text("iframe — Game Category Fragment", 165, 262, size=12, color=ACC)
    box(175, 335, 235, 175, "City Building\nGames", size=13, fill=CON, stroke=BDR)
    box(430, 335, 235, 175, "First Person\nShooter Games", size=13, fill=CON, stroke=BDR)

    text("Downsides of iframes", 790, 210, size=16, color=INK)
    for i, t in enumerate([
        "• Can't be bookmarked",
        "• Poor SEO",
        "• Stability & performance issues",
        "• Obsolete in modern web dev",
    ]):
        text(t, 790, 255 + i * 32, size=13, color=MID)
    text("Recommended: Web Components / Single SPA.", 790, 400, size=13, color=ACC)
    save("Integration of micro frontends with an Iframe")


# ------------------------------------------------------------------ 12
def web_application_architecture():
    new()
    title("Web application architecture", 60, 40)
    subtitle("A classic multi-server layout: the client talks to the backend server, which reads\n"
             "and writes through a cache, a database for persistence, and a messaging server for\n"
             "asynchronous work.", 60, 96, width=840)

    browser(80, 250, 220, 160, "Client / Browser", size=13)
    arrow_right(300, 330, 140, "HTTP")
    acc_box(440, 250, 220, 160, "Backend Server")

    cache(760, 150, 190, 100, "Cache Server")
    database(760, 305, 175, 150, "Database")
    queue(780, 505, 220, 72, "Messaging Server")

    arrow(660, 290, 760, 200, color=INK)
    arrow(660, 330, 760, 380, color=INK)
    arrow(660, 375, 780, 520, color=MID, dash=True)
    text("cache reads / writes", 700, 175, size=11, color=MID)
    text("persist data", 680, 415, size=11, color=MID)
    text("async messages / events", 700, 545, size=11, color=MID)

    save("Web application architecture (3)")


if __name__ == "__main__":
    business_logic_layered()
    hexagonal_use_case()
    inter_module_communication()
    inter_module_eventbus()
    event_driven_architecture()
    online_game_store_monolith_frontend()
    full_stack_teams()
    micro_frontends()
    website_ui_micro_frontends()
    client_side_integration()
    iframe_integration()
    web_application_architecture()
    print("wrote 12 scenes")
