#!/usr/bin/env python3
"""Web/mobile batch b9 — responsive UI, mobile app types, MBaaS and course covers.

Meaning-first scenes drawn with ekit. One function per source image; each saves a
`<basename>.excalidraw` file next to this script.
"""
from ekit import *


# --------------------------------------------------------------------- helpers
def _grid(x0, y0, cols, rows, cw, ch, gap, cell_labels=False):
    """Draw a rows x columns grid of cells (to show a responsive layout)."""
    for r in range(rows):
        for c in range(cols):
            cx = x0 + c * (cw + gap)
            cy = y0 + r * (ch + gap)
            rect(cx, cy, cw, ch, fill=WHITE, stroke=BDR)
            if cell_labels and r == 0:
                text("Col %d" % (c + 1), cx + cw / 2, cy + ch / 2,
                     size=10, color=MID, align="center", anchor="cm")


# ------------------------------------------------------------------ 1. responsive
def responsive_ui():
    new()
    title("Responsive user interface", 60, 40)
    subtitle("A responsive (mobile-friendly) site is built once as a grid of rows and columns; "
             "the columns re-arrange themselves as the screen gets smaller — desktop-first, one codebase.",
             60, 96, width=940)

    browser(70, 220, 430, 310, "")
    text("Desktop browser", 70, 195, size=14, color=INK)
    _grid(94, 270, 4, 2, 88, 95, 10, cell_labels=True)
    text("4 columns", 285, 545, size=12, color=MID, align="center", anchor="ct")

    browser(545, 220, 230, 310, "")
    text("Tablet browser", 545, 195, size=14, color=INK)
    _grid(567, 288, 2, 3, 88, 72, 8, cell_labels=True)
    text("2 columns", 660, 545, size=12, color=MID, align="center", anchor="ct")

    mobile(820, 220, 150, 300, "")
    text("Mobile browser", 820, 195, size=14, color=INK)
    _grid(840, 280, 1, 4, 110, 52, 6)
    text("1 column", 895, 545, size=12, color=MID, align="center", anchor="ct")

    arrow(500, 375, 545, 375, color=MID)
    text("narrower screen", 522, 365, size=11, color=MID, align="center", anchor="cb")
    arrow(775, 375, 820, 375, color=MID)
    text("narrower screen", 797, 365, size=11, color=MID, align="center", anchor="cb")

    text("Same page, same code — only the grid re-arranges.", 70, 590, size=13, color=MID)
    save("Responsive user interface")


# ------------------------------------------------------------------ 2. users-min
def users_min():
    new()
    title("Before you design your mobile app", 60, 40)
    subtitle("Check the analytics first. On this website sessions are overwhelmingly desktop, "
             "so a mobile-friendly responsive UI is the right call — not mobile-first.",
             60, 96, width=900)

    browser(70, 190, 470, 340, "")
    text("Analytics — Sessions by device", 95, 222, size=16, color=INK)

    text("Desktop", 178, 292, size=14, color=INK, align="right", anchor="rm")
    rect(190, 276, 250, 32, fill=WHITE, stroke=ACC)
    text("83.5%", 450, 292, size=14, color=INK, anchor="lm")

    text("Mobile", 178, 356, size=14, color=INK, align="right", anchor="rm")
    rect(190, 340, 42, 32, fill=CON, stroke=BDR)
    text("14.1%", 242, 356, size=14, color=INK, anchor="lm")

    text("Tablet", 178, 420, size=14, color=INK, align="right", anchor="rm")
    rect(190, 404, 9, 32, fill=CON, stroke=BDR)
    text("2.4%", 209, 420, size=14, color=INK, anchor="lm")

    arrow(545, 350, 650, 330)
    acc_box(650, 255, 300, 150, "Decision\nMobile-friendly\nresponsive UI")
    subtitle("Mobile-first isn't justified here — keep one desktop-first responsive site.",
             650, 430, width=300)
    save("users-min")


# -------------------------------------------------------- 3. responsive frameworks
def responsive_ui_frameworks():
    new()
    title("Responsive user interface", 60, 40)
    subtitle("Don't hand-write the layout: use a production-grade CSS framework to build the "
             "responsive grid of rows and columns.", 60, 96, width=900)

    dashed_group(70, 180, 360, 400, "Responsive frameworks")
    box(105, 245, 290, 52, "BootstrapJS", fill=WHITE, stroke=ACC)
    box(105, 315, 290, 52, "Tailwind CSS")
    box(105, 385, 290, 52, "jQuery Mobile")
    box(105, 455, 290, 52, "Skeleton")
    box(105, 525, 290, 52, "HTML5 Boilerplate")

    arrow(430, 380, 560, 380, color=INK)
    text("grid + components", 495, 370, size=11, color=MID, align="center", anchor="cb")

    browser(560, 220, 420, 310, "")
    _grid(584, 270, 4, 2, 88, 95, 10, cell_labels=True)
    subtitle("The same page re-arranges across screen sizes via CSS media queries.",
             560, 555, width=420)
    save("Responsive user interface (2)")


# ------------------------------------------------------------------ 4. native app
def native_app():
    new()
    title("Native App", 60, 40)
    subtitle("A native app is compiled for one OS and talks straight to the OS and hardware — "
             "no wrapper — so it gets full device access and the best performance.",
             60, 96, width=900)

    mobile(80, 220, 150, 270, "Native App", fill=WHITE, stroke=ACC)
    arrow(240, 355, 340, 355)
    text("direct calls", 290, 345, size=12, color=MID, align="center", anchor="cb")
    box(340, 290, 210, 130, "Mobile OS\n(Android / iOS)")
    arrow(550, 355, 650, 355)
    text("full access", 600, 345, size=12, color=MID, align="center", anchor="cb")
    box(650, 290, 200, 130, "Device Hardware\n(camera, sensors, GPS)")

    text("Technologies for writing native apps", 80, 515, size=15, color=INK)
    box(80, 548, 250, 72, "Android\nJava · Kotlin · C++")
    box(360, 548, 250, 72, "iOS\nSwift · Objective-C\n+ Cocoa Touch")
    subtitle("One build runs on a single OS only.", 650, 565, width=250)
    save("Native App")


# ------------------------------------------------------------------ 5. hybrid app
def hybrid_app():
    new()
    title("Hybrid app", 60, 40)
    subtitle("Web technologies (HTML5, CSS, JS) run inside a native container; a wrapper / middle "
             "layer bridges them to the OS — one codebase, many platforms, a little slower.",
             60, 96, width=980)

    box(70, 250, 240, 110, "Hybrid App\nHTML5 · CSS · JavaScript", fill=WHITE, stroke=ACC)
    arrow(310, 305, 360, 305)
    text("runs in", 335, 295, size=11, color=MID, align="center", anchor="cb")
    box(360, 250, 180, 110, "Native\nContainer")
    arrow(540, 305, 590, 305)
    box(590, 250, 160, 110, "Wrapper /\nMiddle Layer", fill=WHITE, stroke=ACC)
    arrow(750, 305, 800, 305)
    box(800, 250, 150, 110, "Mobile OS")
    arrow(950, 305, 1000, 305)
    box(1000, 250, 170, 110, "Device\nHardware")

    subtitle("The extra wrapper layer is why hybrid apps are slightly slower than native apps.",
             70, 390, width=900)

    dashed_group(70, 450, 900, 150, "Hybrid app frameworks")
    box(100, 505, 195, 64, "React Native")
    box(315, 505, 195, 64, "Ionic")
    box(530, 505, 195, 64, "Cordova")
    box(745, 505, 195, 64, "Flutter")
    save("Hybrid app")


# ------------------------------------------------------------ 6. progressive web app
def pwa():
    new()
    title("Progressive web app", 60, 40)
    subtitle("A website that installs like an app: run it in the browser, or install it to run in its "
             "own window — offline-capable, with push notifications.", 60, 96, width=920)

    browser(70, 210, 340, 290, "")
    text("app.example.com", 95, 216, size=11, color=MID)
    badge(396, 221, "+", r=14, size=18)
    text("Install", 396, 250, size=11, color=ACC, align="center", anchor="ct")
    text("Website with app-like UI", 240, 380, size=14, color=MID, align="center", anchor="cm")

    arrow(420, 360, 560, 360)
    text("install from the browser", 490, 350, size=11, color=MID, align="center", anchor="cb")
    mobile(560, 200, 150, 300, "Installed PWA")

    dashed_group(770, 190, 470, 340, "PWA capabilities")
    box(800, 240, 410, 48, "Works offline")
    box(800, 300, 410, 48, "Push notifications")
    box(800, 360, 410, 48, "Installable — no app store")
    box(800, 420, 410, 48, "Indexable by search engines")
    box(800, 480, 410, 48, "Always up to date")

    subtitle("Built with open web tech — HTML, CSS, JavaScript (Angular, React, Ionic, Polymer).",
             70, 530, width=680)
    save("Progressive web app")


# ------------------------------------------------------------------ 7. mobile BaaS
def mobile_baas():
    new()
    title("Mobile BaaS (Backend as a Service)", 60, 40)
    subtitle("The cloud vendor runs the backend — auth, storage, push, messaging, analytics — "
             "behind one API per feature. Business logic lives in the app (a fat client).",
             60, 96, width=980)

    mobile(70, 250, 150, 270, "Mobile App\n(fat client)", fill=WHITE, stroke=ACC)
    arrow(230, 385, 360, 385)
    text("one API per feature", 295, 375, size=11, color=MID, align="center", anchor="cb")

    dashed_group(360, 180, 650, 400, "Mobile BaaS — Firebase · AWS Amplify · Parse")
    box(400, 240, 250, 70, "User Authentication")
    box(680, 240, 250, 70, "Push Notifications")
    box(400, 320, 250, 70, "Real-time Database")
    box(680, 320, 250, 70, "Data Storage")
    box(400, 400, 250, 70, "Messaging / Chat")
    box(680, 400, 250, 70, "Analytics")
    box(400, 480, 250, 70, "Crash Reporting")
    box(680, 480, 250, 70, "Social Integration")

    subtitle("No infrastructure to build or maintain · a generous free tier while bootstrapping.",
             360, 600, width=660)
    subtitle("Risk: vendor lock-in — the provider owns the backend.", 70, 560, width=260)
    save("Mobile BaaS (Backend as a Service)")


# ------------------------------------------------------------ 8. custom mobile backend
def custom_backend():
    new()
    title("Custom backend for a mobile app", 60, 40)
    subtitle("The conventional way: mobile and web clients talk over dedicated APIs to a backend "
             "you build and fully control — server, messaging, cache and database.",
             60, 96, width=980)

    mobile(70, 240, 150, 260, "Mobile App")
    browser(70, 540, 180, 120, "Web Client")
    arrow(230, 380, 380, 380)
    text("dedicated API", 305, 370, size=11, color=MID, align="center", anchor="cb")

    dashed_group(380, 190, 620, 420, "Custom Backend")
    box(420, 240, 250, 110, "Backend Server", fill=WHITE, stroke=ACC)
    box(700, 240, 250, 110, "Messaging Server")
    cache(420, 390, 250, 110, "Cache Server", fill=CON, stroke=INK)
    database(700, 380, 250, 140, "Database")

    subtitle("You own the design — add new clients and dedicated APIs as the business grows.",
             380, 620, width=620)
    save("Custom backend for a mobile app")


# ------------------------------------------------------ 9. BaaS + custom backend
def baas_plus_custom():
    new()
    title("Mobile BaaS with a custom backend", 60, 40)
    subtitle("Use both: managed BaaS for the usual features, and a custom (legacy) backend for what "
             "only it can do — e.g. a banking app cross-verifying data.", 60, 96, width=980)

    mobile(70, 300, 150, 260, "Banking App", fill=WHITE, stroke=ACC)

    dashed_group(360, 170, 620, 230, "Mobile BaaS — Firebase / AWS Amplify")
    box(400, 225, 250, 70, "User Authentication")
    box(700, 225, 250, 70, "Push Notifications")
    box(400, 315, 250, 70, "Real-time DB")
    box(700, 315, 250, 70, "Storage")

    arrow(230, 385, 360, 300)
    text("auth, push, storage", 300, 330, size=11, color=MID, align="center", anchor="ct")

    dashed_group(360, 470, 620, 200, "Custom / Legacy Enterprise Backend")
    box(400, 520, 250, 110, "Backend Server", fill=WHITE, stroke=ACC)
    database(700, 510, 250, 130, "Core Banking DB")

    arrow(230, 460, 360, 560)
    text("cross-verify data", 300, 540, size=11, color=MID, align="center", anchor="ct")

    subtitle("Managed services where it's convenient; the custom backend where integration and "
             "control matter.", 70, 620, width=900)
    save("Mobile BaaS with a custom backend")


# ------------------------------------------------------------------ 10. course cover 1
def cover_web():
    new()
    rect(60, 110, 1200, 600, fill=WHITE, stroke=BDR, rx=True)
    rect(60, 110, 1200, 16, fill=ACC, stroke=ACC, rx=True)
    text("ZERO TO SOFTWARE ARCHITECT  ·  LEARNING TRACK  ·  COURSE 1", 100, 150, size=13, color=MID)
    text("Web Application &\nSoftware Architecture 101", 100, 185, size=42, color=INK)
    line(100, 330, 720, 330, color=ACC, w=3)
    subtitle("Master the fundamentals of web architecture with insights from real-world "
             "implementations of web-scale services.", 100, 350, size=17, width=740)

    text("What you'll master", 900, 185, size=16, color=INK)
    for i, s in enumerate([
        "• Clients, servers & layers",
        "• Scalability & high availability",
        "• Caching, queues & databases",
        "• Monoliths → microservices",
    ]):
        text(s, 900, 225 + i * 30, size=15, color=MID)

    person(140, 480, "Users", scale=0.8)
    arrow(185, 510, 250, 510)
    hexagon(250, 465, 150, 90, "Load\nBalancer")
    arrow(400, 510, 470, 510)
    box(470, 465, 140, 90, "App\nServer")
    arrow(610, 510, 680, 510)
    cache(680, 465, 130, 90, "Cache", fill=CON, stroke=INK)
    arrow(810, 510, 880, 510)
    database(880, 460, 140, 100, "Database")
    queue(470, 585, 180, 55, "Message Queue")
    line(540, 555, 540, 585, color=MID, dash=True)

    text("zerotosoftwarearchitect.com", 100, 665, size=13, color=MID)
    save("Course cover-min")


# ------------------------------------------------------------------ 11. course cover 2
def cover_cloud():
    new()
    rect(60, 110, 1200, 600, fill=WHITE, stroke=BDR, rx=True)
    rect(60, 110, 1200, 16, fill=ACC, stroke=ACC, rx=True)
    text("ZERO TO SOFTWARE ARCHITECT  ·  LEARNING TRACK  ·  COURSE 2", 100, 150, size=13, color=MID)
    text("Cloud Computing 101\nMaster the Fundamentals", 100, 185, size=40, color=INK)
    line(100, 315, 650, 315, color=ACC, w=3)
    subtitle("A platform-agnostic cloud course: regions and availability zones, containers, "
             "autoscaling and deployment workflows — the same on AWS, Google Cloud or Azure.",
             100, 335, size=17, width=720)

    text("What you'll master", 900, 185, size=16, color=INK)
    for i, s in enumerate([
        "• Service & deployment models",
        "• Regions & availability zones",
        "• Containers & autoscaling",
        "• Serverless, FaaS & edge computing",
    ]):
        text(s, 900, 225 + i * 30, size=15, color=MID)

    person(120, 480, "Users", scale=0.8)
    arrow(165, 510, 230, 510)
    hexagon(230, 465, 170, 90, "Regional\nLoad\nBalancer")
    arrow(400, 510, 470, 510)
    cloud(590, 480, 170, 110, "Cloud")
    dashed_group(680, 440, 460, 180, "Region · Availability Zones")
    for i, s in enumerate(["Service\ninstance", "Service\ninstance", "Service\ninstance"]):
        container(715 + i * 140, 490, 110, 90, s, size=11)

    text("zerotosoftwarearchitect.com", 100, 665, size=13, color=MID)
    save("Cloud course cover-min")


# ------------------------------------------------------------------ 12. course cover 3
def cover_distributed():
    new()
    rect(60, 110, 1200, 600, fill=WHITE, stroke=BDR, rx=True)
    rect(60, 110, 1200, 16, fill=ACC, stroke=ACC, rx=True)
    text("ZERO TO SOFTWARE ARCHITECT  ·  LEARNING TRACK  ·  COURSE 3", 100, 150, size=13, color=MID)
    text("Design Modern Web-Scale\nDistributed Applications\nLike a Pro", 100, 180, size=40, color=INK)
    line(100, 350, 720, 350, color=ACC, w=3)
    subtitle("Application data and data-access patterns are the heart of distributed systems — "
             "sharding, distributed transactions, concurrency and consistency at web scale.",
             100, 370, size=17, width=760)

    text("You'll also learn", 900, 180, size=16, color=INK)
    for i, s in enumerate([
        "• Sharding & partitioning",
        "• Distributed transactions",
        "• Consistency & ACID at scale",
        "• Handling concurrent traffic",
    ]):
        text(s, 900, 220 + i * 30, size=15, color=MID)

    person(110, 500, "Users", scale=0.8)
    arrow(155, 535, 215, 535)
    box(215, 490, 140, 90, "Edge\nLocation")
    arrow(355, 535, 410, 535)
    dashed_group(410, 455, 470, 180, "Sharded data")
    for i, s in enumerate(["Shard A", "Shard B", "Shard C"]):
        box(440 + i * 145, 500, 120, 90, s)
    arrow(880, 535, 940, 535)
    database(940, 480, 150, 120, "Origin\nData")

    text("zerotosoftwarearchitect.com", 100, 665, size=13, color=MID)
    save("Course cover large font-min")


if __name__ == "__main__":
    responsive_ui()
    users_min()
    responsive_ui_frameworks()
    native_app()
    hybrid_app()
    pwa()
    mobile_baas()
    custom_backend()
    baas_plus_custom()
    cover_web()
    cover_cloud()
    cover_distributed()
    print("wrote 12 scenes")
