# 🚀 Terraform Complete Mastery Guide - Part 2
**Production Ready, Best Practices & Real-World Projects**

> **Continuation from Part 1** - Advanced production concepts, testing, CI/CD, and complete projects  
> *Days 12-22 + 5 Real-World Projects*

---

## 📚 Table of Contents - Part 2

### **PART 4: PRODUCTION READY**
- [Day 12: Workspaces](#day-12-workspaces)
- [Day 13: Remote State](#day-13-remote-state)
- [Day 14: State Locking](#day-14-state-locking)
- [Day 15: Import & Migration](#day-15-import--migration)
- [Day 16: Provisioners](#day-16-provisioners)
- [Day 17: Lifecycle & Conditions](#day-17-lifecycle--conditions)
- [Day 18: Terraform Cloud](#day-18-terraform-cloud)

### **PART 5: BEST PRACTICES**
- [Day 19: Project Structure](#day-19-project-structure)
- [Day 20: Security Best Practices](#day-20-security-best-practices)
- [Day 21: Testing Strategies](#day-21-testing-strategies)
- [Day 22: CI/CD Integration](#day-22-cicd-integration)

### **PART 6: REAL-WORLD PROJECTS**
- [Project 1: Simple Web Server](#project-1-simple-web-server)
- [Project 2: VPC & Networking](#project-2-vpc--networking)
- [Project 3: Multi-Tier Application](#project-3-multi-tier-application)
- [Project 4: EKS Kubernetes Cluster](#project-4-eks-kubernetes-cluster)
- [Project 5: Multi-Cloud Deployment](#project-5-multi-cloud-deployment)

### **BONUS CONTENT**
- [Advanced State Management](#advanced-state-management)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Performance Optimization](#performance-optimization)
- [Certification Prep](#certification-preparation)
- [Cheat Sheets](#cheat-sheets)

---

## Day 12: Workspaces - Managing Multiple Environments

### 🎯 Learning Objectives
- Understand Terraform workspaces
- Manage multiple environments
- Use workspace-specific configurations
- Know when to use workspaces vs modules

---

### 🌍 What are Workspaces?

**Workspace** = Named containers for Terraform state

Think of workspaces like **Git branches** for your infrastructure:
- Each workspace has its **own state file**
- Same code, different state
- Useful for dev/staging/prod environments

```plaintext
┌─────────────────────────────────────┐
│     Terraform Configuration         │
│         (same code)                 │
└────────────┬────────────────────────┘
             │
      ┌──────┴──────────┐
      │                 │
   ┌──▼──┐          ┌──▼──┐          ┌──────┐
   │ dev │          │stage│          │ prod │
   └─────┘          └─────┘          └──────┘
   State 1          State 2          State 3
```

---

### 📋 Workspace Commands

```bash
# List workspaces
terraform workspace list
# Output:
# * default
#   dev
#   staging
#   prod

# Show current workspace
terraform workspace show
# default

# Create new workspace
terraform workspace new dev
# Created and switched to workspace "dev"

# Switch workspace
terraform workspace select staging
# Switched to workspace "staging"

# Delete workspace
terraform workspace delete dev
# Deleted workspace "dev"
```

---

### 🎨 Basic Workspace Usage

```hcl
# File: main.tf

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

# Use workspace name in resources
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  
  tags = {
    Name        = "web-server-${terraform.workspace}"
    Environment = terraform.workspace
  }
}

# Workspace-specific configuration
locals {
  environment = terraform.workspace
  
  # Different settings per workspace
  instance_count = {
    default = 1
    dev     = 1
    staging = 2
    prod    = 5
  }
  
  instance_type = {
    default = "t2.micro"
    dev     = "t2.micro"
    staging = "t2.small"
    prod    = "t3.large"
  }
}

resource "aws_instance" "app" {
  count = local.instance_count[local.environment]
  
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = local.instance_type[local.environment]
  
  tags = {
    Name = "${terraform.workspace}-app-${count.index + 1}"
  }
}

# File: variables.tf

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t2.micro"
}

# File: outputs.tf

output "workspace" {
  description = "Current workspace"
  value       = terraform.workspace
}

output "instance_ids" {
  description = "Instance IDs in this workspace"
  value       = aws_instance.app[*].id
}
```

**Usage:**

```bash
# Create dev environment
terraform workspace new dev
terraform apply

# Create staging environment
terraform workspace new staging
terraform apply

# Create production environment
terraform workspace new prod
terraform apply

# Switch between environments
terraform workspace select dev
terraform plan

terraform workspace select prod
terraform plan
```

---

### 🎯 Advanced Workspace Patterns

#### **1. Environment-Specific Variables**

```hcl
# File: variables.tf

variable "environment_config" {
  type = map(object({
    instance_count    = number
    instance_type     = string
    volume_size       = number
    enable_monitoring = bool
    multi_az          = bool
  }))
  
  default = {
    dev = {
      instance_count    = 1
      instance_type     = "t2.micro"
      volume_size       = 20
      enable_monitoring = false
      multi_az          = false
    }
    staging = {
      instance_count    = 2
      instance_type     = "t2.small"
      volume_size       = 30
      enable_monitoring = false
      multi_az          = false
    }
    prod = {
      instance_count    = 5
      instance_type     = "t3.large"
      volume_size       = 50
      enable_monitoring = true
      multi_az          = true
    }
  }
}

# File: main.tf

locals {
  environment = terraform.workspace
  config      = var.environment_config[local.environment]
}

resource "aws_instance" "app" {
  count = local.config.instance_count
  
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = local.config.instance_type
  monitoring    = local.config.enable_monitoring
  
  root_block_device {
    volume_size = local.config.volume_size
    volume_type = "gp3"
  }
  
  tags = {
    Name        = "${local.environment}-app-${count.index + 1}"
    Environment = local.environment
  }
}

resource "aws_db_instance" "main" {
  identifier     = "${local.environment}-database"
  engine         = "mysql"
  instance_class = local.environment == "prod" ? "db.r5.large" : "db.t3.micro"
  multi_az       = local.config.multi_az
  
  allocated_storage = local.config.volume_size
  
  backup_retention_period = local.environment == "prod" ? 30 : 7
  
  tags = {
    Environment = local.environment
  }
}
```

---

#### **2. Workspace-Specific Backend Configuration**

```hcl
# File: backend.tf

terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
    
    # Workspace states are stored at:
    # s3://my-terraform-state/infrastructure/env:/dev/terraform.tfstate
    # s3://my-terraform-state/infrastructure/env:/staging/terraform.tfstate
    # s3://my-terraform-state/infrastructure/env:/prod/terraform.tfstate
  }
}
```

---

#### **3. Complete Multi-Environment Setup**

```hcl
# ==================================================
# File: variables.tf
# ==================================================

variable "project_name" {
  type    = string
  default = "myapp"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "vpc_config" {
  type = map(object({
    cidr_block          = string
    availability_zones  = list(string)
    public_subnet_cidrs = list(string)
  }))
  
  default = {
    dev = {
      cidr_block          = "10.0.0.0/16"
      availability_zones  = ["us-east-1a"]
      public_subnet_cidrs = ["10.0.1.0/24"]
    }
    staging = {
      cidr_block          = "10.1.0.0/16"
      availability_zones  = ["us-east-1a", "us-east-1b"]
      public_subnet_cidrs = ["10.1.1.0/24", "10.1.2.0/24"]
    }
    prod = {
      cidr_block          = "10.2.0.0/16"
      availability_zones  = ["us-east-1a", "us-east-1b", "us-east-1c"]
      public_subnet_cidrs = ["10.2.1.0/24", "10.2.2.0/24", "10.2.3.0/24"]
    }
  }
}

# ==================================================
# File: main.tf
# ==================================================

locals {
  environment = terraform.workspace == "default" ? "dev" : terraform.workspace
  vpc_config  = var.vpc_config[local.environment]
  
  common_tags = {
    Project     = var.project_name
    Environment = local.environment
    Workspace   = terraform.workspace
    ManagedBy   = "Terraform"
  }
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = local.vpc_config.cidr_block
  enable_dns_hostnames = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${local.environment}-vpc"
    }
  )
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${local.environment}-igw"
    }
  )
}

# Public Subnets
resource "aws_subnet" "public" {
  count = length(local.vpc_config.public_subnet_cidrs)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = local.vpc_config.public_subnet_cidrs[count.index]
  availability_zone       = local.vpc_config.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${local.environment}-public-${count.index + 1}"
    }
  )
}

# Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = merge(
    local.common_tags,
    {
      Name = "${var.project_name}-${local.environment}-public-rt"
    }
  )
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public)
  
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# ==================================================
# File: outputs.tf
# ==================================================

output "workspace" {
  description = "Current Terraform workspace"
  value       = terraform.workspace
}

output "environment" {
  description = "Environment name"
  value       = local.environment
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.main.cidr_block
}

output "subnet_ids" {
  description = "Subnet IDs"
  value       = aws_subnet.public[*].id
}

output "resource_names" {
  description = "Names of created resources"
  value = {
    vpc     = aws_vpc.main.tags["Name"]
    subnets = aws_subnet.public[*].tags["Name"]
  }
}
```

**Deploy to multiple environments:**

```bash
# Development
terraform workspace new dev
terraform apply -auto-approve

# Staging
terraform workspace new staging
terraform apply -auto-approve

# Production
terraform workspace new prod
terraform apply -auto-approve

# View resources per environment
terraform workspace select dev
terraform output

terraform workspace select staging
terraform output

terraform workspace select prod
terraform output

# Destroy specific environment
terraform workspace select dev
terraform destroy

# List all workspaces
terraform workspace list
#   default
# * dev
#   staging
#   prod
```

---

### ⚖️ Workspaces vs Separate Directories

#### **When to Use Workspaces:**

✅ **Use workspaces when:**
- Same infrastructure, different environments
- Small to medium projects
- Environments have similar configurations
- Quick environment switching needed
- Testing changes before production

#### **When to Use Separate Directories:**

✅ **Use separate directories when:**
- Environments have different architectures
- Different teams manage different environments
- Need different backend configurations
- Large, complex projects
- Strict separation required (compliance)

**Example structure with separate directories:**

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       ├── terraform.tfvars
│       └── backend.tf
└── modules/
    ├── vpc/
    ├── compute/
    └── database/
```

---

### 🎓 Workspace Best Practices

#### **1. Always Check Current Workspace**

```bash
# Before applying changes
echo "Current workspace: $(terraform workspace show)"
terraform workspace show

# Add to scripts
#!/bin/bash
WORKSPACE=$(terraform workspace show)
echo "You are in workspace: $WORKSPACE"
read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi
terraform apply
```

#### **2. Use Consistent Naming**

```hcl
locals {
  environment = terraform.workspace
  
  # Consistent resource naming
  name_prefix = "${var.project_name}-${local.environment}"
  
  resource_names = {
    vpc        = "${local.name_prefix}-vpc"
    subnet     = "${local.name_prefix}-subnet"
    instance   = "${local.name_prefix}-instance"
    lb         = "${local.name_prefix}-lb"
    db         = "${local.name_prefix}-db"
  }
}
```

#### **3. Protect Production Workspace**

```hcl
# Add preconditions
resource "aws_instance" "critical" {
  ami           = "ami-12345"
  instance_type = "t3.large"
  
  lifecycle {
    precondition {
      condition     = terraform.workspace == "prod"
      error_message = "This resource can only be created in production workspace."
    }
  }
}

# Or prevent certain actions
locals {
  allowed_to_delete_db = terraform.workspace != "prod"
}

resource "aws_db_instance" "main" {
  identifier = "${terraform.workspace}-db"
  
  skip_final_snapshot = local.allowed_to_delete_db
  
  lifecycle {
    prevent_destroy = terraform.workspace == "prod"
  }
}
```

#### **4. Document Workspace Usage**

```markdown
# README.md

## Workspace Management

### Available Workspaces
- `dev` - Development environment
- `staging` - Staging environment
- `prod` - Production environment

### Switching Workspaces

```bash
# List workspaces
terraform workspace list

# Switch to dev
terraform workspace select dev

# Switch to prod
terraform workspace select prod
```

### Deploying to Environments

```bash
# Deploy to dev
terraform workspace select dev
terraform apply

# Deploy to staging
terraform workspace select staging
terraform apply -var-file="staging.tfvars"

# Deploy to prod (requires approval)
terraform workspace select prod
terraform plan -out=prod.tfplan
# Review plan
terraform apply prod.tfplan
```

### State File Locations
- Dev: `s3://bucket/project/env:/dev/terraform.tfstate`
- Staging: `s3://bucket/project/env:/staging/terraform.tfstate`
- Prod: `s3://bucket/project/env:/prod/terraform.tfstate`
```

---

### ✅ Day 12 Checklist

- [x] Understand Terraform workspaces
- [x] Workspace commands (list, new, select, delete)
- [x] Using workspace name in configurations
- [x] Environment-specific variables
- [x] Complete multi-environment setup
- [x] Workspaces vs separate directories
- [x] Best practices

**Next:** Remote State - Collaboration and state management!

---

## Day 13: Remote State - Collaboration & State Management

### 🎯 Learning Objectives
- Understand remote state backends
- Configure S3 backend
- Set up Azure Blob Storage
- Use Terraform Cloud
- Implement state locking
- Enable team collaboration

---

### 🗄️ What is Remote State?

By default, Terraform stores state **locally** in `terraform.tfstate`.

**Problems with local state:**
- ❌ Not shared with team
- ❌ No locking (conflicts)
- ❌ No backup/versioning
- ❌ Contains sensitive data in plain text
- ❌ Single point of failure

**Remote state backend** stores state in a shared location:
- ✅ Team collaboration
- ✅ State locking
- ✅ Encryption
- ✅ Versioning/backup
- ✅ Centralized management

---

### 📦 Backend Types

| Backend | Use Case | Features |
|---------|----------|----------|
| **S3** | AWS environments | Encryption, versioning, locking (with DynamoDB) |
| **Azure Blob** | Azure environments | Encryption, locking |
| **GCS** | GCP environments | Encryption, versioning |
| **Terraform Cloud** | Any environment | Full featured, UI, runs, policies |
| **HTTP** | Custom solutions | Flexible, requires implementation |
| **Consul** | HashiCorp stack | High availability, locking |
| **etcd** | Kubernetes environments | Distributed, consistent |

---

### ☁️ AWS S3 Backend (Most Common)

#### **Prerequisites**

```bash
# 1. Create S3 bucket
aws s3 mb s3://my-terraform-state --region us-east-1

# 2. Enable versioning
aws s3api put-bucket-versioning \
  --bucket my-terraform-state \
  --versioning-configuration Status=Enabled

# 3. Enable encryption
aws s3api put-bucket-encryption \
  --bucket my-terraform-state \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'

# 4. Block public access
aws s3api put-public-access-block \
  --bucket my-terraform-state \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

# 5. Create DynamoDB table for locking
aws dynamodb create-table \
  --table-name terraform-state-lock \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

#### **Terraform Configuration with S3 Backend**

```hcl
# ==================================================
# File: backend.tf
# ==================================================

terraform {
  required_version = ">= 1.0"
  
  # S3 backend configuration
  backend "s3" {
    bucket         = "my-terraform-state"           # S3 bucket name
    key            = "project/terraform.tfstate"    # State file path
    region         = "us-east-1"                    # AWS region
    encrypt        = true                           # Enable encryption
    dynamodb_table = "terraform-state-lock"         # DynamoDB table for locking
    
    # Optional: Use specific profile
    profile = "terraform"
    
    # Optional: KMS encryption
    # kms_key_id = "arn:aws:kms:us-east-1:ACCOUNT_ID:key/KEY_ID"
  }
  
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
```

**Initialize backend:**

```bash
# Initialize with backend configuration
terraform init

# Output:
# Initializing the backend...
# Successfully configured the backend "s3"!
# ...
```

---

#### **Migrate from Local to Remote State**

```bash
# 1. Start with local state (terraform.tfstate exists locally)

# 2. Add backend configuration to backend.tf (as shown above)

# 3. Initialize backend
terraform init

# Terraform will detect the change and ask:
# Do you want to copy existing state to the new backend?
# Enter a value: yes

# State is now in S3!

# 4. Remove local state file (after confirming remote state works)
rm terraform.tfstate
rm terraform.tfstate.backup
```

---

#### **Complete S3 Backend Setup with Terraform**

```hcl
# ==================================================
# File: backend-setup/main.tf
# ==================================================
# Run this FIRST to create the backend infrastructure

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

variable "region" {
  default = "us-east-1"
}

variable "state_bucket_name" {
  description = "Name of S3 bucket for Terraform state"
  type        = string
}

variable "dynamodb_table_name" {
  description = "Name of DynamoDB table for state locking"
  type        = string
  default     = "terraform-state-lock"
}

# S3 Bucket for state
resource "aws_s3_bucket" "terraform_state" {
  bucket = var.state_bucket_name
  
  tags = {
    Name        = "Terraform State Bucket"
    Purpose     = "Terraform State Storage"
    ManagedBy   = "Terraform"
  }
}

# Enable versioning
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  versioning_configuration {
    status = "Enabled"
  }
}

# Enable encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Bucket lifecycle policy
resource "aws_s3_bucket_lifecycle_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  rule {
    id     = "delete-old-versions"
    status = "Enabled"
    
    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}

# DynamoDB table for state locking
resource "aws_dynamodb_table" "terraform_lock" {
  name           = var.dynamodb_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"
  
  attribute {
    name = "LockID"
    type = "S"
  }
  
  tags = {
    Name      = "Terraform State Lock Table"
    Purpose   = "State Locking"
    ManagedBy = "Terraform"
  }
}

# Outputs
output "s3_bucket_name" {
  description = "Name of S3 bucket for state"
  value       = aws_s3_bucket.terraform_state.id
}

output "s3_bucket_arn" {
  description = "ARN of S3 bucket"
  value       = aws_s3_bucket.terraform_state.arn
}

output "dynamodb_table_name" {
  description = "Name of DynamoDB table"
  value       = aws_dynamodb_table.terraform_lock.name
}

output "backend_config" {
  description = "Backend configuration for other projects"
  value = <<-EOT
    terraform {
      backend "s3" {
        bucket         = "${aws_s3_bucket.terraform_state.id}"
        key            = "PROJECT_NAME/terraform.tfstate"
        region         = "${var.region}"
        encrypt        = true
        dynamodb_table = "${aws_dynamodb_table.terraform_lock.name}"
      }
    }
  EOT
}
```

**Deploy backend infrastructure:**

```bash
# Go to backend-setup directory
cd backend-setup

# Create terraform.tfvars
cat > terraform.tfvars <<EOF
region             = "us-east-1"
state_bucket_name  = "my-company-terraform-state"
dynamodb_table_name = "terraform-state-lock"
EOF

# Deploy
terraform init
terraform apply

# Copy the backend configuration
terraform output backend_config
```

---

### 🔐 State Locking

State locking **prevents** concurrent modifications:

```plaintext
Developer A starts: terraform apply
  ├─ Acquires lock on DynamoDB
  ├─ Makes changes
  └─ Releases lock

Developer B tries: terraform apply (while A is working)
  └─ ❌ Error: state is locked!
```

**Force unlock (use carefully!):**

```bash
# If Terraform crashes and lock isn't released
terraform force-unlock LOCK_ID

# Get lock ID from error message:
# Error: Error acquiring the state lock
# Lock Info:
#   ID:        abc123def456
#   ...
```

---

### 🌐 Azure Blob Storage Backend

#### **Prerequisites**

```bash
# 1. Create storage account
az storage account create \
  --name mystorageaccount \
  --resource-group myresourcegroup \
  --location eastus \
  --sku Standard_LRS \
  --encryption-services blob

# 2. Create container
az storage container create \
  --name terraform-state \
  --account-name mystorageaccount
```

#### **Backend Configuration**

```hcl
# File: backend.tf

terraform {
  backend "azurerm" {
    resource_group_name  = "myresourcegroup"
    storage_account_name = "mystorageaccount"
    container_name       = "terraform-state"
    key                  = "project.terraform.tfstate"
    
    # Authentication options:
    
    # Option 1: Service Principal
    # client_id       = "00000000-0000-0000-0000-000000000000"
    # client_secret   = "secret"
    # tenant_id       = "00000000-0000-0000-0000-000000000000"
    # subscription_id = "00000000-0000-0000-0000-000000000000"
    
    # Option 2: Managed Identity
    # use_msi = true
    
    # Option 3: Azure CLI (default)
    # Automatically uses Azure CLI credentials
  }
}
```

---

### ☁️ Google Cloud Storage Backend

```hcl
# File: backend.tf

terraform {
  backend "gcs" {
    bucket  = "my-terraform-state"
    prefix  = "terraform/state"
    
    # Optional: encryption key
    # encryption_key = "base64-encoded-key"
    
    # Authentication via GOOGLE_APPLICATION_CREDENTIALS env var
    # or Application Default Credentials
  }
}
```

**Create GCS bucket:**

```bash
# Create bucket
gsutil mb -p PROJECT_ID -l us-east1 gs://my-terraform-state

# Enable versioning
gsutil versioning set on gs://my-terraform-state

# Set lifecycle policy to delete old versions
cat > lifecycle.json <<EOF
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "Delete"},
        "condition": {
          "numNewerVersions": 3,
          "isLive": false
        }
      }
    ]
  }
}
EOF

gsutil lifecycle set lifecycle.json gs://my-terraform-state
```

---

### 🏢 Terraform Cloud Backend

**Benefits:**
- Free for small teams (up to 5 users)
- Built-in state storage & locking
- Web UI for viewing state
- Terraform runs in cloud
- Cost estimation
- Policy as code (Sentinel)
- Team management

#### **Setup**

```hcl
# File: backend.tf

terraform {
  cloud {
    organization = "my-company"
    
    workspaces {
      name = "my-app-production"
      
      # Or use tags for multiple workspaces
      # tags = ["app:myapp", "env:prod"]
    }
  }
}
```

**Login and Initialize:**

```bash
# Login to Terraform Cloud
terraform login

# Initialize
terraform init

# Run (executes remotely)
terraform apply
```

---

### 🔄 Working with Remote State

#### **Viewing Remote State**

```bash
# Show state
terraform show

# List resources
terraform state list

# Show specific resource
terraform state show aws_instance.web

# Pull state to local file
terraform state pull > terraform.tfstate.json

# View in JSON
cat terraform.tfstate.json | jq
```

#### **Refreshing Remote State**

```bash
# Refresh state from real infrastructure
terraform refresh

# Or
terraform apply -refresh-only
```

#### **Backing Up Remote State**

```bash
# Pull and save state regularly
terraform state pull > backups/terraform-$(date +%Y%m%d-%H%M%S).tfstate

# Automated backup script
#!/bin/bash
BACKUP_DIR="state-backups"
mkdir -p $BACKUP_DIR
DATE=$(date +%Y%m%d-%H%M%S)
terraform state pull > "$BACKUP_DIR/terraform-$DATE.tfstate"
echo "State backed up to $BACKUP_DIR/terraform-$DATE.tfstate"
```

---

### 🎓 Complete Multi-Environment Example with Remote State

```
project/
├── backend-setup/           # Set up backend infrastructure once
│   ├── main.tf
│   └── terraform.tfvars
├── environments/
│   ├── dev/
│   │   ├── backend.tf      # Points to s3://bucket/dev/terraform.tfstate
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── backend.tf      # Points to s3://bucket/staging/terraform.tfstate
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── backend.tf      # Points to s3://bucket/prod/terraform.tfstate
│       ├── main.tf
│       └── terraform.tfvars
└── modules/
    └── vpc/
```

**Environment-specific backend:**

```hcl
# environments/dev/backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

# environments/staging/backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "staging/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

# environments/prod/backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

---

### ⚠️ Remote State Best Practices

#### **1. Never Commit State Files**

```gitignore
# .gitignore

# Local state files
*.tfstate
*.tfstate.*

# Crash log files
crash.log

# Variable files that may contain secrets
*.tfvars
*.tfvars.json

# CLI configuration files
.terraformrc
terraform.rc
```

#### **2. Enable Encryption**

```hcl
# S3 with KMS encryption
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "arn:aws:kms:us-east-1:ACCOUNT:key/KEY_ID"
    dynamodb_table = "terraform-state-lock"
  }
}
```

#### **3. Implement Access Controls**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::my-terraform-state",
        "arn:aws:s3:::my-terraform-state/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:DeleteItem"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/terraform-state-lock"
    }
  ]
}
```

#### **4. Enable Versioning**

Always enable versioning on S3:
- Recover from accidental deletions
- Rollback to previous state
- Audit trail

#### **5. Regular Backups**

```bash
# Automated backup script
#!/bin/bash
set -e

BUCKET="my-terraform-state"
BACKUP_BUCKET="my-terraform-state-backups"
DATE=$(date +%Y/%m/%d)

# Sync state bucket to backup bucket
aws s3 sync \
  s3://$BUCKET \
  s3://$BACKUP_BUCKET/$DATE/ \
  --storage-class GLACIER
  
echo "Backup completed: s3://$BACKUP_BUCKET/$DATE/"
```

---

### ✅ Day 13 Checklist

- [x] Understand remote state backends
- [x] Configure S3 backend with DynamoDB locking
- [x] Set up Azure Blob Storage backend
- [x] Use Google Cloud Storage backend
- [x] Configure Terraform Cloud
- [x] Migrate from local to remote state
- [x] State locking mechanisms
- [x] Remote state best practices
- [x] Access controls and encryption

**Next:** State management operations and importing existing infrastructure!

---

## Day 14-15: Advanced State Management & Import

### 🎯 Learning Objectives
- Perform state operations
- Import existing infrastructure
- Move resources between states
- Handle state drift
- Recover from state issues

---

### 🔧 Terraform State Commands

#### **List Resources**

```bash
# List all resources in state
terraform state list

# Output:
# aws_vpc.main
# aws_subnet.public[0]
# aws_subnet.public[1]
# aws_instance.web[0]
# aws_instance.web[1]

# Filter by resource type
terraform state list | grep aws_instance
```

#### **Show Resource Details**

```bash
# Show specific resource
terraform state show aws_instance.web[0]

# Output:
# resource "aws_instance" "web" {
#     ami                          = "ami-12345"
#     instance_type                = "t2.micro"
#     id                           = "i-1234567890"
#     public_ip                    = "54.123.45.67"
#     ...
# }
```

#### **Move Resources**

```bash
# Rename resource
terraform state mv aws_instance.old_name aws_instance.new_name

# Move to module
terraform state mv aws_instance.web module.compute.aws_instance.web

# Move from module
terraform state mv module.compute.aws_instance.web aws_instance.web

# Move between different counts/for_each
terraform state mv 'aws_instance.web[0]' 'aws_instance.web["primary"]'
```

#### **Remove from State**

```bash
# Remove resource from state (doesn't delete real resource)
terraform state rm aws_instance.web[0]

# Remove module
terraform state rm module.vpc

# Remove all resources matching pattern
terraform state list | grep 'aws_instance\.temp' | xargs -n1 terraform state rm
```

#### **Replace Provider**

```bash
# If you change provider configuration
terraform state replace-provider \
  registry.terraform.io/hashicorp/aws \
  registry.terraform.io/hashicorp/aws
```

---

### 📥 Importing Existing Infrastructure

**Import** = Bring existing resources under Terraform management

#### **Basic Import**

```hcl
# 1. Write the resource configuration
resource "aws_instance" "imported_server" {
  ami           = "ami-12345"  # Must match actual
  instance_type = "t2.micro"    # Must match actual
  
  # Add all required arguments
}
```

```bash
# 2. Import the resource
terraform import aws_instance.imported_server i-1234567890abcdef0

# 3. Verify
terraform plan  # Should show no changes if config matches reality
```

---

#### **Import Examples**

**Import EC2 Instance:**

```hcl
resource "aws_instance" "existing" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "Existing Server"
  }
}
```

```bash
terraform import aws_instance.existing i-0123456789abcdef0
```

**Import VPC:**

```hcl
resource "aws_vpc" "existing" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "Existing VPC"
  }
}
```

```bash
terraform import aws_vpc.existing vpc-0123456789abcdef0
```

**Import S3 Bucket:**

```hcl
resource "aws_s3_bucket" "existing" {
  bucket = "my-existing-bucket"
}
```

```bash
terraform import aws_s3_bucket.existing my-existing-bucket
```

**Import RDS Instance:**

```hcl
resource "aws_db_instance" "existing" {
  identifier     = "production-db"
  engine         = "mysql"
  engine_version = "8.0.33"
  instance_class = "db.t3.micro"
  
  # ... other configuration
}
```

```bash
terraform import aws_db_instance.existing production-db
```

---

#### **Bulk Import Script**

```bash
#!/bin/bash
# import-infrastructure.sh

set -e

echo "Importing VPC..."
terraform import aws_vpc.main vpc-abc123

echo "Importing Subnets..."
terraform import 'aws_subnet.public[0]' subnet-111111
terraform import 'aws_subnet.public[1]' subnet-222222
terraform import 'aws_subnet.private[0]' subnet-333333

echo "Importing Security Groups..."
terraform import aws_security_group.web sg-web123
terraform import aws_security_group.db sg-db456

echo "Importing Instances..."
terraform import 'aws_instance.web[0]' i-instance1
terraform import 'aws_instance.web[1]' i-instance2

echo "Import complete!"
terraform plan
```

---

#### **Generate Configuration from Import (Terraform 1.5+)**

```hcl
# Use import blocks (Terraform 1.5+)
import {
  to = aws_instance.example
  id = "i-1234567890abcdef0"
}

# Terraform will generate the configuration!
```

```bash
# Generate configuration
terraform plan -generate-config-out=generated.tf

# Review generated.tf
cat generated.tf

# Apply
terraform apply
```

---

### 🔄 Moving Resources Between States

#### **Scenario: Split Monolithic State**

**Initial setup:**

```
project/
└── main.tf  (contains VPC + compute + database)
```

**Goal:**

```
project/
├── networking/
│   └── main.tf  (VPC resources)
├── compute/
│   └── main.tf  (EC2 instances)
└── database/
    └── main.tf  (RDS instances)
```

**Process:**

```bash
# 1. Export current state
cd project
terraform state pull > full-state.json

# 2. Create new directories with code split
mkdir networking compute database
# ... move code to appropriate files ...

# 3. Initialize new states
cd networking
terraform init

cd ../compute
terraform init

cd ../database
terraform init

# 4. Move resources using terraform state mv with -state and -state-out

# Move VPC to networking
cd ../project
terraform state mv \
  -state=terraform.tfstate \
  -state-out=networking/terraform.tfstate \
  aws_vpc.main

terraform state mv \
  -state=terraform.tfstate \
  -state-out=networking/terraform.tfstate \
  'aws_subnet.public[0]'

# Move instances to compute
terraform state mv \
  -state=terraform.tfstate \
  -state-out=compute/terraform.tfstate \
  'aws_instance.web[0]'

# Move database to database/
terraform state mv \
  -state=terraform.tfstate \
  -state-out=database/terraform.tfstate \
  aws_db_instance.main

# 5. Verify each directory
cd networking
terraform plan  # Should show no changes

cd ../compute
terraform plan  # Should show no changes

cd ../database
terraform plan  # Should show no changes
```

---

### 🔍 Detecting and Handling State Drift

**Drift** = Real infrastructure differs from Terraform state

#### **Detect Drift**

```bash
# Refresh state and show changes
terraform plan -refresh-only

# Or
terraform apply -refresh-only

# Output will show drift:
# Note: Objects have changed outside of Terraform
# 
# Terraform detected the following changes made outside of Terraform:
#
#   # aws_instance.web[0] has changed
#   ~ resource "aws_instance" "web" {
#       ~ instance_type = "t2.micro" -> "t2.small"
#       # ...
#     }
```

#### **Fix Drift**

**Option 1: Update Terraform to match reality**

```hcl
# Update your Terraform code to match real infrastructure
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.small"  # Changed to match reality
}
```

**Option 2: Fix infrastructure to match Terraform**

```bash
# Apply to restore desired state
terraform apply

# This will change instance_type back to t2.micro
```

**Option 3: Accept drift (use lifecycle ignore)**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    # Ignore manual changes to instance_type
    ignore_changes = [instance_type]
  }
}
```

---

### 🚨 State Disasters & Recovery

#### **Lost State File**

**Prevention:**
- Always use remote state with versioning
- Regular backups
- Never commit state to git

**Recovery:**

```bash
# Option 1: Restore from S3 versioning
aws s3api list-object-versions \
  --bucket my-terraform-state \
  --prefix project/terraform.tfstate

# Download specific version
aws s3api get-object \
  --bucket my-terraform-state \
  --key project/terraform.tfstate \
  --version-id VERSION_ID \
  terraform.tfstate

# Option 2: Recreate by importing all resources
# Write resource configurations
# Import each resource one by one
terraform import aws_vpc.main vpc-123456
terraform import aws_subnet.public[0] subnet-111111
# ...
```

#### **Corrupted State**

```bash
# Restore from backup
terraform state pull > corrupted-state.json
# Fix the JSON manually or restore from backup

# Push fixed state
terraform state push fixed-state.json

# Or restore S3 version
aws s3api copy-object \
  --bucket my-terraform-state \
  --copy-source my-terraform-state/project/terraform.tfstate?versionId=GOOD_VERSION \
  --key project/terraform.tfstate
```

#### **Locked State (Orphaned Lock)**

```bash
# Check error for Lock ID
# Error: Error acquiring the state lock
# Lock Info:
#   ID:        abc123-def456-ghi789
#   Path:      ...
#   Operation: OperationTypeApply
#   Who:       user@hostname
#   Created:   2025-12-19 10:30:00

# Force unlock
terraform force-unlock abc123-def456-ghi789

# Or remove lock from DynamoDB
aws dynamodb delete-item \
  --table-name terraform-state-lock \
  --key '{"LockID": {"S": "my-bucket/project/terraform.tfstate"}}'
```

---

### 🎓 Complete Import Workflow Example

**Scenario:** Import existing AWS infrastructure into Terraform

```bash
# ==================================================
# Step 1: Discover existing resources
# ==================================================

# List VPCs
aws ec2 describe-vpcs --output table

# List subnets
aws ec2 describe-subnets --output table

# List instances
aws ec2 describe-instances --output table

# List security groups
aws ec2 describe-security-groups --output table

# ==================================================
# Step 2: Create Terraform configuration
# ==================================================
```

```hcl
# File: main.tf

terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "imported/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

provider "aws" {
  region = "us-east-1"
}

# VPC (to be imported)
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "production-vpc"
  }
}

# Subnets (to be imported)
resource "aws_subnet" "public_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet-1"
  }
}

resource "aws_subnet" "public_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet-2"
  }
}

# Security Group (to be imported)
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
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
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "web-sg"
  }
}

# Instances (to be imported)
resource "aws_instance" "web_1" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public_1.id
  vpc_security_group_ids = [aws_security_group.web.id]
  
  tags = {
    Name = "web-server-1"
  }
}

resource "aws_instance" "web_2" {
  ami                    = "ami-0c55b159cbfafe1f0"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public_2.id
  vpc_security_group_ids = [aws_security_group.web.id]
  
  tags = {
    Name = "web-server-2"
  }
}
```

```bash
# ==================================================
# Step 3: Initialize
# ==================================================

terraform init

# ==================================================
# Step 4: Import resources
# ==================================================

# Create import script
cat > import.sh <<'EOF'
#!/bin/bash
set -e

echo "Importing VPC..."
terraform import aws_vpc.main vpc-0a1b2c3d4e5f6g7h8

echo "Importing Subnets..."
terraform import aws_subnet.public_1 subnet-111111111111
terraform import aws_subnet.public_2 subnet-222222222222

echo "Importing Security Group..."
terraform import aws_security_group.web sg-web1234567890

echo "Importing Instances..."
terraform import aws_instance.web_1 i-0123456789abcdef0
terraform import aws_instance.web_2 i-0fedcba9876543210

echo "Import complete!"
EOF

chmod +x import.sh
./import.sh

# ==================================================
# Step 5: Verify and adjust configuration
# ==================================================

terraform plan

# If plan shows changes, update your Terraform code to match reality
# Iterate until plan shows no changes

# ==================================================
# Step 6: Document and commit
# ==================================================

cat > README.md <<EOF
# Imported Infrastructure

This Terraform configuration manages the following imported resources:
- VPC: vpc-0a1b2c3d4e5f6g7h8
- Subnets: subnet-111111111111, subnet-222222222222
- Security Group: sg-web1234567890
- Instances: i-0123456789abcdef0, i-0fedcba9876543210

## Import Date
$(date)

## Import Process
Resources were imported from existing AWS infrastructure.
See import.sh for the import commands used.
EOF

git add .
git commit -m "Import existing infrastructure into Terraform"
```

---

### ✅ Day 14-15 Checklist

- [x] State commands (list, show, mv, rm)
- [x] Importing existing resources
- [x] Bulk import strategies
- [x] Moving resources between states
- [x] Detecting state drift
- [x] Handling drift (update, fix, ignore)
- [x] State disaster recovery
- [x] Force unlocking
- [x] Complete import workflow

**Next:** Provisioners and post-deployment configuration!

---

## Day 16: Provisioners - Post-Deployment Configuration

### 🎯 Learning Objectives
- Understand provisioners (when to use and avoid)
- Use local-exec provisioner
- Use remote-exec provisioner
- Use file provisioner
- Handle provisioner failures
- Know alternatives to provisioners

---

### ⚠️ Provisioners - Use Sparingly!

**Provisioners** = Run scripts during resource creation/destruction

**❌ Terraform recommends AVOIDING provisioners when possible:**
- Break declarative model
- Create hidden dependencies
- Harder to maintain
- Error-prone

**✅ Better alternatives:**
- Cloud-init / user_data
- Configuration management (Ansible, Chef, Puppet)
- Pre-baked AMIs (Packer)
- Container images

**When provisioners are acceptable:**
- Bootstrapping infrastructure
- Integration with external systems
- No better alternative exists

---

### 🖥️ Local-Exec Provisioner

Runs commands **on the machine running Terraform**

```hcl
# Basic local-exec
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command = "echo ${self.public_ip} > instance_ip.txt"
  }
}
```

#### **Use Cases**

```hcl
# 1. Update DNS after resource creation
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command = <<-EOT
      aws route53 change-resource-record-sets \
        --hosted-zone-id ${var.zone_id} \
        --change-batch file://dns-change.json
    EOT
  }
}

# 2. Trigger external API
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command = "curl -X POST https://api.example.com/notify -d '{\"ip\":\"${self.public_ip}\"}'"
  }
}

# 3. Run Ansible playbook
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' playbook.yml"
  }
}

# 4. Save outputs to file
resource "aws_eks_cluster" "main" {
  name     = "my-cluster"
  role_arn = aws_iam_role.eks.arn
  
  vpc_config {
    subnet_ids = aws_subnet.private[*].id
  }
  
  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --name ${self.name} --region ${var.region}"
  }
}

# 5. Run scripts with environment variables
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command = "./notify-slack.sh"
    
    environment = {
      INSTANCE_ID = self.id
      PUBLIC_IP   = self.public_ip
      ENVIRONMENT = var.environment
    }
  }
}

# 6. Working directory
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "local-exec" {
    command     = "./deploy.sh ${self.public_ip}"
    working_dir = "${path.module}/scripts"
  }
}
```

---

### 🌐 Remote-Exec Provisioner

Runs commands **on the remote resource** (via SSH or WinRM)

```hcl
# Basic remote-exec
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  
  # Connection block required
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
  
  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd",
    ]
  }
}
```

#### **Connection Types**

```hcl
# SSH Connection (Linux)
resource "aws_instance" "linux" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  key_name      = "my-key"
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
    port        = 22
    timeout     = "5m"
  }
  
  provisioner "remote-exec" {
    inline = ["echo 'Connected!'"]
  }
}

# WinRM Connection (Windows)
resource "aws_instance" "windows" {
  ami           = "ami-windows"
  instance_type = "t2.micro"
  
  connection {
    type     = "winrm"
    user     = "Administrator"
    password = var.admin_password
    host     = self.public_ip
    port     = 5985
    https    = false
    insecure = true
    timeout  = "10m"
  }
  
  provisioner "remote-exec" {
    inline = [
      "powershell.exe -Command \"Write-Host 'Connected!'\"",
    ]
  }
}

# SSH with Bastion Host
resource "aws_instance" "private" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.private.id
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.private_ip
    
    # Bastion configuration
    bastion_host        = aws_instance.bastion.public_ip
    bastion_user        = "ec2-user"
    bastion_private_key = file("~/.ssh/id_rsa")
  }
  
  provisioner "remote-exec" {
    inline = ["echo 'Connected via bastion!'"]
  }
}
```

#### **Remote-Exec Modes**

```hcl
# 1. Inline commands
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y nginx",
    "sudo systemctl start nginx",
  ]
}

# 2. Single script
provisioner "remote-exec" {
  script = "scripts/install.sh"
}

# 3. Multiple scripts
provisioner "remote-exec" {
  scripts = [
    "scripts/install-deps.sh",
    "scripts/configure.sh",
    "scripts/start-services.sh",
  ]
}
```

#### **Complete Web Server Example**

```hcl
# File: main.tf

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Allow HTTP and SSH"
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.web.id]
  
  tags = {
    Name = "web-server"
  }
  
  # Connection for remote-exec
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
  
  # Install and configure web server
  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd",
      "echo '<h1>Hello from Terraform!</h1>' | sudo tee /var/www/html/index.html",
    ]
  }
  
  # Save IP locally
  provisioner "local-exec" {
    command = "echo ${self.public_ip} > web_server_ip.txt"
  }
}

output "web_url" {
  value = "http://${aws_instance.web.public_ip}"
}
```

---

### 📁 File Provisioner

Copies files from **local machine** to **remote resource**

```hcl
# Basic file copy
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
  
  # Copy single file
  provisioner "file" {
    source      = "scripts/app.conf"
    destination = "/tmp/app.conf"
  }
  
  # Copy directory
  provisioner "file" {
    source      = "scripts/"
    destination = "/tmp/scripts"
  }
  
  # Copy with content
  provisioner "file" {
    content     = templatefile("config.tpl", { ip = self.private_ip })
    destination = "/tmp/config.ini"
  }
}
```

#### **Complete Application Deployment**

```hcl
# File: main.tf

resource "aws_instance" "app" {
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.app.id]
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
  
  # Upload application files
  provisioner "file" {
    source      = "app/"
    destination = "/tmp/app"
  }
  
  # Upload configuration
  provisioner "file" {
    content = templatefile("${path.module}/templates/app.conf.tpl", {
      db_host     = aws_db_instance.main.endpoint
      db_name     = var.db_name
      db_user     = var.db_user
      environment = var.environment
    })
    destination = "/tmp/app.conf"
  }
  
  # Upload service file
  provisioner "file" {
    source      = "systemd/app.service"
    destination = "/tmp/app.service"
  }
  
  # Install and start application
  provisioner "remote-exec" {
    inline = [
      "sudo yum install -y python3 python3-pip",
      "sudo pip3 install -r /tmp/app/requirements.txt",
      "sudo mv /tmp/app /opt/app",
      "sudo mv /tmp/app.conf /opt/app/config.ini",
      "sudo mv /tmp/app.service /etc/systemd/system/app.service",
      "sudo systemctl daemon-reload",
      "sudo systemctl start app",
      "sudo systemctl enable app",
    ]
  }
}
```

---

### 🔄 Provisioner Types: Creation vs Destruction

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  # Runs when resource is CREATED (default)
  provisioner "local-exec" {
    command = "echo 'Instance created: ${self.id}' >> log.txt"
  }
  
  # Runs when resource is DESTROYED
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance destroyed' >> log.txt"
  }
  
  # Can use self only in creation-time provisioners
  provisioner "local-exec" {
    command = "echo 'IP: ${self.public_ip}' >> log.txt"
  }
  
  # Destroy provisioner - cannot use self
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Cleaning up' >> log.txt"
    # Note: self attributes not available here
  }
}
```

#### **Cleanup Example**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  # Register with monitoring on creation
  provisioner "local-exec" {
    command = "curl -X POST https://monitor.example.com/register -d '{\"instance\":\"${self.id}\"}'"
  }
  
  # Deregister from monitoring on destruction
  provisioner "local-exec" {
    when    = destroy
    command = "curl -X DELETE https://monitor.example.com/deregister/INSTANCE_ID"
    # Note: In real scenario, you'd need to store instance ID separately
  }
}
```

---

### ⚠️ Provisioner Failure Handling

```hcl
# Default: Fail the resource if provisioner fails
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "remote-exec" {
    inline = ["some-command-that-might-fail"]
  }
}

# Continue on failure
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  provisioner "remote-exec" {
    inline     = ["some-command-that-might-fail"]
    on_failure = continue  # Resource still created even if this fails
  }
}

# Multiple provisioners with different failure handling
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  # Critical: Must succeed
  provisioner "remote-exec" {
    inline     = ["sudo yum install -y httpd"]
    on_failure = fail
  }
  
  # Optional: Can fail
  provisioner "remote-exec" {
    inline     = ["sudo yum install -y optional-package"]
    on_failure = continue
  }
  
  # Critical: Must succeed
  provisioner "remote-exec" {
    inline     = ["sudo systemctl start httpd"]
    on_failure = fail
  }
}
```

---

### 🎯 Better Alternatives to Provisioners

#### **1. User Data (Best for AWS)**

```hcl
# Instead of provisioners, use user_data
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo '<h1>Hello from User Data!</h1>' > /var/www/html/index.html
              EOF
  
  user_data_replace_on_change = true
}

# Or use templatefile
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  user_data = templatefile("${path.module}/user_data.sh", {
    db_endpoint = aws_db_instance.main.endpoint
    app_version = var.app_version
  })
}
```

#### **2. Pre-Baked AMIs with Packer**

```hcl
# File: packer-template.pkr.hcl

packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1.0"
    }
  }
}

source "amazon-ebs" "web" {
  ami_name      = "web-server-{{timestamp}}"
  instance_type = "t2.micro"
  region        = "us-east-1"
  source_ami_filter {
    filters = {
      name                = "amzn2-ami-hvm-*-x86_64-gp2"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["amazon"]
  }
  ssh_username = "ec2-user"
}

build {
  sources = ["source.amazon-ebs.web"]
  
  provisioner "shell" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y httpd php php-mysql",
      "sudo systemctl enable httpd",
    ]
  }
  
  provisioner "file" {
    source      = "app/"
    destination = "/tmp/app"
  }
  
  provisioner "shell" {
    inline = [
      "sudo mv /tmp/app/* /var/www/html/",
      "sudo chown -R apache:apache /var/www/html",
    ]
  }
}
```

```hcl
# File: terraform/main.tf

# Use the pre-baked AMI
data "aws_ami" "web" {
  most_recent = true
  owners      = ["self"]
  
  filter {
    name   = "name"
    values = ["web-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.web.id
  instance_type = "t2.micro"
  
  # No provisioners needed! Application already installed.
}
```

#### **3. Configuration Management Tools**

```hcl
# Trigger Ansible after instance creation
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  
  tags = {
    Name = "web-server"
  }
  
  provisioner "local-exec" {
    command = <<-EOT
      sleep 30  # Wait for instance to be ready
      ansible-playbook \
        -i '${self.public_ip},' \
        -u ec2-user \
        --private-key ~/.ssh/id_rsa \
        playbook.yml
    EOT
  }
}
```

#### **4. Cloud-Init**

```hcl
# cloud-init config
data "cloudinit_config" "web" {
  gzip          = true
  base64_encode = true
  
  part {
    content_type = "text/cloud-config"
    content = yamlencode({
      package_update = true
      packages = [
        "httpd",
        "php",
        "php-mysql"
      ]
      runcmd = [
        ["systemctl", "start", "httpd"],
        ["systemctl", "enable", "httpd"],
      ]
      write_files = [
        {
          path    = "/var/www/html/index.php"
          content = file("${path.module}/app/index.php")
          owner   = "apache:apache"
        }
      ]
    })
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  user_data     = data.cloudinit_config.web.rendered
}
```

---

### ✅ Day 16 Checklist

- [x] Understand provisioners and their limitations
- [x] local-exec provisioner
- [x] remote-exec provisioner
- [x] file provisioner
- [x] Creation vs destruction provisioners
- [x] Failure handling
- [x] Better alternatives (user_data, Packer, Ansible, cloud-init)

**Next:** Lifecycle rules and advanced resource management!

---

## Day 17: Lifecycle Rules & Advanced Resource Management

### 🎯 Learning Objectives
- Use lifecycle meta-arguments
- Prevent resource destruction
- Create before destroy pattern
- Ignore changes
- Replace triggered by changes
- Handle dependencies correctly

---

### 🔄 Lifecycle Meta-Argument

Control how Terraform creates, updates, and destroys resources.

```hcl
resource "aws_instance" "example" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    create_before_destroy = true
    prevent_destroy       = false
    ignore_changes        = []
    replace_triggered_by  = []
    precondition {
      # conditions
    }
    postcondition {
      # conditions
    }
  }
}
```

---

### 🛡️ Prevent Destroy

Prevent accidental deletion of critical resources.

```hcl
# Protect production database
resource "aws_db_instance" "production" {
  identifier     = "prod-db"
  engine         = "mysql"
  instance_class = "db.t3.micro"
  
  lifecycle {
    prevent_destroy = true
  }
}

# Trying to destroy will fail:
# Error: Instance cannot be destroyed
# Resource aws_db_instance.production has lifecycle.prevent_destroy set
```

#### **Conditional prevent_destroy**

```hcl
variable "environment" {
  type = string
}

locals {
  is_production = var.environment == "prod"
}

resource "aws_db_instance" "main" {
  identifier     = "${var.environment}-db"
  engine         = "mysql"
  instance_class = "db.t3.micro"
  
  lifecycle {
    prevent_destroy = local.is_production
  }
}
```

#### **S3 Bucket Protection**

```hcl
resource "aws_s3_bucket" "important_data" {
  bucket = "my-important-data-bucket"
  
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_versioning" "important_data" {
  bucket = aws_s3_bucket.important_data.id
  
  versioning_configuration {
    status = "Enabled"
  }
  
  lifecycle {
    prevent_destroy = true
  }
}
```

---

### 🔄 Create Before Destroy

Create replacement before destroying original (minimizes downtime).

```hcl
# Default behavior (destroy then create)
# Results in downtime!
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  # Change AMI:
  # 1. Destroy old instance
  # 2. Create new instance
  # ⚠️ Downtime!
}

# Create before destroy (zero downtime)
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    create_before_destroy = true
  }
  
  # Change AMI:
  # 1. Create new instance
  # 2. Destroy old instance
  # ✅ No downtime!
}
```

#### **Launch Configuration Example**

```hcl
# Launch configurations are immutable
# Any change requires replacement
resource "aws_launch_configuration" "web" {
  name_prefix   = "web-"
  image_id      = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "web" {
  launch_configuration = aws_launch_configuration.web.id
  min_size             = 2
  max_size             = 10
  desired_capacity     = 2
  
  lifecycle {
    create_before_destroy = true
  }
}
```

#### **Security Group with Create Before Destroy**

```hcl
resource "aws_security_group" "app" {
  name        = "app-sg-${random_id.sg.hex}"
  description = "Security group for app"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "random_id" "sg" {
  byte_length = 4
  
  keepers = {
    # Force new security group when rules change
    ingress_rules = jsonencode(["80", "443"])
  }
}
```

---

### 🙈 Ignore Changes

Ignore changes to specific attributes (useful for external modifications).

```hcl
# Ignore all changes to tags
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name = "web-server"
  }
  
  lifecycle {
    ignore_changes = [tags]
  }
  
  # Manual tag changes won't be reverted
}

# Ignore specific tag
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  tags = {
    Name        = "web-server"
    Environment = "prod"
  }
  
  lifecycle {
    ignore_changes = [tags["Environment"]]
  }
}

# Ignore AMI changes (useful for auto-patching)
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  lifecycle {
    ignore_changes = [ami]
  }
  
  # AMI can be updated manually without Terraform reverting
}

# Ignore multiple attributes
resource "aws_autoscaling_group" "web" {
  launch_configuration = aws_launch_configuration.web.id
  min_size             = 2
  max_size             = 10
  desired_capacity     = 5
  
  lifecycle {
    ignore_changes = [
      desired_capacity,  # Allow auto-scaling to change this
      target_group_arns, # Allow external changes
    ]
  }
}

# Ignore all changes (dangerous!)
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    ignore_changes = all
  }
  
  # Terraform will never update this resource
  # Only useful for imported resources you don't want to manage
}
```

#### **Real-World Example: Auto-Scaling**

```hcl
resource "aws_autoscaling_group" "web" {
  name                 = "web-asg"
  launch_configuration = aws_launch_configuration.web.id
  vpc_zone_identifier  = aws_subnet.private[*].id
  
  min_size         = var.min_size
  max_size         = var.max_size
  desired_capacity = var.desired_size
  
  health_check_type         = "ELB"
  health_check_grace_period = 300
  
  target_group_arns = [aws_lb_target_group.web.arn]
  
  lifecycle {
    create_before_destroy = true
    
    # Allow ASG to scale without Terraform reverting
    ignore_changes = [
      desired_capacity,  # Auto-scaling changes this
      target_group_arns, # May be updated by deployment tools
    ]
  }
  
  tag {
    key                 = "Name"
    value               = "web-server"
    propagate_at_launch = true
  }
}
```

---

### 🔄 Replace Triggered By

Force replacement when specific resources change.

```hcl
# Force instance replacement when certificate changes
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    replace_triggered_by = [
      aws_acm_certificate.web.id
    ]
  }
}

resource "aws_acm_certificate" "web" {
  domain_name       = "example.com"
  validation_method = "DNS"
}

# Replace all instances when launch template changes
resource "aws_launch_template" "web" {
  name_prefix   = "web-"
  image_id      = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
}

resource "aws_instance" "web" {
  count = 3
  
  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }
  
  lifecycle {
    replace_triggered_by = [
      aws_launch_template.web.id
    ]
  }
}

# Replace based on null_resource trigger
resource "null_resource" "app_version" {
  triggers = {
    version = var.app_version
  }
}

resource "aws_instance" "app" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  
  lifecycle {
    replace_triggered_by = [
      null_resource.app_version
    ]
  }
}
```

---

### ✅ Preconditions and Postconditions

Validate assumptions before/after resource operations.

```hcl
# Precondition: Check before creating resource
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  lifecycle {
    precondition {
      condition     = data.aws_ami.selected.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture."
    }
    
    precondition {
      condition     = contains(["t2.micro", "t2.small", "t2.medium"], var.instance_type)
      error_message = "Instance type must be t2.micro, t2.small, or t2.medium."
    }
  }
}

# Postcondition: Verify after creating resource
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  lifecycle {
    postcondition {
      condition     = self.public_ip != ""
      error_message = "Instance must have a public IP address."
    }
    
    postcondition {
      condition     = self.instance_state == "running"
      error_message = "Instance must be in running state."
    }
  }
}

# Data source with postcondition
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  
  lifecycle {
    postcondition {
      condition     = self.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture."
    }
    
    postcondition {
      condition     = self.root_device_type == "ebs"
      error_message = "AMI must use EBS root device."
    }
  }
}
```

#### **Complex Validation Example**

```hcl
variable "environment" {
  type = string
}

variable "instance_type" {
  type = string
}

variable "multi_az" {
  type = bool
}

locals {
  production_instance_types = ["t3.large", "t3.xlarge", "m5.large", "m5.xlarge"]
  valid_environments        = ["dev", "staging", "prod"]
}

resource "aws_db_instance" "main" {
  identifier     = "${var.environment}-database"
  engine         = "mysql"
  instance_class = var.instance_type
  multi_az       = var.multi_az
  
  lifecycle {
    # Validate environment
    precondition {
      condition     = contains(local.valid_environments, var.environment)
      error_message = "Environment must be one of: ${join(", ", local.valid_environments)}."
    }
    
    # Production requirements
    precondition {
      condition = (
        var.environment != "prod" ||
        (contains(local.production_instance_types, var.instance_type) && var.multi_az)
      )
      error_message = "Production databases must use ${join(", ", local.production_instance_types)} and multi_az=true."
    }
    
    # Verify after creation
    postcondition {
      condition     = self.status == "available"
      error_message = "Database must be in available state after creation."
    }
    
    postcondition {
      condition = (
        var.environment != "prod" ||
        self.backup_retention_period >= 7
      )
      error_message = "Production databases must have backup retention >= 7 days."
    }
  }
}
```

---

### 🎓 Complete Lifecycle Example

```hcl
# ==================================================
# File: main.tf
# ==================================================

variable "environment" {
  type = string
}

variable "app_version" {
  type = string
}

locals {
  is_production = var.environment == "prod"
}

# S3 bucket for application assets (protected)
resource "aws_s3_bucket" "assets" {
  bucket = "${var.environment}-app-assets"
  
  lifecycle {
    prevent_destroy = local.is_production
  }
}

# Application version tracker
resource "null_resource" "app_version_tracker" {
  triggers = {
    version = var.app_version
  }
}

# Launch template (immutable - use create_before_destroy)
resource "aws_launch_template" "app" {
  name_prefix   = "${var.environment}-app-"
  image_id      = data.aws_ami.app.id
  instance_type = var.environment == "prod" ? "t3.large" : "t2.micro"
  
  user_data = base64encode(templatefile("${path.module}/user_data.sh", {
    app_version = var.app_version
    environment = var.environment
  }))
  
  lifecycle {
    create_before_destroy = true
    
    precondition {
      condition     = data.aws_ami.app.architecture == "x86_64"
      error_message = "AMI must be x86_64 architecture."
    }
  }
}

# Auto Scaling Group
resource "aws_autoscaling_group" "app" {
  name                = "${var.environment}-app-asg"
  vpc_zone_identifier = aws_subnet.private[*].id
  target_group_arns   = [aws_lb_target_group.app.arn]
  
  min_size         = local.is_production ? 3 : 1
  max_size         = local.is_production ? 10 : 2
  desired_capacity = local.is_production ? 5 : 1
  
  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }
  
  health_check_type         = "ELB"
  health_check_grace_period = 300
  
  lifecycle {
    create_before_destroy = true
    
    # Allow auto-scaling to manage capacity
    ignore_changes = [
      desired_capacity,
    ]
    
    # Force replacement when app version changes
    replace_triggered_by = [
      null_resource.app_version_tracker
    ]
  }
  
  tag {
    key                 = "Name"
    value               = "${var.environment}-app-server"
    propagate_at_launch = true
  }
  
  tag {
    key                 = "Environment"
    value               = var.environment
    propagate_at_launch = true
  }
  
  tag {
    key                 = "AppVersion"
    value               = var.app_version
    propagate_at_launch = true
  }
}

# Database (protected in production, ignore minor version upgrades)
resource "aws_db_instance" "main" {
  identifier     = "${var.environment}-database"
  engine         = "mysql"
  engine_version = "8.0"
  instance_class = local.is_production ? "db.r5.large" : "db.t3.micro"
  
  allocated_storage     = local.is_production ? 100 : 20
  max_allocated_storage = local.is_production ? 1000 : 100
  
  multi_az               = local.is_production
  backup_retention_period = local.is_production ? 30 : 7
  
  lifecycle {
    prevent_destroy = local.is_production
    
    # Allow AWS to update minor versions
    ignore_changes = [
      engine_version,  # Allow patch updates
    ]
    
    # Validate production requirements
    precondition {
      condition = (
        !local.is_production ||
        (self.multi_az && self.backup_retention_period >= 7)
      )
      error_message = "Production database must have multi_az=true and backup_retention >= 7 days."
    }
    
    # Verify after creation
    postcondition {
      condition     = self.status == "available"
      error_message = "Database must be available after creation."
    }
  }
}

# Security group (allow external updates to rules)
resource "aws_security_group" "app" {
  name        = "${var.environment}-app-sg"
  description = "Security group for app servers"
  vpc_id      = aws_vpc.main.id
  
  lifecycle {
    create_before_destroy = true
    
    # Allow external security tools to manage rules
    ignore_changes = [
      ingress,
      egress,
    ]
  }
}

# ==================================================
# Outputs
# ==================================================

output "asg_name" {
  description = "Auto Scaling Group name"
  value       = aws_autoscaling_group.app.name
}

output "database_endpoint" {
  description = "Database endpoint"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}
```

**Usage:**

```bash
# Development
terraform apply -var="environment=dev" -var="app_version=1.0.0"

# Production (database protected)
terraform apply -var="environment=prod" -var="app_version=1.0.0"

# Update app version (triggers ASG replacement)
terraform apply -var="environment=prod" -var="app_version=1.1.0"

# Try to destroy production database (fails)
terraform destroy -target=aws_db_instance.main
# Error: Instance cannot be destroyed
```

---

### ✅ Day 17 Checklist

- [x] Lifecycle meta-argument
- [x] prevent_destroy
- [x] create_before_destroy
- [x] ignore_changes
- [x] replace_triggered_by
- [x] precondition and postcondition
- [x] Real-world lifecycle patterns
- [x] Complete production example

**Next:** Terraform Cloud and Enterprise features!

---

## Day 18: Terraform Cloud & Collaboration

### 🎯 Learning Objectives
- Understand Terraform Cloud benefits
- Set up Terraform Cloud workspaces
- Configure VCS integration
- Use remote runs
- Implement team collaboration
- Use Sentinel policies (Enterprise)

---

### ☁️ What is Terraform Cloud?

**Terraform Cloud** = HashiCorp's managed service for Terraform

**Benefits:**
- ✅ Remote state storage (encrypted)
- ✅ Remote execution (runs in cloud)
- ✅ Collaboration (teams, RBAC)
- ✅ VCS integration (GitHub, GitLab, Bitbucket)
- ✅ Cost estimation
- ✅ Policy as code (Sentinel)
- ✅ Private module registry
- ✅ Audit logs
- ✅ UI for viewing state and runs

**Pricing:**
- **Free**: Up to 5 users, remote state, basic features
- **Team**: $20/user/month, team management, SSO
- **Business**: Custom pricing, Sentinel policies, audit logs

**Terraform Cloud vs Enterprise:**
- **Cloud**: SaaS, managed by HashiCorp
- **Enterprise**: Self-hosted, more control

---

### 🚀 Getting Started with Terraform Cloud

#### **1. Create Account**

```bash
# Visit https://app.terraform.io/signup

# Or use CLI
terraform login

# Opens browser for authentication
# Saves token to ~/.terraform.d/credentials.tfrc.json
```

#### **2. Create Organization**

```bash
# Via Web UI:
# 1. Go to https://app.terraform.io
# 2. Click "Create an organization"
# 3. Enter organization name (e.g., "my-company")
```

#### **3. Configure Terraform**

```hcl
# File: main.tf

terraform {
  cloud {
    organization = "my-company"
    
    workspaces {
      name = "my-app-production"
    }
  }
  
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
```

#### **4. Initialize and Run**

```bash
# Initialize (connects to Terraform Cloud)
terraform init

# Plan (runs remotely)
terraform plan

# Apply (runs remotely)
terraform apply

# View in UI
# https://app.terraform.io/app/my-company/workspaces/my-app-production/runs
```

---

### 🏢 Workspaces in Terraform Cloud

**Workspace** = Container for Terraform configuration, state, and variables

```plaintext
Organization: my-company
├── Workspace: frontend-prod
│   ├── State
│   ├── Variables
│   └── Runs
├── Workspace: frontend-staging
│   ├── State
│   ├── Variables
│   └── Runs
└── Workspace: backend-prod
    ├── State
    ├── Variables
    └── Runs
```

#### **Create Workspace via Terraform**

```hcl
terraform {
  cloud {
    organization = "my-company"
    
    workspaces {
      # Single workspace
      name = "my-app-production"
      
      # Or use tags for multiple workspaces
      # tags = ["app:myapp", "env:prod"]
    }
  }
}
```

#### **Workspace Variables**

Set via UI or API:

```bash
# Via UI:
# 1. Go to workspace
# 2. Click "Variables"
# 3. Add variables

# Variable types:
# - Terraform Variables (var.xxx)
# - Environment Variables (AWS_ACCESS_KEY_ID, etc.)

# Mark as sensitive to hide values
```

**Example:**

```
Terraform Variables:
- region = "us-east-1"
- instance_type = "t3.large"
- environment = "production"

Environment Variables:
- AWS_ACCESS_KEY_ID = "AKIAxxxx"  (sensitive)
- AWS_SECRET_ACCESS_KEY = "xxxxx" (sensitive)
```

---

### 🔗 VCS Integration (GitHub, GitLab, Bitbucket)

Connect workspace to Git repository for automatic runs.

#### **Setup VCS Integration**

```bash
# 1. In Terraform Cloud UI:
# Settings → VCS Providers → Add VCS Provider
# Choose: GitHub, GitLab, Bitbucket, etc.

# 2. Authorize Terraform Cloud

# 3. Create workspace with VCS connection:
# - Select repository
# - Choose branch (e.g., main)
# - Set working directory (if code is in subdirectory)
```

#### **Workflow**

```plaintext
Developer Workflow:
1. Developer pushes code to GitHub
2. Terraform Cloud detects push
3. Automatically triggers terraform plan
4. Shows plan in GitHub PR as comment
5. Team reviews plan
6. Merge PR → triggers terraform apply
```

#### **Configuration**

```hcl
# .terraform.cloud.json (in repository root)
{
  "organization": "my-company",
  "workspaces": {
    "name": "my-app-production"
  }
}
```

**Working Directory:**

```
repo/
├── frontend/
│   └── main.tf  ← Workspace "frontend" uses this directory
├── backend/
│   └── main.tf  ← Workspace "backend" uses this directory
└── infrastructure/
    └── main.tf  ← Workspace "infrastructure" uses this directory
```

**Trigger Patterns:**

```bash
# Workspace settings:
# VCS → Trigger Patterns

# Run only when specific paths change:
# - Always trigger: false
# - Patterns:
#   - /frontend/**
#   - /shared/**

# Example: frontend workspace only runs when frontend/ or shared/ changes
```

---

### 🎯 Run Triggers

Automatically trigger workspace runs based on other workspaces.

```plaintext
Example:
1. "networking" workspace creates VPC
2. "database" workspace depends on VPC
3. When "networking" completes → auto-trigger "database"
```

**Setup:**

```bash
# In dependent workspace (e.g., "database"):
# Settings → Run Triggers → Source Workspaces
# Add: "networking"

# Now when "networking" apply completes → "database" runs automatically
```

---

### 👥 Team Collaboration

#### **Teams and Permissions**

```bash
# Organization Settings → Teams

# Create teams:
# - Developers (read/write)
# - Operators (admin)
# - Auditors (read-only)

# Workspace permissions:
# - Read: View state, runs
# - Plan: Trigger plans
# - Write: Approve applies
# - Admin: Manage workspace settings
```

**Example Structure:**

```
Organization: my-company
├── Team: developers
│   ├── Workspace: dev-* (write)
│   └── Workspace: prod-* (plan)
├── Team: operators
│   └── Workspace: * (admin)
└── Team: managers
    └── Workspace: * (read)
```

#### **Approval Workflow**

```hcl
# Workspace settings:
# Settings → General → Apply Method: Manual

# Workflow:
# 1. Developer pushes code
# 2. Terraform plan runs automatically
# 3. Plan requires approval
# 4. Operator reviews and approves
# 5. Terraform apply runs
```

---

### 💰 Cost Estimation

Terraform Cloud shows estimated AWS costs before applying.

```plaintext
Plan output:

Resources: 12 to add, 5 to change, 0 to destroy.

Cost Estimation:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
+ aws_instance.web
  +$8.76 per month

+ aws_db_instance.main
  +$50.00 per month

+ aws_lb.main
  +$20.00 per month

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Monthly Cost: $78.76
Cost Delta: +$25.00 from current
```

---

### 🛡️ Sentinel Policies (Enterprise/Business)

**Sentinel** = Policy as code framework

**Use cases:**
- Enforce tagging standards
- Require encryption
- Limit instance types
- Enforce naming conventions
- Check for security groups
- Validate CIDR ranges

#### **Sentinel Policy Example**

```hcl
# File: require-tags.sentinel

import "tfplan/v2" as tfplan

# Get all AWS instances
all_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_instance" and
    rc.mode is "managed" and
    (rc.change.actions contains "create" or rc.change.actions contains "update")
}

# Rule: All instances must have required tags
required_tags = ["Name", "Environment", "Owner"]

instance_has_required_tags = rule {
    all all_instances as _, instance {
        all required_tags as tag {
            instance.change.after.tags contains tag
        }
    }
}

# Main rule
main = rule {
    instance_has_required_tags
}
```

```hcl
# File: enforce-encryption.sentinel

import "tfplan/v2" as tfplan

# Get all S3 buckets
all_buckets = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket" and
    rc.mode is "managed"
}

# Get all bucket encryption configurations
all_bucket_encryption = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_s3_bucket_server_side_encryption_configuration" and
    rc.mode is "managed"
}

# Rule: All S3 buckets must have encryption
main = rule {
    length(all_buckets) == length(all_bucket_encryption)
}
```

```hcl
# File: restrict-instance-types.sentinel

import "tfplan/v2" as tfplan

# Allowed instance types
allowed_types = ["t3.micro", "t3.small", "t3.medium"]

# Get all instances
all_instances = filter tfplan.resource_changes as _, rc {
    rc.type is "aws_instance" and
    rc.mode is "managed" and
    (rc.change.actions contains "create" or rc.change.actions contains "update")
}

# Rule: Instance types must be in allowed list
instance_type_allowed = rule {
    all all_instances as _, instance {
        instance.change.after.instance_type in allowed_types
    }
}

main = rule {
    instance_type_allowed
}
```

#### **Policy Sets**

```hcl
# sentinel.hcl

policy "require-tags" {
    enforcement_level = "hard-mandatory"  # Must pass
}

policy "enforce-encryption" {
    enforcement_level = "hard-mandatory"  # Must pass
}

policy "restrict-instance-types" {
    enforcement_level = "soft-mandatory"  # Can override
}

policy "check-naming-convention" {
    enforcement_level = "advisory"  # Warning only
}
```

**Enforcement Levels:**
- `advisory` - Warning only, doesn't block
- `soft-mandatory` - Must pass, but can be overridden
- `hard-mandatory` - Must pass, cannot be overridden

---

### 📦 Private Module Registry

Share modules within your organization.

#### **Publish Module**

```bash
# 1. Create GitHub repository:
# terraform-aws-vpc (naming convention important!)

# 2. Add tag for version:
git tag v1.0.0
git push origin v1.0.0

# 3. In Terraform Cloud UI:
# Registry → Modules → Publish → Connect to VCS
# Select repository: terraform-aws-vpc

# Module is now available as:
# my-company/vpc/aws
```

#### **Use Private Module**

```hcl
terraform {
  cloud {
    organization = "my-company"
    workspaces {
      name = "my-app"
    }
  }
}

module "vpc" {
  source  = "app.terraform.io/my-company/vpc/aws"
  version = "1.0.0"
  
  project_name = "myapp"
  environment  = "prod"
  vpc_cidr     = "10.0.0.0/16"
}
```

---

### 🎓 Complete Terraform Cloud Setup Example

```hcl
# ==================================================
# File: main.tf
# ==================================================

terraform {
  required_version = ">= 1.0"
  
  # Terraform Cloud configuration
  cloud {
    organization = "my-company"
    
    workspaces {
      name = "production-infrastructure"
    }
  }
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# AWS provider (credentials from environment variables)
provider "aws" {
  region = var.region
}

# ==================================================
# Variables (set in Terraform Cloud UI)
# ==================================================

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

# ==================================================
# Resources
# ==================================================

module "vpc" {
  source  = "app.terraform.io/my-company/vpc/aws"
  version = "1.0.0"
  
  project_name = "myapp"
  environment  = var.environment
  
  vpc_cidr             = "10.0.0.0/16"
  availability_zones   = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
}

resource "aws_instance" "web" {
  count = 3
  
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = var.instance_type
  subnet_id              = module.vpc.public_subnet_ids[count.index]
  vpc_security_group_ids = [aws_security_group.web.id]
  
  tags = {
    Name        = "web-${count.index + 1}"
    Environment = var.environment
    Owner       = "platform-team"
    ManagedBy   = "Terraform"
  }
}

# ==================================================
# Outputs
# ==================================================

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "instance_ips" {
  description = "Instance public IPs"
  value       = aws_instance.web[*].public_ip
}
```

**Terraform Cloud Configuration:**

```bash
# Workspace: production-infrastructure
# Settings:

# General:
# - Execution Mode: Remote
# - Apply Method: Manual (requires approval)
# - Terraform Version: 1.7.0

# VCS:
# - Repository: github.com/mycompany/terraform-infrastructure
# - Branch: main
# - Working Directory: /production

# Variables (Terraform):
# - region = "us-east-1"
# - environment = "production"
# - instance_type = "t3.large"

# Variables (Environment - Sensitive):
# - AWS_ACCESS_KEY_ID = "AKIAxxxx"
# - AWS_SECRET_ACCESS_KEY = "xxxxx"

# Run Triggers:
# - Source Workspaces: ["networking-production"]

# Notifications:
# - Slack: #infrastructure-alerts
# - Email: platform-team@company.com

# Team Access:
# - developers: Plan
# - operators: Write
# - managers: Read
```

**Workflow:**

```bash
# 1. Developer creates branch
git checkout -b feature/add-cache

# 2. Makes changes
# ... edit main.tf ...

# 3. Commits and pushes
git add .
git commit -m "Add ElastiCache cluster"
git push origin feature/add-cache

# 4. Creates Pull Request
# GitHub → Create PR

# 5. Terraform Cloud automatically:
#    - Detects PR
#    - Runs terraform plan
#    - Posts plan as PR comment

# 6. Team reviews plan in PR comment

# 7. PR is approved and merged

# 8. Terraform Cloud automatically:
#    - Detects merge to main
#    - Runs terraform plan
#    - Waits for approval (Manual apply)

# 9. Operator reviews plan in Terraform Cloud UI

# 10. Operator clicks "Confirm & Apply"

# 11. Terraform apply runs remotely

# 12. Notifications sent to Slack/Email

# 13. State is saved securely in Terraform Cloud
```

---

### ✅ Day 18 Checklist

- [x] Terraform Cloud benefits
- [x] Account and organization setup
- [x] Workspace configuration
- [x] VCS integration (GitHub, GitLab)
- [x] Remote runs
- [x] Team collaboration and RBAC
- [x] Run triggers
- [x] Cost estimation
- [x] Sentinel policies (Policy as Code)
- [x] Private module registry
- [x] Complete collaboration workflow

**Next:** Best practices for project structure and organization!

---

## Day 19: Project Structure & Organization

### 🎯 Learning Objectives
- Organize Terraform projects effectively
- Structure multi-environment setups
- Use naming conventions
- Manage large codebases
- Implement DRY principles

---

### 📁 Project Structure Patterns

#### **Pattern 1: Simple Single Environment**

```
terraform/
├── main.tf           # Main resources
├── variables.tf      # Input variables
├── outputs.tf        # Output values
├── providers.tf      # Provider configuration
├── versions.tf       # Version constraints
├── terraform.tfvars  # Variable values (gitignored)
└── README.md         # Documentation
```

**Best for:**
- Small projects
- Single environment
- Learning/prototyping

---

#### **Pattern 2: Multi-Environment with Workspaces**

```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
├── versions.tf
├── dev.tfvars        # Dev variables
├── staging.tfvars    # Staging variables
├── prod.tfvars       # Prod variables
└── README.md
```

**Usage:**

```bash
# Development
terraform workspace select dev
terraform apply -var-file="dev.tfvars"

# Production
terraform workspace select prod
terraform apply -var-file="prod.tfvars"
```

**Best for:**
- Medium projects
- Similar infrastructure across environments
- Same team managing all environments

---

#### **Pattern 3: Separate Environment Directories**

```
terraform/
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── compute/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── database/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── backend.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── backend.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── backend.tf
│       └── terraform.tfvars
└── README.md
```

**Best for:**
- Large projects
- Different architectures per environment
- Separate teams per environment
- Strict isolation required

---

#### **Pattern 4: Layered Architecture**

```
terraform/
├── 00-bootstrap/         # Account setup, state backend
│   ├── main.tf
│   └── terraform.tfvars
├── 10-networking/        # VPC, subnets, routing
│   ├── main.tf
│   ├── backend.tf
│   └── terraform.tfvars
├── 20-security/          # IAM, security groups
│   ├── main.tf
│   ├── backend.tf
│   └── terraform.tfvars
├── 30-data/              # RDS, ElastiCache, S3
│   ├── main.tf
│   ├── backend.tf
│   └── terraform.tfvars
├── 40-compute/           # EC2, ECS, Lambda
│   ├── main.tf
│   ├── backend.tf
│   └── terraform.tfvars
└── 50-applications/      # Application-specific resources
    ├── main.tf
    ├── backend.tf
    └── terraform.tfvars
```

**Deployment order:**

```bash
# 1. Bootstrap (run once)
cd 00-bootstrap
terraform apply

# 2. Networking
cd ../10-networking
terraform apply

# 3. Security
cd ../20-security
terraform apply

# 4. Data layer
cd ../30-data
terraform apply

# 5. Compute layer
cd ../40-compute
terraform apply

# 6. Applications
cd ../50-applications
terraform apply
```

**Best for:**
- Very large projects
- Complex dependencies
- Multiple teams owning different layers
- Gradual infrastructure changes

---

### 📋 File Organization Best Practices

#### **Core Files**

```hcl
# ==================================================
# File: versions.tf
# ==================================================
# Terraform and provider version constraints

terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

# ==================================================
# File: providers.tf
# ==================================================
# Provider configurations

provider "aws" {
  region = var.region
  
  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

provider "aws" {
  alias  = "us-west-2"
  region = "us-west-2"
  
  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

# ==================================================
# File: backend.tf
# ==================================================
# Remote state backend

terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

# ==================================================
# File: variables.tf
# ==================================================
# Input variables

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  validation {
    condition     = length(var.project_name) > 0
    error_message = "Project name cannot be empty."
  }
}

variable "environment" {
  description = "Environment name"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# ==================================================
# File: locals.tf
# ==================================================
# Local values

locals {
  name_prefix = "${var.project_name}-${var.environment}"
  
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
  
  # Environment-specific configuration
  config = {
    dev = {
      instance_count = 1
      instance_type  = "t3.micro"
      multi_az       = false
    }
    staging = {
      instance_count = 2
      instance_type  = "t3.small"
      multi_az       = false
    }
    prod = {
      instance_count = 5
      instance_type  = "t3.large"
      multi_az       = true
    }
  }
  
  env_config = local.config[var.environment]
}

# ==================================================
# File: data.tf
# ==================================================
# Data sources

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# ==================================================
# File: main.tf
# ==================================================
# Main resources

module "vpc" {
  source = "./modules/vpc"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_cidr             = var.vpc_cidr
  availability_zones   = var.availability_zones
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
}

module "compute" {
  source = "./modules/compute"
  
  project_name = var.project_name
  environment  = var.environment
  
  vpc_id              = module.vpc.vpc_id
  subnet_ids          = module.vpc.private_subnet_ids
  instance_count      = local.env_config.instance_count
  instance_type       = local.env_config.instance_type
}

# ==================================================
# File: outputs.tf
# ==================================================
# Output values

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "instance_ids" {
  description = "EC2 instance IDs"
  value       = module.compute.instance_ids
}

# ==================================================
# File: terraform.tfvars
# ==================================================
# Variable values (add to .gitignore!)

region       = "us-east-1"
project_name = "myapp"
environment  = "prod"

vpc_cidr             = "10.0.0.0/16"
availability_zones   = ["us-east-1a", "us-east-1b", "us-east-1c"]
public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
```

---

### 🎯 Naming Conventions

#### **Resource Names**

```hcl
# Pattern: {project}-{environment}-{resource_type}-{description}

# Good ✅
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

resource "aws_subnet" "public" {
  count = 3
  
  vpc_id     = aws_vpc.main.id
  cidr_block = var.public_subnet_cidrs[count.index]
  
  tags = {
    Name = "${var.project_name}-${var.environment}-public-subnet-${count.index + 1}"
  }
}

resource "aws_instance" "web" {
  count = 5
  
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t3.micro"
  
  tags = {
    Name = "${var.project_name}-${var.environment}-web-${count.index + 1}"
  }
}

# Bad ❌
resource "aws_vpc" "vpc1" {  # Unclear name
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "my-vpc"  # Not environment-specific
  }
}
```

#### **Variable Names**

```hcl
# Good ✅
variable "vpc_cidr_block" {
  description = "CIDR block for VPC"
  type        = string
}

variable "database_instance_class" {
  description = "RDS instance class"
  type        = string
}

variable "enable_nat_gateway" {
  description = "Enable NAT gateway for private subnets"
  type        = bool
}

# Bad ❌
variable "cidr" {  # Too vague
  type = string
}

variable "db_size" {  # Unclear what "size" means
  type = string
}

variable "nat" {  # Boolean should start with "enable_" or "is_"
  type = bool
}
```

#### **Module Names**

```hcl
# Directory structure
modules/
├── vpc-with-nat/           # Good: descriptive
├── ec2-auto-scaling/       # Good: clear purpose
├── rds-mysql-primary/      # Good: specific
├── s3-static-website/      # Good: use case clear
├── networking/             # OK: generic but acceptable
└── compute/                # OK: generic but acceptable

# Bad examples:
├── module1/                # Bad: meaningless
├── stuff/                  # Bad: too vague
└── resources/              # Bad: too generic
```

---

### 🏗️ Module Organization

#### **Module Structure**

```
modules/
└── vpc/
    ├── README.md          # Module documentation
    ├── main.tf            # Main resources
    ├── variables.tf       # Input variables
    ├── outputs.tf         # Output values
    ├── versions.tf        # Provider requirements
    ├── locals.tf          # Local values (optional)
    ├── data.tf            # Data sources (optional)
    └── examples/          # Usage examples
        ├── complete/
        │   ├── main.tf
        │   └── README.md
        └── simple/
            ├── main.tf
            └── README.md
```

#### **Module README Template**

```markdown
# VPC Module

## Description
Creates a production-ready VPC with public and private subnets across multiple availability zones.

## Features
- [x] Multi-AZ deployment
- [x] NAT Gateway (optional single/multi)
- [x] Internet Gateway for public subnets
- [x] Automatic route table configuration
- [x] VPC Flow Logs (optional)
- [x] DNS support enabled

## Requirements
- Terraform >= 1.5.0
- AWS Provider >= 5.0

## Usage

### Basic Example
```hcl
module "vpc" {
  source = "./modules/vpc"
  
  project_name = "myapp"
  environment  = "prod"
  
  vpc_cidr             = "10.0.0.0/16"
  availability_zones   = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
}
```

### Complete Example
See [examples/complete](./examples/complete)

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|----------|
| project_name | Project name | string | - | yes |
| environment | Environment name | string | - | yes |
| vpc_cidr | VPC CIDR block | string | "10.0.0.0/16" | no |
| enable_nat_gateway | Enable NAT gateway | bool | true | no |

## Outputs

| Name | Description |
|------|-------------|
| vpc_id | VPC ID |
| public_subnet_ids | Public subnet IDs |
| private_subnet_ids | Private subnet IDs |

## Cost Estimation
- VPC: Free
- Internet Gateway: Free
- NAT Gateway: ~$32/month per AZ
- VPC Flow Logs: ~$0.50/GB ingested

**Total (3 AZs): ~$96/month**

## Authors
Platform Team <platform@company.com>

## License
MIT
```

---

### 🔐 Secrets Management

#### **❌ Never Do This**

```hcl
# BAD - Hardcoded secrets
resource "aws_db_instance" "main" {
  username = "admin"
  password = "MyPassword123!"  # ❌ Never hardcode!
}

# BAD - Secrets in tfvars (even if gitignored)
# terraform.tfvars
database_password = "MyPassword123!"  # ❌ Still bad!
```

#### **✅ Use These Instead**

```hcl
# Method 1: AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "prod/database/password"
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = jsondecode(data.aws_secretsmanager_secret_version.db_password.secret_string)["password"]
}

# Method 2: Random password + store in Secrets Manager
resource "random_password" "db_password" {
  length  = 32
  special = true
}

resource "aws_secretsmanager_secret" "db_password" {
  name = "prod/database/password"
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({
    username = "admin"
    password = random_password.db_password.result
  })
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = random_password.db_password.result
  
  # Password is in state, but state should be encrypted
}

# Method 3: Environment variables (for Terraform Cloud)
variable "database_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

# Set as environment variable:
# export TF_VAR_database_password="xxx"

# Or in Terraform Cloud as sensitive variable
```

---

### 📝 Documentation Best Practices

#### **Project README**

```markdown
# Production Infrastructure

Terraform code for managing production infrastructure.

## Architecture

```
┌─────────────────────────────────────────┐
│              AWS Cloud                  │
│  ┌────────────────────────────────┐    │
│  │  VPC (10.0.0.0/16)             │    │
│  │  ┌─────────┐    ┌───────────┐ │    │
│  │  │ Public  │    │  Private  │ │    │
│  │  │ Subnets │───▶│  Subnets  │ │    │
│  │  │  + ALB  │    │   + EC2   │ │    │
│  │  └─────────┘    │   + RDS   │ │    │
│  │       │         └───────────┘ │    │
│  │       │                        │    │
│  │  ┌────▼─────┐                 │    │
│  │  │   IGW    │                 │    │
│  │  └──────────┘                 │    │
│  └────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

## Prerequisites

- Terraform >= 1.5.0
- AWS CLI configured
- S3 bucket for state: `my-terraform-state`
- DynamoDB table for locking: `terraform-state-lock`

## Directory Structure

```
terraform/
├── environments/
│   ├── dev/       # Development environment
│   ├── staging/   # Staging environment
│   └── prod/      # Production environment
└── modules/       # Reusable modules
```

## Usage

### Initial Setup

```bash
# 1. Clone repository
git clone git@github.com:company/terraform-infrastructure.git
cd terraform-infrastructure

# 2. Choose environment
cd environments/prod

# 3. Initialize Terraform
terraform init

# 4. Review plan
terraform plan

# 5. Apply changes
terraform apply
```

### Making Changes

```bash
# 1. Create feature branch
git checkout -b feature/add-cache

# 2. Make changes
# ... edit files ...

# 3. Validate
terraform validate
terraform fmt -recursive

# 4. Plan
terraform plan -out=tfplan

# 5. Create PR
git add .
git commit -m "Add ElastiCache cluster"
git push origin feature/add-cache

# 6. After approval, merge and apply
```

## Environments

### Development
- **Purpose**: Testing and development
- **Scale**: Minimal (1 instance, t3.micro)
- **Cost**: ~$50/month

### Staging
- **Purpose**: Pre-production testing
- **Scale**: Medium (2 instances, t3.small)
- **Cost**: ~$200/month

### Production
- **Purpose**: Live traffic
- **Scale**: High (5+ instances, t3.large, Multi-AZ)
- **Cost**: ~$1,500/month

## State Management

State is stored in S3:
- Bucket: `my-terraform-state`
- Locking: DynamoDB table `terraform-state-lock`
- Encryption: AES256

## Team

- **Owner**: Platform Team
- **On-call**: PagerDuty rotation
- **Slack**: #infrastructure

## Resources

- [Terraform Docs](https://www.terraform.io/docs)
- [AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Internal Wiki](https://wiki.company.com/terraform)
```

---

### ✅ Day 19 Checklist

- [x] Project structure patterns
- [x] File organization
- [x] Naming conventions
- [x] Module organization
- [x] Secrets management
- [x] Documentation best practices

**Next:** Security best practices!

---

## Day 20: Security Best Practices

### 🎯 Learning Objectives
- Secure Terraform state
- Manage secrets properly
- Implement least privilege IAM
- Use security scanning tools
- Follow compliance requirements

---

### 🔒 State Security

#### **Encrypt State at Rest**

```hcl
# S3 backend with encryption
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true                    # ✅ Enable encryption
    kms_key_id     = "arn:aws:kms:us-east-1:ACCOUNT:key/KEY_ID"  # ✅ Use KMS
    dynamodb_table = "terraform-state-lock"
  }
}
```

#### **Restrict State Access**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTerraformStateRead",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::ACCOUNT:role/terraform-role",
          "arn:aws:iam::ACCOUNT:user/terraform-ci"
        ]
      },
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-terraform-state",
        "arn:aws:s3:::my-terraform-state/*"
      ]
    },
    {
      "Sid": "AllowTerraformStateWrite",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT:role/terraform-role"
      },
      "Action": [
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::my-terraform-state/*",
      "Condition": {
        "StringEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    },
    {
      "Sid": "DenyUnencryptedUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-terraform-state/*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    }
  ]
}
```

#### **Enable Versioning and Logging**

```hcl
# State bucket with security features
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state"
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_logging" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  target_bucket = aws_s3_bucket.logs.id
  target_prefix = "terraform-state-logs/"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.terraform_state.arn
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

---

### 🔑 Secrets Management

#### **❌ What NOT to Do**

```hcl
# ❌ Hardcoded credentials
provider "aws" {
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# ❌ Secrets in variables
variable "database_password" {
  default = "MyP@ssw0rd123"
}

# ❌ Secrets in terraform.tfvars (even gitignored)
database_password = "MyP@ssw0rd123"
```

#### **✅ Proper Secrets Management**

```hcl
# Method 1: AWS Secrets Manager
data "aws_secretsmanager_secret" "db_creds" {
  name = "prod/database/credentials"
}

data "aws_secretsmanager_secret_version" "db_creds" {
  secret_id = data.aws_secretsmanager_secret.db_creds.id
}

locals {
  db_creds = jsondecode(data.aws_secretsmanager_secret_version.db_creds.secret_string)
}

resource "aws_db_instance" "main" {
  username = local.db_creds.username
  password = local.db_creds.password
}

# Method 2: Generate and store secrets
resource "random_password" "db_password" {
  length  = 32
  special = true
}

resource "aws_secretsmanager_secret" "db_password" {
  name                    = "prod/database/password"
  recovery_window_in_days = 30
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({
    username = "admin"
    password = random_password.db_password.result
    engine   = "mysql"
  })
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = random_password.db_password.result
}

# Method 3: AWS Systems Manager Parameter Store
resource "aws_ssm_parameter" "db_password" {
  name  = "/prod/database/password"
  type  = "SecureString"
  value = random_password.db_password.result
  
  tags = {
    Environment = "production"
  }
}

data "aws_ssm_parameter" "db_password" {
  name = "/prod/database/password"
}

resource "aws_db_instance" "main" {
  username = "admin"
  password = data.aws_ssm_parameter.db_password.value
}
```

#### **Sensitive Variables**

```hcl
# Mark variables as sensitive
variable "database_password" {
  description = "Database password"
  type        = string
  sensitive   = true  # ✅ Hides value in outputs
}

variable "api_key" {
  description = "API key"
  type        = string
  sensitive   = true
}

# Sensitive outputs
output "database_password" {
  description = "Database password"
  value       = random_password.db_password.result
  sensitive   = true  # ✅ Hidden in terraform output
}

# Values are hidden in CLI output but STILL IN STATE FILE!
# Must encrypt state!
```

---

### 👤 IAM Best Practices

#### **Least Privilege Policy**

```hcl
# Bad: Too broad ❌
data "aws_iam_policy_document" "terraform_bad" {
  statement {
    effect    = "Allow"
    actions   = ["*"]
    resources = ["*"]
  }
}

# Good: Specific permissions ✅
data "aws_iam_policy_document" "terraform_good" {
  # VPC management
  statement {
    effect = "Allow"
    actions = [
      "ec2:CreateVpc",
      "ec2:DeleteVpc",
      "ec2:DescribeVpcs",
      "ec2:ModifyVpcAttribute",
      "ec2:CreateSubnet",
      "ec2:DeleteSubnet",
      "ec2:DescribeSubnets",
    ]
    resources = ["*"]
  }
  
  # S3 state bucket access
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
      "s3:ListBucket",
    ]
    resources = [
      "arn:aws:s3:::my-terraform-state",
      "arn:aws:s3:::my-terraform-state/*",
    ]
  }
  
  # DynamoDB state locking
  statement {
    effect = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:DeleteItem",
      "dynamodb:DescribeTable",
    ]
    resources = [
      "arn:aws:dynamodb:*:*:table/terraform-state-lock",
    ]
  }
}

resource "aws_iam_policy" "terraform" {
  name   = "terraform-deployment"
  policy = data.aws_iam_policy_document.terraform_good.json
}
```

#### **Assume Role Pattern**

```hcl
# Terraform role with specific permissions
resource "aws_iam_role" "terraform" {
  name = "terraform-deployment"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = [
            "arn:aws:iam::ACCOUNT:user/terraform-ci",
            "arn:aws:iam::ACCOUNT:role/GitHubActions",
          ]
        }
        Action = "sts:AssumeRole"
        Condition = {
          StringEquals = {
            "sts:ExternalId" = "terraform-deployment-key"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "terraform" {
  role       = aws_iam_role.terraform.name
  policy_arn = aws_iam_policy.terraform.arn
}

# Use in Terraform
provider "aws" {
  region = "us-east-1"
  
  assume_role {
    role_arn     = "arn:aws:iam::ACCOUNT:role/terraform-deployment"
    external_id  = "terraform-deployment-key"
    session_name = "terraform-session"
  }
}
```

---

### 🛡️ Security Scanning

#### **tfsec - Security Scanner**

```bash
# Install
brew install tfsec

# Or
curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash

# Scan current directory
tfsec .

# Output:
# Result #1 HIGH S3 Bucket does not have encryption enabled
#   /main.tf:10-15
# 
# 10 resource "aws_s3_bucket" "data" {
# 11   bucket = "my-data-bucket"
# 12 }
#
# Fix: Add encryption configuration
```

**Fix security issues:**

```hcl
# Before (insecure)
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

# After (secure)
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "data" {
  bucket = aws_s3_bucket.data.id
  
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

#### **Checkov - Policy Scanner**

```bash
# Install
pip install checkov

# Scan
checkov -d .

# Output:
# Check: CKV_AWS_18: "Ensure S3 bucket has access logging enabled"
# FAILED for resource: aws_s3_bucket.data
# Fix: Enable logging
```

**Integration in CI/CD:**

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on: [pull_request]

jobs:
  tfsec:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          soft_fail: false
  
  checkov:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: .
          soft_fail: false
```

---

### 🔐 Compliance and Auditing

#### **Tagging Strategy**

```hcl
# Required tags for compliance
locals {
  required_tags = {
    Project     = var.project_name
    Environment = var.environment
    Owner       = var.owner_email
    CostCenter  = var.cost_center
    Compliance  = var.compliance_level  # "pci", "hipaa", "sox"
    ManagedBy   = "Terraform"
    CreatedDate = timestamp()
  }
}

# Apply to all resources via provider
provider "aws" {
  region = var.region
  
  default_tags {
    tags = local.required_tags
  }
}

# Enforce tagging with precondition
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  
  tags = merge(
    local.required_tags,
    {
      Name = "web-server"
    }
  )
  
  lifecycle {
    precondition {
      condition     = length(keys(merge(local.required_tags, self.tags))) >= 7
      error_message = "All required tags must be present."
    }
  }
}
```

#### **Audit Logging**

```hcl
# Enable CloudTrail for all API calls
resource "aws_cloudtrail" "main" {
  name                          = "terraform-audit-trail"
  s3_bucket_name                = aws_s3_bucket.cloudtrail.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
  
  event_selector {
    read_write_type           = "All"
    include_management_events = true
    
    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::my-terraform-state/*"]
    }
  }
}

# VPC Flow Logs
resource "aws_flow_log" "main" {
  vpc_id          = aws_vpc.main.id
  traffic_type    = "ALL"
  iam_role_arn    = aws_iam_role.flow_log.arn
  log_destination = aws_cloudwatch_log_group.flow_log.arn
}

# S3 access logging
resource "aws_s3_bucket_logging" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  target_bucket = aws_s3_bucket.logs.id
  target_prefix = "terraform-state-access/"
}
```

---

### ✅ Day 20 Checklist

- [x] State encryption and access control
- [x] Secrets management (Secrets Manager, SSM)
- [x] Sensitive variables and outputs
- [x] Least privilege IAM policies
- [x] Security scanning (tfsec, Checkov)
- [x] Compliance tagging
- [x] Audit logging

**Next:** Testing strategies for Terraform!

---

## Day 21: Testing Strategies

### 🎯 Learning Objectives
- Test Terraform configurations
- Use terraform validate and fmt
- Implement automated testing
- Use Terratest for integration tests
- Set up pre-commit hooks

---

### ✅ Built-in Validation

#### **terraform validate**

```bash
# Validate syntax and configuration
terraform validate

# Output on success:
# Success! The configuration is valid.

# Output on error:
# Error: Invalid reference
#   on main.tf line 15:
#   Resource 'aws_subnet.public' not found.
```

#### **terraform fmt**

```bash
# Format code (dry run)
terraform fmt -check -diff

# Format code (apply changes)
terraform fmt -recursive

# Returns:
# main.tf
# modules/vpc/main.tf
# modules/compute/main.tf
```

#### **terraform plan**

```bash
# Detailed plan
terraform plan

# Save plan for review
terraform plan -out=tfplan

# Review saved plan
terraform show tfplan

# JSON output for automated testing
terraform plan -out=tfplan
terraform show -json tfplan > plan.json
```

---

### 🧪 Testing Pyramid

```plaintext
        /\
       /  \
      / E2E\         End-to-End Tests (Terratest)
     /______\
    /        \
   / Integr. \       Integration Tests (Kitchen-Terraform)
  /___________\
 /             \
/   Unit Tests  \    Unit Tests (validate, fmt, tflint)
/_________________\
```

---

### 🔍 Static Analysis

#### **TFLint - Linter**

```bash
# Install
brew install tflint

# Or
curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash

# Initialize plugins
tflint --init

# Run linter
tflint

# Output:
# 3 issue(s) found:
# 
# Warning: terraform_unused_declarations (main.tf:10)
# variable "unused_var" is declared but not used
# 
# Error: aws_instance_invalid_type (main.tf:25)
# "t2.mega" is an invalid instance type
```

**Configuration:**

```hcl
# .tflint.hcl

plugin "aws" {
  enabled = true
  version = "0.27.0"
  source  = "github.com/terraform-linters/tflint-ruleset-aws"
}

rule "terraform_naming_convention" {
  enabled = true
  
  format = "snake_case"
}

rule "terraform_unused_declarations" {
  enabled = true
}

rule "terraform_deprecated_interpolation" {
  enabled = true
}

rule "terraform_module_pinned_source" {
  enabled = true
  style   = "semver"
}
```

---

### 🧪 Terratest - Go-Based Testing

**Install:**

```bash
go mod init github.com/mycompany/terraform-tests
go get github.com/gruntwork-io/terratest/modules/terraform
```

**Test Structure:**

```
tests/
├── go.mod
├── go.sum
└── terraform_basic_test.go
```

**Example Test:**

```go
// File: tests/terraform_basic_test.go

package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestTerraformBasicExample(t *testing.T) {
    t.Parallel()
    
    // Terraform options
    terraformOptions := &terraform.Options{
        // Path to Terraform code
        TerraformDir: "../examples/basic",
        
        // Variables to pass
        Vars: map[string]interface{}{
            "instance_type": "t2.micro",
            "region":        "us-east-1",
        },
        
        // Disable colors in output
        NoColor: true,
    }
    
    // Clean up resources
    defer terraform.Destroy(t, terraformOptions)
    
    // Run terraform init and apply
    terraform.InitAndApply(t, terraformOptions)
    
    // Get outputs
    instanceId := terraform.Output(t, terraformOptions, "instance_id")
    publicIp := terraform.Output(t, terraformOptions, "public_ip")
    
    // Assertions
    assert.NotEmpty(t, instanceId)
    assert.NotEmpty(t, publicIp)
    assert.Regexp(t, "^i-[a-f0-9]+$", instanceId)
}
```

**Advanced Test:**

```go
// File: tests/terraform_vpc_test.go

package test

import (
    "fmt"
    "testing"
    "github.com/gruntwork-io/terratest/modules/aws"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestTerraformVPCExample(t *testing.T) {
    t.Parallel()
    
    expectedRegion := "us-east-1"
    expectedVpcCidr := "10.0.0.0/16"
    
    terraformOptions := &terraform.Options{
        TerraformDir: "../modules/vpc",
        
        Vars: map[string]interface{}{
            "project_name":       "test",
            "environment":        "test",
            "vpc_cidr":           expectedVpcCidr,
            "availability_zones": []string{"us-east-1a", "us-east-1b"},
            "public_subnet_cidrs": []string{
                "10.0.1.0/24",
                "10.0.2.0/24",
            },
            "private_subnet_cidrs": []string{
                "10.0.11.0/24",
                "10.0.12.0/24",
            },
        },
    }
    
    defer terraform.Destroy(t, terraformOptions)
    
    terraform.InitAndApply(t, terraformOptions)
    
    // Get outputs
    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    publicSubnetIds := terraform.OutputList(t, terraformOptions, "public_subnet_ids")
    privateSubnetIds := terraform.OutputList(t, terraformOptions, "private_subnet_ids")
    
    // Validate VPC exists
    vpc := aws.GetVpcById(t, vpcId, expectedRegion)
    assert.Equal(t, expectedVpcCidr, *vpc.CidrBlock)
    assert.True(t, *vpc.EnableDnsHostnames)
    
    // Validate subnets
    assert.Equal(t, 2, len(publicSubnetIds))
    assert.Equal(t, 2, len(privateSubnetIds))
    
    // Validate subnet CIDR blocks
    for i, subnetId := range publicSubnetIds {
        subnet := aws.GetSubnetById(t, subnetId, expectedRegion)
        expectedCidr := fmt.Sprintf("10.0.%d.0/24", i+1)
        assert.Equal(t, expectedCidr, *subnet.CidrBlock)
    }
    
    // Validate NAT gateways exist
    natGateways := aws.GetNatGatewaysInVpc(t, vpcId, expectedRegion)
    assert.Equal(t, 2, len(natGateways))
}
```

**Run tests:**

```bash
# Run all tests
cd tests
go test -v -timeout 30m

# Run specific test
go test -v -run TestTerraformVPCExample -timeout 30m

# Run tests in parallel
go test -v -parallel 10 -timeout 30m
```

---

### 🔧 Pre-Commit Hooks

**Install pre-commit:**

```bash
# macOS
brew install pre-commit

# Linux
pip install pre-commit
```

**Configuration:**

```yaml
# File: .pre-commit-config.yaml

repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.83.5
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_docs
        args:
          - --hook-config=--path-to-file=README.md
          - --hook-config=--add-to-existing-file=true
          - --hook-config=--create-file-if-not-exist=true
      - id: terraform_tflint
        args:
          - --args=--config=__GIT_WORKING_DIR__/.tflint.hcl
      - id: terraform_tfsec
        args:
          - --args=--soft-fail

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
```

**Install hooks:**

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

---

### 📊 Test Coverage

**Example test suite:**

```go
// File: tests/terraform_test.go

package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

// Test 1: Basic validation
func TestValidation(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "..",
    }
    
    // Should not error
    terraform.Init(t, terraformOptions)
    terraform.Validate(t, terraformOptions)
}

// Test 2: Plan shows no changes for existing state
func TestIdempotency(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "..",
    }
    
    defer terraform.Destroy(t, terraformOptions)
    
    // First apply
    terraform.InitAndApply(t, terraformOptions)
    
    // Second plan should show no changes
    planExitCode := terraform.PlanExitCode(t, terraformOptions)
    assert.Equal(t, 0, planExitCode)
}

// Test 3: Outputs are correct type
func TestOutputs(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "..",
    }
    
    defer terraform.Destroy(t, terraformOptions)
    
    terraform.InitAndApply(t, terraformOptions)
    
    // String output
    vpcId := terraform.Output(t, terraformOptions, "vpc_id")
    assert.Regexp(t, "^vpc-[a-f0-9]+$", vpcId)
    
    // List output
    subnetIds := terraform.OutputList(t, terraformOptions, "subnet_ids")
    assert.Greater(t, len(subnetIds), 0)
    
    // Map output
    tags := terraform.OutputMap(t, terraformOptions, "common_tags")
    assert.Contains(t, tags, "Environment")
}

// Test 4: Security group rules are correct
func TestSecurityGroups(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "..",
    }
    
    defer terraform.Destroy(t, terraformOptions)
    
    terraform.InitAndApply(t, terraformOptions)
    
    sgId := terraform.Output(t, terraformOptions, "security_group_id")
    
    // Verify security group rules
    region := terraform.Output(t, terraformOptions, "region")
    sg := aws.GetSecurityGroupById(t, sgId, region)
    
    assert.Equal(t, 2, len(sg.IpPermissions))  // 2 ingress rules
    assert.Equal(t, 1, len(sg.IpPermissionsEgress))  // 1 egress rule
}
```

---

### 🎯 Complete Testing Workflow

```bash
#!/bin/bash
# File: scripts/test.sh

set -e

echo "===== Running Terraform Tests ====="

# 1. Format check
echo "1. Checking format..."
terraform fmt -check -recursive -diff

# 2. Validation
echo "2. Validating configuration..."
terraform validate

# 3. Linting
echo "3. Running TFLint..."
tflint --init
tflint --recursive

# 4. Security scanning
echo "4. Running tfsec..."
tfsec .

echo "5. Running Checkov..."
checkov -d .

# 6. Run Terratest (if Go is installed)
if command -v go &> /dev/null; then
    echo "6. Running Terratest..."
    cd tests
    go test -v -timeout 30m
    cd ..
fi

echo "===== All Tests Passed! ====="
```

---

### ✅ Day 21 Checklist

- [x] terraform validate and fmt
- [x] terraform plan testing
- [x] TFLint for static analysis
- [x] Terratest for integration tests
- [x] Pre-commit hooks
- [x] Test coverage strategies
- [x] Complete testing workflow

**Next:** CI/CD integration!

---

## Day 22: CI/CD Integration

### 🎯 Learning Objectives
- Set up Terraform CI/CD pipelines
- Use GitHub Actions
- Use GitLab CI
- Use Jenkins
- Implement approval workflows
- Handle secrets in CI/CD

---

### 🔄 CI/CD Workflow

```plaintext
Developer Workflow:
1. Developer creates branch
2. Makes Terraform changes
3. Pushes to Git
4. CI runs automatically:
   - terraform fmt -check
   - terraform validate
   - tflint
   - tfsec/checkov
   - terraform plan
5. Plan posted as PR comment
6. Team reviews plan
7. PR merged to main
8. CD runs automatically:
   - terraform plan
   - Wait for approval
   - terraform apply
```

---

### 🐙 GitHub Actions

#### **Complete Workflow**

```yaml
# File: .github/workflows/terraform.yml

name: Terraform CI/CD

on:
  pull_request:
    branches: [main]
    paths:
      - 'terraform/**'
      - '.github/workflows/terraform.yml'
  push:
    branches: [main]
    paths:
      - 'terraform/**'

env:
  TF_VERSION: '1.7.0'
  AWS_REGION: 'us-east-1'

jobs:
  terraform-check:
    name: Terraform Check
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: terraform
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      
      - name: Terraform Format
        id: fmt
        run: terraform fmt -check -recursive -diff
        continue-on-error: true
      
      - name: Terraform Init
        id: init
        run: terraform init -backend=false
      
      - name: Terraform Validate
        id: validate
        run: terraform validate -no-color
      
      - name: TFLint
        uses: terraform-linters/setup-tflint@v4
        with:
          tflint_version: latest
      
      - name: Run TFLint
        run: |
          tflint --init
          tflint --format compact
      
      - name: tfsec
        uses: aquasecurity/tfsec-action@v1.0.3
        with:
          working_directory: terraform
          soft_fail: false
      
      - name: Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform
          soft_fail: false
          framework: terraform
  
  terraform-plan:
    name: Terraform Plan
    runs-on: ubuntu-latest
    needs: terraform-check
    if: github.event_name == 'pull_request'
    defaults:
      run:
        working-directory: terraform
    
    permissions:
      contents: read
      pull-requests: write
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Terraform Init
        run: terraform init
      
      - name: Terraform Plan
        id: plan
        run: |
          terraform plan -no-color -out=tfplan
          terraform show -no-color tfplan > plan_output.txt
        continue-on-error: true
      
      - name: Comment Plan on PR
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            const plan = fs.readFileSync('terraform/plan_output.txt', 'utf8');
            const output = `#### Terraform Plan 📖
            <details><summary>Show Plan</summary>
            
            \`\`\`terraform
            ${plan}
            \`\`\`
            
            </details>
            
            *Pushed by: @${{ github.actor }}, Action: \`${{ github.event_name }}\`*`;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: output
            });
      
      - name: Plan Status
        if: steps.plan.outcome == 'failure'
        run: exit 1
  
  terraform-apply:
    name: Terraform Apply
    runs-on: ubuntu-latest
    needs: terraform-check
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    defaults:
      run:
        working-directory: terraform
    
    environment:
      name: production
      url: https://console.aws.amazon.com
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Terraform Init
        run: terraform init
      
      - name: Terraform Plan
        run: terraform plan -out=tfplan
      
      - name: Terraform Apply
        run: terraform apply -auto-approve tfplan
      
      - name: Post-deployment tests
        run: |
          # Run smoke tests
          echo "Running post-deployment tests..."
          # Add your tests here
```

**OIDC Configuration for AWS:**

```hcl
# Configure GitHub OIDC provider in AWS
resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"
  
  client_id_list = ["sts.amazonaws.com"]
  
  thumbprint_list = [
    "6938fd4d98bab03faadb97b34396831e3780aea1"
  ]
}

resource "aws_iam_role" "github_actions" {
  name = "github-actions-terraform"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = aws_iam_openid_connect_provider.github.arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "token.actions.githubusercontent.com:aud" = "sts.amazonaws.com"
          }
          StringLike = {
            "token.actions.githubusercontent.com:sub" = "repo:myorg/myrepo:*"
          }
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "github_actions" {
  role       = aws_iam_role.github_actions.name
  policy_arn = aws_iam_policy.terraform_deployment.arn
}
```

---

### 🦊 GitLab CI

```yaml
# File: .gitlab-ci.yml

image:
  name: hashicorp/terraform:1.7.0
  entrypoint: [""]

variables:
  TF_ROOT: ${CI_PROJECT_DIR}/terraform
  TF_ADDRESS: ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/terraform/state/production

cache:
  paths:
    - ${TF_ROOT}/.terraform

before_script:
  - cd ${TF_ROOT}

stages:
  - validate
  - plan
  - apply

validate:
  stage: validate
  script:
    - terraform fmt -check -recursive
    - terraform init -backend=false
    - terraform validate
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'

security_scan:
  stage: validate
  image: aquasec/tfsec:latest
  script:
    - tfsec ${TF_ROOT}
  allow_failure: true
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'

plan:
  stage: plan
  script:
    - terraform init
    - terraform plan -out=tfplan
    - terraform show -no-color tfplan > plan_output.txt
  artifacts:
    paths:
      - ${TF_ROOT}/tfplan
      - ${TF_ROOT}/plan_output.txt
    expire_in: 1 week
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_COMMIT_BRANCH == "main"'

apply:
  stage: apply
  script:
    - terraform init
    - terraform apply -auto-approve tfplan
  dependencies:
    - plan
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: manual
  only:
    - main
```

---

### 🔨 Jenkins

```groovy
// File: Jenkinsfile

pipeline {
    agent any
    
    parameters {
        choice(
            name: 'ACTION',
            choices: ['plan', 'apply', 'destroy'],
            description: 'Terraform action to perform'
        )
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'prod'],
            description: 'Environment to deploy'
        )
    }
    
    environment {
        AWS_CREDENTIALS = credentials('aws-credentials')
        TF_VERSION = '1.7.0'
        TF_ROOT = 'terraform'
    }
    
    stages {
        stage('Setup') {
            steps {
                script {
                    // Install Terraform
                    sh '''
                        if ! command -v terraform &> /dev/null; then
                            wget https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip
                            unzip terraform_${TF_VERSION}_linux_amd64.zip
                            sudo mv terraform /usr/local/bin/
                        fi
                    '''
                }
            }
        }
        
        stage('Validate') {
            steps {
                dir("${TF_ROOT}") {
                    sh 'terraform fmt -check -recursive'
                    sh 'terraform init -backend=false'
                    sh 'terraform validate'
                }
            }
        }
        
        stage('Security Scan') {
            steps {
                script {
                    // Run tfsec
                    sh 'docker run --rm -v $(pwd):/src aquasec/tfsec /src/${TF_ROOT}'
                }
            }
        }
        
        stage('Plan') {
            steps {
                dir("${TF_ROOT}") {
                    withCredentials([
                        [
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: 'aws-credentials',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                        ]
                    ]) {
                        sh 'terraform init'
                        sh 'terraform plan -out=tfplan'
                        sh 'terraform show -no-color tfplan > plan_output.txt'
                    }
                }
                
                archiveArtifacts artifacts: "${TF_ROOT}/plan_output.txt"
            }
        }
        
        stage('Approval') {
            when {
                expression { params.ACTION == 'apply' }
                expression { params.ENVIRONMENT == 'prod' }
            }
            steps {
                script {
                    def plan = readFile("${TF_ROOT}/plan_output.txt")
                    
                    input(
                        message: "Review the plan and approve to proceed with apply:",
                        parameters: [
                            text(
                                name: 'PLAN',
                                defaultValue: plan,
                                description: 'Terraform Plan Output'
                            )
                        ]
                    )
                }
            }
        }
        
        stage('Apply') {
            when {
                expression { params.ACTION == 'apply' }
            }
            steps {
                dir("${TF_ROOT}") {
                    withCredentials([
                        [
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: 'aws-credentials',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                        ]
                    ]) {
                        sh 'terraform apply -auto-approve tfplan'
                    }
                }
            }
        }
        
        stage('Destroy') {
            when {
                expression { params.ACTION == 'destroy' }
            }
            steps {
                input message: 'Are you sure you want to destroy?', ok: 'Destroy'
                
                dir("${TF_ROOT}") {
                    withCredentials([
                        [
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: 'aws-credentials',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                        ]
                    ]) {
                        sh 'terraform destroy -auto-approve'
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            slackSend(
                color: 'good',
                message: "Terraform ${params.ACTION} succeeded for ${params.ENVIRONMENT}"
            )
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Terraform ${params.ACTION} failed for ${params.ENVIRONMENT}"
            )
        }
    }
}
```

---

### 🔐 Secrets Management in CI/CD

#### **GitHub Actions Secrets**

```yaml
# Use GitHub Secrets
steps:
  - name: Configure AWS
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    run: terraform apply
```

#### **Terraform Cloud Variables**

```hcl
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "production"
    }
  }
}

# Variables set in Terraform Cloud UI as sensitive
# - AWS_ACCESS_KEY_ID (sensitive)
# - AWS_SECRET_ACCESS_KEY (sensitive)
# - database_password (sensitive)
```

#### **AWS Secrets Manager Integration**

```yaml
steps:
  - name: Get secrets from AWS Secrets Manager
    uses: aws-actions/aws-secretsmanager-get-secrets@v1
    with:
      secret-ids: |
        prod/database/password
        prod/api/keys
      parse-json-secrets: true
  
  - name: Use secrets
    run: |
      terraform apply \
        -var="db_password=${{ env.PROD_DATABASE_PASSWORD_PASSWORD }}"
```

---

### ✅ Day 22 Checklist

- [x] CI/CD workflow design
- [x] GitHub Actions integration
- [x] GitLab CI configuration
- [x] Jenkins pipeline
- [x] Approval workflows
- [x] Secrets management in CI/CD
- [x] OIDC authentication

**Next:** Real-World Projects!

---

# 🚀 PART 6: REAL-WORLD PROJECTS

## Project 1: Simple Web Server

### 📋 Project Overview

Deploy a simple web server on AWS with:
- EC2 instance running Apache
- Security group allowing HTTP/HTTPS
- Elastic IP for static IP
- User data for automatic configuration

**Architecture:**

```plaintext
┌─────────────────────────────┐
│         Internet            │
└────────────┬────────────────┘
             │
      ┌──────▼───────┐
      │ Elastic IP   │
      └──────┬───────┘
             │
      ┌──────▼────────┐
      │ Security Group│
      │  Port 80, 443 │
      └──────┬────────┘
             │
      ┌──────▼────────┐
      │  EC2 Instance │
      │    Apache     │
      └───────────────┘
```

---

### 📁 Project Structure

```
project-1-simple-web-server/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── user_data.sh
└── README.md
```

---

### 💻 Complete Code

```hcl
# ==================================================
# File: variables.tf
# ==================================================

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name for tagging"
  type        = string
  default     = "simple-web"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "allowed_ips" {
  description = "IP addresses allowed to access the server"
  type        = list(string)
  default     = ["0.0.0.0/0"]  # Change to your IP for security
}

# ==================================================
# File: main.tf
# ==================================================

terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
  
  default_tags {
    tags = {
      Project   = var.project_name
      ManagedBy = "Terraform"
    }
  }
}

# Data sources
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

data "aws_availability_zones" "available" {
  state = "available"
}

# Security Group
resource "aws_security_group" "web" {
  name        = "${var.project_name}-sg"
  description = "Security group for web server"
  
  # HTTP
  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.allowed_ips
  }
  
  # HTTPS
  ingress {
    description = "HTTPS from anywhere"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.allowed_ips
  }
  
  # SSH (optional - for management)
  ingress {
    description = "SSH from allowed IPs"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_ips
  }
  
  # Allow all outbound
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = file("${path.module}/user_data.sh")
  
  root_block_device {
    volume_size = 8
    volume_type = "gp3"
    encrypted   = true
  }
  
  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required"
    http_put_response_hop_limit = 1
  }
  
  tags = {
    Name = "${var.project_name}-server"
  }
}

# Elastic IP
resource "aws_eip" "web" {
  instance = aws_instance.web.id
  domain   = "vpc"
  
  tags = {
    Name = "${var.project_name}-eip"
  }
}

# ==================================================
# File: outputs.tf
# ==================================================

output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP address (Elastic IP)"
  value       = aws_eip.web.public_ip
}

output "web_url" {
  description = "URL to access the web server"
  value       = "http://${aws_eip.web.public_ip}"
}

output "ssh_command" {
  description = "SSH command to connect"
  value       = "ssh -i your-key.pem ec2-user@${aws_eip.web.public_ip}"
}

# ==================================================
# File: user_data.sh
# ==================================================

#!/bin/bash
set -e

# Update system
yum update -y

# Install Apache
yum install -y httpd

# Create simple webpage
cat > /var/www/html/index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { color: #333; }
        .info { background: #e8f4f8; padding: 15px; border-radius: 5px; }
        .success { color: #28a745; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Simple Web Server</h1>
        <p class="success">✓ Apache is running successfully!</p>
        <div class="info">
            <h3>Server Information</h3>
            <p><strong>Hostname:</strong> $(hostname)</p>
            <p><strong>IP Address:</strong> $(hostname -I)</p>
            <p><strong>Date:</strong> $(date)</p>
        </div>
        <p>This server was deployed using Terraform! 🎉</p>
    </div>
</body>
</html>
EOF

# Start and enable Apache
systemctl start httpd
systemctl enable httpd

# Configure firewall (if firewalld is running)
if systemctl is-active --quiet firewalld; then
    firewall-cmd --permanent --add-service=http
    firewall-cmd --permanent --add-service=https
    firewall-cmd --reload
fi

echo "Web server setup complete!"

# ==================================================
# File: terraform.tfvars
# ==================================================

region        = "us-east-1"
project_name  = "simple-web"
instance_type = "t2.micro"

# IMPORTANT: Change this to your IP for security
# Get your IP: curl ifconfig.me
allowed_ips = ["0.0.0.0/0"]  # Allow from anywhere (not recommended for prod)
# allowed_ips = ["YOUR.IP.ADDRESS.HERE/32"]  # Restrict to your IP

# ==================================================
# File: README.md
# ==================================================
```

```markdown
# Project 1: Simple Web Server

## Description
Deploy a simple web server on AWS using Terraform.

## Architecture
- EC2 instance running Amazon Linux 2
- Apache web server
- Elastic IP for static IP address
- Security group with HTTP/HTTPS access

## Prerequisites
- AWS account
- AWS CLI configured
- Terraform >= 1.5.0

## Deployment

1. **Initialize Terraform:**
   ```bash
   terraform init
   ```

2. **Review the plan:**
   ```bash
   terraform plan
   ```

3. **Deploy:**
   ```bash
   terraform apply
   ```

4. **Access the web server:**
   ```bash
   # Get the URL from output
   terraform output web_url
   
   # Open in browser
   open $(terraform output -raw web_url)
   ```

## Outputs
- `instance_id` - EC2 instance ID
- `public_ip` - Elastic IP address
- `web_url` - URL to access the server
- `ssh_command` - SSH command to connect

## Cost Estimate
- EC2 t2.micro: ~$8.50/month
- Elastic IP: Free (when attached)
- **Total: ~$8.50/month**

## Cleanup
```bash
terraform destroy
```

## Security Notes
- Change `allowed_ips` in `terraform.tfvars` to your IP
- Add SSH key for EC2 access
- Enable HTTPS with SSL certificate for production
```

---

### 🧪 Testing

```bash
# Deploy
terraform apply -auto-approve

# Get URL
URL=$(terraform output -raw web_url)

# Test HTTP access
curl -I $URL

# Expected output:
# HTTP/1.1 200 OK
# Server: Apache/2.4.x

# Verify content
curl $URL | grep "Apache is running"

# Cleanup
terraform destroy -auto-approve
```

---

## Project 2: Complete VPC & Networking

### 📋 Project Overview

Create a production-ready VPC with:
- Public and private subnets across 3 AZs
- Internet Gateway
- NAT Gateways (one per AZ)
- Route tables
- Bastion host for secure access
- Network ACLs

**Architecture:**

```plaintext
┌──────────────────────────────────────────────────┐
│                  AWS Cloud                        │
│  ┌────────────────────────────────────────────┐  │
│  │  VPC (10.0.0.0/16)                         │  │
│  │                                             │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────┐│  │
│  │  │   AZ-1a     │  │   AZ-1b     │  │AZ-1c││  │
│  │  │             │  │             │  │     ││  │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │┌───┐││  │
│  │  │ │ Public  │ │  │ │ Public  │ │  ││Pub││  │
│  │  │ │10.0.1.0 │ │  │ │10.0.2.0 │ │  ││lic││  │
│  │  │ └────┬────┘ │  │ └────┬────┘ │  │└─┬─┘││  │
│  │  │      │NAT   │  │      │NAT   │  │  │  ││  │
│  │  │ ┌────▼────┐ │  │ ┌────▼────┐ │  │┌─▼─┐││  │
│  │  │ │ Private │ │  │ │ Private │ │  ││Pri││  │
│  │  │ │10.0.11.0│ │  │ │10.0.12.0│ │  ││vat││  │
│  │  │ └─────────┘ │  │ └─────────┘ │  │└───┘││  │
│  │  └─────────────┘  └─────────────┘  └─────┘│  │
│  │         │                  │               │  │
│  │         └──────────┬───────┘               │  │
│  │                    │                       │  │
│  │              ┌─────▼──────┐                │  │
│  │              │    IGW     │                │  │
│  │              └────────────┘                │  │
│  └─────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

---

### 📁 Project Structure

```
project-2-vpc-networking/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── vpc.tf
├── subnets.tf
├── routing.tf
├── nat.tf
├── bastion.tf
└── README.md
```

---

### 💻 Complete Code

```hcl
# ==================================================
# File: variables.tf
# ==================================================

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "vpc-project"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "prod"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "public_subnet_cidrs" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "private_subnet_cidrs" {
  description = "Private subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
}

variable "enable_nat_gateway" {
  description = "Enable NAT Gateway"
  type        = bool
  default     = true
}

variable "single_nat_gateway" {
  description = "Use single NAT Gateway for all AZs"
  type        = bool
  default     = false
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames"
  type        = bool
  default     = true
}

variable "enable_dns_support" {
  description = "Enable DNS support"
  type        = bool
  default     = true
}

variable "enable_flow_logs" {
  description = "Enable VPC Flow Logs"
  type        = bool
  default     = true
}

variable "bastion_instance_type" {
  description = "Bastion host instance type"
  type        = string
  default     = "t3.micro"
}

variable "bastion_key_name" {
  description = "SSH key name for bastion host"
  type        = string
  default     = ""
}

# ==================================================
# File: main.tf
# ==================================================

terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
  
  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

locals {
  name_prefix = "${var.project_name}-${var.environment}"
}

# ==================================================
# File: vpc.tf
# ==================================================

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support
  
  tags = {
    Name = "${local.name_prefix}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${local.name_prefix}-igw"
  }
}

# VPC Flow Logs
resource "aws_cloudwatch_log_group" "flow_logs" {
  count = var.enable_flow_logs ? 1 : 0
  
  name              = "/aws/vpc/${local.name_prefix}"
  retention_in_days = 7
  
  tags = {
    Name = "${local.name_prefix}-flow-logs"
  }
}

resource "aws_iam_role" "flow_logs" {
  count = var.enable_flow_logs ? 1 : 0
  
  name = "${local.name_prefix}-flow-logs-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "vpc-flow-logs.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "flow_logs" {
  count = var.enable_flow_logs ? 1 : 0
  
  name = "${local.name_prefix}-flow-logs-policy"
  role = aws_iam_role.flow_logs[0].id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_flow_log" "main" {
  count = var.enable_flow_logs ? 1 : 0
  
  vpc_id          = aws_vpc.main.id
  traffic_type    = "ALL"
  iam_role_arn    = aws_iam_role.flow_logs[0].arn
  log_destination = aws_cloudwatch_log_group.flow_logs[0].arn
  
  tags = {
    Name = "${local.name_prefix}-flow-log"
  }
}

# ==================================================
# File: subnets.tf
# ==================================================

# Public Subnets
resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidrs)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${local.name_prefix}-public-${var.availability_zones[count.index]}"
    Type = "public"
  }
}

# Private Subnets
resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "${local.name_prefix}-private-${var.availability_zones[count.index]}"
    Type = "private"
  }
}

# ==================================================
# File: nat.tf
# ==================================================

# Elastic IPs for NAT Gateways
resource "aws_eip" "nat" {
  count = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.availability_zones)) : 0
  
  domain = "vpc"
  
  tags = {
    Name = "${local.name_prefix}-nat-eip-${count.index + 1}"
  }
  
  depends_on = [aws_internet_gateway.main]
}

# NAT Gateways
resource "aws_nat_gateway" "main" {
  count = var.enable_nat_gateway ? (var.single_nat_gateway ? 1 : length(var.availability_zones)) : 0
  
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id
  
  tags = {
    Name = "${local.name_prefix}-nat-${count.index + 1}"
  }
  
  depends_on = [aws_internet_gateway.main]
}

# ==================================================
# File: routing.tf
# ==================================================

# Public Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${local.name_prefix}-public-rt"
  }
}

# Public Route Table Associations
resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public)
  
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# Private Route Tables
resource "aws_route_table" "private" {
  count = var.enable_nat_gateway ? length(var.availability_zones) : 1
  
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${local.name_prefix}-private-rt-${count.index + 1}"
  }
}

# Private Routes (to NAT Gateway)
resource "aws_route" "private_nat" {
  count = var.enable_nat_gateway ? length(var.availability_zones) : 0
  
  route_table_id         = aws_route_table.private[count.index].id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = var.single_nat_gateway ? aws_nat_gateway.main[0].id : aws_nat_gateway.main[count.index].id
}

# Private Route Table Associations
resource "aws_route_table_association" "private" {
  count = length(aws_subnet.private)
  
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = var.enable_nat_gateway ? aws_route_table.private[var.single_nat_gateway ? 0 : count.index].id : aws_route_table.private[0].id
}

# ==================================================
# File: bastion.tf
# ==================================================

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Bastion Security Group
resource "aws_security_group" "bastion" {
  name        = "${local.name_prefix}-bastion-sg"
  description = "Security group for bastion host"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Restrict this in production!
  }
  
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${local.name_prefix}-bastion-sg"
  }
}

# Bastion Host
resource "aws_instance" "bastion" {
  count = var.bastion_key_name != "" ? 1 : 0
  
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = var.bastion_instance_type
  key_name               = var.bastion_key_name
  subnet_id              = aws_subnet.public[0].id
  vpc_security_group_ids = [aws_security_group.bastion.id]
  
  root_block_device {
    volume_size = 8
    volume_type = "gp3"
    encrypted   = true
  }
  
  tags = {
    Name = "${local.name_prefix}-bastion"
  }
}

# Elastic IP for Bastion
resource "aws_eip" "bastion" {
  count = var.bastion_key_name != "" ? 1 : 0
  
  instance = aws_instance.bastion[0].id
  domain   = "vpc"
  
  tags = {
    Name = "${local.name_prefix}-bastion-eip"
  }
}

# ==================================================
# File: outputs.tf
# ==================================================

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "VPC CIDR block"
  value       = aws_vpc.main.cidr_block
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "public_subnet_cidrs" {
  description = "Public subnet CIDR blocks"
  value       = aws_subnet.public[*].cidr_block
}

output "private_subnet_cidrs" {
  description = "Private subnet CIDR blocks"
  value       = aws_subnet.private[*].cidr_block
}

output "internet_gateway_id" {
  description = "Internet Gateway ID"
  value       = aws_internet_gateway.main.id
}

output "nat_gateway_ids" {
  description = "NAT Gateway IDs"
  value       = aws_nat_gateway.main[*].id
}

output "nat_gateway_ips" {
  description = "NAT Gateway public IPs"
  value       = aws_eip.nat[*].public_ip
}

output "bastion_public_ip" {
  description = "Bastion host public IP"
  value       = length(aws_eip.bastion) > 0 ? aws_eip.bastion[0].public_ip : null
}

output "bastion_ssh_command" {
  description = "SSH command for bastion"
  value       = length(aws_instance.bastion) > 0 ? "ssh -i ${var.bastion_key_name}.pem ec2-user@${aws_eip.bastion[0].public_ip}" : "No bastion host deployed"
}

# ==================================================
# File: terraform.tfvars
# ==================================================

region             = "us-east-1"
project_name       = "vpc-project"
environment        = "prod"
vpc_cidr           = "10.0.0.0/16"
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]

enable_nat_gateway   = true
single_nat_gateway   = false  # Use one NAT per AZ for HA
enable_dns_hostnames = true
enable_dns_support   = true
enable_flow_logs     = true

bastion_instance_type = "t3.micro"
bastion_key_name      = ""  # Set your SSH key name
```

---

### 🧪 Testing

```bash
# Deploy
terraform apply -auto-approve

# Verify VPC
aws ec2 describe-vpcs --vpc-ids $(terraform output -raw vpc_id)

# Verify subnets
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$(terraform output -raw vpc_id)"

# Test connectivity from bastion (if deployed)
BASTION_IP=$(terraform output -raw bastion_public_ip)
ssh -i your-key.pem ec2-user@$BASTION_IP

# Cleanup
terraform destroy -auto-approve
```

---

### 💰 Cost Estimate

**Monthly costs:**
- VPC: Free
- Internet Gateway: Free
- NAT Gateways (3): ~$96/month ($32 each)
- Elastic IPs (NAT): Free (attached)
- Bastion (t3.micro): ~$7.50/month
- VPC Flow Logs: ~$10/month

**Total: ~$113.50/month**

---

## Project 3: Multi-Tier Application

Complete 3-tier architecture with Application Load Balancer, Auto Scaling, and RDS.

*Due to length, I'll provide the key structure:*

```plaintext
Architecture:
┌────────────────────────────────────┐
│     Application Load Balancer      │
│         (Public Subnets)           │
└─────────────┬──────────────────────┘
              │
┌─────────────▼──────────────────────┐
│    Auto Scaling Group (Web Tier)   │
│         (Private Subnets)          │
└─────────────┬──────────────────────┘
              │
┌─────────────▼──────────────────────┐
│         RDS MySQL (Multi-AZ)       │
│      (Private DB Subnets)          │
└────────────────────────────────────┘
```

**Key components:**
- VPC with public, private, and database subnets
- Application Load Balancer
- Auto Scaling Group (2-10 instances)
- Launch Template with user data
- RDS MySQL Multi-AZ
- ElastiCache Redis cluster
- CloudWatch alarms
- SNS notifications

---

## Project 3: Multi-Tier Application

### 📋 Project Overview

Deploy a complete 3-tier application with:
- Application Load Balancer (public)
- Auto Scaling Group with Launch Template
- RDS MySQL (Multi-AZ)
- ElastiCache Redis
- CloudWatch monitoring
- SNS notifications

**Architecture:**

```plaintext
Internet
   │
   ▼
┌──────────────────┐
│  Route 53 DNS    │
└────────┬─────────┘
         │
   ▼
┌──────────────────┐
│  CloudFront CDN  │ (Optional)
└────────┬─────────┘
         │
   ▼
┌──────────────────────────────────┐
│  Application Load Balancer       │
│  (Public Subnets across 3 AZs)   │
└────────┬─────────────────────────┘
         │
   ▼
┌──────────────────────────────────┐
│   Auto Scaling Group             │
│   EC2 Instances (Web/App Tier)   │
│   (Private Subnets across 3 AZs) │
└────┬────────────────────┬────────┘
     │                    │
     ▼                    ▼
┌─────────────┐    ┌──────────────┐
│ RDS MySQL   │    │ ElastiCache  │
│ Multi-AZ    │    │ Redis        │
│ (DB Subnet) │    │ (Cache Layer)│
└─────────────┘    └──────────────┘
```

---

### 📁 Project Structure

```
project-3-multi-tier-app/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── vpc.tf
├── security-groups.tf
├── alb.tf
├── asg.tf
├── rds.tf
├── elasticache.tf
├── cloudwatch.tf
├── sns.tf
├── user_data.sh
└── README.md
```

---

### 💻 Complete Code

```hcl
# ==================================================
# File: variables.tf
# ==================================================

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "multi-tier-app"
}

variable "environment" {
  description = "Environment"
  type        = string
  default     = "prod"
}

variable "vpc_cidr" {
  description = "VPC CIDR"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

# ASG Configuration
variable "min_size" {
  description = "Minimum instances"
  type        = number
  default     = 2
}

variable "max_size" {
  description = "Maximum instances"
  type        = number
  default     = 10
}

variable "desired_capacity" {
  description = "Desired instances"
  type        = number
  default     = 3
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

# Database Configuration
variable "db_instance_class" {
  description = "RDS instance class"
  type        = string
  default     = "db.t3.medium"
}

variable "db_name" {
  description = "Database name"
  type        = string
  default     = "appdb"
}

variable "db_username" {
  description = "Database username"
  type        = string
  default     = "admin"
}

variable "db_multi_az" {
  description = "Enable Multi-AZ"
  type        = bool
  default     = true
}

# ElastiCache Configuration
variable "redis_node_type" {
  description = "Redis node type"
  type        = string
  default     = "cache.t3.micro"
}

variable "redis_num_cache_nodes" {
  description = "Number of cache nodes"
  type        = number
  default     = 2
}

variable "alert_email" {
  description = "Email for alerts"
  type        = string
}

# ==================================================
# File: main.tf
# ==================================================

terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "aws" {
  region = var.region
  
  default_tags {
    tags = {
      Project     = var.project_name
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

locals {
  name_prefix = "${var.project_name}-${var.environment}"
  
  public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24", "10.0.13.0/24"]
  database_subnet_cidrs = ["10.0.21.0/24", "10.0.22.0/24", "10.0.23.0/24"]
}

data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# ==================================================
# File: vpc.tf
# ==================================================

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${local.name_prefix}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${local.name_prefix}-igw"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count = length(local.public_subnet_cidrs)
  
  vpc_id                  = aws_vpc.main.id
  cidr_block              = local.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${local.name_prefix}-public-${count.index + 1}"
    Type = "public"
  }
}

# Private Subnets (for application)
resource "aws_subnet" "private" {
  count = length(local.private_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = local.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "${local.name_prefix}-private-${count.index + 1}"
    Type = "private"
  }
}

# Database Subnets
resource "aws_subnet" "database" {
  count = length(local.database_subnet_cidrs)
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = local.database_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  
  tags = {
    Name = "${local.name_prefix}-database-${count.index + 1}"
    Type = "database"
  }
}

# NAT Gateways
resource "aws_eip" "nat" {
  count = length(var.availability_zones)
  domain = "vpc"
  
  tags = {
    Name = "${local.name_prefix}-nat-eip-${count.index + 1}"
  }
}

resource "aws_nat_gateway" "main" {
  count = length(var.availability_zones)
  
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id
  
  tags = {
    Name = "${local.name_prefix}-nat-${count.index + 1}"
  }
  
  depends_on = [aws_internet_gateway.main]
}

# Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${local.name_prefix}-public-rt"
  }
}

resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public)
  
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  count = length(var.availability_zones)
  
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }
  
  tags = {
    Name = "${local.name_prefix}-private-rt-${count.index + 1}"
  }
}

resource "aws_route_table_association" "private" {
  count = length(aws_subnet.private)
  
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# ==================================================
# File: security-groups.tf
# ==================================================

# ALB Security Group
resource "aws_security_group" "alb" {
  name        = "${local.name_prefix}-alb-sg"
  description = "Security group for ALB"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description = "HTTP from internet"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    description = "HTTPS from internet"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${local.name_prefix}-alb-sg"
  }
}

# Application Security Group
resource "aws_security_group" "app" {
  name        = "${local.name_prefix}-app-sg"
  description = "Security group for application servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description     = "HTTP from ALB"
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
  }
  
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${local.name_prefix}-app-sg"
  }
}

# Database Security Group
resource "aws_security_group" "database" {
  name        = "${local.name_prefix}-database-sg"
  description = "Security group for RDS"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description     = "MySQL from app servers"
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]
  }
  
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${local.name_prefix}-database-sg"
  }
}

# Cache Security Group
resource "aws_security_group" "cache" {
  name        = "${local.name_prefix}-cache-sg"
  description = "Security group for ElastiCache"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    description     = "Redis from app servers"
    from_port       = 6379
    to_port         = 6379
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]
  }
  
  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${local.name_prefix}-cache-sg"
  }
}

# ==================================================
# File: alb.tf
# ==================================================

resource "aws_lb" "main" {
  name               = "${local.name_prefix}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = aws_subnet.public[*].id
  
  enable_deletion_protection = false
  enable_http2              = true
  
  tags = {
    Name = "${local.name_prefix}-alb"
  }
}

resource "aws_lb_target_group" "app" {
  name     = "${local.name_prefix}-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
  
  health_check {
    enabled             = true
    healthy_threshold   = 2
    unhealthy_threshold = 3
    timeout             = 5
    interval            = 30
    path                = "/health"
    matcher             = "200"
  }
  
  deregistration_delay = 30
  
  tags = {
    Name = "${local.name_prefix}-tg"
  }
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.main.arn
  port              = 80
  protocol          = "HTTP"
  
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app.arn
  }
}

# ==================================================
# File: asg.tf
# ==================================================

resource "aws_launch_template" "app" {
  name_prefix   = "${local.name_prefix}-lt-"
  image_id      = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  
  vpc_security_group_ids = [aws_security_group.app.id]
  
  user_data = base64encode(templatefile("${path.module}/user_data.sh", {
    db_endpoint    = aws_db_instance.main.endpoint
    redis_endpoint = aws_elasticache_cluster.main.cache_nodes[0].address
    db_name        = var.db_name
    db_username    = var.db_username
    region         = var.region
  }))
  
  iam_instance_profile {
    name = aws_iam_instance_profile.app.name
  }
  
  monitoring {
    enabled = true
  }
  
  metadata_options {
    http_endpoint               = "enabled"
    http_tokens                 = "required"
    http_put_response_hop_limit = 1
  }
  
  tag_specifications {
    resource_type = "instance"
    
    tags = {
      Name = "${local.name_prefix}-app-instance"
    }
  }
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "app" {
  name                = "${local.name_prefix}-asg"
  vpc_zone_identifier = aws_subnet.private[*].id
  target_group_arns   = [aws_lb_target_group.app.arn]
  
  min_size         = var.min_size
  max_size         = var.max_size
  desired_capacity = var.desired_capacity
  
  health_check_type         = "ELB"
  health_check_grace_period = 300
  
  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }
  
  tag {
    key                 = "Name"
    value               = "${local.name_prefix}-app-instance"
    propagate_at_launch = true
  }
  
  lifecycle {
    create_before_destroy = true
    ignore_changes        = [desired_capacity]
  }
}

# IAM Role for EC2 instances
resource "aws_iam_role" "app" {
  name = "${local.name_prefix}-app-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "app_ssm" {
  role       = aws_iam_role.app.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_role_policy_attachment" "app_cloudwatch" {
  role       = aws_iam_role.app.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"
}

resource "aws_iam_instance_profile" "app" {
  name = "${local.name_prefix}-app-profile"
  role = aws_iam_role.app.name
}

# Auto Scaling Policies
resource "aws_autoscaling_policy" "scale_up" {
  name                   = "${local.name_prefix}-scale-up"
  autoscaling_group_name = aws_autoscaling_group.app.name
  adjustment_type        = "ChangeInCapacity"
  scaling_adjustment     = 2
  cooldown               = 300
}

resource "aws_autoscaling_policy" "scale_down" {
  name                   = "${local.name_prefix}-scale-down"
  autoscaling_group_name = aws_autoscaling_group.app.name
  adjustment_type        = "ChangeInCapacity"
  scaling_adjustment     = -1
  cooldown               = 300
}

# ==================================================
# File: rds.tf
# ==================================================

resource "random_password" "db_password" {
  length  = 32
  special = true
}

resource "aws_secretsmanager_secret" "db_password" {
  name                    = "${local.name_prefix}-db-password"
  recovery_window_in_days = 7
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({
    username = var.db_username
    password = random_password.db_password.result
    engine   = "mysql"
    host     = aws_db_instance.main.endpoint
    port     = 3306
    dbname   = var.db_name
  })
}

resource "aws_db_subnet_group" "main" {
  name       = "${local.name_prefix}-db-subnet-group"
  subnet_ids = aws_subnet.database[*].id
  
  tags = {
    Name = "${local.name_prefix}-db-subnet-group"
  }
}

resource "aws_db_instance" "main" {
  identifier     = "${local.name_prefix}-db"
  engine         = "mysql"
  engine_version = "8.0.35"
  instance_class = var.db_instance_class
  
  allocated_storage     = 100
  max_allocated_storage = 1000
  storage_type          = "gp3"
  storage_encrypted     = true
  
  db_name  = var.db_name
  username = var.db_username
  password = random_password.db_password.result
  
  multi_az               = var.db_multi_az
  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.database.id]
  
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "mon:04:00-mon:05:00"
  
  enabled_cloudwatch_logs_exports = ["error", "general", "slowquery"]
  
  skip_final_snapshot = false
  final_snapshot_identifier = "${local.name_prefix}-db-final-snapshot"
  
  tags = {
    Name = "${local.name_prefix}-db"
  }
}

# ==================================================
# File: elasticache.tf
# ==================================================

resource "aws_elasticache_subnet_group" "main" {
  name       = "${local.name_prefix}-cache-subnet-group"
  subnet_ids = aws_subnet.private[*].id
  
  tags = {
    Name = "${local.name_prefix}-cache-subnet-group"
  }
}

resource "aws_elasticache_cluster" "main" {
  cluster_id           = "${local.name_prefix}-redis"
  engine               = "redis"
  node_type            = var.redis_node_type
  num_cache_nodes      = var.redis_num_cache_nodes
  parameter_group_name = "default.redis7"
  engine_version       = "7.0"
  port                 = 6379
  
  subnet_group_name    = aws_elasticache_subnet_group.main.name
  security_group_ids   = [aws_security_group.cache.id]
  
  snapshot_retention_limit = 5
  snapshot_window          = "03:00-05:00"
  
  tags = {
    Name = "${local.name_prefix}-redis"
  }
}

# ==================================================
# File: cloudwatch.tf
# ==================================================

# High CPU Alarm
resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  alarm_name          = "${local.name_prefix}-high-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300
  statistic           = "Average"
  threshold           = 75
  alarm_description   = "Triggers when CPU exceeds 75%"
  alarm_actions       = [aws_sns_topic.alerts.arn, aws_autoscaling_policy.scale_up.arn]
  
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.app.name
  }
}

# Low CPU Alarm
resource "aws_cloudwatch_metric_alarm" "low_cpu" {
  alarm_name          = "${local.name_prefix}-low-cpu"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = 300
  statistic           = "Average"
  threshold           = 25
  alarm_description   = "Triggers when CPU below 25%"
  alarm_actions       = [aws_autoscaling_policy.scale_down.arn]
  
  dimensions = {
    AutoScalingGroupName = aws_autoscaling_group.app.name
  }
}

# Database CPU Alarm
resource "aws_cloudwatch_metric_alarm" "db_cpu" {
  alarm_name          = "${local.name_prefix}-db-high-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/RDS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Database CPU is high"
  alarm_actions       = [aws_sns_topic.alerts.arn]
  
  dimensions = {
    DBInstanceIdentifier = aws_db_instance.main.id
  }
}

# ==================================================
# File: sns.tf
# ==================================================

resource "aws_sns_topic" "alerts" {
  name = "${local.name_prefix}-alerts"
  
  tags = {
    Name = "${local.name_prefix}-alerts"
  }
}

resource "aws_sns_topic_subscription" "alerts_email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = var.alert_email
}

# ==================================================
# File: outputs.tf
# ==================================================

output "alb_dns_name" {
  description = "ALB DNS name"
  value       = aws_lb.main.dns_name
}

output "alb_url" {
  description = "Application URL"
  value       = "http://${aws_lb.main.dns_name}"
}

output "database_endpoint" {
  description = "RDS endpoint"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}

output "redis_endpoint" {
  description = "Redis endpoint"
  value       = aws_elasticache_cluster.main.cache_nodes[0].address
}

output "asg_name" {
  description = "Auto Scaling Group name"
  value       = aws_autoscaling_group.app.name
}

# ==================================================
# File: user_data.sh
# ==================================================

#!/bin/bash
set -e

# Update system
yum update -y

# Install dependencies
yum install -y httpd php php-mysqlnd php-redis amazon-cloudwatch-agent

# Get DB password from Secrets Manager
DB_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id ${db_name}-db-password \
  --region ${region} \
  --query SecretString \
  --output text | jq -r .password)

# Configure application
cat > /var/www/html/config.php <<EOF
<?php
define('DB_HOST', '${db_endpoint}');
define('DB_USER', '${db_username}');
define('DB_PASS', '$DB_PASSWORD');
define('DB_NAME', '${db_name}');
define('REDIS_HOST', '${redis_endpoint}');
?>
EOF

# Create sample application
cat > /var/www/html/index.php <<'EOF'
<?php
require_once 'config.php';

// Database connection
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
if ($mysqli->connect_error) {
    die("Database connection failed: " . $mysqli->connect_error);
}

// Redis connection
$redis = new Redis();
$redis->connect(REDIS_HOST, 6379);

// Page view counter
$views = $redis->incr('page_views');

?>
<!DOCTYPE html>
<html>
<head>
    <title>Multi-Tier Application</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; }
        .status { color: #28a745; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🚀 Multi-Tier Application</h1>
    <div class="status">✓ Application is running!</div>
    <p><strong>Page Views:</strong> <?php echo $views; ?></p>
    <p><strong>Database:</strong> Connected to MySQL</p>
    <p><strong>Cache:</strong> Connected to Redis</p>
    <p><strong>Server:</strong> <?php echo gethostname(); ?></p>
</body>
</html>
EOF

# Health check endpoint
cat > /var/www/html/health <<'EOF'
OK
EOF

# Start Apache
systemctl start httpd
systemctl enable httpd

# Configure CloudWatch agent
cat > /opt/aws/amazon-cloudwatch-agent/etc/config.json <<'EOF'
{
  "metrics": {
    "namespace": "MultiTierApp",
    "metrics_collected": {
      "mem": {
        "measurement": [{"name": "mem_used_percent"}],
        "metrics_collection_interval": 60
      },
      "disk": {
        "measurement": [{"name": "used_percent"}],
        "metrics_collection_interval": 60,
        "resources": ["*"]
      }
    }
  }
}
EOF

# Start CloudWatch agent
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -s \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json

echo "Application setup complete!"

# ==================================================
# File: terraform.tfvars
# ==================================================

region      = "us-east-1"
project_name = "multi-tier-app"
environment = "prod"

vpc_cidr           = "10.0.0.0/16"
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

# Auto Scaling
min_size         = 2
max_size         = 10
desired_capacity = 3
instance_type    = "t3.medium"

# Database
db_instance_class = "db.t3.medium"
db_name          = "appdb"
db_username      = "admin"
db_multi_az      = true

# Cache
redis_node_type       = "cache.t3.micro"
redis_num_cache_nodes = 2

# Alerts
alert_email = "your-email@example.com"
```

---

### 💰 Cost Estimate

**Monthly costs:**
- ALB: ~$22/month
- EC2 (3x t3.medium): ~$90/month
- RDS Multi-AZ (db.t3.medium): ~$120/month
- ElastiCache (2 nodes): ~$30/month
- NAT Gateways (3): ~$96/month
- Data transfer: ~$50/month

**Total: ~$408/month**

---

## Project 4: EKS Kubernetes Cluster

### 📋 Project Overview

Deploy production-ready EKS cluster with:
- EKS Control Plane
- Managed Node Groups
- VPC with private subnets
- IAM roles and policies
- OIDC provider
- Kubernetes addons (CoreDNS, kube-proxy, VPC-CNI)

**Architecture:**

```plaintext
┌────────────────────────────────────┐
│     EKS Control Plane              │
│     (Managed by AWS)               │
└────────┬───────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Worker Nodes (Managed Node Group) │
│  - Auto Scaling                    │
│  - Private Subnets                 │
│  - Multi-AZ                        │
└────────┬───────────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│  Application Pods                  │
│  - Load Balancer Controller        │
│  - Metrics Server                  │
│  - Cluster Autoscaler              │
└────────────────────────────────────┘
```

---

### 💻 Key Configuration

```hcl
# Simplified EKS setup - Key components

resource "aws_eks_cluster" "main" {
  name     = "${local.name_prefix}-eks"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = "1.28"
  
  vpc_config {
    subnet_ids              = aws_subnet.private[*].id
    endpoint_private_access = true
    endpoint_public_access  = true
    public_access_cidrs     = ["0.0.0.0/0"]
  }
  
  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
}

resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${local.name_prefix}-node-group"
  node_role_arn   = aws_iam_role.eks_node.arn
  subnet_ids      = aws_subnet.private[*].id
  
  scaling_config {
    desired_size = 3
    max_size     = 10
    min_size     = 2
  }
  
  instance_types = ["t3.medium"]
  capacity_type  = "ON_DEMAND"
  
  update_config {
    max_unavailable = 1
  }
}
```

---

## Project 5: Multi-Cloud Deployment

### 📋 Project Overview

Deploy resources across AWS, Azure, and GCP simultaneously:
- AWS: VPC + EC2
- Azure: VNet + VM
- GCP: VPC + Compute Instance
- Unified monitoring and management

**Architecture:**

```plaintext
┌──────────┐   ┌──────────┐   ┌──────────┐
│   AWS    │   │  Azure   │   │   GCP    │
│          │   │          │   │          │
│  VPC     │   │  VNet    │   │  VPC     │
│  EC2     │   │  VM      │   │  CE      │
└────┬─────┘   └────┬─────┘   └────┬─────┘
     │              │              │
     └──────────────┴──────────────┘
              Terraform
```

---

### 💻 Multi-Provider Configuration

```hcl
# Providers for all three clouds

terraform {
  required_version = ">= 1.5.0"
  
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

# AWS Resources
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  
  tags = {
    Name  = "multi-cloud-aws"
    Cloud = "AWS"
  }
}

# Azure Resources
provider "azurerm" {
  features {}
}

resource "azurerm_virtual_machine" "web" {
  name                = "multi-cloud-azure"
  location            = "East US"
  resource_group_name = azurerm_resource_group.main.name
  vm_size             = "Standard_B1s"
  
  tags = {
    Cloud = "Azure"
  }
}

# GCP Resources
provider "google" {
  project = "my-project"
  region  = "us-central1"
}

resource "google_compute_instance" "web" {
  name         = "multi-cloud-gcp"
  machine_type = "e2-micro"
  zone         = "us-central1-a"
  
  labels = {
    cloud = "gcp"
  }
}
```

---

# 📚 BONUS SECTIONS

## Bonus 1: Advanced State Management & Surgery

### 🔧 State File Deep Dive

The Terraform state file (`.tfstate`) is JSON-formatted and contains:

**State File Structure:**

```json
{
  "version": 4,
  "terraform_version": "1.5.0",
  "serial": 15,
  "lineage": "abc123-def456-ghi789",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "id": "i-0123456789abcdef0",
            "ami": "ami-12345678",
            "instance_type": "t2.micro"
          },
          "private": "eyJzY2hlbWF...",
          "dependencies": []
        }
      ]
    }
  ]
}
```

---

### 🚨 State Surgery Techniques

**⚠️ WARNING:** Always backup state before surgery!

```bash
# 1. Backup current state
terraform state pull > terraform.tfstate.backup

# 2. List all resources
terraform state list

# 3. Show specific resource details
terraform state show aws_instance.web

# 4. Remove resource from state (doesn't delete actual resource)
terraform state rm aws_instance.web

# 5. Move resource to different address
terraform state mv aws_instance.web aws_instance.server

# 6. Replace provider in state
terraform state replace-provider hashicorp/aws registry.terraform.io/hashicorp/aws

# 7. Import existing resource
terraform import aws_instance.web i-0123456789abcdef0
```

---

### 🔄 State Recovery Scenarios

**Scenario 1: Corrupted State File**

```bash
# Step 1: Check if backup exists
ls -la terraform.tfstate.backup

# Step 2: Restore from backup
cp terraform.tfstate.backup terraform.tfstate

# Step 3: Verify
terraform plan

# If no backup, restore from remote backend
terraform state pull > terraform.tfstate
```

**Scenario 2: Lost State File**

```bash
# Option 1: Recreate state with imports
# Create empty main.tf with resource definitions
terraform init

# Import each resource
terraform import aws_vpc.main vpc-12345678
terraform import aws_subnet.public[0] subnet-11111111
terraform import aws_subnet.public[1] subnet-22222222

# Option 2: Use terraform refresh (if resources exist)
terraform refresh
```

**Scenario 3: State Drift (Manual Changes)**

```bash
# Detect drift
terraform plan -detailed-exitcode
# Exit code 2 = changes detected

# Option 1: Update state to match reality
terraform refresh

# Option 2: Update infrastructure to match state
terraform apply

# Option 3: Accept drift for specific attribute
resource "aws_instance" "web" {
  # ... 
  
  lifecycle {
    ignore_changes = [ami]  # Ignore AMI changes
  }
}
```

---

### 🛠️ Advanced State Manipulation

**Bulk State Operations:**

```bash
#!/bin/bash
# Script: bulk_state_operations.sh

# Move all resources with prefix
for resource in $(terraform state list | grep "aws_subnet"); do
    new_name=$(echo $resource | sed 's/public/private/g')
    terraform state mv "$resource" "$new_name"
done

# Remove all resources of specific type
terraform state list | grep "aws_route_table_association" | \
    xargs -I {} terraform state rm {}

# Export state to JSON for analysis
terraform state pull | jq . > state_analysis.json

# Count resources by type
terraform state list | cut -d. -f1 | sort | uniq -c
```

---

### 🔐 State Encryption Best Practices

```hcl
# S3 backend with full encryption

terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "arn:aws:kms:us-east-1:123456789012:key/abc-def-ghi"
    dynamodb_table = "terraform-locks"
    
    # Additional security
    acl                  = "private"
    skip_metadata_api_check = true
    skip_credentials_validation = false
  }
}

# Prevent accidental state deletion
resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  rule {
    id     = "keep-versions"
    status = "Enabled"
    
    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}
```

---

### 📊 State Analysis & Monitoring

```bash
# Analyze state file size
terraform state pull | wc -c

# Count total resources
terraform state list | wc -l

# Resources by type
terraform state list | cut -d. -f1 | sort | uniq -c | sort -rn

# Find large resources
terraform state show aws_instance.large_data | wc -c

# Check for sensitive data in state
terraform state pull | grep -i "password\|secret\|key"

# State lineage tracking
terraform state pull | jq -r '.lineage'

# State serial number (version)
terraform state pull | jq -r '.serial'
```

---

## Bonus 2: Comprehensive Troubleshooting Guide

### 🐛 Common Errors & Solutions

#### Error 1: Provider Version Conflicts

**Error Message:**
```
Error: Failed to query available provider packages
Could not retrieve the list of available versions for provider hashicorp/aws
```

**Solution:**
```hcl
# Fix: Lock provider versions

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"  # Lock to major version
    }
  }
}

# Then run:
# terraform init -upgrade
```

---

#### Error 2: State Lock Errors

**Error Message:**
```
Error: Error acquiring the state lock
Lock Info:
  ID:        abc-123-def-456
  Path:      s3-bucket/terraform.tfstate
  Operation: OperationTypeApply
  Who:       user@hostname
  Version:   1.5.0
  Created:   2024-01-15 10:30:00
```

**Solution:**
```bash
# Option 1: Wait for lock to release (if operation is running)
# Wait 5-10 minutes

# Option 2: Force unlock (DANGEROUS - only if operation crashed)
terraform force-unlock abc-123-def-456

# Option 3: Check DynamoDB for stale lock
aws dynamodb get-item \
    --table-name terraform-locks \
    --key '{"LockID": {"S": "my-bucket/terraform.tfstate-md5"}}'

# Option 4: Delete stale lock from DynamoDB
aws dynamodb delete-item \
    --table-name terraform-locks \
    --key '{"LockID": {"S": "my-bucket/terraform.tfstate-md5"}}'
```

---

#### Error 3: Resource Already Exists

**Error Message:**
```
Error: creating EC2 Instance: ResourceAlreadyExists: Instance i-123 already exists
```

**Solution:**
```bash
# Import existing resource
terraform import aws_instance.web i-0123456789abcdef0

# Or remove from state if it shouldn't be managed
terraform state rm aws_instance.web
```

---

#### Error 4: Dependency Cycle

**Error Message:**
```
Error: Cycle: aws_subnet.private, aws_nat_gateway.main, aws_route_table.private
```

**Solution:**
```hcl
# Break cycle with depends_on

resource "aws_subnet" "private" {
  # ... configuration
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route_table" "private" {
  # Don't reference NAT gateway directly
  # Use depends_on instead
  
  depends_on = [aws_nat_gateway.main]
}
```

---

#### Error 5: Authentication Errors

**Error Message:**
```
Error: error configuring Terraform AWS Provider: no valid credential sources
```

**Solution:**
```bash
# Check AWS credentials
aws sts get-caller-identity

# Set credentials
export AWS_ACCESS_KEY_ID="your-key"
export AWS_SECRET_ACCESS_KEY="your-secret"
export AWS_DEFAULT_REGION="us-east-1"

# Or use AWS SSO
aws sso login --profile my-profile
export AWS_PROFILE=my-profile

# Verify Terraform can authenticate
terraform init
```

---

### 🔍 Debugging Techniques

**Enable Debug Logging:**

```bash
# Trace-level logging (most verbose)
export TF_LOG=TRACE
export TF_LOG_PATH=./terraform-trace.log
terraform apply

# Different log levels
export TF_LOG=DEBUG   # Debug information
export TF_LOG=INFO    # Info messages
export TF_LOG=WARN    # Warnings only
export TF_LOG=ERROR   # Errors only

# Component-specific logging
export TF_LOG_CORE=TRACE     # Core operations
export TF_LOG_PROVIDER=TRACE # Provider operations

# Disable logging
unset TF_LOG TF_LOG_PATH
```

**Analyze Plan Output:**

```bash
# Save plan to file
terraform plan -out=tfplan

# Show plan in JSON
terraform show -json tfplan | jq . > plan.json

# Analyze what's changing
terraform show tfplan | grep "will be created"
terraform show tfplan | grep "will be destroyed"
terraform show tfplan | grep "will be updated"

# Show specific resource changes
terraform show tfplan | grep -A 10 "aws_instance.web"
```

**Resource Graph Analysis:**

```bash
# Generate dependency graph
terraform graph | dot -Tpng > graph.png

# Show only specific resource dependencies
terraform graph -draw-cycles | grep aws_instance

# Analyze cycle issues
terraform graph -type=plan | grep -A 5 -B 5 cycle
```

---

### 🛡️ Disaster Recovery Procedures

**Procedure 1: Complete Infrastructure Loss**

```bash
#!/bin/bash
# disaster_recovery.sh

set -e

echo "=== Terraform Disaster Recovery ==="

# Step 1: Verify state backup exists
echo "Checking state backup..."
if [ ! -f "terraform.tfstate.backup" ]; then
    echo "ERROR: No backup found!"
    exit 1
fi

# Step 2: Restore state
echo "Restoring state from backup..."
cp terraform.tfstate.backup terraform.tfstate

# Step 3: Refresh state
echo "Refreshing state..."
terraform refresh -lock=false

# Step 4: Check what needs recreation
echo "Checking infrastructure status..."
terraform plan -out=recovery.tfplan

# Step 5: Apply if needed
read -p "Apply recovery plan? (yes/no): " confirm
if [ "$confirm" = "yes" ]; then
    terraform apply recovery.tfplan
    echo "Recovery complete!"
fi
```

**Procedure 2: State File Corruption**

```bash
# Attempt recovery from remote backend versions
aws s3api list-object-versions \
    --bucket my-terraform-state \
    --prefix prod/terraform.tfstate

# Download previous version
aws s3api get-object \
    --bucket my-terraform-state \
    --key prod/terraform.tfstate \
    --version-id <VERSION_ID> \
    terraform.tfstate.recovered

# Validate recovered state
terraform state list -state=terraform.tfstate.recovered

# Replace current state if valid
mv terraform.tfstate.recovered terraform.tfstate
```

---

## Bonus 3: Terraform Certification Prep

### 📜 HashiCorp Certified: Terraform Associate (003)

#### Exam Objectives Mapping

**1. Understand Infrastructure as Code (IaC) concepts**
- ✅ See Part 1: Day 1 (Introduction)
- Benefits of IaC, IaC vs manual provisioning

**2. Understand Terraform's purpose (vs other IaC)**
- ✅ See Part 1: Day 1
- Terraform vs CloudFormation, Ansible, Pulumi

**3. Understand Terraform basics**
- ✅ See Part 1: Days 2-4
- Installation, providers, resources, CLI workflow

**4. Use the Terraform CLI (outside of core workflow)**
- ✅ See Part 1: Day 3 & Part 2: Testing
- `terraform fmt`, `validate`, `taint`, `import`, `state`

**5. Interact with Terraform modules**
- ✅ See Part 1: Day 11
- Module sources, inputs, outputs, versioning

**6. Navigate Terraform workflow**
- ✅ See Part 1: Day 3
- `init`, `plan`, `apply`, `destroy`

**7. Implement and maintain state**
- ✅ See Part 2: Days 13-15
- Local vs remote state, locking, workspaces

**8. Read, generate, and modify configuration**
- ✅ See Part 1: Days 5-10
- Resources, variables, outputs, expressions, functions

**9. Understand Terraform Cloud and Enterprise capabilities**
- ✅ See Part 2: Day 18
- Remote state, VCS integration, Sentinel, cost estimation

---

### 📝 Sample Exam Questions

**Question 1:**
Which command should you run to preview changes without modifying infrastructure?

A) `terraform apply -dry-run`
B) `terraform plan`
C) `terraform preview`
D) `terraform validate`

**Answer: B** - `terraform plan` shows changes without applying them.

---

**Question 2:**
What is the purpose of the `terraform.tfstate.backup` file?

A) It's automatically uploaded to Terraform Cloud
B) It contains the previous state before the last apply
C) It's used for disaster recovery only
D) It stores encrypted secrets

**Answer: B** - It's the previous state file, created before modifications.

---

**Question 3:**
Which meta-argument can you use to create multiple similar resources?

A) `loop`
B) `replicate`
C) `count` or `for_each`
D) `multiply`

**Answer: C** - Use `count` or `for_each` for multiple instances.

---

**Question 4:**
What does `terraform refresh` do?

A) Updates state to match real infrastructure
B) Downloads latest provider versions
C) Clears the Terraform cache
D) Reloads configuration files

**Answer: A** - Queries infrastructure and updates state file.

---

**Question 5:**
Which backend supports state locking?

A) local
B) s3 (with DynamoDB)
C) http
D) All of the above

**Answer: D** - All listed backends support locking (S3 requires DynamoDB table).

---

### 🎯 Study Tips

**Week 1-2: Fundamentals**
- Install Terraform and practice basic commands
- Create simple EC2/VPC resources
- Practice `init`, `plan`, `apply`, `destroy` workflow
- Understand state file structure

**Week 3-4: Advanced Concepts**
- Work with modules (create and consume)
- Practice state management (`state list`, `mv`, `rm`, `import`)
- Set up remote state with S3/DynamoDB
- Use workspaces for multiple environments

**Week 5-6: Best Practices**
- Implement proper project structure
- Practice variable validation and sensitive data handling
- Work with `count`, `for_each`, `dynamic` blocks
- Use provisioners and lifecycle rules

**Week 7-8: Exam Preparation**
- Review official Terraform documentation
- Take practice exams
- Build complete projects (like Projects 1-5 in this guide)
- Review all exam objectives

**Resources:**
- 📚 Official Study Guide: https://developer.hashicorp.com/terraform/tutorials/certification
- 🎓 Practice Exams: HashiCorp Learn platform
- 📖 This Complete Guide (all sections!)

---

## Bonus 4: Ultimate Terraform Cheat Sheet

### 🚀 Essential Commands

```bash
# INITIALIZATION
terraform init                  # Initialize working directory
terraform init -upgrade         # Upgrade providers
terraform init -backend-config="bucket=mybucket"  # Configure backend

# PLANNING
terraform plan                  # Show execution plan
terraform plan -out=tfplan      # Save plan to file
terraform plan -destroy         # Plan destruction
terraform plan -target=aws_instance.web  # Plan specific resource

# APPLYING
terraform apply                 # Apply changes
terraform apply tfplan          # Apply saved plan
terraform apply -auto-approve   # Skip confirmation
terraform apply -parallelism=20 # Adjust parallel operations

# DESTROYING
terraform destroy               # Destroy all resources
terraform destroy -target=aws_instance.web  # Destroy specific resource
terraform destroy -auto-approve # Skip confirmation

# STATE MANAGEMENT
terraform state list            # List all resources
terraform state show aws_instance.web  # Show resource details
terraform state mv SOURCE DEST  # Move/rename resource
terraform state rm aws_instance.web    # Remove from state
terraform state pull            # Download remote state
terraform state push            # Upload state

# IMPORTING
terraform import aws_instance.web i-12345  # Import existing resource

# WORKSPACES
terraform workspace list        # List workspaces
terraform workspace new dev     # Create workspace
terraform workspace select dev  # Switch workspace
terraform workspace delete dev  # Delete workspace

# VALIDATION & FORMATTING
terraform fmt                   # Format code
terraform fmt -recursive        # Format all files
terraform validate              # Validate configuration
terraform validate -json        # JSON output

# OUTPUTS
terraform output                # Show all outputs
terraform output instance_ip    # Show specific output
terraform output -json          # JSON format

# CONSOLE & TESTING
terraform console               # Interactive console
terraform test                  # Run tests (1.6+)

# TROUBLESHOOTING
terraform refresh               # Update state
terraform taint aws_instance.web  # Mark for recreation
terraform untaint aws_instance.web # Remove taint
terraform force-unlock LOCK_ID  # Force unlock state
terraform show                  # Show current state
terraform graph                 # Generate dependency graph
```

---

### 📦 HCL Syntax Quick Reference

**Resource Block:**

```hcl
resource "provider_type" "name" {
  argument1 = "value"
  argument2 = 123
  
  nested_block {
    key = "value"
  }
  
  dynamic "dynamic_block" {
    for_each = var.list
    content {
      name = dynamic_block.value
    }
  }
  
  count = 3
  # OR
  for_each = toset(["a", "b", "c"])
  
  lifecycle {
    create_before_destroy = true
    prevent_destroy       = false
    ignore_changes        = [tags]
  }
  
  depends_on = [resource_type.other]
  provider   = aws.alternate
}
```

**Variable Block:**

```hcl
variable "name" {
  description = "Description"
  type        = string
  default     = "default_value"
  sensitive   = false
  nullable    = false
  
  validation {
    condition     = length(var.name) > 3
    error_message = "Must be > 3 characters"
  }
}
```

**Output Block:**

```hcl
output "name" {
  description = "Description"
  value       = resource.attribute
  sensitive   = false
  depends_on  = [resource.other]
}
```

**Locals Block:**

```hcl
locals {
  common_tags = {
    Project     = "MyProject"
    Environment = var.environment
  }
  
  instance_count = var.environment == "prod" ? 3 : 1
}
```

---

### 🔧 Common Functions Reference

**String Functions:**
```hcl
upper("hello")              # "HELLO"
lower("HELLO")              # "hello"
title("hello world")        # "Hello World"
trim("  text  ", " ")       # "text"
trimspace("  text  ")       # "text"
replace("hello", "l", "r")  # "herro"
join(",", ["a", "b"])       # "a,b"
split(",", "a,b,c")         # ["a", "b", "c"]
format("Hello %s", "World") # "Hello World"
```

**Numeric Functions:**
```hcl
min(1, 2, 3)                # 1
max(1, 2, 3)                # 3
abs(-5)                     # 5
ceil(4.3)                   # 5
floor(4.7)                  # 4
```

**Collection Functions:**
```hcl
length([1, 2, 3])           # 3
element([1, 2, 3], 0)       # 1
concat([1, 2], [3, 4])      # [1, 2, 3, 4]
contains([1, 2], 1)         # true
merge({a=1}, {b=2})         # {a=1, b=2}
keys({a=1, b=2})            # ["a", "b"]
values({a=1, b=2})          # [1, 2]
lookup({a=1}, "a", 0)       # 1
```

**Type Conversion:**
```hcl
tostring(123)               # "123"
tonumber("123")             # 123
tobool("true")              # true
tolist([1, 2])              # [1, 2]
toset([1, 1, 2])           # [1, 2]
tomap({a=1})                # {a=1}
```

**Date/Time:**
```hcl
timestamp()                 # "2024-01-15T10:30:00Z"
formatdate("YYYY-MM-DD", timestamp())  # "2024-01-15"
```

**Encoding:**
```hcl
base64encode("text")        # "dGV4dA=="
base64decode("dGV4dA==")    # "text"
jsonencode({a=1})           # "{\"a\":1}"
jsondecode("{\"a\":1}")     # {a=1}
```

**Filesystem:**
```hcl
file("path/to/file")        # Read file
fileexists("path")          # Check if exists
templatefile("template.tpl", {var = "value"})
```

**IP Network:**
```hcl
cidrsubnet("10.0.0.0/16", 8, 0)  # "10.0.0.0/24"
cidrhost("10.0.0.0/24", 5)        # "10.0.0.5"
```

---

### 🎨 Common Patterns

**Conditional Resource Creation:**

```hcl
resource "aws_instance" "example" {
  count = var.create_instance ? 1 : 0
  # configuration
}
```

**Multiple Instances with Count:**

```hcl
resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = var.availability_zones[count.index]
}
```

**Multiple Instances with for_each:**

```hcl
resource "aws_instance" "servers" {
  for_each = var.server_config
  
  instance_type = each.value.type
  ami           = each.value.ami
  
  tags = {
    Name = each.key
  }
}
```

**Dynamic Blocks:**

```hcl
resource "aws_security_group" "example" {
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

---

### ⚡ Performance Tips

```bash
# Increase parallelism (default is 10)
terraform apply -parallelism=50

# Reduce output verbosity
terraform apply -compact-warnings

# Target specific resources
terraform apply -target=module.vpc

# Refresh only (don't apply)
terraform apply -refresh-only

# Skip refresh during plan
terraform plan -refresh=false
```

---

### 🔐 Security Checklist

```hcl
# ✅ DO:
- Store secrets in AWS Secrets Manager/SSM
- Use remote state with encryption
- Enable state locking
- Use .gitignore for sensitive files
- Implement least-privilege IAM
- Enable MFA for production
- Use OIDC instead of static credentials
- Scan code with tfsec/Checkov

# ❌ DON'T:
- Hardcode secrets in .tf files
- Commit .tfstate files to Git
- Use root AWS credentials
- Disable state encryption
- Skip security scanning
- Use wildcard IAM permissions
```

---

### 📋 Common Variable Types

```hcl
# String
variable "name" {
  type = string
}

# Number
variable "count" {
  type = number
}

# Bool
variable "enabled" {
  type = bool
}

# List
variable "zones" {
  type = list(string)
}

# Map
variable "tags" {
  type = map(string)
}

# Object
variable "config" {
  type = object({
    name = string
    size = number
  })
}

# Tuple
variable "tuple_example" {
  type = tuple([string, number, bool])
}

# Set
variable "unique_items" {
  type = set(string)
}

# Any (not recommended)
variable "flexible" {
  type = any
}
```

---

### 🎯 Best Practices Summary

1. **Version Control Everything** (except state)
2. **Use Remote State** (S3/Terraform Cloud)
3. **Enable State Locking** (DynamoDB)
4. **Structure Code** (modules, environments)
5. **Validate & Format** (pre-commit hooks)
6. **Use Workspaces** (dev/staging/prod)
7. **Implement Security Scanning** (tfsec, Checkov)
8. **Document Everything** (README, comments)
9. **Test Infrastructure** (Terratest)
10. **Automate CI/CD** (GitHub Actions)

---

## 🎓 Conclusion

Congratulations! 🎉 You've completed the **Terraform Complete Mastery Guide from Zero to Hero**!

### What You've Learned:

**Part 1 (Days 1-11):**
- ✅ Terraform fundamentals and installation
- ✅ HCL syntax and 100+ functions
- ✅ Providers (AWS, Azure, GCP)
- ✅ Resources, variables, outputs
- ✅ Advanced features (count, for_each, dynamic blocks)
- ✅ Modules and reusable infrastructure

**Part 2 (Days 12-22):**
- ✅ Workspaces and remote state
- ✅ State management and locking
- ✅ Provisioners and lifecycle rules
- ✅ Terraform Cloud collaboration
- ✅ Project structure and organization
- ✅ Security best practices
- ✅ Testing strategies
- ✅ CI/CD integration

**Real-World Projects:**
- ✅ Project 1: Simple Web Server
- ✅ Project 2: VPC & Networking
- ✅ Project 3: Multi-Tier Application
- ✅ Project 4: EKS Kubernetes Cluster
- ✅ Project 5: Multi-Cloud Deployment

**Bonus Content:**
- ✅ State management surgery
- ✅ Troubleshooting guide
- ✅ Certification preparation
- ✅ Complete cheat sheet

---

### 🚀 Next Steps:

1. **Practice**: Build your own infrastructure projects
2. **Contribute**: Create and share Terraform modules
3. **Certify**: Get HashiCorp Certified: Terraform Associate
4. **Automate**: Implement CI/CD pipelines
5. **Scale**: Apply patterns to production workloads

---

### 📚 Additional Resources:

- **Official Docs**: https://developer.hashicorp.com/terraform
- **Registry**: https://registry.terraform.io
- **Community**: https://discuss.hashicorp.com
- **GitHub**: https://github.com/hashicorp/terraform
- **Certification**: https://www.hashicorp.com/certification/terraform-associate

---

### 💡 Remember:

> "Infrastructure as Code is not about the tools,
> it's about the mindset of treating infrastructure
> as software with all the associated disciplines:
> version control, testing, and continuous delivery."

---

**Happy Terraforming! 🌍**

*This guide was created with ❤️ for the DevOps and Cloud Engineering community.*

---

**Document Information:**
- **Title**: Terraform Complete Mastery Guide - Part 2
- **Version**: 2.0
- **Last Updated**: December 2024
- **Author**: Tech Mastery Notebooks
- **Terraform Version**: 1.5.0 - 1.7.0
- **Total Lines**: ~15,000+ lines of comprehensive content

---

*End of Part 2*
