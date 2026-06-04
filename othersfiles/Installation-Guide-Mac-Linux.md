# Installation Guide — Docker, Kubernetes, Ansible, Terraform

Cross-platform installation, configuration, verification, and local-lab setup for all four tools on:

- **macOS** — Intel and Apple Silicon (M1/M2/M3/M4)
- **Linux** — Ubuntu/Debian, RHEL/Fedora/Rocky/AlmaLinux, Arch

Each section ends with verification commands, a minimum-viable local lab, and uninstall/upgrade procedures.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Docker](#docker)
3. [Kubernetes (Local Clusters)](#kubernetes-local-clusters)
4. [Ansible](#ansible)
5. [Terraform](#terraform)
6. [Combined Practice Lab](#combined-practice-lab)
7. [Common Gotchas](#common-gotchas)
8. [Maintenance & Upgrades](#maintenance--upgrades)

---

## Prerequisites

### macOS

```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install Homebrew (skip if already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Verify
brew --version
```

For Apple Silicon, ensure Homebrew is installed at `/opt/homebrew` (default). Confirm with `brew --prefix`.

### Linux — Common Utilities

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install -y curl wget gnupg lsb-release ca-certificates software-properties-common apt-transport-https unzip jq

# RHEL / Fedora / Rocky / AlmaLinux
sudo dnf install -y curl wget gnupg2 ca-certificates unzip jq dnf-plugins-core

# Arch
sudo pacman -Syu --noconfirm curl wget gnupg ca-certificates unzip jq
```

### Recommended Versions (as of 2026)

| Tool | Stable | Notes |
|------|--------|-------|
| Docker Engine | 27.x | OCI-compliant, BuildKit default |
| Kubernetes | 1.31 / 1.32 | One minor version behind upstream is safe |
| Ansible-core | 2.18 | Python 3.11+ required |
| Terraform | 1.10 | Last MPL version line; 1.6+ defaults BSL — verify license fit |
| OpenTofu | 1.8 | Open-source Terraform fork (interchangeable) |

---

## Docker

### macOS (Option 1 — Docker Desktop, GUI + CLI)

```bash
brew install --cask docker
open /Applications/Docker.app
```

Wait for Docker Desktop to start; whale icon turns steady in the menu bar.

### macOS (Option 2 — Colima, lightweight FOSS alternative)

```bash
brew install colima docker docker-compose
colima start --cpu 4 --memory 8 --disk 60
docker context use colima
```

Why Colima: no Docker Desktop license, runs Lima VM with QEMU/HVF, supports `arm64` and `amd64` via emulation. Recommended for license-sensitive enterprises.

### macOS (Option 3 — Rancher Desktop)

```bash
brew install --cask rancher
open /Applications/Rancher\ Desktop.app
```

Bundles `containerd`, `nerdctl`, and K8s (k3s). Choose Docker Engine mode for parity with Docker CLI.

### Ubuntu / Debian

```bash
# Remove old versions
sudo apt remove -y docker docker-engine docker.io containerd runc

# Set up the official repo
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Run docker without sudo (log out and back in afterward)
sudo usermod -aG docker $USER

# Enable on boot
sudo systemctl enable --now docker
```

### RHEL / Fedora / Rocky / AlmaLinux

```bash
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

### Arch

```bash
sudo pacman -S --noconfirm docker docker-compose docker-buildx
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

### Verify Docker

```bash
docker version
docker run --rm hello-world
docker buildx version
docker compose version
```

### Rootless Docker (Linux, security best practice)

```bash
sudo apt install -y uidmap dbus-user-session
dockerd-rootless-setuptool.sh install
export PATH=/usr/bin:$PATH
export DOCKER_HOST=unix:///run/user/$(id -u)/docker.sock
systemctl --user enable --now docker
```

### Uninstall Docker

```bash
# macOS Docker Desktop
brew uninstall --cask docker
rm -rf ~/Library/Containers/com.docker.docker ~/Library/Application\ Support/Docker\ Desktop

# Colima
colima stop && colima delete
brew uninstall colima docker

# Ubuntu/Debian
sudo apt purge -y docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker /etc/docker

# Fedora/RHEL
sudo dnf remove -y docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker /etc/docker
```

---

## Kubernetes (Local Clusters)

You'll need both a **cluster runtime** (kind / minikube / k3d / Docker Desktop) and the **kubectl** client. Pick *one* runtime.

### kubectl — All Platforms

```bash
# macOS
brew install kubectl

# Ubuntu/Debian
curl -fsSL -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg \
  https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /" | \
  sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update && sudo apt install -y kubectl

# Fedora/RHEL
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.31/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.31/rpm/repodata/repomd.xml.key
EOF
sudo dnf install -y kubectl

# Arch
sudo pacman -S --noconfirm kubectl
```

### Shell Completion (zsh + bash)

```bash
# bash
echo 'source <(kubectl completion bash)' >> ~/.bashrc
echo 'alias k=kubectl; complete -F __start_kubectl k' >> ~/.bashrc

# zsh
echo 'source <(kubectl completion zsh)' >> ~/.zshrc
echo 'alias k=kubectl' >> ~/.zshrc
```

### Runtime Option 1 — kind (Kubernetes IN Docker) — Recommended for CKAD prep

```bash
# macOS
brew install kind

# Linux
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-arm64
chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind

# Multi-node cluster
cat <<EOF > kind-cluster.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
EOF

kind create cluster --name lab --config kind-cluster.yaml
kubectl get nodes
```

### Runtime Option 2 — minikube

```bash
# macOS
brew install minikube

# Linux (amd64)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start --cpus=4 --memory=8g --driver=docker
minikube addons enable ingress
minikube addons enable metrics-server
kubectl get nodes
```

### Runtime Option 3 — k3d (k3s in Docker, fast)

```bash
brew install k3d   # macOS
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash   # Linux

k3d cluster create lab --agents 2 -p "8080:80@loadbalancer"
kubectl get nodes
```

### Runtime Option 4 — Docker Desktop Kubernetes

Enable in Docker Desktop -> Settings -> Kubernetes -> Enable Kubernetes -> Apply & Restart. Simple but tied to Docker Desktop licensing.

### Helm

```bash
# macOS
brew install helm

# Linux universal installer
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

helm version
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### Useful Companion Tools

```bash
brew install k9s stern kubectx kustomize krew
kubectl krew install ctx ns neat tree
```

### Verify Kubernetes

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl get all
```

### Uninstall

```bash
kind delete cluster --name lab
minikube delete --all --purge
k3d cluster delete lab

brew uninstall kubectl kind minikube k3d helm   # macOS
sudo apt remove kubectl                          # Debian/Ubuntu
sudo dnf remove kubectl                          # RHEL/Fedora
```

---

## Ansible

### macOS

```bash
brew install ansible
# Optional collections
ansible-galaxy collection install community.general community.docker kubernetes.core ansible.posix
```

### Ubuntu / Debian

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible
```

### RHEL / Fedora / Rocky

```bash
sudo dnf install -y epel-release
sudo dnf install -y ansible-core
```

### Arch

```bash
sudo pacman -S --noconfirm ansible
```

### Universal — via `pipx` (recommended for latest ansible-core)

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install --include-deps ansible        # full package
pipx install ansible-core                  # minimal
pipx inject ansible-core ansible-lint
```

### Verify Ansible

```bash
ansible --version
ansible localhost -m ping
ansible-config dump --only-changed
```

Sample `ansible.cfg`:

```ini
[defaults]
inventory = ./inventory.ini
host_key_checking = False
retry_files_enabled = False
stdout_callback = yaml
forks = 20
gathering = smart
fact_caching = jsonfile
fact_caching_connection = ~/.ansible/cache
fact_caching_timeout = 7200

[ssh_connection]
pipelining = True
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

Sample `inventory.ini`:

```ini
[web]
web1 ansible_host=192.168.56.11
web2 ansible_host=192.168.56.12

[db]
db1 ansible_host=192.168.56.21

[all:vars]
ansible_user=vagrant
ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key
```

### Local Practice VMs

#### macOS / Linux — Multipass (lightweight Ubuntu VMs)

```bash
# macOS
brew install --cask multipass
# Ubuntu
sudo snap install multipass

multipass launch --name web1 --cpus 1 --memory 1G --disk 5G
multipass launch --name web2 --cpus 1 --memory 1G --disk 5G
multipass list

# Inject your SSH key
multipass exec web1 -- bash -c 'mkdir -p ~/.ssh && echo "<YOUR_PUBLIC_KEY>" >> ~/.ssh/authorized_keys'
```

#### Vagrant (cross-platform)

```bash
brew install --cask vagrant virtualbox   # macOS Intel only
# Apple Silicon: use VMware Fusion or Parallels provider
```

`Vagrantfile`:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  (1..2).each do |i|
    config.vm.define "web#{i}" do |node|
      node.vm.hostname = "web#{i}"
      node.vm.network "private_network", ip: "192.168.56.1#{i}"
    end
  end
end
```

```bash
vagrant up
ansible all -i inventory.ini -m ping
```

### Uninstall

```bash
brew uninstall ansible           # macOS
pipx uninstall ansible           # pipx
sudo apt remove ansible          # Debian/Ubuntu
sudo dnf remove ansible-core     # RHEL/Fedora
```

---

## Terraform

### macOS

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
# OR open-source fork:
brew install opentofu
```

### Ubuntu / Debian

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | \
  sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
  https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install -y terraform
```

### RHEL / Fedora

```bash
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf install -y terraform
```

### Arch

```bash
sudo pacman -S --noconfirm terraform
# or OpenTofu via AUR
yay -S opentofu-bin
```

### Manual (any OS) via `tfenv` (version manager)

```bash
brew install tfenv
tfenv install 1.10.0
tfenv use 1.10.0
tfenv list
```

### Shell Completion

```bash
terraform -install-autocomplete
```

### Verify Terraform

```bash
terraform version
mkdir tf-test && cd tf-test
cat > main.tf <<EOF
terraform {
  required_version = ">= 1.5"
}

output "hello" {
  value = "Terraform is installed."
}
EOF
terraform init
terraform plan
```

### Local Provider Practice — LocalStack (AWS emulator)

```bash
# Install
brew install localstack/tap/localstack-cli   # macOS
pipx install localstack

# Start
localstack start -d
# Health check
curl http://localhost:4566/_localstack/health
```

`main.tf` example targeting LocalStack:

```hcl
terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = "http://localhost:4566"
    ec2 = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "demo" {
  bucket = "demo-bucket-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}
```

`access_key`/`secret_key` set to `"test"` are LocalStack's documented sentinel values, not real credentials.

### Uninstall

```bash
brew uninstall terraform                  # macOS
sudo apt remove terraform                 # Debian/Ubuntu
sudo dnf remove terraform                 # RHEL/Fedora
tfenv uninstall 1.10.0                    # tfenv
```

---

## Combined Practice Lab

A single repo to practice all four tools together:

```bash
mkdir -p ~/devops-lab && cd ~/devops-lab

# 1. Provision a local K8s cluster with Terraform's kind provider
cat > main.tf <<'EOF'
terraform {
  required_providers {
    kind = { source = "tehcyx/kind", version = "~> 0.4" }
    helm = { source = "hashicorp/helm", version = "~> 2.13" }
  }
}

provider "kind" {}

resource "kind_cluster" "lab" {
  name            = "devops-lab"
  wait_for_ready  = true
  kubeconfig_path = pathexpand("~/.kube/config")
}

provider "helm" {
  kubernetes {
    config_path = pathexpand("~/.kube/config")
  }
}

resource "helm_release" "nginx" {
  name             = "nginx"
  repository       = "https://charts.bitnami.com/bitnami"
  chart            = "nginx"
  namespace        = "web"
  create_namespace = true
  depends_on       = [kind_cluster.lab]
}
EOF

terraform init && terraform apply -auto-approve

# 2. Build a custom image with Docker
mkdir app && cd app
cat > Dockerfile <<'EOF'
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir flask gunicorn
COPY app.py .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
EOF

cat > app.py <<'EOF'
from flask import Flask
app = Flask(__name__)
@app.get("/")
def root():
    return "hello from the devops lab"
EOF

docker build -t devops-lab/app:0.1.0 .
kind load docker-image devops-lab/app:0.1.0 --name devops-lab
cd ..

# 3. Deploy with kubectl
kubectl create namespace app
kubectl create deployment app --image=devops-lab/app:0.1.0 -n app
kubectl expose deployment app --port=80 --target-port=8000 -n app

# 4. Configure VMs with Ansible (Multipass)
multipass launch --name target -c 1 -m 1G -d 5G
multipass exec target -- bash -c 'sudo apt update && sudo apt install -y openssh-server'

cat > inventory.ini <<EOF
[targets]
target ansible_host=$(multipass info target | awk '/IPv4/ {print $2}') ansible_user=ubuntu
EOF

ansible all -i inventory.ini -m ping
```

You now have **Terraform** managing **a Kubernetes (kind) cluster**, **Docker** building images, **kubectl** deploying them, and **Ansible** configuring an external VM — all four tools exercised end to end on one laptop.

---

## Common Gotchas

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `docker: permission denied` on Linux | User not in docker group | `sudo usermod -aG docker $USER` and re-login |
| Docker images very slow on Apple Silicon | Running `amd64` image | Force native: `--platform=linux/arm64` or rebuild with `buildx --platform linux/arm64` |
| `kind` cluster cannot pull image | Image not loaded into kind nodes | `kind load docker-image <image> --name <cluster>` |
| `minikube` requires sudo for hyperkit | Driver/permissions misconfig | `minikube delete && minikube start --driver=docker` |
| `kubectl: no configuration has been provided` | KUBECONFIG empty | `export KUBECONFIG=~/.kube/config`, or `kind get kubeconfig --name lab > ~/.kube/config` |
| Ansible `ERROR! the role 'X' was not found` | Roles path missing | `ansible-galaxy install -r requirements.yml -p roles/` |
| Ansible Vault prompts repeatedly | No vault-id file | `--vault-password-file ~/.vault_pass` (mode `0600`) |
| Terraform `Error: error configuring Terraform AWS Provider` | Env vars missing | `export AWS_PROFILE=<profile>` or `aws configure sso` |
| Terraform `state locked` | Crashed previous run | `terraform force-unlock <LOCK_ID>` (only if you're sure) |
| SELinux blocks bind-mounts in Docker | Volume mount fails on RHEL | Append `:Z` to the mount: `-v $(pwd):/app:Z` |
| `cgroup v2` errors in kind/minikube | Older runtime | Update Docker to 25+, switch to systemd cgroup driver |

---

## Maintenance & Upgrades

```bash
# Homebrew (macOS): upgrade everything weekly
brew update && brew upgrade

# Ubuntu/Debian
sudo apt update && sudo apt upgrade -y

# Fedora/RHEL
sudo dnf upgrade -y

# Arch
sudo pacman -Syu --noconfirm

# Terraform via tfenv
tfenv install latest && tfenv use latest

# Kubernetes (kind / minikube image upgrade)
kind create cluster --image kindest/node:v1.32.0
minikube start --kubernetes-version=v1.32.0

# Ansible-core via pipx
pipx upgrade ansible-core

# Docker images cleanup (run monthly)
docker system prune -af --volumes
```

### Backup Before Major Upgrades

```bash
# Kubeconfig
cp ~/.kube/config ~/.kube/config.bak.$(date +%F)

# Terraform state (if local — push to S3/GCS in production)
cp terraform.tfstate terraform.tfstate.backup.$(date +%F)

# Ansible Vault password file
gpg -c ~/.vault_pass    # encrypt with passphrase, store offline
```

---

You're ready to practice. Open any of the four `*-Interview-Questions.md` files and start the corresponding lab section.
