# Terraform: Zero to Hero Course

**Complete Guide with Simple Explanations and Examples**

---

## Table of Contents
1. [Introduction to Terraform](#1-introduction-to-terraform)
2. [Installation and Setup](#2-installation-and-setup)
3. [Terraform Basics](#3-terraform-basics)
4. [Providers](#4-providers)
5. [Resources](#5-resources)
6. [Variables](#6-variables)
7. [Outputs](#7-outputs)
8. [Data Sources](#8-data-sources)
9. [State Management](#9-state-management)
10. [Modules](#10-modules)
11. [Provisioners](#11-provisioners)
12. [Functions and Expressions](#12-functions-and-expressions)
13. [Workspaces](#13-workspaces)
14. [Remote State](#14-remote-state)
15. [Best Practices](#15-best-practices)
16. [Advanced Topics](#16-advanced-topics)
17. [Real-World Project](#17-real-world-project)

---

## 1. Introduction to Terraform

### What is Terraform?
Terraform is like a blueprint maker for cloud infrastructure. Instead of clicking buttons in AWS, Azure, or Google Cloud, you write simple code that describes what you want, and Terraform builds it for you automatically. Think of it as "infrastructure as code" - you write recipes (code) and Terraform cooks (builds) your cloud infrastructure.

### Why Use Terraform?
- **Version Control**: Track changes to your infrastructure like you track code changes
- **Reusability**: Write once, use many times across different environments
- **Automation**: No more manual clicking through cloud consoles

### Key Concepts (Simple Terms)
- **Provider**: The cloud service you're using (AWS, Azure, Google Cloud, etc.)
- **Resource**: Something you want to create (like a server, database, or network)
- **State**: Terraform's memory of what it has created
- **Plan**: A preview of what Terraform will do before it does it
- **Apply**: Actually creating/changing your infrastructure

---

## 2. Installation and Setup

### Installing Terraform

**macOS:**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

**Linux:**
```bash
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

**Windows:**
```powershell
choco install terraform
```

### Verify Installation
```bash
terraform version
```

### Basic Commands Overview
```bash
terraform init      # Initialize project (download providers)
terraform plan      # Preview changes
terraform apply     # Create/update infrastructure
terraform destroy   # Delete everything
terraform fmt       # Format your code nicely
terraform validate  # Check if code is correct
```

---

## 3. Terraform Basics

### Your First Terraform File

**Simple Explanation**: This creates a basic file on your computer. It's the "Hello World" of Terraform - the simplest thing you can create.

**File: `main.tf`**
```hcl
# This creates a simple text file on your computer
resource "local_file" "hello" {
  filename = "hello.txt"
  content  = "Hello from Terraform!"
}
```

**Run it:**
```bash
terraform init    # Get ready (downloads the 'local' provider)
terraform plan    # See what will happen
terraform apply   # Create the file (type 'yes' when asked)
```

**What happens**: Terraform creates a file called `hello.txt` with the text "Hello from Terraform!" in your current directory.

---

## 4. Providers

### What is a Provider?
A provider is like a translator between Terraform and cloud services. AWS speaks its own language, Azure speaks differently - providers help Terraform talk to all of them.

### AWS Provider Example

**Simple Explanation**: This tells Terraform "I want to use AWS, and I want to create things in the US East region."

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
  region = "us-east-1"
}
```

### Multi-Provider Example

**Simple Explanation**: You can use multiple cloud providers in one project. Here we use both AWS and Azure.

```hcl
# AWS Provider
provider "aws" {
  region = "us-east-1"
  alias  = "us_east"
}

# Azure Provider
provider "azurerm" {
  features {}
}

# Use specific provider
resource "aws_s3_bucket" "my_bucket" {
  provider = aws.us_east
  bucket   = "my-awesome-bucket"
}
```

---

## 5. Resources

### What is a Resource?
A resource is anything you want to create in the cloud - a virtual machine, a database, a storage bucket, etc. It's the actual "thing" you're building.

### EC2 Instance (Virtual Server) Example

**Simple Explanation**: This creates a virtual computer in AWS. The `ami` is the operating system image, and `instance_type` is how powerful the computer is (t2.micro is the smallest/cheapest).

```hcl
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu 20.04
  instance_type = "t2.micro"                # Small, free-tier server
  
  tags = {
    Name = "MyWebServer"
    Environment = "Development"
  }
}
```

### S3 Bucket (Cloud Storage) Example

**Simple Explanation**: This creates a storage bucket in AWS where you can store files, like Dropbox but for your applications.

```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name-12345"
  
  tags = {
    Name        = "My Bucket"
    Environment = "Dev"
  }
}

# Make the bucket private (secure)
resource "aws_s3_bucket_acl" "bucket_acl" {
  bucket = aws_s3_bucket.my_bucket.id
  acl    = "private"
}
```

### Resource Dependencies

**Simple Explanation**: Sometimes one resource depends on another (you need a network before you can create a server in it). Terraform automatically figures this out when you reference one resource in another.

```hcl
# First create a VPC (Virtual Private Cloud - like your own network)
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Then create a subnet inside that VPC
resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id  # This creates automatic dependency
  cidr_block = "10.0.1.0/24"
}

# Finally create a server in that subnet
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id  # Depends on subnet
}
```

---

## 6. Variables

### What are Variables?
Variables are like blank spaces in a form that you can fill in differently each time. Instead of hardcoding values, you use variables to make your code reusable.

### Basic Variable Definition

**Simple Explanation**: Define variables in `variables.tf` so you can change values without editing the main code.

**File: `variables.tf`**
```hcl
# Simple string variable
variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

# Number variable
variable "instance_count" {
  description = "Number of EC2 instances to create"
  type        = number
  default     = 2
}

# Boolean variable (true/false)
variable "enable_monitoring" {
  description = "Enable CloudWatch monitoring"
  type        = bool
  default     = true
}

# List variable (multiple values)
variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

# Map variable (key-value pairs)
variable "instance_tags" {
  description = "Tags for EC2 instances"
  type        = map(string)
  default = {
    Environment = "Dev"
    Team        = "Engineering"
  }
}
```

### Using Variables

**File: `main.tf`**
```hcl
provider "aws" {
  region = var.region  # Use the variable
}

resource "aws_instance" "web" {
  count         = var.instance_count  # Create multiple instances
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  monitoring = var.enable_monitoring
  
  tags = var.instance_tags
}
```

### Providing Variable Values

**Method 1: terraform.tfvars file**
```hcl
region         = "us-west-2"
instance_count = 3
enable_monitoring = false
```

**Method 2: Command line**
```bash
terraform apply -var="region=us-west-2" -var="instance_count=3"
```

**Method 3: Environment variables**
```bash
export TF_VAR_region="us-west-2"
terraform apply
```

---

## 7. Outputs

### What are Outputs?
Outputs are like receipts - after Terraform creates something, outputs show you important information about what was created (like IP addresses, URLs, etc.).

### Basic Output Examples

**Simple Explanation**: After creating resources, you often need to know details about them (like the IP address of a server). Outputs display this information.

**File: `outputs.tf`**
```hcl
# Output the instance's public IP address
output "instance_ip" {
  description = "The public IP address of the web server"
  value       = aws_instance.web.public_ip
}

# Output the S3 bucket name
output "bucket_name" {
  description = "The name of the S3 bucket"
  value       = aws_s3_bucket.my_bucket.id
}

# Output multiple instance IPs (when count is used)
output "all_instance_ips" {
  description = "Public IPs of all web servers"
  value       = aws_instance.web[*].public_ip
}

# Sensitive output (won't show in console by default)
output "database_password" {
  description = "RDS database password"
  value       = aws_db_instance.main.password
  sensitive   = true
}
```

### Viewing Outputs
```bash
terraform output              # Show all outputs
terraform output instance_ip  # Show specific output
terraform output -json        # Get outputs in JSON format
```

---

## 8. Data Sources

### What are Data Sources?
Data sources let you fetch information about existing resources (not created by Terraform). It's like looking up information in a phone book - you're reading, not creating.

### Example: Getting Latest AMI

**Simple Explanation**: Instead of hardcoding an AMI ID (which changes), use a data source to automatically find the latest Ubuntu image.

```hcl
# Find the latest Ubuntu AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical (Ubuntu's owner)
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

# Use the data source in a resource
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id  # Use the found AMI
  instance_type = "t2.micro"
}
```

### Example: Getting Existing VPC

**Simple Explanation**: If a VPC already exists (maybe created manually), use a data source to find it and use it in your code.

```hcl
# Find existing VPC by tag
data "aws_vpc" "existing" {
  tags = {
    Name = "my-existing-vpc"
  }
}

# Create subnet in the existing VPC
resource "aws_subnet" "new_subnet" {
  vpc_id     = data.aws_vpc.existing.id
  cidr_block = "10.0.1.0/24"
}
```

---

## 9. State Management

### What is State?
State is Terraform's memory - it remembers what it created so it knows what to update or delete. The state file (`terraform.tfstate`) is like a detailed receipt of everything Terraform has built.

### State Commands

**Simple Explanation**: These commands help you inspect and manage what Terraform knows about your infrastructure.

```bash
# List all resources in state
terraform state list

# Show details of a specific resource
terraform state show aws_instance.web

# Remove a resource from state (doesn't delete actual resource)
terraform state rm aws_instance.web

# Move a resource to a different name in state
terraform state mv aws_instance.web aws_instance.web_server

# Pull remote state to local
terraform state pull > terraform.tfstate.backup
```

### Local Backend (Default)

**Simple Explanation**: By default, state is stored in a local file. This works for solo projects but not for teams.

```hcl
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```

### Remote Backend (S3)

**Simple Explanation**: Store state in S3 so your whole team can access it. The DynamoDB table prevents two people from running Terraform at the same time (state locking).

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

---

## 10. Modules

### What are Modules?
Modules are like reusable templates - instead of copying and pasting code, you create a module once and reuse it many times. It's like having a recipe that you can use to cook the same meal repeatedly.

### Creating a Simple Module

**Simple Explanation**: Group related resources together into a module. Here's a module that creates a web server with all necessary components.

**Directory Structure:**
```
modules/
  web-server/
    main.tf
    variables.tf
    outputs.tf
root/
  main.tf
```

**File: `modules/web-server/main.tf`**
```hcl
resource "aws_instance" "server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  tags = {
    Name = var.server_name
  }
}

resource "aws_security_group" "server_sg" {
  name = "${var.server_name}-sg"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

**File: `modules/web-server/variables.tf`**
```hcl
variable "ami_id" {
  description = "AMI ID for the instance"
  type        = string
}

variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.micro"
}

variable "server_name" {
  description = "Name of the server"
  type        = string
}
```

**File: `modules/web-server/outputs.tf`**
```hcl
output "instance_id" {
  value = aws_instance.server.id
}

output "public_ip" {
  value = aws_instance.server.public_ip
}
```

### Using the Module

**File: `main.tf`**
```hcl
# Use the module to create a dev web server
module "dev_server" {
  source        = "./modules/web-server"
  ami_id        = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  server_name   = "dev-web-server"
}

# Use the same module for production
module "prod_server" {
  source        = "./modules/web-server"
  ami_id        = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.large"
  server_name   = "prod-web-server"
}

# Access module outputs
output "dev_ip" {
  value = module.dev_server.public_ip
}
```

### Using Public Modules

**Simple Explanation**: Instead of writing everything from scratch, use pre-built modules from the Terraform Registry (like using npm packages or pip libraries).

```hcl
# Use AWS VPC module from Terraform Registry
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  
  name = "my-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
  
  enable_nat_gateway = true
  enable_vpn_gateway = false
}
```

---

## 11. Provisioners

### What are Provisioners?
Provisioners run scripts or commands on resources after they're created. Think of it as the "post-installation setup" - like installing software on a new computer after you buy it.

### File Provisioner

**Simple Explanation**: Copy files from your computer to the newly created server.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-key-pair"
  
  # Copy a file to the server
  provisioner "file" {
    source      = "app.conf"
    destination = "/etc/app/app.conf"
    
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }
}
```

### Remote-Exec Provisioner

**Simple Explanation**: Run commands on the server after it's created (like installing web server software).

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-key-pair"
  
  # Run commands on the server
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx",
      "sudo systemctl start nginx"
    ]
    
    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }
}
```

### Local-Exec Provisioner

**Simple Explanation**: Run commands on YOUR computer (not the server) after a resource is created.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  # Run a command locally
  provisioner "local-exec" {
    command = "echo ${self.public_ip} > ip_address.txt"
  }
  
  # Run when destroying
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance destroyed' >> log.txt"
  }
}
```

---

## 12. Functions and Expressions

### Built-in Functions

**Simple Explanation**: Terraform has built-in functions to manipulate data, like Excel formulas but for infrastructure code.

```hcl
# String functions
locals {
  server_name = "web-server"
  upper_name  = upper(local.server_name)      # "WEB-SERVER"
  lower_name  = lower(local.server_name)      # "web-server"
  title_name  = title(local.server_name)      # "Web-Server"
  
  # Join strings
  full_name = join("-", ["dev", "web", "server"])  # "dev-web-server"
  
  # Split strings
  parts = split("-", "dev-web-server")  # ["dev", "web", "server"]
}

# Numeric functions
locals {
  numbers = [1, 5, 3, 8, 2]
  max_num = max(local.numbers...)     # 8
  min_num = min(local.numbers...)     # 1
  
  # Round numbers
  rounded = ceil(4.3)    # 5
  floored = floor(4.7)   # 4
}

# Collection functions
locals {
  servers = ["web1", "web2", "web3"]
  
  # Get length
  count = length(local.servers)  # 3
  
  # Get element
  first = element(local.servers, 0)  # "web1"
  
  # Check if contains
  has_web1 = contains(local.servers, "web1")  # true
  
  # Merge maps
  tags1 = { Name = "Server", Env = "Dev" }
  tags2 = { Team = "Engineering" }
  all_tags = merge(local.tags1, local.tags2)
}
```

### Conditional Expressions

**Simple Explanation**: Make decisions in your code - "if this, then that."

```hcl
variable "environment" {
  default = "dev"
}

# Ternary operator: condition ? true_value : false_value
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.environment == "prod" ? "t2.large" : "t2.micro"
  
  tags = {
    Name = var.environment == "prod" ? "Production Server" : "Dev Server"
  }
}
```

### For Expressions

**Simple Explanation**: Loop through lists or maps to transform data, like map/filter in JavaScript or list comprehensions in Python.

```hcl
locals {
  # List transformation
  server_names = ["web1", "web2", "web3"]
  upper_names  = [for s in local.server_names : upper(s)]
  # Result: ["WEB1", "WEB2", "WEB3"]
  
  # List filtering
  numbers = [1, 2, 3, 4, 5]
  even_numbers = [for n in local.numbers : n if n % 2 == 0]
  # Result: [2, 4]
  
  # Map transformation
  users = {
    john = "admin"
    jane = "user"
  }
  upper_roles = { for name, role in local.users : name => upper(role) }
  # Result: { john = "ADMIN", jane = "USER" }
}
```

### Dynamic Blocks

**Simple Explanation**: Create repeating blocks dynamically instead of copying and pasting the same code multiple times.

```hcl
variable "ingress_rules" {
  default = [
    { port = 80, description = "HTTP" },
    { port = 443, description = "HTTPS" },
    { port = 22, description = "SSH" }
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"
  
  # Create multiple ingress rules dynamically
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = ingress.value.description
    }
  }
}
```

---

## 13. Workspaces

### What are Workspaces?
Workspaces are like having multiple copies of your infrastructure using the same code but different state files. Think of it as having dev, staging, and production environments from one codebase.

### Working with Workspaces

**Simple Explanation**: Create separate environments (dev, staging, prod) without duplicating your Terraform code.

```bash
# List workspaces
terraform workspace list

# Create new workspace
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

# Switch workspace
terraform workspace select dev

# Show current workspace
terraform workspace show

# Delete workspace
terraform workspace delete staging
```

### Using Workspace in Code

```hcl
# Use workspace name in resource naming
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = terraform.workspace == "prod" ? "t2.large" : "t2.micro"
  
  tags = {
    Name        = "web-${terraform.workspace}"
    Environment = terraform.workspace
  }
}

# Different configurations per workspace
locals {
  instance_counts = {
    dev     = 1
    staging = 2
    prod    = 5
  }
  
  current_count = local.instance_counts[terraform.workspace]
}

resource "aws_instance" "app" {
  count         = local.current_count
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

---

## 14. Remote State

### What is Remote State?
Remote state stores your state file in a shared location (like S3 or Terraform Cloud) so teams can collaborate. It also adds locking so two people can't modify infrastructure at the same time.

### S3 Backend Configuration

**Simple Explanation**: Store state in S3 bucket so it's backed up and shareable with your team.

**Step 1: Create S3 bucket and DynamoDB table (one-time setup)**
```hcl
# Run this first to create backend resources
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state-bucket"
  
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  
  attribute {
    name = "LockID"
    type = "S"
  }
}
```

**Step 2: Configure backend in your main project**
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

### Terraform Cloud Backend

**Simple Explanation**: Use Terraform Cloud (free for small teams) to store state and run Terraform in the cloud.

```hcl
terraform {
  cloud {
    organization = "my-org"
    
    workspaces {
      name = "my-app-prod"
    }
  }
}
```

### Remote State Data Source

**Simple Explanation**: Read outputs from another Terraform project's state file. Useful when different teams manage different parts of infrastructure.

```hcl
# Read state from another project
data "terraform_remote_state" "network" {
  backend = "s3"
  
  config = {
    bucket = "my-terraform-state-bucket"
    key    = "network/terraform.tfstate"
    region = "us-east-1"
  }
}

# Use outputs from the other project
resource "aws_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = data.terraform_remote_state.network.outputs.subnet_id
}
```

---

## 15. Best Practices

### Project Structure

**Simple Explanation**: Organize your Terraform code in a clean, maintainable structure.

```
project/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── outputs.tf
│   ├── staging/
│   └── prod/
├── modules/
│   ├── networking/
│   ├── compute/
│   └── database/
├── global/
│   ├── iam/
│   └── s3/
└── README.md
```

### Naming Conventions

```hcl
# Good naming practices
resource "aws_instance" "web_server" {         # Use underscores
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
  
  tags = {
    Name        = "web-server-${var.environment}"  # Use hyphens in tags
    Environment = var.environment
    ManagedBy   = "Terraform"
    Project     = var.project_name
  }
}

# Use locals for computed values
locals {
  common_tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
    Project     = var.project_name
  }
  
  name_prefix = "${var.project_name}-${var.environment}"
}

resource "aws_s3_bucket" "assets" {
  bucket = "${local.name_prefix}-assets"
  tags   = local.common_tags
}
```

### Variable Validation

**Simple Explanation**: Add validation rules to variables to catch mistakes early.

```hcl
variable "environment" {
  description = "Environment name"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_count" {
  description = "Number of instances"
  type        = number
  
  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 10
    error_message = "Instance count must be between 1 and 10."
  }
}
```

### Use Terraform Fmt and Validate

```bash
# Format code properly
terraform fmt -recursive

# Validate configuration
terraform validate

# Check for security issues (requires tfsec)
tfsec .
```

### Security Best Practices

```hcl
# Don't hardcode sensitive values
resource "aws_db_instance" "main" {
  username = var.db_username         # Good: Use variables
  password = var.db_password         # Good: Pass via environment or vault
  
  # Bad examples (don't do this):
  # username = "admin"
  # password = "password123"
}

# Use sensitive flag for outputs
output "database_password" {
  value     = aws_db_instance.main.password
  sensitive = true  # Prevents showing in logs
}

# Enable encryption
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
```

---

## 16. Advanced Topics

### Count vs For_Each

**Simple Explanation**: Both create multiple resources, but `for_each` is better when you need to reference specific items.

```hcl
# Count (good for identical resources)
variable "instance_count" {
  default = 3
}

resource "aws_instance" "web" {
  count         = var.instance_count
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "web-${count.index}"
  }
}

# For_each (better for named resources)
variable "servers" {
  default = {
    web  = "t2.micro"
    api  = "t2.small"
    db   = "t2.medium"
  }
}

resource "aws_instance" "servers" {
  for_each = var.servers
  
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = each.value
  
  tags = {
    Name = each.key
  }
}

# Access specific instance
output "web_server_ip" {
  value = aws_instance.servers["web"].public_ip
}
```

### Lifecycle Rules

**Simple Explanation**: Control how Terraform creates, updates, or destroys resources.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  lifecycle {
    # Create new resource before destroying old one
    create_before_destroy = true
    
    # Prevent accidental deletion
    prevent_destroy = false
    
    # Ignore changes to specific attributes
    ignore_changes = [
      tags["LastModified"],
      user_data
    ]
  }
}
```

### Depends_On

**Simple Explanation**: Explicitly declare dependencies when Terraform can't figure them out automatically.

```hcl
resource "aws_iam_role" "example" {
  name = "example-role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy" "example" {
  name = "example-policy"
  role = aws_iam_role.example.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = ["s3:*"]
      Effect   = "Allow"
      Resource = "*"
    }]
  })
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.example.name
  
  # Wait for policy to be attached before creating instance
  depends_on = [aws_iam_role_policy.example]
}
```

### Terraform Import

**Simple Explanation**: Import existing resources (created manually or by other tools) into Terraform management.

```bash
# Import existing EC2 instance
terraform import aws_instance.web i-1234567890abcdef0

# Import S3 bucket
terraform import aws_s3_bucket.my_bucket my-existing-bucket

# After import, write the configuration to match
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  # ... other attributes
}
```

### Null Resource and Triggers

**Simple Explanation**: Run provisioners or scripts without creating actual infrastructure, useful for running automation tasks.

```hcl
resource "null_resource" "health_check" {
  # Run this whenever the instance ID changes
  triggers = {
    instance_id = aws_instance.web.id
  }
  
  provisioner "local-exec" {
    command = "curl http://${aws_instance.web.public_ip}/health"
  }
}
```

---

## 17. Real-World Project

### Complete 3-Tier Web Application

**Simple Explanation**: Build a complete production-ready web application infrastructure with web servers, application servers, and database.

**Project Structure:**
```
web-app/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
├── modules/
│   ├── networking/
│   ├── security/
│   ├── compute/
│   └── database/
```

**File: `variables.tf`**
```hcl
variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "myapp"
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "db_username" {
  description = "Database username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
```

**File: `main.tf`**
```hcl
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
    key            = "web-app/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
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

# VPC and Networking
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${var.project_name}-${var.environment}-igw"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-${var.environment}-public-${count.index + 1}"
  }
}

# Private Subnets
resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index + 2)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "${var.project_name}-${var.environment}-private-${count.index + 1}"
  }
}

# Data source for availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Route Table for Public Subnets
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${var.project_name}-${var.environment}-public-rt"
  }
}

# Associate public subnets with route table
resource "aws_route_table_association" "public" {
  count          = 2
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# Security Group for Web Servers
resource "aws_security_group" "web" {
  name        = "${var.project_name}-${var.environment}-web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTP"
  }
  
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTPS"
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-${var.environment}-web-sg"
  }
}

# Security Group for Database
resource "aws_security_group" "db" {
  name        = "${var.project_name}-${var.environment}-db-sg"
  description = "Security group for database"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.web.id]
    description     = "Allow MySQL from web servers"
  }
  
  tags = {
    Name = "${var.project_name}-${var.environment}-db-sg"
  }
}

# Application Load Balancer
resource "aws_lb" "main" {
  name               = "${var.project_name}-${var.environment}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.web.id]
  subnets            = aws_subnet.public[*].id
  
  tags = {
    Name = "${var.project_name}-${var.environment}-alb"
  }
}

# Target Group
resource "aws_lb_target_group" "web" {
  name     = "${var.project_name}-${var.environment}-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id
  
  health_check {
    path                = "/"
    healthy_threshold   = 2
    unhealthy_threshold = 10
  }
  
  tags = {
    Name = "${var.project_name}-${var.environment}-tg"
  }
}

# Listener
resource "aws_lb_listener" "web" {
  load_balancer_arn = aws_lb.main.arn
  port              = "80"
  protocol          = "HTTP"
  
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web.arn
  }
}

# Launch Template
resource "aws_launch_template" "web" {
  name_prefix   = "${var.project_name}-${var.environment}-"
  image_id      = data.aws_ami.ubuntu.id
  instance_type = var.environment == "prod" ? "t3.medium" : "t3.micro"
  
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = base64encode(<<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y nginx
              echo "<h1>Hello from ${var.project_name}-${var.environment}</h1>" > /var/www/html/index.html
              systemctl start nginx
              systemctl enable nginx
              EOF
  )
  
  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "${var.project_name}-${var.environment}-web"
    }
  }
}

# Auto Scaling Group
resource "aws_autoscaling_group" "web" {
  name                = "${var.project_name}-${var.environment}-asg"
  vpc_zone_identifier = aws_subnet.public[*].id
  target_group_arns   = [aws_lb_target_group.web.arn]
  health_check_type   = "ELB"
  min_size            = var.environment == "prod" ? 2 : 1
  max_size            = var.environment == "prod" ? 10 : 3
  desired_capacity    = var.environment == "prod" ? 4 : 2
  
  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }
  
  tag {
    key                 = "Name"
    value               = "${var.project_name}-${var.environment}-asg-instance"
    propagate_at_launch = true
  }
}

# RDS Subnet Group
resource "aws_db_subnet_group" "main" {
  name       = "${var.project_name}-${var.environment}-db-subnet"
  subnet_ids = aws_subnet.private[*].id
  
  tags = {
    Name = "${var.project_name}-${var.environment}-db-subnet"
  }
}

# RDS Instance
resource "aws_db_instance" "main" {
  identifier             = "${var.project_name}-${var.environment}-db"
  engine                 = "mysql"
  engine_version         = "8.0"
  instance_class         = var.environment == "prod" ? "db.t3.medium" : "db.t3.micro"
  allocated_storage      = var.environment == "prod" ? 100 : 20
  storage_encrypted      = true
  db_name                = replace(var.project_name, "-", "")
  username               = var.db_username
  password               = var.db_password
  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.db.id]
  skip_final_snapshot    = var.environment != "prod"
  multi_az               = var.environment == "prod"
  
  backup_retention_period = var.environment == "prod" ? 7 : 1
  
  tags = {
    Name = "${var.project_name}-${var.environment}-db"
  }
}

# Get latest Ubuntu AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}
```

**File: `outputs.tf`**
```hcl
output "load_balancer_dns" {
  description = "DNS name of the load balancer"
  value       = aws_lb.main.dns_name
}

output "database_endpoint" {
  description = "RDS database endpoint"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "web_url" {
  description = "URL to access the application"
  value       = "http://${aws_lb.main.dns_name}"
}
```

**File: `terraform.tfvars`**
```hcl
project_name = "myapp"
environment  = "dev"
region       = "us-east-1"
vpc_cidr     = "10.0.0.0/16"

# Don't put sensitive values here in production!
# Use environment variables or secret management instead
db_username = "admin"
db_password = "changeme123!"
```

### Running the Project

```bash
# Initialize
terraform init

# Plan
terraform plan

# Apply
terraform apply -auto-approve

# Get outputs
terraform output

# Access the application
terraform output web_url

# Destroy when done
terraform destroy -auto-approve
```

---

## Quick Reference Commands

```bash
# Initialization
terraform init                    # Initialize working directory
terraform init -upgrade           # Upgrade providers

# Planning
terraform plan                    # Show execution plan
terraform plan -out=plan.tfplan   # Save plan to file

# Applying
terraform apply                   # Apply changes
terraform apply plan.tfplan       # Apply saved plan
terraform apply -auto-approve     # Skip confirmation

# Destroying
terraform destroy                 # Destroy all resources
terraform destroy -target=<resource>  # Destroy specific resource

# State Management
terraform state list              # List resources in state
terraform state show <resource>   # Show resource details
terraform state rm <resource>     # Remove resource from state
terraform state mv <src> <dest>   # Rename resource in state

# Outputs
terraform output                  # Show all outputs
terraform output <name>           # Show specific output

# Formatting & Validation
terraform fmt                     # Format code
terraform fmt -recursive          # Format all files
terraform validate                # Validate configuration

# Workspaces
terraform workspace list          # List workspaces
terraform workspace new <name>    # Create workspace
terraform workspace select <name> # Switch workspace

# Other
terraform show                    # Show current state
terraform console                 # Interactive console
terraform graph                   # Generate dependency graph
terraform providers               # Show providers
```

---

## Congratulations! 🎉

You've completed the Terraform Zero to Hero course! You now know:

1. ✅ What Terraform is and why to use it
2. ✅ How to install and configure Terraform
3. ✅ Basic concepts (providers, resources, state)
4. ✅ Variables, outputs, and data sources
5. ✅ Modules for code reusability
6. ✅ Functions and expressions
7. ✅ Workspaces and remote state
8. ✅ Best practices and security
9. ✅ Advanced features
10. ✅ Real-world project implementation

### Next Steps:
- Practice building infrastructure in your cloud provider
- Explore Terraform Registry for pre-built modules
- Learn about Terraform Cloud for team collaboration
- Contribute to open-source Terraform modules
- Build automated CI/CD pipelines with Terraform

### Resources:
- [Terraform Documentation](https://www.terraform.io/docs)
- [Terraform Registry](https://registry.terraform.io/)
- [HashiCorp Learn](https://learn.hashicorp.com/terraform)
- [Terraform Best Practices](https://www.terraform-best-practices.com/)

Happy Terraforming! 🚀
