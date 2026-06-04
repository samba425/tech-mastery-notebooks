# Docker Interview Questions — Zero to Hero

330+ questions covering fundamentals through advanced topics, with hands-on labs, mock interview sets, scenario-based questions, comparison tables, a cheat sheet, and curated resources.

> Target audiences: junior, mid-level, senior DevOps/SRE/Platform engineers and Docker Certified Associate (DCA) candidates.

---

## Table of Contents

- [A. Fundamentals & Core Concepts](#a-fundamentals--core-concepts)
- [B. Architecture & Internals](#b-architecture--internals)
- [C. Configuration & Day-to-Day Usage](#c-configuration--day-to-day-usage)
- [D. Advanced Topics](#d-advanced-topics)
- [E. Security, Performance & Best Practices](#e-security-performance--best-practices)
- [F. Troubleshooting & Debugging](#f-troubleshooting--debugging)
- [G. Real-World Scenario-Based Questions](#g-real-world-scenario-based-questions)
- [H. Comparison Tables](#h-comparison-tables)
- [I. Hands-On Labs](#i-hands-on-labs)
- [J. Mock Interview Sets](#j-mock-interview-sets)
- [K. Cheat Sheet](#k-cheat-sheet)
- [L. Curated Resources](#l-curated-resources)

---

## A. Fundamentals & Core Concepts

**1. What is Docker?**
Docker is an open-source platform that packages an application and its dependencies into a lightweight, portable, OS-level virtualized unit called a container, which runs consistently across environments.

**2. What is a container?**
A container is an isolated user-space process running on a shared host kernel, with its own filesystem, network namespace, and PID space, created from a read-only image.

**3. Container vs. virtual machine?**
A VM virtualizes hardware and bundles a full guest OS (slow boot, GB-sized). A container virtualizes the OS — shares the host kernel — making it lightweight (MB-sized) and starting in milliseconds.

**4. What problem does Docker solve?**
"Works on my machine." Docker packages app + dependencies + config into an immutable image so behavior is identical across dev, CI, and prod.

**5. What is an image?**
An immutable, read-only template made of stacked layers. Identified by a content-addressable digest (e.g., `sha256:abcd...`).

**6. What is a Dockerfile?**
A text file with declarative instructions (`FROM`, `RUN`, `COPY`, `CMD`, etc.) that the Docker engine processes to build an image.

**7. What is a registry?**
A service that stores and distributes images — Docker Hub, GHCR, ECR, GCR, Quay, Harbor, ACR.

**8. What is a repository?**
A collection of images in a registry sharing the same name but differentiated by tags (e.g., `nginx:1.25`, `nginx:alpine`).

**9. What's a tag?**
A human-friendly label attached to an image digest (`nginx:1.25.3`). Tags are mutable — pin by digest for production: `nginx@sha256:abcd...`.

**10. Image vs. container relationship?**
An image is the class; a container is an instance. Many containers can run from one image; each gets its own writable top layer.

**11. What is the Docker daemon?**
`dockerd` — long-running background service that builds, runs, and manages containers. Listens on a Unix socket (`/var/run/docker.sock`) or TCP.

**12. What is the Docker CLI?**
`docker` — REST client that talks to the daemon over its API.

**13. What is `containerd`?**
A high-level container runtime maintained by CNCF. Docker delegates lifecycle, image, and storage management to it.

**14. What is `runc`?**
The low-level OCI-compliant runtime that actually creates and runs containers using Linux namespaces and cgroups.

**15. What is OCI?**
Open Container Initiative — a Linux Foundation project that standardizes the container image format and runtime spec.

**16. Difference between `CMD` and `ENTRYPOINT`?**
`ENTRYPOINT` defines the executable; `CMD` defines default args. CLI args after `docker run <image>` override `CMD`, not `ENTRYPOINT`. Best practice: use `ENTRYPOINT ["binary"]` plus `CMD ["--flag"]`.

**17. `COPY` vs `ADD`?**
Both copy files; `ADD` also auto-extracts local tar files and can fetch URLs. Prefer `COPY` (predictable). Use `ADD` only for local archives.

**18. `EXPOSE` — does it publish a port?**
No. `EXPOSE` is metadata documenting which port the container listens on. Publishing is done at run time with `-p host:container`.

**19. What is a base image?**
The image specified in `FROM`. Examples: `alpine`, `ubuntu`, `python:3.12-slim`, `scratch`.

**20. What is `scratch`?**
An empty image — 0 bytes. Used for building minimal images from statically compiled binaries (Go, Rust).

**21. What is a layer?**
A filesystem change set produced by a single Dockerfile instruction. Layers are stacked using a union FS and cached for reuse.

**22. What is UnionFS?**
A filesystem service that overlays multiple directories, presenting them as one. OverlayFS is the most common backend on Linux.

**23. What is the copy-on-write (CoW) strategy?**
Container writes don't modify image layers. Modified files are copied up to the writable container layer. Saves disk and enables fast container startup.

**24. What is the writable container layer?**
The single thin R/W layer added on top of image layers when a container starts. Lost when the container is removed unless committed.

**25. Difference between `docker run` and `docker start`?**
`docker run` creates **and** starts a new container from an image. `docker start` starts an existing stopped container.

**26. What does `docker exec` do?**
Runs a command inside an already-running container. Common for debugging: `docker exec -it <id> sh`.

**27. What's `docker attach`?**
Attaches your terminal to a running container's main process (STDIN/STDOUT). Detach with `Ctrl-P Ctrl-Q` (not `Ctrl-C`, which sends SIGINT).

**28. What is `docker logs`?**
Streams the STDOUT/STDERR of a container's main process from the configured logging driver.

**29. What is a Docker volume?**
A managed, host-stored data location that survives container removal. Created with `docker volume create` or `-v vol:/path`.

**30. Volume vs. bind mount?**
**Volume**: managed by Docker, stored in `/var/lib/docker/volumes/`. **Bind mount**: maps an arbitrary host path into the container.

**31. What is `tmpfs` mount?**
An in-memory mount. Data lost on container stop. Useful for sensitive data or temp scratch space.

**32. What is the default network driver?**
`bridge` — every Docker host has a default bridge `docker0`.

**33. List the network drivers.**
`bridge`, `host`, `none`, `overlay` (Swarm), `macvlan`, `ipvlan`, third-party (Weave, Calico).

**34. What is `host` network mode?**
Container shares the host's network namespace — no isolation, no port mapping needed. Performance benefit; security trade-off.

**35. What is `none` network mode?**
Container has only a loopback interface. Useful for security or apps that don't need network.

**36. How does container-to-container DNS work?**
On user-defined bridge networks, Docker provides an embedded DNS server (127.0.0.11) that resolves container names.

**37. What is Docker Compose?**
A tool to define multi-container applications declaratively in `docker-compose.yml` and orchestrate them with one command.

**38. What is Docker Swarm?**
Docker's native clustering / orchestration mode. Built into the engine; lighter but less feature-rich than Kubernetes.

**39. What is BuildKit?**
The next-generation Docker builder enabled by default in 23+. Provides parallel stages, build secrets, cache mounts, frontends, and improved caching.

**40. What is `docker buildx`?**
A CLI plugin built on BuildKit that adds multi-arch builds, multiple builder instances, and OCI output formats.

**41. What is a manifest list?**
A list pointing to platform-specific images (linux/amd64, linux/arm64). Lets one tag work across architectures.

**42. What is a multi-stage build?**
A Dockerfile with multiple `FROM` statements. Each stage can copy artifacts from earlier stages, allowing tiny final images.

**43. What is `WORKDIR`?**
Sets the working directory for subsequent `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD`.

**44. What is `USER` for?**
Sets the UID for subsequent instructions and container runtime. Critical for non-root container security.

**45. What is `LABEL` used for?**
Attaches metadata key/value pairs (`maintainer`, `org.opencontainers.image.*`). Used by tools for filtering and provenance.

**46. What is `HEALTHCHECK`?**
Instruction that defines a command Docker periodically runs inside the container; sets container status to `healthy`/`unhealthy`.

**47. What's `ONBUILD`?**
A deferred instruction executed when the image is used as a base in another `FROM`. Rarely used outside language-specific base images.

**48. What is `ARG` vs `ENV`?**
`ARG` is build-time only and not present at runtime. `ENV` persists into the running container.

**49. Can a Dockerfile inherit from another Dockerfile?**
No, only from an image. Use multi-stage builds, build args, or composition patterns.

**50. What is `docker commit`?**
Creates an image from a running container's changes. Discouraged in CI; use Dockerfiles for reproducibility.

**51. What does `docker save` / `load` do?**
`save` writes an image to a tar archive; `load` re-imports it. Used for air-gapped transfer.

**52. `docker export` / `import`?**
`export` flattens a container's filesystem to tar; `import` creates a single-layer image. Loses image history/metadata.

**53. What's the difference between `docker pause` and `docker stop`?**
`pause` freezes processes via the freezer cgroup (memory remains). `stop` sends SIGTERM then SIGKILL after 10s.

**54. How do you handle SIGTERM in a container?**
The main process (PID 1) must trap it. Use `exec` form (`CMD ["bin", "arg"]`) so the binary is PID 1, not a shell that ignores signals.

**55. What is the PID 1 problem?**
PID 1 in Linux has special signal-handling semantics (ignores SIGTERM by default unless explicitly handled) and reaps zombies. Many apps don't expect to be PID 1.

**56. Solution to PID 1 problem?**
Use a small init like `tini` (`docker run --init`) or `dumb-init` to forward signals and reap zombies.

**57. What is `restart` policy?**
Controls daemon behavior when a container exits: `no`, `on-failure[:max]`, `always`, `unless-stopped`.

**58. What is `docker inspect`?**
Returns full JSON metadata for any Docker object — useful with `--format` Go templates.

**59. Image cache invalidation rules?**
A layer's cache is invalidated when its instruction or inputs change. Once a layer changes, all subsequent layers are rebuilt.

**60. What is `.dockerignore`?**
Like `.gitignore` for the build context — files matching its patterns aren't sent to the daemon. Crucial for build performance and security.

---

## B. Architecture & Internals

**61. Draw the Docker architecture.**
Client (CLI) -> dockerd REST API -> containerd -> containerd-shim -> runc -> container processes. Engine also talks to networking, volumes, plugins, and the registry.

**62. What does containerd-shim do?**
A small process that adopts the container after `runc` exits, decoupling container lifecycle from `containerd` restarts.

**63. Where is Docker's data stored?**
`/var/lib/docker/` (Linux): subdirectories `image/`, `containers/`, `volumes/`, `network/`, `overlay2/` (or chosen storage driver).

**64. What is a storage driver?**
The layer-management backend: `overlay2` (default, recommended), `btrfs`, `zfs`, `aufs` (deprecated), `devicemapper` (deprecated).

**65. Why is `overlay2` preferred?**
Built into modern Linux kernels (4.x+), excellent performance, supports page cache sharing, no patches required.

**66. How does layer caching across builds work?**
Build context + each instruction's directives produce a layer ID. If the daemon sees an identical layer, it reuses it. BuildKit additionally supports content-based caching.

**67. What is content-addressable storage in Docker?**
Images and layers are referenced by SHA-256 digests of their content. Guarantees immutability and verifiability.

**68. What namespaces does Docker use?**
`pid`, `net`, `mnt`, `uts`, `ipc`, `user`, and `cgroup` — providing isolated views of process IDs, network, filesystem, hostname, IPC, users, and cgroups respectively.

**69. What are cgroups?**
Control groups — kernel feature to limit and account resource usage (CPU, memory, blkio, pids, network).

**70. cgroup v1 vs v2?**
v2 has a unified hierarchy (single tree), better resource control, and is required for rootless Docker. Most modern distros default to v2.

**71. What is a seccomp profile?**
A whitelist of allowed syscalls. Docker ships a default profile blocking ~44 dangerous syscalls.

**72. What is AppArmor?**
A Linux MAC system. Docker auto-applies a default profile (`docker-default`) on Ubuntu/Debian to restrict container capabilities.

**73. What is SELinux integration?**
Docker labels container processes/files with SELinux contexts. Use `:Z` (private) or `:z` (shared) on bind mounts in RHEL-family systems.

**74. What Linux capabilities does Docker grant by default?**
A reduced set including `CHOWN`, `SETUID`, `SETGID`, `NET_BIND_SERVICE`, `KILL`. Dangerous ones like `SYS_ADMIN` are dropped.

**75. What is `--privileged`?**
Gives the container nearly all host capabilities, disables seccomp, removes most isolation. Essentially "no security." Use sparingly.

**76. How does Docker networking work under the hood?**
Linux bridges (`docker0`), `veth` pairs (one end in host netns, one in container netns), iptables NAT rules for port publishing.

**77. What is `iptables` MASQUERADE for?**
SNAT for outbound container traffic so packets appear to originate from the host IP.

**78. How are published ports implemented?**
`iptables -t nat -A DOCKER` DNAT rules redirect host port to container IP:port; `docker-proxy` userland process handles edge cases.

**79. What is `docker-proxy`?**
Userland TCP/UDP proxy used as fallback when iptables rules don't apply (loopback, hairpin NAT). Can be disabled with `--userland-proxy=false`.

**80. Bridge vs overlay network internals?**
Bridge uses local Linux bridge + iptables. Overlay uses VXLAN tunnels to connect Swarm nodes — requires a key/value store (built-in for Swarm).

**81. What is a `veth` pair?**
A virtual Ethernet cable — two endpoints; what enters one exits the other. Connects container netns to host bridge.

**82. What's MACVLAN good for?**
Containers appear as physical devices on the L2 network with their own MAC/IP. Useful when integrating with legacy infra.

**83. Docker DNS resolution order?**
On a user-defined network: Docker's embedded DNS (127.0.0.11) resolves container names, then forwards to external resolvers from `/etc/resolv.conf`.

**84. How does `docker logs` retrieve output?**
The logging driver writes container stdout/stderr to its configured backend. For the default `json-file` driver, logs live in `/var/lib/docker/containers/<id>/<id>-json.log`.

**85. List logging drivers.**
`json-file` (default), `journald`, `syslog`, `local`, `fluentd`, `gelf`, `awslogs`, `gcplogs`, `splunk`, `none`.

**86. How does the build context get sent to the daemon?**
The CLI tars the build context (current dir minus `.dockerignore` patterns) and POSTs it to `/build`. BuildKit can stream incrementally.

**87. What is BuildKit's frontend?**
A pluggable parser — `dockerfile.v0` is default. Custom frontends can implement other DSLs.

**88. What is the gRPC frontend protocol?**
BuildKit's interface: frontends emit a directed acyclic graph (LLB) describing build steps; the backend executes and caches.

**89. How does BuildKit cache mounts work?**
`RUN --mount=type=cache,target=/root/.npm npm install` — persistent cache directory across builds, not stored in the image layer.

**90. What's a build secret?**
`RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret` — mounts a secret into the build step without baking it into a layer.

**91. How are SSH credentials forwarded into a build?**
`--ssh default` plus `RUN --mount=type=ssh git clone git@...` — uses an SSH agent socket inside the build.

**92. How does Docker handle image distribution authentication?**
`docker login` writes credentials to `~/.docker/config.json` (often via credential helpers like `osxkeychain`, `pass`, `secretservice`).

**93. What is Notary / Content Trust?**
TUF-based image signing (`DOCKER_CONTENT_TRUST=1`). Mostly superseded by Sigstore/cosign.

**94. What is `cosign`?**
A Sigstore tool for signing OCI artifacts keyless (OIDC-based) or with key pairs. Industry standard for supply-chain signing.

**95. How is image provenance tracked?**
SLSA provenance attestations, in-toto, and SBOMs (e.g., `syft`, `trivy sbom`).

**96. Where does Docker store image manifests locally?**
Under `/var/lib/docker/image/<driver>/repositories.json` and content-addressable in `/image/<driver>/imagedb/content/sha256/`.

**97. How is registry pagination handled?**
Registry V2 API uses `Link` headers and `?n=` + `?last=` query params.

**98. What is `dive`?**
A CLI tool to explore image layer contents and inefficiencies — `dive <image>`.

**99. What is `docker system events`?**
Real-time stream of daemon events (create, start, die, pull, etc.) — useful for auditing and automation.

**100. How is the `docker.sock` security-sensitive?**
Mounting it into a container gives that container root on the host. Never expose it to untrusted code or over TCP without TLS+mTLS.

**101. What is rootless mode?**
Run dockerd as a non-root user using user namespaces. Significantly reduces blast radius if a container escapes.

**102. Limitations of rootless mode?**
No host-network mode, limited overlay support, port < 1024 needs `setcap`, some storage drivers unavailable.

**103. What is the OCI image spec?**
Defines the structure of layers, manifest, config, and index files in an image.

**104. What is the OCI runtime spec?**
Defines `config.json` and the lifecycle (`create`, `start`, `kill`, `delete`) a runtime must implement.

**105. What is a bundle?**
A directory with `config.json` + root filesystem that `runc` consumes to launch a container.

**106. What is CRIU?**
Checkpoint/Restore In Userspace — used by experimental `docker checkpoint` to snapshot and restore a running container's state.

**107. What's a container's view of `/proc`?**
A virtual filesystem mounted with namespace-aware views: PID namespace scopes process visibility; some sensitive entries are masked.

**108. How does Docker handle `/sys`?**
Mounted read-only by default to prevent containers from reconfiguring kernel features.

**109. What is `pivot_root`?**
A syscall that swaps a process's root filesystem with another mount. `runc` uses it to enter the container's rootfs.

**110. What is the difference between containers and chroot?**
chroot only changes the filesystem view. Containers add namespaces (PID, network, UTS, etc.), cgroups (limits), and security (capabilities, seccomp, MAC).

**111. How does BuildKit parallelize stages?**
Multi-stage Dockerfiles are converted to a DAG; independent branches build in parallel up to `--parallelism`.

**112. What is the maximum number of layers?**
Historically 127 for `aufs`; `overlay2` allows ~256+. In practice keep layers low for cache hits and pull speed.

**113. How does Docker reclaim disk space?**
`docker system prune`, `docker image prune`, `docker volume prune`, `docker builder prune`. Use `-a` to be aggressive and `--filter "until=24h"` for retention.

**114. What's a dangling image?**
An image with no tag (often an intermediate from a failed build or a previously tagged image whose tag moved).

**115. What is `docker context`?**
Manages remote daemon connections; switch with `docker context use <name>`.

**116. How is the Docker API versioned?**
URL-style: `/v1.45/containers/json`. The daemon negotiates an acceptable version with the client.

**117. What is the difference between client API version and daemon API version?**
Client should be ≤ daemon version. Forcing with `DOCKER_API_VERSION` works for slightly older daemons.

**118. What is `docker engine api`?**
The REST + JSON HTTP API the daemon exposes. The CLI is one client; SDKs exist for Go, Python, Java, etc.

**119. What's the difference between `docker info` and `docker version`?**
`version` shows client/server versions; `info` shows runtime state (containers, images, plugins, storage driver, kernel, cgroup driver, etc.).

**120. What cgroup driver should Docker use with K8s?**
`systemd` — must match the kubelet's cgroup driver to avoid pod startup issues.

---

## C. Configuration & Day-to-Day Usage

**121. Write a minimal Dockerfile for a Python Flask app.**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

**122. How do you build and tag?**
`docker build -t myapp:0.1.0 -t myapp:latest .`

**123. How do you build for a specific architecture?**
`docker buildx build --platform linux/arm64 -t myapp:arm64 .`

**124. How do you push to a private registry?**
`docker login registry.example.com` then `docker tag myapp registry.example.com/team/myapp:0.1.0 && docker push registry.example.com/team/myapp:0.1.0`.

**125. List running containers vs all containers?**
`docker ps` vs `docker ps -a`.

**126. Run a detached web server with port mapping?**
`docker run -d --name web -p 8080:80 nginx`

**127. Run a one-shot container that's auto-deleted?**
`docker run --rm -it python:3.12-slim python`

**128. Set environment variables at runtime?**
`docker run -e DB_HOST=db.example -e DB_PORT=5432 myapp`
Or from a file: `docker run --env-file .env myapp`.

**129. Mount a volume read-only?**
`docker run -v mydata:/data:ro myapp`

**130. Create a named volume?**
`docker volume create logs && docker run -v logs:/var/log/app myapp`

**131. Copy a file from host into a running container?**
`docker cp ./script.sh <container>:/tmp/script.sh`

**132. Tail logs of a container?**
`docker logs -f --tail=100 <container>`

**133. Get a shell in a running container?**
`docker exec -it <container> sh` (use `bash` if image has it).

**134. Restart a stopped container?**
`docker start <container>` (re-uses existing R/W layer and config).

**135. Update a container's CPU limit at runtime?**
`docker update --cpus="1.5" --memory="512m" <container>`.

**136. Apply CPU and memory limits at run?**
`docker run --cpus=2 --memory=1g --memory-swap=1g myapp`.

**137. Set restart policy?**
`docker run --restart=on-failure:5 myapp`.

**138. View resource stats?**
`docker stats` for live, `docker stats --no-stream` for one-shot.

**139. Filter `docker ps` output?**
`docker ps --filter "status=exited" --filter "label=team=payments"`.

**140. Use Go template formatting?**
`docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Status}}'`.

**141. Bulk remove stopped containers?**
`docker container prune -f`.

**142. Build with no cache?**
`docker build --no-cache -t myapp .`.

**143. Pass build args?**
`docker build --build-arg APP_VERSION=1.2.3 -t myapp .` — used in Dockerfile with `ARG APP_VERSION`.

**144. Use multi-platform build and push in one shot?**
```bash
docker buildx create --use --name multi
docker buildx build --platform linux/amd64,linux/arm64 -t reg/app:1.0.0 --push .
```

**145. Inspect image labels?**
`docker inspect --format '{{json .Config.Labels}}' nginx:latest`.

**146. Set image label in Dockerfile?**
```dockerfile
LABEL org.opencontainers.image.source="https://github.com/me/app"
LABEL org.opencontainers.image.licenses="MIT"
```

**147. Use a `.dockerignore` example?**
```
.git
node_modules
*.log
Dockerfile
docker-compose*.yml
.env*
```

**148. Override the default user?**
`docker run --user 1000:1000 myapp`.

**149. Run with a non-root user in the Dockerfile?**
```dockerfile
RUN useradd -m -u 1000 app
USER app
```

**150. Create a custom bridge network?**
`docker network create --driver bridge mynet --subnet=10.10.0.0/16`.

**151. Connect a running container to a network?**
`docker network connect mynet <container>`.

**152. Disconnect from a network?**
`docker network disconnect mynet <container>`.

**153. Inspect a network?**
`docker network inspect mynet`.

**154. Resolve a container by name on a bridge network?**
On a user-defined bridge, just use the container's name: `ping web` works. On the default bridge it does not — use `--network mynet` instead.

**155. Persist database data across container recreations?**
Use a named volume:
```bash
docker run -d -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/pgpass postgres:16
```

**156. Pass secrets at runtime?**
With Compose use `secrets:` (file-based) or env vars sourced from secret managers. Avoid baking secrets into images.

**157. View image history?**
`docker history myapp:0.1.0`.

**158. Show image disk usage?**
`docker system df -v`.

**159. Tag an existing image?**
`docker tag myapp:0.1.0 myapp:stable`.

**160. Remove an image?**
`docker rmi myapp:0.1.0`. Use `-f` if containers reference it.

**161. Force-remove a running container?**
`docker rm -f <container>` (sends SIGKILL).

**162. Save and load an image for offline transfer?**
```bash
docker save -o myapp.tar myapp:0.1.0
scp myapp.tar dest:
docker load -i myapp.tar
```

**163. Pull a specific digest?**
`docker pull nginx@sha256:abcdef...`. Immutable reference for production.

**164. Pull all tags of a repo?**
`docker pull -a nginx` (avoid in CI — wasteful).

**165. Use Compose to start a stack?**
```bash
docker compose up -d
docker compose ps
docker compose logs -f web
docker compose down
```

**166. Compose v1 vs v2?**
v1 was Python (`docker-compose`); v2 is Go and a subcommand (`docker compose`). v2 is the standard going forward.

**167. Define a service in `docker-compose.yml`?**
```yaml
services:
  web:
    image: nginx:1.27
    ports: ["8080:80"]
    restart: unless-stopped
    networks: [appnet]
    depends_on:
      api:
        condition: service_healthy
  api:
    build: ./api
    healthcheck:
      test: ["CMD", "wget", "-q", "-O-", "http://localhost:8000/health"]
      interval: 10s
      retries: 3
networks:
  appnet:
```

**168. Use Compose profiles?**
```yaml
services:
  debug:
    image: busybox
    profiles: ["dev"]
```
Start with `docker compose --profile dev up`.

**169. Set environment variables in Compose?**
Inline `environment:`, file `env_file:`, or via `.env` (variable substitution in the yml file).

**170. Use named volumes in Compose?**
```yaml
services:
  db:
    image: postgres:16
    volumes: ["pgdata:/var/lib/postgresql/data"]
volumes:
  pgdata:
```

**171. Override a Compose file?**
Default load order: `docker-compose.yml` + `docker-compose.override.yml`. Custom: `docker compose -f base.yml -f prod.yml up`.

**172. `extends` keyword?**
Allows a service to inherit another's config. Reduces duplication across files.

**173. Scale a Compose service?**
`docker compose up -d --scale web=3` (no built-in load balancer; use a reverse proxy).

**174. Bind-mount source code for local dev?**
```yaml
services:
  app:
    build: .
    volumes: [".:/app", "/app/node_modules"]
```
The anonymous volume on `node_modules` keeps the image-installed modules.

**175. Define a healthcheck in Dockerfile?**
```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost/health || exit 1
```

**176. Pause/unpause a container?**
`docker pause <container>` / `docker unpause <container>`.

**177. Use Docker contexts to switch hosts?**
```bash
docker context create staging --docker "host=ssh://deploy@staging"
docker context use staging
docker ps
```

**178. Cleanup everything not used in last 24h?**
`docker system prune -af --filter "until=24h" --volumes`.

**179. Connect to a registry over HTTPS with custom CA?**
Put the CA cert in `/etc/docker/certs.d/<registry>/ca.crt` and restart the daemon.

**180. Use insecure registry (lab only)?**
In `/etc/docker/daemon.json`:
```json
{ "insecure-registries": ["registry.local:5000"] }
```
Restart daemon. **Never** use in production.

---

## D. Advanced Topics

**181. Explain BuildKit's LLB.**
LLB (Low-Level Build) is a directed acyclic graph IR. Each node represents a filesystem op or process. BuildKit caches and parallelizes nodes.

**182. How would you minimize a Python image to under 100 MB?**
- Use `python:3.12-slim` or `-alpine` (mind musl gotchas).
- Multi-stage build: build wheels in a builder, copy to final stage.
- `PIP_NO_CACHE_DIR=1` and `--no-compile`.
- Delete `__pycache__`, locales, docs.
- Use `distroless` (`gcr.io/distroless/python3`) for the final stage.

**183. Multi-stage Go example?**
```dockerfile
FROM golang:1.23-alpine AS build
WORKDIR /src
COPY go.* ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /out/app ./cmd/api

FROM gcr.io/distroless/static:nonroot
COPY --from=build /out/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

**184. What is `--cache-from` / `--cache-to`?**
BuildKit can import/export cache to a registry: `--cache-to type=registry,ref=reg/cache,mode=max --cache-from type=registry,ref=reg/cache`.

**185. What are inline cache and registry cache?**
Inline: cache metadata baked into the image manifest (`--cache-to type=inline`). Registry: cache stored as a separate manifest, supports more layers.

**186. Reproducible builds?**
Use `SOURCE_DATE_EPOCH`, pin base image digests, vendor dependencies, lockfiles, and tools like Bazel/Nix when bit-for-bit determinism is required.

**187. Build SBOM for an image?**
`docker sbom <image>` or `syft <image>` to produce SPDX/CycloneDX SBOMs.

**188. Sign an image with cosign?**
```bash
cosign generate-key-pair
cosign sign --key cosign.key reg/app:1.0.0
cosign verify --key cosign.pub reg/app:1.0.0
```

**189. Attest provenance with cosign?**
`cosign attest --predicate provenance.json --type slsaprovenance --key cosign.key reg/app:1.0.0`.

**190. What is the supply chain risk of `FROM ubuntu:latest`?**
`latest` is mutable; image content can change without warning. Pin by digest: `FROM ubuntu@sha256:<digest>`.

**191. Implement build secrets using BuildKit.**
```dockerfile
# syntax=docker/dockerfile:1.7
FROM alpine
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci
```
Build: `docker build --secret id=npmrc,src=$HOME/.npmrc .`.

**192. Implement SSH-mount for private Git clones.**
```dockerfile
# syntax=docker/dockerfile:1.7
FROM alpine
RUN apk add --no-cache git openssh-client
RUN mkdir -p ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN --mount=type=ssh git clone git@github.com:org/private.git
```
Build: `docker build --ssh default .` (uses `SSH_AUTH_SOCK`).

**193. Cache mounts for package managers?**
```dockerfile
RUN --mount=type=cache,target=/var/cache/apt \
    apt update && apt install -y curl
```

**194. Distroless images: pros and cons?**
Pros: tiny, no shell, smaller attack surface. Cons: hard to debug (no shell), can't `apt install` at runtime, glibc vs musl compat issues.

**195. How do you debug a distroless container?**
Attach a debug sidecar (`docker run --pid=container:<id> --network=container:<id> nicolaka/netshoot`), or use `kubectl debug` in K8s.

**196. Multi-arch base image vs native?**
Multi-arch lets one `docker pull` resolve the right platform automatically. Native is faster to build but requires platform-specific tags.

**197. What is `qemu-user-static`?**
A binfmt_misc handler that lets your `amd64` host run `arm64` binaries by emulation — used by buildx for cross-builds.

**198. How do you create and use a buildx builder with cluster nodes?**
```bash
docker buildx create --name fleet --node node1 --platform linux/amd64 --use
docker buildx create --append --name fleet --node node2 --platform linux/arm64
docker buildx inspect --bootstrap
```

**199. What is a "frontend" in BuildKit?**
A parser/compiler that converts a Dockerfile (or another DSL) into LLB. Hint: the `# syntax=` comment selects a frontend version.

**200. Use `--squash`?**
Combines all new layers into one. Deprecated in BuildKit; multi-stage builds and proper caching are preferred.

**201. What is `oci-archive` output type?**
`docker buildx build -o type=oci,dest=image.tar` writes an OCI-format tarball.

**202. Multi-stage build with shared cache?**
Stages share the build cache automatically; copying between stages is just a layer reference.

**203. What's `BUILDKIT_INLINE_CACHE`?**
A legacy env var equivalent to `--cache-to=type=inline` (writes cache metadata into manifest).

**204. How does Docker Swarm differ from compose?**
Compose: single host, dev-friendly. Swarm: cluster of nodes, service replicas, overlay networking, rolling updates, secrets, configs.

**205. Initialize a Swarm?**
```bash
docker swarm init --advertise-addr <MGR_IP>
docker swarm join-token worker
```

**206. Deploy a stack?**
```bash
docker stack deploy -c docker-compose.yml mystack
docker stack services mystack
```

**207. What is a Swarm service?**
A declared specification (image, replicas, networks, mounts) that the manager maintains across the cluster.

**208. What's the difference between replicas and global mode?**
`replicated`: N copies across cluster. `global`: one task per node — for daemons (log shippers, monitoring agents).

**209. Rolling update with Swarm?**
```yaml
deploy:
  update_config:
    parallelism: 2
    delay: 10s
    order: start-first
    failure_action: rollback
```

**210. Swarm secrets?**
`echo "<value>" | docker secret create db_pass -` then mount in compose:
```yaml
secrets:
  db_pass:
    external: true
services:
  app:
    secrets: [db_pass]
```
The secret appears in the container at `/run/secrets/db_pass`.

**211. Why isn't Swarm "dead"?**
It's still maintained by Mirantis and widely used in edge/small-cluster contexts. Kubernetes is the industry default, but Swarm is simpler.

**212. What is a Compose extension field?**
`x-*` keys are ignored by Compose but available to extensions or templating tools. Common for YAML anchors:
```yaml
x-logging: &default-logging
  driver: json-file
  options:
    max-size: "10m"
services:
  api: { logging: *default-logging }
```

**213. Run docker-in-docker (DinD)?**
`docker run --privileged -d --name dind docker:dind`. Useful for CI; security concerns — prefer mounting `/var/run/docker.sock` from the host or using rootless DinD.

**214. Risks of DinD vs sock-mount?**
DinD: privileged, isolated but heavy. Sock-mount: lightweight but the sibling container effectively gets root on the host. Use `sysbox` runtime or rootless when possible.

**215. What is `sysbox`?**
A drop-in runtime by Nestybox that allows secure rootless DinD, systemd-in-container, etc.

**216. Use `docker context` to deploy to remote Swarm?**
```bash
docker context create swarm-prod --docker "host=ssh://root@manager.prod"
docker --context swarm-prod stack deploy -c stack.yml prod
```

**217. Inspect a container's network namespace?**
```bash
PID=$(docker inspect -f '{{.State.Pid}}' <container>)
sudo nsenter -t $PID -n ip addr
```

**218. Run a process in a container's network namespace?**
`sudo nsenter -t $PID -n /bin/bash` or `docker run --network=container:<id> nicolaka/netshoot`.

**219. What is `slirp4netns`?**
A userland network stack used by rootless Docker/Podman to provide network isolation without root.

**220. What is `pasta`?**
A newer, faster alternative to slirp4netns for rootless networking.

**221. Implement zero-downtime deploys with vanilla Docker?**
Run new container alongside old, wait for healthcheck, switch reverse proxy, drain and remove old. Tools like `traefik`/`caddy` automate this with labels.

**222. Implement blue/green with Compose?**
Two stacks (`blue`, `green`) sharing a network; flip the upstream in your edge proxy.

**223. What is `docker plugin`?**
A package extending Docker (network, volume, log, authz). Installed from registry: `docker plugin install vieux/sshfs`.

**224. Custom volume plugin example?**
`docker volume create -d vieux/sshfs -o sshcmd=user@host:/data sshvol`.

**225. Authorization plugin (`AuthZ`)?**
Intercepts API calls to enforce policy (e.g., Open Policy Agent, OpenContrail). Configured via `--authorization-plugin`.

**226. What's `runsc` / gVisor?**
A user-space kernel that re-implements Linux syscalls. Alternative runtime for stronger isolation, at performance cost.

**227. How to set gVisor as runtime?**
Install runsc, in `/etc/docker/daemon.json`:
```json
{ "runtimes": { "runsc": { "path": "/usr/local/bin/runsc" } } }
```
Run: `docker run --runtime=runsc alpine`.

**228. What is Kata Containers?**
Lightweight VMs running OCI containers — kernel isolation per container. Provides VM-grade isolation with container UX.

**229. What is Firecracker?**
AWS micro-VM monitor. Used by Fargate and Lambda. Faster than QEMU, designed for serverless containers.

**230. How does container hot-reload work in dev?**
Bind-mount source code, run the app under a watcher (`nodemon`, `air`, `entr`, `watchdog`); the running PID 1 reloads when files change.

**231. What is a sidecar pattern (Docker context)?**
Two containers sharing volumes/network to extend behavior (logger, proxy, secrets-fetcher). Pattern transfers cleanly to K8s sidecars.

**232. What is the ambassador pattern?**
A proxy container that intermediates outbound connections (service discovery, mTLS termination) so the main app stays simple.

**233. What is the adapter pattern?**
A container that reshapes monitoring/logging output to a standard format the platform expects.

**234. How does Docker Desktop's K8s integration work?**
Embeds a single-node K8s cluster running on the same VM as the Docker engine; managed by Kubernetes Add-On.

**235. What's `docker scout`?**
A CVE scanner and SBOM service integrated into the CLI; replaces `docker scan`.

**236. What is `nerdctl`?**
A Docker-CLI-compatible front end for containerd, supports BuildKit, encryption, lazy pulls (stargz).

**237. What is stargz / eStargz?**
A lazy-pull image format — start the container without downloading every layer fully.

**238. What is overlaybd?**
Alibaba's lazy-pull and snapshot tech for fast container starts.

**239. What is the `--init` flag actually doing?**
Sets PID 1 to `tini`, which forwards signals and reaps zombies, fixing the PID-1 problem.

**240. How can a container influence host kernel parameters?**
With `--sysctl net.core.somaxconn=1024` (only sysctls in allowed namespaces are writable). Generally avoid; tune the host instead.

---

## E. Security, Performance & Best Practices

**241. Top 5 Docker security best practices?**
1) Never run as root inside the container.
2) Use minimal base images (distroless/scratch).
3) Pin image digests, sign images, scan them.
4) Drop capabilities and apply seccomp/AppArmor.
5) Don't mount `/var/run/docker.sock` into untrusted containers.

**242. How do you drop capabilities?**
`docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp`.

**243. Read-only root filesystem?**
`docker run --read-only --tmpfs /tmp myapp`. Often combined with `--cap-drop=ALL`.

**244. How to prevent privilege escalation?**
`docker run --security-opt=no-new-privileges:true myapp`.

**245. Why avoid `latest` tag?**
Mutable; non-reproducible; hides version drift; supply-chain risk. Pin to a digest or precise tag.

**246. How do you scan images?**
`docker scout cves myapp`, `trivy image myapp`, `grype myapp`, or integrate into CI.

**247. Where should secrets live?**
External secret managers (Vault, AWS Secrets Manager, K8s Secrets encrypted at rest). At minimum: build-time `--mount=type=secret` and runtime env vars sourced from a secret store. Never `ENV PASSWORD=...` in a Dockerfile.

**248. Why is `chmod 777` in a Dockerfile dangerous?**
Defeats permission enforcement; any user inside the container can modify those files; aggravates container escape impact.

**249. Best practice for the build context?**
Keep it small. Use `.dockerignore`. Never include `.git`, secrets, IDE files, or huge artifacts.

**250. Why prefer `COPY` over `ADD`?**
`ADD` has surprising behaviors (URL fetch, tar extract). `COPY` is explicit and auditable.

**251. Single `RUN` chain best practice?**
Combine related apt/yum installs in one RUN to reduce layers and clean caches in the same layer:
```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*
```

**252. Why `--no-install-recommends`?**
Skips optional recommended packages, shrinking the image substantially.

**253. Order Dockerfile layers for cache reuse?**
Place least-changing layers first: install OS packages, then language deps (`requirements.txt`), then source code. Source changes won't bust dependency caches.

**254. Why pin `pip` / `npm` lockfiles?**
Reproducible builds, deterministic vulnerability scanning, faster CI.

**255. Healthcheck best practices?**
Cheap and fast (< 1s), check the actual readiness path, distinguish liveness vs readiness in orchestrators.

**256. Set resource limits for production?**
Always set `--memory`, `--cpus`, `--pids-limit`, `--ulimit nofile=...` to prevent noisy-neighbor and OOM cascade.

**257. Why limit `pids`?**
Prevents fork bombs from exhausting the host.

**258. What is `--security-opt seccomp=profile.json`?**
Apply a custom seccomp filter. Use to tighten beyond the default.

**259. Run containers with a custom AppArmor profile?**
`docker run --security-opt apparmor=myprofile myapp` after loading the profile with `apparmor_parser`.

**260. Image hardening checklist?**
- Non-root USER
- Minimal base
- Pinned digests
- No secrets baked in
- Drop all caps, add minimal set
- Read-only FS where possible
- HEALTHCHECK defined
- LABEL provenance metadata
- SBOM + signature published

**261. Image performance: layer order impact?**
Wrong order causes cache misses, ballooning CI times and pull sizes. Keep volatile layers at the end.

**262. Why is `apt-get update` alone a smell?**
If split across multiple `RUN`s, cache may serve stale package lists; always combine with the install in the same RUN.

**263. Reduce image pull time on K8s nodes?**
Smaller images, lazy-pull (stargz), pre-pull DaemonSet, registry mirror near the cluster, image policy webhooks to enforce caching.

**264. How does `--shm-size` matter?**
Many DB clients/browsers need >64MB shared memory; default is 64MB. Increase for Chrome/Selenium: `--shm-size=2g`.

**265. Tuning Docker for high-throughput containers?**
Set ulimits, use `host` network if topology allows, prefer `overlay2`, ensure SSD storage, monitor file descriptors, configure `daemon.json` `default-ulimits`.

**266. Why prefer immutable infrastructure?**
Containers are immutable; redeploy a new image rather than mutating a running one. Improves auditability, rollback, and reliability.

**267. Logging best practice?**
Write to stdout/stderr only; let the platform handle aggregation. Rotate driver logs (`json-file` `max-size: 10m, max-file: 5`) to avoid disk fill.

**268. Why `json-file` rotation is critical?**
Default has no size limit. Long-running containers can fill `/var/lib/docker` and crash the host.

**269. Use of `tini`?**
`docker run --init` adds `tini` as PID 1 — reaps zombies and forwards signals. Use unless your app intentionally handles PID 1.

**270. Container immutability vs config?**
Image is immutable; config is injected (env vars, mounted configs). Avoid `docker commit` for production changes.

---

## F. Troubleshooting & Debugging

**271. Container exits immediately — how to debug?**
`docker logs <id>` first. If empty: `docker inspect` → check `ExitCode` and `Error`. Run interactively: `docker run -it --entrypoint sh <image>`.

**272. What does exit code 137 mean?**
SIGKILL — usually OOM. Check `dmesg | grep -i oom` and the daemon's events.

**273. Exit code 139?**
SIGSEGV — segmentation fault in the application.

**274. Exit code 143?**
SIGTERM accepted gracefully (typically from `docker stop`).

**275. `docker run` says "no space left on device" — where?**
Check `docker system df`. Often `/var/lib/docker/overlay2` fills with stale layers. `docker system prune -af --volumes`.

**276. Image pull fails with "manifest unknown"?**
Wrong tag, missing platform variant, or registry mirror out of date. Verify with `docker manifest inspect <image>`.

**277. Port already in use?**
`lsof -i :8080` to find the offender. Change host port or stop the conflicting process.

**278. Container can't reach the internet?**
Check `iptables -L`, MTU on overlay/VPN (often need `--mtu=1450`), DNS in `/etc/resolv.conf` inside the container.

**279. DNS works on host but not in container?**
Daemon's `--dns` flag or `daemon.json` `dns`. For systemd-resolved, use `--dns=8.8.8.8` or configure host's `127.0.0.53` correctly.

**280. Container can't connect to a service on host (Linux)?**
Use `host.docker.internal` (requires `--add-host=host.docker.internal:host-gateway`), or use the host's bridge IP.

**281. File permission errors with bind mounts?**
UID inside container ≠ UID owning host file. Fix by matching UIDs (`--user $(id -u):$(id -g)`) or `chown` on the host.

**282. SELinux denies bind-mount access (RHEL)?**
Append `:Z` (private label) or `:z` (shared) to the mount: `-v $(pwd):/app:Z`.

**283. Build is slow due to large context?**
Trim with `.dockerignore`, copy only required files, use BuildKit and cache mounts.

**284. `docker compose up` hangs on dependency?**
A `depends_on` healthcheck failing. Inspect with `docker compose ps` and `docker logs`.

**285. "Bad address" or `glibc` errors on Alpine?**
Alpine uses musl libc. Some prebuilt binaries (e.g., Node native modules) need `apk add libc6-compat` or just use the `slim` Debian variant.

**286. Why does an image work locally but not on K8s nodes?**
Architecture mismatch (built for `arm64`, nodes are `amd64`) or it uses a feature not allowed by the cluster's PSS profile.

**287. Container OOM-killed at start?**
Set higher `--memory` and `--memory-swap`, profile actual usage with `docker stats`, optimize JVM/Python memory.

**288. Identify a process consuming CPU inside a container?**
`docker top <id>` and `docker exec <id> top` then map host PIDs via `/proc/<pid>/cgroup`.

**289. Inspect network packets in a container?**
`docker run --rm --net=container:<id> nicolaka/netshoot tcpdump -i any port 80`.

**290. Container's `/etc/hosts` not editable?**
Use `--add-host name:IP` at run time. The file is generated each start.

**291. Image layers ballooning?**
Use `dive <image>` to find waste. Common culprit: `apt install` cache not cleaned, copy of `.git`, dev dependencies.

**292. Build fails with "no space left" on `/var/lib/docker`?**
`docker builder prune -af`; consider moving storage to a larger disk via `daemon.json` `data-root`.

**293. Repeated 'pull rate limit' errors from Docker Hub?**
Authenticate (`docker login`) for higher anonymous limits, or mirror images to a private registry / pull-through cache.

**294. Container can't write to mounted volume?**
Wrong UID/GID, or volume mounted read-only. Check `docker inspect` Mounts section.

**295. Network slow inside container?**
Check MTU mismatch on the bridge, kernel TCP settings, and `--net=host` for latency-sensitive workloads.

**296. Compose service won't restart after host reboot?**
Add `restart: unless-stopped` and ensure Docker is `enabled` (`systemctl enable docker`).

**297. Image healthcheck "starting" forever?**
Set a sane `--start-period` so initial slow boots don't count as failures.

**298. Inspect why a container won't start?**
`docker events --since 30m` to see lifecycle events; `journalctl -u docker` for daemon-side errors.

**299. Stuck "Removal In Progress" state?**
Daemon might be stuck on AUFS/devicemapper IO; switch to overlay2, restart `dockerd`, or `docker rm -f`.

**300. Where to find a coredump from a containerized app?**
Configure host `core_pattern` (`echo '/cores/core.%e.%p' | sudo tee /proc/sys/kernel/core_pattern`) and bind-mount `/cores` into the container.

---

## G. Real-World Scenario-Based Questions

**301. Slim a 2 GB Node.js image down to 200 MB. Strategy?**
- Switch base to `node:20-alpine` or `node:20-slim`.
- Multi-stage: install dev deps in builder, copy only `dist/` and `node_modules` (prod) to runner stage.
- `npm ci --omit=dev`.
- Remove `.git`, README, locales; use `.dockerignore`.
- Consider distroless `nodejs` base.

**302. Design a CI pipeline that builds, tests, scans, and signs Docker images.**
Build with BuildKit + remote cache; test inside the image; scan with `trivy`/`scout`; SBOM via `syft`; sign with `cosign keyless`; push only on green; emit SLSA provenance.

**303. Multi-arch publishing strategy?**
Use `docker buildx` with QEMU emulation in CI, or run native runners per arch and use `docker manifest create` to assemble. Push to a registry that supports manifest lists.

**304. Migrate a monolith from VM to containers — first steps?**
Identify processes, externalize state (DB, sessions, file storage), define one container per process, configure with env vars, add healthchecks, run via Compose first, then orchestrate (K8s).

**305. Hot-fix a container image with a CVE — no source available.**
Rebase: pull image, install patched OS package in a new layer, `docker build -t image:patched`, push to private registry, repoint downstream. Track upstream for permanent fix.

**306. Force registry pull instead of cached image on every deploy?**
Tag with immutable digest or use unique tag per release (commit SHA). Set `imagePullPolicy=Always` for K8s; pull explicitly in scripts.

**307. Build images in CI without giving CI root?**
Use rootless BuildKit (`buildkitd --rootless`), Kaniko, BuildKit's daemonless `buildctl`, or Docker `buildx` on a non-privileged container with sysbox.

**308. Compose file shared across dev/staging/prod?**
Base `docker-compose.yml` + overrides (`docker-compose.dev.yml`, `docker-compose.prod.yml`). Inject env via `.env.<env>`.

**309. Implement zero-downtime deploys with a single host?**
Use a reverse proxy (Traefik/Caddy) with label-based service discovery. Spin up `app-v2`, wait for healthcheck, traffic shifts, drain and stop `app-v1`.

**310. Stop container from logging sensitive data?**
Filter at source (don't log secrets), enforce structured logs, redact at logging pipeline (Fluent Bit filters), and use `--log-driver=none` for ultra-sensitive workloads — pair with side-channel observability.

**311. Build image only when sources change in CI?**
Compute `docker build --cache-from registry/app:cache --cache-to type=registry,ref=registry/app:cache,mode=max`; if the resulting digest matches the previous tag, skip push.

**312. Reduce CI minutes spent in tests?**
Pre-build a "test base" image with deps; CI mounts only source as bind mount; parallelize across services in Compose with `--parallel`.

**313. Roll back a bad image quickly?**
Always tag with both immutable (SHA) and floating (`stable`) refs. Roll back by retagging `stable` -> previous digest and triggering re-pull.

**314. Centralize logs from 100 containers?**
Configure daemon `daemon.json` `log-driver: fluentd` (or `gelf`/`syslog`), or run a logging DaemonSet (Vector, Fluent Bit) that tails `/var/lib/docker/containers/*/*.log`.

**315. Centralize metrics?**
Enable Docker's Prometheus endpoint in `daemon.json` (`metrics-addr`), run cAdvisor and node-exporter, scrape with Prometheus.

**316. Restrict pulling images to a whitelist?**
Run an authorization plugin (e.g., OPA + opa-docker-authz) that enforces image source allow-lists, or a pull-through proxy with strict mirroring rules.

**317. Detect a compromised container at runtime?**
Use Falco/Tracee with rules detecting unexpected syscalls (e.g., `execve("/bin/nc")` in a web container). Stream alerts to SIEM.

**318. Implement secret rotation without restart?**
Use a sidecar fetching secrets and writing to a tmpfs the main app re-reads via SIGHUP; or use a service mesh / SDS-based pattern.

**319. Migrate from Docker Compose to Kubernetes — first step?**
Use `kompose convert` for an initial draft; then refactor: persistent volumes, ConfigMaps, Secrets, Services, NetworkPolicies, HPA, Ingress.

**320. Compose service unhealthy after host reboot — what likely cause?**
Boot ordering: a dependency (database) takes longer to come up. Add restart policies and `depends_on: condition: service_healthy`.

**321. Database container loses data after recreate — what was missed?**
Anonymous volume vs named volume. Use `volumes: [pgdata:/var/lib/postgresql/data]` and declare `pgdata:` at the bottom.

**322. CI image build takes 25 minutes — optimization plan?**
- Enable BuildKit + remote cache (`--cache-from/--cache-to`).
- Re-order Dockerfile for layer cache.
- Use `docker buildx` with parallel stages.
- Vendor dependencies; pre-build base image.
- Replace heavy base with slim/distroless.

**323. Forbid running images from public Docker Hub in production?**
Image policy admission controllers (in K8s) or authz plugins (in Docker) that allow only `harbor.internal/*`.

**324. Container needs to talk to a host MySQL?**
- Linux: `--network host` (simplest), or `--add-host host.docker.internal:host-gateway` and connect to `host.docker.internal`.
- macOS/Windows: `host.docker.internal` is built-in.

**325. Container needs to call AWS APIs — credentials handling?**
On EC2/ECS use the instance/task IAM role (metadata service). Locally use `~/.aws/credentials` bind-mounted read-only or `aws-vault`.

**326. Backup persistent volume?**
`docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar czf /backup/data-$(date +%F).tgz -C /data .`

**327. Restore from backup tarball?**
`docker run --rm -v mydata:/data -v $(pwd):/backup alpine sh -c "cd /data && tar xzf /backup/data-2026-05-01.tgz"`.

**328. Auto-update containers safely?**
Use `watchtower` for non-production. For production, drive updates from CI with explicit promotion gates; never auto-update prod.

**329. Run Docker on a 2 GB RAM IoT device?**
Use `containerd` directly or `balena-engine`. Run only essential containers with strict memory limits. Consider `nerdctl` with lazy-pull.

**330. Identify the slowest stage of a build?**
`docker buildx build --progress=plain --no-cache .` then read per-stage timing or use `docker buildx du`.

---

## H. Comparison Tables

### Docker Engine vs Podman vs containerd vs CRI-O

| Feature | Docker | Podman | containerd | CRI-O |
|---------|--------|--------|------------|-------|
| Daemonless | No | Yes | No | No |
| Rootless | Yes (limited) | Yes (first-class) | Limited | Limited |
| Default in K8s | Deprecated | No | Yes (most distros) | Yes (OpenShift) |
| Build images | Yes (BuildKit) | Yes (buildah) | No (separate) | No (separate) |
| CLI compat with Docker | N/A | High | nerdctl | None |
| Image format | OCI | OCI | OCI | OCI |
| systemd integration | Optional | Native | Optional | Native |

### Bridge vs Host vs Overlay vs Macvlan

| Mode | Isolation | Cross-host | Performance | Use case |
|------|-----------|-----------|-------------|----------|
| bridge | Full | No | Good (NAT cost) | Local single-host apps |
| host | None | N/A | Best | Latency-critical workloads |
| overlay | Full | Yes (VXLAN) | Some overhead | Swarm, multi-host |
| macvlan | Full | Yes (L2) | Near-native | Containers as L2 devices |

### Volume vs Bind Mount vs tmpfs

| Type | Lifecycle | Backup | Sharing | Use |
|------|-----------|--------|---------|-----|
| Volume | Docker-managed | `docker volume` cmds | Across containers | Default for persistence |
| Bind | Host-owned path | Host backup | Arbitrary | Dev hot-reload |
| tmpfs | RAM only | None | Single container | Secrets, scratch |

### Docker vs Vagrant vs LXC

| Aspect | Docker | Vagrant | LXC |
|--------|--------|---------|-----|
| Boundary | Process | VM | OS-level container |
| Kernel | Shared | Own | Shared |
| Startup | ms | minutes | s |
| Use | App packaging | Dev VMs | System containers |

### Docker Compose vs Kubernetes

| Aspect | Compose | Kubernetes |
|--------|---------|-----------|
| Scope | Single host | Cluster |
| YAML | Simple | Complex |
| Networking | Built-in bridges | CNI plugins |
| Self-healing | Basic restart | Full reconcile loop |
| Scaling | Manual `--scale` | HPA/VPA/CA |
| Production use | Small workloads | Default |

---

## I. Hands-On Labs

Each lab is self-contained. Required: Docker 24+, `docker compose` v2, internet access.

### Lab 1 — Multi-Stage Python Image

Build a Flask app whose final image is < 100 MB.

```dockerfile
# Dockerfile
FROM python:3.12-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels
COPY app.py .
USER 1000
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "ok"
```

```
# requirements.txt
flask==3.0.3
gunicorn==22.0.0
```

```bash
docker build -t flask-slim:0.1 .
docker run -d -p 8000:8000 --name flask flask-slim:0.1
curl localhost:8000
docker images flask-slim:0.1   # < 100 MB
```

Expected: image well under 100 MB; container runs as UID 1000; HTTP 200.

---

### Lab 2 — Multi-Arch Image with `buildx`

```bash
docker buildx create --name multi --use
docker buildx inspect --bootstrap
docker buildx build --platform linux/amd64,linux/arm64 \
  -t <YOUR_DOCKERHUB_USER>/flask-slim:multi --push .
docker buildx imagetools inspect <YOUR_DOCKERHUB_USER>/flask-slim:multi
```

Expected: manifest list with `linux/amd64` and `linux/arm64` entries.

---

### Lab 3 — Private Registry with TLS

```bash
mkdir -p certs auth data

# 1. Generate self-signed cert (lab only). Production must use a CA-signed cert.
openssl req -newkey rsa:4096 -nodes -sha256 \
  -keyout certs/domain.key -x509 -days 90 -out certs/domain.crt \
  -subj "/CN=registry.local" \
  -addext "subjectAltName=DNS:registry.local"

# 2. Username / password auth (htpasswd via bcrypt)
docker run --rm --entrypoint htpasswd httpd:2 -Bbn admin "<CHOOSE_STRONG_PASSWORD>" > auth/htpasswd

# 3. Start registry
docker run -d -p 5000:5000 --name registry \
  -v $(pwd)/certs:/certs -v $(pwd)/auth:/auth -v $(pwd)/data:/var/lib/registry \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM=Registry \
  registry:2
```

Trust the cert: copy `certs/domain.crt` to `/etc/docker/certs.d/registry.local/ca.crt`, restart daemon.

`docker login registry.local:5000` -> push -> pull. Note: self-signed certs are flagged as Informational per certificate guidance — fine for lab, never production.

---

### Lab 4 — Compose with Healthchecks & Dependencies

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/pgpass
      POSTGRES_DB: app
    secrets: [pgpass]
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 10
  api:
    image: flask-slim:0.1
    depends_on:
      db:
        condition: service_healthy
    ports: ["8000:8000"]

secrets:
  pgpass:
    file: ./pgpass.txt    # contents are a strong password; do NOT commit

volumes:
  pgdata:
```

`echo "<STRONG_PASSWORD>" > pgpass.txt && chmod 600 pgpass.txt && docker compose up -d`.

Expected: API starts only after Postgres is healthy.

---

### Lab 5 — Image Hardening

Take `nginx:1.27` and produce a hardened variant:

```dockerfile
FROM nginx:1.27-alpine
RUN adduser -D -u 1001 www && \
    chown -R 1001:1001 /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx
COPY nginx.conf /etc/nginx/nginx.conf
USER 1001
EXPOSE 8080
HEALTHCHECK CMD wget -q -O- http://localhost:8080/ || exit 1
```

Run with security flags:

```bash
docker run -d --name web \
  --read-only --tmpfs /var/cache/nginx --tmpfs /var/run \
  --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
  --security-opt=no-new-privileges:true \
  -p 8080:8080 nginx-hardened:1.0
```

Verify with `docker scout cves nginx-hardened:1.0`.

---

### Lab 6 — BuildKit Cache & Secrets

```dockerfile
# syntax=docker/dockerfile:1.7
FROM node:20-slim AS deps
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci --omit=dev
```

```bash
docker build --secret id=npmrc,src=$HOME/.npmrc -t myapp:cached .
```

Re-run; the second build should be nearly instant.

---

### Lab 7 — Debug a CrashLooping Container

```bash
docker run -d --name buggy --restart=on-failure ubuntu:22.04 bash -c "exit 1"
docker logs buggy
docker inspect --format '{{.State.ExitCode}} {{.RestartCount}}' buggy
```

Diagnose, fix the command, redeploy. Lesson: always inspect exit code and restart count first.

---

### Lab 8 — Swarm Stack

```bash
docker swarm init
cat > stack.yml <<'EOF'
services:
  web:
    image: nginx:1.27
    ports: ["8080:80"]
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
EOF
docker stack deploy -c stack.yml demo
docker service ls
docker service scale demo_web=5
docker stack rm demo
docker swarm leave --force
```

---

### Lab 9 — Image Layer Forensics

```bash
brew install dive       # or: snap install dive
dive nginx:1.27
```

Find which layer adds the largest contribution. Suggest one Dockerfile change that would shrink it.

---

### Lab 10 — Supply-Chain Pipeline

```bash
docker scout cves nginx:1.27
syft nginx:1.27 -o spdx-json > sbom.json
cosign generate-key-pair             # produces cosign.key (passphrase-protected) and cosign.pub
cosign sign --key cosign.key <YOUR_REGISTRY>/nginx-mine:1.0
cosign verify --key cosign.pub <YOUR_REGISTRY>/nginx-mine:1.0
```

---

## J. Mock Interview Sets

Treat each set as a 60-minute closed-book exercise. 4 minutes per question.

### Mock Set 1 — Fundamentals & CLI

1. Container vs VM in one paragraph.
2. Write a Dockerfile for a static HTML site served via nginx.
3. Difference between `CMD` and `ENTRYPOINT` with examples.
4. How do you persist data across container restarts?
5. Three storage drivers Docker supports; which is the default?
6. Run a container that auto-removes when exiting and prints `hello`.
7. What does `EXPOSE 8080` do? What doesn't it do?
8. Difference between bind mount and named volume.
9. Show the command to find all stopped containers older than 24h.
10. What does `docker history` show?
11. How would you free disk reclaimed by old images and volumes?
12. Multi-stage build — why and one example.
13. What does `.dockerignore` affect?
14. Explain `docker exec -it <id> sh` step by step.
15. What is `docker context`?

### Mock Set 2 — Architecture, BuildKit & Networking

1. Walk through what happens when you run `docker run nginx`.
2. Role of `containerd`, `runc`, `containerd-shim`.
3. Two ways BuildKit improves on the legacy builder.
4. Implement a build that pulls a private npm package using a secret.
5. Build a multi-arch image for `linux/amd64` and `linux/arm64`.
6. What namespaces does Docker use? Pick three and explain.
7. Why is the cgroup driver important for K8s compatibility?
8. Bridge vs overlay network — when do you pick each?
9. How would you debug DNS resolution failing inside a container?
10. Implement a `docker network create` with custom subnet and pass two containers attached to it that can resolve each other by name.
11. What is `host.docker.internal`? When is it needed?
12. Read-only root filesystem — show the `docker run` flags.
13. Capabilities — drop all, add only `NET_BIND_SERVICE`. Why?
14. What is rootless Docker, and what does it not support?
15. Where does Docker store image layers? Which storage driver should you use today?

### Mock Set 3 — Production & Scenarios

1. Image is 1.8 GB. Walk through your slimming plan.
2. CI takes 25 minutes to build. Three concrete actions to halve it.
3. Deploy zero-downtime updates on a single host with Compose + a reverse proxy.
4. Implement image signing and verification with cosign.
5. Centralize logs from 200 containers across 10 hosts.
6. Quota a container to 1 CPU, 512 MB RAM, 128 PIDs.
7. Production app suddenly OOM-killed. Diagnosis playbook.
8. Engineer mounted `/var/run/docker.sock` into an internet-exposed container. What's the exposure? Mitigation?
9. Container is healthy but unreachable from outside the host. Top 5 things to check.
10. Move data from one volume to another safely.
11. Write a Compose file for app + db + cache + reverse proxy, all with healthchecks.
12. Backup strategy for Docker volumes — script it.
13. Push image to ECR — full workflow.
14. Implement supply chain: build -> SBOM -> scan -> sign -> push -> verify on pull.
15. Detect runtime tampering inside a container.

---

## K. Cheat Sheet

### Lifecycle

```bash
docker pull <image>:<tag>
docker run -d --name <n> -p 8080:80 --restart=unless-stopped <image>
docker exec -it <n> sh
docker logs -f --tail=200 <n>
docker stop <n> && docker rm <n>
docker rmi <image>
```

### Build

```bash
docker build -t name:tag --pull --no-cache .
docker build --build-arg FOO=bar -t name:tag .
docker buildx build --platform linux/amd64,linux/arm64 -t reg/name:tag --push .
docker buildx build --cache-to=type=registry,ref=reg/cache,mode=max \
                    --cache-from=type=registry,ref=reg/cache .
```

### Compose

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f api
docker compose exec api sh
docker compose down -v
docker compose --profile dev up
docker compose -f base.yml -f prod.yml up -d
```

### Volumes & Networks

```bash
docker volume create data
docker volume ls
docker volume inspect data
docker volume rm data

docker network create --driver bridge mynet --subnet 10.10.0.0/16
docker network connect mynet <container>
docker network disconnect mynet <container>
docker network rm mynet
```

### Inspection

```bash
docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}'
docker inspect <id> --format '{{json .NetworkSettings}}' | jq
docker top <id>
docker stats --no-stream
docker events --since 1h --filter type=container
docker system df -v
```

### Cleanup

```bash
docker container prune -f
docker image prune -af
docker volume prune -f
docker network prune -f
docker builder prune -af
docker system prune -af --volumes
```

### Security & Runtime

```bash
docker run \
  --read-only --tmpfs /tmp \
  --cap-drop=ALL --cap-add=NET_BIND_SERVICE \
  --security-opt=no-new-privileges:true \
  --security-opt=seccomp=default.json \
  --pids-limit=128 --memory=512m --cpus=1 \
  --user 1001:1001 \
  myimage:1.0
```

### Registry & Signing

```bash
docker login <registry>
docker tag local:latest reg/name:1.0.0
docker push reg/name:1.0.0
docker pull reg/name@sha256:<digest>

cosign sign --key cosign.key reg/name:1.0.0
cosign verify --key cosign.pub reg/name:1.0.0
```

### Common Dockerfile Patterns

```dockerfile
# Slim Python
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 1000
CMD ["python", "main.py"]

# Static Go via distroless
FROM golang:1.23 AS b
COPY . /src
WORKDIR /src
RUN CGO_ENABLED=0 go build -o /app .
FROM gcr.io/distroless/static:nonroot
COPY --from=b /app /app
USER nonroot
ENTRYPOINT ["/app"]
```

---

## L. Curated Resources

### Official

- Docker docs — https://docs.docker.com
- Dockerfile reference — https://docs.docker.com/reference/dockerfile/
- BuildKit — https://docs.docker.com/build/buildkit/
- Compose spec — https://compose-spec.io/
- OCI spec — https://github.com/opencontainers/image-spec

### Books

- *Docker Deep Dive* — Nigel Poulton
- *Docker in Action, 2e* — Jeff Nickoloff & Stephen Kuenzli
- *Container Security* — Liz Rice
- *The Docker Book* — James Turnbull

### Videos / Courses

- Docker Mastery — Bret Fisher (Udemy)
- TechWorld with Nana — Docker tutorial (YouTube)
- KodeKloud DCA prep
- KubeCon talks on supply chain and BuildKit

### Repos

- https://github.com/wsargent/docker-cheat-sheet
- https://github.com/docker/awesome-compose
- https://github.com/aquasecurity/trivy
- https://github.com/wagoodman/dive
- https://github.com/sigstore/cosign

### Cert

- Docker Certified Associate (DCA) curriculum (note: cert was retired but objectives still used by employers as a study map)
- LF + CNCF — Kubernetes & Cloud Native Associate (KCNA) for adjacent knowledge

---

End of Docker interview guide. Practice the labs end-to-end at least once before any onsite.
