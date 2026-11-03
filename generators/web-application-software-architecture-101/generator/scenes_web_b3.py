#!/usr/bin/env python3
"""Batch b3 — Web Application & Software Architecture 101 diagrams."""
from ekit import *


# ---------------------------------------------------------------- 1
def horizontal_scalability():
    new()
    title("Horizontal scalability", 60, 40)
    subtitle("Scaling out: add more servers to the resource pool so the fleet as a whole "
             "handles the rising traffic.", 60, 96, width=860)
    line(720, 150, 720, 600, color=BDR, dash=True)

    text("Before", 80, 150, size=17)
    browser(80, 190, 180, 110, "Workload\n(Website)")
    arrow_right(260, 245, 60, "traffic")
    server(330, 175, 140, 160, "Server\n16 GB RAM")
    text("One server can be scaled only so far —\nit eventually hits a ceiling.", 80, 380,
         size=13, color=MID, width=280)

    text("After", 800, 150, size=17)
    browser(800, 190, 180, 110, "Workload\n(Website)")
    arrow_right(980, 245, 80, "traffic")
    dashed_group(1060, 155, 420, 300, "Server fleet")
    for i, x in enumerate([1075, 1210, 1345]):
        server(x, 200, 120, 150, "Server %d\n16 GB" % (i + 1))
    text("Total = 48 GB. Servers are added on a surge and\nremoved when traffic drops (cloud elasticity).",
         800, 480, size=13, color=MID, width=620)
    save("Horizontal scalability")


# ---------------------------------------------------------------- 2
def microservice_architecture():
    new()
    title("Microservice architecture", 60, 40)
    subtitle("A large application is split into small, independently deployable services — "
             "each owns its own data and scales on its own.", 60, 96, width=900)
    browser(70, 210, 160, 110, "User Interface\n(web / mobile)")
    arrow_right(230, 265, 90, "HTTPS")
    acc_box(330, 225, 190, 80, "API Gateway")
    dashed_group(560, 165, 880, 420, "Loosely-coupled microservices")
    for name, x in [("User Service", 600), ("Order Service", 840), ("Payment Service", 1080)]:
        box(x, 230, 190, 90, name, fill=WHITE, stroke=INK)
        arrow(520, 265, x + 5, 275, color=MID, dash=True)
        database(x + 25, 380, 140, 120, "DB")
        arrow_down(x + 95, 320, 55)
    text("Each service can be deployed and scaled independently; if one fails, the others stay up.",
         560, 545, size=13, color=MID, width=820)
    save("Microservice architecture")


# ---------------------------------------------------------------- 3
def app_monitoring():
    new()
    title("App monitoring architectural flow", 60, 40)
    subtitle("Containers expose metrics, Prometheus scrapes and stores them as time-series, "
             "and Grafana visualizes them on a dashboard.", 60, 96, width=940)
    dashed_group(70, 200, 300, 340, "Docker host")
    for i in range(3):
        container(95, 235 + i * 95, 250, 70, "app container %d" % (i + 1))
    arrow_right(410, 350, 50, "scrape")
    box(470, 305, 180, 95, "cAdvisor\n(metrics exporter)", fill=WHITE, stroke=INK)
    arrow_right(650, 352, 50)
    acc_box(710, 305, 190, 95, "Prometheus\n(time-series store)")
    arrow_right(900, 352, 50, "query")
    browser(960, 285, 300, 150, "Grafana Dashboard\n(web UI)")
    box(710, 460, 190, 80, "Alertmanager\n(alerts)", fill=CON, stroke=BDR)
    arrow_down(805, 400, 60, "rules")
    text("Tools like cAdvisor, Prometheus and Grafana profile the system via web dashboards.",
         470, 580, size=13, color=MID, width=820)
    save("App monitoring architectural flow")


# ---------------------------------------------------------------- 4
def microservice_architecture_2():
    new()
    title("Microservice architecture", 60, 40)
    subtitle("Fault tolerance (fail-soft): a failing feature degrades on its own while the "
             "rest of the application keeps running.", 60, 96, width=940)
    browser(60, 230, 150, 100, "User Interface")
    arrow_right(210, 280, 80, "HTTPS")
    acc_box(300, 240, 180, 80, "API Gateway")
    dashed_group(520, 160, 960, 430, "Independent microservices (own data)")
    svcs = [("Image Upload", 545, True), ("Comments", 775, False),
            ("Instant Messaging", 1005, False), ("Live Streaming", 1235, False)]
    for name, x, down in svcs:
        if down:
            box(x, 225, 205, 85, name + "\n(DOWN)", fill=WHITE, stroke=ACC)
        else:
            box(x, 225, 205, 85, name, fill=WHITE, stroke=INK)
        arrow(480, 280, x + 5, 265, color=MID, dash=True)
        database(x + 35, 375, 135, 115, "DB")
        arrow_down(x + 100, 310, 55)
    text("Only the failed feature is unavailable —\nusers can still comment, chat and stream.",
         60, 470, size=13, color=MID, width=430)
    save("Microservice architecture (2)")


# ---------------------------------------------------------------- 5
def ha_redundancy():
    new()
    title("HA - Redundancy", 60, 40)
    subtitle("Active–passive HA: standby (passive) nodes stay idle and take over the moment "
             "an active node goes down.", 60, 96, width=900)

    dashed_group(70, 175, 620, 400, "Active–Passive mode")
    box(95, 220, 160, 70, "Workload\n(Website)")
    arrow_right(255, 255, 55, "traffic")
    acc_box(330, 205, 200, 90, "Node A\n(active)")
    box(330, 320, 200, 80, "Node B\n(standby)", dash=True)
    box(330, 425, 200, 80, "Node C\n(standby)", dash=True)
    text("Active node serves the live\nrequests; standby nodes\nremain idle.", 95, 320,
         size=13, color=MID, width=220)

    dashed_group(730, 175, 600, 400, "On failure → failover")
    box(755, 220, 150, 70, "Workload\n(Website)")
    arrow_right(905, 255, 50, "traffic")
    box(975, 205, 200, 90, "Node A\n(DOWN)", fill=WHITE, stroke=ACC)
    acc_box(975, 360, 200, 90, "Node C\n(promoted → active)")
    arrow(1075, 300, 1075, 360, color=ACC, dash=True)
    text("takes over", 1085, 322, size=11, color=ACC)
    text("Standby takes over; when the failed node\nrecovers it becomes passive again.",
         755, 480, size=13, color=MID, width=560)
    save("HA - Redundancy")


# ---------------------------------------------------------------- 6
def ha_replication():
    new()
    title("HA - Replication", 60, 40)
    subtitle("Active–active HA: every node runs the workload and replicates data, so the load "
             "is shared and the service survives node loss.", 60, 96, width=940)

    dashed_group(70, 175, 620, 410, "Active–Active (all nodes serve)")
    box(95, 220, 150, 70, "Workload\n(Website)")
    arrow_right(245, 255, 45, "traffic")
    for i, (x, y) in enumerate([(320, 215), (475, 215), (320, 320), (475, 320)]):
        acc_box(x, y, 145, 80, "Node %d\n(active)" % (i + 1))
    line(465, 255, 475, 255, color=MID, dash=True)
    line(465, 360, 475, 360, color=MID, dash=True)
    line(392, 295, 392, 320, color=MID, dash=True)
    line(547, 295, 547, 320, color=MID, dash=True)
    text("Data is replicated across nodes,\nkeeping them in sync.", 95, 340,
         size=13, color=MID, width=230)

    dashed_group(730, 175, 600, 410, "Two nodes down → remaining share load")
    box(755, 220, 150, 70, "Workload\n(Website)")
    arrow_right(905, 255, 45, "traffic")
    for i, (x, y) in enumerate([(975, 215), (1130, 215), (975, 320), (1130, 320)]):
        if i >= 2:
            box(x, y, 145, 80, "Node %d\n(DOWN)" % (i + 1), fill=WHITE, stroke=ACC)
        else:
            acc_box(x, y, 145, 80, "Node %d\n(active)" % (i + 1))
    text("The service as a whole is still up.", 755, 470, size=13, color=MID, width=500)
    save("HA - Replication")


# ---------------------------------------------------------------- 7
def ha_clustering():
    new()
    title("HA clustering", 60, 40)
    subtitle("A fail-over cluster: nodes watch each other over a heartbeat network and keep "
             "one consistent state via shared memory.", 60, 96, width=940)
    dashed_group(110, 175, 1120, 460, "Highly Available Cluster")

    acc_box(535, 200, 260, 70, "Node Coordinator\n(ZooKeeper)")
    database(560, 320, 210, 110, "Shared Memory\n(distributed)")
    arrow_down(665, 270, 50, "coordination")

    for name, x in [("Node A", 140), ("Node B", 560), ("Node C", 980)]:
        server(x, 470, 200, 105, name)
    arrow(665, 430, 250, 472, color=MID, dash=True)
    arrow(665, 430, 665, 472, color=MID, dash=True)
    arrow(665, 430, 1075, 472, color=MID, dash=True)

    line(340, 522, 560, 522, color=MID, dash=True)
    line(760, 522, 980, 522, color=MID, dash=True)
    text("heartbeat network", 450, 498, size=12, color=MID)
    text("All nodes share one consistent application state.", 110, 655,
         size=13, color=MID, width=700)
    save("HA clustering")


# ---------------------------------------------------------------- 8
def load_balancing():
    new()
    title("Load balancing", 60, 40)
    subtitle("A load balancer is the single point of contact that spreads client traffic across "
             "the server cluster.", 60, 96, width=880)
    person(155, 165, "", scale=0.8)
    box(70, 250, 170, 80, "End Users\n(clients)")
    arrow_right(240, 290, 80, "requests")
    acc_box(330, 250, 200, 90, "Load Balancer")
    text("single point of contact", 330, 355, size=12, color=MID)
    for i, y in enumerate([170, 275, 380]):
        server(620, y, 190, 95, "Backend Server %d" % (i + 1))
        arrow(520, 295, 620, y + 47, color=MID)
    text("Traffic is spread across the cluster, so no single server is overloaded.",
         620, 520, size=13, color=MID, width=560)
    save("Load balancing")


# ---------------------------------------------------------------- 9
def load_balancing_components():
    new()
    title("Load balancing at different components", 60, 40)
    subtitle("Load balancers can sit in front of any component — application servers, databases, "
             "even queues — to spread load uniformly.", 60, 96, width=980)
    text("Application tier", 540, 150, size=13, color=MID)
    text("Database tier", 1030, 150, size=13, color=MID)

    box(70, 300, 150, 80, "End Users\n(clients)")
    arrow_right(220, 340, 70, "requests")
    acc_box(290, 300, 180, 80, "Load Balancer")
    for i, y in enumerate([180, 300, 420]):
        server(540, y, 170, 90, "App Server %d" % (i + 1))
        arrow(470, 340, 540, y + 45, color=MID)

    acc_box(790, 300, 180, 80, "Load Balancer")
    for i, y in enumerate([180, 300, 420]):
        arrow(710, y + 45, 790, 340, color=MID)
    for i, y in enumerate([175, 315, 455]):
        database(1030, y, 150, 110, "Database %d" % (i + 1))
        arrow(970, 340, 1030, y + 55, color=MID)

    text("The same pattern applies to a message queue or a cache cluster.",
         70, 610, size=13, color=MID, width=760)
    save("Load balancing at different components of the application")


# ---------------------------------------------------------------- 10
def health_checks():
    new()
    title("Health checks by load balancer", 60, 40)
    subtitle("The load balancer probes every node; only in-service machines receive traffic, "
             "down nodes are removed from the list.", 60, 96, width=940)
    acc_box(80, 300, 200, 100, "Load Balancer\n\"How are you feeling, buddy?\"", size=13)
    servers = [("Server 1\n(in-service)", 210, False),
               ("Server 2\n(in-service)", 360, False),
               ("Server 3\n(out-of-service)", 510, True)]
    for label, y, down in servers:
        if down:
            box(560, y, 220, 110, label, fill=WHITE, stroke=ACC)
        else:
            box(560, y, 220, 110, label, fill=CON, stroke=BDR)
    for label, y, down in servers:
        arrow(280, 350, 560, y + 55, color=MID, dash=True)
    arrow(280, 325, 560, 265, color=INK)
    arrow(280, 375, 560, 415, color=INK)
    text("health checks", 300, 235, size=12, color=MID)
    text("Only in-service nodes get live requests.", 560, 645, size=13, color=MID, width=540)
    save("Health checks by load balancer")


# ---------------------------------------------------------------- 11
def domain_name_system():
    new()
    title("Domain name system", 60, 40)
    subtitle("DNS maps easy-to-remember domain names (amazon.com) to the numeric IP addresses "
             "of machines.", 60, 96, width=900)
    browser(70, 200, 190, 130, "Browser\namazon.com")
    arrow_right(260, 265, 80, "query")
    cloud(470, 265, 200, 110, "DNS")
    arrow_right(590, 265, 80, "IP address")
    box(690, 205, 230, 120, "IP address\n2001:db8:0:1234::1", fill=WHITE, stroke=ACC)
    text("names → addresses", 470, 362, size=12, color=MID, width=200)

    dashed_group(70, 400, 1200, 250, "Four key components of the DNS infrastructure")
    comps = [("DNS Resolver\n(recursive)", 100), ("Root\nNameserver", 400),
             ("Top-Level Domain\nNameserver (.com)", 700),
             ("Authoritative\nNameserver (amazon.com)", 1000)]
    for name, x in comps:
        box(x, 460, 240, 100, name, size=13, fill=WHITE, stroke=INK)
    for x in (340, 640, 940):
        arrow_right(x, 510, 60)
    save("Domain name system")


# ---------------------------------------------------------------- 12
def dns_lookup():
    new()
    title("DNS query lookup process", 60, 40)
    subtitle("Resolving amazon.com: the resolver walks Root → TLD → Authoritative nameservers, "
             "caches the result and returns the IP to the client.", 60, 96, width=1000)
    browser(60, 300, 150, 130, "Client\n(browser)")
    acc_box(280, 315, 200, 100, "DNS Resolver\n(recursive)")

    server(700, 170, 260, 90, "Root Nameserver")
    server(700, 320, 260, 90, "Top-Level Domain\nNameserver (.com)")
    server(700, 470, 260, 90, "Authoritative\nNameserver (amazon.com)")

    arrow(210, 370, 280, 370)
    badge(245, 345, 1)
    arrow(280, 410, 210, 410, color=ACC, dash=True)
    badge(245, 440, 8)

    arrow(480, 330, 700, 215)
    badge(600, 262, 2)
    arrow(700, 235, 480, 345, color=ACC, dash=True)
    badge(600, 300, 3)

    arrow(480, 360, 700, 365)
    badge(600, 350, 4)
    arrow(700, 385, 480, 375, color=ACC, dash=True)
    badge(600, 400, 5)

    arrow(480, 400, 700, 505)
    badge(600, 462, 6)
    arrow(700, 525, 480, 415, color=ACC, dash=True)
    badge(600, 488, 7)

    text("1. Client sends DNS query to the resolver\n"
         "2. Resolver asks the root nameserver\n"
         "3. Root returns the TLD nameserver address\n"
         "4. Resolver asks the .com TLD nameserver\n"
         "5. TLD returns the authoritative name server\n"
         "6. Resolver asks the authoritative server\n"
         "7. Authoritative returns amazon.com's IP\n"
         "8. Resolver caches and returns the IP to the client",
         1010, 190, size=12, color=INK, width=470)
    text("Blue = replies", 1010, 470, size=12, color=ACC)
    text("Dark = queries", 1010, 500, size=12, color=INK)
    save("DNS query lookup process")


if __name__ == "__main__":
    horizontal_scalability()
    microservice_architecture()
    app_monitoring()
    microservice_architecture_2()
    ha_redundancy()
    ha_replication()
    ha_clustering()
    load_balancing()
    load_balancing_components()
    health_checks()
    domain_name_system()
    dns_lookup()
    print("wrote 12 b3 scenes")
