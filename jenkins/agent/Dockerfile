FROM jenkins/inbound-agent:latest

USER root

# Встановлення інструментів для збірки
RUN apt-get update && apt-get install -y \
    build-essential \
    rpm \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Виправлення: /home/jenkins/agent/workspace/count-files-pipeline@tmp/durable-0d54e212/script.sh.copy: 1: docker: not found
RUN curl -fsSL https://get.docker.com | sh

USER jenkins
