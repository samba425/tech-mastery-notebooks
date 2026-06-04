# Kubernetes Interview Questions — Zero to Hero

330+ questions covering fundamentals through advanced topics, mapped where possible to **CKA**, **CKAD**, and **CKS** exam objectives. Includes hands-on labs, mock interview sets, scenario questions, comparison tables, a kubectl cheat sheet, and curated resources.

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

**1. What is Kubernetes?**
An open-source container orchestration platform that automates deployment, scaling, networking, and lifecycle management of containerized applications across a cluster of machines.

**2. Why Kubernetes over a container engine alone?**
Self-healing, declarative state, horizontal scaling, service discovery, rolling updates, secret/config management, multi-host networking — features Docker alone doesn't provide.

**3. What is a Pod?**
The smallest deployable unit in K8s — one or more containers sharing a network namespace, IPC namespace, and volumes; co-scheduled and co-located.

**4. Why is a Pod, not a container, the atomic unit?**
Sidecars (logging, proxy, init) often need to share storage and localhost. Pods model those tightly coupled workloads cleanly.

**5. What is a Node?**
A worker machine (VM or bare metal) that runs Pods. Has `kubelet`, `kube-proxy`, and a container runtime.

**6. What is the control plane?**
Cluster brain: API server, etcd, controller manager, scheduler, cloud-controller-manager. Makes global decisions.

**7. What is etcd?**
A distributed, strongly consistent key-value store that holds all cluster state.

**8. What is `kubelet`?**
The node agent. Receives PodSpecs from the API and ensures the containers are running as described.

**9. What is `kube-proxy`?**
A node component that programs iptables/IPVS rules to implement Services (ClusterIP routing).

**10. What is `kube-scheduler`?**
Watches for unscheduled pods and binds them to nodes by ranking nodes against constraints (resources, taints, affinity).

**11. What is `kube-controller-manager`?**
Runs core controllers (Deployment, ReplicaSet, Node, Endpoint, ServiceAccount, etc.) — each implementing a reconcile loop.

**12. What is `kube-apiserver`?**
The front-door REST API. Validates and persists objects to etcd; everything in K8s talks through it.

**13. What is the reconcile loop?**
Controllers continually compare *desired state* (spec) with *current state* (status) and take action to converge.

**14. What is a Deployment?**
A higher-level controller that manages ReplicaSets to provide declarative updates, rollback, and scaling for stateless pods.

**15. What is a ReplicaSet?**
Ensures a specified number of pod replicas are running. You rarely create them directly; Deployments manage them.

**16. What is a StatefulSet?**
Manages stateful pods with stable network identities (`pod-0`, `pod-1`), ordered start/stop, and per-pod PersistentVolumes.

**17. What is a DaemonSet?**
Runs one pod per node (or subset). Use for cluster-wide agents — log shippers, CNI, monitoring agents.

**18. What is a Job?**
Runs pods until a specified number successfully complete. Used for batch tasks.

**19. What is a CronJob?**
A Job that runs on a time schedule (cron syntax).

**20. What is a Service?**
A stable virtual IP and DNS name that load-balances to a set of pods selected by labels.

**21. Service types?**
`ClusterIP` (internal only), `NodePort` (exposes on every node port 30000-32767), `LoadBalancer` (cloud LB), `ExternalName` (DNS CNAME).

**22. What is a Headless Service?**
`clusterIP: None` — DNS returns pod IPs directly. Used by StatefulSets and clients that do their own load balancing.

**23. What is Ingress?**
A layer-7 routing object — maps HTTP(S) rules (host, path) to Services. Needs an Ingress controller (NGINX, Traefik, HAProxy, ALB).

**24. What's the Gateway API?**
The modern, role-oriented replacement for Ingress: `GatewayClass`, `Gateway`, `HTTPRoute`, `TCPRoute`, with cleaner extensibility.

**25. What is a Namespace?**
A virtual cluster — scope for object names, RBAC, network policies, resource quotas.

**26. Default namespaces?**
`default`, `kube-system` (control plane and add-ons), `kube-public` (publicly readable), `kube-node-lease` (heartbeats).

**27. What is a ConfigMap?**
A key-value store for non-sensitive configuration consumed by pods as env vars, mounted files, or CLI args.

**28. What is a Secret?**
Same as ConfigMap but base64-encoded and intended for sensitive data. Should be encrypted at rest in etcd via an encryption provider.

**29. What is a PersistentVolume (PV)?**
A cluster-level storage resource provisioned statically by an admin or dynamically by a StorageClass.

**30. What is a PersistentVolumeClaim (PVC)?**
A request for storage by a user; binds to a matching PV. Pods mount PVCs, not PVs.

**31. What is a StorageClass?**
A template describing how to dynamically provision storage (provisioner, parameters, reclaim policy).

**32. What is a Label?**
A key/value pair attached to objects, used by selectors for grouping (e.g., `app=web,env=prod`).

**33. What is an Annotation?**
Metadata key/value, larger and unstructured; not used for selection. Useful for tooling and audit data.

**34. What is a Selector?**
A query over labels: equality (`app=web`), set-based (`env in (dev,stage)`), or exists (`tier`).

**35. What's the difference between an Annotation and a Label?**
Labels are for selection; Annotations are arbitrary metadata, can be long, never selected on.

**36. What is RBAC?**
Role-Based Access Control: Roles/ClusterRoles define permissions, RoleBindings/ClusterRoleBindings tie them to subjects (users, groups, ServiceAccounts).

**37. What is a ServiceAccount?**
An identity for pods to authenticate to the API. Default SA exists per namespace.

**38. What is a NetworkPolicy?**
A firewall-like object that restricts pod-to-pod and pod-to-external traffic. Requires a CNI that enforces them (Calico, Cilium).

**39. What is Helm?**
A package manager that templates and deploys Kubernetes manifests as versioned "charts."

**40. What is a Helm chart?**
A directory of templates (`templates/`), default values (`values.yaml`), and metadata (`Chart.yaml`).

**41. What is a CRD?**
Custom Resource Definition — extends the Kubernetes API with your own resource kind.

**42. What is an Operator?**
A controller that watches a CRD and reconciles complex application logic (e.g., spinning up a Postgres cluster).

**43. What is a Pod IP?**
Each pod gets a unique cluster-routable IP (no NAT to other pods).

**44. What is a Service IP (ClusterIP)?**
A virtual IP allocated from the cluster's service CIDR; not on any interface — handled by `kube-proxy` rules.

**45. What is a CNI?**
Container Network Interface — plugin spec for pod networking (Calico, Cilium, Flannel, Weave).

**46. What is CSI?**
Container Storage Interface — plugin spec for dynamic storage drivers.

**47. What is CRI?**
Container Runtime Interface — gRPC API that `kubelet` uses to talk to a runtime (containerd, CRI-O).

**48. What is an admission controller?**
Code that intercepts API requests after authentication and authorization but before persistence; can mutate or validate.

**49. Validating vs Mutating admission webhook?**
Mutating runs first and can change the object; Validating runs last and can only accept/reject.

**50. What is `kubectl`?**
The official CLI client for the Kubernetes API.

**51. What is `kubeadm`?**
A bootstrapping tool that installs and joins K8s clusters (control plane + workers).

**52. What is a manifest?**
A YAML (or JSON) file describing a Kubernetes object. Applied with `kubectl apply -f`.

**53. Imperative vs declarative?**
Imperative: `kubectl run nginx`. Declarative: `kubectl apply -f deploy.yaml`. Declarative is recommended for production.

**54. What's the difference between `apply` and `create`?**
`create` errors if the object exists; `apply` does a 3-way merge (last-applied vs current vs new), allowing updates.

**55. What is a kubeconfig?**
A file (`~/.kube/config`) with clusters, users, contexts. Tells `kubectl` how to authenticate to which cluster.

**56. What is a context?**
A `cluster + user + namespace` tuple; switched with `kubectl config use-context`.

**57. What is a probe?**
Periodic check on a container: `liveness` (restart if failing), `readiness` (remove from Service endpoints), `startup` (gate other probes).

**58. Liveness vs Readiness?**
Liveness restarts unhealthy containers; Readiness pulls them from load balancing without killing them.

**59. What is an initContainer?**
A container that runs to completion before the main containers start. Used for setup tasks.

**60. What is a sidecar?**
A helper container in the same pod (logging, proxy, secrets agent). Since 1.28 GA, sidecars are formalized as initContainers with `restartPolicy: Always`.

---

## B. Architecture & Internals

**61. Walk through what happens when you `kubectl apply -f deploy.yaml`.**
1) kubectl parses YAML and POSTs to API server. 2) API server authenticates, authorizes (RBAC), runs admission webhooks, validates schema. 3) Object persisted to etcd. 4) Deployment controller creates a ReplicaSet. 5) ReplicaSet creates Pods. 6) Scheduler picks nodes. 7) Kubelet on each node receives PodSpec, instructs runtime to pull image and start containers. 8) Status reported back; controllers reconcile.

**62. How is leader election done in controllers?**
Endpoints/Leases API + atomic update. Only the leader runs reconcile loops; others stand by.

**63. What is the etcd snapshot/restore procedure?**
`etcdctl snapshot save snap.db` then on restore: stop control plane, `etcdctl snapshot restore snap.db --data-dir=/var/lib/etcd-new`, point etcd to new data dir, start control plane. `[CKA]`

**64. How many etcd nodes do you need?**
Odd number for quorum: 3, 5, or 7. Quorum = `(n/2)+1` for write availability.

**65. What's in a PodSpec?**
Containers (image, command, env, ports, resources, probes, mounts), volumes, nodeSelector, tolerations, affinity, serviceAccount, securityContext, networking flags.

**66. How does the scheduler decide?**
**Filter** (predicate) phase removes ineligible nodes (resource fit, taints, affinity), **Score** (priority) phase ranks remaining nodes, highest score wins.

**67. What are taints and tolerations?**
A *taint* on a node repels pods unless they carry a matching *toleration*. Used to dedicate nodes for special workloads.

**68. NodeAffinity vs nodeSelector?**
`nodeSelector` is a simple key=value equality. `nodeAffinity` supports operators (`In`, `NotIn`, `Exists`, `Gt`, `Lt`) and soft preferences (`preferredDuringSchedulingIgnoredDuringExecution`).

**69. Pod affinity vs anti-affinity?**
Affinity attracts pods to nodes where matching pods run (co-location). Anti-affinity repels (spread for HA).

**70. Topology Spread Constraints?**
Newer, more expressive way to spread pods across zones/nodes:
```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels: { app: web }
```

**71. PodDisruptionBudget (PDB)?**
Limits the number of pods voluntarily disrupted (drain, evict). `minAvailable` or `maxUnavailable`. Doesn't apply to involuntary disruptions like node crashes.

**72. What is a graceful shutdown sequence?**
SIGTERM sent to container -> preStop hook runs -> `terminationGracePeriodSeconds` timer -> SIGKILL. Pod removed from Service endpoints during this period.

**73. What is `kube-proxy` in iptables mode?**
Programs DNAT rules to send Service traffic to backend pod IPs. Cleanup via periodic resync.

**74. What is `kube-proxy` in IPVS mode?**
Uses IPVS for scalable L4 load balancing — better for thousands of services.

**75. What does `eBPF`-based kube-proxy (Cilium) do?**
Replaces iptables/IPVS with eBPF programs at the socket / TC layer for near-native performance and richer observability.

**76. How does DNS work in a cluster?**
CoreDNS runs as a Deployment with a ClusterIP. `/etc/resolv.conf` in pods points to it. Resolves `service.namespace.svc.cluster.local`.

**77. What are the DNS A records for a Service?**
`<svc>.<ns>.svc.cluster.local` (ClusterIP), and for a Headless Service, each backing pod gets `<pod-name>.<svc>.<ns>.svc.cluster.local`.

**78. SRV records?**
`_port-name._proto.<svc>.<ns>.svc.cluster.local`. Useful for service discovery.

**79. How does a Service forward traffic to pods?**
Service has an Endpoints (or EndpointSlice) object listing healthy pod IPs. `kube-proxy` programs rules per node.

**80. EndpointSlices vs Endpoints?**
EndpointSlices scale better (sharded), are the default since v1.21, and support dual-stack and topology hints.

**81. How does Ingress controller work?**
Watches Ingress objects, configures its underlying proxy (NGINX, Envoy), terminates TLS, routes to backend Services.

**82. What is TLS termination at Ingress?**
Decrypts HTTPS at the controller. Use TLS 1.2+ with strong ciphers (per security guidance). Keep certs in `kubernetes.io/tls` Secrets, ideally rotated by cert-manager.

**83. How does HPA work?**
Horizontal Pod Autoscaler queries metrics (CPU, memory, custom) every 15s via `metrics-server` or external adapter; computes desired replica count using `currentReplicas * (currentMetric / desiredMetric)`.

**84. VPA?**
Vertical Pod Autoscaler adjusts CPU/memory requests/limits over time based on observed usage. Recommends, auto-updates, or admission-mutates.

**85. Cluster Autoscaler?**
Adds/removes nodes (via cloud provider API) when pods are pending due to insufficient resources or nodes are underutilized.

**86. KEDA?**
Kubernetes Event-Driven Autoscaling — scales workloads from external triggers (Kafka lag, queue depth, Prometheus query) including scale-to-zero.

**87. What is the kubelet's pod manifest directory?**
`/etc/kubernetes/manifests` on control plane nodes. Files there create *static pods* directly (used for control plane components).

**88. Static pods vs pods?**
Static pods are managed by kubelet, mirror objects appear in API server. Used to bootstrap control plane.

**89. How is the API server highly available?**
Stateless — run multiple replicas behind a load balancer; etcd must be quorum-replicated.

**90. CRD storage in etcd?**
Custom resources are stored under `/registry/<group>/<resource>/<namespace>/<name>` like core resources.

**91. What is API aggregation?**
The API server can proxy `/apis/<group>` to an external API service (e.g., `metrics-server`, `service-catalog`).

**92. What is server-side apply (SSA)?**
A field-management mechanism where each manager (e.g., a controller, kubectl) records owned fields, preventing accidental overwrites.

**93. What are conditions?**
Per-resource status entries with `type`, `status`, `reason`, `message`, `lastTransitionTime` — used to surface state changes (e.g., `Ready=False`).

**94. Watch vs poll?**
`kubectl get -w` (and controllers) uses HTTP watch (long-poll with `Transfer-Encoding: chunked`) to receive incremental object updates.

**95. List/Watch with resource version?**
Initial list returns `resourceVersion`; watch starts from there. On disconnect, client re-lists at last RV or older.

**96. What is the informer pattern?**
client-go primitive: shared cache + watch handler. Controllers use it to build local indexed views of API objects.

**97. What is the work queue pattern?**
Informer events enqueue keys; workers dequeue and reconcile. Provides rate limiting and retry semantics.

**98. What's a finalizer?**
A pre-delete hook on an object. Deletion is held until controllers remove their finalizer; ensures cleanup of external resources.

**99. What's the `--field-manager` for SSA?**
Identifies which actor owns which fields, used to detect conflicts.

**100. What is `serverSideApply` conflict?**
When two managers claim the same field with different values; the client must resolve and retry with `--force-conflicts`.

**101. How does the API server handle authentication?**
Pluggable: client certificates, bearer tokens, OIDC, webhooks, ServiceAccount tokens, bootstrap tokens.

**102. ServiceAccount token projection?**
`TokenRequest`/`TokenProjected` volume issues short-lived audience-scoped JWTs to pods. Auto-rotated by kubelet.

**103. What is the audit log?**
API server logs every request (stage `RequestReceived`, `ResponseStarted`, `ResponseComplete`, `Panic`) per policy. Critical for compliance.

**104. How is etcd encrypted at rest?**
Via `EncryptionConfiguration` referenced by `--encryption-provider-config`. Recommended providers: `aescbc` (legacy) or KMS v2 with cloud KMS. Note: AES-CBC is acceptable for symmetric at-rest where authenticated by other means, but AES-GCM is preferred per crypto guidance.

**105. How does the cluster verify pulled images?**
By digest if specified; otherwise just by tag. Image signature verification needs an admission webhook (cosign + policy controllers like sigstore-policy-controller, Kyverno).

**106. How does node-to-node Pod traffic flow?**
Encapsulated (VXLAN/Geneve) or routed (BGP) by the CNI. Each pod's IP is reachable across nodes without NAT.

**107. What is Container Network Topology hints?**
Endpoints carry zone hints; kube-proxy prefers same-zone endpoints to reduce cross-zone traffic costs.

**108. eBPF in K8s?**
Used by Cilium for networking and observability, by Falco/Tetragon for security, and by `pixie`/`parca` for tracing — runs sandboxed kernel programs.

**109. What is the difference between cluster scope and namespace scope?**
ClusterRoles, Nodes, PVs, StorageClasses, CRDs, Namespaces are cluster-scoped. Pods, Deployments, Services, ConfigMaps, Secrets are namespace-scoped.

**110. How does the controller handle drift?**
Compares spec to status, takes corrective action. Many controllers also re-list periodically (resync) to handle missed events.

**111. What is API priority and fairness (APF)?**
Replaces `--max-requests-inflight`; classifies requests into priority levels and flow schemas to prevent noisy tenants from starving others.

**112. What is the difference between deployment strategies `RollingUpdate` and `Recreate`?**
`RollingUpdate` gradually replaces old pods with new (configurable `maxSurge`, `maxUnavailable`). `Recreate` deletes all old, then creates new — downtime.

**113. What's the default rolling update behavior?**
`maxSurge: 25%`, `maxUnavailable: 25%`.

**114. How does a Deployment roll back?**
`kubectl rollout undo deployment/<name> [--to-revision=N]`. Uses ReplicaSet history (default 10 revisions).

**115. What's a `revisionHistoryLimit`?**
How many old ReplicaSets to retain. Default 10; lower in CI-heavy clusters.

**116. What is the difference between a Deployment and a StatefulSet rolling update?**
Deployment updates pods in any order. StatefulSet updates in reverse ordinal order with partition support for canary.

**117. What is the OnDelete update strategy?**
For StatefulSets/DaemonSets: pods only update when manually deleted. Useful for controlled upgrades.

**118. What is `kubectl drain`?**
Cordons the node (no new pods), then evicts existing pods respecting PDBs. Used before maintenance.

**119. What does `kubectl uncordon` do?**
Marks the node schedulable again.

**120. What's the difference between eviction and deletion?**
Eviction respects PDBs and graceful shutdown; deletion is forceful. The scheduler considers evicted pods rescheduable; deletions may not be.

---

## C. Configuration & Day-to-Day Usage

**121. Show a minimal Pod YAML.**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello
  labels: { app: hello }
spec:
  containers:
    - name: app
      image: nginx:1.27
      ports: [{ containerPort: 80 }]
```

**122. Show a Deployment with rolling update and probes.**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }
  selector:
    matchLabels: { app: web }
  template:
    metadata:
      labels: { app: web }
    spec:
      containers:
        - name: web
          image: nginx:1.27
          ports: [{ containerPort: 80 }]
          readinessProbe:
            httpGet: { path: /, port: 80 }
            periodSeconds: 5
          livenessProbe:
            httpGet: { path: /, port: 80 }
            initialDelaySeconds: 10
          resources:
            requests: { cpu: 100m, memory: 128Mi }
            limits:   { cpu: 500m, memory: 256Mi }
```

**123. Show a ClusterIP Service.**
```yaml
apiVersion: v1
kind: Service
metadata: { name: web }
spec:
  selector: { app: web }
  ports:
    - port: 80
      targetPort: 80
```

**124. Show an Ingress.**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
    - hosts: [app.example.com]
      secretName: app-tls
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service: { name: web, port: { number: 80 } }
```

**125. Create a ConfigMap from a file?**
`kubectl create configmap nginx-conf --from-file=./nginx.conf`

**126. Mount it as a file in a pod?**
```yaml
volumes:
  - name: cfg
    configMap: { name: nginx-conf }
volumeMounts:
  - name: cfg
    mountPath: /etc/nginx/nginx.conf
    subPath: nginx.conf
```

**127. Inject a ConfigMap value as an env var?**
```yaml
env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef: { name: app-config, key: log_level }
```

**128. Create a Secret from literals?**
`kubectl create secret generic db --from-literal=password='<STRONG_PASSWORD>'`. Do **not** put secrets in source-control YAML.

**129. Reference a Secret in a Pod?**
```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef: { name: db, key: password }
```

**130. Show a StatefulSet for Postgres.**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata: { name: pg }
spec:
  serviceName: pg
  replicas: 3
  selector: { matchLabels: { app: pg } }
  template:
    metadata: { labels: { app: pg } }
    spec:
      containers:
        - name: pg
          image: postgres:16
          env:
            - name: POSTGRES_PASSWORD
              valueFrom: { secretKeyRef: { name: pg, key: pw } }
          volumeMounts: [{ name: data, mountPath: /var/lib/postgresql/data }]
  volumeClaimTemplates:
    - metadata: { name: data }
      spec:
        accessModes: [ReadWriteOnce]
        resources: { requests: { storage: 20Gi } }
        storageClassName: standard
```

**131. Show a DaemonSet.**
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata: { name: node-exporter, namespace: monitoring }
spec:
  selector: { matchLabels: { app: node-exporter } }
  template:
    metadata: { labels: { app: node-exporter } }
    spec:
      hostNetwork: true
      containers:
        - name: node-exporter
          image: quay.io/prometheus/node-exporter:v1.8.2
          args: [--path.rootfs=/host]
          volumeMounts: [{ name: root, mountPath: /host, readOnly: true }]
      volumes: [{ name: root, hostPath: { path: / } }]
      tolerations:
        - operator: Exists
```

**132. Show a Job.**
```yaml
apiVersion: batch/v1
kind: Job
metadata: { name: migrate }
spec:
  backoffLimit: 4
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - { name: m, image: myrepo/migrator:1.0, args: [--apply] }
```

**133. Show a CronJob.**
```yaml
apiVersion: batch/v1
kind: CronJob
metadata: { name: nightly }
spec:
  schedule: "0 2 * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - { name: backup, image: myrepo/backup:1.0 }
```

**134. Create a ServiceAccount and bind a Role.**
```yaml
apiVersion: v1
kind: ServiceAccount
metadata: { name: deployer, namespace: apps }
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata: { name: deploy, namespace: apps }
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "update", "patch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata: { name: deploy, namespace: apps }
subjects:
  - kind: ServiceAccount
    name: deployer
    namespace: apps
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: deploy
```

**135. Show a NetworkPolicy denying all ingress by default and allowing only from `web`.**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: deny-all, namespace: apps }
spec:
  podSelector: {}
  policyTypes: [Ingress]
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata: { name: allow-web-to-api, namespace: apps }
spec:
  podSelector: { matchLabels: { app: api } }
  policyTypes: [Ingress]
  ingress:
    - from: [{ podSelector: { matchLabels: { app: web } } }]
      ports: [{ protocol: TCP, port: 8080 }]
```

**136. Use `kubectl` to scale a deployment?**
`kubectl scale deployment web --replicas=5`

**137. Apply a manifest declaratively?**
`kubectl apply -f deploy.yaml`. Use `-k ./` for kustomize.

**138. Diff before applying?**
`kubectl diff -f deploy.yaml`

**139. Roll back?**
`kubectl rollout undo deployment/web --to-revision=3`

**140. Watch a rollout?**
`kubectl rollout status deployment/web`

**141. Delete a resource quickly?**
`kubectl delete deploy/web --grace-period=0 --force` (only for stuck resources).

**142. Edit a live resource?**
`kubectl edit deploy web` (opens editor; saves apply).

**143. Run a temporary debug pod?**
`kubectl run debug --image=nicolaka/netshoot -it --rm --restart=Never -- bash`

**144. Get pod logs across all containers?**
`kubectl logs pod/myapp --all-containers --since=1h`

**145. Stream logs from many pods?**
`stern web-` (third-party CLI), or `kubectl logs -l app=web -f --max-log-requests=10`.

**146. Forward a local port to a pod?**
`kubectl port-forward deploy/web 8080:80`

**147. Copy a file to a pod?**
`kubectl cp ./file.txt myapp:/tmp/file.txt`

**148. Exec into a pod?**
`kubectl exec -it myapp -c app -- sh`

**149. Show resource usage?**
`kubectl top nodes` / `kubectl top pods -A` (requires metrics-server).

**150. Switch namespace context?**
`kubectl config set-context --current --namespace=apps` (or `kubens apps`).

**151. Switch cluster context?**
`kubectl config use-context prod` (or `kubectx prod`).

**152. Find all pods on a specific node?**
`kubectl get pods -A -o wide --field-selector spec.nodeName=<node>`

**153. Find broken pods?**
`kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded`

**154. Output YAML for a resource you'd create?**
`kubectl create deployment web --image=nginx -o yaml --dry-run=client > deploy.yaml` `[CKAD]`

**155. Create a kustomization?**
```yaml
# kustomization.yaml
resources:
  - deploy.yaml
  - svc.yaml
images:
  - name: myapp
    newTag: 1.2.3
patches:
  - path: patch-replicas.yaml
```
`kubectl apply -k .`

**156. Install a Helm chart?**
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install web bitnami/nginx -n web --create-namespace
helm upgrade --install web bitnami/nginx -n web -f values.yaml
helm uninstall web -n web
```

**157. View Helm release values?**
`helm get values web -n web -a`

**158. Helm chart structure?**
```
mychart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    _helpers.tpl
  charts/         # subcharts
```

**159. Use a Helm template function?**
```yaml
metadata:
  name: {{ include "mychart.fullname" . }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
```

**160. Lint a chart?**
`helm lint ./mychart && helm template ./mychart | kubectl apply --dry-run=client -f -`

**161. Render templates without installing?**
`helm template web ./mychart -f values-prod.yaml > rendered.yaml`

**162. Use a values file per environment?**
`helm upgrade --install web ./mychart -f values.yaml -f values-prod.yaml`. Later files override earlier.

**163. Create a CRD?**
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata: { name: widgets.example.com }
spec:
  group: example.com
  scope: Namespaced
  names:
    plural: widgets
    singular: widget
    kind: Widget
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                color: { type: string }
```

**164. Use a CRD instance?**
```yaml
apiVersion: example.com/v1
kind: Widget
metadata: { name: blue }
spec: { color: "blue" }
```

**165. Set resource quotas?**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata: { name: team-quota, namespace: team-a }
spec:
  hard:
    requests.cpu: "20"
    requests.memory: 40Gi
    limits.cpu: "40"
    limits.memory: 80Gi
    pods: "100"
```

**166. Set defaults via LimitRange?**
```yaml
apiVersion: v1
kind: LimitRange
metadata: { name: defaults, namespace: team-a }
spec:
  limits:
    - type: Container
      default: { cpu: 500m, memory: 256Mi }
      defaultRequest: { cpu: 100m, memory: 128Mi }
```

**167. Use `EmptyDir` for scratch?**
```yaml
volumes:
  - name: cache
    emptyDir: { sizeLimit: 1Gi, medium: Memory }   # tmpfs if Memory
```

**168. Use a PVC in a Pod?**
```yaml
volumes:
  - name: data
    persistentVolumeClaim: { claimName: data-pvc }
volumeMounts:
  - { name: data, mountPath: /data }
```

**169. Define a PVC?**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: { name: data-pvc }
spec:
  accessModes: [ReadWriteOnce]
  resources: { requests: { storage: 5Gi } }
  storageClassName: standard
```

**170. Available `accessModes`?**
`ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany`, `ReadWriteOncePod` (1.27+).

**171. Image pull policy options?**
`Always`, `IfNotPresent` (default for tags), `Never`. `latest` implicitly forces `Always`.

**172. Use an image pull secret?**
```bash
kubectl create secret docker-registry regcred \
  --docker-server=<REG> --docker-username=<USER> \
  --docker-password='<PASSWORD>' --docker-email=<EMAIL>
```
```yaml
spec:
  imagePullSecrets: [{ name: regcred }]
```

**173. Apply via stdin?**
`cat deploy.yaml | kubectl apply -f -`

**174. Annotate a resource?**
`kubectl annotate deploy web "owner=team-x" --overwrite`

**175. Label a node?**
`kubectl label node <node> disktype=ssd`

**176. Taint a node?**
`kubectl taint nodes <node> dedicated=gpu:NoSchedule`

**177. Tolerate a taint?**
```yaml
tolerations:
  - key: dedicated
    operator: Equal
    value: gpu
    effect: NoSchedule
```

**178. Use nodeSelector?**
```yaml
nodeSelector: { disktype: ssd }
```

**179. Use podAntiAffinity to spread replicas?**
```yaml
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels: { app: web }
        topologyKey: kubernetes.io/hostname
```

**180. Use PriorityClass to evict lower-priority pods first?**
```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata: { name: high }
value: 1000000
preemptionPolicy: PreemptLowerPriority
globalDefault: false
description: "High priority workloads"
```

---

## D. Advanced Topics

**181. Explain the operator pattern in depth.**
A custom controller that watches a CRD and applications. Reconciles app-specific state (provisioning, backup, failover). Built with controller-runtime, kubebuilder, or operator-sdk.

**182. What is `controller-runtime`?**
Go library that abstracts informers, caches, reconcilers, webhooks, leader election. Foundation for kubebuilder/operator-sdk.

**183. Outline the reconcile function structure.**
```go
func (r *MyReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    obj := &v1.MyKind{}
    if err := r.Get(ctx, req.NamespacedName, obj); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }
    // 1. Add finalizer if missing
    // 2. Handle deletion (run finalizer cleanup, remove finalizer)
    // 3. Reconcile desired state (create/update child resources)
    // 4. Update status
    return ctrl.Result{RequeueAfter: 30 * time.Second}, nil
}
```

**184. How do you write a validating admission webhook?**
Implement an HTTPS server that handles `/validate`, registered via `ValidatingWebhookConfiguration` with appropriate `rules`, `caBundle`, `failurePolicy`, `sideEffects: None`, `admissionReviewVersions`.

**185. Why is `failurePolicy: Fail` risky during cluster upgrades?**
Webhook downtime can block all API writes for its rules. Use `Ignore` for cluster-add-on webhooks, or scope tightly.

**186. What is Pod Security Standards (PSS)?**
Three baselines: `privileged`, `baseline`, `restricted`. Enforced per namespace via Pod Security Admission (PSA) labels.

**187. Enable PSA?**
```yaml
metadata:
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
```

**188. What is OPA Gatekeeper?**
General-purpose policy engine — defines `ConstraintTemplate` (Rego) + `Constraint`. Enforces, audits.

**189. What is Kyverno?**
Policy engine using K8s-native YAML (no Rego). Supports validate, mutate, generate, image verify.

**190. Image signature enforcement?**
Sigstore policy controller / Kyverno's `verifyImages` rule checks cosign signatures and rejects unsigned images.

**191. What is a Service Mesh?**
A platform providing transparent service-to-service communication: mTLS, traffic routing, retries, observability. Examples: Istio, Linkerd, Cilium Service Mesh.

**192. mTLS in service mesh?**
Sidecars (or eBPF) terminate TLS using SPIFFE-style certificates issued by the mesh CA. Required keys/algorithms should be RSA-2048+ or ECC P-256.

**193. What is SPIFFE/SPIRE?**
SPIFFE is an identity spec (SVIDs). SPIRE is the runtime that issues short-lived workload certs/JWTs. Foundation of zero-trust mesh.

**194. What is Gateway API L4/L7?**
`HTTPRoute`, `TLSRoute`, `TCPRoute`, `UDPRoute` — typed routes that bind to Gateways. Replaces vendor-specific Ingress annotations.

**195. What is GitOps?**
Git is the source of truth; an agent (Argo CD, Flux) reconciles cluster state from Git. Auditable, declarative, rollback via revert.

**196. Argo CD vs Flux?**
Argo CD has a polished UI and Application CRDs (pull model). Flux is more "Unix philosophy" with focused controllers (Source, Kustomize, Helm). Both are CNCF graduated.

**197. App-of-apps pattern?**
A root Argo CD Application that points to a Git path containing child Application manifests. Allows hierarchical management.

**198. ApplicationSet?**
Generates many Argo CD Applications from generators (list, cluster, git directory). Pattern for managing fleets.

**199. Helm hooks?**
`pre-install`, `post-install`, `pre-upgrade`, `post-upgrade`, `pre-delete`, `post-delete`, `pre-rollback`, `post-rollback`. Used for migrations, test pods.

**200. Helm Chart dependencies?**
Defined in `Chart.yaml` under `dependencies:`, pulled into `charts/` via `helm dependency update`.

**201. OCI registries for Helm?**
`helm push mychart-1.0.0.tgz oci://reg/charts` and `helm install web oci://reg/charts/mychart --version 1.0.0`.

**202. Operator SDK vs kubebuilder?**
Operator SDK wraps kubebuilder and adds Ansible/Helm operators. Kubebuilder is the lower-level Go scaffolding.

**203. How does cert-manager work?**
Installs CRDs (Issuer, ClusterIssuer, Certificate). Watches for Ingress/Gateway annotations or Certificate resources, orchestrates ACME (Let's Encrypt) or other CA flows, manages renewals.

**204. Configure cert-manager + Let's Encrypt?**
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata: { name: letsencrypt-prod }
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: <YOUR_EMAIL>
    privateKeySecretRef: { name: letsencrypt-prod }
    solvers:
      - http01: { ingress: { class: nginx } }
```

**205. Multi-cluster patterns?**
- Federation (deprecated KubeFed)
- Cluster API for lifecycle
- Argo CD multi-cluster
- Service mesh federation (Istio multi-primary)
- Submariner / Skupper for cross-cluster networking

**206. What is Cluster API?**
A K8s-style API to manage clusters (clusters, machines, KubeadmControlPlane). Treats clusters as workloads.

**207. What is etcd defragmentation?**
`etcdctl defrag` reclaims space after large deletes. Required as part of routine etcd maintenance.

**208. What is `kube-bench`?**
Aqua's tool that runs CIS Kubernetes Benchmark checks against your cluster.

**209. What is `kube-hunter`?**
Aqua's pen-test tool that probes a cluster for vulnerabilities.

**210. What is Falco?**
Runtime security tool with eBPF/kernel-module sensors. Detects suspicious syscalls (e.g., shell spawned in a container).

**211. What is Tetragon?**
Cilium's eBPF-based runtime security with policy enforcement (block syscalls) — successor concept to Falco.

**212. How do you implement multi-tenancy?**
- Namespaces + RBAC + ResourceQuota/LimitRange
- NetworkPolicies isolating tenant namespaces
- Strict Pod Security Admission profiles
- Dedicated node pools per tenant if needed
- Multi-cluster (hard isolation)

**213. Hard vs soft multi-tenancy?**
Soft: namespaces in a shared cluster. Hard: separate clusters or virtual clusters (vcluster, Capsule).

**214. What is vcluster?**
Virtual K8s clusters running inside a host cluster — control plane in a pod, shared worker nodes.

**215. What is the difference between an Operator and a Helm chart?**
Helm renders YAML once at install/upgrade. Operators provide *continuous* reconciliation and domain-specific logic (failover, backup, version upgrades).

**216. Backup strategy for K8s?**
- etcd snapshots (control plane state)
- Velero (cluster-resource + PV snapshots)
- Application-level (DB dumps, object store backups)

**217. Velero workflow?**
```bash
velero install --provider aws --bucket <BUCKET> ...
velero backup create daily --include-namespaces apps --ttl 720h
velero restore create --from-backup daily
```

**218. Upgrade a cluster (kubeadm)?**
1) `kubeadm upgrade plan` 2) `kubeadm upgrade apply v1.31.0` on first CP node, then `kubeadm upgrade node` on others. 3) Drain, upgrade kubelet+kubectl, uncordon for each worker. `[CKA]`

**219. Skew policy?**
kubelet ≤ control plane minor version; never skip minor versions when upgrading.

**220. What is `serviceMonitor` / `podMonitor`?**
Prometheus Operator CRs that select Services/Pods to scrape; an alternative to native Prometheus YAML scrape configs.

**221. PrometheusRule?**
CR defining recording and alerting rules consumed by the Prometheus Operator.

**222. What is the Operator Lifecycle Manager (OLM)?**
Manages installation and updates of operators via Subscriptions and CatalogSources. Common on OpenShift.

**223. What is GitOps drift?**
Cluster state diverges from Git. Argo CD shows `OutOfSync`; auto-sync optionally remediates.

**224. Progressive delivery — what tools?**
Argo Rollouts, Flagger — implement canary, blue/green, experiments with metric-based promotion.

**225. Implement canary with Argo Rollouts?**
```yaml
spec:
  strategy:
    canary:
      steps:
        - setWeight: 5
        - pause: { duration: 5m }
        - setWeight: 25
        - pause: { duration: 10m }
        - setWeight: 100
      analysis:
        templates: [{ templateName: latency }]
```

**226. What is `EndpointSlice` topology aware routing?**
Hints in EndpointSlices let kube-proxy prefer same-zone backends, reducing cross-AZ traffic.

**227. What is in-place pod resize?**
Beta feature (1.27+) allowing CPU/memory request/limit changes without recreating the pod.

**228. What is the difference between `containerd` and Docker for K8s?**
Since 1.24, the dockershim was removed from kubelet. Clusters use containerd (or CRI-O) directly via CRI; Docker is no longer a runtime for kubelet.

**229. What are sandbox containers?**
Pods run inside lightweight VMs (Kata, gVisor) for stronger isolation. Configured via RuntimeClass.

**230. What is RuntimeClass?**
Selects an alternative runtime handler per pod (e.g., `runc` vs `kata-qemu`):
```yaml
spec:
  runtimeClassName: kata
```

**231. What is `vertical-pod-autoscaler` in `Auto` mode risk?**
Eviction to apply new requests — incompatible with HPA on CPU/memory. Use HPA on custom metrics with VPA in Initial/Off mode.

**232. What is `ResourceClaim` (Dynamic Resource Allocation)?**
Beta API allowing pods to claim specialized devices (GPUs, accelerators) similar to PVCs.

**233. What is Sidecar containers (v1.28 GA)?**
Init containers with `restartPolicy: Always` run for the pod's lifetime alongside main containers — first-class support.

**234. What is the `ImageVolumes` feature?**
Mount OCI image content as a volume into a pod without running it as a container (alpha/beta in newer releases).

**235. What is Kueue?**
A K8s-native job queue and batch scheduler — provides resource fairness across teams.

**236. What is Karpenter?**
AWS-built node autoscaler that provisions right-sized nodes from EC2 in seconds, replacing CA in many AWS setups.

**237. What is the OpenTelemetry Operator?**
Installs and manages OTel Collectors and auto-instrumentation injection (Java, Node, Python, .NET, Go).

**238. What is the `local-path-provisioner`?**
Rancher's simple dynamic provisioner using `hostPath`. Default in k3s/k3d/RKE2.

**239. What is the EFK / PLG stack?**
EFK: Elasticsearch, Fluentd, Kibana. PLG: Promtail, Loki, Grafana. Logging pipelines on K8s.

**240. What is Cilium's Hubble?**
Service map + flow logs built on Cilium's eBPF data plane.

---

## E. Security, Performance & Best Practices

**241. Hardening checklist — top 10:**
1) Enforce PSS `restricted` profile via PSA. 2) Disable anonymous auth. 3) Encrypt etcd at rest. 4) Enable audit logging. 5) Run kube-bench periodically. 6) Use NetworkPolicies default deny. 7) Sign images and verify at admission. 8) Use ServiceAccount tokens via Projected with short TTL. 9) Patch nodes regularly. 10) Limit kubelet read-only port and use webhook authz.

**242. RBAC best practices?**
Least privilege; avoid `cluster-admin`; prefer Roles over ClusterRoles when namespace-scoped; one SA per workload; periodic audit (`rbac-lookup`, `audit2rbac`).

**243. Why disable the default ServiceAccount token auto-mount?**
`automountServiceAccountToken: false` for pods that don't need API access — reduces leak risk.

**244. How to scope a Secret to one pod?**
Strict RBAC on the Secret + use Projected token; consider external secret managers (Vault, AWS SM, SOPS) with sealed-secrets or external-secrets-operator.

**245. What is SOPS-encrypted GitOps?**
Encrypt secrets with `sops` (using KMS, AGE, GPG); commit encrypted; Flux SOPS controller decrypts at sync.

**246. external-secrets-operator vs sealed-secrets?**
ESO syncs values from external stores into K8s Secrets continuously. Sealed-Secrets encrypts the entire Secret blob with the cluster's public key.

**247. Image pull from private registry — secure pattern?**
Per-namespace `imagePullSecret` referenced by the SA, or use cloud-provider IAM integrations (IRSA on EKS, Workload Identity on GKE).

**248. PodSecurityContext essentials?**
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000
  seccompProfile: { type: RuntimeDefault }
containers:
  - securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities: { drop: [ALL], add: [NET_BIND_SERVICE] }
```

**249. How to test NetworkPolicies?**
`kubectl run probe --image=nicolaka/netshoot -it --rm -- bash` then `curl` to allowed/denied destinations.

**250. CNI for network policy enforcement?**
Calico, Cilium, Antrea, Weave. The default Flannel doesn't enforce NetworkPolicy.

**251. Performance: where to set `--max-pods`?**
On kubelet (default 110). Tune carefully — too many pods saturates kube-proxy and Pod CIDR.

**252. etcd performance tips?**
Dedicated SSD, low-latency disk, separate from other workloads, regular defrag, monitor `etcd_disk_wal_fsync_duration_seconds`.

**253. API server tuning?**
Tune APF, `--max-requests-inflight`, `--watch-cache-sizes`. Scale horizontally behind LB.

**254. Avoid `kubectl get all` in scripts — why?**
It hits multiple API endpoints; expensive in big clusters and doesn't return *all* resource kinds.

**255. Helm best practices?**
- Pin chart versions
- Validate with `helm lint` + `kubeval`/`kubeconform`
- Avoid `lookup` in templates (non-reproducible)
- Don't bake secrets in `values.yaml`
- Use schema (`values.schema.json`)

**256. Resource request/limit best practice?**
Set requests = observed steady-state. Limits = burst ceiling. Never leave CPU limits much higher than requests on critical paths (throttling).

**257. Why setting CPU limits can backfire?**
CFS throttling can spike latencies. Many teams set CPU requests only and skip CPU limits; opinions vary — measure.

**258. QoS classes?**
`Guaranteed` (requests=limits), `Burstable` (requests<limits), `BestEffort` (none). Eviction order: BestEffort → Burstable → Guaranteed.

**259. Pod evictions vs deletions?**
Node pressure evictions (memory, disk) preempt low-QoS pods; PDBs not respected. Voluntary evictions (`drain`) respect PDBs.

**260. Pod priority preemption?**
Higher-priority pending pods can evict lower-priority running pods to make room.

**261. How to reduce control-plane load from sidecar logs?**
Use a logging agent (Fluent Bit, Vector) DaemonSet to tail container files directly; avoid `kubectl logs` polling.

**262. Why limit watch concurrency?**
Too many controllers watching everything floods API/etcd. Use field/label selectors and namespace scoping.

**263. RBAC review tools?**
`rakkess` (effective access), `rbac-lookup`, `audit2rbac` (build minimal RBAC from audit logs).

**264. NetworkPolicy review?**
`np-viewer`, Cilium's Hubble, Calico's `calicoctl` audit.

**265. Image scanning best practices?**
Scan at build (CI), scan in registry continuously, admission-time policy with Trivy Operator or Kyverno.

**266. Secret rotation?**
Use external-secrets-operator with TTL; rotating Secret triggers Deployment reconcile via `reloader` annotation or pod restart hook.

**267. Pod-to-Pod TLS without a mesh?**
Application-managed mTLS using cert-manager-issued certs mounted via Secret. Heavier ops than mesh.

**268. Hardening kubelet?**
Disable anonymous auth (`--anonymous-auth=false`), enable webhook authz, set TLS cipher suites to strong AEAD, rotate certs (`--rotate-certificates`), restrict `kubectl exec` via RBAC.

**269. Audit policy minimum?**
Log at least `Metadata` for everything, `Request` for changes, `RequestResponse` for Secrets. Keep volume bounded with rules.

**270. Common CKS topics?**
PSS, NetworkPolicies, image signing, audit, runtime detection (Falco), upgrade hygiene, secret encryption, RBAC, supply chain (cosign, SBOM).

---

## F. Troubleshooting & Debugging

**271. Pod stuck in `Pending` — diagnosis?**
`kubectl describe pod` — usually scheduling issues (insufficient resources, no matching node selector, unbound PVC, taints).

**272. `ImagePullBackOff` — causes?**
- Bad image name/tag
- Private registry without imagePullSecret
- Registry rate-limit / outage
- Image arch mismatch
- DNS issue from node to registry

**273. `CrashLoopBackOff` — playbook?**
1) `kubectl logs <pod> --previous` 2) `kubectl describe` for events 3) Check probes (failing readiness causes restarts) 4) `kubectl exec` if you can keep it alive (`sleep infinity`) 5) Inspect exit code (`State.Terminated.ExitCode`).

**274. Pod stuck `Terminating`?**
- Finalizers blocking deletion: `kubectl patch pod <p> -p '{"metadata":{"finalizers":null}}' --type=merge`
- Stuck volume detach (node gone): force delete `--grace-period=0 --force`

**275. `0/3 nodes are available: 3 Insufficient cpu` — fix?**
Lower pod requests, scale up nodes, scale down other workloads, or adjust priority.

**276. Pods can't resolve external DNS?**
Check CoreDNS pods/logs, kubelet `--cluster-dns` arg, `ndots:5` rewriting; consider `dnsPolicy: None` with explicit `dnsConfig` for special pods.

**277. CoreDNS NXDOMAIN spam?**
Typically due to `ndots:5` causing search-domain expansions. Add `search` domains carefully or use FQDNs.

**278. Service has no endpoints?**
Label selector doesn't match any pod labels, or pods aren't ready (readinessProbe failing).

**279. Pod-to-pod traffic blocked?**
NetworkPolicy denying, CNI plugin misconfigured, IPtables/IPVS rules stale (restart kube-proxy).

**280. Pod can't reach a Service inside its own pod?**
Loopback isn't routed through kube-proxy in default IPVS mode; use a sidecar or the pod's localhost listener.

**281. Slow pod startup?**
Image pull (too big / cold cache), init containers, slow PVC provisioning, registry latency. Check `kubectl describe pod` event timestamps.

**282. PVC stuck `Pending`?**
- StorageClass missing or invalid
- Provisioner pod down
- WaitForFirstConsumer + no consuming pod yet
- Quota exhausted

**283. Node `NotReady`?**
`kubectl describe node` — check `Conditions` (MemoryPressure, DiskPressure, PIDPressure, NetworkUnavailable). Inspect kubelet logs (`journalctl -u kubelet`).

**284. Schedule pods only on healthy nodes?**
Default behavior; ensure `node.kubernetes.io/not-ready:NoSchedule` taint isn't tolerated by your pods.

**285. `kubectl exec` fails with "unable to upgrade connection"?**
kubelet -> API connectivity issue, certificate trust problem, or webhook authz denying.

**286. Container OOMKilled (exit 137)?**
Increase memory limit, fix memory leak, profile heap. `kubectl describe pod` shows OOMKilled.

**287. Excessive evictions on node?**
`kubelet` thresholds (`--eviction-hard`); investigate disk usage, image cache, log volumes.

**288. etcd alarms (`NOSPACE`)?**
DB size hit quota (default 2GiB). Defrag, compact, and increase `--quota-backend-bytes`.

**289. API server unreachable?**
Check etcd quorum; LB health; cert validity; SAN of API server cert; firewall rules.

**290. Cluster autoscaler not adding nodes?**
Pods don't have scheduling failures CA understands, taints don't match, ASG limit reached, node group selector wrong.

**291. Slow Helm install?**
`--atomic --wait` blocks until all resources are ready. Often crashloops keep it spinning. Tail `kubectl get events -w`.

**292. Argo CD `OutOfSync` but auto-sync isn't fixing?**
Check sync policy (`automated.prune`, `selfHeal`), resource ignore rules, finalizers blocking deletes.

**293. Webhook timeouts?**
Webhook endpoint slow; set `timeoutSeconds`, increase replicas, set `failurePolicy: Ignore` for non-critical webhooks.

**294. Mass pod restarts after node upgrade?**
Taint+drain procedure not respected, or PDBs too strict (or none). Use `kubectl drain --grace-period=120 --delete-emptydir-data=false --ignore-daemonsets`.

**295. Pods running but service unhealthy externally?**
Check Ingress controller logs, TLS expiry, LoadBalancer health checks, security groups, DNS propagation.

**296. Random 502s from Ingress?**
- Backend pod terminating but still in endpoints (use `preStop` sleep + readinessProbe to drain)
- Keep-alive mismatch
- Worker connection limits

**297. `etcdctl` connection refused inside cluster?**
Use mTLS certs:
```bash
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key endpoint health
```

**298. Why is `kubectl top` empty?**
`metrics-server` not installed or `--kubelet-insecure-tls` flag missing in lab clusters with self-signed kubelet certs.

**299. Slow `kubectl` calls?**
Large object cache, server-side throttling (APF), or network. Use `--cache-dir`, narrow with selectors/`-o name`.

**300. Pods scheduled to wrong AZ?**
Use topologySpreadConstraints + nodeAffinity on `topology.kubernetes.io/zone`.

---

## G. Real-World Scenario-Based Questions

**301. Migrate a monolith to K8s — phases?**
1) Containerize 2) Externalize state and config 3) Run via Deployment + Service 4) Add health probes + resource requests 5) Add HPA 6) Set up CI/CD with GitOps 7) Add observability and policies.

**302. Design a multi-region cluster topology.**
One cluster per region (HA control planes), global LB (Anycast or DNS), cross-region replication for stateful services (Postgres logical replication, Kafka MirrorMaker), Argo CD ApplicationSets to fan out manifests, mesh federation for in-cluster traffic.

**303. Implement zero-downtime DB schema migrations.**
Use **backward-compatible migrations**: deploy code that handles both schemas → run migration as a Job → deploy code that only uses new schema. Argo Rollouts with analysis can automate.

**304. Implement canary release.**
Argo Rollouts canary: weight 10% → analysis → 50% → analysis → 100%. AnalysisTemplate queries Prometheus for error rate; abort on regression. `[CKAD]`

**305. Auto-scale a Kafka consumer based on lag.**
Install KEDA, create `ScaledObject` with `kafka` trigger and `lagThreshold`. Scales from 0..N consumers.

**306. Restrict tenants to their namespaces with full self-service.**
Per-tenant namespace; tenant gets `admin` ClusterRole bound only to their namespace; ResourceQuota + LimitRange + NetworkPolicy applied via Kyverno generation rule.

**307. Roll out a kernel upgrade across all nodes.**
Drain node → upgrade OS → reboot → uncordon. Tools: kured (Kubernetes Reboot Daemon) automates with PDB respect; or operator (Cluster API).

**308. Encrypt application secrets without giving devs cluster-admin.**
external-secrets-operator with KMS backend; devs manage `ExternalSecret` referencing keys in Vault/AWS SM. Their RBAC limits which secret paths they can reference (via Vault policies).

**309. Build a CI pipeline that deploys to K8s on merge to main.**
Build image → scan (Trivy) → push with SHA tag → update Kustomize overlay in Git → Argo CD detects → syncs → run smoke tests → notify.

**310. Detect a crypto-miner running in a pod.**
Falco rule detecting outbound to known mining pools, high CPU + low disk I/O signature. Kill pod, snapshot for forensics, rotate compromised credentials.

**311. Reduce cross-AZ traffic costs.**
Topology-aware routing on Services; node affinity to keep tightly coupled pods in same AZ; cache layer per AZ.

**312. Implement a private internal Helm chart registry.**
ChartMuseum or Harbor with OCI Helm support; CI publishes charts; Argo CD references private registry with credentials.

**313. App needs 10K req/s; current pod can do 200. Scaling plan?**
50 pods baseline + HPA on requests-per-second custom metric (Prometheus adapter). Cluster Autoscaler/Karpenter for node capacity. Connection pooling on upstream. Spread across multiple AZs.

**314. Service mesh adoption — first 30 days?**
Start with one namespace and observability only (no mTLS enforcement). Validate latency overhead. Add mTLS STRICT progressively. Migrate ingress from Ingress controller to Gateway or mesh ingress.

**315. App fails after upgrade — quick rollback?**
`kubectl rollout undo deployment/app`. Or in GitOps: `git revert` the offending commit; Argo CD reverts cluster state.

**316. Restrict prod image registries.**
Kyverno ClusterPolicy rejecting any image not from `registry.internal/*`.

**317. Throughput drops after kubelet upgrade.**
Check CPU manager policy, cgroup driver mismatch, kernel version compatibility, sidecar resource caps; look at `kubelet_pleg_relist_duration_seconds`.

**318. Stuck `Terminating` namespace?**
Often a finalizer on a CRD with no controller. Manually edit the namespace JSON to remove `spec.finalizers`, PUT to `/api/v1/namespaces/<ns>/finalize`. `[CKA]`

**319. Disaster recovery for the whole cluster.**
- etcd snapshot to S3 hourly
- Velero backups daily (resources + PV snapshots)
- DR runbook with restore order: etcd → control plane → workloads
- Test quarterly

**320. Sticky sessions in K8s?**
Use Service `sessionAffinity: ClientIP` (L4 sticky), or Ingress controller cookie-based stickiness for HTTP.

**321. Run a workload that needs >1 CPU exclusively.**
`static` CPU manager policy on kubelet + Guaranteed QoS pod with integer CPU requests = limits.

**322. Run sandboxed code (CTF judge, plugin runtime).**
Per-pod RuntimeClass = gVisor or Kata; strict seccomp; network egress denied; ephemeral PV; CPU/memory quotas.

**323. Apply different security profiles per environment via GitOps.**
Kustomize overlays for prod with stricter PSS labels, NetworkPolicies, image policies — Argo CD ApplicationSet per env.

**324. Storage migration from EBS gp2 to gp3?**
Use a VolumeSnapshot to capture, create new PVC from snapshot with new StorageClass, swap PVC reference on the pod, delete old PVC.

**325. Run a CI runner on K8s securely.**
Use ephemeral pods (Tekton, Actions Runner Controller), least-privileged SA, no docker.sock (use Kaniko or BuildKit rootless), strict NetworkPolicy.

**326. Implement traffic mirroring for safe testing?**
Istio `VirtualService` with `mirror:` field copies live traffic to a shadow service. Argo Rollouts also supports.

**327. Replace `kubectl edit` for incident hot-patches?**
Don't. Use Git → PR → Argo CD sync (or `kubectl apply -f`); manual edits cause drift and lose audit trail.

**328. Implement blue/green with Argo Rollouts?**
```yaml
strategy:
  blueGreen:
    activeService: web-active
    previewService: web-preview
    autoPromotionEnabled: false
```

**329. Pull-secret rotation across 50 namespaces?**
`kubectl create secret docker-registry ...` templated by Kyverno generate rule, or external-secrets-operator with a ClusterExternalSecret.

**330. Track which deployment caused an SLO regression.**
Correlate deploy events with metrics (KEDA's KEDA-Notification, Argo Events, custom annotations). Tools: Prometheus + Grafana + deploy markers via the Annotation API.

---

## H. Comparison Tables

### Workload Resources

| Resource | Stateless | Stateful | DaemonSet | Job | CronJob |
|----------|-----------|---------|-----------|-----|---------|
| Pod identity | Random | Stable ordinal | Per node | Run-to-completion | Scheduled |
| Storage | EphemeralOrPVC | PVC per pod | Often hostPath | Optional | Optional |
| Use case | Web/API | DB, queue | Agent | One-off task | Recurring |

### Services

| Type | Scope | Exposure | LB |
|------|-------|----------|----|
| ClusterIP | Cluster-internal | None | kube-proxy |
| NodePort | Each node | port 30000-32767 | kube-proxy |
| LoadBalancer | External | Cloud LB | Cloud LB |
| ExternalName | DNS CNAME | None | None |
| Headless | No VIP | DNS pod IPs | Client |

### Ingress vs Gateway API

| Aspect | Ingress | Gateway API |
|--------|---------|-------------|
| Roles | Single object | GatewayClass / Gateway / Route |
| Multi-tenant | Annotations hack | Built-in role split |
| L4 support | Vendor-specific | Native (TCPRoute, etc.) |
| Extensibility | Annotations | Typed extensions |
| Maturity | GA, ubiquitous | GA in 1.30 |

### Container Runtimes

| Runtime | OCI | CRI | Daemon | Use |
|---------|-----|-----|--------|-----|
| containerd | Yes | Yes | Yes | Default in most K8s |
| CRI-O | Yes | Yes | Yes | OpenShift, lightweight |
| docker | Yes | Removed (1.24) | Yes | Dev only |
| runsc (gVisor) | Yes | Via RuntimeClass | No | Sandboxed isolation |
| kata | Yes | Via RuntimeClass | No | VM isolation |

### CNI Plugins (selected)

| CNI | NetworkPolicy | Encryption | eBPF | Best for |
|-----|--------------|-----------|------|---------|
| Calico | Yes | WireGuard | Optional | Policy-rich |
| Cilium | Yes | WireGuard/IPsec | Full | Performance + observability |
| Flannel | No | No | No | Simple labs |
| Weave | Yes | Yes | No | Mesh-like |
| Antrea | Yes | IPsec | Optional | OVS-based |

### HPA vs VPA vs CA vs KEDA

| Aspect | HPA | VPA | CA | KEDA |
|--------|-----|-----|----|------|
| Scales | Pod count | Pod size | Node count | Pod count (event) |
| Source | metrics-server / custom | Recommender | Pending pods | External events |
| Conflicts | — | With HPA on same metric | With non-K8s scalers | — |

---

## I. Hands-On Labs

Prereqs: a working `kind`/`minikube`/`k3d` cluster, `kubectl`, `helm`. Substitute your registry where shown.

### Lab 1 — Deploy a Multi-Container Pod (Sidecar)

```yaml
apiVersion: v1
kind: Pod
metadata: { name: app, labels: { app: app } }
spec:
  containers:
    - name: app
      image: nginx:1.27
      volumeMounts: [{ name: logs, mountPath: /var/log/nginx }]
    - name: log-shipper
      image: busybox
      args: [sh, -c, "tail -F /var/log/nginx/access.log"]
      volumeMounts: [{ name: logs, mountPath: /var/log/nginx }]
  volumes: [{ name: logs, emptyDir: {} }]
```

`kubectl apply -f pod.yaml && kubectl logs app -c log-shipper -f`

---

### Lab 2 — Rolling Update + Rollback

```bash
kubectl create deployment web --image=nginx:1.27
kubectl scale deployment web --replicas=4
kubectl set image deployment/web nginx=nginx:1.28
kubectl rollout status deployment/web
kubectl rollout history deployment/web
kubectl rollout undo deployment/web
```

Expected: zero-downtime upgrade; rollback works.

---

### Lab 3 — StatefulSet with Per-Pod PVCs

Apply the StatefulSet from Q130 (Postgres), confirm:
```bash
kubectl get pvc -l app=pg
kubectl exec -it pg-0 -- psql -U postgres -c "select inet_server_addr()"
```

Test deletion + recreation of `pg-0`; data persists via the bound PVC.

---

### Lab 4 — NetworkPolicy Default-Deny

Apply both manifests from Q135. Verify:
```bash
kubectl run probe --image=nicolaka/netshoot -it --rm --restart=Never -- \
  bash -c "curl --max-time 3 http://api.apps.svc.cluster.local:8080 || echo BLOCKED"
```

Run the same probe with label `app=web` and confirm it succeeds.

---

### Lab 5 — Ingress + cert-manager + Let's Encrypt (Staging)

```bash
helm repo add jetstack https://charts.jetstack.io
helm upgrade --install cert-manager jetstack/cert-manager \
  -n cert-manager --create-namespace --set installCRDs=true
```

Apply the `ClusterIssuer` from Q204 (use staging URL `https://acme-staging-v02.api.letsencrypt.org/directory` for tests). Annotate your Ingress, watch `Certificate` reach `Ready=True`.

---

### Lab 6 — HPA on CPU

```bash
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata: { name: php }
spec:
  replicas: 1
  selector: { matchLabels: { app: php } }
  template:
    metadata: { labels: { app: php } }
    spec:
      containers:
        - name: php
          image: registry.k8s.io/hpa-example
          resources: { requests: { cpu: 200m } }
          ports: [{ containerPort: 80 }]
---
apiVersion: v1
kind: Service
metadata: { name: php }
spec:
  selector: { app: php }
  ports: [{ port: 80 }]
EOF

kubectl autoscale deploy php --cpu-percent=50 --min=1 --max=10

# Load
kubectl run load --image=busybox -it --rm --restart=Never -- \
  /bin/sh -c "while sleep 0.01; do wget -q -O- http://php; done"

# Watch
kubectl get hpa php -w
```

---

### Lab 7 — Write a Tiny CRD + Controller (Conceptual Walkthrough)

```bash
go install sigs.k8s.io/kubebuilder/v3/cmd/kubebuilder@latest
kubebuilder init --domain example.com --repo example.com/widget
kubebuilder create api --group app --version v1 --kind Widget
# Edit api/v1/widget_types.go and controllers/widget_controller.go
make install run
kubectl apply -f config/samples/app_v1_widget.yaml
```

Goal: see your reconcile log lines fire on resource create/update/delete.

---

### Lab 8 — Backup with Velero

```bash
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.10.0 \
  --bucket <BUCKET> --backup-location-config region=us-east-1 \
  --secret-file ./credentials-velero \
  --use-volume-snapshots=true

velero backup create app-backup --include-namespaces apps
velero restore create --from-backup app-backup
```

---

### Lab 9 — Cluster Hardening Scan

```bash
docker run --rm -it --pid=host \
  -v /etc:/etc:ro -v /var:/var:ro \
  aquasec/kube-bench:latest --benchmark cis-1.24
```

Address every `[FAIL]` item per cluster context.

---

### Lab 10 — GitOps with Argo CD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f \
  https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd port-forward svc/argocd-server 8080:443

argocd login localhost:8080 --insecure --username admin \
  --password "$(kubectl -n argocd get secret argocd-initial-admin-secret \
                   -o jsonpath='{.data.password}' | base64 -d)"

argocd app create demo \
  --repo https://github.com/argoproj/argocd-example-apps.git \
  --path guestbook --dest-server https://kubernetes.default.svc \
  --dest-namespace default --sync-policy automated --self-heal --auto-prune
```

Edit a manifest in Git -> watch Argo CD sync -> revert and watch self-heal.

---

## J. Mock Interview Sets

60 minutes per set, 4 minutes per question.

### Mock Set 1 — Foundations

1. Difference between a Pod and a Deployment.
2. Walk through what happens when you apply a Deployment YAML.
3. Show the difference between liveness and readiness probes.
4. ClusterIP vs NodePort vs LoadBalancer — when do you pick each?
5. How is DNS resolved inside a pod?
6. What is RBAC; show a Role + RoleBinding.
7. PV vs PVC vs StorageClass.
8. ConfigMap vs Secret; how would you rotate a Secret?
9. Explain `kubectl apply` vs `kubectl create`.
10. What are taints/tolerations vs nodeSelector vs affinity?
11. Default Pod Security Standards; how to enforce.
12. Why prefer Deployments over manually creating Pods.
13. Difference between Service `targetPort` and `port`.
14. Helm chart structure and what `helm install` does under the hood.
15. Show a Pod with non-root user, dropped caps, and read-only FS.

### Mock Set 2 — Architecture & Networking

1. Control plane components and their responsibilities.
2. Why etcd needs odd-numbered members.
3. Explain `kube-proxy` modes.
4. How is a pod's IP routed across nodes?
5. NetworkPolicy default-deny — write the YAML.
6. CNI vs CSI vs CRI.
7. Difference between Endpoints and EndpointSlices.
8. Describe how HPA computes target replicas.
9. What is APF and why is it useful?
10. Explain CRD + Operator pattern.
11. Validating vs mutating webhooks; risk of `failurePolicy: Fail`.
12. Ingress vs Gateway API.
13. Implement mTLS between two services.
14. CoreDNS pain points (NXDOMAIN, ndots:5) and mitigation.
15. Explain how the scheduler filters and scores nodes.

### Mock Set 3 — Production & Troubleshooting

1. Pod stuck in CrashLoopBackOff — give a 6-step playbook.
2. Pod Pending with insufficient cpu — three resolutions.
3. Slow `kubectl` calls — diagnose.
4. etcd alarm `NOSPACE` — fix.
5. Implement zero-downtime DB migration on K8s.
6. Cluster upgrade from 1.30 to 1.31 — steps.
7. Cluster disaster recovery — components to back up and tools.
8. Multi-tenancy approach — soft vs hard, when each.
9. Image signing and verification end-to-end.
10. Reduce cross-AZ traffic costs.
11. Adopt a service mesh — first 30 days plan.
12. Implement canary with Argo Rollouts.
13. Detect a runtime compromise.
14. Build a CI/CD pipeline that auto-deploys via GitOps.
15. Container OOMKilled — root cause and remediation.

---

## K. Cheat Sheet

### Context & Namespaces

```bash
kubectl config get-contexts
kubectl config use-context <ctx>
kubectl config set-context --current --namespace=apps

# Aliases (Krew)
kubectl krew install ctx ns
kubectx prod && kubens apps
```

### Get / Describe / Edit

```bash
kubectl get pods -A -o wide
kubectl get all -n apps
kubectl describe pod <pod> -n apps
kubectl edit deploy/web -n apps
kubectl get events -A --sort-by=.lastTimestamp
```

### Logs / Exec / Port-Forward

```bash
kubectl logs deploy/web -c app --since=1h --tail=200 -f
kubectl logs -l app=web --max-log-requests=10
kubectl exec -it pod/<pod> -c app -- sh
kubectl port-forward svc/web 8080:80
kubectl cp pod/<pod>:/etc/hosts ./hosts.txt
```

### Imperative Quick Drills (CKAD speed)

```bash
kubectl run debug --image=alpine -it --rm --restart=Never -- sh
kubectl create deploy web --image=nginx:1.27 --replicas=3 --port=80
kubectl expose deploy web --port=80 --target-port=80 --type=ClusterIP
kubectl create configmap app-config --from-literal=LOG=info
kubectl create secret generic db --from-literal=password='<P>'
kubectl create serviceaccount deployer
kubectl create role deploy --verb=get,list,watch,patch --resource=deployments
kubectl create rolebinding deploy --role=deploy --serviceaccount=apps:deployer

kubectl create job hello --image=busybox -- echo hello
kubectl create cronjob nightly --image=busybox --schedule="0 2 * * *" -- echo hi

# Generate YAML
kubectl create deploy web --image=nginx -o yaml --dry-run=client > deploy.yaml
```

### Scale / Rollout

```bash
kubectl scale deploy/web --replicas=5
kubectl rollout status deploy/web
kubectl rollout history deploy/web
kubectl rollout undo deploy/web --to-revision=3
kubectl set image deploy/web app=myrepo/app:1.2.0
```

### Labels & Selectors

```bash
kubectl label pod/<p> tier=backend
kubectl get pods -l 'env in (dev,stage),app=web'
kubectl get pods --field-selector=status.phase=Running
```

### Node Management

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --grace-period=120
kubectl uncordon <node>
kubectl top nodes
kubectl describe node <node>
```

### Debugging

```bash
kubectl debug node/<n> -it --image=ubuntu
kubectl debug -it <pod> --image=nicolaka/netshoot --target=app
kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded
kubectl get events --field-selector type=Warning -A
```

### Helm

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search repo nginx
helm install web bitnami/nginx -n web --create-namespace
helm upgrade --install web bitnami/nginx -n web -f values.yaml
helm rollback web 1 -n web
helm uninstall web -n web
helm template ./mychart -f values-prod.yaml
helm lint ./mychart
```

### YAML Anchors & Snippets

```yaml
# Probes
livenessProbe:  { httpGet: { path: /healthz, port: 8080 }, periodSeconds: 10 }
readinessProbe: { httpGet: { path: /ready,   port: 8080 }, periodSeconds: 5  }

# Resources
resources:
  requests: { cpu: 100m, memory: 128Mi }
  limits:   { cpu: 500m, memory: 256Mi }

# Security
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  capabilities: { drop: [ALL] }
  readOnlyRootFilesystem: true
  seccompProfile: { type: RuntimeDefault }
```

### Pod Lifecycle Hooks

```yaml
lifecycle:
  preStop:
    exec: { command: ["sh","-c","sleep 15"] }   # Drain time
```

### JSONPath / Custom Columns

```bash
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.phase}{"\n"}{end}'
kubectl get pods -o custom-columns=NAME:.metadata.name,IP:.status.podIP,NODE:.spec.nodeName
```

### Common One-Liners

```bash
# Restart all pods in a deployment
kubectl rollout restart deploy/web -n apps

# Get pod count per node
kubectl get pods -A -o wide | awk '{print $8}' | sort | uniq -c

# Find pods using a specific image
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{": "}{.spec.containers[*].image}{"\n"}{end}' | grep nginx
```

---

## L. Curated Resources

### Official

- Kubernetes docs — https://kubernetes.io/docs/
- KEPs (enhancement proposals) — https://github.com/kubernetes/enhancements
- Components ref — https://kubernetes.io/docs/concepts/overview/components/
- API ref — https://kubernetes.io/docs/reference/kubernetes-api/

### Certifications

- CKA / CKAD / CKS curricula — https://www.cncf.io/training/certification/
- KillerCoda labs — https://killercoda.com/cks
- KodeKloud labs — https://kodekloud.com

### Books

- *Kubernetes Up & Running* — Brendan Burns, Kelsey Hightower, Joe Beda
- *Kubernetes in Action, 2e* — Marko Lukša
- *Programming Kubernetes* — Michael Hausenblas
- *Production Kubernetes* — Josh Rosso, Rich Lander, Alexander Brand, John Harris
- *Kubernetes Patterns, 2e* — Bilgin Ibryam, Roland Huss

### Videos

- TGI Kubernetes (Joe Beda)
- TechWorld with Nana
- Learnk8s
- KubeCon talks (CNCF YouTube)

### Repos

- https://github.com/kubernetes/community
- https://github.com/dgkanatsios/CKAD-exercises
- https://github.com/walidshaari/Kubernetes-Certified-Administrator
- https://github.com/kelseyhightower/kubernetes-the-hard-way

### Tools

- `k9s`, `stern`, `kubectx`, `kubens`, `krew`, `kubeconform`, `kubeval`
- `kind`, `minikube`, `k3d`, `kubeadm`
- `argo-cd`, `flux`, `kustomize`, `helm`
- `velero`, `cert-manager`, `external-secrets-operator`, `keda`, `kyverno`, `falco`

---

End of Kubernetes interview guide. Pair this with daily kubectl reps and at least one CKA mock exam before any onsite.
