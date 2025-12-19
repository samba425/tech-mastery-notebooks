# 🐳 Docker Zero to Hero - Complete Course

A comprehensive course covering Docker from basics to advanced topics with concise concepts and practical examples.

---

## 📚 Table of Contents

1. [Introduction and Installation](#part-1-introduction-and-installation)
2. [Docker Images](#part-2-docker-images)
3. [Containers](#part-3-containers)
4. [Dockerfile](#part-4-dockerfile)
5. [Docker Compose](#part-5-docker-compose)
6. [Networking](#part-6-networking)
7. [Volumes and Storage](#part-7-volumes-and-storage)
8. [Registry](#part-8-registry)
9. [Security](#part-9-security)
10. [Advanced Topics](#part-10-advanced-topics)

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BEGINNER                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 01. Intro    │───▶│ 02. Images   │───▶│ 03. Contain  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      INTERMEDIATE                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 04. Dockerf  │───▶│ 05. Compose  │───▶│ 06. Network  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        ADVANCED                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 07. Volumes  │───▶│ 08. Registry │───▶│ 09. Security │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                  │                   │
│                                                  ▼                   │
│                                          ┌──────────────┐           │
│                                          │ 10. Advanced │           │
│                                          └──────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
```

---

# Part 1: Introduction and Installation

## What is Docker?

Docker is a platform for developing, shipping, and running applications in containers. Containers package an application with all its dependencies, ensuring consistent behavior across different environments.

## Why Docker?

Docker solves the "it works on my machine" problem by providing isolated, reproducible environments. It enables faster deployments, better resource utilization, and simplified DevOps workflows.

### Key Benefits

| Benefit | Description |
|---------|-------------|
| **Portability** | Run anywhere Docker is installed |
| **Consistency** | Same environment from dev to prod |
| **Isolation** | Applications don't interfere with each other |
| **Efficiency** | Lighter than VMs, share OS kernel |
| **Speed** | Start containers in seconds |
| **Scalability** | Easy to scale horizontally |

## Docker Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DOCKER ARCHITECTURE                         │
│                                                                     │
│   ┌─────────────────┐          ┌─────────────────────────────────┐ │
│   │  Docker Client  │          │        Docker Host              │ │
│   │                 │          │                                  │ │
│   │  docker build   │◀────────▶│  Docker Daemon (dockerd)        │ │
│   │  docker pull    │  REST    │                                  │ │
│   │  docker run     │  API     │  ┌─────────────────────────────┐│ │
│   │                 │          │  │       Containers            ││ │
│   └─────────────────┘          │  │  ┌─────┐ ┌─────┐ ┌─────┐   ││ │
│                                │  │  │ App │ │ DB  │ │ Web │   ││ │
│                                │  │  └─────┘ └─────┘ └─────┘   ││ │
│                                │  └─────────────────────────────┘│ │
│                                │                                  │ │
│                                │  ┌─────────────────────────────┐│ │
│                                │  │         Images              ││ │
│                                │  │  nginx | postgres | node    ││ │
│                                │  └─────────────────────────────┘│ │
│                                └─────────────────────────────────┘ │
│                                           │                        │
│                                           │ pull/push              │
│                                           ▼                        │
│                                ┌─────────────────────┐             │
│                                │   Docker Registry   │             │
│                                │   (Docker Hub)      │             │
│                                └─────────────────────┘             │
└─────────────────────────────────────────────────────────────────────┘
```

## Containers vs Virtual Machines

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│        Virtual Machines                    Containers               │
│   ┌─────────────────────────┐    ┌─────────────────────────┐      │
│   │ ┌─────┐ ┌─────┐ ┌─────┐│    │ ┌─────┐ ┌─────┐ ┌─────┐│      │
│   │ │App A│ │App B│ │App C││    │ │App A│ │App B│ │App C││      │
│   │ └─────┘ └─────┘ └─────┘│    │ └─────┘ └─────┘ └─────┘│      │
│   │ ┌─────┐ ┌─────┐ ┌─────┐│    │ ┌─────────────────────┐│      │
│   │ │Bins │ │Bins │ │Bins ││    │ │       Docker        ││      │
│   │ │Libs │ │Libs │ │Libs ││    │ │       Engine        ││      │
│   │ └─────┘ └─────┘ └─────┘│    │ └─────────────────────┘│      │
│   │ ┌─────┐ ┌─────┐ ┌─────┐│    │ ┌─────────────────────┐│      │
│   │ │Guest│ │Guest│ │Guest││    │ │      Host OS        ││      │
│   │ │ OS  │ │ OS  │ │ OS  ││    │ └─────────────────────┘│      │
│   │ └─────┘ └─────┘ └─────┘│    │ ┌─────────────────────┐│      │
│   │ ┌─────────────────────┐│    │ │    Infrastructure   ││      │
│   │ │     Hypervisor      ││    │ └─────────────────────┘│      │
│   │ └─────────────────────┘│    └─────────────────────────┘      │
│   │ ┌─────────────────────┐│                                     │
│   │ │       Host OS       ││         Lightweight                 │
│   │ └─────────────────────┘│         Fast startup                │
│   │ ┌─────────────────────┐│         Share OS kernel             │
│   │ │    Infrastructure   ││                                     │
│   │ └─────────────────────┘│                                     │
│   └─────────────────────────┘                                     │
│         Heavy, slow startup                                        │
│         Full OS per VM                                             │
└─────────────────────────────────────────────────────────────────────┘
```

| Feature | Virtual Machines | Containers |
|---------|-----------------|------------|
| **Size** | Gigabytes | Megabytes |
| **Startup** | Minutes | Seconds |
| **OS** | Full OS per VM | Shared kernel |
| **Isolation** | Complete | Process-level |
| **Performance** | Near native | Native |

## Installing Docker

### Ubuntu/Debian

```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add user to docker group (avoid using sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker run hello-world
```

### macOS

```bash
# Download Docker Desktop from docker.com
# Or use Homebrew
brew install --cask docker

# Start Docker Desktop from Applications
# Verify installation
docker --version
docker run hello-world
```

### Windows

1. Enable WSL 2 (Windows Subsystem for Linux)
2. Download Docker Desktop from docker.com
3. Run installer and follow prompts
4. Restart computer
5. Verify: `docker --version`

## Your First Docker Container

```bash
# Run hello-world
docker run hello-world

# Run nginx web server
docker run -d -p 8080:80 nginx
# Visit http://localhost:8080

# Run interactive Ubuntu
docker run -it ubuntu /bin/bash
```

---

# Part 2: Docker Images

## What are Docker Images?

Docker images are read-only templates containing the application, dependencies, and instructions for creating containers. They're built in layers, where each layer represents a set of changes.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        IMAGE LAYERS                                 │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │  Layer 5: Application Code        (Your app)                │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 4: npm install             (Dependencies)            │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 3: Node.js                 (Runtime)                 │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 2: apt-get update/install  (System packages)         │  │
│   ├─────────────────────────────────────────────────────────────┤  │
│   │  Layer 1: Ubuntu 22.04            (Base OS)                 │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│   Each layer is cached and reusable across images                  │
└─────────────────────────────────────────────────────────────────────┘
```

## Working with Images

### Listing Images

```bash
# List local images
docker images

# List with specific format
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# List all images (including intermediate)
docker images -a

# Filter images
docker images --filter "dangling=true"
```

### Pulling Images

```bash
# Pull latest tag
docker pull nginx

# Pull specific tag
docker pull nginx:1.24

# Pull from specific registry
docker pull gcr.io/google-containers/nginx:latest

# Pull all tags
docker pull -a nginx
```

### Image Tags

```bash
# Tag an image
docker tag nginx:latest myregistry.com/nginx:v1.0

# Tag for Docker Hub
docker tag myapp:latest username/myapp:v1.0
```

### Removing Images

```bash
# Remove specific image
docker rmi nginx:latest

# Remove by image ID
docker rmi 605c77e624dd

# Force remove
docker rmi -f nginx:latest

# Remove all unused images
docker image prune

# Remove all images
docker rmi $(docker images -q)
```

## Image Inspection

```bash
# Full image details
docker inspect nginx:latest

# Get specific field
docker inspect --format='{{.Config.Cmd}}' nginx

# View layers
docker history nginx:latest
docker history --no-trunc nginx:latest
```

## Building Images

```bash
# Build from Dockerfile
docker build -t myapp:v1.0 .

# Build with different Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build with build arguments
docker build --build-arg VERSION=1.0 -t myapp .

# Build without cache
docker build --no-cache -t myapp .
```

---

# Part 3: Containers

## What are Containers?

Containers are runnable instances of Docker images. They provide isolated environments with their own filesystem, networking, and process space, but share the host kernel.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      IMAGE vs CONTAINER                             │
│                                                                     │
│   ┌─────────────────────┐         ┌─────────────────────────────┐  │
│   │      IMAGE          │         │        CONTAINER            │  │
│   │  (Read-only)        │────────▶│   (Read-Write Layer)        │  │
│   │                     │  run    │                             │  │
│   │  ┌───────────────┐  │         │  ┌───────────────────────┐  │  │
│   │  │ Application   │  │         │  │  Writable Layer      │  │  │
│   │  ├───────────────┤  │         │  │  (Container Changes) │  │  │
│   │  │ Dependencies  │  │         │  ├───────────────────────┤  │  │
│   │  ├───────────────┤  │         │  │  Image Layers        │  │  │
│   │  │ Base OS       │  │         │  │  (Read-only)         │  │  │
│   │  └───────────────┘  │         │  └───────────────────────┘  │  │
│   │                     │         │                             │  │
│   │  Template           │         │  Running Instance          │  │
│   └─────────────────────┘         └─────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Running Containers

### Basic Run

```bash
# Run container (foreground)
docker run nginx

# Run detached (background)
docker run -d nginx

# Run with name
docker run -d --name webserver nginx

# Run interactive
docker run -it ubuntu /bin/bash

# Run and auto-remove on exit
docker run --rm nginx
```

### Port Mapping

```bash
# Map host:container ports
docker run -d -p 8080:80 nginx

# Map multiple ports
docker run -d -p 8080:80 -p 8443:443 nginx

# Map to specific interface
docker run -d -p 127.0.0.1:8080:80 nginx

# Random host port
docker run -d -P nginx
```

### Environment Variables

```bash
# Set environment variable
docker run -d -e MYSQL_ROOT_PASSWORD=secret mysql

# Multiple variables
docker run -d \
  -e DB_HOST=localhost \
  -e DB_PORT=5432 \
  myapp

# From file
docker run -d --env-file ./env.list myapp
```

## Container Lifecycle

```bash
# Start stopped container
docker start container_name

# Stop running container
docker stop container_name

# Restart container
docker restart container_name

# Pause container
docker pause container_name

# Unpause container
docker unpause container_name

# Kill container (SIGKILL)
docker kill container_name
```

## Container Management

### Listing Containers

```bash
# Running containers
docker ps

# All containers
docker ps -a

# Latest container
docker ps -l

# Container IDs only
docker ps -q
```

### Removing Containers

```bash
# Remove stopped container
docker rm container_name

# Force remove running container
docker rm -f container_name

# Remove all stopped containers
docker container prune

# Remove all containers
docker rm -f $(docker ps -aq)
```

## Executing Commands

```bash
# Execute command in running container
docker exec container_name ls -la

# Interactive shell
docker exec -it container_name /bin/bash

# Execute as root
docker exec -u root container_name whoami

# Execute with environment variable
docker exec -e VAR=value container_name printenv
```

## Container Logs

```bash
# View logs
docker logs container_name

# Follow logs
docker logs -f container_name

# Last N lines
docker logs --tail 100 container_name

# With timestamps
docker logs -t container_name

# Since specific time
docker logs --since 2023-01-01 container_name
```

## Container Stats

```bash
# Real-time stats
docker stats

# Specific container
docker stats container_name

# No streaming
docker stats --no-stream
```

---

# Part 4: Dockerfile

## What is a Dockerfile?

A Dockerfile is a text file containing instructions to build a Docker image. Each instruction creates a layer in the image, and Docker caches these layers for faster builds.

## Dockerfile Instructions

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image to build upon |
| `WORKDIR` | Set working directory |
| `COPY` | Copy files from host to image |
| `ADD` | Copy files (with URL/tar support) |
| `RUN` | Execute commands during build |
| `ENV` | Set environment variables |
| `EXPOSE` | Document exposed ports |
| `CMD` | Default command to run |
| `ENTRYPOINT` | Configure container executable |
| `ARG` | Build-time variables |
| `VOLUME` | Create mount point |
| `USER` | Set user for commands |
| `LABEL` | Add metadata |

## Basic Dockerfile

```dockerfile
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]
```

## Dockerfile Best Practices

### Optimize Layer Caching

```dockerfile
# Good: Dependencies first, then code
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
CMD ["npm", "start"]

# Bad: Everything together (cache broken on any change)
FROM node:18-alpine
COPY . /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]
```

### Reduce Image Size

```dockerfile
# Good: Alpine base + cleanup
FROM python:3.11-alpine
RUN apk add --no-cache gcc musl-dev \
    && pip install --no-cache-dir package \
    && apk del gcc musl-dev

# Good: Specific packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    package1 \
    package2 \
    && rm -rf /var/lib/apt/lists/*
```

### Security Practices

```dockerfile
# Create non-root user
FROM node:18-alpine
RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -D appuser
USER appuser
WORKDIR /app
COPY --chown=appuser:appgroup . .
```

## Multi-Stage Builds

Multi-stage builds create smaller, more secure images by separating build and runtime environments.

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

## Building Images

```bash
# Build image
docker build -t myapp:v1 .

# Build with build args
docker build --build-arg NODE_ENV=production -t myapp:prod .

# Build from specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build without cache
docker build --no-cache -t myapp:v1 .

# Build with target stage
docker build --target builder -t myapp:builder .
```

---

# Part 5: Docker Compose

## What is Docker Compose?

Docker Compose is a tool for defining and running multi-container applications. It uses a YAML file to configure services, networks, and volumes.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      DOCKER COMPOSE                                 │
│                                                                     │
│   docker-compose.yml                                               │
│   ┌──────────────────────────────────────────────────────────────┐ │
│   │                                                              │ │
│   │  services:                                                   │ │
│   │    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │ │
│   │    │   web       │  │    api      │  │     db      │       │ │
│   │    │  (nginx)    │──│  (node)     │──│  (postgres) │       │ │
│   │    └─────────────┘  └─────────────┘  └─────────────┘       │ │
│   │          │                │                │                │ │
│   │          └────────────────┼────────────────┘                │ │
│   │                           │                                  │ │
│   │  networks:               │                                  │ │
│   │    ┌──────────────────────▼──────────────────────┐         │ │
│   │    │              app-network                     │         │ │
│   │    └─────────────────────────────────────────────┘         │ │
│   │                                                              │ │
│   │  volumes:                                                    │ │
│   │    ┌────────────┐  ┌────────────┐                          │ │
│   │    │  db-data   │  │  uploads   │                          │ │
│   │    └────────────┘  └────────────┘                          │ │
│   │                                                              │ │
│   └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Basic docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - api

  api:
    build: ./api
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
      - DB_PORT=5432
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

## Compose Commands

```bash
# Start services
docker compose up

# Start in background
docker compose up -d

# Build and start
docker compose up --build

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# View logs
docker compose logs -f

# List containers
docker compose ps

# Execute command in service
docker compose exec api npm test

# Scale service
docker compose up -d --scale api=3
```

## Complete Application Example

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d myapp"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - backend

volumes:
  postgres-data:
  redis-data:

networks:
  default:
    name: myapp-network
```

---

# Part 6: Networking

## Docker Network Types

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DOCKER NETWORK DRIVERS                          │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                        BRIDGE                                │   │
│  │  Default network for containers on single host               │   │
│  │  Containers can communicate via container name               │   │
│  │                                                              │   │
│  │  ┌───────┐   ┌───────┐   ┌───────┐                         │   │
│  │  │ App A │───│Bridge │───│ App B │                         │   │
│  │  └───────┘   │Network│   └───────┘                         │   │
│  │              └───┬───┘                                      │   │
│  │                  │ NAT                                      │   │
│  │              ┌───▼───┐                                      │   │
│  │              │ Host  │                                      │   │
│  └──────────────└───────┘──────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                        HOST                                  │   │
│  │  Container uses host's network directly                      │   │
│  │  No network isolation, best performance                      │   │
│  │                                                              │   │
│  │  ┌───────┐                                                  │   │
│  │  │ App   │ → Uses host's IP:PORT directly                   │   │
│  │  └───────┘                                                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                       OVERLAY                                │   │
│  │  Multi-host networking for Docker Swarm                      │   │
│  │  Containers across hosts can communicate                     │   │
│  │                                                              │   │
│  │  Host A           Host B           Host C                   │   │
│  │  ┌─────┐          ┌─────┐          ┌─────┐                 │   │
│  │  │App 1│──────────│App 2│──────────│App 3│                 │   │
│  │  └─────┘          └─────┘          └─────┘                 │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

| Driver | Use Case |
|--------|----------|
| **bridge** | Default, isolated network on single host |
| **host** | No isolation, use host's network directly |
| **overlay** | Multi-host networking (Swarm) |
| **macvlan** | Assign MAC address, appear as physical device |
| **none** | Disable networking |

## Network Commands

```bash
# List networks
docker network ls

# Create network
docker network create mynetwork

# Create with driver
docker network create --driver bridge --subnet 172.20.0.0/16 mynetwork

# Inspect network
docker network inspect mynetwork

# Connect container to network
docker network connect mynetwork container_name

# Disconnect
docker network disconnect mynetwork container_name

# Remove network
docker network rm mynetwork

# Prune unused networks
docker network prune
```

## Container Communication

### Using Bridge Network

```bash
# Create network
docker network create app-network

# Run containers on same network
docker run -d --name api --network app-network myapi
docker run -d --name web --network app-network nginx

# Containers can reach each other by name
docker exec web ping api
docker exec web curl http://api:3000
```

### Docker Compose Networking

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    networks:
      - frontend-net
      - backend-net

  api:
    build: ./api
    networks:
      - backend-net

  db:
    image: postgres
    networks:
      - backend-net

networks:
  frontend-net:
  backend-net:
    internal: true  # No external access
```

---

# Part 7: Volumes and Storage

## Docker Storage Types

```
┌─────────────────────────────────────────────────────────────────────┐
│                      DOCKER STORAGE TYPES                           │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │                    NAMED VOLUMES                               ││
│  │  Managed by Docker, persistent, recommended for production     ││
│  │                                                                ││
│  │  docker run -v myvolume:/app/data myapp                        ││
│  │                                                                ││
│  │  Host: /var/lib/docker/volumes/myvolume/_data                  ││
│  │                          │                                     ││
│  │                          ▼                                     ││
│  │  Container:          /app/data                                 ││
│  └────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │                    BIND MOUNTS                                 ││
│  │  Direct mapping from host to container, good for development   ││
│  │                                                                ││
│  │  docker run -v /host/path:/container/path myapp                ││
│  │                                                                ││
│  │  Host:      /home/user/project                                 ││
│  │                    │                                           ││
│  │                    ▼                                           ││
│  │  Container:     /app                                           ││
│  └────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │                    TMPFS MOUNTS                                ││
│  │  Stored in memory, not persisted, good for sensitive data      ││
│  │                                                                ││
│  │  docker run --tmpfs /app/temp myapp                            ││
│  │                                                                ││
│  │  Memory ──▶ /app/temp                                          ││
│  └────────────────────────────────────────────────────────────────┘│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Volume Commands

```bash
# List volumes
docker volume ls

# Create volume
docker volume create myvolume

# Inspect volume
docker volume inspect myvolume

# Remove volume
docker volume rm myvolume

# Remove unused volumes
docker volume prune
```

## Using Volumes

### Named Volumes

```bash
# Create and use named volume
docker run -d \
  --name db \
  -v postgres-data:/var/lib/postgresql/data \
  postgres

# Volume syntax
docker run -v volume_name:/container/path image
```

### Bind Mounts

```bash
# Mount current directory
docker run -d \
  -v $(pwd):/app \
  -w /app \
  node:18 npm start

# Mount specific path
docker run -d \
  -v /host/config:/etc/app/config:ro \
  myapp

# Read-only mount
docker run -v /data:/data:ro myapp
```

### tmpfs Mounts

```bash
# Memory-only mount
docker run -d \
  --tmpfs /app/temp:rw,size=100m \
  myapp
```

## Docker Compose Volumes

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - db-data:/var/lib/postgresql/data        # Named volume
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro  # Bind mount

  app:
    build: .
    volumes:
      - .:/app                                   # Bind mount (development)
      - node_modules:/app/node_modules          # Named volume (exclude)
      - /app/temp                               # Anonymous volume

volumes:
  db-data:
    driver: local
  node_modules:
```

---

# Part 8: Registry

## What is Docker Registry?

A Docker Registry is a storage and distribution system for Docker images. Docker Hub is the default public registry, but you can use private registries for proprietary images.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      REGISTRY FLOW                                  │
│                                                                     │
│   Developer                  Registry                Production    │
│   Machine                                            Server         │
│                                                                     │
│   ┌─────────┐   docker push   ┌───────────┐   docker pull          │
│   │  Build  │ ───────────────▶│  Docker   │◀─────────────────┐    │
│   │  Image  │                 │  Registry │                  │    │
│   └─────────┘                 │           │            ┌─────────┐ │
│                               │ ┌───────┐ │            │  Run    │ │
│                               │ │ myapp │ │            │  Image  │ │
│                               │ │ :v1.0 │ │            └─────────┘ │
│                               │ └───────┘ │                        │
│                               └───────────┘                        │
└─────────────────────────────────────────────────────────────────────┘
```

## Docker Hub

### Login and Push

```bash
# Login to Docker Hub
docker login

# Tag for Docker Hub
docker tag myapp:v1.0 username/myapp:v1.0

# Push to Docker Hub
docker push username/myapp:v1.0

# Pull from Docker Hub
docker pull username/myapp:v1.0
```

### Public vs Private

```bash
# Public image (anyone can pull)
docker push username/public-app:v1.0

# Private image (requires auth)
docker push username/private-app:v1.0
```

## Private Registry

### Run Local Registry

```bash
# Start registry container
docker run -d -p 5000:5000 --name registry registry:2

# Tag for local registry
docker tag myapp:v1.0 localhost:5000/myapp:v1.0

# Push to local registry
docker push localhost:5000/myapp:v1.0

# Pull from local registry
docker pull localhost:5000/myapp:v1.0
```

### Registry with Docker Compose

```yaml
version: '3.8'

services:
  registry:
    image: registry:2
    ports:
      - "5000:5000"
    volumes:
      - registry-data:/var/lib/registry
    environment:
      REGISTRY_STORAGE_DELETE_ENABLED: "true"

volumes:
  registry-data:
```

## Cloud Registries

### AWS ECR

```bash
# Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com

# Tag and push
docker tag myapp:v1.0 123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1.0
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/myapp:v1.0
```

### Google Container Registry

```bash
# Configure Docker for GCR
gcloud auth configure-docker

# Tag and push
docker tag myapp:v1.0 gcr.io/my-project/myapp:v1.0
docker push gcr.io/my-project/myapp:v1.0
```

### Azure Container Registry

```bash
# Login to ACR
az acr login --name myregistry

# Tag and push
docker tag myapp:v1.0 myregistry.azurecr.io/myapp:v1.0
docker push myregistry.azurecr.io/myapp:v1.0
```

---

# Part 9: Security

## Image Security

### Scan Images

```bash
# Scan with Docker Scout (Docker Desktop)
docker scout quickview nginx:latest

# Scan with Docker Scout CVEs
docker scout cves nginx:latest

# Scan with Trivy
trivy image nginx:latest

# Scan with Snyk
snyk container test nginx:latest
```

### Use Minimal Base Images

```dockerfile
# Good: Alpine-based (small attack surface)
FROM node:18-alpine

# Good: Distroless (no shell, minimal)
FROM gcr.io/distroless/nodejs18-debian11

# Good: Scratch (empty, for Go binaries)
FROM scratch
COPY myapp /myapp
ENTRYPOINT ["/myapp"]
```

## Runtime Security

### Run as Non-Root

```dockerfile
FROM node:18-alpine

# Create non-root user
RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -D appuser

# Change ownership
COPY --chown=appuser:appgroup . /app

# Switch to non-root user
USER appuser

WORKDIR /app
CMD ["node", "server.js"]
```

### Drop Capabilities

```bash
# Run with no capabilities
docker run --cap-drop=ALL myapp

# Add only required capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp
```

### Read-Only Filesystem

```bash
# Read-only root filesystem
docker run --read-only \
  --tmpfs /tmp \
  --tmpfs /var/run \
  myapp
```

### Resource Limits

```bash
# Limit memory
docker run -m 512m --memory-swap 512m myapp

# Limit CPU
docker run --cpus=".5" myapp

# Combined
docker run -m 512m --cpus="1" myapp
```

## Security Best Practices Checklist

| Category | Best Practice |
|----------|--------------|
| **Images** | Use official/verified images |
| **Images** | Keep images updated |
| **Images** | Scan for vulnerabilities |
| **Images** | Use minimal base images |
| **Runtime** | Run as non-root |
| **Runtime** | Drop all capabilities |
| **Runtime** | Use read-only filesystem |
| **Runtime** | Limit resources |
| **Network** | Use user-defined networks |
| **Secrets** | Use Docker secrets/external managers |

---

# Part 10: Advanced Topics

## Multi-Stage Builds

### Go Application

```dockerfile
# Build stage
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# Production stage
FROM scratch
COPY --from=builder /app/main /main
ENTRYPOINT ["/main"]
```

### Node.js Application

```dockerfile
# Dependencies stage
FROM node:18-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine AS production
WORKDIR /app
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## Docker Buildx

Buildx is Docker's extended build capabilities, supporting multi-platform builds.

```bash
# Create builder
docker buildx create --name mybuilder --use

# Build for multiple platforms
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t username/myapp:latest \
  --push .

# Build with cache
docker buildx build \
  --cache-from type=registry,ref=username/myapp:cache \
  --cache-to type=registry,ref=username/myapp:cache,mode=max \
  -t username/myapp:latest \
  --push .
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            username/myapp:latest
            username/myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### GitLab CI

```yaml
stages:
  - build
  - push

variables:
  IMAGE_NAME: $CI_REGISTRY_IMAGE

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $IMAGE_NAME:$CI_COMMIT_SHA .
    - docker tag $IMAGE_NAME:$CI_COMMIT_SHA $IMAGE_NAME:latest

push:
  stage: push
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker push $IMAGE_NAME:$CI_COMMIT_SHA
    - docker push $IMAGE_NAME:latest
  only:
    - main
```

## Troubleshooting

### Common Issues and Solutions

| Problem | Check | Solution |
|---------|-------|----------|
| Container won't start | `docker logs container` | Fix application errors |
| Port already in use | `lsof -i :port` | Use different port or stop conflicting service |
| Permission denied | File ownership | Check user/group permissions |
| Out of disk space | `docker system df` | `docker system prune -a` |
| Image pull fails | Network/registry | Check registry access, credentials |
| Container keeps restarting | `docker logs` | Fix application, check health checks |

### Debugging Commands

```bash
# Container logs
docker logs container_name
docker logs -f --tail 100 container_name

# Container processes
docker top container_name

# Container resource usage
docker stats container_name

# Execute shell in container
docker exec -it container_name /bin/sh

# Inspect container
docker inspect container_name

# Docker events
docker events

# System-wide info
docker system df
docker system info
```

### Cleanup Commands

```bash
# Remove unused data
docker system prune

# Remove all unused data (including volumes)
docker system prune -a --volumes

# Remove specific resources
docker container prune
docker image prune
docker network prune
docker volume prune
```

---

## 🎉 Congratulations!

You've completed the Docker Zero to Hero course! You now have the knowledge to:

- ✅ Install and configure Docker
- ✅ Work with images and containers
- ✅ Write efficient Dockerfiles
- ✅ Orchestrate multi-container apps with Compose
- ✅ Configure networking and storage
- ✅ Use registries for image distribution
- ✅ Implement security best practices
- ✅ Set up CI/CD pipelines

---

## 📚 Additional Resources

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker GitHub](https://github.com/docker)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Happy Containerizing! 🐳**

