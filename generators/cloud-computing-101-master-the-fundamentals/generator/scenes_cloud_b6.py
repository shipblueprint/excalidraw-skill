#!/usr/bin/env python3
"""Cloud Computing 101 — batch b6 diagrams (data storage, object storage, DevOps).

One function per source image; each calls save("<basename>") writing <basename>.excalidraw.
"""
from ekit import *


# ---------------------------------------------------------------- DevOps
def devops():
    new()
    title("DevOps", 60, 40)
    subtitle("Development + Operations: developers push code into an automated pipeline that "
             "builds, tests, deploys and monitors — managed end to end by the DevOps team.",
             60, 96, width=980)

    dashed_group(150, 160, 1240, 430,
                 "CI/CD Deployment Pipeline — set up & managed by the DevOps team")

    # developer pushes the code
    person(90, 250, "Developer", scale=0.9)
    arrow(150, 285, 200, 285)

    box(200, 240, 150, 90, "Code\nRepository")
    arrow(350, 285, 410, 285)

    acc_box(410, 240, 170, 90, "Build Server\n(Continuous Integration)", size=12)

    # automated build & test stages
    dashed_group(620, 200, 360, 340, "Automated Build & Test Stages")
    tests = ["Static Analysis", "Unit Tests", "Integration Tests",
             "Regression Tests", "Acceptance Tests"]
    for i, t in enumerate(tests):
        bx = 645 + (i % 2) * 165
        by = 235 + (i // 2) * 75
        box(bx, by, 145, 55, t, size=12)
    arrow(580, 285, 620, 285)

    # deployment targets
    arrow(980, 285, 1030, 285)
    box(1030, 245, 170, 80, "Staging\nEnvironment")
    arrow_down(1115, 325, 40)
    box(1030, 365, 170, 80, "Production\nEnvironment", fill=WHITE, stroke=ACC)

    # monitoring in production
    arrow(1200, 405, 1256, 405)
    gear(1290, 405, 28)
    text("Monitoring", 1290, 450, size=12, align="center", anchor="ct", color=MID)

    text("DevOps engineers work in continual contact with developers — no hand-off tickets, ship fast.",
         200, 615, size=13, color=MID)
    save("DevOps")


# ---------------------------------------------------------------- Direct Attached Storage
def das():
    new()
    title("Direct Attached Storage", 60, 40)
    subtitle("DAS: the physical storage is directly attached to the compute in the same machine — "
             "no network involved.", 60, 96, width=820)

    dashed_group(110, 175, 470, 440, "One machine — compute + storage together")
    box(150, 215, 190, 70, "Application")
    arrow_down(245, 285, 40)
    box(150, 325, 190, 70, "File System")
    arrow_down(245, 395, 40)
    database(150, 435, 190, 150, "Storage\n(HDD / SSD)", fill=WHITE, stroke=ACC)

    # direct attachment — no network hop
    box(680, 205, 350, 130,
        "Direct local attachment\nFast access · no eavesdropping\n(not shareable across machines)",
        size=13, fill=CON, stroke=BDR)
    cloud(855, 430, 200, 110, "Network\n(not used)")
    line(755, 385, 955, 485, color=ACC, w=3)
    line(955, 385, 755, 485, color=ACC, w=3)

    text("Examples: internal hard drive, pen drive, external HDD, optical disk.",
         110, 640, size=13, color=MID)
    save("Direct Attached Storage")


# ---------------------------------------------------------------- Network Attached Storage
def nas():
    new()
    title("Network Attached Storage", 60, 40)
    subtitle("NAS: file system + storage live together in a dedicated device, shared by many "
             "machines over the network.", 60, 96, width=900)

    for i, a in enumerate(["Application 1", "Application 2", "Application 3"]):
        box(80, 190 + i * 130, 180, 80, a)

    dashed_group(650, 175, 360, 350, "NAS Device")
    box(680, 215, 300, 70, "File System")
    arrow_down(830, 285, 40)
    database(700, 335, 260, 150, "Storage\n(HDD array, RAID)", fill=WHITE, stroke=ACC)

    # network file access
    arrow(260, 230, 650, 255, color=MID)
    arrow(260, 360, 650, 360, color=MID)
    arrow(260, 490, 650, 465, color=MID)
    text("Network file access (NFS / SMB)", 455, 205, size=12, color=MID,
         align="center", anchor="ct")

    box(80, 560, 430, 70,
        "Downside: centralized storage is a single point of failure.",
        size=13, fill=CON, stroke=BDR)
    text("Best for small-scale business data shared across many machines.",
         80, 660, size=13, color=MID)
    save("Network Attached Storage")


# ---------------------------------------------------------------- Storage Area Network
def san():
    new()
    title("Storage Area Network", 60, 40)
    subtitle("SAN: the file system stays with the application; only raw data blocks travel over a "
             "dedicated network. Multiple storage servers keep redundant copies.",
             60, 96, width=1020)

    for i in range(3):
        box(70, 190 + i * 140, 210, 100, "Application %d\n(+ File System)" % (i + 1))

    box(340, 250, 150, 270, "SAN Fabric\n(network)", fill=CON, stroke=INK)
    for i in range(3):
        arrow(280, 240 + i * 140, 340, 290 + i * 95, color=MID)
    text("raw data blocks", 415, 228, size=12, color=MID, align="center", anchor="ct")

    dashed_group(560, 160, 430, 470, "Redundant Storage Servers — fault tolerant")
    for i in range(3):
        storage(600, 200 + i * 140, 200, 110, "Storage Server %d" % (i + 1))
    arrow(490, 285, 600, 255, color=MID)
    arrow(490, 390, 600, 395, color=MID)
    arrow(490, 495, 600, 535, color=MID)

    # data replicated between servers
    arrow_bidir(830, 255, 830, 395, color=ACC, dash=True)
    arrow_bidir(830, 395, 830, 535, color=ACC, dash=True)
    text("data replicated", 845, 325, size=12, color=ACC)

    text("If a server fails, data is still available from the redundant storage servers.",
         70, 650, size=13, color=MID)
    save("Storage Area Network")


# ---------------------------------------------------------------- Persistent & transient cloud storage
def persistent_transient():
    new()
    title("Persistent & Transient Cloud Storage", 60, 40)
    subtitle("Cloud DAS = disks directly attached to compute instances: a transient local disk "
             "plus a persistent disk that survives the instance.", 60, 96, width=1000)

    dashed_group(80, 165, 1350, 480,
                 "Cloud provider — compute instances with directly attached disks")

    vm(120, 220, 190, 120, "Compute\nInstance 1")
    vm(120, 380, 190, 120, "Compute\nInstance 2")

    database(380, 225, 170, 140, "Persistent Disk\n(HDD / SSD)", fill=WHITE, stroke=ACC)
    rect(370, 395, 190, 130, fill="transparent", stroke=MID, dash=True)
    database(380, 400, 170, 120, "Transient Disk\n(local SSD)", fill=CON, stroke=MID)

    arrow(310, 285, 380, 300, color=INK)
    arrow(310, 440, 380, 450, color=INK)
    text("directly attached", 350, 355, size=11, color=MID, align="center", anchor="cm")

    # persistent disk replicated across AZs / regions
    dashed_group(620, 210, 780, 380,
                 "Persistent disk replicated & resized across AZs / regions")
    arrow(550, 300, 620, 305, color=ACC, dash=True)
    for i, r in enumerate(["Replica — AZ 2", "Replica — Region 2", "Replica — Region 3"]):
        database(660 + i * 250, 290, 190, 140, r)
        if i:
            arrow_bidir(850 + (i - 1) * 250, 360, 660 + i * 250, 360, color=ACC, dash=True)

    text("Transient disk: wiped when the instance stops.", 120, 615, size=13, color=MID)
    text("Persistent disk: data remains after the instance is decommissioned; multiple VMs can share it.",
         560, 615, size=13, color=MID)
    save("Persistent & transient cloud storage")


# ---------------------------------------------------------------- Distributed Object Storage In The Cloud
def distributed_object_storage():
    new()
    title("Distributed Object Storage In The Cloud", 60, 40)
    subtitle("Objects (a unique key + metadata) are grouped into pools and spread across clusters "
             "and regions for availability. Accessed over REST APIs.", 60, 96, width=1020)

    person(90, 260, "Developer", scale=0.9)
    arrow_right(170, 300, 120, "REST API")
    acc_box(300, 255, 190, 90, "Object\nStorage API")

    dashed_group(560, 165, 920, 440, "Cloud Object Store")
    text("Objects — each with a unique key + its own metadata", 600, 192, size=13, color=MID)
    for i in range(4):
        document(600 + i * 210, 225, 170, 100, "Object\nid + metadata", size=12)

    for i, r in enumerate(["Region 1", "Region 2", "Region 3"]):
        dashed_group(590 + i * 270, 390, 230, 180, r)
        storage(615 + i * 270, 435, 180, 110, "Object Pool")

    arrow(490, 300, 560, 300)
    for i in range(3):
        arrow(680 + i * 210, 325, 705 + i * 270, 435, color=MID, dash=True)

    text("Objects are spread across clusters and regions for scalability, high availability and disaster recovery.",
         80, 640, size=13, color=MID)
    save("Distributed Object Storage In The Cloud")


# ---------------------------------------------------------------- YouTube Architecture
def youtube():
    new()
    title("YouTube Architecture", 60, 40)
    subtitle("Popular content is served from the CDN; less popular content comes from the YouTube "
             "backend. Raw video files live in object storage, metadata in MySQL.",
             60, 96, width=1060)

    mobile(80, 200, 130, 200, "Mobile Client")
    browser(80, 440, 190, 150, "Web Client")

    box(300, 195, 210, 100, "CDN Server\n(popular content)")
    acc_box(300, 380, 230, 140, "Application Server\n(Microservices)\nYouTube Backend", size=14)

    arrow(210, 260, 300, 240, color=INK)
    text("popular", 255, 232, size=11, color=MID, align="center", anchor="cb")
    arrow(210, 360, 300, 430, color=INK)
    text("less popular", 245, 412, size=11, color=MID, align="center", anchor="cb")
    arrow(270, 470, 300, 460, color=INK)

    # backend reads/writes
    box(600, 210, 210, 150, "MySQL\n(users, metadata,\npreferences)", size=13)
    database(600, 400, 210, 150, "Object Storage\n(raw video files)", fill=WHITE, stroke=ACC)
    box(880, 400, 220, 90, "Object Storage API\n(on Google BigTable)", size=13)
    storage(880, 520, 220, 120, "Warehouse-scale\nHDDs (GFS)", size=13)

    arrow(530, 455, 600, 455, color=INK)
    text("read / write", 565, 485, size=11, color=MID, align="center", anchor="ct")
    arrow(530, 400, 600, 300, color=INK)
    text("metadata queries", 545, 322, size=11, color=MID, align="center", anchor="cb")
    arrow(410, 380, 410, 300, color=MID, dash=True)
    text("cache popular", 418, 342, size=11, color=MID)

    arrow(810, 465, 880, 445, color=INK)
    arrow_down(990, 490, 30, "GFS")

    text("Raw video data → HDDs (GFS); relationship data & metadata → MySQL / BigTable.",
         80, 660, size=13, color=MID)
    save("YouTube Architecture")


# ---------------------------------------------------------------- Database Component
def database_component():
    new()
    title("Database Component", 60, 40)
    subtitle("A database component = database software that manages the raw data + the physical "
             "storage that holds the raw bytes.", 60, 96, width=1000)

    box(80, 280, 190, 100, "Web Application")
    arrow_right(270, 330, 100, "queries")

    dashed_group(420, 175, 520, 400, "Database Component")
    acc_box(450, 215, 460, 110,
            "Database Software (DBMS)\nmanages data · queries · transactions", size=14)
    arrow_bidir(680, 325, 680, 415, color=INK)
    storage(450, 415, 460, 120, "Physical Data Storage (HDD / SSD)")

    text("Data storage = raw data kept on physical storage.", 980, 240, size=13, color=MID)
    text("Database software = manages that raw data.", 980, 282, size=13, color=MID)
    text("Both together make the database\ncomponent of a web application.",
         980, 345, size=13, color=INK)
    save("Database Component")


# ---------------------------------------------------------------- Object Storage In Buckets
def object_storage_buckets():
    new()
    title("Object Storage In Buckets", 60, 40)
    subtitle("Objects of any format are stored in buckets. A project can hold many buckets; "
             "buckets isolate objects and control access.", 60, 96, width=1020)

    person(90, 275, "Developer", scale=0.9)
    arrow_right(170, 315, 120, "REST API / SDK")

    dashed_group(340, 165, 1120, 470, "Project")

    for bi, (name, stroke, fill) in enumerate([("Bucket: Videos", ACC, WHITE),
                                               ("Bucket: Photos", BDR, CON),
                                               ("Bucket: Backups", BDR, CON)]):
        bx = 380 + bi * 360
        rect(bx, 215, 320, 380, fill=fill, stroke=stroke)
        text(name, bx + 160, 240, size=14, align="center", anchor="ct", color=INK)
        for oi in range(4):
            document(bx + 25 + (oi % 2) * 150, 275 + (oi // 2) * 150,
                     130, 110, "object\nkey + version", size=11)

    text("Object identity = bucket + key + version", 380, 650, size=13, color=INK)
    text("Buckets enable access management, encryption, versioning and object isolation.",
         380, 685, size=13, color=MID)
    save("Object Storage In Buckets")


if __name__ == "__main__":
    devops()
    das()
    nas()
    san()
    persistent_transient()
    distributed_object_storage()
    youtube()
    database_component()
    object_storage_buckets()
    print("wrote 9 scenes")
