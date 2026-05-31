# Jenkins LTS + the Docker CLI, so pipelines can build/run containers
# against the host Docker daemon (mounted socket).
FROM jenkins/jenkins:lts

USER root

# Install the Docker CLI (client only — it talks to the host daemon via the
# mounted /var/run/docker.sock).
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates curl gnupg lsb-release && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends docker-ce-cli docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/*

# Pre-install the plugins our Jenkinsfile needs (saves clicking through the
# plugin picker for these).
RUN jenkins-plugin-cli --plugins \
    workflow-aggregator \
    git \
    docker-workflow
