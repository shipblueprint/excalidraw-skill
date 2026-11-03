#!/usr/bin/env python3
"""Exemplar scenes (Cloud) showing the intended meaning-driven style."""
from ekit import *


def auto_scaling():
    new()
    title("Auto Scaling In The Cloud", 60, 40)
    subtitle("Servers are added on a traffic surge and removed when traffic subsides — "
             "automatically, with no human intervention.", 60, 96, width=760)

    # left: the workload
    box(60, 190, 170, 90, "Workload")
    browser(60, 320, 170, 110, "Website")

    # auto scale policy
    box(300, 210, 170, 70, "Auto Scale Policy", fill=WHITE, stroke=ACC)
    arrow(230, 235, 300, 240)

    # the autoscaling group
    dashed_group(540, 150, 620, 300, "Auto Scaling Group")
    arrow(470, 245, 540, 245)
    running = ["Node 1", "Node 2", "Node 3"]
    for i, n in enumerate(running):
        server(560 + i * 130, 210, 110, 120, n)
    for i, n in enumerate(["Node 4", "Node 5", "Node 6"]):
        rect(560 + i * 130, 360, 110, 120, fill="transparent", stroke=BDR, dash=True)
        text(n + "\n(spun up)", 615 + i * 130, 420, size=12, align="center", anchor="cm", color=MID)

    text("Minimum 3 nodes always running", 560, 480, size=12, color=MID)
    text("Buffer nodes activated only during a surge", 860, 480, size=12, color=MID)
    curved(1010, 195, [[0, 0], [40, -60], [0, -90]], color=ACC, head="arrow")
    text("+ on demand", 1050, 120, size=13, color=ACC)
    save("Auto Scaling In The Cloud")


def kubernetes():
    new()
    title("Kubernetes Cluster", 60, 40)
    subtitle("Containers run in pods on nodes; every node is managed by the master node (the leader).",
             60, 96, width=780)

    master = box(400, 160, 220, 80, "Master Node\n(leader / control plane)", fill=WHITE, stroke=ACC)

    arrow_down(510, 240, 70)
    dashed_group(80, 330, 900, 260, "Kubernetes Cluster")
    for i in range(3):
        x = 120 + i * 290
        box(x, 370, 240, 190, "", fill="transparent", stroke=BDR)
        text("Node " + str(i + 1), x + 12, 378, size=15, color=INK)
        for j in range(2):
            px = x + 20 + j * 110
            box(px, 410, 96, 130, "", fill=WHITE, stroke=INK)
            text("Pod " + str(j + 1), px + 48, 418, size=12, align="center", anchor="ct")
            for k in range(2):
                container(px + 14, 445 + k * 40, 68, 28, "ctr")
    for i in range(3):
        x = 240 + i * 290
        arrow(510, 240, x, 370, dash=True, color=MID)
    save("Kubernetes Cluster")


def mmo():
    new()
    title("My Online MMO Game Architecture", 60, 40)
    subtitle("Deployed on Google App Engine (PaaS): React front end, Java/Spring Boot backend, "
             "Cloud Datastore, and a task queue for async work.", 60, 96, width=860)

    mobile(80, 210, 120, 200, "Game Client")
    arrow_right(200, 300, 110, "HTTPS")

    browser(330, 200, 200, 150, "GAE Front End\nService (React)")
    arrow_right(530, 275, 80)

    box(630, 195, 220, 160, "Backend Service\n(Java, Spring Boot)", fill=WHITE, stroke=ACC)
    arrow_right(850, 250, 90)
    database(970, 200, 130, 150, "Cloud\nDatastore")

    arrow_down(740, 355, 90, "async events")
    queue(650, 465, 180, 70, "Task Queue\n(notifications, jobs)")

    person(160, 470, "Player", scale=0.9)
    save("Online MMO Game Architecture")


if __name__ == "__main__":
    auto_scaling()
    kubernetes()
    mmo()
    print("wrote 3 exemplar scenes")
