#!/usr/bin/env python3
"""
Batch 5 scenes — Microservices deployment with containers, CI/CD pipeline and
continuous monitoring, drawn meaning-first with ekit.
"""
from ekit import *


# ------------------------------------------------------------------ 1.52
def deploying_containers():
    new()
    title("Deploying A Service In Containers", 60, 40)
    subtitle("A developer containerizes a microservice into a Docker image, pushes it to a "
             "registry, and the same image is run as a container in every environment.",
             60, 96, width=900)

    person(120, 220, "Developer")
    box(240, 230, 180, 90, "Build Container Image\n(code, dependencies, config)", size=12)
    arrow(420, 275, 480, 275)
    text("build & push", 450, 258, size=11, color=MID, align="center", anchor="cb")

    # registry — the reusable template (highlighted)
    rect(480, 180, 240, 430, fill=WHITE, stroke=ACC, rx=True)
    text("Image Registry\n(public / private)", 600, 200, size=12, align="center", anchor="ct")
    for i in range(3):
        rect(508, 252 + i * 46, 184, 34, fill=CON, stroke=INK, rx=True)
        text("app-image:v" + str(i + 1), 600, 269 + i * 46, size=10, align="center", anchor="cm")
    text("images are templates that\ncan be reused later", 600, 402, size=10, color=MID,
         align="center", anchor="ct")

    envs = [("Environment 1  (Test)", "runs the microservice"),
            ("Environment 2  (Pre-Production)", "same image, no rebuild"),
            ("Environment 3  (Production)", "identical artifacts")]
    for i, (label, cap) in enumerate(envs):
        gy = 200 + i * 150
        dashed_group(790, gy, 400, 130, label)
        container(810, gy + 25, 110, 80, "container")
        text(cap, 1010, gy + 65, size=11, color=MID, align="center", anchor="cm")
        arrow(720, gy + 65, 790, gy + 65, dash=True, color=MID)

    save("Deploying A Service In Containers")


# ------------------------------------------------------------------ 1.53
def primary_ways():
    new()
    title("Primary Ways Of Running & Deploying Applications On The Cloud", 60, 40)
    subtitle("An application runs directly on bare metal, inside a virtual machine, or in "
             "containers on either of them.", 60, 96, width=940)

    panels = [
        (50, "Running Apps In Virtual Machines"),
        (550, "Running An App Directly On Bare Metal"),
        (1050, "Running Applications In Containers"),
    ]
    for x, label in panels:
        dashed_group(x, 180, 400, 440, label)
        box(x + 20, 480, 360, 55, "Host Operating System", size=13)
        box(x + 10, 545, 380, 60, "Bare Metal Server", size=13)

    # panel 1 — VMs
    x = 50
    for j, vname in enumerate(["VM 1", "VM 2"]):
        vx = x + 30 + j * 175
        vm(vx, 230, 160, 200, "")
        text(vname, vx + 80, 300, size=13, align="center", anchor="cm")
        text("App", vx + 80, 350, size=12, color=MID, align="center", anchor="cm")

    # panel 2 — direct on bare metal
    x = 550
    box(x + 90, 240, 220, 190, "", fill=WHITE, stroke=INK)
    text("App", x + 200, 310, size=16, align="center", anchor="cm")
    text("(directly on the OS)", x + 200, 355, size=11, color=MID, align="center", anchor="cm")

    # panel 3 — containers (highlighted: the course's focus)
    x = 1050
    for j, name in enumerate(["App A", "App B", "App C"]):
        container(x + 25 + j * 125, 250, 105, 130, name, stroke=ACC)
    text("share the host OS kernel", x + 200, 420, size=11, color=MID, align="center", anchor="cm")

    text("Containers can also run inside a VM, combining both approaches.", 50, 640,
         size=12, color=MID)
    save("Primary Ways Of Running & Deploying Applications On The Cloud")


# ------------------------------------------------------------------ 1.54
def multiple_microservices():
    new()
    title("Multiple Microservices Per Host", 60, 40)
    subtitle("Many containerized microservices share one host — efficient use of resources, but "
             "they can interfere (the noisy neighbour problem).", 60, 96, width=980)

    dashed_group(150, 190, 980, 430, "Host  (Bare Metal Server or Virtual Machine)")

    services = [
        ("Photo Service", "C++"),
        ("Post Service", "Java"),
        ("User Service", "Go"),
        ("Live Stream", "Python"),
        ("Notification", "Ruby on Rails"),
        ("Search", "Node.js"),
    ]
    for i, (name, stack) in enumerate(services):
        cx = 190 + (i % 3) * 300
        cy = 225 + (i // 3) * 160
        container(cx, cy, 200, 110, name, size=13)
        text(stack, cx + 100, cy + 110 + 34, size=10, color=MID, align="center", anchor="ct")

    rect(170, 545, 940, 45, fill=CON, stroke=INK, rx=True)
    text("Host Operating System", 640, 567, size=13, align="center", anchor="cm")

    text("One host runs many\ncontainerized services", 1150, 240, size=13, color=INK)
    text("• services written in\ndifferent stacks coexist", 1150, 310, size=12, color=MID)
    text("• containers isolate each\nservice from the host", 1150, 380, size=12, color=MID)
    text("Downside: noisy neighbour", 1150, 460, size=13, color=ACC)
    text("busy containers compete\nfor the same host resources", 1150, 490, size=11, color=MID)

    save("Multiple Microservices Per Host")


# ------------------------------------------------------------------ 1.55
def single_microservice():
    new()
    title("Single Microservice Per Host", 60, 40)
    subtitle("One microservice per host: it gets 100% of the host resources and there is no noisy "
             "neighbour — but hosts multiply quickly.", 60, 96, width=980)

    hosts = [
        (50, "Host 1 – Photo Service (C++)"),
        (520, "Host 2 – Post Service (Java)"),
        (990, "Host 3 – User Service (Go)"),
    ]
    for x, name in hosts:
        dashed_group(x, 180, 400, 420, name)
        container(x + 105, 230, 190, 130, "", stroke=ACC)
        text(name.split("– ")[1].split(" (")[0], x + 200, 295, size=13, align="center", anchor="cm")
        text("100% of host resources", x + 200, 400, size=11, color=MID, align="center", anchor="cm")
        box(x + 20, 425, 360, 50, "Host OS", size=13)
        box(x + 10, 485, 380, 60, "Bare Metal Server", size=13)

    text("No noisy neighbour and 100% resource access, but many hosts mean more infrastructure "
         "to manage — which is where container orchestration comes in.",
         50, 630, size=12, color=MID, width=1300)
    save("Single Microservices Per Host")


# ------------------------------------------------------------------ 1.56
def container_orchestration():
    new()
    title("Container Orchestration", 60, 40)
    subtitle("An orchestrator schedules containers across many hosts, scales them, balances traffic "
             "and keeps them healthy — Kubernetes, Docker Swarm, Mesos.", 60, 96, width=980)

    acc_box(520, 160, 460, 80, "Container Orchestrator\n(Kubernetes · Docker Swarm · Mesos)", size=14)

    person(90, 330, "User")
    arrow(140, 370, 200, 370)
    box(200, 325, 160, 90, "Load Balancer", size=14)
    arrow(280, 415, 280, 470)
    text("routes traffic", 288, 455, size=11, color=MID, anchor="lm")

    dashed_group(180, 470, 1100, 190, "Cluster — hosts across regions, AZs & data centers")

    hosts = [(230, "Host 1 (AZ-A)"), (620, "Host 2 (AZ-B)"), (1010, "Host 3 (AZ-C)")]
    for hx, hlabel in hosts:
        rect(hx, 500, 300, 150, fill="transparent", stroke=BDR, rx=True)
        text(hlabel, hx + 150, 512, size=12, align="center", anchor="ct")
        for k in range(3):
            container(hx + 20 + k * 90, 540, 70, 90, "")
        arrow(750, 240, hx + 150, 500, dash=True, color=MID)

    text("Capabilities: autoscaling · load balancing · resource allocation · health monitoring · "
         "ensuring availability · portability across clouds.", 180, 675, size=12, color=MID, width=1100)
    save("Container Orchestration")


# ------------------------------------------------------------------ 1.59
def infrastructure_as_code():
    new()
    title("Infrastructure As Code", 60, 40)
    subtitle("Instead of configuring hardware by hand, the infrastructure is defined in code and "
             "provisioned automatically — repeatable and far less error-prone.", 60, 96, width=1000)

    # manual approach (before)
    person(120, 240, "Engineer")
    arrow_down(120, 320, 30)
    box(40, 355, 220, 90, "Manually configure\neach machine", size=12, fill="transparent", stroke=BDR)
    arrow(150, 445, 150, 480)
    server(60, 480, 180, 110, "Machine", size=13)
    text("slow · error-prone · inconsistent", 40, 610, size=11, color=MID)

    # infrastructure as code (the fix)
    dashed_group(430, 170, 640, 470, "Infrastructure As Code")
    document(460, 215, 180, 110, "Infra Config\n(version controlled)", size=12)
    arrow(640, 270, 710, 270)
    box(710, 225, 220, 90, "Provisioning Tool\n(Terraform / CloudFormation)",
        size=12, fill=WHITE, stroke=ACC)
    arrow_down(860, 315, 75)
    dashed_group(460, 390, 580, 220, "Same config → consistent environments")
    for i, env in enumerate(["Dev", "Staging", "Production"]):
        server(480 + i * 170, 440, 150, 110, env, size=13)

    text("Automated, repeatable infrastructure removes manual configuration — and the human "
         "errors it invites.", 60, 660, size=12, color=MID, width=1200)
    save("Infrastructure As Code")


# ------------------------------------------------------------------ 1.60
def code_deployment_workflow():
    new()
    title("Code Deployment Workflow", 60, 40)
    subtitle("The deployment pipeline: code flows from the developer's laptop through build, tests "
             "and QA into staging and finally production.", 60, 96, width=1000)

    person(80, 300, "Developer")
    arrow(120, 340, 170, 340)
    box(170, 295, 150, 90, "Remote Code\nRepository (GitHub)", size=12)
    arrow(320, 340, 370, 340)
    text("git push", 345, 325, size=11, color=MID, align="center", anchor="cb")

    dashed_group(370, 230, 330, 240, "Continuous Integration (Jenkins)")
    box(390, 260, 140, 60, "Build", size=13)
    box(545, 260, 140, 60, "Unit &\nIntegration Tests", size=11)
    text("• static code analysis", 390, 340, size=11, color=MID)
    text("• code quality & formatting", 390, 362, size=11, color=MID)
    text("• compliance checks", 390, 384, size=11, color=MID)

    arrow(700, 340, 740, 340)
    person(820, 190, "Tester")
    box(740, 295, 160, 90, "QA / Regression\nUAT", size=12)
    arrow(900, 340, 940, 340)
    box(940, 295, 150, 90, "Staging\nEnvironment", size=13)
    arrow(1090, 340, 1130, 340)
    text("verified", 1110, 325, size=11, color=MID, align="center", anchor="cb")
    acc_box(1130, 295, 170, 90, "Production\n(live)", size=13)

    text("Every stage gates the next: the pipeline delivers the commit to production efficiently, "
         "with minimal manual intervention.", 60, 510, size=12, color=MID, width=1200)
    save("Code Deployment Workflow")


# ------------------------------------------------------------------ 1.61
def continuous_integration():
    new()
    title("Continuous Integration Of Code", 60, 40)
    subtitle("Developers push small changes to a shared branch often; every push triggers an "
             "automated build and tests, so integration issues surface early.", 60, 96, width=1000)

    for i, dev in enumerate(["Dev A", "Dev B", "Dev C"]):
        person(110, 210 + i * 120, dev)
    box(340, 260, 220, 120, "Remote Repository\n(shared branch)", size=13)
    arrow(160, 250, 340, 290)
    arrow(160, 370, 340, 320)
    arrow(160, 490, 340, 350)

    arrow(560, 320, 660, 320)
    text("every push", 610, 305, size=11, color=MID, align="center", anchor="cb")
    acc_box(660, 250, 280, 140, "CI Server (Jenkins)\nBuild + run all tests", size=14)

    curved(800, 250, [[0, 0], [-320, -70], [-660, -30]], color=ACC, dash=True)
    text("fast feedback — fix issues early", 470, 175, size=12, color=ACC, align="center", anchor="cm")

    text("Frequent small commits avoid 'merge hell' and keep everyone in sync with the common "
         "branch.", 60, 560, size=12, color=MID, width=1100)
    save("Continuous Integration Of Code")


# ------------------------------------------------------------------ 1.62
def blue_green():
    new()
    title("Blue-Green Deployment", 60, 40)
    subtitle("Two identical production environments; deploy to the idle one, test it, then switch "
             "traffic to it — zero downtime.", 60, 96, width=940)

    person(80, 340, "End Users")
    arrow(130, 380, 180, 380)
    box(180, 335, 150, 95, "Load Balancer", size=14, fill=WHITE, stroke=ACC)

    dashed_group(450, 170, 560, 210, "Blue Environment — currently LIVE")
    box(480, 225, 500, 125, "App v1", size=15, fill=WHITE, stroke=INK)
    text("serving 100% of production traffic", 730, 362, size=11, color=ACC,
         align="center", anchor="cm")

    dashed_group(450, 470, 560, 210, "Green Environment — idle")
    box(480, 525, 500, 125, "App v2  (new version)", size=15, fill=WHITE, stroke=ACC)
    text("deployed & tested in isolation — no user impact", 730, 662, size=11, color=MID,
         align="center", anchor="cm")

    arrow(330, 370, 450, 290, color=INK)
    text("live traffic", 385, 305, size=11, color=INK, align="center", anchor="cb")
    arrow(330, 410, 450, 545, dash=True, color=MID)
    arrow_bidir(1020, 300, 1020, 560, color=ACC)
    text("switch traffic\nafter verification", 1040, 430, size=12, color=ACC, anchor="lm")

    text("One environment is live at a time: deploy to the idle one, test it, then flip the load "
         "balancer — zero downtime.", 60, 700, size=12, color=MID, width=1300)
    save("Blue-Green Deployment")


# ------------------------------------------------------------------ 1.63
def continuous_monitoring():
    new()
    title("Continuous Monitoring Stack", 60, 40)
    subtitle("Containers are monitored with cAdvisor, whose metrics stream into Prometheus (a "
             "time-series DB); Grafana turns them into dashboards.", 60, 96, width=1000)

    dashed_group(60, 220, 300, 330, "Docker Containers")
    for i in range(3):
        container(110, 265 + i * 90, 200, 70, "service " + str(i + 1), size=11)

    arrow(360, 385, 430, 385)
    text("container stats", 395, 370, size=11, color=MID, align="center", anchor="cb")
    box(430, 330, 240, 110, "cAdvisor", size=15)
    text("exposes container metrics\nas Prometheus metrics", 550, 450, size=11, color=MID,
         align="center", anchor="ct")

    arrow(670, 385, 740, 385)
    text("metrics", 705, 370, size=11, color=MID, align="center", anchor="cb")
    database(740, 300, 170, 170, "Prometheus\n(time-series DB)", size=13, stroke=ACC)

    arrow(910, 385, 980, 385)
    text("data source", 945, 370, size=11, color=MID, align="center", anchor="cb")
    box(980, 310, 250, 150, "Grafana\nDashboards", size=15, fill=WHITE, stroke=INK)
    text("charts, heatmaps, geo maps", 1105, 470, size=11, color=MID, align="center", anchor="ct")

    curved(1105, 300, [[0, 0], [-140, -80], [-280, -80]], color=ACC, dash=True)
    text("queries", 965, 200, size=11, color=ACC, align="center", anchor="cm")

    arrow(1230, 385, 1340, 385)
    person(1400, 330, "Developer / SRE")

    text("All container data flows cAdvisor → Prometheus → Grafana; dashboards query Prometheus as "
         "their data source.", 60, 590, size=12, color=MID, width=1200)
    save("Continuous Monitoring Stack")


# ------------------------------------------------------------------ 1.64
def elk_stack():
    new()
    title("ELK Stack", 60, 40)
    subtitle("Elastic Logstash Kibana: Logstash ingests logs from every component, standardizes "
             "them, stores them in Elasticsearch, and Kibana visualizes them.", 60, 96, width=1040)

    dashed_group(60, 190, 270, 440, "Application Components")
    for i, name in enumerate(["Application Server", "Web Server", "Database", "Message Server"]):
        box(80, 225 + i * 105, 230, 75, name, size=12)

    box(430, 330, 230, 130, "Logstash\n(data processing pipeline)", size=13)
    badge(447, 347, "L")
    for y in (262, 367, 472, 577):
        arrow(330, y, 430, 380, color=MID)
    text("logs in various formats", 335, 620, size=11, color=MID)

    arrow(660, 395, 740, 395)
    text("standardized", 700, 380, size=11, color=MID, align="center", anchor="cb")
    database(740, 320, 190, 170, "Elasticsearch\n(document store)", size=13, stroke=ACC)
    badge(757, 337, "E")

    arrow(930, 395, 1010, 395)
    text("indexed", 970, 380, size=11, color=MID, align="center", anchor="cb")
    box(1010, 320, 250, 150, "Kibana Dashboard\n(centralized log search)", size=13,
        fill=WHITE, stroke=INK)
    badge(1027, 337, "K")

    arrow(1260, 395, 1340, 395)
    person(1400, 340, "Developer")

    text("Optionally, a message queue (Kafka / RabbitMQ) can sit before Logstash to decouple "
         "ingestion.", 60, 660, size=12, color=MID, width=1200)
    save("ELK Stack")


if __name__ == "__main__":
    deploying_containers()
    primary_ways()
    multiple_microservices()
    single_microservice()
    container_orchestration()
    infrastructure_as_code()
    code_deployment_workflow()
    continuous_integration()
    blue_green()
    continuous_monitoring()
    elk_stack()
    print("wrote 11 scenes")
