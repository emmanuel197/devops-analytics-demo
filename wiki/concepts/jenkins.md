---
tags: [jenkins, ci-cd, devops]
status: done
phase: 1
updated: 2026-05-31
---

# Jenkins

## What it is
An automation server that runs a **pipeline** against your code (build, test,
deploy). Self-hosted — you run the Jenkins server yourself (here: a Docker
container). The pipeline is defined as code in a `Jenkinsfile` committed to the repo.

## How it maps to what I already know
GitHub Actions, stage for stage:

| GitHub Actions | Jenkins |
|---|---|
| `.github/workflows/deploy.yml` | `Jenkinsfile` |
| `jobs → steps` | `stages { stage { steps } }` |
| Runs on GitHub's runners | Runs on my Jenkins server |
| `on: push` | "Build Now" / SCM poll / webhook |

## Hands-on (what I built)
- Ran Jenkins LTS in Docker, with the **Docker CLI installed** + the host Docker
  socket mounted (`/var/run/docker.sock`) so the pipeline can build images
  ("Docker-out-of-Docker").
- Wrote a `Jenkinsfile` with 3 stages: **Checkout → Build image → Test**.
- Connected a Pipeline job to the GitHub repo ("Pipeline script from SCM").
- Build #1 green: image `taskboard:1` built + tagged, `Ran 4 tests ... OK`.

## Key commands / snippets
```bash
# start Jenkins (build image with Docker CLI + plugins, run with socket mount)
docker compose -f jenkins/docker-compose.yml up -d --build
# first-run unlock secret
docker exec jenkins-jenkins-1 cat /var/jenkins_home/secrets/initialAdminPassword
```
Pipeline test stage runs tests inside the freshly built image, using in-memory
SQLite (`DJANGO_TEST_SQLITE=1`) so no Postgres is needed in CI.

## Likely interview Q&A
- **Q: Jenkins vs GitHub Actions?** A: Same CI/CD concept; Jenkins is
  self-hosted/plugin-driven (full control, you maintain it), Actions is managed
  by GitHub. Jenkinsfile ≈ workflow yaml.
- **Q: How does a containerized Jenkins build images?** A: Mount the host Docker
  socket into the Jenkins container so its Docker CLI drives the host daemon.
- **Q: Declarative vs scripted pipeline?** A: I used declarative
  (`pipeline { stages { } }`) — structured and readable; scripted is full Groovy.
- **Q: How do you trigger builds?** A: Manual (Build Now), SCM polling, or a
  webhook from GitHub on push.

## Gotchas
- First-run **unlock password** is a bootstrap secret in
  `$JENKINS_HOME/secrets/initialAdminPassword` (+ echoed to logs) so only someone
  with host access can finish setup — prevents drive-by takeover.
- Default branch specifier is `*/master`; our repo is `main`.
- Harmless `No directory at: /app/staticfiles/` warning during tests (collectstatic
  not run in the test path).

See [[plan]] · next: [[concepts/prometheus-grafana]].
