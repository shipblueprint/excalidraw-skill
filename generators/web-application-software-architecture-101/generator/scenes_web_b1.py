#!/usr/bin/env python3
"""Web architecture scenes (batch 1): tiers, clients/servers, layers, APIs, REST."""
from ekit import *


# 1 -------------------------------------------------------------------------
def web_application_architecture():
    new()
    title("Web Application Architecture", 60, 40)
    subtitle("A web service is assembled from separate tiers/components: a user interface "
             "(client), a backend application server, and supporting services.", 60, 96, width=900)

    person(120, 210, "User", scale=0.9)
    browser(60, 330, 200, 130, "User Interface\n(Client)")

    acc_box(340, 260, 200, 200, "Backend Server\n(business logic)")

    database(650, 160, 150, 160, "Database")
    cache(650, 400, 150, 120, "Cache Server")
    queue(900, 280, 170, 90, "Messaging Server")

    arrow(260, 360, 340, 360)
    text("HTTP", 300, 348, size=12, color=MID, align="center", anchor="cb")

    arrow(540, 300, 650, 250)
    text("read / write", 595, 285, size=11, color=MID, align="center", anchor="cb")
    arrow(540, 400, 650, 450)
    text("cache data", 595, 430, size=11, color=MID, align="center", anchor="cb")
    arrow(540, 360, 900, 325)
    text("async events", 720, 335, size=11, color=MID, align="center", anchor="cb")

    save("Web Application Architecture")


# 2 -------------------------------------------------------------------------
def single_tier():
    new()
    title("Single-tier application", 60, 40)
    subtitle("User interface, business logic, and database all run on the same machine — "
             "everything is local, so there is no network latency.", 60, 96, width=900)

    person(120, 250, "User", scale=1.0)
    arrow(190, 315, 320, 315)
    text("same machine", 255, 303, size=11, color=MID, align="center", anchor="cb")

    dashed_group(320, 180, 520, 440, "Single machine (one tier)")
    box(350, 220, 460, 80, "User Interface")
    box(350, 320, 460, 80, "Backend / Business Logic")
    database(350, 420, 460, 150, "Database")

    text("Data never leaves the machine -> highest privacy, no network hop", 350, 650, size=13, color=ACC)
    text("Examples: MS Office, Photoshop / Gimp, PC games", 980, 250, size=13, color=MID)
    save("Single-tier application")


# 3 -------------------------------------------------------------------------
def client_server():
    new()
    title("Client-server architecture", 60, 40)
    subtitle("Two tiers: the client keeps the user interface and business logic; the backend "
             "server owns the database. The client sends a request, the server responds.",
             60, 96, width=980)

    person(110, 170, "User", scale=0.8)

    dashed_group(60, 280, 340, 300, "Client (Tier 1) - UI + business logic")
    browser(90, 330, 280, 100, "User Interface")
    box(90, 450, 280, 80, "Business Logic")

    dashed_group(640, 280, 360, 300, "Backend Server (Tier 2)")
    database(680, 330, 280, 200, "Database")

    arrow(400, 380, 640, 380)
    text("Request", 520, 368, size=13, color=MID, align="center", anchor="cb")
    arrow(640, 480, 400, 480)
    text("Response", 520, 468, size=13, color=MID, align="center", anchor="cb")

    text("Client and server are physically separate machines", 60, 620, size=13, color=MID)
    save("Client-server architecture")


# 4 -------------------------------------------------------------------------
def three_tier():
    new()
    title("Three-tier application", 60, 40)
    subtitle("User interface, business logic, and database each live on a different machine — "
             "three physically separated tiers.", 60, 96, width=900)

    person(190, 180, "User", scale=0.8)

    dashed_group(70, 260, 300, 260, "Tier 1 - User Interface")
    browser(100, 330, 240, 140, "HTML / CSS / JS\n(client)")

    dashed_group(470, 260, 300, 260, "Tier 2 - Backend Server")
    server(500, 320, 240, 160, "Apache\n(business logic)")

    dashed_group(870, 260, 300, 270, "Tier 3 - Database")
    database(900, 330, 240, 170, "MySQL")

    arrow(370, 380, 470, 380)
    text("Request", 420, 368, size=12, color=MID, align="center", anchor="cb")
    arrow(470, 470, 370, 470)
    text("Response", 420, 458, size=12, color=MID, align="center", anchor="cb")

    arrow(770, 380, 870, 380)
    text("Query", 820, 368, size=12, color=MID, align="center", anchor="cb")
    arrow(870, 470, 770, 470)
    text("Result", 820, 458, size=12, color=MID, align="center", anchor="cb")

    text("A blog: HTML/CSS/JS -> Apache -> MySQL", 70, 600, size=13, color=MID)
    save("Three-tier application")


# 5 -------------------------------------------------------------------------
def layers_of_web_app():
    new()
    title("Layers of a web application", 60, 40)
    subtitle("Application layers are a logical, code-level organization — user interface, "
             "controller, service and data-access layers stacked inside one application.",
             60, 96, width=980)

    browser(60, 280, 180, 130, "User Interface\n(client)")

    dashed_group(300, 180, 430, 430, "Application code - layers")
    box(330, 220, 370, 70, "Controller")
    box(330, 310, 370, 70, "Service Layer (business logic)")
    box(330, 400, 370, 70, "Data Access Layer")
    text("Object Model (shared domain objects)", 330, 490, size=13, color=MID)

    arrow(240, 345, 330, 255)
    text("REST API", 285, 285, size=11, color=MID, align="center", anchor="cb")
    arrow_down(515, 290, 20)
    arrow_down(515, 380, 20)

    database(880, 280, 160, 220, "Database")
    arrow(700, 435, 880, 380)
    text("SQL", 790, 420, size=11, color=MID, align="center", anchor="cb")

    text("Layers = logical code organization  |  Tiers = physical separation", 60, 660, size=13, color=ACC)
    save("Layers of a web application")


# 6 -------------------------------------------------------------------------
def web_application_architecture_2():
    new()
    title("Web application architecture", 60, 40)
    subtitle("A typical online architecture: clients reach a backend server, which coordinates "
             "surrounding services — a database, a cache, and a message queue.", 60, 96, width=960)

    browser(60, 210, 170, 120, "Web Client")
    mobile(60, 380, 120, 150, "Mobile Client")

    arrow(180, 270, 340, 300)
    text("HTTPS", 255, 270, size=12, color=MID, align="center", anchor="cb")
    arrow(135, 530, 340, 400)
    text("HTTPS", 240, 480, size=12, color=MID, align="center", anchor="cb")

    acc_box(340, 260, 200, 180, "Backend Server\n(application)")

    database(640, 170, 150, 160, "Database")
    cache(640, 400, 150, 120, "Cache Server")
    queue(880, 280, 180, 90, "Message Queue\n(async work)")

    arrow(540, 300, 640, 250)
    arrow(540, 400, 640, 450)
    arrow(540, 350, 880, 325)

    save("Web application architecture (2)")


# 7 -------------------------------------------------------------------------
def client_server_2():
    new()
    title("Client-server architecture", 60, 40)
    subtitle("The request-response model: any client sends a request and the backend server "
             "returns the response. No request, no response.", 60, 96, width=900)

    dashed_group(50, 180, 280, 420, "Clients")
    browser(75, 220, 230, 110, "Desktop / Browser")
    mobile(75, 360, 120, 150, "Mobile App")
    box(210, 390, 95, 90, "Tablet", size=13)

    arrow(330, 330, 620, 330)
    text("Request (HTTP)", 475, 318, size=13, color=MID, align="center", anchor="cb")
    arrow(620, 430, 330, 430)
    text("Response", 475, 418, size=13, color=MID, align="center", anchor="cb")

    server(620, 250, 230, 200, "Backend Server")

    text("Every website and app is built on this model", 60, 640, size=13, color=MID)
    save("Client-server architecture (2)")


# 8 -------------------------------------------------------------------------
def client():
    new()
    title("Client", 60, 40)
    subtitle("The client is the gateway to the application: it runs the user interface and can be "
             "a mobile app, a desktop, a tablet, or a web-based console.", 60, 96, width=980)

    dashed_group(60, 180, 620, 440, "Client - holds the User Interface")
    browser(90, 240, 260, 150, "Web Browser\n(HTML / CSS / JS)")
    mobile(385, 215, 120, 180, "Mobile App")
    box(385, 420, 120, 80, "Tablet", size=13)
    box(90, 420, 260, 80, "Desktop App", size=14)

    server(760, 250, 230, 190, "Backend Server")
    arrow(680, 320, 760, 320)
    text("Request", 720, 308, size=12, color=MID, align="center", anchor="cb")
    arrow(760, 400, 680, 400)
    text("Response", 720, 388, size=12, color=MID, align="center", anchor="cb")

    text("UI technologies: JavaScript / React / Angular / Vue / Svelte", 90, 650, size=13, color=MID)
    save("Client")


# 9 -------------------------------------------------------------------------
def thin_thick_client():
    new()
    title("Thin client - Thick client", 60, 40)
    subtitle("Thin client: only the user interface, so every action calls the server (three-tier). "
             "Thick client: holds business logic too (two-tier).", 60, 96, width=1000)

    dashed_group(50, 180, 650, 400, "Thin client - UI only (three-tier)")
    box(80, 250, 220, 110, "User Interface\n(no business logic)")
    arrow(300, 305, 400, 305)
    text("Request", 350, 293, size=12, color=MID, align="center", anchor="cb")
    server(400, 240, 260, 170, "Backend Server\n(business logic + database)")

    dashed_group(740, 180, 670, 400, "Thick client / Fat client - UI + business logic (two-tier)")
    box(770, 250, 220, 100, "User Interface")
    box(770, 370, 220, 80, "Business Logic")
    arrow(990, 350, 1090, 350)
    text("Request", 1040, 338, size=12, color=MID, align="center", anchor="cb")
    server(1090, 240, 260, 170, "Backend Server\n(database only)")

    text("Thin client = three-tier   |   Thick client = two-tier", 50, 640, size=13, color=ACC)
    save("Thin client - Thick client")


# 10 ------------------------------------------------------------------------
def application_server():
    new()
    title("Application server", 60, 40)
    subtitle("The application server receives client requests, executes the business logic, and "
             "returns a response. Every component (database, cache, queue) runs on a server too.",
             60, 96, width=1000)

    dashed_group(50, 190, 300, 370, "Clients")
    browser(75, 235, 250, 100, "Desktop Browser")
    mobile(75, 370, 120, 140, "Mobile App")
    box(210, 395, 115, 90, "Web Console", size=12)

    arrow(350, 350, 470, 350)
    text("Request", 410, 338, size=12, color=MID, align="center", anchor="cb")
    arrow(470, 420, 350, 420)
    text("Response", 410, 408, size=12, color=MID, align="center", anchor="cb")

    acc_box(470, 250, 250, 190, "Application Server\n(web server +\nbusiness logic)")

    arrow(720, 320, 830, 300)
    text("query", 775, 300, size=11, color=MID, align="center", anchor="cb")
    arrow(830, 400, 720, 400)
    text("result", 775, 388, size=11, color=MID, align="center", anchor="cb")
    database(830, 230, 170, 200, "Database")

    text("Other server types:", 80, 600, size=13, color=MID)
    box(80, 625, 110, 55, "Proxy", size=13)
    box(200, 625, 110, 55, "Mail", size=13)
    box(320, 625, 110, 55, "File", size=13)
    box(440, 625, 140, 55, "Data Storage", size=12)
    box(590, 625, 130, 55, "Batch Job", size=13)

    save("Application server")


# 11 ------------------------------------------------------------------------
def rest_api_architecture():
    new()
    title("REST API architecture", 60, 40)
    subtitle("Clients call REST endpoints over HTTP; the REST API is the backend's interface to "
             "the outside world and returns a response.", 60, 96, width=980)

    dashed_group(40, 190, 300, 360, "Clients")
    browser(65, 235, 250, 100, "Desktop / Browser")
    mobile(65, 370, 120, 140, "Mobile App")

    arrow(340, 350, 560, 350)
    text("HTTP Request", 450, 338, size=12, color=MID, align="center", anchor="cb")
    text("GET / POST / PUT / DELETE", 450, 300, size=11, color=ACC, align="center", anchor="cb")

    rect(560, 210, 300, 280, fill="transparent", stroke=INK)
    text("Backend Server", 710, 232, size=14, align="center", anchor="ct")
    acc_box(590, 290, 240, 70, "REST API\n(endpoints)")
    box(590, 400, 240, 70, "Business Logic")
    arrow_down(710, 360, 40)

    arrow(560, 460, 340, 460)
    text("Response", 450, 448, size=12, color=MID, align="center", anchor="cb")

    database(950, 280, 180, 180, "Database")
    arrow(860, 430, 950, 430)
    text("SQL", 905, 418, size=11, color=MID, align="center", anchor="cb")

    text("Every request hits a REST endpoint on the backend", 60, 600, size=13, color=MID)
    save("REST API architecture")


# 12 ------------------------------------------------------------------------
def api():
    new()
    title("API", 60, 40)
    subtitle("An API is the interface of a service to the outside world. Clients and internal "
             "microservices alike talk through APIs — the client-server model.", 60, 96, width=1000)

    dashed_group(40, 180, 300, 410, "Clients / Consumers")
    browser(65, 225, 250, 100, "Browser / Web UI")
    mobile(65, 350, 120, 140, "Mobile App")
    box(65, 510, 250, 60, "Third-party Client", size=13)

    arrow(340, 360, 520, 360)
    text("Request", 430, 348, size=12, color=MID, align="center", anchor="cb")

    acc_box(520, 270, 150, 180, "API\n(interface)")

    arrow(670, 340, 800, 300)
    text("routes to", 740, 310, size=11, color=MID, align="center", anchor="cb")

    box(800, 230, 250, 90, "Backend Service 1\n(a microservice)")
    box(800, 470, 250, 90, "Backend Service 2\n(a microservice)")
    arrow_bidir(925, 320, 925, 470)
    text("internal API call", 940, 395, size=11, color=MID, align="left", anchor="lm")

    arrow(520, 470, 340, 470)
    text("Response", 430, 458, size=12, color=MID, align="center", anchor="cb")

    database(1100, 340, 170, 180, "Database")
    arrow(1050, 290, 1100, 380)
    text("data", 1075, 370, size=11, color=MID, align="center", anchor="cb")

    text("Each API is powered by a dedicated backend service; services call each other via APIs too.",
         60, 640, size=13, color=MID)
    save("API")


if __name__ == "__main__":
    web_application_architecture()
    single_tier()
    client_server()
    three_tier()
    layers_of_web_app()
    web_application_architecture_2()
    client_server_2()
    client()
    thin_thick_client()
    application_server()
    rest_api_architecture()
    api()
    print("wrote 12 web-architecture scenes")
