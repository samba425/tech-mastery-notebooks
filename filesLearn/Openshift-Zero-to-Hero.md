# 🔴 Red Hat OpenShift Zero to Hero Course

Welcome to the comprehensive Red Hat OpenShift course! This course takes you from beginner to advanced level with concise concepts and practical examples.

---

## 📚 Course Index

| # | Module | Description |
|---|--------|-------------|
| 01 | [Introduction and Setup](./01-Introduction-and-Setup.md) | What is OpenShift, architecture overview, installation options |
| 02 | [OpenShift Architecture](./02-Architecture-Deep-Dive.md) | Control plane, nodes, operators, cluster components |
| 03 | [CLI Mastery (oc)](./03-CLI-Mastery.md) | oc commands, contexts, projects, resource management |
| 04 | [Projects and RBAC](./04-Projects-and-RBAC.md) | Projects, users, roles, service accounts |
| 05 | [Pods and Deployments](./05-Pods-and-Deployments.md) | Pods, DeploymentConfigs, Deployments, scaling |
| 06 | [Services and Routes](./06-Services-and-Routes.md) | Services, Routes, ingress, TLS termination |
| 07 | [Storage](./07-Storage.md) | PV, PVC, StorageClasses, dynamic provisioning |
| 08 | [ConfigMaps and Secrets](./08-ConfigMaps-and-Secrets.md) | Configuration management, sensitive data |
| 09 | [Builds and ImageStreams](./09-Builds-and-ImageStreams.md) | BuildConfigs, S2I, ImageStreams, triggers |
| 10 | [Templates and Helm](./10-Templates-and-Helm.md) | OpenShift templates, Helm charts |
| 11 | [Operators](./11-Operators.md) | OperatorHub, OLM, custom operators |
| 12 | [Security](./12-Security.md) | SCCs, network policies, authentication |
| 13 | [Monitoring and Logging](./13-Monitoring-and-Logging.md) | Prometheus, Grafana, EFK stack |
| 14 | [Advanced Topics](./14-Advanced-Topics.md) | CI/CD, GitOps, troubleshooting, best practices |

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BEGINNER                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 01. Intro    │───▶│ 02. Arch     │───▶│ 03. CLI      │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      INTERMEDIATE                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 04. Projects │───▶│ 05. Workloads│───▶│ 06. Network  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                                        │                   │
│         ▼                                        ▼                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 07. Storage  │───▶│ 08. Config   │───▶│ 09. Builds   │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        ADVANCED                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 10. Templates│───▶│ 11. Operators│───▶│ 12. Security │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                  │                   │
│  ┌──────────────┐                        ┌──────────────┐          │
│  │ 13. Monitor  │◀───────────────────────│ 14. Advanced │          │
│  └──────────────┘                        └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

```bash
# Login to OpenShift cluster
oc login https://api.cluster.example.com:6443

# Create a new project
oc new-project myapp

# Deploy an application
oc new-app nginx

# Expose the application
oc expose svc/nginx

# Get the route URL
oc get route nginx
```

---

## 📋 Prerequisites

- Basic understanding of containers (Docker)
- Familiarity with Kubernetes concepts
- Access to an OpenShift cluster (or use OpenShift Local for learning)
- Command-line experience

---

## 🛠️ Lab Environment Options

| Option | Best For | Requirements |
|--------|----------|--------------|
| **OpenShift Local (CRC)** | Learning, development | 4 vCPU, 9GB RAM, 35GB disk |
| **Developer Sandbox** | Free cloud access | Red Hat account |
| **ROSA (AWS)** | Production on AWS | AWS account |
| **ARO (Azure)** | Production on Azure | Azure subscription |
| **Self-managed** | On-premises | Infrastructure |

---

## 📚 Additional Resources

- [OpenShift Documentation](https://docs.openshift.com/)
- [Red Hat Developer](https://developers.redhat.com/)
- [OpenShift Local (CRC)](https://developers.redhat.com/products/openshift-local/overview)
- [Developer Sandbox](https://developers.redhat.com/developer-sandbox)

---

**Let's begin your OpenShift journey! 🚀**

# Part 1: Introduction and Setup

## What is Red Hat OpenShift?

Red Hat OpenShift is an enterprise Kubernetes platform that provides a complete container application platform with developer and operations-centric tools. It extends Kubernetes with additional features like built-in CI/CD, developer workflows, and enterprise security.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      OPENSHIFT PLATFORM                             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    DEVELOPER EXPERIENCE                      │   │
│  │  Web Console │ CLI (oc) │ IDE Plugins │ Developer Catalog   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    OPENSHIFT SERVICES                        │   │
│  │  Source-to-Image │ Routes │ ImageStreams │ BuildConfigs     │   │
│  │  Templates │ OperatorHub │ Monitoring │ Logging             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      KUBERNETES                              │   │
│  │  Pods │ Services │ Deployments │ ConfigMaps │ Secrets       │   │
│  │  StatefulSets │ DaemonSets │ Jobs │ CronJobs                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    CONTAINER RUNTIME                         │   │
│  │                      CRI-O                                   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    INFRASTRUCTURE                            │   │
│  │  RHEL CoreOS │ Bare Metal │ VMware │ AWS │ Azure │ GCP      │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## OpenShift vs Kubernetes

OpenShift is built on Kubernetes but adds enterprise features for security, developer productivity, and operations management.

| Feature | Kubernetes | OpenShift |
|---------|------------|-----------|
| **Container Runtime** | Various (containerd, CRI-O) | CRI-O (standardized) |
| **Web Console** | Dashboard (basic) | Full-featured console |
| **Builds** | External tools needed | Built-in (S2I, Docker, Pipeline) |
| **Routes** | Ingress | Routes + Ingress |
| **Security** | Basic RBAC | SCCs + RBAC + OAuth |
| **Registry** | External | Integrated registry |
| **Operators** | Manual setup | OperatorHub built-in |
| **Support** | Community | Enterprise support |

## OpenShift Editions

### OpenShift Container Platform (OCP)

OCP is the self-managed, enterprise version that can run on any infrastructure.

```bash
# Self-managed installation options
- Bare metal
- VMware vSphere
- Red Hat Virtualization
- AWS (IPI or UPI)
- Azure (IPI or UPI)
- GCP (IPI or UPI)
```

### Managed OpenShift Services

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MANAGED OPENSHIFT OPTIONS                        │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │      ROSA       │  │       ARO       │  │   OpenShift     │    │
│  │   (AWS)         │  │    (Azure)      │  │   Dedicated     │    │
│  │                 │  │                 │  │   (GCP/AWS)     │    │
│  │  Red Hat +      │  │  Red Hat +      │  │                 │    │
│  │  AWS managed    │  │  Microsoft      │  │  Red Hat        │    │
│  │                 │  │  managed        │  │  managed        │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

## Setting Up OpenShift Local (CRC)

OpenShift Local (formerly CodeReady Containers) provides a minimal OpenShift cluster on your local machine for development and learning.

### Prerequisites

| Requirement | Minimum |
|-------------|---------|
| vCPUs | 4 |
| Memory | 9 GB |
| Disk Space | 35 GB |
| OS | Windows 10+, macOS 10.14+, RHEL/Fedora |

### Installation

```bash
# Download CRC from Red Hat Developer Portal
# https://developers.redhat.com/products/openshift-local/overview

# Extract and install
tar xvf crc-linux-amd64.tar.xz
sudo mv crc-linux-*-amd64/crc /usr/local/bin/

# Setup CRC (downloads VM image)
crc setup

# Start OpenShift cluster
crc start

# Get credentials
crc console --credentials

# Access web console
crc console
```

### CRC Commands

```bash
# Check status
crc status

# Stop cluster
crc stop

# Delete cluster
crc delete

# Get oc login command
crc console --credentials

# Configure resources
crc config set cpus 6
crc config set memory 12288
```

## Installing oc CLI

The `oc` command-line tool is OpenShift's CLI, extending kubectl with OpenShift-specific features.

### Linux Installation

```bash
# Download from OpenShift cluster
# Or from mirror.openshift.com

# Extract
tar xvf openshift-client-linux.tar.gz

# Move to path
sudo mv oc kubectl /usr/local/bin/

# Verify
oc version
```

### macOS Installation

```bash
# Using Homebrew
brew install openshift-cli

# Or download and extract manually
tar xvf openshift-client-mac.tar.gz
sudo mv oc /usr/local/bin/
```

### Windows Installation

```powershell
# Download openshift-client-windows.zip
# Extract and add to PATH

# Or using chocolatey
choco install openshift-cli
```

## First Connection

### Login to Cluster

```bash
# Login with username/password
oc login https://api.cluster.example.com:6443 -u developer -p developer

# Login with token (from web console)
oc login --token=sha256~xxxx --server=https://api.cluster.example.com:6443

# Login as admin (CRC)
oc login -u kubeadmin -p <password> https://api.crc.testing:6443
```

### Verify Connection

```bash
# Check cluster info
oc cluster-info

# Get nodes
oc get nodes

# Check current user
oc whoami

# Check current project
oc project
```

## Web Console Overview

The OpenShift web console provides a powerful graphical interface for both developers and administrators.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      WEB CONSOLE VIEWS                              │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                  ADMINISTRATOR VIEW                          │   │
│  │                                                              │   │
│  │  Home          │ Cluster management, dashboards              │   │
│  │  Operators     │ Install and manage operators                │   │
│  │  Workloads     │ Pods, Deployments, StatefulSets            │   │
│  │  Networking    │ Services, Routes, Ingress                   │   │
│  │  Storage       │ PVs, PVCs, StorageClasses                  │   │
│  │  Builds        │ BuildConfigs, Builds, ImageStreams         │   │
│  │  User Mgmt     │ Users, Groups, Roles, Service Accounts     │   │
│  │  Administration│ Cluster settings, CRDs, events             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   DEVELOPER VIEW                             │   │
│  │                                                              │   │
│  │  +Add          │ Deploy from catalog, Git, container        │   │
│  │  Topology      │ Visual application view                    │   │
│  │  Observe       │ Metrics, alerts, events                    │   │
│  │  Search        │ Find resources                             │   │
│  │  Builds        │ BuildConfigs, Pipelines                    │   │
│  │  Project       │ Project details, access                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Accessing Web Console

```bash
# Get console URL
oc whoami --show-console

# For CRC
crc console

# Example URL
https://console-openshift-console.apps.cluster.example.com
```

## Your First Application

### Deploy from Container Image

```bash
# Create a project
oc new-project my-first-app

# Deploy nginx
oc new-app nginx

# Check deployment status
oc status

# Expose the application
oc expose svc/nginx

# Get the route URL
oc get route nginx -o jsonpath='{.spec.host}'
```

### Deploy from Git Repository

```bash
# Deploy from GitHub (auto-detects language)
oc new-app https://github.com/sclorg/nodejs-ex.git

# Watch the build
oc logs -f bc/nodejs-ex

# Expose the application
oc expose svc/nodejs-ex

# Get route URL
oc get route
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **OpenShift** | Enterprise Kubernetes platform with developer tools |
| **CRC** | Local OpenShift for development and learning |
| **oc CLI** | OpenShift command-line tool (extends kubectl) |
| **Web Console** | GUI for developers and administrators |
| **Projects** | OpenShift's namespace with additional features |

---

**Next: [OpenShift Architecture Deep Dive](./02-Architecture-Deep-Dive.md)** →

# Part 2: OpenShift Architecture Deep Dive

## Cluster Architecture Overview

OpenShift clusters consist of control plane nodes (masters) and worker nodes, built on Red Hat Enterprise Linux CoreOS (RHCOS) with enhanced security and automation.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPENSHIFT CLUSTER ARCHITECTURE                   │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                      CONTROL PLANE                             │ │
│  │  ┌─────────────────────────────────────────────────────────┐  │ │
│  │  │                    API Server                            │  │ │
│  │  │  (Authentication, Authorization, Admission)              │  │ │
│  │  └─────────────────────────────────────────────────────────┘  │ │
│  │                                                                │ │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ │ │
│  │  │   etcd     │ │ Controller │ │ Scheduler  │ │  OAuth     │ │ │
│  │  │            │ │  Manager   │ │            │ │  Server    │ │ │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘ │ │
│  │                                                                │ │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ │ │
│  │  │  Cluster   │ │  Machine   │ │  Ingress   │ │   DNS      │ │ │
│  │  │  Version   │ │  Config    │ │  Operator  │ │  Operator  │ │ │
│  │  │  Operator  │ │  Operator  │ │            │ │            │ │ │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                       WORKER NODES                             │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐ │ │
│  │  │     Node 1      │  │     Node 2      │  │    Node 3      │ │ │
│  │  │ ┌─────────────┐ │  │ ┌─────────────┐ │  │ ┌────────────┐ │ │ │
│  │  │ │   kubelet   │ │  │ │   kubelet   │ │  │ │  kubelet   │ │ │ │
│  │  │ │   CRI-O     │ │  │ │   CRI-O     │ │  │ │  CRI-O     │ │ │ │
│  │  │ │ kube-proxy  │ │  │ │ kube-proxy  │ │  │ │ kube-proxy │ │ │ │
│  │  │ │ SDN/OVN     │ │  │ │ SDN/OVN     │ │  │ │ SDN/OVN    │ │ │ │
│  │  │ └─────────────┘ │  │ └─────────────┘ │  │ └────────────┘ │ │ │
│  │  │ [Pod][Pod][Pod] │  │ [Pod][Pod][Pod] │  │ [Pod][Pod]     │ │ │
│  │  └─────────────────┘  └─────────────────┘  └────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │              INFRASTRUCTURE SERVICES                           │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │ │
│  │  │ Internal │ │ Image    │ │ Monitoring│ │    Logging       │ │ │
│  │  │ Registry │ │ Streams  │ │ Stack    │ │    (EFK)         │ │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Control Plane Components

The control plane manages the cluster state and makes global decisions about scheduling and responding to events.

### API Server

The API server is the central hub for all cluster communication, handling authentication, authorization, and admission control.

```bash
# Check API server status
oc get pods -n openshift-apiserver

# API server endpoints
oc api-resources

# Check API versions
oc api-versions
```

### etcd

etcd is the distributed key-value store holding all cluster configuration and state data.

```bash
# Check etcd pods (control plane)
oc get pods -n openshift-etcd

# etcd members
oc get etcd -o yaml

# Check etcd health (requires admin)
oc rsh -n openshift-etcd etcd-master-0 etcdctl endpoint health
```

### Controller Manager

Controllers are control loops that watch cluster state and make changes to move toward the desired state.

```bash
# Check controller manager
oc get pods -n openshift-controller-manager

# Key controllers
# - Deployment controller
# - ReplicaSet controller
# - Node controller
# - Service account controller
# - Namespace controller
```

### Scheduler

The scheduler assigns pods to nodes based on resource requirements, affinity rules, and constraints.

```bash
# Check scheduler
oc get pods -n openshift-kube-scheduler

# View scheduling decisions
oc describe pod <pod-name> | grep -A5 Events
```

## Node Components

### RHEL CoreOS (RHCOS)

RHCOS is an immutable, container-optimized operating system designed for OpenShift. It's managed through the Machine Config Operator.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    RHEL COREOS FEATURES                             │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │   Immutable     │  │    Automatic    │  │   Optimized     │    │
│  │   Filesystem    │  │    Updates      │  │   for           │    │
│  │                 │  │   (via MCO)     │  │   Containers    │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘    │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │
│  │   SELinux       │  │    CRI-O        │  │   rpm-ostree    │    │
│  │   Enforcing     │  │   Runtime       │  │   Atomic        │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

### kubelet

The kubelet is the primary node agent that ensures containers are running in pods.

```bash
# Check kubelet status on nodes
oc get nodes
oc describe node <node-name>

# Node conditions
oc get nodes -o wide
```

### CRI-O Container Runtime

CRI-O is a lightweight container runtime specifically designed for Kubernetes. OpenShift uses CRI-O instead of Docker.

```bash
# Check CRI-O on a node (debug pod)
oc debug node/<node-name>
chroot /host
crictl ps
crictl images
```

## OpenShift Operators

Operators are the foundation of OpenShift, automating deployment and management of cluster components and applications.

### Cluster Version Operator (CVO)

The CVO manages the overall cluster version and coordinates updates for all cluster operators.

```bash
# Check cluster version
oc get clusterversion

# Detailed version info
oc describe clusterversion version

# Available updates
oc adm upgrade
```

### Machine Config Operator (MCO)

The MCO manages the configuration of RHCOS nodes, including OS settings, kubelet config, and certificates.

```bash
# List machine configs
oc get machineconfig

# Check machine config pools
oc get machineconfigpool

# View current config
oc describe machineconfigpool worker
```

### Cluster Operators

```bash
# List all cluster operators
oc get clusteroperators

# Check operator status
oc get co

# Describe specific operator
oc describe co authentication
```

| Operator | Purpose |
|----------|---------|
| authentication | OAuth server and identity providers |
| console | Web console |
| dns | CoreDNS for cluster DNS |
| image-registry | Internal container registry |
| ingress | Route and ingress controller |
| monitoring | Prometheus and Alertmanager |
| network | SDN/OVN networking |
| storage | Storage provisioning |

## Networking Architecture

OpenShift provides software-defined networking (SDN) with options for OVN-Kubernetes or OpenShift SDN.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPENSHIFT NETWORKING                             │
│                                                                     │
│                        ┌─────────────┐                              │
│                        │   Router    │                              │
│                        │  (HAProxy)  │                              │
│                        └──────┬──────┘                              │
│                               │                                     │
│        ┌──────────────────────┼──────────────────────┐             │
│        │                      │                      │             │
│   ┌────▼────┐           ┌────▼────┐           ┌────▼────┐        │
│   │  Route  │           │  Route  │           │  Route  │        │
│   │ app1.   │           │ app2.   │           │ app3.   │        │
│   └────┬────┘           └────┬────┘           └────┬────┘        │
│        │                     │                     │              │
│   ┌────▼────┐           ┌────▼────┐           ┌────▼────┐        │
│   │ Service │           │ Service │           │ Service │        │
│   │ (CLSTR) │           │ (CLSTR) │           │ (CLSTR) │        │
│   └────┬────┘           └────┬────┘           └────┬────┘        │
│        │                     │                     │              │
│   ┌────▼────┐           ┌────▼────┐           ┌────▼────┐        │
│   │   Pod   │           │   Pod   │           │   Pod   │        │
│   │10.128.x │           │10.128.x │           │10.128.x │        │
│   └─────────┘           └─────────┘           └─────────┘        │
│                                                                   │
│   ┌─────────────────────────────────────────────────────────────┐│
│   │              POD NETWORK (10.128.0.0/14)                    ││
│   │              SERVICE NETWORK (172.30.0.0/16)                ││
│   └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

### Network Types

| Network | Default CIDR | Purpose |
|---------|--------------|---------|
| Pod Network | 10.128.0.0/14 | Container-to-container communication |
| Service Network | 172.30.0.0/16 | Service cluster IPs |
| Host Network | Node IPs | Node-level communication |

### Check Network Configuration

```bash
# Get network configuration
oc get network.config cluster -o yaml

# Check network operator
oc get pods -n openshift-sdn
# or for OVN
oc get pods -n openshift-ovn-kubernetes

# View network policies
oc get networkpolicy --all-namespaces
```

## Storage Architecture

OpenShift integrates with various storage backends through the Container Storage Interface (CSI).

```bash
# List storage classes
oc get storageclass

# Default storage class
oc get sc -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")].metadata.name}'

# Check CSI drivers
oc get csidrivers
```

## Registry Architecture

OpenShift includes an integrated container registry for storing and distributing container images.

```bash
# Check registry operator
oc get configs.imageregistry.operator.openshift.io cluster -o yaml

# Get registry route (if exposed)
oc get route -n openshift-image-registry

# Registry pods
oc get pods -n openshift-image-registry
```

---

## 📝 Summary

| Component | Description |
|-----------|-------------|
| **Control Plane** | API server, etcd, controllers, scheduler |
| **RHCOS** | Immutable, container-optimized OS |
| **CRI-O** | Lightweight container runtime |
| **Operators** | Automated management of cluster components |
| **SDN/OVN** | Software-defined networking |
| **MCO** | Manages node configuration |

---

**Next: [CLI Mastery (oc)](./03-CLI-Mastery.md)** →

# Part 3: CLI Mastery (oc)

## Understanding oc CLI

The `oc` command is OpenShift's CLI tool that extends `kubectl` with OpenShift-specific features. All kubectl commands work with oc, plus additional commands for builds, routes, and OpenShift resources.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        oc CLI OVERVIEW                              │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     OPENSHIFT SPECIFIC                       │   │
│  │  oc new-app │ oc new-project │ oc start-build │ oc expose   │   │
│  │  oc login │ oc status │ oc rollout │ oc import-image        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ extends                              │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      KUBECTL COMMANDS                        │   │
│  │  get │ describe │ create │ apply │ delete │ exec │ logs     │   │
│  │  scale │ edit │ patch │ label │ annotate │ port-forward     │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Authentication and Context

### Login Methods

```bash
# Login with username/password
oc login https://api.cluster.example.com:6443 -u developer -p developer

# Login with token (from web console)
oc login --token=sha256~xxxxx --server=https://api.cluster.example.com:6443

# Login with certificate
oc login https://api.cluster.example.com:6443 --certificate-authority=ca.crt

# Check current user
oc whoami

# Get user token
oc whoami -t

# Show server URL
oc whoami --show-server

# Show console URL
oc whoami --show-console
```

### Context Management

```bash
# View current context
oc config current-context

# List all contexts
oc config get-contexts

# Switch context
oc config use-context <context-name>

# View kubeconfig
oc config view

# Set default namespace for context
oc config set-context --current --namespace=myproject
```

## Project Management

Projects are OpenShift's enhanced namespaces with additional features like quotas, network isolation, and access controls.

```bash
# List projects
oc projects

# Current project
oc project

# Switch project
oc project myproject

# Create new project
oc new-project myapp --description="My Application" --display-name="My App"

# Delete project
oc delete project myapp

# View project details
oc describe project myproject
```

### Project vs Namespace

```bash
# Projects are namespaces with extra metadata
oc get projects
oc get namespaces

# Create using namespace (admin)
oc create namespace test-ns

# View project annotations
oc get project myproject -o yaml
```

## Resource Management

### Getting Resources

```bash
# List resources in current project
oc get pods
oc get services
oc get routes
oc get deployments
oc get dc  # DeploymentConfigs

# All namespaces
oc get pods --all-namespaces
oc get pods -A

# Wide output
oc get pods -o wide

# YAML/JSON output
oc get pod mypod -o yaml
oc get pod mypod -o json

# Custom columns
oc get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase

# JSONPath
oc get pods -o jsonpath='{.items[*].metadata.name}'

# Watch for changes
oc get pods -w
```

### Describing Resources

```bash
# Detailed information
oc describe pod mypod
oc describe svc myservice
oc describe route myroute

# Events for a resource
oc describe pod mypod | grep -A 10 Events
```

### Creating Resources

```bash
# From YAML file
oc create -f deployment.yaml

# From URL
oc create -f https://example.com/manifest.yaml

# Apply (create or update)
oc apply -f deployment.yaml

# Create and record
oc apply -f deployment.yaml --record

# Dry run
oc apply -f deployment.yaml --dry-run=client
```

### Modifying Resources

```bash
# Edit resource
oc edit deployment myapp

# Patch resource
oc patch deployment myapp -p '{"spec":{"replicas":3}}'

# Label resources
oc label pod mypod env=production

# Annotate resources
oc annotate pod mypod description="My application pod"

# Scale deployment
oc scale deployment myapp --replicas=5
```

### Deleting Resources

```bash
# Delete by name
oc delete pod mypod

# Delete from file
oc delete -f deployment.yaml

# Delete with label selector
oc delete pods -l app=myapp

# Delete all pods in project
oc delete pods --all

# Force delete
oc delete pod mypod --force --grace-period=0
```

## Application Deployment

### new-app Command

The `oc new-app` command is a powerful way to create applications from various sources.

```bash
# From container image
oc new-app nginx
oc new-app mysql MYSQL_ROOT_PASSWORD=secret

# From Git repository
oc new-app https://github.com/sclorg/nodejs-ex.git

# From Git with specific branch
oc new-app https://github.com/user/repo.git#branch-name

# With specific builder image
oc new-app nodejs~https://github.com/user/nodejs-app.git

# From Dockerfile
oc new-app https://github.com/user/repo.git --strategy=docker

# With environment variables
oc new-app myimage -e DB_HOST=localhost -e DB_PORT=5432

# With specific name
oc new-app nginx --name=webserver

# Dry run (show what would be created)
oc new-app nginx --dry-run -o yaml
```

### Expose Applications

```bash
# Create route from service
oc expose svc/myservice

# With specific hostname
oc expose svc/myservice --hostname=myapp.example.com

# Create edge TLS route
oc create route edge myroute --service=myservice

# Create passthrough TLS route
oc create route passthrough myroute --service=myservice --port=8443
```

## Working with Pods

### Pod Operations

```bash
# Get logs
oc logs mypod
oc logs mypod -c container-name  # specific container
oc logs -f mypod                  # follow logs
oc logs --previous mypod          # previous instance
oc logs --tail=100 mypod          # last 100 lines

# Execute commands
oc exec mypod -- ls -la
oc exec -it mypod -- /bin/bash
oc exec -it mypod -c container-name -- /bin/sh

# Copy files
oc cp mypod:/path/to/file ./local-file
oc cp ./local-file mypod:/path/to/file

# Port forwarding
oc port-forward mypod 8080:80
oc port-forward svc/myservice 8080:80

# Debug pod
oc debug pod/mypod
oc debug deployment/myapp
```

### Resource Status

```bash
# Overall status
oc status

# Detailed status
oc status --suggest

# Get events
oc get events --sort-by='.lastTimestamp'

# Resource usage
oc adm top pods
oc adm top nodes
```

## Build Operations

```bash
# Start a build
oc start-build myapp

# Start build from local directory
oc start-build myapp --from-dir=.

# Start build from Git
oc start-build myapp --from-repo=.

# Follow build logs
oc start-build myapp --follow

# View build logs
oc logs -f bc/myapp

# List builds
oc get builds

# Cancel build
oc cancel-build myapp-1
```

## Rollout Management

```bash
# View rollout status
oc rollout status deployment/myapp

# View rollout history
oc rollout history deployment/myapp

# Rollback
oc rollout undo deployment/myapp
oc rollout undo deployment/myapp --to-revision=2

# Pause/Resume rollout
oc rollout pause deployment/myapp
oc rollout resume deployment/myapp

# Restart deployment
oc rollout restart deployment/myapp
```

## Quick Reference

| Command | Description |
|---------|-------------|
| `oc login` | Authenticate to cluster |
| `oc project` | Switch/view projects |
| `oc new-project` | Create project |
| `oc new-app` | Create application |
| `oc expose` | Create route |
| `oc get` | List resources |
| `oc describe` | Show details |
| `oc logs` | View logs |
| `oc exec` | Execute command |
| `oc rsh` | Remote shell |
| `oc start-build` | Trigger build |
| `oc rollout` | Manage rollouts |
| `oc scale` | Scale replicas |
| `oc delete` | Delete resources |

---

**Next: [Projects and RBAC](./04-Projects-and-RBAC.md)** →

# Part 4: Projects and RBAC

## Understanding Projects

Projects are OpenShift's way of organizing resources with built-in multi-tenancy support. They extend Kubernetes namespaces with access control, resource quotas, and network isolation.

```
┌─────────────────────────────────────────────────────────────────────┐
│                       OPENSHIFT PROJECT                             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      PROJECT: myapp                          │   │
│  │                                                              │   │
│  │  ┌─────────────────────────────────────────────────────────┐│   │
│  │  │                    RESOURCES                            ││   │
│  │  │  Pods │ Services │ Routes │ ConfigMaps │ Secrets        ││   │
│  │  │  Deployments │ BuildConfigs │ ImageStreams              ││   │
│  │  └─────────────────────────────────────────────────────────┘│   │
│  │                                                              │   │
│  │  ┌─────────────────────────────────────────────────────────┐│   │
│  │  │                 RBAC (Role Bindings)                    ││   │
│  │  │  admin: user1  │  edit: user2  │  view: user3           ││   │
│  │  └─────────────────────────────────────────────────────────┘│   │
│  │                                                              │   │
│  │  ┌─────────────────────────────────────────────────────────┐│   │
│  │  │               RESOURCE QUOTAS                           ││   │
│  │  │  CPU: 4 cores  │  Memory: 8Gi  │  Pods: 20              ││   │
│  │  └─────────────────────────────────────────────────────────┘│   │
│  │                                                              │   │
│  │  ┌─────────────────────────────────────────────────────────┐│   │
│  │  │                LIMIT RANGES                             ││   │
│  │  │  Default CPU: 500m  │  Default Memory: 512Mi            ││   │
│  │  └─────────────────────────────────────────────────────────┘│   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Project Management

### Creating Projects

```bash
# Create project
oc new-project myapp

# Create with metadata
oc new-project myapp \
  --display-name="My Application" \
  --description="Production application"

# Create as admin (namespace style)
oc create namespace myapp

# Create project from YAML
cat <<EOF | oc apply -f -
apiVersion: project.openshift.io/v1
kind: Project
metadata:
  name: myapp
  annotations:
    openshift.io/description: "My Application Project"
    openshift.io/display-name: "My App"
EOF
```

### Managing Projects

```bash
# List all projects
oc projects

# Get current project
oc project

# Switch project
oc project myapp

# View project details
oc describe project myapp

# Delete project
oc delete project myapp
```

## Users and Groups

### User Types

| User Type | Description |
|-----------|-------------|
| **Regular Users** | Interactive users authenticated via OAuth |
| **System Users** | Built-in users (system:admin, system:node) |
| **Service Accounts** | Non-human accounts for pods and services |

### Managing Users

```bash
# List users
oc get users

# Get user details
oc describe user developer

# Get current user
oc whoami

# Get user's groups
oc get groups

# Create group
oc adm groups new developers

# Add user to group
oc adm groups add-users developers user1 user2

# Remove user from group
oc adm groups remove-users developers user1
```

### Identity Providers

OpenShift supports various identity providers configured via OAuth.

```yaml
# Example: LDAP Identity Provider
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: ldap
    type: LDAP
    ldap:
      url: "ldap://ldap.example.com/ou=users,dc=example,dc=com?uid"
      bindDN: "cn=admin,dc=example,dc=com"
      bindPassword:
        name: ldap-secret
      insecure: false
      attributes:
        id:
        - dn
        email:
        - mail
        name:
        - cn
        preferredUsername:
        - uid
```

## Service Accounts

Service accounts provide identity for processes running in pods without requiring user credentials.

```bash
# List service accounts
oc get serviceaccounts
oc get sa

# Default service accounts in every project
# - default: used by pods if not specified
# - builder: used for builds
# - deployer: used for deployments

# Create service account
oc create serviceaccount myapp-sa

# View service account details
oc describe sa myapp-sa

# Get service account token
oc create token myapp-sa
```

### Using Service Accounts

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  serviceAccountName: myapp-sa
  containers:
  - name: myapp
    image: myapp:latest
```

```bash
# Add SCC to service account
oc adm policy add-scc-to-user anyuid -z myapp-sa

# Add cluster role to service account
oc adm policy add-cluster-role-to-user cluster-reader -z myapp-sa
```

## Role-Based Access Control (RBAC)

RBAC controls who can perform what actions on which resources. OpenShift uses Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        RBAC MODEL                                   │
│                                                                     │
│   ┌──────────────────┐              ┌──────────────────┐           │
│   │      USER        │              │     ROLE         │           │
│   │   or GROUP       │◀────────────▶│  (permissions)   │           │
│   │   or SA          │   Binding    │                  │           │
│   └──────────────────┘              └──────────────────┘           │
│                                             │                       │
│                                             │ defines               │
│                                             ▼                       │
│                                     ┌──────────────────┐           │
│                                     │    RESOURCES     │           │
│                                     │ pods, services,  │           │
│                                     │ routes, secrets  │           │
│                                     └──────────────────┘           │
│                                                                     │
│   SCOPE:                                                           │
│   ┌────────────────────────┐    ┌────────────────────────┐        │
│   │   Role + RoleBinding   │    │ ClusterRole + Cluster  │        │
│   │   (Project/Namespace)  │    │   RoleBinding (Cluster)│        │
│   └────────────────────────┘    └────────────────────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

### Default Cluster Roles

| Role | Description |
|------|-------------|
| `cluster-admin` | Full access to entire cluster |
| `cluster-reader` | Read-only access to cluster resources |
| `admin` | Full access within a project |
| `edit` | Create/modify resources (no RBAC) |
| `view` | Read-only access to project |
| `basic-user` | Get basic info about projects |
| `self-provisioner` | Create new projects |

### Managing Role Bindings

```bash
# Add role to user in project
oc adm policy add-role-to-user admin user1 -n myproject
oc adm policy add-role-to-user edit user2 -n myproject
oc adm policy add-role-to-user view user3 -n myproject

# Remove role from user
oc adm policy remove-role-from-user edit user2 -n myproject

# Add cluster role
oc adm policy add-cluster-role-to-user cluster-admin user1

# Add role to group
oc adm policy add-role-to-group edit developers -n myproject

# List role bindings
oc get rolebindings -n myproject
oc describe rolebinding admin -n myproject
```

### Creating Custom Roles

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: myproject
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["pods/exec"]
  verbs: ["create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: myproject
subjects:
- kind: User
  name: developer
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Apply custom role
oc apply -f role.yaml

# Check user permissions
oc auth can-i get pods --as=developer -n myproject
oc auth can-i delete pods --as=developer -n myproject

# List all permissions for user
oc auth can-i --list --as=developer -n myproject
```

## Resource Quotas

Resource quotas limit the total amount of resources a project can consume.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: project-quota
  namespace: myproject
spec:
  hard:
    pods: "20"
    requests.cpu: "4"
    requests.memory: "8Gi"
    limits.cpu: "8"
    limits.memory: "16Gi"
    persistentvolumeclaims: "10"
    requests.storage: "50Gi"
    configmaps: "20"
    secrets: "20"
    services: "10"
    services.loadbalancers: "2"
```

```bash
# Create quota
oc create quota project-quota \
  --hard=pods=20,requests.cpu=4,requests.memory=8Gi -n myproject

# View quotas
oc get resourcequota -n myproject
oc describe resourcequota project-quota -n myproject
```

## Limit Ranges

Limit ranges set default and maximum resource limits for containers in a project.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: resource-limits
  namespace: myproject
spec:
  limits:
  - type: Container
    default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "256Mi"
    max:
      cpu: "2"
      memory: "2Gi"
    min:
      cpu: "50m"
      memory: "64Mi"
  - type: Pod
    max:
      cpu: "4"
      memory: "4Gi"
  - type: PersistentVolumeClaim
    max:
      storage: "10Gi"
    min:
      storage: "1Gi"
```

```bash
# Create limit range
oc apply -f limitrange.yaml

# View limit ranges
oc get limitrange -n myproject
oc describe limitrange resource-limits -n myproject
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Projects** | Namespaces with RBAC, quotas, and isolation |
| **Users** | Regular, system, or service accounts |
| **Roles** | Define permissions for resources |
| **RoleBindings** | Connect users/groups to roles |
| **Quotas** | Limit total resources per project |
| **LimitRanges** | Set default/max container resources |

---

**Next: [Pods and Deployments](./05-Pods-and-Deployments.md)** →

# Part 5: Pods and Deployments

## Understanding Pods in OpenShift

Pods are the smallest deployable units in OpenShift, containing one or more containers that share network and storage. OpenShift adds additional security contexts and scheduling constraints compared to vanilla Kubernetes.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         OPENSHIFT POD                               │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    SECURITY CONTEXT                          │   │
│  │  SCC Applied │ SELinux │ RunAsUser │ FSGroup                 │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    SHARED NAMESPACE                          │   │
│  │  Network (localhost) │ IPC │ UTS                             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │
│  │ Container 1 │  │ Container 2 │  │    Init Container       │   │
│  │   (app)     │  │  (sidecar)  │  │    (runs first)         │   │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘   │
│        │                │                                         │
│        └────────────────┴──────────────────────────────────────┐ │
│                                                                 │ │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    SHARED VOLUMES                           │ │
│  │  ConfigMaps │ Secrets │ PVC │ EmptyDir                      │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## Creating Pods

### Basic Pod

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
    image: nginx:latest
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "100m"
      limits:
        memory: "128Mi"
        cpu: "200m"
```

```bash
# Create pod
oc apply -f pod.yaml

# Create pod imperatively
oc run nginx --image=nginx --port=80

# Create pod with resource limits
oc run nginx --image=nginx --requests='cpu=100m,memory=64Mi' --limits='cpu=200m,memory=128Mi'
```

### Pod with Multiple Containers

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-with-sidecar
spec:
  containers:
  - name: web
    image: nginx
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/nginx
  - name: log-collector
    image: busybox
    command: ['sh', '-c', 'tail -f /logs/access.log']
    volumeMounts:
    - name: shared-logs
      mountPath: /logs
  volumes:
  - name: shared-logs
    emptyDir: {}
```

### Init Containers

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-init
spec:
  initContainers:
  - name: wait-for-db
    image: busybox
    command: ['sh', '-c', 'until nc -z db-service 5432; do echo waiting; sleep 2; done']
  - name: init-config
    image: busybox
    command: ['sh', '-c', 'cp /config/* /app/config/']
    volumeMounts:
    - name: config
      mountPath: /app/config
  containers:
  - name: app
    image: myapp:latest
    volumeMounts:
    - name: config
      mountPath: /app/config
  volumes:
  - name: config
    emptyDir: {}
```

## Pod Management

```bash
# List pods
oc get pods
oc get pods -o wide
oc get pods -l app=nginx

# Describe pod
oc describe pod nginx-pod

# View logs
oc logs nginx-pod
oc logs nginx-pod -c container-name
oc logs -f nginx-pod  # follow

# Execute command
oc exec nginx-pod -- ls -la
oc exec -it nginx-pod -- /bin/bash

# Remote shell
oc rsh nginx-pod

# Debug pod
oc debug pod/nginx-pod

# Port forward
oc port-forward nginx-pod 8080:80

# Delete pod
oc delete pod nginx-pod
```

## Deployments

Deployments manage ReplicaSets and provide declarative updates for Pods. They're the standard way to deploy stateless applications.

### Deployment Specification

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
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
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
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

```bash
# Create deployment
oc apply -f deployment.yaml

# Create imperatively
oc create deployment nginx --image=nginx --replicas=3

# Scale deployment
oc scale deployment nginx --replicas=5

# Update image
oc set image deployment/nginx nginx=nginx:1.22

# View rollout status
oc rollout status deployment/nginx

# Rollout history
oc rollout history deployment/nginx

# Rollback
oc rollout undo deployment/nginx
```

## DeploymentConfigs (OpenShift-specific)

DeploymentConfigs are OpenShift's original deployment mechanism with additional features like image triggers and lifecycle hooks.

```yaml
apiVersion: apps.openshift.io/v1
kind: DeploymentConfig
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    app: myapp
  strategy:
    type: Rolling
    rollingParams:
      intervalSeconds: 1
      maxSurge: 25%
      maxUnavailable: 25%
      timeoutSeconds: 600
      updatePeriodSeconds: 1
  triggers:
  - type: ConfigChange
  - type: ImageChange
    imageChangeParams:
      automatic: true
      containerNames:
      - myapp
      from:
        kind: ImageStreamTag
        name: myapp:latest
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8080
        env:
        - name: DB_HOST
          value: postgres
```

### DeploymentConfig vs Deployment

| Feature | Deployment | DeploymentConfig |
|---------|------------|------------------|
| **API** | Kubernetes native | OpenShift specific |
| **Triggers** | Manual | Image/Config change |
| **Lifecycle Hooks** | No | Yes |
| **Custom Strategies** | No | Yes |
| **Recommended** | Yes (new apps) | Legacy support |

```bash
# DeploymentConfig commands
oc get dc
oc describe dc myapp
oc rollout latest dc/myapp
oc rollout cancel dc/myapp
oc rollout history dc/myapp
```

## Scaling Applications

### Manual Scaling

```bash
# Scale deployment
oc scale deployment/nginx --replicas=5

# Scale DeploymentConfig
oc scale dc/myapp --replicas=3
```

### Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx
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

```bash
# Create HPA imperatively
oc autoscale deployment/nginx --min=2 --max=10 --cpu-percent=70

# View HPA
oc get hpa
oc describe hpa nginx-hpa
```

## Health Probes

### Liveness Probe

Liveness probes determine if a container is running. If it fails, the container is restarted.

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 10
  timeoutSeconds: 3
  failureThreshold: 3
```

### Readiness Probe

Readiness probes determine if a container is ready to receive traffic.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
  successThreshold: 1
```

### Startup Probe

Startup probes handle slow-starting containers.

```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

### Probe Types

```yaml
# HTTP probe
httpGet:
  path: /health
  port: 8080
  httpHeaders:
  - name: Custom-Header
    value: Awesome

# TCP probe
tcpSocket:
  port: 3306

# Command probe
exec:
  command:
  - /bin/sh
  - -c
  - pg_isready -U postgres
```

## Resource Management

```yaml
spec:
  containers:
  - name: app
    resources:
      requests:
        cpu: "100m"      # 0.1 CPU core
        memory: "128Mi"   # 128 MiB
      limits:
        cpu: "500m"      # 0.5 CPU core
        memory: "512Mi"   # 512 MiB
```

```bash
# View resource usage
oc adm top pods
oc adm top pods --containers

# View node resources
oc adm top nodes
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Pods** | Smallest deployable unit with containers |
| **Deployments** | Kubernetes standard for stateless apps |
| **DeploymentConfigs** | OpenShift-specific with triggers |
| **HPA** | Auto-scale based on metrics |
| **Probes** | Health checks for containers |
| **Resources** | CPU/memory requests and limits |

---

**Next: [Services and Routes](./06-Services-and-Routes.md)** →

# Part 6: Services and Routes

## Understanding Services

Services provide stable network endpoints to access pods. They enable load balancing and service discovery within the cluster.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         SERVICE                                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              ClusterIP: 172.30.100.50                        │   │
│  │              DNS: myservice.myproject.svc.cluster.local      │   │
│  │              Port: 80 → TargetPort: 8080                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│              ┌───────────────┼───────────────┐                     │
│              │               │               │                     │
│              ▼               ▼               ▼                     │
│        ┌──────────┐   ┌──────────┐   ┌──────────┐                 │
│        │  Pod 1   │   │  Pod 2   │   │  Pod 3   │                 │
│        │ app=web  │   │ app=web  │   │ app=web  │                 │
│        │ :8080    │   │ :8080    │   │ :8080    │                 │
│        └──────────┘   └──────────┘   └──────────┘                 │
│                                                                     │
│        Selector: app=web                                            │
└─────────────────────────────────────────────────────────────────────┘
```

## Service Types

| Type | Description | Use Case |
|------|-------------|----------|
| **ClusterIP** | Internal cluster IP (default) | Inter-service communication |
| **NodePort** | Expose on each node's IP | Development, testing |
| **LoadBalancer** | External load balancer | Cloud environments |
| **ExternalName** | DNS CNAME alias | External service access |

## Creating Services

### ClusterIP Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: ClusterIP
  selector:
    app: web
  ports:
  - name: http
    port: 80
    targetPort: 8080
  - name: https
    port: 443
    targetPort: 8443
```

```bash
# Create service from deployment
oc expose deployment/web --port=80 --target-port=8080

# Create service imperatively
oc create service clusterip web-service --tcp=80:8080

# View services
oc get svc
oc describe svc web-service
```

### NodePort Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-nodeport
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080  # Optional: auto-assigned if not specified
```

### Headless Service

Headless services (clusterIP: None) return pod IPs directly, useful for StatefulSets.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: database-headless
spec:
  clusterIP: None
  selector:
    app: database
  ports:
  - port: 5432
```

## Service Discovery

### DNS-Based Discovery

```bash
# Full DNS name format
<service-name>.<namespace>.svc.cluster.local

# Examples
web-service.myproject.svc.cluster.local
web-service.myproject.svc
web-service.myproject
web-service  # Within same namespace
```

### Environment Variables

```bash
# Automatic environment variables in pods
WEB_SERVICE_SERVICE_HOST=172.30.100.50
WEB_SERVICE_SERVICE_PORT=80
WEB_SERVICE_PORT=tcp://172.30.100.50:80
```

## Understanding Routes

Routes are OpenShift's way to expose services externally with HTTP/HTTPS. They provide DNS-based access with optional TLS termination.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPENSHIFT ROUTING                                │
│                                                                     │
│   External Traffic                                                  │
│         │                                                           │
│         ▼                                                           │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                    ROUTER (HAProxy)                          │  │
│   │              *.apps.cluster.example.com                      │  │
│   └─────────────────────────────────────────────────────────────┘  │
│         │                                                           │
│         │  Route Rules                                              │
│         ▼                                                           │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │  Route: myapp.apps.cluster.example.com                       │  │
│   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │  │
│   │  │ /api → api  │  │ /web → web  │  │ / → default │         │  │
│   │  │   service   │  │   service   │  │   service   │         │  │
│   │  └─────────────┘  └─────────────┘  └─────────────┘         │  │
│   └─────────────────────────────────────────────────────────────┘  │
│         │                                                           │
│         ▼                                                           │
│   ┌─────────────┐                                                  │
│   │   Service   │ ──────▶ Pods                                     │
│   └─────────────┘                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

## Creating Routes

### Basic Route

```bash
# Expose service as route
oc expose svc/web-service

# With specific hostname
oc expose svc/web-service --hostname=myapp.apps.cluster.example.com

# View routes
oc get routes
oc describe route web-service
```

### Route YAML

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: web-route
spec:
  host: myapp.apps.cluster.example.com
  port:
    targetPort: 8080
  to:
    kind: Service
    name: web-service
    weight: 100
  wildcardPolicy: None
```

## TLS Routes

### Edge Termination

TLS terminates at the router; traffic to pods is unencrypted.

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: secure-route
spec:
  host: secure.apps.cluster.example.com
  to:
    kind: Service
    name: web-service
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
```

```bash
# Create edge route
oc create route edge secure-route --service=web-service

# With custom certificate
oc create route edge secure-route \
  --service=web-service \
  --cert=tls.crt \
  --key=tls.key \
  --ca-cert=ca.crt
```

### Passthrough Termination

TLS passes through to the pod; application handles TLS.

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: passthrough-route
spec:
  host: secure.apps.cluster.example.com
  to:
    kind: Service
    name: web-service
  port:
    targetPort: 8443
  tls:
    termination: passthrough
```

```bash
oc create route passthrough secure-route --service=web-service --port=8443
```

### Re-encrypt Termination

TLS terminates at router, then re-encrypts to pod.

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: reencrypt-route
spec:
  host: secure.apps.cluster.example.com
  to:
    kind: Service
    name: web-service
  tls:
    termination: reencrypt
    destinationCACertificate: |
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
```

### TLS Termination Comparison

| Type | Router TLS | Backend TLS | Use Case |
|------|------------|-------------|----------|
| **Edge** | Yes | No | Most common, easy setup |
| **Passthrough** | Pass-through | Yes | End-to-end encryption |
| **Re-encrypt** | Yes | Yes | Compliance requirements |

## Path-Based Routing

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: api-route
spec:
  host: myapp.apps.cluster.example.com
  path: /api
  to:
    kind: Service
    name: api-service
---
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: web-route
spec:
  host: myapp.apps.cluster.example.com
  path: /
  to:
    kind: Service
    name: web-service
```

## Route Annotations

```yaml
metadata:
  annotations:
    # Load balancing
    haproxy.router.openshift.io/balance: roundrobin
    
    # Timeouts
    haproxy.router.openshift.io/timeout: 60s
    
    # Rate limiting
    haproxy.router.openshift.io/rate-limit-connections: "true"
    haproxy.router.openshift.io/rate-limit-connections.rate-http: "100"
    
    # IP whitelist
    haproxy.router.openshift.io/ip_whitelist: "192.168.1.0/24 10.0.0.0/8"
    
    # Sticky sessions
    haproxy.router.openshift.io/disable_cookies: "false"
```

## Weighted Routes (A/B Testing)

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: ab-route
spec:
  host: myapp.apps.cluster.example.com
  to:
    kind: Service
    name: web-v1
    weight: 80
  alternateBackends:
  - kind: Service
    name: web-v2
    weight: 20
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Service** | Internal load balancer for pods |
| **ClusterIP** | Internal-only access |
| **Route** | External HTTP/HTTPS access |
| **Edge TLS** | TLS terminates at router |
| **Passthrough** | TLS to application |
| **Re-encrypt** | Double TLS encryption |

---

**Next: [Storage](./07-Storage.md)** →

# Part 7: Storage

## OpenShift Storage Model

OpenShift provides persistent storage through the Kubernetes Container Storage Interface (CSI). Storage is abstracted into StorageClasses, PersistentVolumes (PV), and PersistentVolumeClaims (PVC).

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STORAGE ARCHITECTURE                             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    APPLICATION                               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │   │
│  │  │    Pod      │  │    Pod      │  │    Pod      │         │   │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────┐ │         │   │
│  │  │ │Container│ │  │ │Container│ │  │ │Container│ │         │   │
│  │  │ │  /data  │ │  │ │  /data  │ │  │ │  /data  │ │         │   │
│  │  │ └────┬────┘ │  │ └────┬────┘ │  │ └────┬────┘ │         │   │
│  │  └──────┼──────┘  └──────┼──────┘  └──────┼──────┘         │   │
│  └─────────┼────────────────┼────────────────┼─────────────────┘   │
│            │                │                │                      │
│            └────────────────┼────────────────┘                      │
│                             │                                       │
│  ┌──────────────────────────▼──────────────────────────────────┐   │
│  │               PersistentVolumeClaim (PVC)                    │   │
│  │            "I need 10Gi of fast storage"                     │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │ binds to                              │
│  ┌──────────────────────────▼──────────────────────────────────┐   │
│  │                PersistentVolume (PV)                         │   │
│  │              "Here is 10Gi of SSD storage"                   │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │ provisioned by                        │
│  ┌──────────────────────────▼──────────────────────────────────┐   │
│  │                   StorageClass                               │   │
│  │         provisioner: kubernetes.io/aws-ebs                   │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │                                       │
│  ┌──────────────────────────▼──────────────────────────────────┐   │
│  │                   Storage Backend                            │   │
│  │        AWS EBS │ GCE PD │ NFS │ Ceph │ vSphere              │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Storage Classes

StorageClasses define different "classes" of storage with specific characteristics like performance, backup policies, or provisioner type.

```bash
# List storage classes
oc get storageclass
oc get sc

# View default storage class
oc get sc -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")].metadata.name}'

# Describe storage class
oc describe sc gp2
```

### StorageClass Example

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iopsPerGB: "10"
  encrypted: "true"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

### Common Storage Provisioners

| Provider | Provisioner |
|----------|-------------|
| AWS EBS | kubernetes.io/aws-ebs |
| GCE PD | kubernetes.io/gce-pd |
| Azure Disk | kubernetes.io/azure-disk |
| vSphere | kubernetes.io/vsphere-volume |
| NFS | kubernetes.io/nfs |
| OpenShift Data Foundation | openshift-storage.rbd.csi.ceph.com |

## PersistentVolumes (PV)

PersistentVolumes represent actual storage resources in the cluster.

### Static PV Provisioning

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: nfs-storage
  nfs:
    server: nfs.example.com
    path: /exports/data
```

```bash
# List PVs
oc get pv

# Describe PV
oc describe pv nfs-pv
```

### Access Modes

| Mode | Abbreviation | Description |
|------|--------------|-------------|
| ReadWriteOnce | RWO | Single node read/write |
| ReadOnlyMany | ROX | Multiple nodes read-only |
| ReadWriteMany | RWX | Multiple nodes read/write |
| ReadWriteOncePod | RWOP | Single pod read/write |

## PersistentVolumeClaims (PVC)

PVCs are requests for storage by users/applications.

### Creating PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-storage
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: gp2
```

```bash
# Create PVC
oc apply -f pvc.yaml

# Create PVC imperatively
oc create pvc app-storage --access-mode=ReadWriteOnce --size=5Gi

# List PVCs
oc get pvc

# Describe PVC
oc describe pvc app-storage

# Delete PVC
oc delete pvc app-storage
```

## Using Storage in Pods

### Mount PVC in Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-storage
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /usr/share/nginx/html
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: app-storage
```

### Mount PVC in Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: database
spec:
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: postgres
        image: postgres:14
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        env:
        - name: POSTGRES_PASSWORD
          value: secret
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: postgres-data
```

## EmptyDir Volumes

EmptyDir volumes provide temporary storage that exists for the lifetime of a pod.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shared-storage
spec:
  containers:
  - name: writer
    image: busybox
    command: ['sh', '-c', 'echo "Hello" > /data/message; sleep 3600']
    volumeMounts:
    - name: shared
      mountPath: /data
  - name: reader
    image: busybox
    command: ['sh', '-c', 'cat /data/message; sleep 3600']
    volumeMounts:
    - name: shared
      mountPath: /data
  volumes:
  - name: shared
    emptyDir: {}
```

### Memory-backed EmptyDir

```yaml
volumes:
- name: cache
  emptyDir:
    medium: Memory
    sizeLimit: 500Mi
```

## ConfigMap and Secret Volumes

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-config
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config
      mountPath: /etc/nginx/conf.d
    - name: secrets
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: config
    configMap:
      name: nginx-config
  - name: secrets
    secret:
      secretName: app-secrets
```

## Volume Expansion

Expand PVCs if the StorageClass supports it.

```bash
# Check if expansion is supported
oc get sc gp2 -o jsonpath='{.allowVolumeExpansion}'

# Expand PVC
oc patch pvc app-storage -p '{"spec":{"resources":{"requests":{"storage":"10Gi"}}}}'
```

## Reclaim Policies

| Policy | Description |
|--------|-------------|
| **Retain** | Keep PV after PVC deletion |
| **Delete** | Delete PV and underlying storage |
| **Recycle** | (Deprecated) Basic scrub and reuse |

```bash
# Change reclaim policy
oc patch pv my-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

## OpenShift Data Foundation

OpenShift Data Foundation (ODF) provides software-defined storage using Ceph.

```bash
# Check ODF status
oc get storagecluster -n openshift-storage

# ODF storage classes
oc get sc | grep openshift-storage
# - ocs-storagecluster-ceph-rbd (block)
# - ocs-storagecluster-cephfs (file)
# - openshift-storage.noobaa.io (object)
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **StorageClass** | Defines storage types and provisioner |
| **PersistentVolume** | Actual storage resource |
| **PersistentVolumeClaim** | Request for storage |
| **AccessModes** | RWO, ROX, RWX, RWOP |
| **EmptyDir** | Temporary pod-lifetime storage |
| **ODF** | OpenShift's software-defined storage |

---

**Next: [ConfigMaps and Secrets](./08-ConfigMaps-and-Secrets.md)** →

# Part 8: ConfigMaps and Secrets

## Understanding ConfigMaps

ConfigMaps store non-sensitive configuration data as key-value pairs. They decouple configuration from container images, making applications more portable.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONFIGMAP USAGE                                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     CONFIGMAP                                │   │
│  │  ┌─────────────────┐  ┌─────────────────────────────────┐   │   │
│  │  │ Key-Value Pairs │  │        Configuration Files       │   │   │
│  │  │ DB_HOST=db      │  │  app.conf:                       │   │   │
│  │  │ DB_PORT=5432    │  │    server.port=8080              │   │   │
│  │  │ LOG_LEVEL=info  │  │    log.level=INFO                │   │   │
│  │  └─────────────────┘  └─────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                    │                          │                     │
│                    ▼                          ▼                     │
│  ┌────────────────────────────┐  ┌────────────────────────────┐   │
│  │   Environment Variables    │  │      Volume Mount          │   │
│  │   env:                     │  │   volumeMounts:            │   │
│  │   - name: DB_HOST          │  │   - name: config           │   │
│  │     valueFrom:             │  │     mountPath: /etc/config │   │
│  │       configMapKeyRef:     │  │                            │   │
│  └────────────────────────────┘  └────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Creating ConfigMaps

### From Literal Values

```bash
# Create from literals
oc create configmap app-config \
  --from-literal=DB_HOST=postgres \
  --from-literal=DB_PORT=5432 \
  --from-literal=LOG_LEVEL=info

# View ConfigMap
oc get configmap app-config -o yaml
```

### From Files

```bash
# Create from file
oc create configmap nginx-config --from-file=nginx.conf

# Create from directory
oc create configmap app-config --from-file=config/

# Create from env file
oc create configmap app-config --from-env-file=app.env
```

### From YAML

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Simple key-value
  DB_HOST: postgres
  DB_PORT: "5432"
  LOG_LEVEL: info
  
  # Multi-line configuration file
  app.properties: |
    server.port=8080
    server.host=0.0.0.0
    logging.level=INFO
    
  nginx.conf: |
    server {
      listen 80;
      location / {
        root /usr/share/nginx/html;
      }
    }
```

## Using ConfigMaps

### As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: myapp
    # Single key
    env:
    - name: DATABASE_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DB_HOST
    # All keys
    envFrom:
    - configMapRef:
        name: app-config
```

### As Volume Mount

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config-volume
      mountPath: /etc/nginx/conf.d
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
```

### Mount Specific Keys

```yaml
volumes:
- name: config
  configMap:
    name: app-config
    items:
    - key: app.properties
      path: application.properties
    - key: nginx.conf
      path: server.conf
```

## Managing ConfigMaps

```bash
# List ConfigMaps
oc get configmap
oc get cm

# Describe ConfigMap
oc describe cm app-config

# Edit ConfigMap
oc edit cm app-config

# Delete ConfigMap
oc delete cm app-config

# Update ConfigMap from file
oc create configmap app-config --from-file=app.conf --dry-run=client -o yaml | oc apply -f -
```

## Understanding Secrets

Secrets store sensitive data like passwords, tokens, and keys. They're base64-encoded (not encrypted) by default but can be encrypted at rest in etcd.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SECRET TYPES                                   │
│                                                                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐  │
│  │     Opaque       │  │ kubernetes.io/   │  │ kubernetes.io/  │  │
│  │   (Generic)      │  │ basic-auth       │  │ ssh-auth        │  │
│  │                  │  │                  │  │                 │  │
│  │  DB_PASSWORD     │  │  username        │  │  ssh-privatekey │  │
│  │  API_KEY         │  │  password        │  │                 │  │
│  └──────────────────┘  └──────────────────┘  └─────────────────┘  │
│                                                                     │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐  │
│  │ kubernetes.io/   │  │ kubernetes.io/   │  │ kubernetes.io/  │  │
│  │ tls              │  │ dockerconfigjson │  │ service-account │  │
│  │                  │  │                  │  │ -token          │  │
│  │  tls.crt         │  │  .dockerconfig   │  │                 │  │
│  │  tls.key         │  │  json            │  │  (auto-created) │  │
│  └──────────────────┘  └──────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## Creating Secrets

### Generic (Opaque) Secrets

```bash
# From literals
oc create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=secretpassword

# From files
oc create secret generic ssl-certs \
  --from-file=ca.crt \
  --from-file=server.crt \
  --from-file=server.key
```

### From YAML

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  # Base64 encoded values
  username: YWRtaW4=
  password: c2VjcmV0cGFzc3dvcmQ=
---
# Using stringData (plain text, auto-encoded)
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  username: admin
  password: secretpassword
```

### TLS Secrets

```bash
# Create TLS secret
oc create secret tls my-tls-secret \
  --cert=tls.crt \
  --key=tls.key
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-tls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-cert>
  tls.key: <base64-encoded-key>
```

### Docker Registry Secrets

```bash
# Create registry secret
oc create secret docker-registry registry-secret \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=password \
  --docker-email=user@example.com

# Link to service account
oc secrets link default registry-secret --for=pull
```

## Using Secrets

### As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: myapp
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
    # All keys
    envFrom:
    - secretRef:
        name: db-secret
```

### As Volume Mount

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
    - name: secrets
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secrets
    secret:
      secretName: db-secret
      defaultMode: 0400
```

### For Image Pull

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: registry.example.com/myapp:latest
  imagePullSecrets:
  - name: registry-secret
```

## Managing Secrets

```bash
# List secrets
oc get secrets

# Describe secret (shows metadata, not data)
oc describe secret db-secret

# View secret data (base64)
oc get secret db-secret -o yaml

# Decode secret value
oc get secret db-secret -o jsonpath='{.data.password}' | base64 -d

# Edit secret
oc edit secret db-secret

# Delete secret
oc delete secret db-secret
```

## Encryption at Rest

OpenShift can encrypt secrets in etcd using the encryption configuration.

```yaml
# Check encryption status
oc get apiserver cluster -o jsonpath='{.spec.encryption}'

# Enable encryption (cluster admin)
oc patch apiserver cluster --type=merge -p '{"spec":{"encryption":{"type":"aescbc"}}}'
```

## Best Practices

| Practice | Description |
|----------|-------------|
| **Don't commit secrets** | Never store secrets in Git |
| **Use external secrets** | Consider Vault, AWS Secrets Manager |
| **Limit access** | Use RBAC to restrict secret access |
| **Rotate regularly** | Update secrets periodically |
| **Use immutable** | Mark as immutable when possible |
| **Mount read-only** | Always mount secrets as read-only |

### Immutable ConfigMaps/Secrets

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
immutable: true  # Cannot be modified after creation
data:
  key: value
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **ConfigMap** | Non-sensitive configuration data |
| **Secret** | Sensitive data (base64 encoded) |
| **Environment** | Inject as env variables |
| **Volume** | Mount as files |
| **Opaque** | Generic secret type |
| **TLS** | Certificate secrets |

---

**Next: [Builds and ImageStreams](./09-Builds-and-ImageStreams.md)** →

# Part 9: Builds and ImageStreams

## OpenShift Build System

OpenShift provides built-in CI/CD capabilities through BuildConfigs. Unlike Kubernetes, you can build container images directly in the cluster from source code.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPENSHIFT BUILD FLOW                             │
│                                                                     │
│  ┌──────────────────┐                                              │
│  │   Source Code    │                                              │
│  │  (Git/Local)     │                                              │
│  └────────┬─────────┘                                              │
│           │                                                         │
│           ▼                                                         │
│  ┌──────────────────┐     ┌──────────────────┐                     │
│  │   BuildConfig    │────▶│     Build        │                     │
│  │  (Definition)    │     │   (Execution)    │                     │
│  └──────────────────┘     └────────┬─────────┘                     │
│                                    │                                │
│           ┌────────────────────────┼────────────────────────┐      │
│           │                        │                        │      │
│           ▼                        ▼                        ▼      │
│  ┌──────────────┐       ┌──────────────┐       ┌──────────────┐   │
│  │    S2I       │       │   Docker     │       │   Pipeline   │   │
│  │   Build      │       │   Build      │       │   Build      │   │
│  └──────┬───────┘       └──────┬───────┘       └──────┬───────┘   │
│         │                      │                      │            │
│         └──────────────────────┼──────────────────────┘            │
│                                │                                    │
│                                ▼                                    │
│                    ┌──────────────────┐                            │
│                    │   ImageStream    │                            │
│                    │   (Registry)     │                            │
│                    └──────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘
```

## Build Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Source-to-Image (S2I)** | Build from source without Dockerfile | Most common, language-specific |
| **Docker** | Build using Dockerfile | Custom build requirements |
| **Pipeline** | Tekton-based CI/CD | Complex pipelines |
| **Custom** | Custom builder image | Specialized builds |

## Source-to-Image (S2I)

S2I builds container images directly from source code without requiring a Dockerfile. It uses builder images that know how to build specific languages.

### Creating S2I Build

```bash
# Create from Git repository
oc new-app nodejs~https://github.com/sclorg/nodejs-ex.git

# Specify builder image
oc new-app python:3.9~https://github.com/user/python-app.git

# With specific branch
oc new-app nodejs~https://github.com/user/app.git#develop

# With context directory
oc new-app nodejs~https://github.com/user/repo.git --context-dir=app
```

### S2I BuildConfig YAML

```yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: myapp
spec:
  source:
    type: Git
    git:
      uri: https://github.com/user/nodejs-app.git
      ref: main
    contextDir: /
  strategy:
    type: Source
    sourceStrategy:
      from:
        kind: ImageStreamTag
        namespace: openshift
        name: nodejs:18-ubi8
      env:
      - name: NPM_RUN
        value: "start"
  output:
    to:
      kind: ImageStreamTag
      name: myapp:latest
  triggers:
  - type: ConfigChange
  - type: ImageChange
  - type: GitHub
    github:
      secret: webhook-secret
```

## Docker Build Strategy

Use Docker builds when you have a Dockerfile and need custom build steps.

```yaml
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  name: myapp-docker
spec:
  source:
    type: Git
    git:
      uri: https://github.com/user/app.git
      ref: main
    dockerfile: |
      FROM node:18-alpine
      WORKDIR /app
      COPY package*.json ./
      RUN npm install
      COPY . .
      EXPOSE 3000
      CMD ["npm", "start"]
  strategy:
    type: Docker
    dockerStrategy:
      dockerfilePath: Dockerfile
      buildArgs:
      - name: NODE_ENV
        value: production
  output:
    to:
      kind: ImageStreamTag
      name: myapp:latest
```

## Build from Local Directory

```bash
# Start build from local source
oc start-build myapp --from-dir=.

# Start build from local archive
oc start-build myapp --from-archive=app.tar.gz

# Start build from local file
oc start-build myapp --from-file=app.jar
```

## Managing Builds

```bash
# List BuildConfigs
oc get buildconfig
oc get bc

# List builds
oc get builds

# Start a build
oc start-build myapp

# Start build and follow logs
oc start-build myapp --follow

# View build logs
oc logs -f build/myapp-1

# Cancel build
oc cancel-build myapp-1

# Delete BuildConfig
oc delete bc myapp
```

## Build Triggers

### Webhook Triggers

```bash
# Get webhook URL
oc describe bc myapp | grep -A 5 Webhook

# Generic webhook
curl -X POST -k https://api.cluster.example.com/apis/build.openshift.io/v1/namespaces/myproject/buildconfigs/myapp/webhooks/<secret>/generic
```

### Image Change Trigger

Automatically rebuild when base image updates.

```yaml
triggers:
- type: ImageChange
  imageChange:
    from:
      kind: ImageStreamTag
      name: nodejs:18-ubi8
      namespace: openshift
```

### Config Change Trigger

Rebuild when BuildConfig changes.

```yaml
triggers:
- type: ConfigChange
```

## ImageStreams

ImageStreams provide an abstraction layer for container images, enabling automatic deployments when images change and tracking image history.

```
┌─────────────────────────────────────────────────────────────────────┐
│                       IMAGESTREAM                                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    ImageStream: myapp                        │   │
│  │                                                              │   │
│  │  ┌────────────────────────────────────────────────────────┐ │   │
│  │  │  ImageStreamTag: latest                                │ │   │
│  │  │  → image-registry.openshift.io/proj/myapp@sha256:abc   │ │   │
│  │  └────────────────────────────────────────────────────────┘ │   │
│  │                                                              │   │
│  │  ┌────────────────────────────────────────────────────────┐ │   │
│  │  │  ImageStreamTag: v1.0                                  │ │   │
│  │  │  → image-registry.openshift.io/proj/myapp@sha256:def   │ │   │
│  │  └────────────────────────────────────────────────────────┘ │   │
│  │                                                              │   │
│  │  ┌────────────────────────────────────────────────────────┐ │   │
│  │  │  ImageStreamTag: v0.9                                  │ │   │
│  │  │  → image-registry.openshift.io/proj/myapp@sha256:ghi   │ │   │
│  │  └────────────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Creating ImageStreams

```yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  name: myapp
spec:
  lookupPolicy:
    local: true
  tags:
  - name: latest
    from:
      kind: DockerImage
      name: docker.io/library/nginx:latest
    importPolicy:
      scheduled: true
    referencePolicy:
      type: Local
```

```bash
# Create ImageStream
oc create imagestream myapp

# Import external image
oc import-image myapp:latest --from=docker.io/library/nginx:latest --confirm

# Import with scheduled updates
oc import-image myapp:latest --from=docker.io/library/nginx:latest --scheduled --confirm

# Tag image
oc tag myapp:latest myapp:v1.0
```

### Managing ImageStreams

```bash
# List ImageStreams
oc get imagestream
oc get is

# Describe ImageStream
oc describe is myapp

# List tags
oc get istag

# Delete tag
oc delete istag myapp:v1.0

# View image history
oc describe is myapp
```

### Using ImageStreams in Deployments

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
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
        # Reference ImageStream
        image: image-registry.openshift-image-registry.svc:5000/myproject/myapp:latest
        # Or with lookupPolicy.local=true
        image: myapp:latest
```

## Internal Registry

OpenShift includes an integrated container registry.

```bash
# Get registry route
oc get route -n openshift-image-registry

# Login to registry
podman login -u $(oc whoami) -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000

# Push image to registry
podman tag myapp:latest image-registry.openshift-image-registry.svc:5000/myproject/myapp:latest
podman push image-registry.openshift-image-registry.svc:5000/myproject/myapp:latest
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **BuildConfig** | Defines how to build images |
| **S2I** | Source-to-Image builds |
| **Docker Build** | Dockerfile-based builds |
| **ImageStream** | Image abstraction and tracking |
| **Triggers** | Automatic build/deploy on changes |
| **Internal Registry** | Built-in image storage |

---

**Next: [Templates and Helm](./10-Templates-and-Helm.md)** →

# Part 10: Templates and Helm

## OpenShift Templates

Templates are OpenShift resources that define a set of objects to be created together with parameterization. They're useful for creating reusable application deployments.

```
┌─────────────────────────────────────────────────────────────────────┐
│                       TEMPLATE FLOW                                 │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                      TEMPLATE                                 │  │
│  │                                                               │  │
│  │  Parameters:                                                  │  │
│  │    APP_NAME=myapp                                            │  │
│  │    IMAGE_TAG=latest                                          │  │
│  │    REPLICAS=3                                                │  │
│  │                                                               │  │
│  │  Objects:                                                     │  │
│  │    - Deployment                                               │  │
│  │    - Service                                                  │  │
│  │    - Route                                                    │  │
│  │    - ConfigMap                                                │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              │ oc process                           │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                   PROCESSED YAML                              │  │
│  │  Parameters replaced with actual values                       │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              │ oc apply                             │
│                              ▼                                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐   │
│  │ Deployment │  │  Service   │  │   Route    │  │ ConfigMap  │   │
│  └────────────┘  └────────────┘  └────────────┘  └────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Creating Templates

### Basic Template

```yaml
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: webapp-template
  annotations:
    description: "A simple web application template"
    tags: "web,nginx"
    iconClass: "icon-nginx"
parameters:
- name: APP_NAME
  description: Application name
  required: true
  value: myapp
- name: IMAGE_TAG
  description: Image tag to deploy
  value: latest
- name: REPLICAS
  description: Number of replicas
  value: "1"
- name: MEMORY_LIMIT
  description: Memory limit
  value: "256Mi"
objects:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: ${APP_NAME}
  spec:
    replicas: ${{REPLICAS}}
    selector:
      matchLabels:
        app: ${APP_NAME}
    template:
      metadata:
        labels:
          app: ${APP_NAME}
      spec:
        containers:
        - name: ${APP_NAME}
          image: nginx:${IMAGE_TAG}
          ports:
          - containerPort: 80
          resources:
            limits:
              memory: ${MEMORY_LIMIT}
- apiVersion: v1
  kind: Service
  metadata:
    name: ${APP_NAME}
  spec:
    selector:
      app: ${APP_NAME}
    ports:
    - port: 80
      targetPort: 80
- apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: ${APP_NAME}
  spec:
    to:
      kind: Service
      name: ${APP_NAME}
```

## Using Templates

### Process and Apply

```bash
# Process template with default values
oc process -f template.yaml | oc apply -f -

# Process with custom parameters
oc process -f template.yaml \
  -p APP_NAME=production-app \
  -p REPLICAS=3 \
  -p IMAGE_TAG=v1.0 | oc apply -f -

# Process from cluster template
oc process webapp-template -p APP_NAME=myapp | oc apply -f -

# View processed output
oc process -f template.yaml -p APP_NAME=test -o yaml
```

### Managing Templates

```bash
# Create template in cluster
oc create -f template.yaml

# List templates
oc get templates

# List templates in openshift namespace (catalog)
oc get templates -n openshift

# Describe template
oc describe template webapp-template

# Delete template
oc delete template webapp-template
```

### new-app with Templates

```bash
# Create from template
oc new-app --template=webapp-template -p APP_NAME=myapp

# From file
oc new-app -f template.yaml -p APP_NAME=myapp

# List available templates
oc new-app --list
```

## Helm on OpenShift

Helm is the Kubernetes package manager and works seamlessly with OpenShift. It provides more advanced templating and package management capabilities.

```
┌─────────────────────────────────────────────────────────────────────┐
│                       HELM ARCHITECTURE                             │
│                                                                     │
│  ┌──────────────────┐                                              │
│  │   Helm Chart     │                                              │
│  │  ┌────────────┐  │                                              │
│  │  │ Chart.yaml │  │    Chart metadata                            │
│  │  ├────────────┤  │                                              │
│  │  │values.yaml │  │    Default configuration                     │
│  │  ├────────────┤  │                                              │
│  │  │ templates/ │  │    Kubernetes manifests                      │
│  │  ├────────────┤  │                                              │
│  │  │  charts/   │  │    Dependencies                              │
│  │  └────────────┘  │                                              │
│  └──────────────────┘                                              │
│           │                                                         │
│           │ helm install/upgrade                                    │
│           ▼                                                         │
│  ┌──────────────────┐                                              │
│  │    Release       │                                              │
│  │  (Instance of    │                                              │
│  │   chart)         │                                              │
│  └──────────────────┘                                              │
│           │                                                         │
│           ▼                                                         │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │              OpenShift Cluster                              │    │
│  │  Deployments │ Services │ Routes │ ConfigMaps │ Secrets    │    │
│  └────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

## Installing Helm

```bash
# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# macOS
brew install helm

# Verify
helm version
```

## Helm Repositories

```bash
# Add repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable

# Update repositories
helm repo update

# List repositories
helm repo list

# Search charts
helm search repo nginx
helm search hub wordpress  # Search Artifact Hub
```

## Installing Charts

```bash
# Install chart
helm install myrelease bitnami/nginx

# Install in specific namespace
helm install myrelease bitnami/nginx -n myproject

# Install with custom values
helm install myrelease bitnami/nginx --set replicaCount=3

# Install with values file
helm install myrelease bitnami/nginx -f values.yaml

# Dry run
helm install myrelease bitnami/nginx --dry-run

# Generate manifests only
helm template myrelease bitnami/nginx
```

## Managing Releases

```bash
# List releases
helm list
helm list -A  # All namespaces

# Get release info
helm status myrelease
helm get values myrelease
helm get manifest myrelease

# Upgrade release
helm upgrade myrelease bitnami/nginx --set replicaCount=5

# Rollback
helm rollback myrelease 1

# Uninstall
helm uninstall myrelease

# History
helm history myrelease
```

## Creating Helm Charts

```bash
# Create chart skeleton
helm create mychart

# Chart structure
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default values
├── charts/             # Dependencies
├── templates/          # Kubernetes templates
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl    # Template helpers
│   └── NOTES.txt       # Post-install notes
└── .helmignore
```

### Chart.yaml

```yaml
apiVersion: v2
name: mychart
description: A Helm chart for my application
type: application
version: 0.1.0
appVersion: "1.0.0"
dependencies:
- name: postgresql
  version: "12.x.x"
  repository: "https://charts.bitnami.com/bitnami"
  condition: postgresql.enabled
```

### values.yaml

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

route:
  enabled: true
  host: ""

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

postgresql:
  enabled: false
```

### Template Example

```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mychart.fullname" . }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "mychart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "mychart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 80
        resources:
          {{- toYaml .Values.resources | nindent 10 }}
```

### OpenShift Route in Helm

```yaml
# templates/route.yaml
{{- if .Values.route.enabled }}
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: {{ include "mychart.fullname" . }}
spec:
  {{- if .Values.route.host }}
  host: {{ .Values.route.host }}
  {{- end }}
  to:
    kind: Service
    name: {{ include "mychart.fullname" . }}
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
{{- end }}
```

## Packaging and Sharing

```bash
# Lint chart
helm lint mychart

# Package chart
helm package mychart

# Create repository index
helm repo index .

# Install from local chart
helm install myrelease ./mychart
```

## Templates vs Helm Comparison

| Feature | OpenShift Templates | Helm |
|---------|---------------------|------|
| **Complexity** | Simple | More powerful |
| **Parameterization** | Basic | Advanced (functions, conditionals) |
| **Dependencies** | None | Built-in |
| **Versioning** | Manual | Automatic |
| **Rollback** | Manual | Built-in |
| **Repository** | None | Helm repos |
| **OpenShift native** | Yes | No (but supported) |

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Templates** | OpenShift-native parameterized objects |
| **Helm** | Kubernetes package manager |
| **Chart** | Helm package with templates |
| **Release** | Instance of deployed chart |
| **Values** | Configuration for charts |
| **Repository** | Chart storage location |

---

**Next: [Operators](./11-Operators.md)** →

# Part 11: Operators

## What are Operators?

Operators extend Kubernetes/OpenShift to automate the management of complex applications. They encode human operational knowledge into software, handling installation, upgrades, and day-2 operations.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    OPERATOR PATTERN                                 │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                 OPERATOR CONTROLLER                           │  │
│  │                                                               │  │
│  │  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐    │  │
│  │  │   Observe   │────▶│   Analyze   │────▶│    Act      │    │  │
│  │  │  (Watch CRs)│     │  (Compare)  │     │  (Reconcile)│    │  │
│  │  └─────────────┘     └─────────────┘     └─────────────┘    │  │
│  │         │                                       │            │  │
│  │         │            Control Loop               │            │  │
│  │         └───────────────────────────────────────┘            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              │ manages                              │
│                              ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                 CUSTOM RESOURCES                              │  │
│  │                                                               │  │
│  │  apiVersion: example.com/v1                                   │  │
│  │  kind: Database                                               │  │
│  │  metadata:                                                    │  │
│  │    name: my-database                                          │  │
│  │  spec:                                                        │  │
│  │    replicas: 3                                                │  │
│  │    storage: 100Gi                                             │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│                              │ creates/manages                      │
│                              ▼                                      │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │  Pods │ Services │ ConfigMaps │ Secrets │ PVCs │ StatefulSets ││
│  └────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

## Operator Lifecycle Manager (OLM)

OLM manages the installation, upgrade, and lifecycle of operators in OpenShift. It's installed by default on OpenShift clusters.

```bash
# Check OLM components
oc get pods -n openshift-operator-lifecycle-manager

# View OLM resources
oc get catalogsources -n openshift-marketplace
oc get subscriptions -A
oc get clusterserviceversions -A
```

### OLM Components

| Component | Description |
|-----------|-------------|
| **CatalogSource** | Repository of available operators |
| **Subscription** | Tracks operator installation/updates |
| **ClusterServiceVersion (CSV)** | Operator version and metadata |
| **InstallPlan** | Resources to install for operator |
| **OperatorGroup** | Defines operator scope |

## OperatorHub

OperatorHub is the marketplace for discovering and installing operators in OpenShift.

```bash
# List available operators
oc get packagemanifests -n openshift-marketplace

# Search for specific operator
oc get packagemanifests -n openshift-marketplace | grep postgres

# Describe operator
oc describe packagemanifest postgresql -n openshift-marketplace
```

### Installing from OperatorHub (Web Console)

1. Navigate to **Operators → OperatorHub**
2. Search for desired operator
3. Click **Install**
4. Select installation options
5. Click **Install**

### Installing from CLI

```yaml
# Create OperatorGroup (if needed)
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: my-operatorgroup
  namespace: my-namespace
spec:
  targetNamespaces:
  - my-namespace
---
# Create Subscription
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: postgresql
  namespace: openshift-operators
spec:
  channel: v5
  name: postgresql
  source: certified-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Automatic
```

```bash
# Apply subscription
oc apply -f subscription.yaml

# Watch installation
oc get csv -w

# Verify operator
oc get pods -n openshift-operators
```

## Managing Operators

### View Installed Operators

```bash
# List subscriptions
oc get subscriptions -A

# List CSVs (installed versions)
oc get csv -A

# Get operator status
oc describe csv postgresql.v5.0.0 -n openshift-operators
```

### Update Operators

```bash
# Check for updates
oc get subscription postgresql -n openshift-operators -o yaml | grep currentCSV

# Approve InstallPlan (if manual approval)
oc get installplan -n openshift-operators
oc patch installplan install-xxxx -n openshift-operators --type merge -p '{"spec":{"approved":true}}'

# Change update channel
oc patch subscription postgresql -n openshift-operators --type merge -p '{"spec":{"channel":"v6"}}'
```

### Uninstall Operators

```bash
# Delete subscription
oc delete subscription postgresql -n openshift-operators

# Delete CSV
oc delete csv postgresql.v5.0.0 -n openshift-operators

# Delete OperatorGroup (if no other operators need it)
oc delete operatorgroup my-operatorgroup -n my-namespace
```

## Using Operators

Once installed, operators provide Custom Resource Definitions (CRDs) that you use to create managed resources.

### Example: PostgreSQL Operator

```yaml
apiVersion: postgres-operator.crunchydata.com/v1beta1
kind: PostgresCluster
metadata:
  name: my-postgres
spec:
  image: registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-14.5-1
  postgresVersion: 14
  instances:
  - name: instance1
    replicas: 3
    dataVolumeClaimSpec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
  backups:
    pgbackrest:
      repos:
      - name: repo1
        volume:
          volumeClaimSpec:
            accessModes:
            - ReadWriteOnce
            resources:
              requests:
                storage: 5Gi
```

```bash
# Create PostgreSQL cluster
oc apply -f postgres-cluster.yaml

# Watch cluster creation
oc get postgrescluster -w

# View created resources
oc get pods -l postgres-operator.crunchydata.com/cluster=my-postgres
oc get svc -l postgres-operator.crunchydata.com/cluster=my-postgres
```

### Example: AMQ Streams (Kafka) Operator

```yaml
apiVersion: kafka.strimzi.io/v1beta2
kind: Kafka
metadata:
  name: my-cluster
spec:
  kafka:
    version: 3.3.1
    replicas: 3
    listeners:
    - name: plain
      port: 9092
      type: internal
      tls: false
    - name: tls
      port: 9093
      type: internal
      tls: true
    storage:
      type: persistent-claim
      size: 10Gi
  zookeeper:
    replicas: 3
    storage:
      type: persistent-claim
      size: 5Gi
  entityOperator:
    topicOperator: {}
    userOperator: {}
```

## Cluster Operators

Cluster operators manage core OpenShift functionality and are installed by default.

```bash
# List cluster operators
oc get clusteroperators
oc get co

# Check operator status
oc describe co authentication

# View operator logs
oc logs -n openshift-authentication deployment/oauth-openshift
```

### Important Cluster Operators

| Operator | Purpose |
|----------|---------|
| authentication | OAuth server |
| console | Web console |
| dns | CoreDNS |
| etcd | etcd cluster |
| image-registry | Internal registry |
| ingress | Router/ingress |
| machine-api | Machine management |
| monitoring | Prometheus stack |
| network | SDN/OVN |
| storage | CSI drivers |

## Operator Capability Levels

| Level | Description |
|-------|-------------|
| **Level 1: Basic Install** | Automated installation |
| **Level 2: Seamless Upgrades** | Automated upgrades |
| **Level 3: Full Lifecycle** | Backup, restore, failover |
| **Level 4: Deep Insights** | Metrics, alerts, logs |
| **Level 5: Auto Pilot** | Auto-scaling, auto-tuning |

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Operator** | Automates application management |
| **OLM** | Manages operator lifecycle |
| **OperatorHub** | Marketplace for operators |
| **Subscription** | Tracks operator updates |
| **CSV** | Operator version metadata |
| **CRD** | Custom resource definitions |

---

**Next: [Security](./12-Security.md)** →

# Part 12: Security

## OpenShift Security Model

OpenShift implements defense-in-depth security with multiple layers including authentication, authorization (RBAC), network policies, and Security Context Constraints (SCCs).

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  1. AUTHENTICATION                                           │   │
│  │     OAuth │ LDAP │ OIDC │ HTPasswd │ Certificates           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  2. AUTHORIZATION (RBAC)                                     │   │
│  │     Roles │ ClusterRoles │ RoleBindings │ Service Accounts  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  3. ADMISSION CONTROL                                        │   │
│  │     SCCs │ Pod Security │ Quotas │ Network Policies         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  4. RUNTIME SECURITY                                         │   │
│  │     SELinux │ Seccomp │ Capabilities │ Read-only FS         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  5. NETWORK SECURITY                                         │   │
│  │     Network Policies │ TLS │ Service Mesh │ Egress          │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Security Context Constraints (SCCs)

SCCs are OpenShift's primary mechanism for controlling pod security. They define what security features pods can request.

### Built-in SCCs

| SCC | Description |
|-----|-------------|
| **restricted** | Default, most restrictive (no root, no privileged) |
| **restricted-v2** | Enhanced restricted with more security |
| **nonroot** | Must run as non-root user |
| **nonroot-v2** | Enhanced nonroot |
| **hostnetwork** | Access to host network |
| **hostaccess** | Access to host namespace |
| **anyuid** | Can run as any UID |
| **privileged** | Full privileges (dangerous) |

### Managing SCCs

```bash
# List SCCs
oc get scc

# Describe SCC
oc describe scc restricted

# View SCC priority
oc get scc -o custom-columns=NAME:.metadata.name,PRIORITY:.priority

# Check which SCC a pod uses
oc get pod mypod -o yaml | grep scc
```

### Assigning SCCs

```bash
# Add SCC to service account
oc adm policy add-scc-to-user anyuid -z myapp-sa -n myproject

# Add SCC to user
oc adm policy add-scc-to-user privileged user1

# Add SCC to group
oc adm policy add-scc-to-group nonroot developers

# Remove SCC
oc adm policy remove-scc-from-user anyuid -z myapp-sa -n myproject

# Check who can use an SCC
oc adm policy who-can use scc privileged
```

### Custom SCC

```yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: custom-scc
allowPrivilegedContainer: false
allowPrivilegeEscalation: false
requiredDropCapabilities:
- ALL
runAsUser:
  type: MustRunAsNonRoot
seLinuxContext:
  type: MustRunAs
fsGroup:
  type: MustRunAs
volumes:
- configMap
- downwardAPI
- emptyDir
- persistentVolumeClaim
- projected
- secret
```

## Pod Security

### Security Context in Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    volumeMounts:
    - name: tmp
      mountPath: /tmp
  volumes:
  - name: tmp
    emptyDir: {}
```

### Pod Security Standards (Kubernetes-native)

```yaml
# Namespace labels for Pod Security Standards
apiVersion: v1
kind: Namespace
metadata:
  name: secure-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

## Network Policies

Network policies control pod-to-pod and external traffic flow.

### Default Deny All

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: myproject
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### Allow Specific Traffic

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-egress-to-db
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector: {}
      podSelector:
        matchLabels:
          k8s-app: kube-dns
    ports:
    - protocol: UDP
      port: 53
```

```bash
# List network policies
oc get networkpolicy

# Describe policy
oc describe networkpolicy allow-frontend-to-backend
```

## OAuth and Authentication

### Configure HTPasswd Identity Provider

```bash
# Create htpasswd file
htpasswd -c -B -b users.htpasswd admin password123
htpasswd -B -b users.htpasswd developer devpass

# Create secret
oc create secret generic htpass-secret \
  --from-file=htpasswd=users.htpasswd \
  -n openshift-config
```

```yaml
# Update OAuth config
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: htpasswd_provider
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
```

### LDAP Integration

```yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: ldap
    type: LDAP
    ldap:
      url: "ldaps://ldap.example.com/ou=users,dc=example,dc=com?uid"
      bindDN: "cn=admin,dc=example,dc=com"
      bindPassword:
        name: ldap-secret
      insecure: false
      ca:
        name: ldap-ca-configmap
      attributes:
        id:
        - dn
        email:
        - mail
        name:
        - cn
        preferredUsername:
        - uid
```

## Image Security

### Allowed Registries

```yaml
# Restrict allowed registries
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  name: cluster
spec:
  registrySources:
    allowedRegistries:
    - quay.io
    - registry.redhat.io
    - image-registry.openshift-image-registry.svc:5000
    blockedRegistries:
    - docker.io/untrusted
```

### Image Signature Verification

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  name: cluster
spec:
  additionalTrustedCA:
    name: registry-cas
```

## Secrets Management

### Sealed Secrets

```bash
# Install Sealed Secrets operator
# Create sealed secret
kubeseal --format yaml < secret.yaml > sealed-secret.yaml
oc apply -f sealed-secret.yaml
```

### External Secrets

```yaml
# Using External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: db-secret
  data:
  - secretKey: password
    remoteRef:
      key: database/credentials
      property: password
```

## Security Best Practices

| Area | Best Practice |
|------|---------------|
| **Pods** | Run as non-root, drop capabilities |
| **Images** | Use trusted registries, scan for vulnerabilities |
| **Network** | Implement network policies |
| **Secrets** | Use external secret management |
| **RBAC** | Principle of least privilege |
| **SCCs** | Use most restrictive SCC possible |
| **TLS** | Encrypt all traffic |
| **Audit** | Enable audit logging |

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **SCC** | Security Context Constraints |
| **Network Policy** | Control traffic flow |
| **OAuth** | Authentication providers |
| **RBAC** | Role-based access control |
| **Secrets** | Sensitive data management |
| **Pod Security** | Container security settings |

---

**Next: [Monitoring and Logging](./13-Monitoring-and-Logging.md)** →

# Part 13: Monitoring and Logging

## OpenShift Monitoring Stack

OpenShift includes a comprehensive monitoring stack based on Prometheus, providing metrics collection, alerting, and visualization out of the box.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MONITORING ARCHITECTURE                          │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     GRAFANA                                  │   │
│  │              (Visualization & Dashboards)                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                  ALERTMANAGER                                │   │
│  │              (Alert Routing & Notification)                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   PROMETHEUS                                 │   │
│  │     (Metrics Collection, Storage & Alerting Rules)          │   │
│  │  ┌────────────────┐  ┌────────────────┐                     │   │
│  │  │ Cluster Prom   │  │  User Workload │                     │   │
│  │  │ (Platform)     │  │  Monitoring    │                     │   │
│  │  └────────────────┘  └────────────────┘                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ scrapes                              │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   METRICS SOURCES                            │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   │   │
│  │  │ Node     │ │ kubelet  │ │ Operators│ │ Applications │   │   │
│  │  │ Exporter │ │          │ │          │ │ (ServiceMon) │   │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────────┘   │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Accessing Monitoring

### Web Console

```bash
# Get Prometheus URL
oc get route prometheus-k8s -n openshift-monitoring

# Get Alertmanager URL
oc get route alertmanager-main -n openshift-monitoring

# Get Grafana URL (if enabled)
oc get route grafana -n openshift-monitoring

# Access via console
# Observe → Metrics (PromQL queries)
# Observe → Dashboards (Grafana)
# Observe → Alerting
```

### CLI Access

```bash
# Get Prometheus token
TOKEN=$(oc whoami -t)
PROM_URL=$(oc get route prometheus-k8s -n openshift-monitoring -o jsonpath='{.spec.host}')

# Query Prometheus API
curl -k -H "Authorization: Bearer $TOKEN" \
  "https://$PROM_URL/api/v1/query?query=up"
```

## User Workload Monitoring

Enable monitoring for user applications in addition to cluster components.

### Enable User Workload Monitoring

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |
    enableUserWorkload: true
```

```bash
# Apply configuration
oc apply -f cluster-monitoring-config.yaml

# Verify user workload pods
oc get pods -n openshift-user-workload-monitoring
```

### ServiceMonitor

Create ServiceMonitors to scrape metrics from your applications.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp-monitor
  namespace: myproject
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
  namespaceSelector:
    matchNames:
    - myproject
```

### PodMonitor

Monitor pods directly without service.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: myapp-pods
  namespace: myproject
spec:
  selector:
    matchLabels:
      app: myapp
  podMetricsEndpoints:
  - port: metrics
    interval: 15s
```

## Alerting

### Creating Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: myapp-alerts
  namespace: myproject
spec:
  groups:
  - name: myapp.rules
    rules:
    - alert: HighErrorRate
      expr: |
        sum(rate(http_requests_total{status=~"5.."}[5m])) /
        sum(rate(http_requests_total[5m])) > 0.1
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "High error rate detected"
        description: "Error rate is {{ $value | humanizePercentage }}"
    
    - alert: PodNotReady
      expr: |
        kube_pod_status_ready{condition="true",namespace="myproject"} == 0
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Pod not ready"
        description: "Pod {{ $labels.pod }} in {{ $labels.namespace }} is not ready"
```

```bash
# View alerts
oc get prometheusrules -A

# Check firing alerts
oc exec -n openshift-monitoring prometheus-k8s-0 -- \
  curl -s localhost:9090/api/v1/alerts | jq '.data.alerts'
```

### Alertmanager Configuration

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: alertmanager-main
  namespace: openshift-monitoring
type: Opaque
stringData:
  alertmanager.yaml: |
    global:
      resolve_timeout: 5m
    route:
      receiver: 'default'
      group_by: ['alertname', 'namespace']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 12h
      routes:
      - match:
          severity: critical
        receiver: 'pagerduty'
      - match:
          severity: warning
        receiver: 'slack'
    receivers:
    - name: 'default'
      email_configs:
      - to: 'team@example.com'
    - name: 'pagerduty'
      pagerduty_configs:
      - service_key: '<key>'
    - name: 'slack'
      slack_configs:
      - api_url: 'https://hooks.slack.com/services/xxx'
        channel: '#alerts'
```

## PromQL Queries

### Common Queries

```promql
# CPU usage by pod
sum(rate(container_cpu_usage_seconds_total{namespace="myproject"}[5m])) by (pod)

# Memory usage by pod
sum(container_memory_working_set_bytes{namespace="myproject"}) by (pod)

# Request rate
sum(rate(http_requests_total{namespace="myproject"}[5m])) by (service)

# Error rate percentage
sum(rate(http_requests_total{status=~"5.."}[5m])) / 
sum(rate(http_requests_total[5m])) * 100

# Pod restart count
sum(kube_pod_container_status_restarts_total{namespace="myproject"}) by (pod)

# Node CPU utilization
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Persistent volume usage
kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes * 100
```

## OpenShift Logging

OpenShift provides cluster logging through the EFK (Elasticsearch, Fluentd, Kibana) stack or the newer Loki-based solution.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LOGGING ARCHITECTURE                             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     KIBANA / LOG CONSOLE                     │   │
│  │                   (Log Visualization)                        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              ELASTICSEARCH / LOKI                            │   │
│  │                   (Log Storage)                              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              FLUENTD / VECTOR                                │   │
│  │              (Log Collection & Forwarding)                   │   │
│  │         Runs on every node as DaemonSet                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ collects from                        │
│                              ▼                                      │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │   Container Logs │ Journal Logs │ Audit Logs │ Infra Logs     ││
│  └────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

### Installing Cluster Logging

```bash
# Install OpenShift Logging Operator from OperatorHub

# Create ClusterLogging instance
oc apply -f - <<EOF
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance
  namespace: openshift-logging
spec:
  managementState: Managed
  logStore:
    type: lokistack
    lokistack:
      name: logging-loki
  collection:
    type: vector
  visualization:
    type: ocp-console
EOF
```

### Log Forwarding

```yaml
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  outputs:
  - name: external-elasticsearch
    type: elasticsearch
    url: https://elasticsearch.example.com:9200
    secret:
      name: es-secret
  - name: splunk
    type: splunk
    url: https://splunk.example.com:8088
    secret:
      name: splunk-secret
  pipelines:
  - name: app-logs
    inputRefs:
    - application
    outputRefs:
    - external-elasticsearch
    labels:
      source: openshift
  - name: infra-logs
    inputRefs:
    - infrastructure
    - audit
    outputRefs:
    - splunk
```

### Viewing Logs

```bash
# View logs in CLI
oc logs deployment/myapp
oc logs -f deployment/myapp
oc logs deployment/myapp --previous
oc logs deployment/myapp -c sidecar

# Aggregate logs from all pods
oc logs -l app=myapp --all-containers

# Access Kibana (if using EFK)
oc get route kibana -n openshift-logging
```

## Resource Metrics

```bash
# Pod resource usage
oc adm top pods -n myproject
oc adm top pods --containers -n myproject

# Node resource usage
oc adm top nodes

# Specific pod metrics
oc adm top pod myapp-xxxxx -n myproject
```

---

## 📝 Summary

| Concept | Description |
|---------|-------------|
| **Prometheus** | Metrics collection and storage |
| **Alertmanager** | Alert routing and notification |
| **Grafana** | Metrics visualization |
| **ServiceMonitor** | Define what to scrape |
| **PrometheusRule** | Define alerting rules |
| **Cluster Logging** | EFK/Loki log aggregation |

---

**Next: [Advanced Topics](./14-Advanced-Topics.md)** →

# Part 14: Advanced Topics

## CI/CD with OpenShift Pipelines

OpenShift Pipelines is based on Tekton, providing cloud-native CI/CD capabilities.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TEKTON PIPELINE FLOW                             │
│                                                                     │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐               │
│  │   Task 1   │───▶│   Task 2   │───▶│   Task 3   │               │
│  │ (Clone Git)│    │  (Build)   │    │  (Deploy)  │               │
│  └────────────┘    └────────────┘    └────────────┘               │
│       │                 │                 │                        │
│       ▼                 ▼                 ▼                        │
│  ┌─────────┐      ┌─────────┐      ┌─────────┐                    │
│  │  Step 1 │      │  Step 1 │      │  Step 1 │                    │
│  │  Step 2 │      │  Step 2 │      │  Step 2 │                    │
│  └─────────┘      └─────────┘      └─────────┘                    │
│                                                                     │
│  Pipeline → PipelineRun (execution instance)                       │
│  Task → TaskRun (execution instance)                               │
└─────────────────────────────────────────────────────────────────────┘
```

### Installing OpenShift Pipelines

```bash
# Install from OperatorHub (Red Hat OpenShift Pipelines)
# Or via CLI:
oc apply -f - <<EOF
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-pipelines-operator
  namespace: openshift-operators
spec:
  channel: latest
  name: openshift-pipelines-operator-rh
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
```

### Creating a Task

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: build-and-push
spec:
  params:
  - name: IMAGE
    type: string
  workspaces:
  - name: source
  steps:
  - name: build
    image: gcr.io/kaniko-project/executor:latest
    command:
    - /kaniko/executor
    args:
    - --dockerfile=Dockerfile
    - --context=$(workspaces.source.path)
    - --destination=$(params.IMAGE)
```

### Creating a Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: build-and-deploy
spec:
  params:
  - name: git-url
    type: string
  - name: image
    type: string
  workspaces:
  - name: shared-workspace
  tasks:
  - name: clone
    taskRef:
      name: git-clone
      kind: ClusterTask
    params:
    - name: url
      value: $(params.git-url)
    workspaces:
    - name: output
      workspace: shared-workspace
  - name: build
    taskRef:
      name: buildah
      kind: ClusterTask
    runAfter:
    - clone
    params:
    - name: IMAGE
      value: $(params.image)
    workspaces:
    - name: source
      workspace: shared-workspace
  - name: deploy
    taskRef:
      name: openshift-client
      kind: ClusterTask
    runAfter:
    - build
    params:
    - name: SCRIPT
      value: |
        oc set image deployment/myapp myapp=$(params.image)
```

### Running Pipelines

```bash
# Start pipeline
tkn pipeline start build-and-deploy \
  -p git-url=https://github.com/user/repo.git \
  -p image=image-registry.openshift-image-registry.svc:5000/myproject/myapp:latest \
  -w name=shared-workspace,claimName=pipeline-pvc

# List pipeline runs
tkn pipelinerun list

# View logs
tkn pipelinerun logs build-and-deploy-xxxxx -f

# Cancel run
tkn pipelinerun cancel build-and-deploy-xxxxx
```

## GitOps with OpenShift GitOps

OpenShift GitOps uses ArgoCD to implement GitOps workflows.

```
┌─────────────────────────────────────────────────────────────────────┐
│                      GITOPS FLOW                                    │
│                                                                     │
│  ┌────────────┐     ┌────────────┐     ┌────────────────────────┐ │
│  │    Git     │     │   ArgoCD   │     │    OpenShift Cluster   │ │
│  │ Repository │────▶│            │────▶│                        │ │
│  │            │     │  (Sync)    │     │   Deployments          │ │
│  │ manifests/ │     │            │     │   Services             │ │
│  │ kustomize/ │     │            │     │   ConfigMaps           │ │
│  │ helm/      │     │            │     │                        │ │
│  └────────────┘     └────────────┘     └────────────────────────┘ │
│                                                                     │
│       │                                          │                  │
│       │           Continuous Sync                │                  │
│       └──────────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
```

### Installing OpenShift GitOps

```bash
# Install operator
oc apply -f - <<EOF
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
  namespace: openshift-operators
spec:
  channel: latest
  name: openshift-gitops-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF

# Get ArgoCD URL
oc get route openshift-gitops-server -n openshift-gitops

# Get admin password
oc extract secret/openshift-gitops-cluster -n openshift-gitops --to=-
```

### Creating ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: openshift-gitops
spec:
  project: default
  source:
    repoURL: https://github.com/user/gitops-repo.git
    targetRevision: main
    path: environments/production
  destination:
    server: https://kubernetes.default.svc
    namespace: myproject
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

```bash
# List applications
argocd app list

# Sync application
argocd app sync myapp

# View app status
argocd app get myapp
```

## Troubleshooting

### Debug Pods

```bash
# Debug failing pod
oc debug pod/myapp-xxxxx

# Debug with specific image
oc debug pod/myapp-xxxxx --image=busybox

# Debug node
oc debug node/worker-0

# Start debug pod in project
oc run debug --image=busybox -it --rm -- /bin/sh
```

### Common Issues

| Issue | Check | Solution |
|-------|-------|----------|
| **ImagePullBackOff** | `oc describe pod` | Check image name, registry auth |
| **CrashLoopBackOff** | `oc logs pod --previous` | Fix application error |
| **Pending pod** | `oc describe pod` | Check resources, node availability |
| **Permission denied** | SCC | Add appropriate SCC |
| **Route not accessible** | `oc get route` | Check router, DNS |

### Diagnostic Commands

```bash
# Cluster health
oc get nodes
oc get co  # Cluster operators
oc adm top nodes

# Events (sorted by time)
oc get events --sort-by='.lastTimestamp'

# Pod diagnostics
oc describe pod myapp-xxxxx
oc logs myapp-xxxxx --previous
oc exec -it myapp-xxxxx -- /bin/sh

# Network diagnostics
oc debug node/worker-0 -- chroot /host tcpdump -i any port 80

# Resource issues
oc describe node worker-0 | grep -A 10 "Allocated resources"
oc adm top pods --containers
```

### Must-Gather

Collect diagnostic data for support.

```bash
# Full cluster must-gather
oc adm must-gather

# Specific image
oc adm must-gather --image=registry.redhat.io/openshift4/ose-must-gather

# With timeout
oc adm must-gather --timeout=30m
```

## Performance Optimization

### Resource Tuning

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    resources:
      requests:
        cpu: "100m"
        memory: "128Mi"
      limits:
        cpu: "500m"
        memory: "512Mi"
```

### Node Tuning Operator

```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: myapp-tuned
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom profile for myapp
      [sysctl]
      net.core.somaxconn=4096
      net.ipv4.tcp_max_syn_backlog=4096
    name: myapp-profile
  recommend:
  - match:
    - label: node-role.kubernetes.io/worker
    priority: 20
    profile: myapp-profile
```

## Cluster Upgrades

```bash
# Check available updates
oc adm upgrade

# View upgrade history
oc get clusterversion -o yaml

# Start upgrade
oc adm upgrade --to-latest
# Or specific version
oc adm upgrade --to=4.14.5

# Monitor upgrade progress
oc get clusterversion
oc get co
watch oc get nodes
```

## Multi-Cluster Management

### Red Hat Advanced Cluster Management (ACM)

```bash
# Install RHACM operator

# Create MultiClusterHub
oc apply -f - <<EOF
apiVersion: operator.open-cluster-management.io/v1
kind: MultiClusterHub
metadata:
  name: multiclusterhub
  namespace: open-cluster-management
spec: {}
EOF

# Import cluster
# Create ManagedCluster and KlusterletAddonConfig
```

## Best Practices Summary

| Area | Best Practice |
|------|---------------|
| **Deployments** | Use Deployments over DeploymentConfigs |
| **Images** | Use ImageStreams for tracking |
| **Builds** | Prefer S2I or Tekton pipelines |
| **Config** | Store in Git (GitOps) |
| **Security** | Use restricted SCC, network policies |
| **Monitoring** | Enable user workload monitoring |
| **Logging** | Forward to external storage |
| **Resources** | Set requests and limits |
| **Health** | Implement liveness/readiness probes |
| **Updates** | Keep cluster and operators updated |

---

## 🎉 Congratulations!

You've completed the OpenShift Zero to Hero course! You now have the knowledge to:

- ✅ Deploy and manage OpenShift clusters
- ✅ Create and manage applications
- ✅ Configure networking with Services and Routes
- ✅ Implement persistent storage
- ✅ Build images with S2I and BuildConfigs
- ✅ Use Operators for complex applications
- ✅ Secure workloads with SCCs and RBAC
- ✅ Monitor and troubleshoot applications
- ✅ Implement CI/CD with Pipelines and GitOps

---

## 📚 Additional Resources

- [OpenShift Documentation](https://docs.openshift.com/)
- [Red Hat Developer](https://developers.redhat.com/)
- [OpenShift Learning Portal](https://learn.openshift.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Tekton Documentation](https://tekton.dev/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)

---

## 🏆 Certifications

Consider pursuing Red Hat certifications:
- **EX180** - Red Hat Certified Specialist in Containers and Kubernetes
- **EX280** - Red Hat Certified Specialist in OpenShift Administration
- **EX288** - Red Hat Certified Specialist in OpenShift Application Development

---

**Happy OpenShifting! 🔴**

