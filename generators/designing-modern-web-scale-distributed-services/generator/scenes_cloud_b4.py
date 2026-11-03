#!/usr/bin/env python3
"""Cloud Computing 101 — batch b4 scenes (meaning-driven, ekit style)."""
from ekit import *


# ---------------------------------------------------------------- local helper
def bar(x, y, w, h, label, size=15, fill=CON, stroke=INK, color=INK):
    """A wide labelled layer bar used by the stack diagrams."""
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", color=color)


# ================================================================ 1. Edge Network
def edge_network():
    new()
    title("Edge Network", 60, 40)
    subtitle("Business logic moves to the drone and the edge node, so alarms fire instantly "
             "instead of a round-trip to the origin data center.", 60, 96, width=940)

    dashed_group(70, 175, 430, 400, "Premises / Edge Location")
    acc_box(100, 220, 220, 90, "AI Drone\n(detects movement,\nruns detection on-device)",
            size=12)
    box(100, 370, 220, 80, "Alarm triggered\n(immediate, no latency)",
        fill=WHITE, stroke=ACC, size=13)
    arrow(210, 312, 210, 368, color=ACC)
    server(350, 240, 150, 190, "Edge Node\n(local compute)", size=13)
    arrow(320, 265, 350, 265, color=MID)

    dashed_group(660, 175, 560, 400, "Cloud Data Center")
    server(720, 235, 180, 180, "Origin Servers\n(heavy processing)", size=13)
    database(960, 255, 180, 175, "Origin\nData Store")
    arrow(900, 320, 960, 320)

    arrow(500, 360, 720, 360, color=MID, dash=True)
    text("streams only data it cannot process locally", 610, 338, size=11,
         color=MID, align="center", anchor="cm", width=230)

    text("Moving compute to the drone and the edge cuts latency, improves response time, "
         "and reduces load on the origin data center.", 80, 600, size=13, color=INK, width=1180)
    save("Edge Network")


# ================================================= 2. Cloud Computing Infrastructure Stack
def infra_stack():
    new()
    title("Cloud Computing Infrastructure Stack", 60, 40)
    subtitle("Layers stacked from raw hardware up to the applications that end users interact with.",
             60, 96, width=880)

    person(480, 150, "End Users Of The Application")
    arrow_down(480, 235, 30, color=MID)

    rect(200, 270, 620, 100, fill=WHITE, stroke=ACC)
    text("Application Software", 510, 288, size=15, anchor="cm")
    text("MMO Game · Food Delivery App · Banking App", 510, 318, size=12,
         color=MID, anchor="cm")

    rect(200, 390, 620, 100, fill=CON, stroke=BDR)
    text("Cluster Infrastructure", 510, 408, size=15, anchor="cm")
    text("Apache Zookeeper · Google File System · Bigtable · Hadoop · Spanner", 510, 438,
         size=11, color=MID, anchor="cm", width=590)
    text("distributed systems managing the cluster of nodes", 840, 408, size=11, color=MID)

    rect(200, 510, 620, 100, fill=CON, stroke=BDR)
    text("Platform Software", 510, 528, size=15, anchor="cm")
    text("Operating System · Device Drivers · Firmware", 510, 558, size=12,
         color=MID, anchor="cm")

    rect(200, 630, 620, 100, fill=CON, stroke=BDR)
    text("Physical Infrastructure", 510, 648, size=15, anchor="cm")
    text("Compute Servers · Storage (HDD / SSD) · RAM · Data Center Network", 510, 678,
         size=11, color=MID, anchor="cm", width=590)

    save("Cloud Computing Infrastructure Stack")


# ================================================================ 3. Single & Multi-Tenant
def single_multi_tenant():
    new()
    title("Single & Multi-Tenant", 60, 40)
    subtitle("Single tenant = one business owns the server; multi-tenant = many businesses share "
             "the same hardware, isolated from each other.", 60, 96, width=940)

    dashed_group(70, 175, 470, 430, "Single Tenant")
    box(140, 235, 200, 70, "Business A")
    arrow_down(240, 305, 45)
    server(140, 360, 200, 150, "Server\n(dedicated)", size=13)
    arrow_down(240, 510, 30)
    database(140, 550, 200, 95, "Database")
    text("Dedicated / isolated resources", 305, 665, size=12, color=MID, anchor="cm")

    dashed_group(660, 175, 760, 430, "Multi-Tenant")
    box(700, 225, 180, 60, "Business A", size=13)
    box(920, 225, 180, 60, "Business B", size=13)
    box(1140, 225, 180, 60, "Business C", size=13)

    rect(700, 345, 620, 130, fill=CON, stroke=INK)
    text("Shared Server (CPU · memory · network)", 1010, 360, size=12,
         color=MID, anchor="cm")
    box(720, 385, 180, 70, "Application A", size=12, fill=WHITE)
    box(920, 385, 180, 70, "Application B", size=12, fill=WHITE)
    box(1120, 385, 180, 70, "Application C", size=12, fill=WHITE)
    arrow(790, 285, 790, 383, color=MID)
    arrow(1010, 285, 1010, 383, color=MID)
    arrow(1230, 285, 1230, 383, color=MID)

    arrow_down(1010, 475, 30)
    database(880, 515, 240, 100, "Shared Database")
    text("Businesses share resources, isolated from each other", 1040, 665, size=12,
         color=MID, anchor="cm")
    save("Single & Multi-Tenant")


# ============================================ 4. Product Search Software as a Service
def product_search_saas():
    new()
    title("Product Search Software as a Service", 60, 40)
    subtitle("Multiple e-commerce sites plug into one third-party search SaaS that stores and "
             "serves all of their inventory.", 60, 96, width=940)

    person(180, 160, "End User")
    browser(60, 245, 240, 115, "E-comm. Website A")
    browser(60, 400, 240, 115, "E-comm. Website B")

    dashed_group(660, 175, 620, 470, "Third-Party SaaS Provider (Multi-Tenant)")
    box(720, 235, 500, 85, "Product Search SaaS Application", size=15, fill=WHITE, stroke=ACC)
    database(800, 370, 340, 220, "Shared Inventory Database\n(Clients A & B Data)")
    arrow_down(970, 320, 50, color=MID)

    arrow(300, 300, 700, 275)
    text("stream inventory data", 500, 270, size=11, color=MID, anchor="cm")
    arrow(300, 455, 700, 320)
    text("product search query", 500, 405, size=11, color=MID, anchor="cm")
    arrow(700, 345, 300, 470, color=MID, dash=True)
    text("search results", 500, 440, size=11, color=MID, anchor="cm")

    text("Multiple businesses share the same SaaS application, database, OS and hardware.",
         80, 610, size=13, color=INK, width=1180)
    save("Product Search Software as a Service")


# ================================================================ 5. Noisy Neighbour
def noisy_neighbour():
    new()
    title("Noisy Neighbour", 60, 40)
    subtitle("When one workload on a shared machine hogs the resources, every other tenant on "
             "it slows down.", 60, 96, width=900)

    dashed_group(120, 180, 800, 380, "Shared Server (Multi-Tenant)")
    acc_box(170, 245, 200, 115, "Application 1\n(eats all resources)", size=13)
    box(430, 245, 200, 115, "Application 2\n(starved, low throughput)", size=12)
    box(690, 245, 200, 115, "Application 3\n(starved, low throughput)", size=12)
    box(170, 460, 720, 70, "Shared CPU · Memory · Network Bandwidth", size=13)
    arrow(270, 362, 270, 458, color=ACC, w=4)
    arrow(500, 362, 500, 458, color=MID)
    arrow(760, 362, 760, 458, color=MID)
    text("hogs all resources", 285, 405, size=11, color=ACC, anchor="lm")

    box(975, 220, 320, 300, "", fill=CON)
    text("Mitigations", 1135, 255, size=15, anchor="cm")
    text("• Overprovision the hardware\n• Kill the noisy tenant's processes\n"
         "• Monitor application performance\n• Use isolated bare-metal servers",
         1005, 295, size=12, color=MID)
    arrow(920, 370, 975, 370, color=MID)

    text("One workload hogging shared resources degrades every other tenant on the same machine.",
         80, 610, size=13, color=INK, width=1180)
    save("Noisy Neighbour")


# ================================================================ 6. Hypervisor
def hypervisor():
    new()
    title("Hypervisor", 60, 40)
    subtitle("A hypervisor on a bare-metal server splits its resources into isolated virtual "
             "machines (VMs).", 60, 96, width=880)

    text("Guests", 970, 275, size=13, color=MID, anchor="lm")
    vm(140, 200, 230, 150, "VM 1\nApp + Guest OS", size=12)
    vm(410, 200, 230, 150, "VM 2\nApp + Guest OS", size=12)
    vm(680, 200, 230, 150, "VM 3\nApp + Guest OS", size=12)

    bar(140, 400, 770, 70, "Hypervisor (Virtual Machine Monitor)", fill=WHITE, stroke=ACC)
    bar(140, 510, 770, 90, "Bare Metal Server — Host\n(CPU · RAM · Storage · Network)", size=14)

    arrow(255, 400, 255, 352, color=MID)
    arrow(525, 400, 525, 352, color=MID)
    arrow(795, 400, 795, 352, color=MID)
    text("resource split", 545, 378, size=11, color=MID, anchor="lm")
    text("host", 970, 555, size=13, color=MID, anchor="lm")

    text("The hypervisor splits the host's physical resources across isolated VMs.", 80, 640,
         size=13, color=INK, width=1180)
    save("Hypervisor")


# ================================================================ 7. Hypervisor Types
def hypervisor_types():
    new()
    title("Hypervisor Types", 60, 40)
    subtitle("Type 1 (native) runs directly on the hardware; Type 2 (hosted) runs on top of a "
             "host operating system.", 60, 96, width=880)

    dashed_group(70, 175, 600, 440, "Native Hypervisor (Type 1)")
    vm(100, 215, 160, 110, "VM 1", size=12)
    vm(280, 215, 160, 110, "VM 2", size=12)
    vm(460, 215, 160, 110, "VM 3", size=12)
    bar(100, 355, 520, 60, "Native Hypervisor", fill=WHITE, stroke=ACC)
    bar(100, 445, 520, 80, "Bare Metal Server")
    text("Runs directly on the hardware — no OS.\nBest performance.", 100, 545,
         size=12, color=MID)

    dashed_group(730, 175, 620, 440, "Hosted Hypervisor (Type 2)")
    vm(760, 215, 160, 110, "VM 1", size=12)
    vm(940, 215, 160, 110, "VM 2", size=12)
    vm(1120, 215, 160, 110, "VM 3", size=12)
    bar(760, 355, 520, 55, "Hosted Hypervisor", fill=WHITE, stroke=ACC)
    bar(760, 425, 520, 55, "Host Operating System")
    bar(760, 495, 520, 60, "Bare Metal Server")
    text("Runs on the host OS — adds latency,\nbut broad hardware compatibility.", 760, 575,
         size=12, color=MID)

    text("Trade-off: performance (Type 1) versus hardware compatibility (Type 2).", 70, 650,
         size=13, color=INK, width=1180)
    save("Hypervisor Types")


# ================================================================ 8. Container Technology
def container_technology():
    new()
    title("Container Technology", 60, 40)
    subtitle("A container bundles the app with its dependencies into one unit that runs the same "
             "in every environment.", 60, 96, width=940)

    person(150, 165, "Developer")
    document(80, 285, 220, 140, "Application Code")
    arrow_right(300, 355, 75, "build image")

    acc_box(400, 285, 240, 140, "Container Image\n\nApp code · dependencies ·\nconfiguration · libraries",
            size=12)

    dashed_group(720, 175, 680, 470, "Any Environment")
    box(760, 240, 260, 110, "Developer Laptop\n(same container)", size=12, fill=WHITE)
    box(1060, 240, 260, 110, "Pre-production\n(same container)", size=12, fill=WHITE)
    box(760, 400, 260, 110, "Public Cloud\n(same container)", size=12, fill=WHITE)
    text("Works identically — no environment-specific errors.", 1050, 560, size=12,
         color=MID, anchor="cm", width=340)

    arrow(640, 320, 760, 295, color=MID)
    arrow(640, 355, 1060, 295, color=MID)
    arrow(640, 390, 760, 455, color=MID)

    text("One standard unit of software runs consistently across public cloud, on-prem, "
         "and a developer's laptop.", 80, 610, size=13, color=INK, width=1180)
    save("Container Technology")


# ================================================================ 9. Containerized Applications
def containerized_applications():
    new()
    title("Containerized Applications", 60, 40)
    subtitle("Containers run on a container engine over a shared host OS, which makes them "
             "lightweight.", 60, 96, width=900)

    container(150, 195, 220, 130, "App A")
    container(410, 195, 220, 130, "App B")
    container(670, 195, 220, 130, "App C")

    bar(150, 385, 740, 60, "Container Engine (Docker)", fill=WHITE, stroke=ACC)
    bar(150, 475, 740, 60, "Host Operating System")
    bar(150, 565, 740, 80, "Bare Metal Server (CPU · RAM · Storage · Network)", size=14)
    text("lightweight — containers\nshare the host OS kernel", 930, 470, size=12, color=MID)

    text("The container engine runs many isolated containers on top of one host operating system.",
         80, 675, size=13, color=INK, width=1180)
    save("Containerized Applications")


# ================================================================ 10. Containers & VMs
def containers_vms():
    new()
    title("Containers & VMs", 60, 40)
    subtitle("VMs provide an abstraction at the hardware level; containers provide an abstraction "
             "at the operating system level.", 60, 96, width=940)

    dashed_group(70, 175, 600, 430, "Virtual Machines (hardware-level abstraction)")
    vm(100, 215, 160, 120, "VM 1\nGuest OS", size=12)
    vm(280, 215, 160, 120, "VM 2\nGuest OS", size=12)
    vm(460, 215, 160, 120, "VM 3\nGuest OS", size=12)
    bar(100, 365, 520, 55, "Hypervisor")
    bar(100, 445, 520, 70, "Bare Metal Server")
    text("Each VM has its own OS · more secure\nboot: seconds to minutes", 100, 540,
         size=12, color=MID)

    dashed_group(730, 175, 620, 430, "Containers (OS-level abstraction)")
    container(760, 215, 150, 120, "App A")
    container(930, 215, 150, 120, "App B")
    container(1100, 215, 150, 120, "App C")
    bar(760, 365, 510, 55, "Container Engine (Docker)", fill=WHITE, stroke=ACC)
    bar(760, 445, 510, 70, "Host Operating System")
    bar(760, 530, 510, 60, "Bare Metal Server")
    text("Containers share one OS kernel · lightweight\nboot: milliseconds", 760, 620,
         size=12, color=MID)

    text("Both technologies are used together: containers are lighter and faster, VMs give "
         "stronger isolation.", 70, 660, size=13, color=INK, width=1180)
    save("Containers & VMs")


# ==================================== 11. Container Running In A Virtual Machine
def container_in_vm():
    new()
    title("Container Running In A Virtual Machine", 60, 40)
    subtitle("Containers can run inside VMs — most Kubernetes deployments do exactly this.",
             60, 96, width=900)

    dashed_group(140, 170, 800, 320, "Virtual Machines (guests)")
    rect(160, 200, 360, 270, fill="transparent", stroke=INK)
    text("VM 1", 172, 208, size=14)
    container(190, 240, 130, 120, "App A")
    container(340, 240, 130, 120, "App B")
    bar(180, 400, 320, 50, "Guest OS", size=13)

    rect(580, 200, 360, 270, fill="transparent", stroke=INK)
    text("VM 2", 592, 208, size=14)
    container(610, 240, 130, 120, "App A")
    container(760, 240, 130, 120, "App B")
    bar(600, 400, 320, 50, "Guest OS", size=13)

    bar(140, 510, 800, 60, "Hypervisor", fill=WHITE, stroke=ACC)
    bar(140, 590, 800, 80, "Bare Metal Server", size=14)
    text("Each VM still needs its own\nOS and disk space.", 960, 250, size=12, color=MID)

    text("Most Kubernetes deployments run containers on VMs.", 80, 700,
         size=13, color=INK, width=1180)
    save("Container Running In A Virtual Machine")


# ============================== 12. Microservices Architecture: Social Network Application
def microservices_social():
    new()
    title("Microservices Architecture: Social Network Application", 60, 40)
    subtitle("Every social-network feature is a separate containerized service with its own "
             "database, reached through an API gateway.", 60, 96, width=1020)

    person(100, 310, "End User")
    acc_box(220, 305, 150, 80, "API Gateway", size=14)
    arrow(140, 345, 220, 345)

    dashed_group(400, 180, 900, 380, "Social Network Application — Microservices")
    box(430, 215, 180, 110, "Photo Upload\nService", size=13, fill=WHITE)
    box(650, 215, 180, 110, "User Tagging\nService", size=13, fill=WHITE)
    box(870, 215, 180, 110, "User Groups\nService", size=13, fill=WHITE)
    box(1090, 215, 180, 110, "Recommendation\nService", size=13, fill=WHITE)

    arrow(370, 325, 430, 285, color=MID)
    arrow(370, 335, 650, 285, color=MID)
    arrow(370, 345, 870, 285, color=MID)
    arrow(370, 355, 1090, 285, color=MID)

    database(450, 420, 140, 110, "Photos DB")
    database(670, 420, 140, 110, "Tags DB")
    database(890, 420, 140, 110, "Groups DB")
    database(1110, 420, 140, 110, "Recs DB")
    arrow_down(520, 325, 95, color=MID)
    arrow_down(740, 325, 95, color=MID)
    arrow_down(960, 325, 95, color=MID)
    arrow_down(1180, 325, 95, color=MID)

    text("Each microservice is deployed as a container and owns its own database.", 80, 620,
         size=13, color=INK, width=1180)
    save("Microservices Architecture Social Network Application")


if __name__ == "__main__":
    edge_network()
    infra_stack()
    single_multi_tenant()
    product_search_saas()
    noisy_neighbour()
    hypervisor()
    hypervisor_types()
    container_technology()
    containerized_applications()
    containers_vms()
    container_in_vm()
    microservices_social()
    print("wrote 12 scenes")
