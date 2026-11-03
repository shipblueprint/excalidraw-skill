#!/usr/bin/env python3
"""Cloud Computing 101 — batch B1 scene set (meaning-driven Excalidraw diagrams).

One function per source image; run this file to (re)write the .excalidraw scenes.
"""
from ekit import *


# --------------------------------------------------------------- 1.1 Cloud
def cloud_hosting():
    new()
    title("Cloud", 60, 40)
    subtitle("The developer deploys the app to the cloud; the provider runs and manages all the "
             "infrastructure, and end-users around the world reach the service over the web.",
             60, 96, width=840)

    # developer + app
    person(140, 240, "Developer")
    box(60, 380, 190, 90, "Developer's App")
    arrow_right(250, 425, 180, "deploys via API")

    # the cloud: infrastructure managed for you
    dashed_group(440, 250, 400, 270, "Cloud — the provider manages all infrastructure")
    server(470, 300, 150, 110, "App Servers")
    database(650, 300, 160, 110, "Data Store")
    text("OS · scaling · monitoring · security", 640, 455, size=12, color=MID,
         align="center", anchor="cm")

    # end-users worldwide
    arrow(840, 400, 945, 400)
    text("over the web", 890, 388, size=11, color=MID, align="center", anchor="cb")
    person(1010, 270, "End-user")
    person(1120, 270, "End-user")
    browser(950, 430, 240, 120, "Service on the cloud")

    save("Cloud")


# ----------------------------------------- 1.2 Intermediary Cloud Service Provider
def intermediary_provider():
    new()
    title("Intermediary Cloud Service Provider", 60, 40)
    subtitle("A smaller provider with a simple, focused interface sits on top of a large cloud "
             "platform, extending its infrastructure — the developer deploys here.", 60, 96, width=880)

    person(110, 180, "Developer")
    box(60, 300, 180, 90, "Developer's App")
    arrow_right(240, 345, 120, "deploy")

    acc_box(360, 280, 300, 130,
            "Intermediary Cloud\nService Provider\n(Netlify · Heroku · Zeit)")
    text("small scale · specific use case\nsimple, intuitive interface", 510, 425, size=12,
         color=MID, align="center", anchor="ct")

    arrow_down(510, 470, 55, "rents / extends infrastructure")

    dashed_group(330, 545, 460, 155, "Large Cloud Provider — AWS / Azure / GCP")
    server(360, 590, 140, 90, "Compute")
    database(530, 595, 130, 85, "Storage")
    server(690, 590, 130, 90, "Networking")

    # served to end-users
    arrow_right(640, 345, 210, "serves")
    person(930, 280, "End-user")
    person(1040, 280, "End-user")
    text("end-users worldwide\nreach the service", 985, 430, size=12, color=MID,
         align="center", anchor="ct")

    save("Intermediary Cloud Service Provider")


# --------------------------------------------------------------- 1.4 Hybrid Cloud
def hybrid_cloud():
    new()
    title("Hybrid Cloud", 60, 40)
    subtitle("A service runs some modules on a private cloud (on-premises) and others on a public "
             "cloud — combining the two deployment models.", 60, 96, width=800)

    dashed_group(60, 170, 1240, 470, "Hybrid Cloud")

    # private / on-prem
    dashed_group(90, 250, 520, 350, "On-premises (Private Cloud)")
    database(150, 330, 170, 140, "Sensitive Data", fill=WHITE, stroke=ACC)
    server(370, 340, 190, 130, "Secure / Legacy\nWorkloads")
    text("sensitive data stays on-prem", 350, 520, size=12, color=MID,
         align="center", anchor="ct")

    # public
    dashed_group(680, 250, 560, 350, "Public Cloud (e.g. Google Cloud)")
    server(720, 340, 190, 130, "App / Web Tier")
    database(950, 330, 170, 140, "Replica &\nAnalytics")
    text("elastic, pay-as-you-go", 960, 520, size=12, color=MID,
         align="center", anchor="ct")

    arrow_bidir(610, 410, 680, 410)
    text("sync / burst compute", 645, 398, size=11, color=MID, align="center", anchor="cb")

    save("Hybrid Cloud")


# --------------------------------------------------------------- 1.5 Multi-Cloud
def multi_cloud():
    new()
    title("Multi-Cloud", 60, 40)
    subtitle("The same service is deployed across multiple public cloud platforms — no dependence on "
             "a single provider, at the cost of more operational complexity.", 60, 96, width=880)

    person(110, 240, "End-users")
    arrow(190, 350, 330, 360)
    acc_box(330, 300, 220, 120, "Service\n(deployed across\nmultiple clouds)")

    for label, y in (("AWS", 170), ("Microsoft Azure", 340), ("Google Cloud", 510)):
        dashed_group(640, y, 380, 150, label)
        server(670, y + 40, 150, 95, "App instances")
        database(850, y + 45, 140, 85, "DB")

    arrow(550, 340, 640, 245)
    arrow(550, 360, 640, 415)
    arrow(550, 380, 640, 585)
    text("+ more complexity to operate across platforms", 440, 445, size=12, color=MID,
         align="center", anchor="ct")

    save("Multi-Cloud")


# ------------------------------------------------- 1.6 Infrastructure as a Service
def infrastructure_as_a_service():
    new()
    title("Infrastructure as a Service", 60, 40)
    subtitle("IaaS gives the highest control: you pick the servers, storage and networking, but you "
             "still manage the OS, middleware and runtimes — the provider owns the hardware.",
             60, 96, width=880)

    person(110, 250, "Business / Developer")
    arrow(190, 320, 360, 290)
    text("access & configure\nover the web", 250, 300, size=11, color=MID,
         align="center", anchor="ct")

    # business-managed software stack
    dashed_group(360, 160, 460, 215, "")
    text("Managed by the Business", 365, 138, size=13, color=MID)
    box(385, 195, 410, 34, "Application")
    box(385, 233, 410, 34, "Runtime")
    box(385, 271, 410, 34, "Middleware")
    box(385, 309, 410, 34, "Operating System")

    line(360, 400, 820, 400, color=ACC, w=3)
    text("IaaS boundary", 828, 391, size=12, color=ACC)

    # provider-managed physical stack
    dashed_group(360, 420, 460, 235, "")
    text("Managed by the Cloud Provider", 365, 666, size=13, color=MID)
    box(385, 455, 410, 34, "Hypervisor / Virtualization")
    box(385, 493, 410, 34, "Physical Servers")
    box(385, 531, 410, 34, "Storage")
    box(385, 569, 410, 34, "Networking")

    text("AWS · Google Cloud · Azure · Digital Ocean", 60, 600, size=13)
    text("Pay as you go · scale up and down on demand", 60, 630, size=12, color=MID)

    save("Infrastructure as a Service")


# ------------------------------------------------------- 1.7 Platform as a Service
def platform_as_a_service():
    new()
    title("Platform as a Service", 60, 40)
    subtitle("With PaaS you only write and deploy the application — the provider runs the runtime, "
             "middleware, OS and scaling as a managed platform.", 60, 96, width=860)

    person(110, 230, "Business / Developer")
    arrow(195, 255, 360, 240)
    text("write code &\ndeploy via the APIs", 250, 300, size=11, color=MID,
         align="center", anchor="ct")

    dashed_group(360, 175, 460, 90, "Managed by the Business")
    box(385, 210, 410, 40, "Application")

    # the managed platform (highlighted)
    rect(360, 300, 460, 340, fill="transparent", stroke=ACC, dash=True, rx=True)
    text("Platform — managed by the Cloud Provider", 365, 278, size=13, color=ACC)
    acc_box(385, 335, 410, 40, "Runtime · Middleware · Services")
    box(385, 385, 410, 40, "OS · Security patches · Scaling")
    box(385, 435, 410, 40, "Databases · Monitoring · Logging")

    line(360, 500, 820, 500, color=ACC, w=3)
    text("platform boundary", 828, 491, size=12, color=ACC)
    box(385, 515, 410, 40, "Physical Hardware · Data Center")

    text("No infrastructure to manage — but watch out for vendor lock-in.", 60, 600, size=12, color=MID)

    save("Platform as a Service")


# ------------------------------------------------- 1.9 App Dashboard (UI mock)
def app_dashboard():
    new()
    title("App Dashboard", 60, 40)
    subtitle("The App Engine console during testing — request rate, client/server errors, and the "
             "autoscaled instances.", 60, 96, width=860)

    browser(60, 170, 1040, 520, "")
    text("Google Cloud Platform — App Engine", 105, 172, size=13)

    # time-range selector
    ranges = ["1h", "6h", "12h", "1d", "2d", "4d", "7d", "14d", "30d"]
    for i, r in enumerate(ranges):
        x = 80 + i * 50
        if r == "7d":
            acc_box(x, 205, 44, 26, r, size=11)
        else:
            box(x, 205, 44, 26, r, size=11)
    box(820, 205, 160, 26, "Version 20190201", size=11)
    box(990, 205, 90, 26, "REFRESH", size=12)

    # summary metric cards
    box(80, 250, 300, 80, "Total requests: 9.3K\n(by version id)", size=13)
    box(400, 250, 300, 80, "Client (4XX): 263", size=13)
    box(720, 250, 300, 80, "Server (5XX): 2.0K", size=13)

    # request-rate chart
    rect(80, 350, 640, 310, fill=WHITE, stroke=BDR, rx=True)
    text("Count/sec (by version id)", 95, 362, size=12)
    line(110, 630, 700, 630, color=MID, w=1)
    line(110, 400, 110, 630, color=MID, w=1)
    pts = [(110, 610), (170, 600), (230, 615), (290, 560), (350, 590), (410, 470),
           (470, 500), (530, 440), (590, 480), (650, 420), (700, 460)]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        line(x1, y1, x2, y2, color=ACC, w=2)

    # autoscaled instances
    rect(740, 350, 340, 310, fill=WHITE, stroke=BDR, rx=True)
    text("Instances (autoscaled)", 755, 362, size=12)
    box(755, 395, 310, 110,
        "ID 00c61b11…9bda\nQPS 0 · Latency 0 ms\nMemory 2148 MB · Dynamic", size=11)
    box(755, 520, 310, 110,
        "ID 00c61b11…d02f\nQPS 1 · Requests 9.3K\nMemory 216.1 MB · Dynamic", size=11)

    text("2 Instances (autoscaled) · Availability: Dynamic", 80, 668, size=11, color=MID)

    save("App Dashboard")


# ------------------------------------------------------- 1.10 Software as a Service
def software_as_a_service():
    new()
    title("Software as a Service", 60, 40)
    subtitle("Consume a fully managed, plug-and-play third-party service — integrate it with your app "
             "via APIs/Webhooks, or use it directly through its web dashboard.", 60, 96, width=900)

    box(60, 260, 220, 130, "Business Application\n(e-commerce platform)")
    arrow_right(280, 325, 150, "APIs / Webhooks")
    acc_box(430, 255, 250, 140, "SaaS Product\n(fully managed service)")

    person(1050, 190, "Direct user")
    browser(950, 300, 200, 140, "SaaS Web Dashboard")
    arrow(950, 370, 680, 355)
    text("use directly via\nweb dashboard", 815, 310, size=11, color=MID,
         align="center", anchor="ct")

    arrow_down(555, 400, 55, "provider manages")
    dashed_group(330, 470, 480, 175, "Everything else is managed by the SaaS provider")
    server(360, 520, 130, 95, "Servers")
    database(510, 525, 120, 90, "Data")
    gear(700, 565, 30)
    text("tech stack · deployment\nscaling · upgrades · security", 700, 620, size=11,
         color=MID, align="center", anchor="ct")

    save("Software as a Service")


# ------------------------------------------------------- 1.11 Functions as a Service
def functions_as_a_service():
    new()
    title("Functions as a Service", 60, 40)
    subtitle("Write only the business logic as functions; the platform runs them on demand when an "
             "event fires, scaling automatically and billing per millisecond.", 60, 96, width=880)

    # event sources
    box(60, 200, 200, 70, "HTTP request")
    box(60, 310, 200, 70, "Queue message")
    box(60, 420, 200, 70, "User click")
    arrow(260, 235, 400, 330)
    arrow(260, 345, 400, 345)
    arrow(260, 455, 400, 360)
    text("event", 335, 292, size=11, color=MID, align="center", anchor="cm")

    # the function (highlighted)
    acc_box(400, 290, 260, 120, "Function\n(your business logic)")

    arrow_right(660, 345, 100, "returns")
    box(760, 300, 200, 90, "Response / result")

    arrow_down(530, 410, 55, "runs on demand")
    dashed_group(400, 470, 620, 170, "Managed by the cloud platform — no server runs when idle")
    server(440, 520, 150, 100, "Ephemeral server\n(spun up per event)")
    text("auto-scaling · provisioning · monitoring", 730, 610, size=12, color=MID,
         align="center", anchor="ct")

    save("Functions as a Service")


# --------------------------------------------- 1.12 Monolith to Microservices
def monolith_to_microservices():
    new()
    title("Monolith to Microservices", 60, 40)
    subtitle("A single deployable monolith is split into independently deployable microservices — "
             "loosely coupled, each scalable on its own.", 60, 96, width=860)

    # the monolith
    rect(60, 200, 330, 400, fill=CON, stroke=INK, rx=True)
    text("Monolith", 82, 210, size=18)
    box(90, 250, 270, 44, "Users")
    box(90, 304, 270, 44, "Orders")
    box(90, 358, 270, 44, "Payments")
    box(90, 412, 270, 44, "Catalog")
    database(110, 470, 230, 100, "Shared Database")

    arrow(390, 400, 520, 400)
    text("split into", 455, 388, size=12, color=MID, align="center", anchor="cb")

    # microservices, each owning its data store
    for label, y in (("Users Service", 200), ("Orders Service", 340), ("Payments Service", 480)):
        dashed_group(545, y - 15, 445, 135, "")
        box(560, y, 260, 110, label)
        database(870, y, 110, 110, "own DB")

    text("Each service has its own database and can be deployed and scaled independently.",
         560, 620, size=12, color=MID)

    save("Monolith to Microservices")


if __name__ == "__main__":
    cloud_hosting()
    intermediary_provider()
    hybrid_cloud()
    multi_cloud()
    infrastructure_as_a_service()
    platform_as_a_service()
    app_dashboard()
    software_as_a_service()
    functions_as_a_service()
    monolith_to_microservices()
    print("wrote 10 Cloud batch-B1 scenes")
