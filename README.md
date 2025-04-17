# 🚀 Backend CI/CD Deployment with Jenkins, Docker & GitHub Webhook

This setup uses Jenkins to automatically build and deploy the backend application using Docker whenever code is pushed to the GitHub repository.

---

## 🐳 Docker Network

Make sure the shared Docker network is created (run only once):

```bash
docker network create myapp
```f
## 🔧 Jenkins Job Setup (backend)

    Go to Jenkins:
    http://51.21.244.204:8080/job/backend/configure

    Enable Trigger

        Under Build Triggers:

    [x] GitHub hook trigger for GITScm polling

---

## Source Code Management

    GitHub repository URL

    Credentials (if private)

    Branch: */main or your desired branch
---

## Build Steps
Under Build > Execute shell:
```bash
    docker stop backend || true
    docker rm backend || true
    docker build -t backend .
    docker run -d --name=backend --network=myapp -p 3000:3000 backend
```
---

 ## 🔁 GitHub Webhook Setup

In your backend GitHub repo:

    Go to Settings → Webhooks → Add webhook

    Fill in:

        Payload URL:

http://51.21.244.204:8080/github-webhook/

Content type:
```bash
application/json
```

SSL verification:
```bash
Disable (since using HTTP)
```
Event:
```bash
        Just the push event
```

    Click Add Webhook
---

## ✅ Test It

    Push changes to your backend repo

    Jenkins will auto-trigger a build

    Docker will redeploy the updated backend on port 5000