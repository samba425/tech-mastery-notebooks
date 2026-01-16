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

# Part 14: Real-World Production Patterns

## Complete Microservices Application Deployment

### E-Commerce Platform Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    Production K8s Cluster                        │
│                                                                  │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐         │
│  │  Ingress   │────▶│   Frontend │────▶│   Backend  │         │
│  │  (NGINX)   │     │   (React)  │     │   (Node.js)│         │
│  └────────────┘     └────────────┘     └────────────┘         │
│        │                                      │                 │
│        │            ┌────────────┐           │                 │
│        └───────────▶│   Static   │           │                 │
│                     │   Assets   │           │                 │
│                     └────────────┘           │                 │
│                                              ▼                 │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐        │
│  │  Auth      │◀────│   API      │────▶│  Payment   │        │
│  │  Service   │     │  Gateway   │     │  Service   │        │
│  └────────────┘     └────────────┘     └────────────┘        │
│        │                  │                   │                │
│        ▼                  ▼                   ▼                │
│  ┌────────────┐     ┌────────────┐     ┌────────────┐        │
│  │PostgreSQL  │     │   MongoDB  │     │   Redis    │        │
│  │(StatefulSet│     │(StatefulSet│     │(Deployment)│        │
│  └────────────┘     └────────────┘     └────────────┘        │
│                                                                │
│  ┌────────────────────────────────────────────────────┐       │
│  │  Monitoring Stack (Prometheus + Grafana)          │       │
│  └────────────────────────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────────┘
```

### 1. Namespace Organization

```yaml
# namespaces.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    environment: production
    team: platform
---
apiVersion: v1
kind: Namespace
metadata:
  name: staging
  labels:
    environment: staging
    team: platform
---
apiVersion: v1
kind: Namespace
metadata:
  name: monitoring
  labels:
    purpose: observability
```

### 2. Complete Frontend Deployment (React SPA)

```yaml
# frontend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: production
  labels:
    app: frontend
    tier: presentation
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
        version: v1.2.0
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - frontend
              topologyKey: kubernetes.io/hostname
      containers:
      - name: frontend
        image: myregistry.io/frontend:v1.2.0
        ports:
        - containerPort: 80
          name: http
        env:
        - name: REACT_APP_API_URL
          valueFrom:
            configMapKeyRef:
              name: frontend-config
              key: api.url
        - name: REACT_APP_ENV
          value: "production"
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
      volumes:
      - name: nginx-config
        configMap:
          name: nginx-config
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: production
spec:
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 80
    name: http
  type: ClusterIP
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: frontend-config
  namespace: production
data:
  api.url: "https://api.myapp.com"
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
  namespace: production
data:
  nginx.conf: |
    events {
        worker_connections 1024;
    }
    http {
        include mime.types;
        default_type application/octet-stream;
        
        gzip on;
        gzip_types text/plain text/css application/json application/javascript;
        
        server {
            listen 80;
            server_name _;
            root /usr/share/nginx/html;
            index index.html;
            
            location / {
                try_files $uri $uri/ /index.html;
            }
            
            location /health {
                return 200 'healthy';
                add_header Content-Type text/plain;
            }
            
            location /ready {
                return 200 'ready';
                add_header Content-Type text/plain;
            }
        }
    }
```

### 3. Backend API Service (Node.js + Express)

```yaml
# backend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-api
  namespace: production
  labels:
    app: backend-api
    tier: application
spec:
  replicas: 5
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2
      maxUnavailable: 1
  selector:
    matchLabels:
      app: backend-api
  template:
    metadata:
      labels:
        app: backend-api
        version: v2.1.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "3000"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: backend-api-sa
      initContainers:
      - name: wait-for-db
        image: busybox:1.28
        command: ['sh', '-c', 'until nc -z postgres-service 5432; do echo waiting for postgres; sleep 2; done;']
      containers:
      - name: backend-api
        image: myregistry.io/backend-api:v2.1.0
        ports:
        - containerPort: 3000
          name: http
        - containerPort: 9090
          name: metrics
        env:
        - name: NODE_ENV
          value: "production"
        - name: PORT
          value: "3000"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: backend-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            configMapKeyRef:
              name: backend-config
              key: redis.url
        - name: JWT_SECRET
          valueFrom:
            secretKeyRef:
              name: backend-secrets
              key: jwt-secret
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: backend-secrets
              key: api-key
        resources:
          requests:
            cpu: "200m"
            memory: "256Mi"
          limits:
            cpu: "1000m"
            memory: "1Gi"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          successThreshold: 1
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "sleep 15"]
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
---
apiVersion: v1
kind: Service
metadata:
  name: backend-api
  namespace: production
  labels:
    app: backend-api
spec:
  selector:
    app: backend-api
  ports:
  - port: 80
    targetPort: 3000
    name: http
  - port: 9090
    targetPort: 9090
    name: metrics
  type: ClusterIP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: backend-api-sa
  namespace: production
---
apiVersion: v1
kind: Secret
metadata:
  name: backend-secrets
  namespace: production
type: Opaque
stringData:
  database-url: "postgresql://user:password@postgres-service:5432/myapp"
  jwt-secret: "your-super-secret-jwt-key-change-in-production"
  api-key: "your-api-key-for-third-party-services"
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend-config
  namespace: production
data:
  redis.url: "redis://redis-service:6379"
  log.level: "info"
  rate.limit: "100"
```

### 4. PostgreSQL StatefulSet (Production-Ready)

```yaml
# postgres-statefulset.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-config
  namespace: production
data:
  POSTGRES_DB: "myapp"
  POSTGRES_USER: "appuser"
---
apiVersion: v1
kind: Secret
metadata:
  name: postgres-secret
  namespace: production
type: Opaque
stringData:
  POSTGRES_PASSWORD: "change-me-in-production"
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: production
spec:
  serviceName: postgres-service
  replicas: 1
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
        image: postgres:15-alpine
        ports:
        - containerPort: 5432
          name: postgres
        envFrom:
        - configMapRef:
            name: postgres-config
        - secretRef:
            name: postgres-secret
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
          subPath: postgres
        - name: postgres-init
          mountPath: /docker-entrypoint-initdb.d
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "2000m"
            memory: "4Gi"
        livenessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - appuser
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - appuser
          initialDelaySeconds: 5
          periodSeconds: 5
      volumes:
      - name: postgres-init
        configMap:
          name: postgres-init-script
  volumeClaimTemplates:
  - metadata:
      name: postgres-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 50Gi
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-service
  namespace: production
spec:
  selector:
    app: postgres
  ports:
  - port: 5432
    targetPort: 5432
  clusterIP: None
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-init-script
  namespace: production
data:
  init.sql: |
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      email VARCHAR(255) UNIQUE NOT NULL,
      password_hash VARCHAR(255) NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS products (
      id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      price DECIMAL(10,2) NOT NULL,
      stock INTEGER DEFAULT 0,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS orders (
      id SERIAL PRIMARY KEY,
      user_id INTEGER REFERENCES users(id),
      total_amount DECIMAL(10,2) NOT NULL,
      status VARCHAR(50) DEFAULT 'pending',
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX idx_orders_user_id ON orders(user_id);
    CREATE INDEX idx_orders_status ON orders(status);
```

### 5. Redis Cache Deployment

```yaml
# redis-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
          name: redis
        command:
        - redis-server
        - --appendonly
        - "yes"
        - --requirepass
        - "$(REDIS_PASSWORD)"
        env:
        - name: REDIS_PASSWORD
          valueFrom:
            secretKeyRef:
              name: redis-secret
              key: password
        volumeMounts:
        - name: redis-storage
          mountPath: /data
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
          limits:
            cpu: "500m"
            memory: "1Gi"
        livenessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
          periodSeconds: 5
      volumes:
      - name: redis-storage
        persistentVolumeClaim:
          claimName: redis-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: redis-service
  namespace: production
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
  type: ClusterIP
---
apiVersion: v1
kind: Secret
metadata:
  name: redis-secret
  namespace: production
type: Opaque
stringData:
  password: "redis-strong-password-change-me"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: redis-pvc
  namespace: production
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: fast-ssd
```

### 6. Production-Grade Ingress with TLS

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  namespace: production
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/limit-rps: "10"
    nginx.ingress.kubernetes.io/enable-cors: "true"
    nginx.ingress.kubernetes.io/cors-allow-methods: "GET, POST, PUT, DELETE, OPTIONS"
    nginx.ingress.kubernetes.io/cors-allow-origin: "https://myapp.com"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.com
    - www.myapp.com
    - api.myapp.com
    secretName: myapp-tls
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
  - host: www.myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
  - host: api.myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: backend-api
            port:
              number: 80
```

### 7. Horizontal Pod Autoscaler

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-api-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend-api
  minReplicas: 3
  maxReplicas: 20
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
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 30
      - type: Pods
        value: 4
        periodSeconds: 30
      selectPolicy: Max
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: frontend
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
```

### 8. Network Policies (Security)

```yaml
# network-policies.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-api-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend-api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  # Allow from frontend
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 3000
  # Allow from ingress controller
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 3000
  egress:
  # Allow to PostgreSQL
  - to:
    - podSelector:
        matchLabels:
          app: postgres
    ports:
    - protocol: TCP
      port: 5432
  # Allow to Redis
  - to:
    - podSelector:
        matchLabels:
          app: redis
    ports:
    - protocol: TCP
      port: 6379
  # Allow DNS
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
  # Allow HTTPS to external APIs
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 443
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: postgres-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: postgres
  policyTypes:
  - Ingress
  ingress:
  # Only allow from backend-api
  - from:
    - podSelector:
        matchLabels:
          app: backend-api
    ports:
    - protocol: TCP
      port: 5432
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: redis-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: redis
  policyTypes:
  - Ingress
  ingress:
  # Only allow from backend-api
  - from:
    - podSelector:
        matchLabels:
          app: backend-api
    ports:
    - protocol: TCP
      port: 6379
```

### 9. Pod Disruption Budget

```yaml
# pdb.yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: backend-api-pdb
  namespace: production
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: backend-api
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: frontend-pdb
  namespace: production
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: frontend
```

### 10. Resource Quotas and Limit Ranges

```yaml
# resource-limits.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: production-quota
  namespace: production
spec:
  hard:
    requests.cpu: "50"
    requests.memory: "100Gi"
    limits.cpu: "100"
    limits.memory: "200Gi"
    persistentvolumeclaims: "20"
    services.loadbalancers: "3"
---
apiVersion: v1
kind: LimitRange
metadata:
  name: production-limitrange
  namespace: production
spec:
  limits:
  - max:
      cpu: "4"
      memory: "8Gi"
    min:
      cpu: "50m"
      memory: "64Mi"
    default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "256Mi"
    type: Container
  - max:
      cpu: "8"
      memory: "16Gi"
    min:
      cpu: "100m"
      memory: "128Mi"
    type: Pod
```

---

# Part 15: Monitoring and Observability

## Complete Monitoring Stack

### 1. Prometheus Setup

```yaml
# prometheus-deployment.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
      evaluation_interval: 15s
    
    scrape_configs:
    - job_name: 'kubernetes-apiservers'
      kubernetes_sd_configs:
      - role: endpoints
      scheme: https
      tls_config:
        ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
      bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
      relabel_configs:
      - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
        action: keep
        regex: default;kubernetes;https
    
    - job_name: 'kubernetes-nodes'
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)
    
    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      serviceAccountName: prometheus
      containers:
      - name: prometheus
        image: prom/prometheus:v2.45.0
        args:
        - '--config.file=/etc/prometheus/prometheus.yml'
        - '--storage.tsdb.path=/prometheus'
        - '--storage.tsdb.retention.time=30d'
        ports:
        - containerPort: 9090
          name: http
        volumeMounts:
        - name: prometheus-config
          mountPath: /etc/prometheus
        - name: prometheus-storage
          mountPath: /prometheus
        resources:
          requests:
            cpu: "500m"
            memory: "2Gi"
          limits:
            cpu: "2000m"
            memory: "8Gi"
      volumes:
      - name: prometheus-config
        configMap:
          name: prometheus-config
      - name: prometheus-storage
        persistentVolumeClaim:
          claimName: prometheus-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: prometheus
  namespace: monitoring
spec:
  selector:
    app: prometheus
  ports:
  - port: 9090
    targetPort: 9090
  type: ClusterIP
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: prometheus
  namespace: monitoring
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus
rules:
- apiGroups: [""]
  resources:
  - nodes
  - nodes/proxy
  - services
  - endpoints
  - pods
  verbs: ["get", "list", "watch"]
- apiGroups:
  - extensions
  resources:
  - ingresses
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: prometheus
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: prometheus
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: monitoring
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: prometheus-pvc
  namespace: monitoring
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
  storageClassName: fast-ssd
```

### 2. Grafana Dashboards

```yaml
# grafana-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana:10.0.0
        ports:
        - containerPort: 3000
          name: http
        env:
        - name: GF_SECURITY_ADMIN_PASSWORD
          valueFrom:
            secretKeyRef:
              name: grafana-secret
              key: admin-password
        - name: GF_SERVER_ROOT_URL
          value: "https://grafana.myapp.com"
        volumeMounts:
        - name: grafana-storage
          mountPath: /var/lib/grafana
        - name: grafana-datasources
          mountPath: /etc/grafana/provisioning/datasources
        - name: grafana-dashboards
          mountPath: /etc/grafana/provisioning/dashboards
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
          limits:
            cpu: "500m"
            memory: "1Gi"
      volumes:
      - name: grafana-storage
        persistentVolumeClaim:
          claimName: grafana-pvc
      - name: grafana-datasources
        configMap:
          name: grafana-datasources
      - name: grafana-dashboards
        configMap:
          name: grafana-dashboards
---
apiVersion: v1
kind: Service
metadata:
  name: grafana
  namespace: monitoring
spec:
  selector:
    app: grafana
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP
---
apiVersion: v1
kind: Secret
metadata:
  name: grafana-secret
  namespace: monitoring
type: Opaque
stringData:
  admin-password: "change-me-in-production"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: grafana-pvc
  namespace: monitoring
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-datasources
  namespace: monitoring
data:
  prometheus.yaml: |
    apiVersion: 1
    datasources:
    - name: Prometheus
      type: prometheus
      access: proxy
      url: http://prometheus:9090
      isDefault: true
      editable: false
```

### 3. Logging with Fluentd

```yaml
# fluentd-daemonset.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: monitoring
  labels:
    app: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      serviceAccountName: fluentd
      containers:
      - name: fluentd
        image: fluent/fluentd-kubernetes-daemonset:v1-debian-elasticsearch
        env:
        - name: FLUENT_ELASTICSEARCH_HOST
          value: "elasticsearch.monitoring.svc.cluster.local"
        - name: FLUENT_ELASTICSEARCH_PORT
          value: "9200"
        - name: FLUENT_ELASTICSEARCH_SCHEME
          value: "http"
        resources:
          requests:
            cpu: "100m"
            memory: "256Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: fluentd
  namespace: monitoring
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: fluentd
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - namespaces
  verbs:
  - get
  - list
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: fluentd
roleRef:
  kind: ClusterRole
  name: fluentd
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: fluentd
  namespace: monitoring
```

---

# Part 16: CI/CD Integration

## GitOps with ArgoCD

### 1. ArgoCD Installation

```yaml
# argocd-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: argocd
```

```bash
# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get initial admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# Port forward to access UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

### 2. Application Definition

```yaml
# application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp-production
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/mycompany/myapp-k8s.git
    targetRevision: main
    path: production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
  revisionHistoryLimit: 10
```

### 3. CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
name: Build and Deploy

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Log in to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v4
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=semver,pattern={{version}}
          type=semver,pattern={{major}}.{{minor}}
          type=sha

    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - name: Checkout k8s repo
      uses: actions/checkout@v3
      with:
        repository: mycompany/myapp-k8s
        token: ${{ secrets.GIT_TOKEN }}

    - name: Update image tag
      run: |
        cd production
        sed -i "s|image: .*|image: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:sha-${GITHUB_SHA::7}|" deployment.yaml

    - name: Commit and push
      run: |
        git config user.name "GitHub Actions"
        git config user.email "actions@github.com"
        git add .
        git commit -m "Update image to sha-${GITHUB_SHA::7}"
        git push
```

---

# Part 17: Disaster Recovery & Backup

## Backup Strategies

### 1. Velero Setup (Cluster Backup)

```bash
# Install Velero CLI
wget https://github.com/vmware-tanzu/velero/releases/download/v1.11.0/velero-v1.11.0-linux-amd64.tar.gz
tar -xvf velero-v1.11.0-linux-amd64.tar.gz
sudo mv velero-v1.11.0-linux-amd64/velero /usr/local/bin/

# Install Velero in cluster (AWS example)
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.7.0 \
  --bucket my-backup-bucket \
  --backup-location-config region=us-east-1 \
  --snapshot-location-config region=us-east-1 \
  --secret-file ./credentials-velero

# Create backup schedule
velero schedule create daily-backup \
  --schedule="0 2 * * *" \
  --include-namespaces production,staging

# Backup specific namespace
velero backup create production-backup --include-namespaces production

# Restore from backup
velero restore create --from-backup production-backup
```

### 2. Database Backup CronJob

```yaml
# postgres-backup-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: postgres-backup
  namespace: production
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres:15-alpine
            command:
            - /bin/sh
            - -c
            - |
              TIMESTAMP=$(date +%Y%m%d_%H%M%S)
              pg_dump -h postgres-service -U appuser -d myapp > /backup/backup_${TIMESTAMP}.sql
              # Upload to S3
              aws s3 cp /backup/backup_${TIMESTAMP}.sql s3://my-backups/postgres/
              # Keep only last 30 days
              find /backup -name "backup_*.sql" -mtime +30 -delete
            env:
            - name: PGPASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: POSTGRES_PASSWORD
            volumeMounts:
            - name: backup-volume
              mountPath: /backup
          restartPolicy: OnFailure
          volumes:
          - name: backup-volume
            persistentVolumeClaim:
              claimName: postgres-backup-pvc
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-backup-pvc
  namespace: production
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
  storageClassName: standard
```

---

# Part 18: Cost Optimization

## Resource Optimization Strategies

### 1. Vertical Pod Autoscaler

```yaml
# vpa.yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: backend-api-vpa
  namespace: production
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend-api
  updatePolicy:
    updateMode: "Auto"
  resourcePolicy:
    containerPolicies:
    - containerName: backend-api
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
```

### 2. Cluster Autoscaler Configuration

```yaml
# cluster-autoscaler.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cluster-autoscaler
  template:
    metadata:
      labels:
        app: cluster-autoscaler
    spec:
      serviceAccountName: cluster-autoscaler
      containers:
      - image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.27.0
        name: cluster-autoscaler
        command:
        - ./cluster-autoscaler
        - --v=4
        - --stderrthreshold=info
        - --cloud-provider=aws
        - --skip-nodes-with-local-storage=false
        - --expander=least-waste
        - --node-group-auto-discovery=asg:tag=k8s.io/cluster-autoscaler/enabled,k8s.io/cluster-autoscaler/my-cluster
        - --balance-similar-node-groups
        - --skip-nodes-with-system-pods=false
        resources:
          limits:
            cpu: 100m
            memory: 300Mi
          requests:
            cpu: 100m
            memory: 300Mi
```

### 3. Pod Priority Classes

```yaml
# priority-classes.yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "High priority for critical services"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: medium-priority
value: 100000
globalDefault: false
description: "Medium priority for regular services"
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 10000
globalDefault: true
description: "Low priority for batch jobs"
```

Apply to deployments:

```yaml
spec:
  template:
    spec:
      priorityClassName: high-priority
      containers:
      - name: backend-api
        image: myapp:latest
```

---

# Part 19: Multi-Cluster Management

## Federation and Multi-Cluster Strategies

### 1. Kubefed (Kubernetes Federation)

```bash
# Install kubefedctl
curl -LO https://github.com/kubernetes-sigs/kubefed/releases/download/v0.10.0/kubefedctl-0.10.0-linux-amd64.tgz
tar -xzf kubefedctl-0.10.0-linux-amd64.tgz
sudo mv kubefedctl /usr/local/bin/

# Initialize federation
kubefedctl join cluster1 --cluster-context cluster1 \
  --host-cluster-context host-cluster

kubefedctl join cluster2 --cluster-context cluster2 \
  --host-cluster-context host-cluster
```

### 2. Federated Deployment

```yaml
# federated-deployment.yaml
apiVersion: types.kubefed.io/v1beta1
kind: FederatedDeployment
metadata:
  name: myapp
  namespace: default
spec:
  template:
    metadata:
      labels:
        app: myapp
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp
            image: myregistry.io/myapp:latest
  placement:
    clusters:
    - name: cluster1
    - name: cluster2
  overrides:
  - clusterName: cluster1
    clusterOverrides:
    - path: "/spec/replicas"
      value: 5
  - clusterName: cluster2
    clusterOverrides:
    - path: "/spec/replicas"
      value: 3
```

---

# Part 20: Troubleshooting Deep Dive

## Advanced Debugging Techniques

### 1. Debug Pod

```yaml
# debug-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: debug-pod
  namespace: production
spec:
  containers:
  - name: debug
    image: nicolaka/netshoot
    command: ["/bin/bash"]
    args: ["-c", "while true; do sleep 30; done"]
    securityContext:
      capabilities:
        add: ["NET_ADMIN", "SYS_ADMIN"]
```

```bash
# Execute into debug pod
kubectl exec -it debug-pod -n production -- /bin/bash

# Inside debug pod
# Test DNS
nslookup backend-api.production.svc.cluster.local

# Test connectivity
curl http://backend-api.production.svc.cluster.local

# Check network
tcpdump -i any port 3000

# Test postgres connectivity
nc -zv postgres-service 5432
```

### 2. Common Issues and Solutions

```bash
# 1. Pod stuck in Pending
kubectl describe pod <pod-name> -n production
# Check: Node resources, PVC binding, node affinity

# 2. Pod stuck in CrashLoopBackOff
kubectl logs <pod-name> -n production --previous
kubectl describe pod <pod-name> -n production
# Check: Application logs, liveness probes, resource limits

# 3. Service not accessible
kubectl get endpoints <service-name> -n production
kubectl port-forward svc/<service-name> 8080:80 -n production
# Check: Selector labels, pod readiness, network policies

# 4. High memory usage
kubectl top pods -n production --sort-by=memory
kubectl exec <pod-name> -n production -- cat /proc/meminfo
# Check: Memory leaks, increase limits, add HPA

# 5. DNS resolution failures
kubectl run -it --rm debug --image=busybox --restart=Never -- nslookup kubernetes.default
# Check: CoreDNS pods, DNS policies

# 6. PV/PVC issues
kubectl get pv
kubectl get pvc -n production
kubectl describe pvc <pvc-name> -n production
# Check: StorageClass, access modes, node affinity

# 7. Image pull errors
kubectl describe pod <pod-name> -n production | grep -A 10 Events
# Check: Image name, registry credentials, network

# 8. Node issues
kubectl describe node <node-name>
kubectl get node <node-name> -o yaml
# Check: Disk pressure, memory pressure, network

# 9. Resource quotas exceeded
kubectl describe quota -n production
# Check: Resource requests/limits

# 10. RBAC permission denied
kubectl auth can-i get pods --as=system:serviceaccount:production:backend-api-sa -n production
kubectl get rolebindings,clusterrolebindings -n production
# Check: ServiceAccount, Role, RoleBinding
```

### 3. Performance Profiling

```bash
# CPU profiling
kubectl top nodes
kubectl top pods -n production --containers

# Get resource metrics
kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes
kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/production/pods

# API server metrics
kubectl get --raw /metrics

# Etcd metrics
kubectl exec -it etcd-master -n kube-system -- etcdctl endpoint status

# Check pod events timeline
kubectl get events -n production --sort-by='.lastTimestamp'
```

---

## 🎉 Final Summary

You've completed the **comprehensive Kubernetes Zero to Hero course** covering:

### ✅ **Core Concepts** (Parts 1-13)
- Architecture, Pods, Deployments, Services
- Storage, ConfigMaps, Secrets
- Ingress, Helm, Security, Advanced Topics

### ✅ **Production Patterns** (Part 14)
- Complete microservices application
- Frontend, Backend, Databases
- Security, Autoscaling, Network Policies

### ✅ **Observability** (Part 15)
- Prometheus monitoring
- Grafana dashboards
- Fluentd logging

### ✅ **CI/CD** (Part 16)
- ArgoCD GitOps
- GitHub Actions pipelines

### ✅ **Operations** (Parts 17-20)
- Disaster recovery with Velero
- Cost optimization
- Multi-cluster management
- Advanced troubleshooting

---

## 🚀 Next Steps

1. **Practice**: Deploy the example applications in your cluster
2. **Experiment**: Modify configurations and observe behavior
3. **Production**: Apply these patterns to real workloads
4. **Certify**: Consider CKA, CKAD, or CKS certifications
5. **Contribute**: Join the Kubernetes community

---

## 📚 Additional Resources

- [Official Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes GitHub](https://github.com/kubernetes/kubernetes)
- [CNCF Landscape](https://landscape.cncf.io/)
- [Helm Documentation](https://helm.sh/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Kubernetes Patterns Book](https://k8spatterns.io/)

---

**Total Content: 5,500+ lines of production-ready Kubernetes knowledge!**

**Happy Orchestrating! ☸️**

