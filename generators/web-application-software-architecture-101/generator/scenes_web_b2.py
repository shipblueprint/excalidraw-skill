#!/usr/bin/env python3
"""Web-architecture batch B2 scenes: APIs, HTTP push/pull, scalability.

One function per source image; each ends with save("<basename>").
"""
from ekit import *


def code_card(x, y, w, h, heading, body, size=12):
    """White card with a heading and monospace-ish body text."""
    rect(x, y, w, h, fill=WHITE, stroke=INK, rx=True)
    text(heading, x + 14, y + 12, size=14, color=INK)
    text(body, x + 14, y + 44, size=size, color=INK)


# --------------------------------------------------------------------- APIs
def feature_apis():
    new()
    title("Feature APIs", 60, 40)
    subtitle("One API per product feature, each powered by a dedicated microservice; "
             "clients and services all talk through APIs.", 60, 96, width=880)

    browser(60, 235, 190, 155, "Client\n(browser / mobile)")

    apis = [("Product Search API", 170), ("Payments API", 275),
            ("Offers & Deals API", 380), ("User Feedback API", 485)]
    services = ["Product Search\nService", "Payments\nService",
                "Offers\nService", "Feedback\nService"]
    for (lbl, y), svc in zip(apis, services):
        box(330, y, 210, 62, lbl, fill=WHITE, stroke=ACC)
        arrow(250, 312, 330, y + 31)
        box(650, y, 210, 62, svc, fill=CON, stroke=INK)
        arrow(540, y + 31, 650, y + 31)

    dashed_group(628, 130, 400, 440, "Each API backed by a dedicated microservice")

    database(930, 165, 150, 115, "Inventory\nDB")
    arrow(860, 200, 930, 210)

    curved(858, 201, [[0, 0], [55, 60], [55, 140]], color=MID, head="arrow", start="arrow")
    text("microservices also call one another via APIs", 640, 600, size=12, color=MID)
    save("Feature APIs")


def public_api():
    new()
    title("Public API", 60, 40)
    subtitle("A business exposes its core service through public APIs so third-party developers "
             "can extend it with new plugins and features.", 60, 96, width=900)

    box(60, 300, 210, 130, "Core Service\n(business logic)", fill=WHITE, stroke=INK)
    acc_box(330, 320, 180, 90, "Public API")
    arrow(270, 365, 330, 365, color=MID)

    person(600, 285, "Third-party\ndevelopers")
    arrow(510, 360, 570, 345, color=MID)

    box(690, 315, 210, 100, "Plugins & Features\n(built by developers)", fill=CON, stroke=INK)
    arrow(660, 365, 690, 365, color=MID)

    box(960, 315, 190, 100, "Marketplace", fill=WHITE, stroke=ACC)
    arrow(900, 365, 960, 365, color=MID)

    box(1210, 315, 200, 100, "Clients\n(use new features)")
    arrow(1150, 365, 1210, 365, color=MID)

    curved(795, 300, [[0, 0], [-90, -80], [-420, -65]], color=ACC, dash=True, head="arrow")
    text("plugged back into the core service", 540, 205, size=12, color=ACC)

    dashed_group(670, 285, 490, 165, "Ecosystem enabled by the public API")
    save("Public API")


# --------------------------------------------------------------------- REST
def rest_api_architecture_2():
    new()
    title("REST API architecture", 60, 40)
    subtitle("Clients talk to stateless REST endpoints over HTTP; every request re-sends auth "
             "info and responses can be cached.", 60, 96, width=900)

    browser(60, 170, 190, 120, "Browser")
    mobile(60, 320, 190, 120, "Mobile App")
    box(60, 470, 190, 80, "Desktop")

    acc_box(350, 280, 220, 150, "REST API")

    box(720, 285, 210, 140, "Backend\nServer", fill=WHITE, stroke=INK)
    database(980, 300, 145, 120, "Database")

    arrow_bidir(250, 230, 350, 320)
    arrow_bidir(250, 380, 350, 360)
    arrow_bidir(250, 510, 350, 400)
    text("HTTP Request\n(GET / POST / PUT / DELETE)", 300, 185, size=12, color=MID, align="center")
    arrow_bidir(570, 355, 720, 355)
    arrow_bidir(930, 355, 980, 360)

    text("Response: JSON, cacheable", 300, 620, size=12, color=ACC)
    text("Stateless: each request re-sends authentication", 350, 470, size=12, color=MID)
    text("Endpoint:  https://myservice.com/users/{username}", 350, 500, size=12, color=MID)
    save("REST API architecture (2)")


def rest_api_gateway():
    new()
    title("REST API Gateway", 60, 40)
    subtitle("The REST API is the single entry point that encapsulates business logic — auth, "
             "authentication and input sanitizing — before resources are reached.", 60, 96, width=940)

    clients = [("Desktop", 170), ("Mobile Client", 270),
               ("Legacy\nApplications", 370), ("Other Services", 470)]
    for lbl, y in clients:
        box(60, y, 200, 64, lbl, fill=CON, stroke=INK)
        arrow(260, y + 32, 350, 360, color=MID)

    acc_box(350, 240, 240, 240, "REST API Gateway")
    text("Authorization · Authentication\nInput sanitizing", 470, 430, size=11,
         color=MID, align="center", anchor="cm")

    box(720, 280, 220, 160, "Application\nBusiness Logic", fill=WHITE, stroke=INK)
    arrow(590, 360, 720, 360)
    text("one entry point", 655, 340, size=12, color=MID, align="center", anchor="cb")

    dashed_group(45, 145, 250, 420, "Any client type")
    text("Backend is decoupled from client implementations", 720, 470, size=12, color=MID)
    save("REST API Gateway")


# --------------------------------------------------------------------- GraphQL
def product_details_json_response():
    new()
    title("Product details JSON response", 60, 40)
    subtitle("GET /products returns every field of every product — the Android app gets far more "
             "than it needs (over-fetching).", 60, 96, width=920)

    browser(60, 190, 180, 125, "Desktop\nCategory page")
    mobile(60, 360, 180, 145, "Android app\nCategory page")
    acc_box(300, 270, 200, 120, "REST API\nGET /products")
    arrow(240, 252, 300, 300)
    arrow(240, 430, 300, 360)
    text("same endpoint", 270, 500, size=12, color=MID, align="center")

    code_card(570, 150, 430, 470, "JSON response", '''{
  "products": [
    {
      "id": 1,
      "name": "Wireless Bluetooth Headphones",
      "description": "High-quality wireless ...",
      "price": 99.99,
      "inventoryCount": 50
    },
    {
      "id": 2,
      "name": "Smartphone Stand",
      "description": "Adjustable smartphone stand ...",
      "price": 19.99,
      "inventoryCount": 150
    }
  ]
}''')

    arrow(1005, 300, 990, 300, color=ACC, w=2)
    text("Android needs only\n\"name\" and \"price\" —\nthe rest is wasted bandwidth", 1010, 300,
         size=13, color=ACC)
    text("Over-fetching: server decides the response shape", 570, 645, size=12, color=MID)
    save("Product details JSON response")


def graphql_query():
    new()
    title("GraphQL query", 60, 40)
    subtitle("One query asks for exactly the fields needed — product, reviews and related "
             "products — and the server returns a single JSON response.", 60, 96, width=940)

    browser(60, 210, 180, 130, "iOS app\nCategory page")
    arrow(240, 275, 520, 330, color=ACC)
    text("1 query", 360, 280, size=12, color=ACC, align="center")

    code_card(60, 400, 400, 240, "GraphQL query", '''query {
  product(id: 56231) {
    id  name  description  price
    reviews { id rating comment }
    relatedProducts { id name price }
  }
}''')

    acc_box(520, 280, 220, 130, "GraphQL API")

    sources = [("Product Service", 180), ("Reviews Service", 290), ("Related Products", 400)]
    for lbl, y in sources:
        box(820, y, 220, 70, lbl, fill=CON, stroke=INK)
        arrow_bidir(740, 345, 820, y + 35, color=MID, dash=True)
    text("resolves fields from\neach data source", 780, 470, size=11, color=MID, align="center")

    arrow(520, 390, 250, 350, color=ACC)
    text("single JSON\nresponse", 370, 400, size=12, color=ACC, align="center")

    text("Avoids the 3 separate REST calls:\nGET /products/{id}  ·  /reviews  ·  /related",
         600, 590, size=12, color=MID)
    save("GraphQL query")


# --------------------------------------------------------------------- HTTP pull / push
def ajax():
    new()
    title("AJAX - Asynchronous JavaScript & XML", 60, 40)
    subtitle("The UI polls the server repeatedly with XMLHttpRequest; a callback updates part of "
             "the page — no reload.", 60, 96, width=940)

    browser(80, 190, 280, 350, "")
    text("User Interface", 220, 240, size=15, color=INK, align="center", anchor="ct")
    text("Callback method\ndynamically updates\nthe presentation", 220, 470, size=13,
         color=MID, align="center", anchor="cm")

    server(760, 260, 220, 210, "Web Server")

    arrow(360, 290, 760, 290, dash=True)
    arrow(360, 380, 760, 380, dash=True)
    arrow(360, 480, 760, 470, dash=True)
    text("XMLHttpRequest — polled every X units of time\n(set by the developer, no user action)",
         560, 180, size=12, color=MID, align="center")
    gear(560, 590, r=18)

    arrow(760, 540, 360, 500, color=ACC)
    text("Response (JSON / XML)", 560, 555, size=12, color=ACC, align="center")

    text("HTTP Pull — polling.  AJAX polling is not the same as AJAX long polling.",
         80, 600, size=12, color=MID)
    save("AJAX - Asynchronous JavaScript & XML")


def persistent_connection():
    new()
    title("Persistent Connection", 60, 40)
    subtitle("HTTP Pull kills the connection after the TTL; a persistent connection stays open "
             "via heartbeat interceptors, enabling HTTP Push.", 60, 96, width=960)

    dashed_group(60, 150, 520, 470, "HTTP Pull")
    browser(100, 240, 170, 120, "Client")
    server(390, 240, 150, 120, "Server")
    arrow_bidir(270, 300, 390, 300)
    text("TTL 30–60s", 330, 250, size=12, color=MID, align="center")
    line(300, 420, 360, 460, color=ACC)
    line(360, 420, 300, 460, color=ACC)
    text("connection is killed after the TTL —\nclient must re-send its request", 320, 490,
         size=12, color=MID, align="center")

    dashed_group(640, 150, 750, 470, "Persistent Connection")
    browser(680, 240, 190, 130, "Client")
    server(1080, 240, 190, 130, "Server")
    arrow_bidir(870, 305, 1080, 305)
    text("connection stays open", 975, 275, size=12, color=MID, align="center")
    arrow(870, 235, 1080, 235, dash=True, color=MID)
    arrow(1080, 255, 870, 255, dash=True, color=MID)
    text("heartbeat interceptors (blank request / response)", 975, 200, size=11,
         color=MID, align="center")
    arrow(1080, 400, 870, 380, color=ACC)
    text("server pushes updates (HTTP Push)", 975, 420, size=12, color=ACC, align="center")
    text("vital for browser-based multiplayer games", 680, 555, size=12, color=MID)
    save("Persistent Connection")


def streaming_api():
    new()
    title("Streaming API", 60, 40)
    subtitle("After an initial request the server streams data to the client in chunks — a one-way "
             "flow from server to client.", 60, 96, width=920)

    browser(80, 250, 200, 150, "Client\n(browser)")
    server(760, 240, 210, 180, "Server")

    arrow(280, 300, 760, 300)
    text("initial request establishes\na persistent connection", 520, 250, size=12,
         color=MID, align="center")
    line(280, 360, 760, 360, dash=True, color=BDR)

    arrow(760, 470, 280, 470, color=ACC)
    for i, cx in enumerate([600, 480, 360]):
        document(cx, 448, 80, 44, "")
        text("chunk " + str(i + 1), cx + 40, 500, size=11, color=MID, align="center")
    text("data streamed in chunks — only server → client", 520, 545, size=12,
         color=ACC, align="center")

    text("HTML5 Event-Source API / Stream API", 80, 470, size=12, color=MID)
    text("use cases: video, live feeds, stock quotes, notifications", 80, 495, size=12, color=MID)
    save("Streaming API")


# --------------------------------------------------------------------- scalability
def scalability():
    new()
    title("Scalability", 60, 40)
    subtitle("A scalable app keeps response time constant (x seconds) even as concurrent users "
             "grow from one to millions.", 60, 96, width=920)

    dashed_group(60, 150, 470, 460, "BEFORE")
    person(160, 240, "Single user")
    server(250, 340, 230, 150, "Application")
    arrow(200, 335, 250, 370)
    text("Response in x seconds", 365, 540, size=13, color=INK, align="center")

    dashed_group(600, 150, 760, 460, "AFTER")
    for cx, top in [(660, 230), (720, 260), (780, 230), (660, 310), (720, 340), (780, 310)]:
        person(cx, top, "", scale=0.7)
    text("Concurrent users\nin the millions", 720, 400, size=12, color=MID, align="center")
    acc_box(880, 340, 260, 150, "Scalable\nApplication")
    arrow(800, 300, 880, 390)
    arrow(800, 400, 880, 410)
    text("Response still x seconds for every user", 1010, 540, size=13, color=ACC, align="center")

    text("Latency stays flat as load grows = scalable (ideally O(1))", 60, 640, size=12, color=MID)
    save("Scalability")


def latency():
    new()
    title("Latency", 60, 40)
    subtitle("Latency = network latency (packet travel time) + application latency (request "
             "processing time).", 60, 96, width=900)

    browser(60, 300, 180, 130, "User")
    cloud(430, 365, 240, 140, "CDN / Edge location")
    server(720, 290, 200, 150, "Origin Server")
    box(980, 300, 200, 120, "Application\nprocesses request", fill=WHITE, stroke=INK)

    arrow(240, 365, 320, 365)
    arrow(550, 365, 720, 375)
    arrow(920, 375, 980, 375)
    arrow(720, 460, 240, 440, color=ACC)
    text("response", 480, 445, size=12, color=ACC, align="center")

    line(150, 260, 820, 260, color=MID)
    line(150, 252, 150, 268, color=MID)
    line(820, 252, 820, 268, color=MID)
    text("Network latency", 485, 240, size=13, color=MID, align="center", anchor="cb")

    line(980, 275, 1180, 275, color=MID)
    line(980, 267, 980, 283, color=MID)
    line(1180, 267, 1180, 283, color=MID)
    text("Application latency", 1080, 255, size=13, color=MID, align="center", anchor="cb")

    text("CDN edge locations near users cut network latency", 60, 500, size=12, color=MID)
    text("Low latency determines whether a business wins or loses a customer", 60, 525,
         size=12, color=MID)
    save("Latency")


def vertical_scalability():
    new()
    title("Vertical scalability", 60, 40)
    subtitle("Scale up: give the same server more power (16 GB → 32 GB RAM). Simple, with no code "
             "changes — but limited by one machine.", 60, 96, width=940)

    dashed_group(60, 150, 450, 440, "BEFORE")
    browser(120, 210, 180, 110, "Website")
    server(150, 370, 240, 190, "Server\n16 GB RAM")
    arrow(210, 320, 260, 380)

    dashed_group(590, 150, 760, 440, "AFTER")
    browser(640, 210, 180, 110, "Website")
    server(700, 370, 260, 190, "Server\n32 GB RAM", fill=WHITE, stroke=ACC)
    arrow(730, 320, 810, 380)
    text("More powerful server,\nhandles all the traffic", 1000, 300, size=13, color=ACC)

    arrow(510, 430, 590, 430, color=ACC)
    text("scale up\n(add RAM / CPU)", 550, 460, size=12, color=ACC, align="center")

    text("Simplest way to scale — no refactoring or complex config", 60, 620, size=12, color=MID)
    text("Limit: there is only so much compute power a single server can take", 60, 645,
         size=12, color=MID)
    save("Vertical scalability")


if __name__ == "__main__":
    feature_apis()
    public_api()
    rest_api_architecture_2()
    rest_api_gateway()
    product_details_json_response()
    graphql_query()
    ajax()
    persistent_connection()
    streaming_api()
    scalability()
    latency()
    vertical_scalability()
    print("wrote 12 web-architecture batch B2 scenes")
