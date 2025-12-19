# ☸️ Kubernetes Zero to Hero - Complete Course

A comprehensive course covering Kubernetes from basics to advanced topics with concise concepts and practical examples.

---

## 📚 Table of Contents

1. [Introduction and Core Concepts](#part-1-introduction-and-core-concepts)
2. [Architecture Deep Dive](#part-2-architecture-deep-dive)
3. [kubectl Mastery](#part-3-kubectl-mastery)
4. [Pods In Depth](#part-4-pods-in-depth)
5. [Controllers and Deployments](#part-5-controllers-and-deployments)
6. [StatefulSets and DaemonSets](#part-6-statefulsets-and-daemonsets)
7. [Services and Networking](#part-7-services-and-networking)
8. [Storage](#part-8-storage)
9. [ConfigMaps and Secrets](#part-9-configmaps-and-secrets)
10. [Ingress](#part-10-ingress)
11. [Helm](#part-11-helm)
12. [Security](#part-12-security)
13. [Advanced Topics](#part-13-advanced-topics)

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BEGINNER                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 01. Intro    │───▶│ 02. Arch     │───▶│ 03. kubectl  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      INTERMEDIATE                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 04. Pods     │───▶│ 05. Deploy   │───▶│ 06. State    │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                  │                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 07. Network  │◀───│ 08. Storage  │◀───│ 09. Config   │◀─────────│
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        ADVANCED                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 10. Ingress  │───▶│ 11. Helm     │───▶│ 12. Security │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                  │                   │
│                                                  ▼                   │
│                                          ┌──────────────┐           │
│                                          │ 13. Advanced │           │
│                                          └──────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
```

---

# Part 1: Introduction and Core Concepts

## What is Kubernetes?

Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications. Originally developed by Google, it's now maintained by the Cloud Native Computing Foundation (CNCF).

## Why Kubernetes?

Kubernetes solves the challenge of running containerized applications at scale by providing automatic healing, scaling, load balancing, and deployment capabilities. It abstracts infrastructure complexity, letting you focus on your applications.

### Key Benefits

| Feature | Description |
|---------|-------------|
| **Self-healing** | Automatically restarts failed containers |
| **Horizontal scaling** | Scale apps up/down based on demand |
| **Service discovery** | Built-in DNS and load balancing |
| **Rolling updates** | Zero-downtime deployments |
| **Secret management** | Secure handling of sensitive data |
| **Declarative config** | Define desired state, K8s maintains it |

## Core Concepts Overview

### Cluster Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         KUBERNETES CLUSTER                          │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                      CONTROL PLANE                             │ │
│  │  ┌─────────┐  ┌──────────────┐  ┌──────────┐  ┌────────────┐ │ │
│  │  │ API     │  │ Controller   │  │Scheduler │  │   etcd     │ │ │
│  │  │ Server  │  │ Manager      │  │          │  │            │ │ │
│  │  └─────────┘  └──────────────┘  └──────────┘  └────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                       WORKER NODES                             │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐ │ │
│  │  │     Node 1      │  │     Node 2      │  │    Node 3      │ │ │
│  │  │ ┌─────────────┐ │  │ ┌─────────────┐ │  │ ┌────────────┐ │ │ │
│  │  │ │   kubelet   │ │  │ │   kubelet   │ │  │ │  kubelet   │ │ │ │
│  │  │ │ kube-proxy  │ │  │ │ kube-proxy  │ │  │ │ kube-proxy │ │ │ │
│  │  │ │  Container  │ │  │ │  Container  │ │  │ │ Container  │ │ │ │
│  │  │ │   Runtime   │ │  │ │   Runtime   │ │  │ │  Runtime   │ │ │ │
│  │  │ └─────────────┘ │  │ └─────────────┘ │  │ └────────────┘ │ │ │
│  │  │ [Pod][Pod][Pod] │  │ [Pod][Pod][Pod] │  │ [Pod][Pod]     │ │ │
│  │  └─────────────────┘  └─────────────────┘  └────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### Kubernetes Objects

| Object | Purpose |
|--------|---------|
| **Pod** | Smallest deployable unit, contains one or more containers |
| **Service** | Stable network endpoint to access Pods |
| **Deployment** | Manages ReplicaSets for stateless apps |
| **ConfigMap** | Store non-sensitive configuration |
| **Secret** | Store sensitive data (passwords, tokens) |
| **Namespace** | Virtual cluster for resource isolation |

## Setting Up Kubernetes

### Local Development Options

| Tool | Best For | Resources |
|------|----------|-----------|
| **Minikube** | Learning, single-node | Moderate |
| **kind** | CI/CD, testing | Low |
| **k3d** | Lightweight local dev | Very Low |
| **Docker Desktop** | Mac/Windows users | Integrated |

### Quick Start with Minikube

```bash
# Install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start cluster
minikube start

# Verify installation
kubectl cluster-info
kubectl get nodes
```

---

# Part 2: Architecture Deep Dive

## Control Plane Components

The control plane makes global decisions about the cluster and detects/responds to cluster events.

### API Server

```
                    ┌─────────────────────┐
                    │      API Server     │
                    │  ┌───────────────┐  │
   kubectl ────────▶│  │ Authentication│  │
   Dashboard ──────▶│  │ Authorization │  │◀──── kubelet
   Controllers ────▶│  │  Admission    │  │◀──── Scheduler
                    │  │  Validation   │  │
                    │  └───────────────┘  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        etcd         │
                    └─────────────────────┘
```

### etcd

etcd is a distributed key-value store that holds all cluster data.

```bash
# Check etcd cluster health
kubectl -n kube-system exec etcd-master -- etcdctl endpoint health
```

### Scheduler

The scheduler watches for newly created Pods and assigns them to nodes.

```
┌────────────────────────────────────────────────────┐
│              SCHEDULER DECISION FLOW               │
│                                                    │
│   New Pod ──▶ Filter Nodes ──▶ Score Nodes ──▶    │
│                    │               │               │
│              ┌─────┴─────┐   ┌─────┴─────┐        │
│              │ Feasible  │   │  Ranked   │        │
│              │  Nodes    │   │   Nodes   │        │
│              └───────────┘   └───────────┘        │
│                                   │               │
│                                   ▼               │
│                            Best Node Selected     │
└────────────────────────────────────────────────────┘
```

### Controller Manager

Controllers are control loops that watch the state of your cluster and make changes.

| Controller | Responsibility |
|------------|---------------|
| Node Controller | Responds to node failures |
| Replication Controller | Maintains correct number of pods |
| Endpoints Controller | Populates Endpoints objects |
| Service Account Controller | Creates default accounts for namespaces |

## Worker Node Components

### kubelet

The kubelet runs on each node and ensures containers are running in Pods.

### kube-proxy

kube-proxy maintains network rules on nodes for Service communication.

### Container Runtime

Container runtimes execute containers (containerd, CRI-O, Docker).

---

# Part 3: kubectl Mastery

## kubectl Basics

kubectl is the command-line tool for interacting with Kubernetes clusters.

```bash
# Syntax
kubectl [command] [TYPE] [NAME] [flags]

# Examples
kubectl get pods
kubectl describe pod nginx
kubectl create -f deployment.yaml
```

## Essential Commands

### Cluster Information

```bash
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
kubectl config view
```

### Working with Pods

```bash
kubectl get pods
kubectl get pods -o wide
kubectl get pods --all-namespaces
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container>
kubectl exec -it <pod-name> -- /bin/sh
kubectl delete pod <pod-name>
```

### Working with Deployments

```bash
kubectl get deployments
kubectl describe deployment <name>
kubectl scale deployment <name> --replicas=3
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>
kubectl rollout undo deployment/<name>
```

### Working with Services

```bash
kubectl get services
kubectl describe service <name>
kubectl expose deployment <name> --port=80 --type=LoadBalancer
```

## Output Formatting

```bash
kubectl get pods -o yaml
kubectl get pods -o json
kubectl get pods -o wide
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase
```

## Context and Configuration

```bash
kubectl config current-context
kubectl config get-contexts
kubectl config use-context <context-name>
kubectl config set-context --current --namespace=<namespace>
```

---

# Part 4: Pods In Depth

## What is a Pod?

A Pod is the smallest deployable unit in Kubernetes, representing a single instance of a running process. Pods can contain one or more containers that share storage and network.

```
┌─────────────────────────────────────────────────────┐
│                      POD                            │
│  ┌─────────────────────────────────────────────┐   │
│  │                Shared Network               │   │
│  │              (localhost:port)               │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │
│  │ Container 1 │  │ Container 2 │  │ Container │  │
│  │   (app)     │  │  (sidecar)  │  │   (init)  │  │
│  └─────────────┘  └─────────────┘  └───────────┘  │
│         │                │                         │
│         └────────────────┴─────────────────────┐  │
│                                                 │  │
│  ┌─────────────────────────────────────────────┐  │
│  │              Shared Storage                 │  │
│  │              (volumes)                      │  │
│  └─────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## Pod Specification

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## Pod Lifecycle

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Pending  │───▶│ Running  │───▶│Succeeded │    │  Failed  │
└──────────┘    └─────┬────┘    └──────────┘    └──────────┘
     │                │                               ▲
     │                └───────────────────────────────┘
     │                         (error)
     ▼
┌──────────┐
│ Unknown  │
└──────────┘
```

| Phase | Description |
|-------|-------------|
| **Pending** | Pod accepted but containers not ready |
| **Running** | At least one container is running |
| **Succeeded** | All containers completed successfully |
| **Failed** | All containers terminated, at least one failed |
| **Unknown** | Pod state cannot be determined |

## Multi-Container Pods

### Sidecar Pattern

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-with-logging
spec:
  containers:
  - name: web
    image: nginx
    volumeMounts:
    - name: logs
      mountPath: /var/log/nginx
  - name: log-shipper
    image: fluentd
    volumeMounts:
    - name: logs
      mountPath: /logs
  volumes:
  - name: logs
    emptyDir: {}
```

## Init Containers

Init containers run before the main containers start.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-init
spec:
  initContainers:
  - name: wait-for-db
    image: busybox
    command: ['sh', '-c', 'until nc -z db-service 5432; do sleep 2; done']
  containers:
  - name: app
    image: myapp:1.0
```

---

# Part 5: Controllers and Deployments

## What are Controllers?

Controllers are control loops that watch the state of your cluster and make or request changes to move the current state toward the desired state.

## Deployments

Deployments manage ReplicaSets and provide declarative updates for Pods.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
```

### Deployment Strategies

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
```

| Strategy | Description |
|----------|-------------|
| **RollingUpdate** | Gradually replace pods (default) |
| **Recreate** | Kill all pods, then create new ones |

### Rolling Updates

```bash
# Update image
kubectl set image deployment/nginx nginx=nginx:1.22

# Check rollout status
kubectl rollout status deployment/nginx

# View history
kubectl rollout history deployment/nginx

# Rollback
kubectl rollout undo deployment/nginx
kubectl rollout undo deployment/nginx --to-revision=2
```

## ReplicaSets

ReplicaSets ensure a specified number of pod replicas are running.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
```

## Jobs and CronJobs

### Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-job
spec:
  completions: 1
  parallelism: 1
  backoffLimit: 3
  template:
    spec:
      containers:
      - name: backup
        image: backup-tool:1.0
        command: ["/backup.sh"]
      restartPolicy: Never
```

### CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-cron
spec:
  schedule: "0 2 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: backup-tool:1.0
          restartPolicy: OnFailure
```

---

# Part 6: StatefulSets and DaemonSets

## StatefulSets

StatefulSets manage stateful applications with stable network identities and persistent storage.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:14
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

### StatefulSet Features

| Feature | Description |
|---------|-------------|
| **Stable Network ID** | Predictable pod names (app-0, app-1) |
| **Stable Storage** | Each pod gets its own PVC |
| **Ordered Operations** | Pods created/deleted in order |
| **Headless Service** | Direct pod-to-pod communication |

## DaemonSets

DaemonSets ensure all (or some) nodes run a copy of a Pod.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluentd:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

### DaemonSet Use Cases

- Log collection (Fluentd, Filebeat)
- Node monitoring (Prometheus Node Exporter)
- Network plugins (Calico, Weave)
- Storage daemons

---

# Part 7: Services and Networking

## What are Services?

Services provide stable network endpoints to access a set of Pods, enabling loose coupling.

```
┌─────────────────────────────────────────────────────────┐
│                       SERVICE                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Stable IP: 10.96.0.100             │   │
│  │              DNS: my-service.default.svc        │   │
│  └─────────────────────────────────────────────────┘   │
│                         │                               │
│         ┌───────────────┼───────────────┐              │
│         │               │               │              │
│         ▼               ▼               ▼              │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│    │  Pod 1  │    │  Pod 2  │    │  Pod 3  │         │
│    │10.0.0.1 │    │10.0.0.2 │    │10.0.0.3 │         │
│    └─────────┘    └─────────┘    └─────────┘         │
└─────────────────────────────────────────────────────────┘
```

## Service Types

### ClusterIP (Default)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

### NodePort

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080
```

### LoadBalancer

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

## Service Type Comparison

| Type | Scope | Use Case |
|------|-------|----------|
| **ClusterIP** | Internal only | Inter-service communication |
| **NodePort** | External via node port | Development, testing |
| **LoadBalancer** | External via cloud LB | Production traffic |
| **ExternalName** | DNS CNAME | External service proxy |

## DNS in Kubernetes

```
┌─────────────────────────────────────────────────────────┐
│                    DNS Resolution                       │
│                                                         │
│  my-service                 → ClusterIP (same namespace)│
│  my-service.default         → ClusterIP                 │
│  my-service.default.svc     → ClusterIP                 │
│  my-service.default.svc.cluster.local → ClusterIP      │
└─────────────────────────────────────────────────────────┘
```

## Network Policies

Network Policies control traffic flow between Pods.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-allow
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```

---

# Part 8: Storage

## Kubernetes Storage Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    STORAGE HIERARCHY                            │
│                                                                 │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│   │   Pod        │    │   Pod        │    │   Pod        │    │
│   │ ┌──────────┐ │    │ ┌──────────┐ │    │ ┌──────────┐ │    │
│   │ │ Container│ │    │ │ Container│ │    │ │ Container│ │    │
│   │ └────┬─────┘ │    │ └────┬─────┘ │    │ └────┬─────┘ │    │
│   │      │       │    │      │       │    │      │       │    │
│   │ ┌────▼─────┐ │    │ ┌────▼─────┐ │    │ ┌────▼─────┐ │    │
│   │ │ Volume   │ │    │ │ Volume   │ │    │ │ Volume   │ │    │
│   │ └────┬─────┘ │    │ └────┬─────┘ │    │ └────┬─────┘ │    │
│   └──────┼───────┘    └──────┼───────┘    └──────┼───────┘    │
│          │                   │                   │            │
│          └───────────────────┼───────────────────┘            │
│                              │                                 │
│                    ┌─────────▼─────────┐                      │
│                    │      PVC          │                      │
│                    │ (Claim)           │                      │
│                    └─────────┬─────────┘                      │
│                              │                                 │
│                    ┌─────────▼─────────┐                      │
│                    │      PV           │                      │
│                    │ (Physical Storage)│                      │
│                    └─────────┬─────────┘                      │
│                              │                                 │
│                    ┌─────────▼─────────┐                      │
│                    │  Storage Backend  │                      │
│                    │  (AWS EBS, GCE PD)│                      │
│                    └───────────────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

## Volumes

### emptyDir

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shared-volume
spec:
  containers:
  - name: writer
    image: busybox
    volumeMounts:
    - name: shared
      mountPath: /data
  - name: reader
    image: busybox
    volumeMounts:
    - name: shared
      mountPath: /data
  volumes:
  - name: shared
    emptyDir: {}
```

### hostPath

```yaml
volumes:
- name: host-data
  hostPath:
    path: /data/app
    type: DirectoryOrCreate
```

## Persistent Volumes (PV) and Claims (PVC)

### PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  hostPath:
    path: /data/pv
```

### PersistentVolumeClaim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

### Using PVC in Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: myapp
    volumeMounts:
    - name: data
      mountPath: /app/data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-pvc
```

## Storage Classes

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iopsPerGB: "10"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

---

# Part 9: ConfigMaps and Secrets

## ConfigMaps

ConfigMaps store non-sensitive configuration data as key-value pairs.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "db.example.com"
  DATABASE_PORT: "5432"
  app.properties: |
    server.port=8080
    logging.level=INFO
```

### Using ConfigMaps

```yaml
# As environment variables
spec:
  containers:
  - name: app
    envFrom:
    - configMapRef:
        name: app-config
        
# As volume
spec:
  containers:
  - name: app
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config
```

## Secrets

Secrets store sensitive data like passwords and API keys (base64 encoded).

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=      # base64 encoded
  password: cGFzc3dvcmQ=  # base64 encoded
```

### Creating Secrets

```bash
# From literal
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=secret

# From file
kubectl create secret generic tls-secret \
  --from-file=tls.crt \
  --from-file=tls.key
```

### Using Secrets

```yaml
# As environment variables
spec:
  containers:
  - name: app
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password

# As volume
spec:
  containers:
  - name: app
    volumeMounts:
    - name: secrets
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secrets
    secret:
      secretName: db-secret
```

---

# Part 10: Ingress

## What is Ingress?

Ingress manages external HTTP/HTTPS access to services, providing load balancing, SSL termination, and name-based virtual hosting.

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   Internet                                                          │
│       │                                                             │
│       ▼                                                             │
│   ┌───────────────────────────────────────┐                        │
│   │        INGRESS CONTROLLER             │                        │
│   │  (nginx, traefik, haproxy, etc.)      │                        │
│   └───────────────────┬───────────────────┘                        │
│                       │                                             │
│   ┌───────────────────▼───────────────────┐                        │
│   │           INGRESS RESOURCE            │                        │
│   │  - Routing rules                      │                        │
│   │  - TLS configuration                  │                        │
│   │  - Path-based routing                 │                        │
│   └───────────────────┬───────────────────┘                        │
│                       │                                             │
│         ┌─────────────┼─────────────┐                              │
│         ▼             ▼             ▼                              │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│   │ Service  │  │ Service  │  │ Service  │                        │
│   │   api    │  │  webapp  │  │  admin   │                        │
│   └──────────┘  └──────────┘  └──────────┘                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Ingress Resource

### Path-Based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

### TLS Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.example.com
    secretName: tls-secret
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

## Installing Ingress Controller

```bash
# NGINX Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.0/deploy/static/provider/cloud/deploy.yaml

# Verify installation
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

---

# Part 11: Helm

## What is Helm?

Helm is the package manager for Kubernetes. It uses charts to define, install, and upgrade applications.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         HELM ARCHITECTURE                           │
│                                                                     │
│   ┌──────────────────┐                                             │
│   │   Helm Client    │                                             │
│   │   (helm CLI)     │                                             │
│   └────────┬─────────┘                                             │
│            │                                                        │
│            ▼                                                        │
│   ┌──────────────────┐       ┌──────────────────┐                  │
│   │   Chart Repo     │       │    K8s Cluster   │                  │
│   │  (charts.yaml)   │──────▶│                  │                  │
│   └──────────────────┘       │  ┌────────────┐  │                  │
│                              │  │  Release   │  │                  │
│                              │  │  Objects   │  │                  │
│                              │  └────────────┘  │                  │
│                              └──────────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
```

## Installing Helm

```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify installation
helm version
```

## Basic Commands

```bash
# Add repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Search charts
helm search repo nginx
helm search hub wordpress

# Install chart
helm install my-release bitnami/nginx

# List releases
helm list

# Upgrade release
helm upgrade my-release bitnami/nginx --set service.type=LoadBalancer

# Uninstall
helm uninstall my-release
```

## Chart Structure

```
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default configuration
├── charts/             # Dependencies
├── templates/          # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl    # Template helpers
│   └── NOTES.txt       # Post-install notes
└── README.md
```

## Creating Charts

```bash
# Create new chart
helm create mychart

# Validate chart
helm lint mychart

# Template locally
helm template mychart

# Package chart
helm package mychart

# Install local chart
helm install myrelease ./mychart
```

---

# Part 12: Security

## RBAC (Role-Based Access Control)

RBAC regulates access to Kubernetes resources based on roles.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          RBAC MODEL                                 │
│                                                                     │
│   ┌──────────────┐         ┌──────────────┐                        │
│   │    User/     │         │    Role/     │                        │
│   │ServiceAccount│◀────────│ ClusterRole  │                        │
│   └──────────────┘         └──────────────┘                        │
│          │                        │                                 │
│          │    Binding             │ Defines                        │
│          │                        │ Permissions                    │
│          ▼                        ▼                                 │
│   ┌──────────────┐         ┌──────────────┐                        │
│   │ RoleBinding/ │────────▶│  Resources   │                        │
│   │ClusterRole   │         │  (pods,      │                        │
│   │   Binding    │         │  services)   │                        │
│   └──────────────┘         └──────────────┘                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Role and RoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### ClusterRole and ClusterRoleBinding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
- kind: Group
  name: managers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

## Service Accounts

Service accounts provide identities for processes running in pods.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: default
---
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  serviceAccountName: app-sa
  containers:
  - name: app
    image: myapp:1.0
```

## Security Contexts

Security contexts define privilege and access control settings.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: app
    image: myapp
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

## Pod Security Standards

| Level | Description |
|-------|-------------|
| **Privileged** | Unrestricted, allows known privilege escalations |
| **Baseline** | Minimally restrictive, prevents known escalations |
| **Restricted** | Heavily restricted, security best practices |

```yaml
# Apply to namespace
apiVersion: v1
kind: Namespace
metadata:
  name: secure-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

---

# Part 13: Advanced Topics

## Health Probes

### Liveness Probe

```yaml
spec:
  containers:
  - name: app
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 10
      failureThreshold: 3
```

### Readiness Probe

```yaml
spec:
  containers:
  - name: app
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
```

### Startup Probe

```yaml
spec:
  containers:
  - name: app
    startupProbe:
      httpGet:
        path: /healthz
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
```

## Horizontal Pod Autoscaler (HPA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

## Node Affinity and Taints

### Node Affinity

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```

### Taints and Tolerations

```bash
# Add taint to node
kubectl taint nodes node1 special=true:NoSchedule
```

```yaml
spec:
  tolerations:
  - key: "special"
    operator: "Equal"
    value: "true"
    effect: "NoSchedule"
```

## Resource Management

```yaml
spec:
  containers:
  - name: app
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "256Mi"
```

## Troubleshooting

### Common Commands

```bash
# Pod status
kubectl describe pod <pod-name>
kubectl logs <pod-name> --previous
kubectl logs <pod-name> -c <container>

# Events
kubectl get events --sort-by='.lastTimestamp'

# Debug pod
kubectl exec -it <pod-name> -- /bin/sh

# Resource usage
kubectl top pods
kubectl top nodes
```

### Common Issues

| Problem | Check | Solution |
|---------|-------|----------|
| Pod Pending | `kubectl describe pod` | Check resources, node availability |
| CrashLoopBackOff | `kubectl logs` | Fix application errors |
| ImagePullBackOff | Image name/registry | Verify image exists, check secrets |
| OOMKilled | Memory limits | Increase memory limits |

---

## 🎉 Congratulations!

You've completed the Kubernetes Zero to Hero course! You now have the knowledge to:

- ✅ Understand Kubernetes architecture
- ✅ Deploy and manage applications
- ✅ Configure networking and storage
- ✅ Secure your cluster with RBAC
- ✅ Use Helm for package management
- ✅ Implement health checks and autoscaling
- ✅ Troubleshoot common issues

---

## 📚 Additional Resources

- [Official Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes GitHub](https://github.com/kubernetes/kubernetes)
- [CNCF Landscape](https://landscape.cncf.io/)
- [Helm Documentation](https://helm.sh/docs/)

---

**Happy Orchestrating! ☸️**

