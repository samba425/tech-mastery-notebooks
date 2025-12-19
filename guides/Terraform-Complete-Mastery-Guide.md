# 🚀 Terraform Complete Mastery Guide
**The Ultimate Zero to Hero Course - Everything You Need to Know**

> **Complete standalone guide covering every Terraform concept, feature, and best practice**  
> *From absolute beginner to production-ready expert*

---

## 📚 Table of Contents

### **PART 1: FOUNDATIONS** 
- [Day 1: What is Terraform?](#day-1-what-is-terraform)
- [Day 1: Installation & Setup](#day-1-installation--setup)
- [Day 2: First Project](#day-2-your-first-project)
- [Day 2: Terraform Workflow](#day-2-terraform-workflow)
- [Day 3: HCL Language Basics](#day-3-hcl-language-basics)

### **PART 2: CORE CONCEPTS**
- [Day 4: Providers Deep Dive](#day-4-providers-deep-dive)
- [Day 4: Resources](#day-4-resources)
- [Day 5: Variables](#day-5-variables)
- [Day 5: Outputs](#day-5-outputs)
- [Day 6: Data Sources](#day-6-data-sources)
- [Day 7: State Management](#day-7-state-management)

### **PART 3: ADVANCED FEATURES**
- [Day 8: Count & For Each](#day-8-count--for-each)
- [Day 9: Dynamic Blocks](#day-9-dynamic-blocks)
- [Day 10: Functions](#day-10-terraform-functions)
- [Day 11: Expressions & Conditionals](#day-11-expressions--conditionals)
- [Day 12: Modules](#day-12-modules)
- [Day 13: Workspaces](#day-13-workspaces)

### **PART 4: PRODUCTION READY**
- [Day 14: Remote State](#day-14-remote-state)
- [Day 15: State Locking](#day-15-state-locking)
- [Day 16: Import & Migration](#day-16-import--migration)
- [Day 17: Provisioners](#day-17-provisioners)
- [Day 18: Lifecycle Rules](#day-18-lifecycle-rules)

### **PART 5: BEST PRACTICES**
- [Day 19: Project Structure](#day-19-project-structure)
- [Day 20: Security Best Practices](#day-20-security)
- [Day 21: Testing Strategies](#day-21-testing)
- [Day 22: CI/CD Integration](#day-22-cicd-integration)

### **PART 6: REAL-WORLD PROJECTS**
- [Project 1: Simple Web Server](#project-1-simple-web-server)
- [Project 2: VPC & Networking](#project-2-vpc--networking)
- [Project 3: Multi-Tier App](#project-3-multi-tier-application)
- [Project 4: EKS Cluster](#project-4-eks-kubernetes-cluster)
- [Project 5: Multi-Cloud](#project-5-multi-cloud-deployment)

### **PART 7: MASTERY**
- [Advanced Patterns](#advanced-patterns)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Performance Optimization](#performance-optimization)
- [Certification Prep](#certification-preparation)

---

# PART 1: FOUNDATIONS

## Day 1: What is Terraform?

### 🎯 Learning Objectives
By the end of this section, you will understand:
- What Terraform is and why it exists
- The problem it solves
- When to use Terraform vs other tools
- How Terraform works under the hood

---

### 🤔 The Problem: Manual Infrastructure Management

**Before Terraform - The Painful Way:**

```plaintext
SCENARIO: Your startup needs 5 web servers

Monday:
👨‍💻 You: Login to AWS Console
      Click EC2 → Launch Instance
      Select AMI, instance type, security group...
      Click through 20+ settings
      Wait 5 minutes
      Repeat 4 more times... 😫
      
Tuesday:
👔 Boss: "We need staging environment too"
👨‍💻 You: *Internal screaming* 😱
      Do everything again...
      
Wednesday:
👔 Boss: "Production needs 10 servers now"
👨‍💻 You: *Updates resume on LinkedIn* 💀

Friday:
👨‍💻 Junior Dev: "How did you configure server 3?"
👨‍💻 You: "Uhh... I don't remember..."
      *Documentation nowhere to be found*

Result: 
❌ Time wasted: 10+ hours
❌ Inconsistencies between environments
❌ No documentation
❌ Can't track who changed what
❌ Can't reproduce setup
❌ Manual errors everywhere
```

**With Terraform - The Smart Way:**

```hcl
# File: main.tf (5 minutes to write)
resource "aws_instance" "web" {
  count         = var.server_count  # Change this one number!
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer-${count.index + 1}"
  }
}

# Terminal (30 seconds to run)
$ terraform apply
Creating 5 servers... ✅ Done in 2 minutes!

# Need 10 servers? Change one line:
server_count = 10

$ terraform apply
Adding 5 more servers... ✅ Done in 2 minutes!

# Need staging? Copy folder, run again:
$ terraform apply
Staging environment created! ✅ Identical to production!

Result:
✅ Time saved: 9+ hours
✅ Consistent environments
✅ Code IS the documentation
✅ Version controlled (Git)
✅ Reproducible always
✅ Zero manual errors
```

---

### 📖 What is Infrastructure as Code (IaC)?

**Simple Analogy: Cooking**

```plaintext
Traditional Infrastructure:
🍳 Like cooking without a recipe
   - Every time is different
   - Can't share with others
   - Forget ingredients
   - Inconsistent results

Infrastructure as Code:
📜 Like having a detailed recipe
   - Same result every time
   - Share recipe with team
   - All ingredients listed
   - Consistent, perfect results
```

**Technical Definition:**

Infrastructure as Code means managing and provisioning infrastructure through **machine-readable code** rather than manual processes or interactive configuration tools.

---

### 🏗️ What is Terraform?

**One-Line Summary:**  
Terraform is a tool that lets you write code to create, change, and version your infrastructure safely and efficiently.

**Detailed Explanation:**

Terraform is:
1. **Declarative** - You declare what you want, not how to get it
2. **Cloud-Agnostic** - Works with AWS, Azure, GCP, and 1000+ providers
3. **Open Source** - Free to use, large community
4. **State-Based** - Tracks what it created
5. **Immutable** - Replace instead of modify

**Think of Terraform as:**
- 🏗️ **Architect** - Designs the infrastructure
- 📝 **Builder** - Creates the infrastructure  
- 🔍 **Inspector** - Tracks what exists
- 🔧 **Maintainer** - Updates infrastructure
- 💥 **Demolition** - Destroys infrastructure

---

### 🆚 Terraform vs Other Tools

#### **1. Terraform vs CloudFormation**

| Feature | Terraform | CloudFormation |
|---------|-----------|----------------|
| **Cloud Support** | Multi-cloud ✅ | AWS only ❌ |
| **Language** | HCL (easy) ✅ | JSON/YAML (verbose) ❌ |
| **State** | Explicit ✅ | AWS managed ✅ |
| **Community** | Huge ✅ | AWS only ❌ |
| **Cost** | Free ✅ | Free ✅ |

**When to use CloudFormation:**
- ✅ AWS-only shop
- ✅ Need AWS-specific features
- ✅ Don't want to manage state

**When to use Terraform:**
- ✅ Multi-cloud environment
- ✅ Need flexibility
- ✅ Want industry standard
- ✅ Better language (HCL)

#### **2. Terraform vs Ansible**

| Purpose | Terraform | Ansible |
|---------|-----------|---------|
| **Primary Use** | Create infrastructure | Configure infrastructure |
| **Type** | Provisioning tool | Configuration management |
| **Example** | Create 10 servers | Install nginx on servers |
| **Approach** | Declarative | Procedural/Declarative |
| **State** | Yes ✅ | No ❌ |

**The Perfect Combo:**
```
Terraform → Creates the servers
    ↓
Ansible → Installs software on servers
```

**Real Example:**
```hcl
# Terraform creates server
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
}
```

```yaml
# Ansible configures server
- name: Install nginx
  apt:
    name: nginx
    state: present
```

#### **3. Terraform vs Pulumi**

| Feature | Terraform | Pulumi |
|---------|-----------|--------|
| **Language** | HCL | Python, TypeScript, Go |
| **Learning Curve** | Easy | Harder (need programming) |
| **Maturity** | Very mature ✅ | Newer |
| **Community** | Huge ✅ | Growing |

**Choose Terraform if:**
- ✅ You're new to IaC
- ✅ Want simplicity
- ✅ Need mature ecosystem

**Choose Pulumi if:**
- ✅ Already know programming
- ✅ Want to use Python/TypeScript
- ✅ Need complex logic

---

### 🔧 How Terraform Works

#### **The Terraform Workflow:**

```plaintext
┌─────────────────────────────────────────────────────────────┐
│                    TERRAFORM WORKFLOW                        │
└─────────────────────────────────────────────────────────────┘

1. WRITE CODE              2. INITIALIZE           3. PLAN
   📝 main.tf          →      ⚙️ terraform init  →    🔍 terraform plan
   "I want a server"         "Download AWS plugin"    "Here's what I'll do"
                                                      "+1 server to create"
           ↓                         ↓                        ↓
           
4. APPLY                   5. STATE SAVED          6. MANAGE
   🚀 terraform apply  →      💾 terraform.tfstate →  🔧 Update/Destroy
   "Creating server..."       "Server ID: i-123"      "Modify as needed"
```

#### **Under the Hood:**

```plaintext
┌──────────────┐
│  Your Code   │  main.tf
│   (HCL)      │  "create an EC2 instance"
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  Terraform   │  Reads your code
│    Core      │  Understands what you want
└──────┬───────┘
       │
       ↓
┌──────────────┐
│   Provider   │  AWS Provider Plugin
│   (Plugin)   │  Knows how to talk to AWS
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  AWS API     │  Actually creates server
│              │  Returns server ID
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  State File  │  terraform.tfstate
│              │  "Server i-123 exists"
└──────────────┘
```

---

### 🎯 When to Use Terraform

#### ✅ **Perfect Use Cases:**

1. **Multi-Cloud Infrastructure**
   ```hcl
   # Same workflow for AWS, Azure, GCP
   resource "aws_instance" "web" { }
   resource "azurerm_virtual_machine" "app" { }
   resource "google_compute_instance" "db" { }
   ```

2. **Consistent Environments**
   ```bash
   # Same code creates dev, staging, prod
   terraform workspace select dev && terraform apply
   terraform workspace select prod && terraform apply
   ```

3. **Version-Controlled Infrastructure**
   ```bash
   git log infrastructure/
   # See who changed what, when, why
   ```

4. **Automated Deployments**
   ```yaml
   # CI/CD pipeline
   - terraform plan
   - terraform apply -auto-approve
   ```

5. **Complex Dependencies**
   ```hcl
   # Terraform handles order automatically
   resource "aws_vpc" "main" { }
   resource "aws_subnet" "public" {
     vpc_id = aws_vpc.main.id  # Terraform creates VPC first
   }
   ```

#### ❌ **Not Great For:**

1. **Configuration Management**
   - Use Ansible, Chef, Puppet instead
   - Terraform creates, doesn't configure

2. **Application Deployment**
   - Use Docker, Kubernetes instead
   - Terraform can create K8s cluster, not deploy apps

3. **Adhoc Changes**
   - Terraform is for infrastructure, not scripts
   - Use shell scripts for one-off tasks

---

### 📊 Terraform Architecture

```plaintext
┌─────────────────────────────────────────────────────────────┐
│                    TERRAFORM ARCHITECTURE                    │
└─────────────────────────────────────────────────────────────┘

                    ┌──────────────┐
                    │  Terraform   │
                    │     CLI      │
                    └──────┬───────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ↓              ↓              ↓
    ┌───────────┐  ┌───────────┐  ┌───────────┐
    │   Core    │  │   State   │  │  Config   │
    │  Engine   │  │  Manager  │  │  Parser   │
    └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
          │              │              │
          └──────────────┼──────────────┘
                         │
                    ┌────┴────┐
                    │ Provider│
                    │Interface│
                    └────┬────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ↓                ↓                ↓
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │   AWS    │    │  Azure   │    │   GCP    │
  │ Provider │    │ Provider │    │ Provider │
  └────┬─────┘    └────┬─────┘    └────┬─────┘
       │               │               │
       ↓               ↓               ↓
  ┌──────────┐    ┌──────────┐    ┌──────────┐
  │   AWS    │    │  Azure   │    │  Google  │
  │   API    │    │   API    │    │   API    │
  └──────────┘    └──────────┘    └──────────┘
```

---

### 🎓 Key Terminology

#### **1. Provider**
```plaintext
What: Plugin that talks to a service (AWS, Azure, etc.)
Think: Like a language translator
Example: AWS provider translates Terraform → AWS API
```

#### **2. Resource**
```plaintext
What: Something you want to create (server, database, etc.)
Think: Building blocks of your infrastructure
Example: aws_instance, aws_s3_bucket
```

#### **3. State**
```plaintext
What: Terraform's memory of what it created
Think: Like a spreadsheet tracking everything
Example: terraform.tfstate file
```

#### **4. Module**
```plaintext
What: Reusable group of resources
Think: Like a function in programming
Example: VPC module used by multiple projects
```

#### **5. Plan**
```plaintext
What: Preview of changes before applying
Think: Like "print preview" before printing
Example: terraform plan output
```

#### **6. Apply**
```plaintext
What: Actually create/update infrastructure
Think: Like clicking "Submit" button
Example: terraform apply command
```

---

### 🏆 Why Terraform is Popular

#### **Statistics:**
- 📈 **40,000+** GitHub stars
- 👥 **10M+** downloads per week
- 🏢 **Fortune 500** companies use it
- 💼 **Top 10** most wanted DevOps skill

#### **Industry Adoption:**

```plaintext
Companies Using Terraform:
✅ Uber          ✅ Slack         ✅ Twitch
✅ Airbnb        ✅ GitHub        ✅ Shopify
✅ Netflix       ✅ Pinterest     ✅ Square
✅ Lyft          ✅ Stripe        ✅ Datadog
```

#### **Job Market:**

```plaintext
Average Salaries (USA, 2025):
💰 DevOps Engineer with Terraform: $120K - $180K
💰 Cloud Engineer with Terraform:  $130K - $190K
💰 SRE with Terraform:             $140K - $200K
💰 Infrastructure Engineer:        $115K - $175K
```

---

### ✅ Summary: Day 1 Checklist

By now you should understand:

- [x] What problem Terraform solves
- [x] How Terraform differs from other tools
- [x] When to use (and not use) Terraform
- [x] Basic Terraform architecture
- [x] Key terminology
- [x] Why Terraform is valuable to learn

**Next:** Let's install Terraform and set up your environment!

---

## Day 1: Installation & Setup

### 🎯 Learning Objectives
- Install Terraform on your OS
- Set up development environment
- Configure cloud provider credentials
- Verify everything works

---

### 💻 Installation by Operating System

#### **macOS Installation** 🍎

**Method 1: Homebrew (Recommended)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add HashiCorp tap
brew tap hashicorp/tap

# Install Terraform
brew install hashicorp/tap/terraform

# Verify installation
terraform --version
# Output: Terraform v1.7.0
```

**Method 2: Manual Download**
```bash
# Download latest version
curl -O https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_darwin_amd64.zip

# Unzip
unzip terraform_1.7.0_darwin_amd64.zip

# Move to PATH
sudo mv terraform /usr/local/bin/

# Verify
terraform --version
```

#### **Linux Installation** 🐧

**Ubuntu/Debian:**
```bash
# Update package manager
sudo apt-get update

# Install dependencies
sudo apt-get install -y gnupg software-properties-common

# Add HashiCorp GPG key
wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Add HashiCorp repository
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list

# Update and install
sudo apt-get update
sudo apt-get install terraform

# Verify
terraform --version
```

**RHEL/CentOS/Fedora:**
```bash
# Add HashiCorp repository
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo \
    https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo

# Install Terraform
sudo yum install terraform

# Verify
terraform --version
```

**Arch Linux:**
```bash
# Install from official repository
sudo pacman -S terraform

# Verify
terraform --version
```

#### **Windows Installation** 🪟

**Method 1: Chocolatey (Recommended)**
```powershell
# Install Chocolatey (if not installed)
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Terraform
choco install terraform

# Verify
terraform --version
```

**Method 2: Manual Installation**
```powershell
# 1. Download from: https://www.terraform.io/downloads
# 2. Unzip the file
# 3. Add to PATH:
#    - Right-click "This PC" → Properties
#    - Advanced system settings → Environment Variables
#    - Add terraform.exe location to PATH
# 4. Open new terminal and verify
terraform --version
```

---

### 🔧 Development Environment Setup

#### **Step 1: Install VS Code**

```bash
# macOS
brew install --cask visual-studio-code

# Ubuntu
sudo snap install code --classic

# Windows
choco install vscode

# Or download from: https://code.visualstudio.com/
```

#### **Step 2: Install Terraform Extension**

1. Open VS Code
2. Press `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux)
3. Search: "HashiCorp Terraform"
4. Click "Install"

**What you get:**
- ✅ Syntax highlighting
- ✅ Auto-completion
- ✅ IntelliSense
- ✅ Error detection
- ✅ Format on save
- ✅ Code snippets

#### **Step 3: Configure VS Code for Terraform**

Create `.vscode/settings.json` in your workspace:

```json
{
  "terraform.experimentalFeatures": {
    "validateOnSave": true,
    "prefillRequiredFields": true
  },
  "terraform.languageServer": {
    "external": true,
    "args": ["serve"]
  },
  "[terraform]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "hashicorp.terraform"
  },
  "files.associations": {
    "*.tf": "terraform",
    "*.tfvars": "terraform"
  }
}
```

#### **Step 4: Install Terraform-Docs (Optional but Recommended)**

```bash
# macOS
brew install terraform-docs

# Linux
curl -sSLo ./terraform-docs.tar.gz \
    https://terraform-docs.io/dl/v0.17.0/terraform-docs-v0.17.0-$(uname)-amd64.tar.gz
tar -xzf terraform-docs.tar.gz
chmod +x terraform-docs
sudo mv terraform-docs /usr/local/bin/

# Windows
choco install terraform-docs
```

#### **Step 5: Install TFLint (Terraform Linter)**

```bash
# macOS
brew install tflint

# Linux
curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash

# Windows
choco install tflint
```

---

### ☁️ Cloud Provider Setup

#### **AWS Setup**

**Step 1: Create AWS Account**
1. Go to https://aws.amazon.com/
2. Click "Create an AWS Account"
3. Complete registration
4. Add credit card (required, but won't be charged with free tier)

**Step 2: Create IAM User**

```bash
# Login to AWS Console → IAM → Users → Add User

Name: terraform-user
Access type: ☑️ Programmatic access

# Attach policies:
☑️ AdministratorAccess (for learning)
# For production, use least privilege!

# Download credentials CSV file
```

**Step 3: Install AWS CLI**

```bash
# macOS
brew install awscli

# Linux
sudo apt-get install awscli  # Ubuntu
sudo yum install awscli      # RHEL/CentOS

# Windows
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

# Verify
aws --version
```

**Step 4: Configure AWS CLI**

```bash
aws configure

# Enter your credentials:
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: json

# Test connection
aws sts get-caller-identity
```

**Step 5: Set Environment Variables (Alternative)**

```bash
# Add to ~/.bashrc or ~/.zshrc
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"

# Reload shell
source ~/.bashrc
```

#### **Azure Setup**

**Step 1: Create Azure Account**
```bash
# Go to: https://azure.microsoft.com/free/
# Sign up for free tier ($200 credit for 30 days)
```

**Step 2: Install Azure CLI**

```bash
# macOS
brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Windows
msiexec.exe /i https://aka.ms/installazurecliwindows

# Verify
az --version
```

**Step 3: Login to Azure**

```bash
# Login
az login

# This opens browser for authentication
# After login, you'll see your subscriptions

# List subscriptions
az account list --output table

# Set default subscription
az account set --subscription="SUBSCRIPTION_ID"
```

**Step 4: Create Service Principal**

```bash
# Create service principal for Terraform
az ad sp create-for-rbac --name="terraform-sp" --role="Contributor" --scopes="/subscriptions/SUBSCRIPTION_ID"

# Output (SAVE THIS!):
{
  "appId": "00000000-0000-0000-0000-000000000000",
  "displayName": "terraform-sp",
  "password": "0000-0000-0000-0000-000000000000",
  "tenant": "00000000-0000-0000-0000-000000000000"
}

# Set environment variables
export ARM_CLIENT_ID="appId"
export ARM_CLIENT_SECRET="password"
export ARM_SUBSCRIPTION_ID="your-subscription-id"
export ARM_TENANT_ID="tenant"
```

#### **Google Cloud Setup**

**Step 1: Create GCP Account**
```bash
# Go to: https://cloud.google.com/free
# Sign up ($300 credit for 90 days)
```

**Step 2: Install gcloud CLI**

```bash
# macOS
brew install --cask google-cloud-sdk

# Linux
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Windows
# Download from: https://cloud.google.com/sdk/docs/install

# Verify
gcloud --version
```

**Step 3: Initialize gcloud**

```bash
# Initialize
gcloud init

# Login
gcloud auth login

# Set project
gcloud config set project PROJECT_ID

# Create service account for Terraform
gcloud iam service-accounts create terraform \
    --display-name="Terraform Service Account"

# Grant permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:terraform@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/editor"

# Create and download key
gcloud iam service-accounts keys create ~/terraform-key.json \
    --iam-account=terraform@PROJECT_ID.iam.gserviceaccount.com

# Set environment variable
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/terraform-key.json"
```

---

### 🧪 Verify Installation

Create this test file to verify everything works:

**File: `test.tf`**
```hcl
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

resource "local_file" "test" {
  filename = "${path.module}/test.txt"
  content  = "Terraform is working! ✅"
}

output "message" {
  value = "Installation successful!"
}
```

**Run the test:**
```bash
# Initialize
terraform init

# Expected output:
# Initializing provider plugins...
# - Finding hashicorp/local versions matching "~> 2.0"...
# - Installing hashicorp/local v2.4.1...
# Terraform has been successfully initialized!

# Plan
terraform plan

# Expected output:
# Terraform will perform the following actions:
#   # local_file.test will be created
# Plan: 1 to add, 0 to change, 0 to destroy.

# Apply
terraform apply -auto-approve

# Expected output:
# local_file.test: Creating...
# local_file.test: Creation complete
# message = "Installation successful!"

# Verify file was created
cat test.txt
# Output: Terraform is working! ✅

# Clean up
terraform destroy -auto-approve
rm test.tf
```

---

### 📁 Project Directory Structure

Create your learning workspace:

```bash
# Create directory structure
mkdir -p ~/terraform-learning/{day1-basics,day2-resources,day3-variables,projects}

cd ~/terraform-learning

# Create gitignore
cat > .gitignore << 'EOF'
# Terraform files
.terraform/
*.tfstate
*.tfstate.backup
*.tfplan
.terraform.lock.hcl

# Environment variables
*.tfvars
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF

# Initialize git
git init
git add .gitignore
git commit -m "Initial commit"
```

---

### ⚙️ Configure Terraform CLI

**Enable autocomplete:**
```bash
# For bash
terraform -install-autocomplete

# For zsh
echo 'autoload -U +X bashcompinit && bashcompinit' >> ~/.zshrc
echo 'complete -o nospace -C /usr/local/bin/terraform terraform' >> ~/.zshrc
source ~/.zshrc
```

**Set up aliases (optional):**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias tf='terraform'
alias tfi='terraform init'
alias tfp='terraform plan'
alias tfa='terraform apply'
alias tfd='terraform destroy'
alias tfv='terraform validate'
alias tff='terraform fmt -recursive'

# Reload
source ~/.bashrc  # or source ~/.zshrc
```

---

### ✅ Installation Checklist

Verify you have everything:

```bash
# 1. Terraform installed
terraform --version
# ✅ Should show v1.7.0 or higher

# 2. VS Code installed
code --version
# ✅ Should show VS Code version

# 3. AWS CLI configured (if using AWS)
aws sts get-caller-identity
# ✅ Should show your AWS account info

# 4. Git installed
git --version
# ✅ Should show git version

# 5. Terraform extension in VS Code
# ✅ Open VS Code, check Extensions panel

# 6. Test terraform works
cd /tmp
echo 'resource "local_file" "test" { filename = "test.txt"; content = "OK" }' > test.tf
terraform init && terraform apply -auto-approve
# ✅ Should create test.txt

# Clean up
rm -rf test.tf test.txt .terraform* terraform.tfstate*
```

---

### 🎉 Congratulations!

You've successfully:
- ✅ Installed Terraform
- ✅ Set up development environment
- ✅ Configured cloud provider
- ✅ Verified installation
- ✅ Created workspace structure

**Next:** Let's create your first real Terraform project!

---

## Day 2: Your First Project

### 🎯 Learning Objectives
- Create your first real infrastructure
- Understand Terraform workflow
- Learn basic Terraform commands
- Deploy to AWS

---

### 🚀 Project: Deploy Your First S3 Bucket

We'll start with the simplest possible AWS resource - an S3 bucket (cloud storage).

#### **Step 1: Create Project Directory**

```bash
mkdir -p ~/terraform-learning/day2-first-project
cd ~/terraform-learning/day2-first-project
```

#### **Step 2: Write Terraform Configuration**

Create `main.tf`:

```hcl
#============================================================================
# TERRAFORM CONFIGURATION
#============================================================================
# This block tells Terraform which providers we need

terraform {
  # Require Terraform 1.0 or higher
  required_version = ">= 1.0"
  
  # Declare providers we'll use
  required_providers {
    aws = {
      source  = "hashicorp/aws"  # Official AWS provider
      version = "~> 5.0"          # Use version 5.x
    }
  }
}

#============================================================================
# PROVIDER CONFIGURATION  
#============================================================================
# Configure the AWS provider

provider "aws" {
  region = "us-east-1"  # Virginia region (cheapest, most services)
  
  # Credentials are automatically loaded from:
  # - Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
  # - AWS CLI configuration (~/.aws/credentials)
  # - IAM role (if running on EC2)
}

#============================================================================
# RESOURCES
#============================================================================
# Define what we want to create

resource "aws_s3_bucket" "my_first_bucket" {
  # Bucket name must be globally unique across all of AWS
  # Use your name or add random suffix to ensure uniqueness
  bucket = "my-terraform-learning-bucket-2025"
  
  # Tags help organize and identify resources
  tags = {
    Name        = "My First Terraform Bucket"
    Environment = "Learning"
    ManagedBy   = "Terraform"
    CreatedAt   = "2025-12-19"
    Owner       = "YourName"
  }
}

# Enable versioning for the bucket (optional but recommended)
resource "aws_s3_bucket_versioning" "my_bucket_versioning" {
  bucket = aws_s3_bucket.my_first_bucket.id
  
  versioning_configuration {
    status = "Enabled"
  }
}

# Block all public access (security best practice)
resource "aws_s3_bucket_public_access_block" "my_bucket_pab" {
  bucket = aws_s3_bucket.my_first_bucket.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

#============================================================================
# OUTPUTS
#============================================================================
# Display information after Terraform runs

output "bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.my_first_bucket.id
}

output "bucket_arn" {
  description = "The ARN of the S3 bucket"
  value       = aws_s3_bucket.my_first_bucket.arn
}

output "bucket_region" {
  description = "The region where the bucket is created"
  value       = aws_s3_bucket.my_first_bucket.region
}

output "creation_date" {
  description = "The creation date of the bucket"
  value       = aws_s3_bucket.my_first_bucket.tags["CreatedAt"]
}
```

---

#### **Step 3: Understanding the Code**

Let's break down each part:

**1. Terraform Block:**
```hcl
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```
**What it does:**
- Tells Terraform which version to use
- Declares we need the AWS provider
- Specifies AWS provider version

**Why it matters:**
- Prevents version conflicts
- Ensures compatibility
- Makes infrastructure reproducible

---

**2. Provider Block:**
```hcl
provider "aws" {
  region = "us-east-1"
}
```
**What it does:**
- Configures AWS provider
- Sets default region

**How authentication works:**
1. Checks environment variables
2. Checks `~/.aws/credentials`
3. Checks IAM role (if on EC2)

---

**3. Resource Block:**
```hcl
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "my-terraform-learning-bucket-2025"
  tags = { ... }
}
```
**What it does:**
- Creates an S3 bucket
- Names it "my-terraform-learning-bucket-2025"
- Adds metadata tags

**Syntax breakdown:**
- `resource` - Terraform keyword
- `"aws_s3_bucket"` - Resource type (from AWS provider)
- `"my_first_bucket"` - Local name (for referencing in code)
- `bucket = "..."` - Argument (actual bucket name in AWS)

---

**4. Output Block:**
```hcl
output "bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.my_first_bucket.id
}
```
**What it does:**
- Displays values after terraform apply
- Can be used by other Terraform configurations
- Useful for debugging and automation

---

## Day 2: Terraform Workflow

### 🔄 The Complete Workflow

```plaintext
┌─────────────────────────────────────────────────────────────────┐
│                     TERRAFORM WORKFLOW                           │
└─────────────────────────────────────────────────────────────────┘

1. WRITE              2. INIT             3. FMT              4. VALIDATE
   📝 Code        →      ⚙️ Setup      →     🎨 Format    →     ✅ Check
   main.tf            Download plugins     Clean code         Syntax OK?
                                                                    
           ↓                  ↓                  ↓                  ↓
           
5. PLAN              6. APPLY            7. VERIFY           8. DESTROY
   🔍 Preview    →      🚀 Create     →     👀 Check     →     💥 Delete
   See changes         Execute plan        Test it           Clean up
```

Now let's execute each step!

---

### Step 4: Initialize Terraform

```bash
terraform init
```

**What happens:**
```plaintext
Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 5.0"...
- Installing hashicorp/aws v5.31.0...
- Installed hashicorp/aws v5.31.0 (signed by HashiCorp)

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.
```

**What Terraform did:**
1. ✅ Created `.terraform/` directory
2. ✅ Downloaded AWS provider plugin
3. ✅ Created `.terraform.lock.hcl` (locks provider versions)
4. ✅ Initialized backend (state storage)

**Check what was created:**
```bash
ls -la
# .terraform/          # Provider plugins
# .terraform.lock.hcl  # Version lock file
# main.tf              # Your configuration
```

---

### Step 5: Format Code

```bash
terraform fmt
```

**What it does:**
- Formats code to Terraform standards
- Fixes indentation
- Aligns arguments
- Makes code consistent

**Example:**
```hcl
# Before formatting (messy)
resource "aws_s3_bucket" "my_bucket" {
bucket="my-bucket"
  tags={
      Name="MyBucket"
    Environment = "Dev"
  }
}

# After formatting (clean)
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
  
  tags = {
    Name        = "MyBucket"
    Environment = "Dev"
  }
}
```

---

### Step 6: Validate Configuration

```bash
terraform validate
```

**Possible outputs:**

**Success:**
```
Success! The configuration is valid.
```

**Error example:**
```
Error: Missing required argument

  on main.tf line 10:
  10: resource "aws_s3_bucket" "my_bucket" {

The argument "bucket" is required, but no definition was found.
```

---

### Step 7: Plan Changes

```bash
terraform plan
```

**Output:**
```hcl
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.my_first_bucket will be created
  + resource "aws_s3_bucket" "my_first_bucket" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "my-terraform-learning-bucket-2025"
      + bucket_domain_name          = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = (known after apply)
      + request_payer               = (known after apply)
      + tags                        = {
          + "CreatedAt"   = "2025-12-19"
          + "Environment" = "Learning"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "My First Terraform Bucket"
          + "Owner"       = "YourName"
        }
      + tags_all                    = {
          + "CreatedAt"   = "2025-12-19"
          + "Environment" = "Learning"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "My First Terraform Bucket"
          + "Owner"       = "YourName"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + bucket_arn      = (known after apply)
  + bucket_name     = "my-terraform-learning-bucket-2025"
  + bucket_region   = (known after apply)
  + creation_date   = "2025-12-19"
```

**Understanding the symbols:**
- `+` = Create new resource
- `-` = Destroy resource
- `~` = Update in-place
- `-/+` = Destroy and recreate
- `(known after apply)` = Value not known until resource is created

**Save plan (optional):**
```bash
terraform plan -out=tfplan
```

---

### Step 8: Apply Changes

```bash
terraform apply
```

**Interactive mode:**
```
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_s3_bucket.my_first_bucket: Creating...
aws_s3_bucket.my_first_bucket: Creation complete after 2s [id=my-terraform-learning-bucket-2025]
aws_s3_bucket_versioning.my_bucket_versioning: Creating...
aws_s3_bucket_public_access_block.my_bucket_pab: Creating...
aws_s3_bucket_versioning.my_bucket_versioning: Creation complete after 1s
aws_s3_bucket_public_access_block.my_bucket_pab: Creation complete after 1s

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

bucket_arn = "arn:aws:s3:::my-terraform-learning-bucket-2025"
bucket_name = "my-terraform-learning-bucket-2025"
bucket_region = "us-east-1"
creation_date = "2025-12-19"
```

**Auto-approve (skip confirmation):**
```bash
terraform apply -auto-approve
```

---

### Step 9: Verify in AWS

**Method 1: AWS Console**
```
1. Go to https://console.aws.amazon.com/
2. Navigate to S3 service
3. Look for "my-terraform-learning-bucket-2025"
4. Click on it to see details
```

**Method 2: AWS CLI**
```bash
aws s3 ls | grep terraform-learning
# Should show your bucket

aws s3api get-bucket-versioning --bucket my-terraform-learning-bucket-2025
# Should show versioning status
```

---

### Step 10: View Outputs

```bash
# View all outputs
terraform output

# View specific output
terraform output bucket_name

# View as JSON
terraform output -json
```

---

### Step 11: Inspect State

```bash
# Show current state
terraform show

# List resources in state
terraform state list

# Show specific resource
terraform state show aws_s3_bucket.my_first_bucket
```

---

### Step 12: Make Changes

Let's update the bucket by adding a new tag.

**Edit `main.tf`:**
```hcl
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "my-terraform-learning-bucket-2025"
  
  tags = {
    Name        = "My First Terraform Bucket"
    Environment = "Learning"
    ManagedBy   = "Terraform"
    CreatedAt   = "2025-12-19"
    Owner       = "YourName"
    Project     = "Terraform Learning"  # NEW TAG
  }
}
```

**Plan the change:**
```bash
terraform plan
```

**Output:**
```
Terraform will perform the following actions:

  # aws_s3_bucket.my_first_bucket will be updated in-place
  ~ resource "aws_s3_bucket" "my_first_bucket" {
        id                          = "my-terraform-learning-bucket-2025"
      ~ tags                        = {
          + "Project"     = "Terraform Learning"
            # (5 unchanged elements hidden)
        }
      ~ tags_all                    = {
          + "Project"     = "Terraform Learning"
            # (5 unchanged elements hidden)
        }
        # (12 unchanged attributes hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
```

**Apply the change:**
```bash
terraform apply -auto-approve
```

---

### Step 13: Destroy Infrastructure

When you're done learning, clean up to avoid charges:

```bash
terraform destroy
```

**Output:**
```
Terraform will perform the following actions:

  # aws_s3_bucket.my_first_bucket will be destroyed
  - resource "aws_s3_bucket" "my_first_bucket" {
      - arn                         = "arn:aws:s3:::my-terraform-learning-bucket-2025"
      - bucket                      = "my-terraform-learning-bucket-2025"
      - id                          = "my-terraform-learning-bucket-2025"
      - tags                        = {
          - "CreatedAt"   = "2025-12-19"
          - "Environment" = "Learning"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "My First Terraform Bucket"
          - "Owner"       = "YourName"
          - "Project"     = "Terraform Learning"
        }
    }

Plan: 0 to add, 0 to change, 3 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_s3_bucket_versioning.my_bucket_versioning: Destroying...
aws_s3_bucket_public_access_block.my_bucket_pab: Destroying...
aws_s3_bucket_versioning.my_bucket_versioning: Destruction complete after 1s
aws_s3_bucket_public_access_block.my_bucket_pab: Destruction complete after 1s
aws_s3_bucket.my_first_bucket: Destroying...
aws_s3_bucket.my_first_bucket: Destruction complete after 1s

Destroy complete! Resources: 3 destroyed.
```

---

### 🎓 Complete Command Reference

#### **Basic Commands**
```bash
# Initialize working directory
terraform init

# Format code
terraform fmt
terraform fmt -recursive       # Format all files
terraform fmt -check           # Check if files need formatting

# Validate configuration
terraform validate

# Show execution plan
terraform plan
terraform plan -out=tfplan     # Save plan to file

# Apply changes
terraform apply
terraform apply -auto-approve  # Skip confirmation
terraform apply tfplan         # Apply saved plan

# Destroy infrastructure
terraform destroy
terraform destroy -auto-approve
```

#### **State Commands**
```bash
# List resources in state
terraform state list

# Show resource details
terraform state show aws_s3_bucket.my_first_bucket

# Remove resource from state (doesn't delete real resource)
terraform state rm aws_s3_bucket.my_first_bucket

# Move resource in state
terraform state mv aws_s3_bucket.old aws_s3_bucket.new

# Pull remote state
terraform state pull

# Push local state to remote
terraform state push
```

#### **Output Commands**
```bash
# Show all outputs
terraform output

# Show specific output
terraform output bucket_name

# Output as JSON
terraform output -json
```

#### **Workspace Commands**
```bash
# List workspaces
terraform workspace list

# Create workspace
terraform workspace new dev

# Select workspace
terraform workspace select prod

# Delete workspace
terraform workspace delete staging
```

#### **Other Useful Commands**
```bash
# Show current state or saved plan
terraform show
terraform show tfplan

# Generate dependency graph
terraform graph | dot -Tsvg > graph.svg

# Interactive console
terraform console

# Get provider information
terraform providers

# Check Terraform version
terraform version

# Refresh state (sync with real infrastructure)
terraform refresh

# Import existing resource
terraform import aws_s3_bucket.my_bucket bucket-name
```

---

### 🐛 Common Errors and Solutions

#### **Error 1: Bucket name already exists**
```
Error: Error creating S3 bucket: BucketAlreadyExists
```
**Solution:** Change bucket name to something unique
```hcl
bucket = "my-terraform-learning-bucket-yourname-2025"
```

#### **Error 2: No AWS credentials**
```
Error: No valid credential sources found for AWS Provider
```
**Solution:** Configure AWS CLI
```bash
aws configure
```

#### **Error 3: Region not specified**
```
Error: Insufficient information to construct AWS client
```
**Solution:** Add region to provider block or set environment variable
```bash
export AWS_DEFAULT_REGION=us-east-1
```

#### **Error 4: Permission denied**
```
Error: AccessDenied: Access Denied
```
**Solution:** Check IAM permissions for your user

#### **Error 5: State lock**
```
Error: Error acquiring the state lock
```
**Solution:** Wait for other operation to complete or force unlock (careful!)
```bash
terraform force-unlock LOCK_ID
```

---

### ✅ Day 2 Checklist

By now you should be able to:

- [x] Write basic Terraform configuration
- [x] Initialize a Terraform project
- [x] Create AWS resources
- [x] Use terraform plan/apply/destroy
- [x] Understand outputs
- [x] Make changes to infrastructure
- [x] Clean up resources

**Congratulations! 🎉** You've deployed your first infrastructure with Terraform!

**Next:** Let's learn the HCL language in depth...

---

## Day 3: HCL Language Basics

### 🎯 Learning Objectives
- Master HCL (HashiCorp Configuration Language) syntax
- Understand all data types
- Learn string interpolation and expressions
- Use built-in functions

---

### 📖 HCL Syntax Fundamentals

#### **Block Structure**
```hcl
# Basic block syntax
block_type "label_one" "label_two" {
  argument_name = "argument_value"
  
  nested_block {
    nested_argument = "value"
  }
}
```

**Real Example:**
```hcl
resource "aws_instance" "web_server" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags {
    Name = "WebServer"
  }
}
```

**Breakdown:**
- `resource` = Block type (keyword)
- `"aws_instance"` = First label (resource type)
- `"web_server"` = Second label (resource name)
- `ami = "..."` = Argument
- `tags { }` = Nested block

---

### 📝 Comments

```hcl
# This is a single-line comment

// This also works for single-line comments

/*
  This is a
  multi-line comment
  spanning multiple lines
*/

# Use comments to explain WHY, not WHAT
resource "aws_instance" "web" {
  # Using t2.micro for cost optimization in dev environment
  instance_type = "t2.micro"  # Free tier eligible
}
```

---

### 🔤 Data Types

#### **1. Primitive Types**

**String:**
```hcl
variable "instance_name" {
  type    = string
  default = "web-server"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

# Multi-line strings
variable "user_data" {
  type    = string
  default = <<-EOF
    #!/bin/bash
    echo "Hello World"
    apt-get update
  EOF
}

# Heredoc with indentation stripped
variable "script" {
  type = string
  default = <<-EOT
    Line 1
      Line 2 (indented)
    Line 3
  EOT
}
```

**Number:**
```hcl
variable "instance_count" {
  type    = number
  default = 3
}

variable "disk_size" {
  type    = number
  default = 100
}

variable "price" {
  type    = number
  default = 0.50  # Decimals work too
}
```

**Boolean:**
```hcl
variable "enable_monitoring" {
  type    = bool
  default = true
}

variable "is_production" {
  type    = bool
  default = false
}

# Use in conditionals
resource "aws_instance" "web" {
  monitoring = var.enable_monitoring  # true or false
}
```

---

#### **2. Collection Types**

**List (Ordered collection of values):**
```hcl
variable "availability_zones" {
  type = list(string)
  default = [
    "us-east-1a",
    "us-east-1b",
    "us-east-1c"
  ]
}

variable "allowed_ports" {
  type = list(number)
  default = [22, 80, 443, 3306]
}

# Access list elements
locals {
  first_az  = var.availability_zones[0]      # "us-east-1a"
  second_az = var.availability_zones[1]      # "us-east-1b"
  last_port = var.allowed_ports[length(var.allowed_ports) - 1]  # 3306
}

# Loop through list
resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  availability_zone = var.availability_zones[count.index]
  cidr_block        = "10.0.${count.index}.0/24"
}
```

**Map (Key-value pairs):**
```hcl
variable "instance_types" {
  type = map(string)
  default = {
    dev     = "t2.micro"
    staging = "t2.small"
    prod    = "t3.large"
  }
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "Production"
    Team        = "DevOps"
    Project     = "WebApp"
    CostCenter  = "Engineering"
  }
}

# Access map values
resource "aws_instance" "web" {
  instance_type = var.instance_types["prod"]  # "t3.large"
  tags          = var.tags
}

# Loop through map
resource "aws_instance" "servers" {
  for_each      = var.instance_types
  instance_type = each.value  # "t2.micro", "t2.small", etc.
  
  tags = {
    Name = "${each.key}-server"  # "dev-server", "staging-server", etc.
  }
}
```

**Set (Unique collection, no duplicates):**
```hcl
variable "security_group_ids" {
  type = set(string)
  default = [
    "sg-12345",
    "sg-67890",
    "sg-12345"  # Duplicate ignored
  ]
  # Result: ["sg-12345", "sg-67890"]
}

# Sets are useful for ensuring uniqueness
resource "aws_instance" "web" {
  vpc_security_group_ids = var.security_group_ids
}
```

---

#### **3. Structural Types**

**Object (Complex structure with different types):**
```hcl
variable "database_config" {
  type = object({
    engine            = string
    engine_version    = string
    instance_class    = string
    allocated_storage = number
    multi_az          = bool
    backup_retention  = number
  })
  
  default = {
    engine            = "mysql"
    engine_version    = "8.0.33"
    instance_class    = "db.t3.micro"
    allocated_storage = 20
    multi_az          = false
    backup_retention  = 7
  }
}

# Use object properties
resource "aws_db_instance" "main" {
  engine               = var.database_config.engine
  engine_version       = var.database_config.engine_version
  instance_class       = var.database_config.instance_class
  allocated_storage    = var.database_config.allocated_storage
  multi_az             = var.database_config.multi_az
  backup_retention_period = var.database_config.backup_retention
}
```

**Tuple (Fixed-length ordered collection):**
```hcl
variable "server_config" {
  type = tuple([string, number, bool])
  default = ["t2.micro", 20, true]
  # [instance_type, disk_size, enable_monitoring]
}

locals {
  instance_type     = var.server_config[0]  # "t2.micro"
  disk_size         = var.server_config[1]  # 20
  enable_monitoring = var.server_config[2]  # true
}
```

---

### 🔗 String Interpolation

```hcl
variable "project" {
  default = "myapp"
}

variable "environment" {
  default = "prod"
}

variable "region" {
  default = "us-east-1"
}

locals {
  # Basic interpolation
  server_name = "${var.project}-${var.environment}-server"
  # Result: "myapp-prod-server"
  
  # Interpolation with functions
  upper_project = "${upper(var.project)}-${var.environment}"
  # Result: "MYAPP-prod"
  
  # Multi-variable interpolation
  full_name = "${var.project}-${var.environment}-${var.region}"
  # Result: "myapp-prod-us-east-1"
  
  # Embedded expressions
  description = "This is ${var.project} running in ${var.environment}"
  # Result: "This is myapp running in prod"
  
  # Conditional in interpolation
  display_name = "${var.environment == "prod" ? "PRODUCTION" : "DEVELOPMENT"}-${var.project}"
  # Result: "PRODUCTION-myapp"
}

resource "aws_instance" "web" {
  tags = {
    Name = "${var.project}-${var.environment}-web-${count.index + 1}"
    Description = "Server for ${var.project} in ${var.region}"
  }
}
```

**Template Strings:**
```hcl
locals {
  # Heredoc with interpolation
  user_data = <<-EOF
    #!/bin/bash
    echo "Setting up ${var.project}"
    export ENVIRONMENT=${var.environment}
    export REGION=${var.region}
    
    # Install application
    apt-get update
    apt-get install -y ${var.project}-server
  EOF
  
  # JSON template
  config = <<-EOT
    {
      "app_name": "${var.project}",
      "environment": "${var.environment}",
      "region": "${var.region}",
      "debug": ${var.environment != "prod"}
    }
  EOT
}
```

---

### ⚙️ Expressions

#### **Arithmetic Operators:**
```hcl
locals {
  # Basic math
  total         = 5 + 3              # 8
  difference    = 10 - 4             # 6
  product       = 2 * 50             # 100
  quotient      = 100 / 5            # 20
  remainder     = 10 % 3             # 1
  
  # More complex
  disk_size     = var.base_size * var.multiplier
  total_cost    = var.instance_count * var.price_per_instance
  subnet_count  = var.az_count * 2  # 2 subnets per AZ
}
```

#### **Comparison Operators:**
```hcl
locals {
  # Equality
  is_prod       = var.environment == "prod"     # true/false
  is_not_dev    = var.environment != "dev"      # true/false
  
  # Comparison
  is_many       = var.instance_count > 5        # true/false
  is_few        = var.instance_count < 10       # true/false
  is_enough     = var.instance_count >= 3       # true/false
  is_limited    = var.instance_count <= 20      # true/false
}
```

#### **Logical Operators:**
```hcl
locals {
  # AND - both must be true
  create_large = var.environment == "prod" && var.instance_count > 10
  
  # OR - at least one must be true
  allow_access = var.is_admin || var.is_developer
  
  # NOT - reverse boolean
  disable_debug = !var.enable_debug
  
  # Complex logic
  should_backup = (var.environment == "prod" || var.environment == "staging") && 
                  var.enable_backups &&
                  !var.is_test_mode
}
```

#### **Conditional (Ternary) Operator:**
```hcl
locals {
  # condition ? true_value : false_value
  
  # Choose instance type
  instance_type = var.environment == "prod" ? "t3.large" : "t2.micro"
  
  # Set monitoring
  monitoring = var.environment == "prod" ? true : false
  
  # Determine count
  instance_count = var.environment == "prod" ? 3 : 1
  
  # Nested conditionals
  storage_size = var.environment == "prod" ? 100 : (
    var.environment == "staging" ? 50 : 20
  )
  
  # With expressions
  name_suffix = var.use_random_suffix ? random_id.suffix.hex : "static"
}

resource "aws_instance" "web" {
  instance_type = local.instance_type
  monitoring    = local.monitoring
  
  tags = {
    Name = var.environment == "prod" ? "PROD-Server" : "DEV-Server"
  }
}
```

---

### 🔧 Built-in Functions

Terraform has 100+ built-in functions. Here are the most useful ones:

#### **Numeric Functions:**
```hcl
locals {
  # abs - Absolute value
  positive = abs(-5)              # 5
  
  # ceil - Round up
  rounded_up = ceil(3.2)          # 4
  
  # floor - Round down
  rounded_down = floor(3.8)       # 3
  
  # max - Maximum value
  highest = max(5, 12, 9)         # 12
  
  # min - Minimum value
  lowest = min(5, 12, 9)          # 5
  
  # pow - Power
  squared = pow(2, 3)             # 8
  
  # log - Logarithm
  logarithm = log(100, 10)        # 2
}
```

#### **String Functions:**
```hcl
locals {
  # upper - Convert to uppercase
  uppercase = upper("hello")               # "HELLO"
  
  # lower - Convert to lowercase
  lowercase = lower("WORLD")               # "world"
  
  # title - Title case
  titled = title("hello world")            # "Hello World"
  
  # trim - Remove whitespace
  trimmed = trim("  hello  ")              # "hello"
  
  # trimprefix - Remove prefix
  no_prefix = trimprefix("Mr. John", "Mr. ")  # "John"
  
  # trimsuffix - Remove suffix
  no_suffix = trimsuffix("file.txt", ".txt")  # "file"
  
  # replace - Replace substring
  replaced = replace("hello world", "world", "terraform")  # "hello terraform"
  
  # split - Split into list
  parts = split(",", "a,b,c")              # ["a", "b", "c"]
  
  # join - Join list into string
  joined = join("-", ["a", "b", "c"])      # "a-b-c"
  
  # substr - Substring
  sub = substr("hello world", 0, 5)        # "hello"
  
  # format - Format string
  formatted = format("Server-%03d", 5)     # "Server-005"
  
  # regex - Regular expression
  matched = regex("[0-9]+", "abc123def")   # "123"
  
  # regexall - All matches
  all_matches = regexall("[0-9]+", "a1b2c3")  # ["1", "2", "3"]
}
```

#### **Collection Functions:**
```hcl
variable "servers" {
  default = ["web1", "web2", "web3"]
}

variable "ports" {
  default = [80, 443, 22]
}

locals {
  # length - Get count
  server_count = length(var.servers)       # 3
  
  # element - Get item by index (with wraparound)
  first_server = element(var.servers, 0)   # "web1"
  wrapped = element(var.servers, 5)        # "web3" (5 % 3 = 2)
  
  # index - Find index of value
  port_index = index(var.ports, 443)       # 1
  
  # contains - Check if value exists
  has_https = contains(var.ports, 443)     # true
  
  # concat - Combine lists
  all_servers = concat(var.servers, ["db1", "db2"])
  # ["web1", "web2", "web3", "db1", "db2"]
  
  # distinct - Remove duplicates
  unique = distinct(["a", "b", "a", "c"]) # ["a", "b", "c"]
  
  # flatten - Flatten nested lists
  flat = flatten([["a", "b"], ["c", "d"]])  # ["a", "b", "c", "d"]
  
  # slice - Get sublist
  subset = slice(var.servers, 0, 2)        # ["web1", "web2"]
  
  # sort - Sort list
  sorted_ports = sort(var.ports)           # [22, 80, 443]
  
  # reverse - Reverse list
  reversed = reverse(var.servers)          # ["web3", "web2", "web1"]
  
  # range - Generate numeric list
  numbers = range(5)                       # [0, 1, 2, 3, 4]
  custom_range = range(2, 10, 2)          # [2, 4, 6, 8]
  
  # zipmap - Create map from two lists
  server_ips = zipmap(
    ["web1", "web2"],
    ["10.0.1.1", "10.0.1.2"]
  )
  # { web1 = "10.0.1.1", web2 = "10.0.1.2" }
}
```

#### **Map Functions:**
```hcl
variable "tags" {
  default = {
    Environment = "prod"
    Team        = "DevOps"
  }
}

variable "extra_tags" {
  default = {
    Project = "WebApp"
    Owner   = "John"
  }
}

locals {
  # keys - Get map keys
  tag_keys = keys(var.tags)               # ["Environment", "Team"]
  
  # values - Get map values
  tag_values = values(var.tags)           # ["prod", "DevOps"]
  
  # lookup - Get value by key with default
  env = lookup(var.tags, "Environment", "dev")  # "prod"
  missing = lookup(var.tags, "Missing", "default")  # "default"
  
  # merge - Combine maps
  all_tags = merge(var.tags, var.extra_tags)
  # {
  #   Environment = "prod"
  #   Team        = "DevOps"
  #   Project     = "WebApp"
  #   Owner       = "John"
  # }
}
```

#### **Type Conversion Functions:**
```hcl
locals {
  # tostring - Convert to string
  str = tostring(123)                     # "123"
  
  # tonumber - Convert to number
  num = tonumber("456")                   # 456
  
  # tobool - Convert to boolean
  boolean = tobool("true")                # true
  
  # tolist - Convert to list
  list_val = tolist(["a", "b"])          # ["a", "b"]
  
  # toset - Convert to set
  set_val = toset(["a", "b", "a"])       # ["a", "b"]
  
  # tomap - Convert to map
  map_val = tomap({key = "value"})       # {key = "value"}
}
```

#### **Date/Time Functions:**
```hcl
locals {
  # timestamp - Current time (UTC)
  now = timestamp()                       # "2025-12-19T10:30:00Z"
  
  # formatdate - Format timestamp
  formatted = formatdate("DD MMM YYYY hh:mm:ss", timestamp())
  # "19 Dec 2025 10:30:00"
  
  # timeadd - Add duration
  future = timeadd(timestamp(), "24h")    # Tomorrow
  past = timeadd(timestamp(), "-1h")      # One hour ago
}
```

#### **Filesystem Functions:**
```hcl
locals {
  # file - Read file contents
  script = file("${path.module}/script.sh")
  
  # fileexists - Check if file exists
  has_config = fileexists("${path.module}/config.json")
  
  # fileset - List files matching pattern
  yaml_files = fileset(path.module, "*.yaml")
  
  # basename - Get filename
  filename = basename("/path/to/file.txt")  # "file.txt"
  
  # dirname - Get directory path
  dirpath = dirname("/path/to/file.txt")   # "/path/to"
  
  # abspath - Absolute path
  absolute = abspath("relative/path")
  
  # pathexpand - Expand home directory
  expanded = pathexpand("~/documents")
}
```

#### **Encoding Functions:**
```hcl
locals {
  # base64encode - Encode to base64
  encoded = base64encode("Hello World")
  
  # base64decode - Decode from base64
  decoded = base64decode(local.encoded)
  
  # jsonencode - Convert to JSON
  json = jsonencode({
    name = "server"
    count = 3
  })
  # '{"name":"server","count":3}'
  
  # jsondecode - Parse JSON
  parsed = jsondecode('{"name":"server"}')
  # {name = "server"}
  
  # yamlencode - Convert to YAML
  yaml = yamlencode({
    name = "server"
    ports = [80, 443]
  })
  
  # yamldecode - Parse YAML
  yaml_parsed = yamldecode(file("config.yaml"))
}
```

#### **IP Network Functions:**
```hcl
locals {
  # cidrsubnet - Calculate subnet
  subnet1 = cidrsubnet("10.0.0.0/16", 8, 0)  # "10.0.0.0/24"
  subnet2 = cidrsubnet("10.0.0.0/16", 8, 1)  # "10.0.1.0/24"
  
  # cidrhost - Get IP from CIDR
  first_ip = cidrhost("10.0.1.0/24", 0)      # "10.0.1.0"
  second_ip = cidrhost("10.0.1.0/24", 1)     # "10.0.1.1"
  
  # cidrnetmask - Get netmask
  netmask = cidrnetmask("10.0.0.0/16")       # "255.255.0.0"
}
```

---

### 🎓 Practical Examples

#### **Example 1: Dynamic Resource Naming**
```hcl
variable "project" {
  default = "webapp"
}

variable "environment" {
  default = "prod"
}

variable "region" {
  default = "us-east-1"
}

locals {
  # Create consistent naming
  name_prefix = "${var.project}-${var.environment}"
  
  # Add region for multi-region deployments
  full_name = "${var.project}-${var.environment}-${var.region}"
  
  # Common tags
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "Terraform"
    CreatedAt   = formatdate("YYYY-MM-DD", timestamp())
  }
}

resource "aws_instance" "web" {
  count = 3
  
  ami           = "ami-12345"
  instance_type = var.environment == "prod" ? "t3.large" : "t2.micro"
  
  tags = merge(
    local.common_tags,
    {
      Name  = "${local.name_prefix}-web-${count.index + 1}"
      Role  = "webserver"
      Index = count.index + 1
    }
  )
}
```

#### **Example 2: Conditional Resource Creation**
```hcl
variable "create_database" {
  type    = bool
  default = true
}

variable "environment" {
  default = "dev"
}

resource "aws_db_instance" "main" {
  count = var.create_database ? 1 : 0
  
  engine         = "mysql"
  instance_class = var.environment == "prod" ? "db.t3.medium" : "db.t3.micro"
  
  # Only enable backups in production
  backup_retention_period = var.environment == "prod" ? 7 : 0
  
  # Multi-AZ only in production
  multi_az = var.environment == "prod" ? true : false
}

output "database_endpoint" {
  value = var.create_database ? aws_db_instance.main[0].endpoint : "No database created"
}
```

#### **Example 3: Working with Lists and Maps**
```hcl
variable "environments" {
  type = map(object({
    instance_type = string
    instance_count = number
    enable_monitoring = bool
  }))
  
  default = {
    dev = {
      instance_type     = "t2.micro"
      instance_count    = 1
      enable_monitoring = false
    }
    staging = {
      instance_type     = "t2.small"
      instance_count    = 2
      enable_monitoring = false
    }
    prod = {
      instance_type     = "t3.large"
      instance_count    = 5
      enable_monitoring = true
    }
  }
}

variable "current_environment" {
  default = "prod"
}

locals {
  config = var.environments[var.current_environment]
}

resource "aws_instance" "servers" {
  count = local.config.instance_count
  
  ami           = "ami-12345"
  instance_type = local.config.instance_type
  monitoring    = local.config.enable_monitoring
  
  tags = {
    Name = "server-${count.index + 1}"
    Environment = var.current_environment
  }
}
```

---

### ✅ Day 3 Checklist

By now you should understand:

- [x] HCL syntax and structure
- [x] All data types (primitive, collection, structural)
- [x] String interpolation
- [x] All expression types
- [x] Built-in functions
- [x] How to combine them in real scenarios

**Next:** Deep dive into Providers!

---

## Day 4: Providers Deep Dive

### 🎯 Learning Objectives
- Master provider configuration
- Work with multiple providers
- Use provider aliases
- Configure authentication
- Understand provider versioning

---

### 🔌 Understanding Providers

**What is a Provider?**

A provider is a plugin that enables Terraform to interact with an API (cloud provider, SaaS, etc.).

```plaintext
┌──────────────┐
│ Your Code    │  "create an EC2 instance"
│   (HCL)      │
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  Terraform   │  Understands what you want
│    Core      │
└──────┬───────┘
       │
       ↓
┌──────────────┐
│   Provider   │  Translates to AWS API calls
│   Plugin     │
└──────┬───────┘
       │
       ↓
┌──────────────┐
│  AWS API     │  Actually creates the resource
└──────────────┘
```

---

### 📦 Provider Configuration

#### **Basic Provider Setup**

```hcl
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"    # Where to download from
      version = "~> 5.0"            # Which version to use
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
```

#### **Understanding Version Constraints**

```hcl
# Exact version
version = "5.0.0"              # Only 5.0.0

# Greater than or equal
version = ">= 5.0.0"           # 5.0.0, 5.1.0, 6.0.0, etc.

# Less than
version = "< 6.0.0"            # Any version before 6.0.0

# Pessimistic constraint (~>)
version = "~> 5.0"             # 5.0, 5.1, 5.2, ... 5.x (not 6.0)
version = "~> 5.0.0"           # 5.0.0, 5.0.1, ... 5.0.x (not 5.1)

# Combined constraints
version = ">= 5.0, < 6.0"      # 5.x versions only

# Best practice for production
version = "5.31.0"             # Pin exact version
```

---

### 🌍 Popular Providers

#### **1. AWS Provider - Complete Configuration**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region     = "us-east-1"
  profile    = "default"        # AWS CLI profile
  
  # Optional: Assume role
  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/TerraformRole"
    session_name = "terraform-session"
    external_id  = "EXTERNAL_ID"
  }
  
  # Optional: Default tags for ALL resources
  default_tags {
    tags = {
      ManagedBy   = "Terraform"
      Environment = "Production"
      Team        = "Platform"
    }
  }
  
  # Optional: Ignore specific tags
  ignore_tags {
    key_prefixes = ["kubernetes.io/"]
    keys         = ["aws:createdBy"]
  }
  
  # Optional: Custom endpoints (for testing/localstack)
  endpoints {
    s3  = "http://localhost:4566"
    ec2 = "http://localhost:4566"
  }
}

# Example resource - automatically gets default_tags
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
  
  # These tags merge with default_tags
  tags = {
    Name = "MyBucket"
  }
  # Final tags:
  # - ManagedBy = "Terraform"
  # - Environment = "Production"
  # - Team = "Platform"
  # - Name = "MyBucket"
}
```

**AWS Authentication Methods:**

```bash
# Method 1: Environment Variables (RECOMMENDED)
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_SESSION_TOKEN="your-session-token"  # If using MFA
export AWS_DEFAULT_REGION="us-east-1"

# Method 2: AWS CLI Profile
aws configure --profile terraform
# Then in Terraform:
provider "aws" {
  profile = "terraform"
}

# Method 3: Shared Credentials File
provider "aws" {
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "default"
}

# Method 4: IAM Role (if running on EC2/ECS/Lambda)
provider "aws" {
  region = "us-east-1"
  # Automatically uses attached IAM role
}

# Method 5: AWS SSO
aws sso login --profile my-sso-profile
# Then:
provider "aws" {
  profile = "my-sso-profile"
}
```

---

#### **2. Azure Provider**

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}  # Required, even if empty
  
  subscription_id = "00000000-0000-0000-0000-000000000000"
  tenant_id       = "11111111-1111-1111-1111-111111111111"
  
  # Optional: Use specific subscription
  skip_provider_registration = true
  
  # Optional: Custom resource provider registration
  features {
    resource_group {
      prevent_deletion_if_contains_resources = true
    }
    
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
    
    virtual_machine {
      delete_os_disk_on_deletion     = true
      graceful_shutdown              = false
      skip_shutdown_and_force_delete = false
    }
  }
}

# Azure authentication methods
```

**Azure Authentication:**

```bash
# Method 1: Azure CLI (RECOMMENDED for development)
az login
# Terraform automatically uses Azure CLI credentials

# Method 2: Service Principal
export ARM_CLIENT_ID="00000000-0000-0000-0000-000000000000"
export ARM_CLIENT_SECRET="your-client-secret"
export ARM_SUBSCRIPTION_ID="00000000-0000-0000-0000-000000000000"
export ARM_TENANT_ID="11111111-1111-1111-1111-111111111111"

# Method 3: Managed Identity (when running on Azure VM/App Service)
provider "azurerm" {
  features {}
  use_msi = true
}

# Method 4: In Terraform code (NOT RECOMMENDED - security risk)
provider "azurerm" {
  features {}
  client_id       = "00000000-0000-0000-0000-000000000000"
  client_secret   = "your-secret"
  subscription_id = "00000000-0000-0000-0000-000000000000"
  tenant_id       = "11111111-1111-1111-1111-111111111111"
}
```

**Azure Example Resource:**

```hcl
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}

resource "azurerm_subnet" "example" {
  name                 = "internal"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.2.0/24"]
}
```

---

#### **3. Google Cloud Provider**

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project     = "my-project-id"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = file("path/to/service-account-key.json")
  
  # Optional: Default labels
  default_labels = {
    managed_by  = "terraform"
    environment = "production"
  }
  
  # Optional: Batching for API calls
  batching {
    send_after      = "10s"
    enable_batching = true
  }
}

# GCP authentication methods
```

**GCP Authentication:**

```bash
# Method 1: Service Account Key (RECOMMENDED for CI/CD)
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

# Method 2: gcloud CLI (for development)
gcloud auth application-default login

# Method 3: In Terraform code
provider "google" {
  credentials = file("service-account-key.json")
}

# Method 4: GCE Metadata (when running on GCE)
provider "google" {
  # Automatically uses GCE metadata service
}
```

**GCP Example Resources:**

```hcl
resource "google_compute_network" "vpc" {
  name                    = "my-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "my-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-central1"
  network       = google_compute_network.vpc.id
}

resource "google_compute_instance" "vm" {
  name         = "my-instance"
  machine_type = "f1-micro"
  zone         = "us-central1-a"
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
  
  network_interface {
    subnetwork = google_compute_subnetwork.subnet.id
    
    access_config {
      // Ephemeral public IP
    }
  }
}
```

---

### 🎭 Multiple Provider Configurations (Aliases)

**Use Case:** Deploy to multiple regions or accounts

```hcl
# Default AWS provider (us-east-1)
provider "aws" {
  region = "us-east-1"
}

# West coast provider
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

# Europe provider
provider "aws" {
  alias  = "europe"
  region = "eu-west-1"
}

# Production account provider
provider "aws" {
  alias   = "prod"
  region  = "us-east-1"
  profile = "production"
}

# Resources using default provider (us-east-1)
resource "aws_s3_bucket" "east_bucket" {
  bucket = "my-east-bucket"
}

# Resources using west provider
resource "aws_s3_bucket" "west_bucket" {
  provider = aws.west  # Specify alias
  bucket   = "my-west-bucket"
}

# Resources using europe provider
resource "aws_vpc" "eu_vpc" {
  provider   = aws.europe
  cidr_block = "10.0.0.0/16"
}

# Resources using production account
resource "aws_instance" "prod_server" {
  provider      = aws.prod
  ami           = "ami-12345"
  instance_type = "t3.large"
}
```

**Multi-Region Deployment Example:**

```hcl
# File: main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Primary region
provider "aws" {
  region = var.primary_region
}

# Secondary region for DR
provider "aws" {
  alias  = "dr"
  region = var.dr_region
}

# Variables
variable "primary_region" {
  default = "us-east-1"
}

variable "dr_region" {
  default = "us-west-2"
}

# Primary region resources
resource "aws_vpc" "primary" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name   = "primary-vpc"
    Region = var.primary_region
  }
}

resource "aws_instance" "primary_web" {
  count         = 3
  ami           = "ami-east-12345"
  instance_type = "t3.medium"
  
  tags = {
    Name = "primary-web-${count.index + 1}"
  }
}

# DR region resources
resource "aws_vpc" "dr" {
  provider   = aws.dr
  cidr_block = "10.1.0.0/16"
  
  tags = {
    Name   = "dr-vpc"
    Region = var.dr_region
  }
}

resource "aws_instance" "dr_web" {
  provider      = aws.dr
  count         = 3
  ami           = "ami-west-12345"
  instance_type = "t3.medium"
  
  tags = {
    Name = "dr-web-${count.index + 1}"
  }
}

# Outputs
output "primary_vpc_id" {
  value = aws_vpc.primary.id
}

output "dr_vpc_id" {
  value = aws_vpc.dr.id
}
```

---

### 🌐 Multi-Cloud Deployment

**Deploy across AWS, Azure, and GCP:**

```hcl
# File: main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

# AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Azure Provider
provider "azurerm" {
  features {}
}

# GCP Provider
provider "google" {
  project = "my-project-id"
  region  = "us-central1"
}

# AWS Resources
resource "aws_s3_bucket" "aws_storage" {
  bucket = "my-aws-storage"
  
  tags = {
    Cloud = "AWS"
  }
}

resource "aws_instance" "aws_server" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
  
  tags = {
    Name  = "AWS-Server"
    Cloud = "AWS"
  }
}

# Azure Resources
resource "azurerm_resource_group" "azure_rg" {
  name     = "my-resource-group"
  location = "East US"
  
  tags = {
    Cloud = "Azure"
  }
}

resource "azurerm_storage_account" "azure_storage" {
  name                     = "myazurestorage"
  resource_group_name      = azurerm_resource_group.azure_rg.name
  location                 = azurerm_resource_group.azure_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  
  tags = {
    Cloud = "Azure"
  }
}

# GCP Resources
resource "google_storage_bucket" "gcp_storage" {
  name     = "my-gcp-storage"
  location = "US"
  
  labels = {
    cloud = "gcp"
  }
}

resource "google_compute_instance" "gcp_server" {
  name         = "gcp-server"
  machine_type = "f1-micro"
  zone         = "us-central1-a"
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
  
  network_interface {
    network = "default"
    
    access_config {}
  }
  
  labels = {
    cloud = "gcp"
  }
}

# Outputs
output "aws_bucket" {
  value = aws_s3_bucket.aws_storage.id
}

output "azure_storage" {
  value = azurerm_storage_account.azure_storage.name
}

output "gcp_bucket" {
  value = google_storage_bucket.gcp_storage.url
}
```

---

### 🔐 Provider Security Best Practices

#### **1. Never Hardcode Credentials**

```hcl
# ❌ BAD - Credentials in code
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# ✅ GOOD - Use environment variables
provider "aws" {
  region = "us-east-1"
  # Credentials from environment or AWS CLI
}

# ✅ GOOD - Use AWS CLI profile
provider "aws" {
  region  = "us-east-1"
  profile = "terraform"
}

# ✅ GOOD - Assume IAM role
provider "aws" {
  region = "us-east-1"
  assume_role {
    role_arn = "arn:aws:iam::123456789012:role/TerraformRole"
  }
}
```

#### **2. Use Least Privilege IAM Policies**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:CreateTags",
        "ec2:DeleteTags"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:RunInstances",
        "ec2:TerminateInstances",
        "ec2:StopInstances",
        "ec2:StartInstances"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

#### **3. Pin Provider Versions**

```hcl
# ✅ GOOD - Exact version for production
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.31.0"
    }
  }
}

# ❌ BAD - No version constraint
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
```

---

### ✅ Day 4 Checklist

By now you should understand:

- [x] What providers are and how they work
- [x] How to configure AWS, Azure, and GCP providers
- [x] Multiple authentication methods
- [x] Provider aliases for multi-region/multi-account
- [x] Multi-cloud deployments
- [x] Provider security best practices

**Next:** Deep dive into Resources!

---

## Day 5: Resources - The Heart of Terraform

### 🎯 Learning Objectives
- Understand resource blocks completely
- Master resource dependencies
- Learn meta-arguments
- Handle resource lifecycle
- Use provisioners correctly

---

### 🏗️ What is a Resource?

A **resource** is any infrastructure component you want to create/manage:
- Virtual machines
- Storage buckets
- Databases
- Networks
- Load balancers
- DNS records
- Anything your provider supports!

---

### 📝 Resource Block Syntax

```hcl
resource "resource_type" "resource_name" {
  # Configuration arguments
  argument1 = "value1"
  argument2 = "value2"
  
  # Nested blocks
  nested_block {
    nested_arg = "value"
  }
  
  # Meta-arguments (special Terraform arguments)
  count    = 3
  depends_on = [other_resource.name]
  lifecycle {
    create_before_destroy = true
  }
}
```

**Breakdown:**
- `resource` = Keyword
- `"resource_type"` = Provider resource type (e.g., `aws_instance`, `azurerm_virtual_machine`)
- `"resource_name"` = Your local name for this resource
- Resource ID = `resource_type.resource_name` (e.g., `aws_instance.web`)

---

### 🌟 Complete Resource Examples

#### **Example 1: AWS EC2 Instance**

```hcl
# Security Group
resource "aws_security_group" "web_sg" {
  name        = "web-server-sg"
  description = "Security group for web server"
  
  # Inbound HTTP
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTP from anywhere"
  }
  
  # Inbound HTTPS
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTPS from anywhere"
  }
  
  # Inbound SSH (restricted)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.0/24"]  # Your office IP
    description = "Allow SSH from office"
  }
  
  # Outbound - all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }
  
  tags = {
    Name = "web-server-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2
  instance_type = "t3.micro"
  
  # Reference security group created above
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  
  # User data script
  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from Terraform!</h1>" > /var/www/html/index.html
  EOF
  
  # Root volume
  root_block_device {
    volume_size           = 20
    volume_type           = "gp3"
    delete_on_termination = true
    encrypted             = true
  }
  
  # Additional volume
  ebs_block_device {
    device_name           = "/dev/sdf"
    volume_size           = 50
    volume_type           = "gp3"
    delete_on_termination = true
    encrypted             = true
  }
  
  # Enable detailed monitoring
  monitoring = true
  
  # Instance metadata options (security best practice)
  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required"  # IMDSv2
    http_put_response_hop_limit = 1
  }
  
  tags = {
    Name        = "web-server"
    Environment = "production"
    ManagedBy   = "Terraform"
  }
  
  # Lifecycle rules
  lifecycle {
    create_before_destroy = true
    ignore_changes        = [user_data]
  }
}

# Elastic IP
resource "aws_eip" "web_eip" {
  instance = aws_instance.web_server.id
  domain   = "vpc"
  
  tags = {
    Name = "web-server-eip"
  }
  
  # Don't create until instance is ready
  depends_on = [aws_instance.web_server]
}
```

---

#### **Example 2: Azure Virtual Machine**

```hcl
# Resource Group
resource "azurerm_resource_group" "main" {
  name     = "vm-resources"
  location = "East US"
  
  tags = {
    Environment = "Production"
  }
}

# Virtual Network
resource "azurerm_virtual_network" "main" {
  name                = "vm-network"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

# Subnet
resource "azurerm_subnet" "internal" {
  name                 = "internal"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.2.0/24"]
}

# Network Interface
resource "azurerm_network_interface" "main" {
  name                = "vm-nic"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  
  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.main.id
  }
}

# Public IP
resource "azurerm_public_ip" "main" {
  name                = "vm-public-ip"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# Network Security Group
resource "azurerm_network_security_group" "main" {
  name                = "vm-nsg"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  
  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# Associate NSG with NIC
resource "azurerm_network_interface_security_group_association" "main" {
  network_interface_id      = azurerm_network_interface.main.id
  network_security_group_id = azurerm_network_security_group.main.id
}

# Virtual Machine
resource "azurerm_linux_virtual_machine" "main" {
  name                = "production-vm"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  size                = "Standard_B2s"
  admin_username      = "adminuser"
  
  network_interface_ids = [
    azurerm_network_interface.main.id,
  ]
  
  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }
  
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
    disk_size_gb         = 30
  }
  
  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-focal"
    sku       = "20_04-lts-gen2"
    version   = "latest"
  }
  
  tags = {
    Environment = "Production"
  }
}
```

---

### 🔗 Resource Dependencies

Terraform automatically detects dependencies when you reference other resources:

#### **Implicit Dependencies (Automatic)**

```hcl
# Security group created first
resource "aws_security_group" "web" {
  name = "web-sg"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance created AFTER security group
# Terraform detects: aws_instance.web depends on aws_security_group.web
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  # This reference creates implicit dependency
  vpc_security_group_ids = [aws_security_group.web.id]
}

# EIP created AFTER instance
# Terraform detects: aws_eip.web depends on aws_instance.web
resource "aws_eip" "web" {
  instance = aws_instance.web.id
  domain   = "vpc"
}
```

**Terraform automatically creates this order:**
```plaintext
1. aws_security_group.web
2. aws_instance.web
3. aws_eip.web
```

---

#### **Explicit Dependencies (Manual)**

Use `depends_on` when Terraform can't detect the dependency:

```hcl
# S3 bucket for storing data
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

# EC2 instance that needs bucket to exist first
# But doesn't reference it directly in code
resource "aws_instance" "processor" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  user_data = <<-EOF
    #!/bin/bash
    # Script uploads data to S3
    aws s3 cp data.txt s3://my-data-bucket/
  EOF
  
  # Explicit dependency - create bucket first!
  depends_on = [aws_s3_bucket.data]
}

# IAM role policy attachment
resource "aws_iam_role_policy_attachment" "s3_access" {
  role       = aws_iam_role.app_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

# Instance profile needs policy attached first
resource "aws_iam_instance_profile" "app_profile" {
  name = "app-profile"
  role = aws_iam_role.app_role.name
  
  # Wait for policy attachment
  depends_on = [aws_iam_role_policy_attachment.s3_access]
}
```

**When to use `depends_on`:**
- Resource needs another to exist but doesn't reference it
- IAM policy attachments before using the role
- Database initialization before app deployment
- Network routes before instances

---

### 🎛️ Meta-Arguments

Meta-arguments work with ALL resource types:

#### **1. `count` - Create Multiple Similar Resources**

```hcl
# Create 3 identical instances
resource "aws_instance" "web" {
  count = 3
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "web-server-${count.index}"
    # Results: web-server-0, web-server-1, web-server-2
  }
}

# Reference specific instance
output "first_instance_ip" {
  value = aws_instance.web[0].private_ip
}

output "all_instance_ips" {
  value = aws_instance.web[*].private_ip
}

# Conditional creation
variable "create_database" {
  type    = bool
  default = true
}

resource "aws_db_instance" "main" {
  count = var.create_database ? 1 : 0  # Create only if true
  
  engine         = "mysql"
  instance_class = "db.t3.micro"
}

# Create different number per environment
variable "environment" {
  default = "prod"
}

resource "aws_instance" "app" {
  count = var.environment == "prod" ? 5 : (
          var.environment == "staging" ? 3 : 1
  )
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
}
```

---

#### **2. `for_each` - Create Resources from Map/Set**

```hcl
# From set
variable "users" {
  type    = set(string)
  default = ["john", "jane", "bob"]
}

resource "aws_iam_user" "users" {
  for_each = var.users
  name     = each.key  # "john", "jane", "bob"
}

# From map
variable "instances" {
  type = map(object({
    instance_type = string
    ami           = string
  }))
  
  default = {
    web = {
      instance_type = "t2.micro"
      ami           = "ami-12345"
    }
    api = {
      instance_type = "t2.small"
      ami           = "ami-12345"
    }
    worker = {
      instance_type = "t2.medium"
      ami           = "ami-67890"
    }
  }
}

resource "aws_instance" "servers" {
  for_each = var.instances
  
  ami           = each.value.ami
  instance_type = each.value.instance_type
  
  tags = {
    Name = "${each.key}-server"  # "web-server", "api-server", "worker-server"
    Type = each.key
  }
}

# Reference specific resource
output "web_server_ip" {
  value = aws_instance.servers["web"].private_ip
}

# Reference all resources
output "all_server_ips" {
  value = {
    for key, instance in aws_instance.servers :
    key => instance.private_ip
  }
}

# Complex example: Create subnets
variable "availability_zones" {
  type = map(string)
  default = {
    "us-east-1a" = "10.0.1.0/24"
    "us-east-1b" = "10.0.2.0/24"
    "us-east-1c" = "10.0.3.0/24"
  }
}

resource "aws_subnet" "public" {
  for_each = var.availability_zones
  
  vpc_id            = aws_vpc.main.id
  availability_zone = each.key
  cidr_block        = each.value
  
  tags = {
    Name = "public-subnet-${each.key}"
  }
}
```

**`count` vs `for_each`:**

| Feature | count | for_each |
|---------|-------|----------|
| Input | Number | Map or Set |
| Index | Numeric (0, 1, 2) | String keys |
| Adding/Removing | Can cause recreation | Stable - no recreation |
| Use When | Same configuration | Different configurations |
| Best For | Simple duplication | Named resources |

---

#### **3. `depends_on` - Manual Dependencies**

```hcl
# Covered above - forces creation order
resource "aws_instance" "app" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  depends_on = [
    aws_db_instance.main,
    aws_s3_bucket.data,
    aws_iam_role_policy_attachment.app_policy
  ]
}
```

---

#### **4. `provider` - Use Specific Provider**

```hcl
# Multi-region deployment
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

# Default provider (us-east-1)
resource "aws_instance" "east" {
  ami           = "ami-east-12345"
  instance_type = "t2.micro"
}

# West provider
resource "aws_instance" "west" {
  provider      = aws.west
  ami           = "ami-west-12345"
  instance_type = "t2.micro"
}
```

---

#### **5. `lifecycle` - Control Resource Behavior**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    # Create new resource before destroying old one
    create_before_destroy = true
    
    # Prevent accidental deletion
    prevent_destroy = true
    
    # Ignore changes to specific attributes
    ignore_changes = [
      tags,
      user_data,
    ]
    
    # Ignore all changes (rare use case)
    # ignore_changes = all
    
    # Custom conditions
    precondition {
      condition     = var.environment == "prod"
      error_message = "This resource can only be created in production."
    }
    
    postcondition {
      condition     = self.instance_state == "running"
      error_message = "Instance must be in running state."
    }
  }
}
```

**Lifecycle options explained:**

**`create_before_destroy`:**
```hcl
# Useful for zero-downtime updates
resource "aws_launch_configuration" "app" {
  image_id      = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    create_before_destroy = true
  }
}

# When you change AMI:
# 1. Create new launch configuration
# 2. Update references to new config
# 3. Delete old launch configuration
```

**`prevent_destroy`:**
```hcl
# Protect critical resources
resource "aws_db_instance" "production" {
  engine         = "mysql"
  instance_class = "db.t3.large"
  
  lifecycle {
    prevent_destroy = true  # terraform destroy will fail
  }
}
```

**`ignore_changes`:**
```hcl
# Don't revert external changes
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "web-server"
  }
  
  lifecycle {
    # If someone manually changes tags, Terraform won't revert them
    ignore_changes = [tags]
    
    # Ignore user_data changes (common for auto-updated startup scripts)
    ignore_changes = [user_data]
  }
}
```

**Conditions (Terraform 1.2+):**
```hcl
variable "environment" {
  type = string
}

variable "instance_type" {
  type = string
}

resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = var.instance_type
  
  lifecycle {
    # Check BEFORE creating
    precondition {
      condition     = var.environment == "prod" ? contains(["t3.large", "t3.xlarge"], var.instance_type) : true
      error_message = "Production instances must be t3.large or larger."
    }
    
    # Check AFTER creating
    postcondition {
      condition     = self.instance_state == "running"
      error_message = "Instance failed to start. State: ${self.instance_state}"
    }
  }
}
```

---

### 📦 Resource Addressing

```hcl
# Single resource
resource "aws_instance" "web" {
  ami = "ami-12345"
}
# Address: aws_instance.web

# With count
resource "aws_instance" "app" {
  count = 3
  ami   = "ami-12345"
}
# Address: aws_instance.app[0], aws_instance.app[1], aws_instance.app[2]

# With for_each
resource "aws_instance" "server" {
  for_each = toset(["web", "api", "worker"])
  ami      = "ami-12345"
}
# Address: aws_instance.server["web"], aws_instance.server["api"]

# In modules
module "vpc" {
  source = "./modules/vpc"
}
# Address: module.vpc.aws_vpc.main
```

---

### 🔄 Resource Behavior

#### **Create:**
```bash
terraform apply
# Creates new resources
```

#### **Update (In-Place):**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"  # Change this to t2.small
  
  tags = {
    Name = "web-server"  # Change tags
  }
}
```
```bash
terraform apply
# Updates existing resource without recreation
# ~ indicates in-place update
```

#### **Replace (Destroy + Create):**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"  # Change AMI (requires new instance)
  instance_type = "t2.micro"
}
```
```bash
terraform apply
# -/+ indicates destroy and recreate
```

#### **Delete:**
```hcl
# Remove resource from configuration
# resource "aws_instance" "web" {
#   ...
# }
```
```bash
terraform apply
# - indicates deletion
```

---

### ✅ Day 5 Checklist

- [x] Understand resource block syntax
- [x] Reference resources and attributes
- [x] Implicit vs explicit dependencies
- [x] All meta-arguments (count, for_each, depends_on, provider, lifecycle)
- [x] Resource addressing
- [x] Resource behavior (create, update, replace, delete)

**Next:** Variables - Making configurations dynamic!

---

## Day 6: Variables - Dynamic Configuration

### 🎯 Learning Objectives
- Master all variable types
- Set variable values multiple ways
- Use variable validation
- Understand variable precedence
- Create reusable configurations

---

### 📥 Input Variables

Variables make your Terraform code reusable and flexible.

#### **Basic Variable Declaration**

```hcl
# File: variables.tf

# String variable
variable "region" {
  type        = string
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

# Number variable
variable "instance_count" {
  type        = number
  description = "Number of EC2 instances to create"
  default     = 3
}

# Boolean variable
variable "enable_monitoring" {
  type        = bool
  description = "Enable detailed monitoring"
  default     = true
}

# List variable
variable "availability_zones" {
  type        = list(string)
  description = "List of availability zones"
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

# Map variable
variable "instance_types" {
  type        = map(string)
  description = "Instance types per environment"
  default = {
    dev     = "t2.micro"
    staging = "t2.small"
    prod    = "t3.large"
  }
}

# Object variable
variable "database_config" {
  type = object({
    engine            = string
    engine_version    = string
    instance_class    = string
    allocated_storage = number
    multi_az          = bool
  })
  
  description = "Database configuration"
  
  default = {
    engine            = "mysql"
    engine_version    = "8.0.33"
    instance_class    = "db.t3.micro"
    allocated_storage = 20
    multi_az          = false
  }
}

# Set variable (unique values only)
variable "allowed_ips" {
  type        = set(string)
  description = "Allowed IP addresses"
  default     = ["203.0.113.0/24", "198.51.100.0/24"]
}

# Any type (not recommended for production)
variable "custom_config" {
  type        = any
  description = "Custom configuration"
  default     = {}
}
```

---

### 🎨 Variable Types Reference

```hcl
# Primitive Types
variable "string_var" {
  type = string
}

variable "number_var" {
  type = number
}

variable "bool_var" {
  type = bool
}

# Collection Types
variable "list_var" {
  type = list(string)  # List of strings
}

variable "list_numbers" {
  type = list(number)  # List of numbers
}

variable "map_var" {
  type = map(string)  # Map with string values
}

variable "set_var" {
  type = set(string)  # Set of unique strings
}

# Structural Types
variable "object_var" {
  type = object({
    name   = string
    age    = number
    active = bool
  })
}

variable "tuple_var" {
  type = tuple([string, number, bool])
}

# Complex nested types
variable "complex_var" {
  type = map(object({
    instance_type = string
    tags          = map(string)
    volumes       = list(object({
      size = number
      type = string
    }))
  }))
}
```

---

### ⚙️ Using Variables

```hcl
# File: main.tf

# Use with var prefix
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_types[var.environment]
  monitoring    = var.enable_monitoring
  
  count = var.instance_count
  
  tags = merge(
    var.common_tags,
    {
      Name = "web-server-${count.index + 1}"
    }
  )
}

# Use in locals
locals {
  full_name = "${var.project}-${var.environment}-${var.region}"
  
  is_production = var.environment == "prod"
  
  instance_type = local.is_production ? "t3.large" : "t2.micro"
}

# Use in outputs
output "instance_ips" {
  value = aws_instance.web[*].private_ip
}
```

---

### 📝 Setting Variable Values

#### **Method 1: Default Values (Lowest Priority)**

```hcl
variable "region" {
  type    = string
  default = "us-east-1"  # Used if no other value provided
}
```

---

#### **Method 2: Command Line**

```bash
# Single variable
terraform apply -var="region=us-west-2"

# Multiple variables
terraform apply \
  -var="region=us-west-2" \
  -var="instance_count=5" \
  -var="enable_monitoring=true"

# List variable
terraform apply -var='availability_zones=["us-west-2a","us-west-2b"]'

# Map variable
terraform apply -var='instance_types={dev="t2.micro",prod="t3.large"}'
```

---

#### **Method 3: Variable Files (.tfvars)**

```hcl
# File: terraform.tfvars (automatically loaded)
region         = "us-west-2"
instance_count = 5
enable_monitoring = true

availability_zones = [
  "us-west-2a",
  "us-west-2b",
  "us-west-2c"
]

instance_types = {
  dev     = "t2.micro"
  staging = "t2.small"
  prod    = "t3.large"
}

database_config = {
  engine            = "postgresql"
  engine_version    = "14.7"
  instance_class    = "db.t3.small"
  allocated_storage = 50
  multi_az          = true
}

common_tags = {
  Project     = "MyApp"
  Team        = "Platform"
  ManagedBy   = "Terraform"
}
```

```hcl
# File: prod.tfvars (load explicitly)
environment       = "prod"
instance_count    = 10
enable_monitoring = true
instance_type     = "t3.large"
```

```bash
# Load specific file
terraform apply -var-file="prod.tfvars"

# Load multiple files
terraform apply -var-file="common.tfvars" -var-file="prod.tfvars"
```

---

#### **Method 4: Environment Variables**

```bash
# Format: TF_VAR_<variable_name>

# String
export TF_VAR_region="us-west-2"

# Number
export TF_VAR_instance_count=5

# Boolean
export TF_VAR_enable_monitoring=true

# List (JSON)
export TF_VAR_availability_zones='["us-west-2a","us-west-2b"]'

# Map (JSON)
export TF_VAR_instance_types='{"dev":"t2.micro","prod":"t3.large"}'

# Object (JSON)
export TF_VAR_database_config='{
  "engine": "mysql",
  "engine_version": "8.0",
  "instance_class": "db.t3.micro",
  "allocated_storage": 20,
  "multi_az": false
}'

# Then run
terraform apply
```

---

#### **Method 5: Interactive Prompt**

```hcl
# Variable without default
variable "database_password" {
  type        = string
  description = "Database admin password"
  sensitive   = true
  # No default - will prompt
}
```

```bash
terraform apply
# Terraform will prompt:
# var.database_password
#   Database admin password
#
#   Enter a value: █
```

---

### 📊 Variable Precedence (Highest to Lowest)

```plaintext
1. Command line -var flags         (highest priority)
2. *.auto.tfvars files (alphabetical order)
3. terraform.tfvars file
4. Environment variables (TF_VAR_*)
5. Default values in variable blocks (lowest priority)
```

**Example:**
```hcl
# variables.tf
variable "region" {
  default = "us-east-1"  # Priority 5
}
```

```bash
# Environment
export TF_VAR_region="us-west-1"  # Priority 4

# terraform.tfvars
region = "us-west-2"  # Priority 3

# prod.auto.tfvars
region = "eu-west-1"  # Priority 2

# Command line
terraform apply -var="region=ap-south-1"  # Priority 1 - WINS!
# Final value: "ap-south-1"
```

---

### ✅ Variable Validation

```hcl
# Validate environment name
variable "environment" {
  type        = string
  description = "Environment name"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# Validate instance count
variable "instance_count" {
  type        = number
  description = "Number of instances"
  
  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 10
    error_message = "Instance count must be between 1 and 10."
  }
}

# Validate CIDR block
variable "vpc_cidr" {
  type        = string
  description = "VPC CIDR block"
  
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.vpc_cidr))
    error_message = "VPC CIDR must be a valid IPv4 CIDR block."
  }
}

# Validate region
variable "region" {
  type        = string
  description = "AWS region"
  
  validation {
    condition     = can(regex("^(us|eu|ap|sa|ca|me|af)-(north|south|east|west|central|northeast|southeast)-[1-3]$", var.region))
    error_message = "Must be a valid AWS region."
  }
}

# Multiple validations
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  
  validation {
    condition     = can(regex("^t[2-3]\\.", var.instance_type))
    error_message = "Instance type must be t2 or t3 series."
  }
  
  validation {
    condition     = contains(["t2.micro", "t2.small", "t3.micro", "t3.small"], var.instance_type)
    error_message = "Instance type must be micro or small."
  }
}

# Complex validation
variable "database_config" {
  type = object({
    engine            = string
    allocated_storage = number
    multi_az          = bool
  })
  
  validation {
    condition     = contains(["mysql", "postgres", "mariadb"], var.database_config.engine)
    error_message = "Database engine must be mysql, postgres, or mariadb."
  }
  
  validation {
    condition     = var.database_config.allocated_storage >= 20
    error_message = "Database storage must be at least 20 GB."
  }
  
  validation {
    condition     = var.database_config.engine == "postgres" ? var.database_config.allocated_storage >= 50 : true
    error_message = "PostgreSQL requires at least 50 GB storage."
  }
}
```

---

### 🔐 Sensitive Variables

```hcl
variable "database_password" {
  type        = string
  description = "Database admin password"
  sensitive   = true  # Won't show in logs/output
}

variable "api_key" {
  type      = string
  sensitive = true
}

# Using sensitive variables
resource "aws_db_instance" "main" {
  engine         = "mysql"
  username       = "admin"
  password       = var.database_password  # Value hidden in logs
  instance_class = "db.t3.micro"
}

# Output won't show value
output "db_password" {
  value     = var.database_password
  sensitive = true
}
```

---

### 🎓 Real-World Example: Complete Variable Setup

```hcl
# ==========================================
# File: variables.tf
# ==========================================

# Project Info
variable "project_name" {
  type        = string
  description = "Project name for resource naming"
  
  validation {
    condition     = length(var.project_name) > 0 && length(var.project_name) <= 20
    error_message = "Project name must be 1-20 characters."
  }
}

variable "environment" {
  type        = string
  description = "Environment (dev/staging/prod)"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# AWS Configuration
variable "region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones"
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

# Networking
variable "vpc_cidr" {
  type        = string
  description = "VPC CIDR block"
  default     = "10.0.0.0/16"
  
  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0))
    error_message = "Must be a valid CIDR block."
  }
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "Public subnet CIDR blocks"
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "Private subnet CIDR blocks"
  default     = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
}

# Compute
variable "instance_config" {
  type = map(object({
    instance_type = string
    instance_count = number
    volume_size    = number
  }))
  
  description = "Instance configuration per environment"
  
  default = {
    dev = {
      instance_type  = "t2.micro"
      instance_count = 1
      volume_size    = 20
    }
    staging = {
      instance_type  = "t2.small"
      instance_count = 2
      volume_size    = 30
    }
    prod = {
      instance_type  = "t3.large"
      instance_count = 5
      volume_size    = 50
    }
  }
}

# Database
variable "create_database" {
  type        = bool
  description = "Whether to create database"
  default     = true
}

variable "database_config" {
  type = object({
    engine            = string
    engine_version    = string
    instance_class    = string
    allocated_storage = number
    multi_az          = bool
    backup_retention  = number
  })
  
  description = "Database configuration"
  
  default = {
    engine            = "mysql"
    engine_version    = "8.0.33"
    instance_class    = "db.t3.micro"
    allocated_storage = 20
    multi_az          = false
    backup_retention  = 7
  }
}

variable "database_password" {
  type        = string
  description = "Database admin password"
  sensitive   = true
}

# Tags
variable "common_tags" {
  type        = map(string)
  description = "Common tags for all resources"
  default     = {}
}

# Feature Flags
variable "enable_monitoring" {
  type        = bool
  description = "Enable detailed monitoring"
  default     = false
}

variable "enable_auto_scaling" {
  type        = bool
  description = "Enable auto scaling"
  default     = false
}

# ==========================================
# File: terraform.tfvars
# ==========================================

project_name = "myapp"
environment  = "dev"
region       = "us-east-1"

availability_zones = ["us-east-1a", "us-east-1b"]

vpc_cidr = "10.0.0.0/16"

public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24"]

create_database = true

common_tags = {
  Project    = "MyApp"
  Team       = "Platform"
  ManagedBy  = "Terraform"
  CostCenter = "Engineering"
}

enable_monitoring    = false
enable_auto_scaling  = false

# ==========================================
# File: prod.tfvars
# ==========================================

environment = "prod"
region      = "us-east-1"

availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

database_config = {
  engine            = "mysql"
  engine_version    = "8.0.33"
  instance_class    = "db.r5.large"
  allocated_storage = 100
  multi_az          = true
  backup_retention  = 30
}

enable_monitoring   = true
enable_auto_scaling = true

common_tags = {
  Project     = "MyApp"
  Team        = "Platform"
  Environment = "Production"
  ManagedBy   = "Terraform"
  CostCenter  = "Engineering"
  Compliance  = "Required"
}

# ==========================================
# File: main.tf (using variables)
# ==========================================

locals {
  name_prefix = "${var.project_name}-${var.environment}"
  config      = var.instance_config[var.environment]
  
  all_tags = merge(
    var.common_tags,
    {
      Environment = var.environment
      Region      = var.region
    }
  )
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = merge(
    local.all_tags,
    {
      Name = "${local.name_prefix}-vpc"
    }
  )
}

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = merge(
    local.all_tags,
    {
      Name = "${local.name_prefix}-public-${var.availability_zones[count.index]}"
      Type = "public"
    }
  )
}

resource "aws_instance" "app" {
  count = local.config.instance_count
  
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = local.config.instance_type
  subnet_id     = aws_subnet.public[count.index % length(aws_subnet.public)].id
  monitoring    = var.enable_monitoring
  
  root_block_device {
    volume_size = local.config.volume_size
  }
  
  tags = merge(
    local.all_tags,
    {
      Name  = "${local.name_prefix}-app-${count.index + 1}"
      Index = count.index + 1
    }
  )
}

resource "aws_db_instance" "main" {
  count = var.create_database ? 1 : 0
  
  identifier          = "${local.name_prefix}-db"
  engine              = var.database_config.engine
  engine_version      = var.database_config.engine_version
  instance_class      = var.database_config.instance_class
  allocated_storage   = var.database_config.allocated_storage
  multi_az            = var.database_config.multi_az
  backup_retention_period = var.database_config.backup_retention
  
  username = "admin"
  password = var.database_password
  
  skip_final_snapshot = var.environment != "prod"
  
  tags = merge(
    local.all_tags,
    {
      Name = "${local.name_prefix}-db"
    }
  )
}
```

**Using this setup:**

```bash
# Development
terraform apply

# Staging
terraform apply -var="environment=staging"

# Production
terraform apply -var-file="prod.tfvars"

# With password from environment
export TF_VAR_database_password="super-secret-password"
terraform apply -var-file="prod.tfvars"
```

---

### ✅ Day 6 Checklist

- [x] All variable types
- [x] Variable declaration syntax
- [x] All methods to set variable values
- [x] Variable precedence
- [x] Variable validation
- [x] Sensitive variables
- [x] Real-world variable organization

**Next:** Outputs - Extracting information!

---

## Day 7: Outputs & Data Sources

### 🎯 Learning Objectives
- Extract and display information with outputs
- Query existing infrastructure with data sources
- Share data between configurations
- Use outputs in modules

---

### 📤 Output Values

Outputs extract information from your Terraform configuration to:
- Display after `terraform apply`
- Pass to other Terraform configurations
- Use in automation scripts
- Share between modules

#### **Basic Output Syntax**

```hcl
output "output_name" {
  description = "What this output represents"
  value       = expression_to_output
  sensitive   = false  # Optional
  depends_on  = []     # Optional
}
```

---

### 🎨 Output Examples

#### **Simple Outputs**

```hcl
# File: outputs.tf

# Single value
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

# Computed attribute
output "instance_public_ip" {
  description = "Public IP address of the instance"
  value       = aws_instance.web.public_ip
}

# Using locals
locals {
  environment = "production"
}

output "environment" {
  description = "Current environment"
  value       = local.environment
}

# Conditional output
output "database_endpoint" {
  description = "Database endpoint (if created)"
  value       = var.create_database ? aws_db_instance.main[0].endpoint : "No database"
}
```

---

#### **List Outputs**

```hcl
# All instance IDs
output "instance_ids" {
  description = "IDs of all instances"
  value       = aws_instance.web[*].id
  # Result: ["i-1234567890abcdef0", "i-0fedcba0987654321"]
}

# All private IPs
output "private_ips" {
  description = "Private IP addresses"
  value       = aws_instance.web[*].private_ip
  # Result: ["10.0.1.10", "10.0.1.11", "10.0.1.12"]
}

# Subnet IDs
output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}
```

---

#### **Map Outputs**

```hcl
# With for_each - creates map
resource "aws_instance" "servers" {
  for_each = toset(["web", "api", "worker"])
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "${each.key}-server"
  }
}

# Output as map
output "server_ips" {
  description = "Map of server names to IP addresses"
  value = {
    for key, instance in aws_instance.servers :
    key => instance.private_ip
  }
  # Result: {
  #   web    = "10.0.1.10"
  #   api    = "10.0.1.11"
  #   worker = "10.0.1.12"
  # }
}

# Specific keys
output "web_server_ip" {
  description = "Web server IP"
  value       = aws_instance.servers["web"].private_ip
}
```

---

#### **Complex Outputs**

```hcl
# Object output
output "database_info" {
  description = "Complete database information"
  value = {
    endpoint           = aws_db_instance.main.endpoint
    port               = aws_db_instance.main.port
    database_name      = aws_db_instance.main.db_name
    connection_string  = "mysql://${aws_db_instance.main.endpoint}/${aws_db_instance.main.db_name}"
  }
}

# Nested output
output "infrastructure_summary" {
  description = "Complete infrastructure summary"
  value = {
    vpc = {
      id         = aws_vpc.main.id
      cidr_block = aws_vpc.main.cidr_block
      region     = var.region
    }
    instances = {
      count      = length(aws_instance.web)
      ids        = aws_instance.web[*].id
      public_ips = aws_instance.web[*].public_ip
    }
    database = var.create_database ? {
      endpoint = aws_db_instance.main[0].endpoint
      port     = aws_db_instance.main[0].port
    } : null
  }
}

# Transformed output
output "instance_details" {
  description = "Detailed instance information"
  value = [
    for i, instance in aws_instance.web : {
      index      = i + 1
      id         = instance.id
      public_ip  = instance.public_ip
      private_ip = instance.private_ip
      az         = instance.availability_zone
      url        = "http://${instance.public_ip}"
    }
  ]
}
```

---

#### **Sensitive Outputs**

```hcl
# Hide sensitive data
output "database_password" {
  description = "Database admin password"
  value       = aws_db_instance.main.password
  sensitive   = true  # Won't show in console
}

output "api_key" {
  description = "API key for external service"
  value       = random_password.api_key.result
  sensitive   = true
}

# When you run terraform apply:
# Outputs:
#
# database_password = <sensitive>
# api_key = <sensitive>

# To see the value:
terraform output database_password
# or
terraform output -json
```

---

#### **Outputs with Dependencies**

```hcl
# Explicit dependency
output "instance_ready" {
  description = "Message when instance is ready"
  value       = "Instance ${aws_instance.web.id} is ready"
  
  depends_on = [
    aws_instance.web,
    aws_eip.web,
    aws_security_group.web
  ]
}
```

---

### 📥 Using Outputs

#### **1. View Outputs After Apply**

```bash
# During terraform apply
terraform apply

# Outputs:
#
# instance_ip = "54.123.45.67"
# vpc_id = "vpc-1234567890abcdef0"
```

#### **2. Query Specific Output**

```bash
# Get specific output
terraform output instance_ip
# 54.123.45.67

# Get as JSON
terraform output -json instance_ip
# "54.123.45.67"

# Get all outputs
terraform output

# Get all outputs as JSON
terraform output -json
```

#### **3. Use in Shell Scripts**

```bash
#!/bin/bash

# Get output value
INSTANCE_IP=$(terraform output -raw instance_ip)

# Use it
echo "Connecting to $INSTANCE_IP"
ssh ec2-user@$INSTANCE_IP

# Get JSON output
DATABASE_INFO=$(terraform output -json database_info)
ENDPOINT=$(echo $DATABASE_INFO | jq -r '.endpoint')

echo "Database endpoint: $ENDPOINT"
```

#### **4. Pass to Another Terraform Configuration**

```hcl
# Configuration A: outputs.tf
output "vpc_id" {
  value = aws_vpc.main.id
}

output "subnet_ids" {
  value = aws_subnet.private[*].id
}
```

```hcl
# Configuration B: data.tf
data "terraform_remote_state" "vpc" {
  backend = "s3"
  
  config = {
    bucket = "my-terraform-state"
    key    = "vpc/terraform.tfstate"
    region = "us-east-1"
  }
}

# Use outputs from Configuration A
resource "aws_instance" "app" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  subnet_id     = data.terraform_remote_state.vpc.outputs.subnet_ids[0]
  
  tags = {
    VPC = data.terraform_remote_state.vpc.outputs.vpc_id
  }
}
```

---

### 📊 Data Sources

Data sources **query** existing infrastructure (not managed by Terraform):
- AWS AMIs
- Existing VPCs
- Route53 zones
- IAM policies
- Any resource created outside Terraform

#### **Data Source Syntax**

```hcl
data "provider_datasource" "name" {
  # Filter/query arguments
  argument1 = "value1"
  argument2 = "value2"
}

# Reference: data.provider_datasource.name.attribute
```

---

### 🔍 Common Data Sources

#### **AWS AMI (Latest Amazon Linux)**

```hcl
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
  
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Use in resource
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
}

# Output AMI details
output "ami_info" {
  value = {
    id           = data.aws_ami.amazon_linux_2.id
    name         = data.aws_ami.amazon_linux_2.name
    architecture = data.aws_ami.amazon_linux_2.architecture
    creation_date = data.aws_ami.amazon_linux_2.creation_date
  }
}
```

#### **Latest Ubuntu AMI**

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "ubuntu_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
}
```

---

#### **Existing VPC**

```hcl
# Query VPC by tag
data "aws_vpc" "existing" {
  tags = {
    Name = "production-vpc"
  }
}

# Query default VPC
data "aws_vpc" "default" {
  default = true
}

# Use VPC ID
resource "aws_subnet" "new_subnet" {
  vpc_id     = data.aws_vpc.existing.id
  cidr_block = "10.0.100.0/24"
}

output "existing_vpc_info" {
  value = {
    id         = data.aws_vpc.existing.id
    cidr_block = data.aws_vpc.existing.cidr_block
  }
}
```

---

#### **Availability Zones**

```hcl
# Get all available AZs in current region
data "aws_availability_zones" "available" {
  state = "available"
}

# Use in resources
resource "aws_subnet" "public" {
  count = length(data.aws_availability_zones.available.names)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

output "available_azs" {
  value = data.aws_availability_zones.available.names
  # ["us-east-1a", "us-east-1b", "us-east-1c", ...]
}
```

---

#### **AWS Account Information**

```hcl
data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

output "account_info" {
  value = {
    account_id = data.aws_caller_identity.current.account_id
    caller_arn = data.aws_caller_identity.current.arn
    user_id    = data.aws_caller_identity.current.user_id
    region     = data.aws_region.current.name
  }
}

# Use in resource naming
resource "aws_s3_bucket" "logs" {
  bucket = "logs-${data.aws_caller_identity.current.account_id}-${data.aws_region.current.name}"
}
```

---

#### **IAM Policy Document**

```hcl
# Create IAM policy using data source
data "aws_iam_policy_document" "s3_read_access" {
  statement {
    effect = "Allow"
    
    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]
    
    resources = [
      "arn:aws:s3:::my-bucket",
      "arn:aws:s3:::my-bucket/*",
    ]
  }
  
  statement {
    effect = "Allow"
    
    actions = [
      "s3:PutObject",
    ]
    
    resources = [
      "arn:aws:s3:::my-bucket/uploads/*",
    ]
  }
}

# Use in IAM policy
resource "aws_iam_policy" "s3_access" {
  name   = "s3-access-policy"
  policy = data.aws_iam_policy_document.s3_read_access.json
}

output "policy_json" {
  value = data.aws_iam_policy_document.s3_read_access.json
}
```

---

#### **Route53 Zone**

```hcl
# Query hosted zone
data "aws_route53_zone" "main" {
  name         = "example.com"
  private_zone = false
}

# Create DNS record
resource "aws_route53_record" "www" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "www.${data.aws_route53_zone.main.name}"
  type    = "A"
  ttl     = 300
  records = [aws_instance.web.public_ip]
}
```

---

#### **Subnet IDs**

```hcl
# Get subnets by filter
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.existing.id]
  }
  
  tags = {
    Type = "private"
  }
}

# Use subnet IDs
resource "aws_db_subnet_group" "main" {
  name       = "main-db-subnet-group"
  subnet_ids = data.aws_subnets.private.ids
}

output "private_subnet_ids" {
  value = data.aws_subnets.private.ids
}
```

---

#### **Security Group**

```hcl
# Query existing security group
data "aws_security_group" "default" {
  vpc_id = data.aws_vpc.default.id
  
  filter {
    name   = "group-name"
    values = ["default"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  vpc_security_group_ids = [data.aws_security_group.default.id]
}
```

---

#### **S3 Bucket**

```hcl
# Query existing bucket
data "aws_s3_bucket" "logs" {
  bucket = "my-logs-bucket"
}

output "bucket_info" {
  value = {
    arn           = data.aws_s3_bucket.logs.arn
    region        = data.aws_s3_bucket.logs.region
    hosted_zone_id = data.aws_s3_bucket.logs.hosted_zone_id
  }
}
```

---

### 🎓 Real-World Example: Complete Setup

```hcl
# ==================================================
# File: data.tf
# ==================================================

# Get current AWS account and region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# Get all available AZs
data "aws_availability_zones" "available" {
  state = "available"
}

# Get latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
  
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Get existing VPC (if using existing)
data "aws_vpc" "existing" {
  count = var.use_existing_vpc ? 1 : 0
  
  tags = {
    Name = var.existing_vpc_name
  }
}

# IAM policy for EC2 to access S3
data "aws_iam_policy_document" "ec2_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "s3_access" {
  statement {
    effect = "Allow"
    
    actions = [
      "s3:GetObject",
      "s3:ListBucket",
    ]
    
    resources = [
      "arn:aws:s3:::${var.s3_bucket_name}",
      "arn:aws:s3:::${var.s3_bucket_name}/*",
    ]
  }
}

# ==================================================
# File: main.tf
# ==================================================

locals {
  vpc_id = var.use_existing_vpc ? data.aws_vpc.existing[0].id : aws_vpc.main[0].id
  
  az_names = slice(
    data.aws_availability_zones.available.names,
    0,
    min(var.az_count, length(data.aws_availability_zones.available.names))
  )
  
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
    AccountID   = data.aws_caller_identity.current.account_id
    Region      = data.aws_region.current.name
  }
}

# Create VPC (if not using existing)
resource "aws_vpc" "main" {
  count = var.use_existing_vpc ? 0 : 1
  
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-vpc"
    }
  )
}

# Create subnets in each AZ
resource "aws_subnet" "public" {
  count = length(local.az_names)
  
  vpc_id                  = local.vpc_id
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone       = local.az_names[count.index]
  map_public_ip_on_launch = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-public-${local.az_names[count.index]}"
      Type = "public"
    }
  )
}

# IAM role for EC2
resource "aws_iam_role" "ec2_role" {
  name               = "${var.project_name}-ec2-role"
  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json
  
  tags = local.common_tags
}

resource "aws_iam_role_policy" "s3_access" {
  name   = "s3-access"
  role   = aws_iam_role.ec2_role.id
  policy = data.aws_iam_policy_document.s3_access.json
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "${var.project_name}-ec2-profile"
  role = aws_iam_role.ec2_role.name
  
  depends_on = [aws_iam_role_policy.s3_access]
}

# EC2 instances using latest AMI
resource "aws_instance" "web" {
  count = var.instance_count
  
  ami                  = data.aws_ami.amazon_linux_2.id
  instance_type        = var.instance_type
  subnet_id            = aws_subnet.public[count.index % length(aws_subnet.public)].id
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name
  
  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    
    # Instance info page
    cat > /var/www/html/index.html <<HTML
    <h1>Server Info</h1>
    <ul>
      <li>Instance ID: $(ec2-metadata --instance-id | cut -d' ' -f2)</li>
      <li>AZ: $(ec2-metadata --availability-zone | cut -d' ' -f2)</li>
      <li>Region: ${data.aws_region.current.name}</li>
      <li>Account: ${data.aws_caller_identity.current.account_id}</li>
    </ul>
    HTML
  EOF
  
  tags = merge(
    local.common_tags,
    {
      Name  = "${var.project_name}-web-${count.index + 1}"
      Index = count.index + 1
    }
  )
}

# ==================================================
# File: outputs.tf
# ==================================================

# Account & Region Info
output "account_id" {
  description = "AWS Account ID"
  value       = data.aws_caller_identity.current.account_id
}

output "region" {
  description = "AWS Region"
  value       = data.aws_region.current.name
}

output "availability_zones" {
  description = "Available AZs used"
  value       = local.az_names
}

# AMI Info
output "ami_id" {
  description = "AMI ID used for instances"
  value       = data.aws_ami.amazon_linux_2.id
}

output "ami_name" {
  description = "AMI name"
  value       = data.aws_ami.amazon_linux_2.name
}

# VPC Info
output "vpc_id" {
  description = "VPC ID"
  value       = local.vpc_id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = var.use_existing_vpc ? data.aws_vpc.existing[0].cidr_block : aws_vpc.main[0].cidr_block
}

# Subnet Info
output "subnet_ids" {
  description = "List of subnet IDs"
  value       = aws_subnet.public[*].id
}

output "subnet_cidrs" {
  description = "List of subnet CIDR blocks"
  value       = aws_subnet.public[*].cidr_block
}

# Instance Info
output "instance_ids" {
  description = "List of instance IDs"
  value       = aws_instance.web[*].id
}

output "instance_public_ips" {
  description = "List of public IP addresses"
  value       = aws_instance.web[*].public_ip
}

output "instance_private_ips" {
  description = "List of private IP addresses"
  value       = aws_instance.web[*].private_ip
}

# Detailed instance info
output "instances_detail" {
  description = "Detailed information about all instances"
  value = [
    for i, instance in aws_instance.web : {
      index      = i + 1
      id         = instance.id
      public_ip  = instance.public_ip
      private_ip = instance.private_ip
      az         = instance.availability_zone
      subnet_id  = instance.subnet_id
      url        = "http://${instance.public_ip}"
    }
  ]
}

# IAM Info
output "iam_role_arn" {
  description = "ARN of IAM role"
  value       = aws_iam_role.ec2_role.arn
}

# Summary
output "infrastructure_summary" {
  description = "Complete infrastructure summary"
  value = {
    account = {
      id     = data.aws_caller_identity.current.account_id
      region = data.aws_region.current.name
    }
    network = {
      vpc_id       = local.vpc_id
      vpc_cidr     = var.use_existing_vpc ? data.aws_vpc.existing[0].cidr_block : aws_vpc.main[0].cidr_block
      subnet_count = length(aws_subnet.public)
      azs          = local.az_names
    }
    compute = {
      instance_count = length(aws_instance.web)
      ami_id         = data.aws_ami.amazon_linux_2.id
      instance_type  = var.instance_type
    }
  }
}

# Connection string for SSH
output "ssh_commands" {
  description = "SSH commands to connect to instances"
  value = [
    for instance in aws_instance.web :
    "ssh -i ~/.ssh/your-key.pem ec2-user@${instance.public_ip}"
  ]
}

# URLs to access web servers
output "web_urls" {
  description = "URLs to access web servers"
  value = [
    for instance in aws_instance.web :
    "http://${instance.public_ip}"
  ]
}
```

**Usage:**

```bash
# Apply configuration
terraform apply

# View specific output
terraform output instance_public_ips

# Get as JSON
terraform output -json infrastructure_summary | jq

# Use in script
INSTANCE_IP=$(terraform output -raw instance_public_ips | jq -r '.[0]')
curl http://$INSTANCE_IP

# SSH to first instance
eval $(terraform output ssh_commands | jq -r '.[0]')
```

---

### ✅ Day 7 Checklist

- [x] Output syntax and types
- [x] Simple, list, map, and complex outputs
- [x] Sensitive outputs
- [x] Using outputs in automation
- [x] Data source syntax
- [x] Common data sources (AMI, VPC, IAM, etc.)
- [x] Querying existing infrastructure
- [x] Complete real-world example

**Next:** Advanced features - count, for_each, dynamic blocks!

---

## Day 8-9: Advanced Iteration & Dynamic Blocks

### 🎯 Learning Objectives
- Master count vs for_each
- Create dynamic resource blocks
- Use for expressions
- Implement conditional logic
- Build flexible configurations

---

### 🔢 Count vs For_Each - Deep Dive

#### **When to Use Count**

✅ **Use count when:**
- Creating identical resources
- Simple duplication
- Resources are interchangeable
- Order doesn't matter long-term

```hcl
# Example: Create 5 identical servers
resource "aws_instance" "web" {
  count = 5
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "web-server-${count.index + 1}"
  }
}

# Accessing resources
output "first_instance" {
  value = aws_instance.web[0].id
}

output "all_instances" {
  value = aws_instance.web[*].id
}
```

**❌ Problem with count:**
```hcl
# Initial: 3 instances
variable "servers" {
  default = ["web1", "web2", "web3"]
}

resource "aws_instance" "server" {
  count = length(var.servers)
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = var.servers[count.index]
  }
}

# Result: 
# [0] = web1
# [1] = web2
# [2] = web3

# Now remove web2
variable "servers" {
  default = ["web1", "web3"]  # Removed web2
}

# Terraform will:
# [0] = web1 (no change)
# [1] = web3 (RECREATE! was web2)
# [2] = DELETE web3

# 😱 web3 gets destroyed and recreated!
```

---

#### **When to Use For_Each**

✅ **Use for_each when:**
- Resources have unique identifiers
- Adding/removing resources shouldn't affect others
- Resources have different configurations
- Stability is important

```hcl
# Example: Named servers
variable "servers" {
  type = set(string)
  default = ["web1", "web2", "web3"]
}

resource "aws_instance" "server" {
  for_each = var.servers
  
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = each.key
  }
}

# Result:
# server["web1"]
# server["web2"]
# server["web3"]

# Now remove web2
variable "servers" {
  default = ["web1", "web3"]
}

# Terraform will:
# server["web1"] - no change
# server["web3"] - no change
# server["web2"] - DELETE only web2
# ✅ web3 is untouched!
```

---

### 🎨 Advanced For_Each Patterns

#### **1. From Map with Different Configurations**

```hcl
variable "instances" {
  type = map(object({
    instance_type = string
    ami           = string
    volume_size   = number
    monitoring    = bool
  }))
  
  default = {
    web = {
      instance_type = "t3.medium"
      ami           = "ami-12345"
      volume_size   = 50
      monitoring    = true
    }
    api = {
      instance_type = "t3.small"
      ami           = "ami-12345"
      volume_size   = 30
      monitoring    = true
    }
    worker = {
      instance_type = "t3.micro"
      ami           = "ami-67890"
      volume_size   = 20
      monitoring    = false
    }
  }
}

resource "aws_instance" "servers" {
  for_each = var.instances
  
  ami           = each.value.ami
  instance_type = each.value.instance_type
  monitoring    = each.value.monitoring
  
  root_block_device {
    volume_size = each.value.volume_size
  }
  
  tags = {
    Name = "${each.key}-server"
    Role = each.key
  }
}

# Access specific server
output "web_server_ip" {
  value = aws_instance.servers["web"].private_ip
}

# Access all servers
output "all_server_ips" {
  value = {
    for key, instance in aws_instance.servers :
    key => instance.private_ip
  }
}
```

---

#### **2. Create Subnets Across AZs**

```hcl
variable "availability_zones" {
  type = map(object({
    cidr_block = string
    public     = bool
  }))
  
  default = {
    "us-east-1a" = {
      cidr_block = "10.0.1.0/24"
      public     = true
    }
    "us-east-1b" = {
      cidr_block = "10.0.2.0/24"
      public     = true
    }
    "us-east-1c" = {
      cidr_block = "10.0.11.0/24"
      public     = false
    }
  }
}

resource "aws_subnet" "main" {
  for_each = var.availability_zones
  
  vpc_id                  = aws_vpc.main.id
  availability_zone       = each.key
  cidr_block              = each.value.cidr_block
  map_public_ip_on_launch = each.value.public
  
  tags = {
    Name = "subnet-${each.key}"
    Type = each.value.public ? "public" : "private"
  }
}

# Create route table association for public subnets only
resource "aws_route_table_association" "public" {
  for_each = {
    for az, config in var.availability_zones :
    az => config if config.public
  }
  
  subnet_id      = aws_subnet.main[each.key].id
  route_table_id = aws_route_table.public.id
}
```

---

#### **3. IAM Users with Different Policies**

```hcl
variable "users" {
  type = map(object({
    policies = list(string)
    groups   = list(string)
  }))
  
  default = {
    "john.doe" = {
      policies = ["arn:aws:iam::aws:policy/PowerUserAccess"]
      groups   = ["developers", "admins"]
    }
    "jane.smith" = {
      policies = ["arn:aws:iam::aws:policy/ReadOnlyAccess"]
      groups   = ["developers"]
    }
    "bob.wilson" = {
      policies = [
        "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
        "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
      ]
      groups = ["viewers"]
    }
  }
}

# Create IAM users
resource "aws_iam_user" "users" {
  for_each = var.users
  name     = each.key
  
  tags = {
    Email = "${replace(each.key, ".", "_")}@company.com"
  }
}

# Attach policies to users
resource "aws_iam_user_policy_attachment" "user_policies" {
  for_each = merge([
    for username, user in var.users : {
      for policy in user.policies :
      "${username}-${basename(policy)}" => {
        user   = username
        policy = policy
      }
    }
  ]...)
  
  user       = aws_iam_user.users[each.value.user].name
  policy_arn = each.value.policy
}

# Add users to groups
resource "aws_iam_user_group_membership" "users" {
  for_each = var.users
  
  user   = aws_iam_user.users[each.key].name
  groups = each.value.groups
}
```

---

### 🔄 For Expressions

Transform collections:

#### **List to List**

```hcl
variable "names" {
  default = ["alice", "bob", "charlie"]
}

locals {
  # Uppercase names
  upper_names = [
    for name in var.names :
    upper(name)
  ]
  # Result: ["ALICE", "BOB", "CHARLIE"]
  
  # Add prefix
  prefixed_names = [
    for name in var.names :
    "user-${name}"
  ]
  # Result: ["user-alice", "user-bob", "user-charlie"]
  
  # Conditional filtering
  long_names = [
    for name in var.names :
    name if length(name) > 4
  ]
  # Result: ["alice", "charlie"]
  
  # Transform objects
  name_lengths = [
    for name in var.names :
    {
      name   = name
      length = length(name)
    }
  ]
  # Result: [
  #   {name = "alice", length = 5},
  #   {name = "bob", length = 3},
  #   {name = "charlie", length = 7}
  # ]
}
```

---

#### **Map to Map**

```hcl
variable "instances" {
  default = {
    web    = "t3.large"
    api    = "t3.medium"
    worker = "t3.small"
  }
}

locals {
  # Transform values
  instance_costs = {
    for name, type in var.instances :
    name => "${type}-cost-optimized"
  }
  # Result: {
  #   web    = "t3.large-cost-optimized"
  #   api    = "t3.medium-cost-optimized"
  #   worker = "t3.small-cost-optimized"
  # }
  
  # Filter map
  large_instances = {
    for name, type in var.instances :
    name => type if can(regex("large", type))
  }
  # Result: {web = "t3.large"}
  
  # Swap key/value
  type_to_name = {
    for name, type in var.instances :
    type => name
  }
  # Result: {
  #   "t3.large"  = "web"
  #   "t3.medium" = "api"
  #   "t3.small"  = "worker"
  # }
}
```

---

#### **List to Map**

```hcl
variable "server_names" {
  default = ["web-1", "web-2", "api-1"]
}

locals {
  # Create map with index
  server_map = {
    for idx, name in var.server_names :
    name => idx
  }
  # Result: {
  #   "web-1" = 0
  #   "web-2" = 1
  #   "api-1" = 2
  # }
  
  # Create map with derived key
  server_config = {
    for name in var.server_names :
    name => {
      type = split("-", name)[0]
      index = split("-", name)[1]
    }
  }
  # Result: {
  #   "web-1" = {type = "web", index = "1"}
  #   "web-2" = {type = "web", index = "2"}
  #   "api-1" = {type = "api", index = "1"}
  # }
}
```

---

#### **Nested For Expressions**

```hcl
variable "vpcs" {
  default = {
    prod = {
      cidr = "10.0.0.0/16"
      azs  = ["us-east-1a", "us-east-1b", "us-east-1c"]
    }
    dev = {
      cidr = "10.1.0.0/16"
      azs  = ["us-east-1a", "us-east-1b"]
    }
  }
}

locals {
  # Flatten nested structure
  all_subnets = flatten([
    for vpc_name, vpc in var.vpcs : [
      for idx, az in vpc.azs : {
        vpc_name = vpc_name
        az       = az
        cidr     = cidrsubnet(vpc.cidr, 8, idx)
      }
    ]
  ])
  # Result: [
  #   {vpc_name = "prod", az = "us-east-1a", cidr = "10.0.0.0/24"},
  #   {vpc_name = "prod", az = "us-east-1b", cidr = "10.0.1.0/24"},
  #   ...
  # ]
  
  # Create subnet map
  subnets = {
    for subnet in local.all_subnets :
    "${subnet.vpc_name}-${subnet.az}" => subnet
  }
}

# Create all subnets
resource "aws_subnet" "all" {
  for_each = local.subnets
  
  vpc_id            = aws_vpc.main[each.value.vpc_name].id
  availability_zone = each.value.az
  cidr_block        = each.value.cidr
  
  tags = {
    Name = each.key
  }
}
```

---

### 🎭 Dynamic Blocks

Create repeating nested blocks dynamically:

#### **Basic Dynamic Block**

```hcl
# Without dynamic block (repetitive)
resource "aws_security_group" "web" {
  name = "web-sg"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.0/24"]
  }
}

# With dynamic block (clean!)
variable "ingress_rules" {
  type = list(object({
    port        = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))
  
  default = [
    {
      port        = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTP"
    },
    {
      port        = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTPS"
    },
    {
      port        = 22
      protocol    = "tcp"
      cidr_blocks = ["203.0.113.0/24"]
      description = "SSH"
    }
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"
  
  dynamic "ingress" {
    for_each = var.ingress_rules
    
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
      description = ingress.value.description
    }
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

**Dynamic block anatomy:**
```hcl
dynamic "BLOCK_NAME" {
  for_each = COLLECTION
  iterator = OPTIONAL_NAME  # defaults to block name
  
  content {
    # Block configuration using:
    # BLOCK_NAME.value or ITERATOR_NAME.value
    # BLOCK_NAME.key or ITERATOR_NAME.key
  }
}
```

---

#### **Advanced Dynamic Block Patterns**

**1. Security Groups with Port Ranges**

```hcl
variable "security_rules" {
  default = {
    http = {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    https = {
      from_port   = 443
      to_port     = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
    ssh = {
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["10.0.0.0/8"]
    }
    ephemeral = {
      from_port   = 1024
      to_port     = 65535
      protocol    = "tcp"
      cidr_blocks = ["10.0.0.0/8"]
    }
  }
}

resource "aws_security_group" "app" {
  name = "app-sg"
  
  dynamic "ingress" {
    for_each = var.security_rules
    iterator = rule
    
    content {
      description = rule.key
      from_port   = rule.value.from_port
      to_port     = rule.value.to_port
      protocol    = rule.value.protocol
      cidr_blocks = rule.value.cidr_blocks
    }
  }
}
```

---

**2. RDS with Optional Features**

```hcl
variable "database_config" {
  type = object({
    engine               = string
    instance_class       = string
    allocated_storage    = number
    backup_retention     = number
    multi_az             = bool
    storage_encrypted    = bool
    performance_insights = optional(bool, false)
    replicas             = optional(number, 0)
  })
}

variable "restore_config" {
  type = object({
    enabled         = bool
    snapshot_id     = optional(string)
    restore_time    = optional(string)
  })
  default = {
    enabled = false
  }
}

resource "aws_db_instance" "main" {
  identifier     = "main-db"
  engine         = var.database_config.engine
  instance_class = var.database_config.instance_class
  
  allocated_storage = var.database_config.allocated_storage
  storage_encrypted = var.database_config.storage_encrypted
  
  multi_az                = var.database_config.multi_az
  backup_retention_period = var.database_config.backup_retention
  
  # Dynamic block for performance insights
  dynamic "performance_insights" {
    for_each = var.database_config.performance_insights ? [1] : []
    
    content {
      enabled          = true
      retention_period = 7
    }
  }
  
  # Dynamic restore configuration
  dynamic "restore_to_point_in_time" {
    for_each = var.restore_config.enabled ? [var.restore_config] : []
    
    content {
      source_db_instance_identifier = restore_to_point_in_time.value.snapshot_id
      restore_time                  = restore_to_point_in_time.value.restore_time
    }
  }
}

# Read replicas
resource "aws_db_instance" "replica" {
  count = var.database_config.replicas
  
  identifier          = "main-db-replica-${count.index + 1}"
  replicate_source_db = aws_db_instance.main.identifier
  instance_class      = var.database_config.instance_class
  
  tags = {
    Name = "replica-${count.index + 1}"
  }
}
```

---

**3. EC2 with Conditional Block Device Mappings**

```hcl
variable "instance_config" {
  type = object({
    instance_type = string
    root_volume = object({
      size = number
      type = string
    })
    additional_volumes = list(object({
      device_name = string
      size        = number
      type        = string
      encrypted   = bool
    }))
  })
  
  default = {
    instance_type = "t3.medium"
    root_volume = {
      size = 30
      type = "gp3"
    }
    additional_volumes = [
      {
        device_name = "/dev/sdf"
        size        = 100
        type        = "gp3"
        encrypted   = true
      },
      {
        device_name = "/dev/sdg"
        size        = 200
        type        = "io2"
        encrypted   = true
      }
    ]
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_config.instance_type
  
  root_block_device {
    volume_size = var.instance_config.root_volume.size
    volume_type = var.instance_config.root_volume.type
    encrypted   = true
  }
  
  dynamic "ebs_block_device" {
    for_each = var.instance_config.additional_volumes
    iterator = volume
    
    content {
      device_name           = volume.value.device_name
      volume_size           = volume.value.size
      volume_type           = volume.value.type
      encrypted             = volume.value.encrypted
      delete_on_termination = true
    }
  }
}
```

---

**4. Nested Dynamic Blocks**

```hcl
variable "load_balancers" {
  type = map(object({
    internal = bool
    listeners = list(object({
      port     = number
      protocol = string
      rules = list(object({
        priority = number
        path     = string
        target   = string
      }))
    }))
  }))
  
  default = {
    public = {
      internal = false
      listeners = [
        {
          port     = 80
          protocol = "HTTP"
          rules = [
            {
              priority = 1
              path     = "/api/*"
              target   = "api"
            },
            {
              priority = 2
              path     = "/*"
              target   = "web"
            }
          ]
        },
        {
          port     = 443
          protocol = "HTTPS"
          rules = [
            {
              priority = 1
              path     = "/api/*"
              target   = "api"
            }
          ]
        }
      ]
    }
  }
}

resource "aws_lb" "main" {
  for_each = var.load_balancers
  
  name               = "${each.key}-lb"
  internal           = each.value.internal
  load_balancer_type = "application"
  subnets            = aws_subnet.public[*].id
}

resource "aws_lb_listener" "main" {
  for_each = merge([
    for lb_name, lb in var.load_balancers : {
      for listener in lb.listeners :
      "${lb_name}-${listener.port}" => {
        lb_name  = lb_name
        port     = listener.port
        protocol = listener.protocol
        rules    = listener.rules
      }
    }
  ]...)
  
  load_balancer_arn = aws_lb.main[each.value.lb_name].arn
  port              = each.value.port
  protocol          = each.value.protocol
  
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.main["${each.value.lb_name}-web"].arn
  }
}

resource "aws_lb_listener_rule" "main" {
  for_each = merge(flatten([
    for lb_name, lb in var.load_balancers : [
      for listener in lb.listeners : [
        for rule in listener.rules : {
          "${lb_name}-${listener.port}-${rule.priority}" = {
            listener_key = "${lb_name}-${listener.port}"
            priority     = rule.priority
            path         = rule.path
            target       = rule.target
            lb_name      = lb_name
          }
        }
      ]
    ]
  ])...)
  
  listener_arn = aws_lb_listener.main[each.value.listener_key].arn
  priority     = each.value.priority
  
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.main["${each.value.lb_name}-${each.value.target}"].arn
  }
  
  condition {
    path_pattern {
      values = [each.value.path]
    }
  }
}
```

---

### 🎓 Real-World Complete Example

```hcl
# ==================================================
# File: variables.tf
# ==================================================

variable "project_name" {
  type = string
}

variable "environment" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "vpc_config" {
  type = object({
    cidr_block         = string
    availability_zones = list(string)
    public_subnets     = list(string)
    private_subnets    = list(string)
  })
}

variable "security_groups" {
  type = map(object({
    description = string
    ingress_rules = list(object({
      from_port   = number
      to_port     = number
      protocol    = string
      cidr_blocks = list(string)
      description = string
    }))
  }))
}

variable "instances" {
  type = map(object({
    count         = number
    instance_type = string
    security_groups = list(string)
    user_data     = optional(string, "")
    volumes = optional(list(object({
      device_name = string
      size        = number
      type        = string
    })), [])
  }))
}

variable "load_balancer" {
  type = object({
    enabled  = bool
    internal = bool
    targets = map(object({
      port              = number
      health_check_path = string
      instances         = list(string)
    }))
  })
}

# ==================================================
# File: terraform.tfvars
# ==================================================

project_name = "webapp"
environment  = "prod"

vpc_config = {
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnets    = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
}

security_groups = {
  web = {
    description = "Security group for web servers"
    ingress_rules = [
      {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "HTTP from anywhere"
      },
      {
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
        description = "HTTPS from anywhere"
      }
    ]
  }
  
  app = {
    description = "Security group for app servers"
    ingress_rules = [
      {
        from_port   = 8080
        to_port     = 8080
        protocol    = "tcp"
        cidr_blocks = ["10.0.0.0/16"]
        description = "App port from VPC"
      }
    ]
  }
  
  db = {
    description = "Security group for database"
    ingress_rules = [
      {
        from_port   = 3306
        to_port     = 3306
        protocol    = "tcp"
        cidr_blocks = ["10.0.0.0/16"]
        description = "MySQL from VPC"
      }
    ]
  }
}

instances = {
  web = {
    count           = 3
    instance_type   = "t3.medium"
    security_groups = ["web"]
    user_data       = <<-EOF
      #!/bin/bash
      yum install -y httpd
      systemctl start httpd
    EOF
    volumes = [
      {
        device_name = "/dev/sdf"
        size        = 50
        type        = "gp3"
      }
    ]
  }
  
  app = {
    count           = 2
    instance_type   = "t3.large"
    security_groups = ["app"]
    volumes = []
  }
}

load_balancer = {
  enabled  = true
  internal = false
  targets = {
    web = {
      port              = 80
      health_check_path = "/health"
      instances         = ["web"]
    }
    app = {
      port              = 8080
      health_check_path = "/api/health"
      instances         = ["app"]
    }
  }
}

# ==================================================
# File: main.tf
# ==================================================

# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_config.cidr_block
  enable_dns_hostnames = true
  
  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count = length(var.vpc_config.public_subnets)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.vpc_config.public_subnets[count.index]
  availability_zone       = var.vpc_config.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-${var.vpc_config.availability_zones[count.index]}"
    Type = "public"
  }
}

# Private Subnets
resource "aws_subnet" "private" {
  count = length(var.vpc_config.private_subnets)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.vpc_config.private_subnets[count.index]
  availability_zone = var.vpc_config.availability_zones[count.index]
  
  tags = {
    Name = "${var.project_name}-private-${var.vpc_config.availability_zones[count.index]}"
    Type = "private"
  }
}

# Security Groups with Dynamic Ingress Rules
resource "aws_security_group" "main" {
  for_each = var.security_groups
  
  name        = "${var.project_name}-${each.key}-sg"
  description = each.value.description
  vpc_id      = aws_vpc.main.id
  
  dynamic "ingress" {
    for_each = each.value.ingress_rules
    
    content {
      description = ingress.value.description
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-${each.key}-sg"
  }
}

# EC2 Instances with Dynamic Configuration
locals {
  # Flatten instance configuration
  instances_flat = flatten([
    for role, config in var.instances : [
      for i in range(config.count) : {
        key             = "${role}-${i}"
        role            = role
        instance_type   = config.instance_type
        security_groups = [for sg in config.security_groups : aws_security_group.main[sg].id]
        user_data       = config.user_data
        volumes         = config.volumes
        subnet_id       = aws_subnet.public[i % length(aws_subnet.public)].id
      }
    ]
  ])
  
  instances_map = {
    for inst in local.instances_flat :
    inst.key => inst
  }
}

resource "aws_instance" "main" {
  for_each = local.instances_map
  
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = each.value.instance_type
  subnet_id              = each.value.subnet_id
  vpc_security_group_ids = each.value.security_groups
  user_data              = each.value.user_data != "" ? each.value.user_data : null
  
  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }
  
  dynamic "ebs_block_device" {
    for_each = each.value.volumes
    
    content {
      device_name = ebs_block_device.value.device_name
      volume_size = ebs_block_device.value.size
      volume_type = ebs_block_device.value.type
      encrypted   = true
    }
  }
  
  tags = {
    Name = "${var.project_name}-${each.key}"
    Role = each.value.role
  }
}

# Load Balancer (conditional)
resource "aws_lb" "main" {
  count = var.load_balancer.enabled ? 1 : 0
  
  name               = "${var.project_name}-lb"
  internal           = var.load_balancer.internal
  load_balancer_type = "application"
  security_groups    = [aws_security_group.main["web"].id]
  subnets            = aws_subnet.public[*].id
  
  tags = {
    Name = "${var.project_name}-lb"
  }
}

# Target Groups
resource "aws_lb_target_group" "main" {
  for_each = var.load_balancer.enabled ? var.load_balancer.targets : {}
  
  name     = "${var.project_name}-${each.key}-tg"
  port     = each.value.port
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
  
  health_check {
    path                = each.value.health_check_path
    healthy_threshold   = 2
    unhealthy_threshold = 10
  }
  
  tags = {
    Name = "${var.project_name}-${each.key}-tg"
  }
}

# Target Group Attachments
locals {
  lb_attachments = var.load_balancer.enabled ? flatten([
    for tg_name, tg_config in var.load_balancer.targets : [
      for role in tg_config.instances : [
        for instance_key, instance in local.instances_map :
        {
          key           = "${tg_name}-${instance_key}"
          tg_name       = tg_name
          instance_id   = aws_instance.main[instance_key].id
        } if instance.role == role
      ]
    ]
  ]) : []
  
  lb_attachments_map = {
    for attach in local.lb_attachments :
    attach.key => attach
  }
}

resource "aws_lb_target_group_attachment" "main" {
  for_each = local.lb_attachments_map
  
  target_group_arn = aws_lb_target_group.main[each.value.tg_name].arn
  target_id        = each.value.instance_id
  port             = var.load_balancer.targets[each.value.tg_name].port
}

# ==================================================
# File: outputs.tf
# ==================================================

output "vpc_id" {
  value = aws_vpc.main.id
}

output "instances" {
  value = {
    for key, instance in aws_instance.main :
    key => {
      id         = instance.id
      private_ip = instance.private_ip
      public_ip  = instance.public_ip
    }
  }
}

output "security_groups" {
  value = {
    for key, sg in aws_security_group.main :
    key => sg.id
  }
}

output "load_balancer_dns" {
  value = var.load_balancer.enabled ? aws_lb.main[0].dns_name : null
}
```

---

### ✅ Day 8-9 Checklist

- [x] Count vs for_each - when to use each
- [x] Advanced for_each patterns
- [x] For expressions (list/map transformations)
- [x] Nested for expressions and flattening
- [x] Dynamic blocks syntax
- [x] Multiple dynamic block patterns
- [x] Nested dynamic blocks
- [x] Real-world complex example

**Next:** Modules - Reusable infrastructure!

---

## Day 10-11: Terraform Modules

### 🎯 Learning Objectives
- Understand modules and their benefits
- Create reusable modules
- Use module inputs and outputs
- Work with module sources
- Follow module best practices

---

### 📦 What are Modules?

**Module** = A container for multiple resources used together.

Think of modules like **functions in programming**:
- **Input** = Variables
- **Processing** = Resources
- **Output** = Output values

**Benefits:**
- **Reusability** - Write once, use many times
- **Organization** - Group related resources
- **Standardization** - Enforce best practices
- **Collaboration** - Share with team

---

### 🏗️ Module Structure

```
my-module/
├── main.tf          # Main resource definitions
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── README.md        # Documentation
├── versions.tf      # Provider requirements (optional)
└── examples/        # Usage examples (optional)
    └── complete/
        ├── main.tf
        └── variables.tf
```

---

### 🎨 Creating Your First Module

#### **Module: VPC**

```hcl
# ==================================================
# File: modules/vpc/variables.tf
# ==================================================

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
}

variable "enable_nat_gateway" {
  description = "Enable NAT Gateway for private subnets"
  type        = bool
  default     = true
}

variable "single_nat_gateway" {
  description = "Use single NAT Gateway for all private subnets"
  type        = bool
  default     = false
}

variable "tags" {
  description = "Additional tags"
  type        = map(string)
  default     = {}
}

# ==================================================
# File: modules/vpc/main.tf
# ==================================================

locals {
  common_tags = merge(
    var.tags,
    {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
      Module      = "VPC"
    }
  )
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-vpc"
    }
  )
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-igw"
    }
  )
}

# Public Subnets
resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-public-${var.availability_zones[count.index]}"
      Type = "public"
    }
  )
}

# Private Subnets
resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-private-${var.availability_zones[count.index]}"
      Type = "private"
    }
  )
}

# Elastic IPs for NAT Gateways
resource "aws_eip" "nat" {
  count = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.private_subnet_cidrs)) : 0
  
  domain = "vpc"
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-nat-eip-${count.index + 1}"
    }
  )
  
  depends_on = [aws_internet_gateway.main]
}

# NAT Gateways
resource "aws_nat_gateway" "main" {
  count = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.private_subnet_cidrs)) : 0
  
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-nat-${count.index + 1}"
    }
  )
  
  depends_on = [aws_internet_gateway.main]
}

# Public Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-public-rt"
    }
  )
}

# Public Route Table Associations
resource "aws_route_table_association" "public" {
  count = length(var.public_subnet_cidrs)
  
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# Private Route Tables
resource "aws_route_table" "private" {
  count = var.enable_nat_gateway ? length(var.private_subnet_cidrs) : 1
  
  vpc_id = aws_vpc.main.id
  
  dynamic "route" {
    for_each = var.enable_nat_gateway ? [1] : []
    
    content {
      cidr_block     = "0.0.0.0/0"
      nat_gateway_id = var.single_nat_gateway ? aws_nat_gateway.main[0].id : aws_nat_gateway.main[count.index].id
    }
  }
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${var.environment}-private-rt-${count.index + 1}"
    }
  )
}

# Private Route Table Associations
resource "aws_route_table_association" "private" {
  count = length(var.private_subnet_cidrs)
  
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = var.enable_nat_gateway ? aws_route_table.private[var.single_nat_gateway ? 0 : count.index].id : aws_route_table.private[0].id
}

# ==================================================
# File: modules/vpc/outputs.tf
# ==================================================

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "public_subnet_cidrs" {
  description = "CIDR blocks of public subnets"
  value       = aws_subnet.public[*].cidr_block
}

output "private_subnet_cidrs" {
  description = "CIDR blocks of private subnets"
  value       = aws_subnet.private[*].cidr_block
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway"
  value       = aws_internet_gateway.main.id
}

output "nat_gateway_ids" {
  description = "IDs of NAT Gateways"
  value       = aws_nat_gateway.main[*].id
}

output "nat_eip_public_ips" {
  description = "Public IPs of NAT Gateway Elastic IPs"
  value       = aws_eip.nat[*].public_ip
}

# ==================================================
# File: modules/vpc/README.md
# ==================================================

# VPC Module

Creates a complete VPC with public and private subnets, Internet Gateway, and NAT Gateway.

## Features

- VPC with customizable CIDR
- Public subnets with Internet Gateway
- Private subnets with NAT Gateway
- Single or multiple NAT Gateways
- Automatic route table configuration

## Usage

```hcl
module "vpc" {
  source = "./modules/vpc"
  
  project_name = "myapp"
  environment  = "prod"
  
  vpc_cidr = "10.0.0.0/16"
  
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  
  enable_nat_gateway  = true
  single_nat_gateway  = false
  
  tags = {
    Team = "Platform"
  }
}
```

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|----------|
| project_name | Project name | string | - | yes |
| environment | Environment | string | - | yes |
| vpc_cidr | VPC CIDR block | string | "10.0.0.0/16" | no |
| availability_zones | List of AZs | list(string) | - | yes |
| public_subnet_cidrs | Public subnet CIDRs | list(string) | - | yes |
| private_subnet_cidrs | Private subnet CIDRs | list(string) | - | yes |
| enable_nat_gateway | Enable NAT Gateway | bool | true | no |
| single_nat_gateway | Use single NAT Gateway | bool | false | no |
| tags | Additional tags | map(string) | {} | no |

## Outputs

| Name | Description |
|------|-------------|
| vpc_id | VPC ID |
| public_subnet_ids | Public subnet IDs |
| private_subnet_ids | Private subnet IDs |
| nat_gateway_ids | NAT Gateway IDs |
```

---

### 🎯 Using the Module

```hcl
# ==================================================
# File: main.tf (root configuration)
# ==================================================

terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# Use the VPC module
module "vpc" {
  source = "./modules/vpc"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_cidr = "10.0.0.0/16"
  
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  
  enable_nat_gateway = true
  single_nat_gateway = false
  
  tags = {
    Team = "Platform"
  }
}

# Use module outputs
resource "aws_instance" "web" {
  count = 3
  
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t3.micro"
  
  # Reference module output
  subnet_id = module.vpc.public_subnet_ids[count.index]
  
  tags = {
    Name = "web-${count.index + 1}"
  }
}

# Output module values
output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnets" {
  value = module.vpc.public_subnet_ids
}
```

---

### 📚 Module Sources

#### **1. Local Path**

```hcl
module "vpc" {
  source = "./modules/vpc"
}

module "networking" {
  source = "../shared-modules/networking"
}
```

#### **2. GitHub**

```hcl
# Public repo
module "vpc" {
  source = "github.com/terraform-aws-modules/terraform-aws-vpc"
}

# With branch/tag
module "vpc" {
  source = "github.com/terraform-aws-modules/terraform-aws-vpc?ref=v5.1.2"
}

# Private repo with SSH
module "vpc" {
  source = "git@github.com:mycompany/terraform-modules.git//vpc"
}

# Subdirectory
module "vpc" {
  source = "github.com/mycompany/terraform-modules//aws/vpc?ref=v1.0.0"
}
```

#### **3. Terraform Registry**

```hcl
# Official modules
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.2"
}

module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = "6.1.1"
}

# Always pin version!
```

#### **4. S3 Bucket**

```hcl
module "vpc" {
  source = "s3::https://s3.amazonaws.com/my-bucket/terraform-modules/vpc.zip"
}
```

#### **5. HTTP URL**

```hcl
module "vpc" {
  source = "https://example.com/terraform-modules/vpc.zip"
}
```

---

### 🔄 Module Composition

Build complex modules from simpler ones:

```hcl
# ==================================================
# Module: application (composite module)
# ==================================================

# File: modules/application/main.tf

module "vpc" {
  source = "../vpc"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_cidr             = var.vpc_cidr
  availability_zones   = var.availability_zones
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
}

module "security_groups" {
  source = "../security-groups"
  
  vpc_id       = module.vpc.vpc_id
  project_name = var.project_name
  environment  = var.environment
}

module "alb" {
  source = "../alb"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.public_subnet_ids
  security_group = module.security_groups.alb_sg_id
}

module "asg" {
  source = "../asg"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_id             = module.vpc.vpc_id
  subnet_ids         = module.vpc.private_subnet_ids
  security_group     = module.security_groups.app_sg_id
  target_group_arns  = [module.alb.target_group_arn]
  
  min_size     = var.min_instances
  max_size     = var.max_instances
  desired_size = var.desired_instances
}

module "rds" {
  source = "../rds"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.private_subnet_ids
  security_group = module.security_groups.db_sg_id
  
  engine         = "mysql"
  engine_version = "8.0.33"
  instance_class = var.db_instance_class
  multi_az       = var.db_multi_az
}

# File: modules/application/outputs.tf

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "alb_dns_name" {
  value = module.alb.dns_name
}

output "database_endpoint" {
  value = module.rds.endpoint
}
```

**Use the composite module:**

```hcl
# Root main.tf

module "production_app" {
  source = "./modules/application"
  
  project_name = "myapp"
  environment  = "prod"
  
  vpc_cidr = "10.0.0.0/16"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  
  min_instances     = 3
  max_instances     = 10
  desired_instances = 5
  
  db_instance_class = "db.r5.large"
  db_multi_az       = true
}

output "app_url" {
  value = "http://${module.production_app.alb_dns_name}"
}
```

---

### 🎓 Module Best Practices

#### **1. Use Clear Variable Names**

```hcl
# ❌ BAD
variable "c" {
  type = string
}

variable "n" {
  type = number
}

# ✅ GOOD
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  
  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0))
    error_message = "Must be a valid CIDR block."
  }
}

variable "instance_count" {
  description = "Number of instances to create"
  type        = number
  
  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 100
    error_message = "Instance count must be between 1 and 100."
  }
}
```

---

#### **2. Provide Sensible Defaults**

```hcl
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"  # Safe default for dev/test
}

variable "enable_monitoring" {
  description = "Enable detailed monitoring"
  type        = bool
  default     = false  # Opt-in for cost savings
}

variable "backup_retention_days" {
  description = "Number of days to retain backups"
  type        = number
  default     = 7  # Reasonable default
}
```

---

#### **3. Use Output Descriptions**

```hcl
output "vpc_id" {
  description = "ID of the VPC created by this module"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "List of IDs of public subnets, ordered by availability zone"
  value       = aws_subnet.public[*].id
}

output "nat_gateway_public_ips" {
  description = "Public IP addresses of NAT Gateways for whitelisting"
  value       = aws_eip.nat[*].public_ip
}
```

---

#### **4. Version Your Modules**

```hcl
# Use Git tags
module "vpc" {
  source = "git::https://github.com/myorg/terraform-modules.git//vpc?ref=v1.2.0"
}

# Follow semantic versioning
# v1.2.0 = MAJOR.MINOR.PATCH
# MAJOR = breaking changes
# MINOR = new features (backwards compatible)
# PATCH = bug fixes
```

---

#### **5. Write Good Documentation**

```markdown
# VPC Module

## Description
Creates a production-ready VPC with public and private subnets across multiple availability zones.

## Features
- [x] Multi-AZ deployment
- [x] NAT Gateway (optional single/multi)
- [x] Internet Gateway for public subnets
- [x] Automatic route table configuration
- [x] Customizable CIDR blocks

## Requirements
- Terraform >= 1.0
- AWS Provider >= 5.0

## Usage

### Basic Example
```hcl
module "vpc" {
  source = "./modules/vpc"
  
  project_name = "myapp"
  environment  = "prod"
  
  availability_zones = ["us-east-1a", "us-east-1b"]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24"]
}
```

### Production Example
```hcl
module "vpc" {
  source = "./modules/vpc"
  
  project_name = "myapp"
  environment  = "prod"
  
  vpc_cidr = "10.0.0.0/16"
  
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  
  enable_nat_gateway = true
  single_nat_gateway = false  # HA setup
  
  tags = {
    Team       = "Platform"
    CostCenter = "Engineering"
  }
}
```

## Inputs

(Table of all inputs with descriptions)

## Outputs

(Table of all outputs with descriptions)

## Cost Estimation

- VPC: Free
- Internet Gateway: Free
- NAT Gateway: ~$32/month per AZ
- Elastic IPs: Free (when attached to NAT Gateway)

**Total (3 AZs with NAT Gateway in each): ~$96/month**

## Known Issues

- NAT Gateway can take 5-10 minutes to provision
- Changing AZ count requires careful planning to avoid downtime

## Contributing

Please see CONTRIBUTING.md

## License

MIT
```

---

#### **6. Organize Module Files**

```
modules/
├── vpc/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── versions.tf
│   ├── README.md
│   └── examples/
│       ├── basic/
│       │   ├── main.tf
│       │   └── README.md
│       └── complete/
│           ├── main.tf
│           └── README.md
├── security-groups/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── README.md
└── ec2-instance/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

---

### ✅ Day 10-11 Checklist

- [x] Module concepts and benefits
- [x] Module structure
- [x] Creating modules (VPC example)
- [x] Using modules
- [x] Module sources (local, GitHub, registry, etc.)
- [x] Module composition
- [x] Module best practices
- [x] Documentation

**Next:** Workspaces, Remote State, and Production Practices!

---

## 📊 Progress Summary

### ✅ **COMPLETED (Days 1-11)**

**PART 1: FOUNDATIONS (Days 1-2)** ✅
- Day 1: What is Terraform, Installation & Setup
- Day 2: First Project, Terraform Workflow

**PART 2: CORE CONCEPTS (Days 3-7)** ✅  
- Day 3: HCL Language Basics (syntax, data types, functions)
- Day 4: Providers Deep Dive (AWS, Azure, GCP)
- Day 5: Resources (meta-arguments, lifecycle, dependencies)
- Day 6: Variables (all types, validation, precedence)
- Day 7: Outputs & Data Sources

**PART 3: ADVANCED FEATURES (Days 8-11)** ✅
- Days 8-9: Advanced Iteration (count, for_each, dynamic blocks, for expressions)
- Days 10-11: Modules (creation, usage, composition, best practices)

---

### 📝 **REMAINING CONTENT**

Due to response length constraints, the following sections will be added next:

**PART 4: PRODUCTION READY (Days 12-18)**
- Day 12: Workspaces (managing multiple environments)
- Day 13: Remote State (S3, Azure Blob, Terraform Cloud)
- Day 14: State Locking (DynamoDB, preventing conflicts)
- Day 15: Import & Migration (bringing existing infrastructure)
- Day 16: Provisioners (local-exec, remote-exec, file)
- Day 17: Lifecycle Rules & Conditions (advanced resource management)
- Day 18: Terraform Cloud & Enterprise

**PART 5: BEST PRACTICES (Days 19-22)**
- Day 19: Project Structure & Organization
- Day 20: Security Best Practices (secrets, policies, compliance)
- Day 21: Testing Strategies (terraform validate, tflint, terratest)
- Day 22: CI/CD Integration (GitHub Actions, GitLab CI, Jenkins)

**PART 6: REAL-WORLD PROJECTS (5 Complete Projects)**
- Project 1: Simple Web Server (EC2 + Security Group + EIP)
- Project 2: Complete VPC & Networking (Multi-AZ, NAT Gateway, Bastion)
- Project 3: Multi-Tier Application (ALB, ASG, RDS, ElastiCache)
- Project 4: EKS Kubernetes Cluster (Production-ready Kubernetes)
- Project 5: Multi-Cloud Deployment (AWS + Azure + GCP together)

**BONUS SECTIONS**
- Advanced State Management
- Terraform Graph & Visualization
- Performance Optimization
- Troubleshooting Guide
- Certification Preparation (Terraform Associate)
- Cheat Sheets & Quick Reference

---

### 📈 **Current Statistics**

- **Total Lines**: ~7,450+
- **Sections Completed**: 11 days of comprehensive content
- **Code Examples**: 100+ real-world examples
- **Remaining Sections**: 11 days + 5 projects + bonus content

---

## 🎯 What You've Learned So Far

At this point, you have mastered:

1. ✅ **Terraform Fundamentals** - Core concepts, workflow, HCL syntax
2. ✅ **Provider Configuration** - AWS, Azure, GCP setup and authentication
3. ✅ **Resource Management** - Creating, updating, and managing infrastructure
4. ✅ **Variables & Outputs** - Dynamic, reusable configurations
5. ✅ **Data Sources** - Querying existing infrastructure
6. ✅ **Advanced Iteration** - count, for_each, dynamic blocks, complex transformations
7. ✅ **Modules** - Creating reusable, composable infrastructure components

**You can now:**
- ✅ Write production-quality Terraform code
- ✅ Create reusable modules
- ✅ Deploy multi-tier applications
- ✅ Use advanced HCL features
- ✅ Follow Terraform best practices

**Next steps will cover:**
- 🔜 Production deployment patterns
- 🔜 State management & collaboration
- 🔜 Security & compliance
- 🔜 Testing & CI/CD
- 🔜 Complete real-world projects

---

## 🚀 Continue Learning

The remaining content (Days 12-22 + 5 Projects + Bonus) will be added to complete this comprehensive guide. Would you like me to:

1. ✅ Continue with Days 12-18 (Production Ready)
2. ✅ Continue with Days 19-22 (Best Practices)
3. ✅ Add all 5 Real-World Projects
4. ✅ Add Bonus Sections

**Let me know and I'll continue building the complete guide!** 🎓

---