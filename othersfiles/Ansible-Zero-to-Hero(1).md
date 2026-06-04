# 🚀 Ansible Zero to Hero - Complete Course

A comprehensive course covering Ansible from basics to advanced topics with concise concepts and practical examples.

---

## 📚 Table of Contents

1. [Introduction and Setup](#part-1-introduction-and-setup)
2. [Inventory Deep Dive](#part-2-inventory-deep-dive)
3. [Ad-hoc Commands](#part-3-ad-hoc-commands)
4. [Playbooks Fundamentals](#part-4-playbooks-fundamentals)
5. [Variables and Facts](#part-5-variables-and-facts)
6. [Conditionals and Loops](#part-6-conditionals-and-loops)
7. [Handlers and Templates](#part-7-handlers-and-templates)
8. [Roles](#part-8-roles)
9. [Ansible Vault](#part-9-ansible-vault)
10. [Advanced Topics](#part-10-advanced-topics)

---

## 🎯 Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BEGINNER                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 01. Setup    │───▶│ 02. Inventory│───▶│ 03. Ad-hoc   │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      INTERMEDIATE                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 04. Playbooks│───▶│ 05. Variables│───▶│ 06. Loops    │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        ADVANCED                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ 07. Templates│───▶│ 08. Roles    │───▶│ 09. Vault    │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                  │                   │
│                                                  ▼                   │
│                                          ┌──────────────┐           │
│                                          │ 10. Advanced │           │
│                                          └──────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
```

---

# Part 1: Introduction and Setup

## What is Ansible?

Ansible is an open-source automation tool used for configuration management, application deployment, and task automation. It uses a simple, human-readable language called YAML and operates over SSH, requiring no agents on managed nodes.

```
┌─────────────────┐          SSH          ┌─────────────────┐
│  Control Node   │ ──────────────────▶   │  Managed Node   │
│  (Your Machine) │                       │  (Target Server)│
│  - Ansible      │                       │  - No Agent     │
│  - Playbooks    │                       │  - Python only  │
└─────────────────┘                       └─────────────────┘
```

## Why Ansible?

Ansible stands out because it's agentless, meaning you don't need to install any software on target machines. It uses simple YAML syntax that's easy to read and write, making infrastructure as code accessible to everyone.

### Key Benefits

| Feature | Description |
|---------|-------------|
| **Agentless** | No software needed on managed nodes |
| **Simple** | YAML-based, human-readable syntax |
| **Powerful** | Can manage thousands of nodes |
| **Idempotent** | Same result regardless of how many times you run it |
| **Extensible** | Large collection of modules and plugins |

## Ansible Architecture

Ansible follows a push-based architecture where the control node pushes configurations to managed nodes over SSH. The control node contains inventory files (list of hosts), playbooks (automation scripts), and modules (units of work).

```
┌─────────────────────────────────────────────────────────────┐
│                      CONTROL NODE                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Inventory  │  │  Playbooks  │  │      Modules        │ │
│  │  (hosts)    │  │  (.yml)     │  │  (apt, yum, copy)   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ SSH/WinRM
                              ▼
        ┌─────────────────────────────────────────────┐
        │              MANAGED NODES                   │
        │  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
        │  │ Web     │  │ DB      │  │ App     │     │
        │  │ Server  │  │ Server  │  │ Server  │     │
        │  └─────────┘  └─────────┘  └─────────┘     │
        └─────────────────────────────────────────────┘
```

### Core Components

| Component | Purpose |
|-----------|---------|
| **Control Node** | Machine where Ansible is installed and run from |
| **Managed Nodes** | Target machines being configured |
| **Inventory** | List of managed nodes |
| **Modules** | Units of code that perform specific tasks |
| **Playbooks** | YAML files containing automation tasks |
| **Plugins** | Extend Ansible's core functionality |

## Installation

### Installing on Ubuntu/Debian

```bash
# Update package index
sudo apt update

# Install software-properties-common
sudo apt install software-properties-common

# Add Ansible PPA
sudo add-apt-repository --yes --update ppa:ansible/ansible

# Install Ansible
sudo apt install ansible

# Verify installation
ansible --version
```

### Installing on RHEL/CentOS/Rocky Linux

```bash
# Enable EPEL repository
sudo dnf install epel-release

# Install Ansible
sudo dnf install ansible

# Verify installation
ansible --version
```

### Installing on macOS

```bash
# Using Homebrew
brew install ansible

# Verify installation
ansible --version
```

### Installing via pip (All Platforms)

```bash
# Install pip if not present
python3 -m ensurepip --upgrade

# Install Ansible using pip
pip3 install ansible

# Verify installation
ansible --version
```

## First Steps

### Creating Your First Inventory

An inventory file defines the hosts Ansible will manage. Create a simple inventory file listing your target servers with their connection details.

**File: `inventory.ini`**

```ini
# Simple inventory file

# Single host
webserver1 ansible_host=192.168.1.10

# Group of hosts
[webservers]
web1 ansible_host=192.168.1.11
web2 ansible_host=192.168.1.12

[dbservers]
db1 ansible_host=192.168.1.20
db2 ansible_host=192.168.1.21

# Group of groups
[production:children]
webservers
dbservers

# Variables for a group
[webservers:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### Testing Connectivity

Use the `ping` module to test if Ansible can connect to your managed nodes.

```bash
# Ping all hosts in inventory
ansible all -i inventory.ini -m ping

# Ping specific group
ansible webservers -i inventory.ini -m ping
```

**Expected Output:**

```
web1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

### Basic ansible.cfg Configuration

**File: `ansible.cfg`**

```ini
[defaults]
inventory = ./inventory/production.ini
remote_user = ubuntu
host_key_checking = False
forks = 10
retry_files_enabled = False
roles_path = ./roles
stdout_callback = yaml

[privilege_escalation]
become = True
become_method = sudo
become_user = root

[ssh_connection]
pipelining = True
```

---

# Part 2: Inventory Deep Dive

## Inventory Basics

The inventory is Ansible's source of truth for all managed hosts. It can be a simple static file or dynamically generated from cloud providers.

## INI Format

INI format is the traditional and most common way to define inventory.

```ini
# Ungrouped hosts
server1.example.com

# Web servers group
[webservers]
web1.example.com
web2.example.com

# Database servers group
[dbservers]
db1.example.com ansible_host=10.0.0.50

# Numeric patterns - creates web[01-10].example.com
[webfarm]
web[01:10].example.com

# Parent group containing child groups
[production:children]
webservers
dbservers

# Variables for all production hosts
[production:vars]
ansible_user=admin
environment=production
```

## YAML Format

YAML format offers more flexibility and readability for complex inventories.

```yaml
---
all:
  hosts:
    server1.example.com:
  
  children:
    webservers:
      hosts:
        web1.example.com:
          http_port: 80
        web2.example.com:
          http_port: 8080
      vars:
        ansible_user: www-data
    
    dbservers:
      hosts:
        db1.example.com:
          ansible_host: 10.0.0.50
          mysql_port: 3306
      vars:
        ansible_user: dba
```

## Host and Group Variables

Variables can be defined in separate files for maintainability.

### Directory Structure

```
inventory/
├── production.ini
├── group_vars/
│   ├── all.yml
│   ├── webservers.yml
│   └── dbservers.yml
└── host_vars/
    └── web1.example.com.yml
```

### Variable Precedence (Low to High)

```
1. group_vars/all
2. group_vars/<group_name>
3. host_vars/<host_name>
4. Playbook vars
5. Extra vars (-e)
```

## Dynamic Inventory

Dynamic inventory scripts generate host information on-the-fly from external sources.

### AWS EC2 Dynamic Inventory

**File: `aws_ec2.yml`**

```yaml
---
plugin: amazon.aws.aws_ec2

regions:
  - us-east-1

filters:
  instance-state-name: running

keyed_groups:
  - key: tags.Environment
    prefix: env
  - key: tags.Role
    prefix: role

compose:
  ansible_host: public_ip_address
```

```bash
# Test dynamic inventory
ansible-inventory -i aws_ec2.yml --list
```

---

# Part 3: Ad-hoc Commands

## What are Ad-hoc Commands?

Ad-hoc commands are one-liner Ansible commands that execute a single task on target hosts. They're perfect for quick tasks without writing a full playbook.

```bash
# Basic syntax
ansible <pattern> -m <module> -a "<arguments>"
```

## Common Modules

### ping Module

```bash
ansible all -m ping
```

### command Module

```bash
ansible all -m command -a "uptime"
ansible all -m command -a "df -h"
ansible all -a "hostname"  # -m command is default
```

### shell Module

```bash
ansible all -m shell -a "ps aux | grep nginx | wc -l"
ansible all -m shell -a "df -h > /tmp/disk_report.txt"
```

### copy Module

```bash
ansible all -m copy -a "src=/local/file.txt dest=/remote/file.txt"
ansible all -m copy -a "src=/local/script.sh dest=/usr/local/bin/script.sh mode=0755"
```

### file Module

```bash
ansible all -m file -a "path=/app/data state=directory mode=0755"
ansible all -m file -a "path=/tmp/unwanted.txt state=absent"
```

### apt Module (Debian/Ubuntu)

```bash
ansible webservers -m apt -a "name=nginx state=present" -b
ansible webservers -m apt -a "upgrade=yes update_cache=yes" -b
```

### service Module

```bash
ansible webservers -m service -a "name=nginx state=started enabled=yes" -b
ansible webservers -m service -a "name=nginx state=restarted" -b
```

### user Module

```bash
ansible all -m user -a "name=deploy state=present" -b
ansible all -m user -a "name=deploy groups=docker,sudo append=yes" -b
```

### setup Module

```bash
ansible all -m setup
ansible all -m setup -a "filter=ansible_distribution*"
```

## Privilege Escalation

```bash
ansible all -m apt -a "name=nginx state=present" -b
ansible all -m command -a "whoami" -b --become-user=postgres
ansible all -m apt -a "name=nginx state=present" -b -K  # Ask for sudo password
```

---

# Part 4: Playbooks Fundamentals

## What are Playbooks?

Playbooks are YAML files that define automation workflows consisting of one or more plays. Each play targets specific hosts and contains a list of tasks to execute in order.

## Playbook Structure

```yaml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  gather_facts: yes
  
  vars:
    http_port: 80
    
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        
    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

## Tasks and Modules

### Package Management

```yaml
- name: Install packages
  apt:
    name:
      - nginx
      - php-fpm
      - mysql-client
    state: present
    update_cache: yes
```

### File Operations

```yaml
- name: Copy configuration
  copy:
    src: nginx.conf
    dest: /etc/nginx/nginx.conf
    owner: root
    mode: '0644'
  notify: Restart nginx

- name: Deploy configuration from template
  template:
    src: app.conf.j2
    dest: /etc/app/app.conf
```

### Service Management

```yaml
- name: Start and enable nginx
  service:
    name: nginx
    state: started
    enabled: yes
```

## Running Playbooks

```bash
ansible-playbook playbook.yml
ansible-playbook -i inventory.ini playbook.yml
ansible-playbook playbook.yml --limit webservers
ansible-playbook playbook.yml --check --diff
ansible-playbook playbook.yml -e "env=production"
```

## Tags

```yaml
tasks:
  - name: Install dependencies
    apt:
      name: nginx
      state: present
    tags: [packages, setup]
      
  - name: Copy configuration
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    tags: [config]
```

```bash
ansible-playbook playbook.yml --tags "config"
ansible-playbook playbook.yml --skip-tags "restart"
```

---

# Part 5: Variables and Facts

## Understanding Variables

Variables in Ansible store values that can be reused throughout playbooks.

```yaml
vars:
  app_name: myapp
  http_port: 8080
  
tasks:
  - name: Create directory
    file:
      path: "/opt/{{ app_name }}"
      state: directory
```

## Variable Types and Sources

### Playbook Variables

```yaml
vars:
  app_name: myapp
  packages:
    - nginx
    - python3
  database:
    host: db.example.com
    port: 5432
```

### Variables from Files

```yaml
vars_files:
  - vars/common.yml
  - "vars/{{ env }}.yml"
```

### Registered Variables

```yaml
- name: Get current date
  command: date +%Y%m%d
  register: current_date
  
- name: Use date in filename
  file:
    path: "/backup/backup_{{ current_date.stdout }}.tar.gz"
    state: touch
```

### Extra Variables (Command Line)

```bash
ansible-playbook deploy.yml -e "version=1.2.3 env=production"
ansible-playbook deploy.yml -e "@vars/deploy.yml"
```

### set_fact

```yaml
- name: Calculate memory for app
  set_fact:
    app_memory: "{{ (ansible_memtotal_mb * 0.6) | int }}M"
```

## Facts

Facts are system information automatically gathered by Ansible.

```yaml
# Common Facts
ansible_distribution       # Ubuntu, CentOS, etc.
ansible_distribution_version
ansible_os_family          # Debian, RedHat, etc.
ansible_hostname
ansible_default_ipv4.address
ansible_memtotal_mb
ansible_processor_vcpus
```

## Magic Variables

```yaml
inventory_hostname      # Name as defined in inventory
group_names             # List of groups current host belongs to
groups                  # Dict of all groups and their hosts
hostvars                # Variables for all hosts
ansible_play_hosts      # All hosts in current play
```

---

# Part 6: Conditionals and Loops

## Conditionals with when

```yaml
- name: Install on Ubuntu only
  apt:
    name: nginx
    state: present
  when: ansible_distribution == "Ubuntu"

- name: Configure if web server
  template:
    src: web.conf.j2
    dest: /etc/app/web.conf
  when: "'webservers' in group_names"
```

## Complex Conditions

```yaml
# AND conditions (list format)
- name: Configure production web servers
  template:
    src: prod.conf.j2
    dest: /etc/app/config.conf
  when:
    - env == "production"
    - server_type == "web"

# OR conditions
- name: Install on Debian-based systems
  apt:
    name: nginx
    state: present
  when: ansible_distribution in ["Ubuntu", "Debian"]
```

## Testing Variable State

```yaml
- name: Use variable if defined
  debug:
    msg: "Port is {{ custom_port }}"
  when: custom_port is defined

- name: Check path exists
  stat:
    path: /opt/app
  register: app_dir
  
- name: Install if directory exists
  command: /opt/app/install.sh
  when: app_dir.stat.exists and app_dir.stat.isdir
```

## Loops

### Basic Loop

```yaml
- name: Install multiple packages
  apt:
    name: "{{ item }}"
    state: present
  loop:
    - nginx
    - php-fpm
    - mysql-client
```

### Loop over Dictionaries

```yaml
vars:
  users:
    - name: alice
      groups: developers
    - name: bob
      groups: admins

tasks:
  - name: Create users
    user:
      name: "{{ item.name }}"
      groups: "{{ item.groups }}"
    loop: "{{ users }}"
```

### until - Retry Loops

```yaml
- name: Wait for service to start
  uri:
    url: http://localhost:8080/health
    status_code: 200
  register: result
  until: result.status == 200
  retries: 30
  delay: 10
```

---

# Part 7: Handlers and Templates

## Understanding Handlers

Handlers are special tasks that run only when notified by other tasks. They typically run once at the end of a play.

```yaml
tasks:
  - name: Update nginx configuration
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: Restart nginx
    
handlers:
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

### Multiple Handlers

```yaml
tasks:
  - name: Update nginx config
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify:
      - Validate nginx config
      - Restart nginx
      
handlers:
  - name: Validate nginx config
    command: nginx -t
    
  - name: Restart nginx
    service:
      name: nginx
      state: restarted
```

## Jinja2 Templates

Templates are files processed by the Jinja2 templating engine.

**File: `templates/nginx.conf.j2`**

```jinja2
# Ansible managed - do not edit manually
user {{ nginx_user | default('www-data') }};
worker_processes {{ nginx_worker_processes | default('auto') }};

events {
    worker_connections {{ nginx_worker_connections | default(1024) }};
}

http {
    keepalive_timeout {{ nginx_keepalive_timeout | default(65) }};
    include /etc/nginx/sites-enabled/*;
}
```

## Template Syntax

### Variables

```jinja2
server_name {{ server_name }};
listen {{ http_port | default(80) }};
host {{ database.host }}:{{ database.port }};
```

### Conditionals

```jinja2
{% if ssl_enabled %}
listen 443 ssl;
ssl_certificate {{ ssl_certificate }};
{% else %}
listen 80;
{% endif %}
```

### Loops

```jinja2
{% for server in upstream_servers %}
server {{ server }};
{% endfor %}
```

### Filters

```jinja2
{{ hostname | upper }}
{{ items | join(', ') }}
{{ variable | default('fallback') }}
{{ data | to_json }}
```

---

# Part 8: Roles

## What are Roles?

Roles are a way to organize playbooks into reusable, self-contained units. They package tasks, handlers, variables, templates, and files into a standardized structure.

## Role Structure

```
roles/
└── nginx/
    ├── defaults/
    │   └── main.yml       # Default variables (lowest priority)
    ├── vars/
    │   └── main.yml       # Role variables (higher priority)
    ├── tasks/
    │   └── main.yml       # Main task file
    ├── handlers/
    │   └── main.yml       # Handler definitions
    ├── templates/
    │   └── nginx.conf.j2  # Jinja2 templates
    ├── files/
    │   └── index.html     # Static files
    ├── meta/
    │   └── main.yml       # Role metadata and dependencies
    └── README.md          # Documentation
```

## Creating Roles

```bash
ansible-galaxy init nginx
ansible-galaxy init --init-path=./roles nginx
```

## Using Roles

```yaml
- name: Configure web servers
  hosts: webservers
  become: yes
  
  roles:
    - nginx
    - php-fpm
    - role: mysql
      vars:
        mysql_port: 3306
```

## Role Dependencies

**File: `roles/wordpress/meta/main.yml`**

```yaml
---
dependencies:
  - role: nginx
  - role: php-fpm
    vars:
      php_version: "8.1"
  - role: mysql
```

## Ansible Galaxy

```bash
# Install role
ansible-galaxy install geerlingguy.nginx

# Install from requirements file
ansible-galaxy install -r requirements.yml
```

**File: `requirements.yml`**

```yaml
---
roles:
  - name: geerlingguy.nginx
    version: "3.1.0"
  - name: geerlingguy.mysql
    version: "4.3.0"
```

---

# Part 9: Ansible Vault

## What is Ansible Vault?

Ansible Vault encrypts sensitive data such as passwords, API keys, and certificates using AES-256 encryption.

## Creating Encrypted Files

```bash
ansible-vault create secrets.yml
ansible-vault create --vault-password-file .vault_pass secrets.yml
```

## Managing Encrypted Files

```bash
ansible-vault encrypt vars/production.yml
ansible-vault decrypt secrets.yml
ansible-vault view secrets.yml
ansible-vault edit secrets.yml
ansible-vault rekey secrets.yml
```

## Encrypt Single Variables

```bash
ansible-vault encrypt_string 'MySecretPassword' --name 'db_password'
```

Output:

```yaml
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          61626364656667...
```

## Using Encrypted Variables

```yaml
# group_vars/production/vault.yml (encrypted)
vault_db_password: ProductionPassword123!

# group_vars/production/vars.yml (plain)
db_password: "{{ vault_db_password }}"
```

## Managing Vault Passwords

```bash
# Prompt at runtime
ansible-playbook playbook.yml --ask-vault-pass

# Password file
ansible-playbook playbook.yml --vault-password-file .vault_pass

# Configure in ansible.cfg
# vault_password_file = .vault_pass
```

## Best Practices

1. **Prefix vault variables** with `vault_`
2. **Use no_log** for sensitive tasks
3. **Never commit** unencrypted secrets
4. **Use pre-commit hooks** to prevent accidents

---

# Part 10: Advanced Topics

## Error Handling

### ignore_errors

```yaml
- name: This might fail
  command: /opt/app/risky-command.sh
  ignore_errors: yes
```

### failed_when

```yaml
- name: Check application status
  command: /opt/app/healthcheck.sh
  register: health
  failed_when: "'CRITICAL' in health.stdout"
```

### changed_when

```yaml
- name: Run idempotent script
  command: /opt/app/configure.sh
  changed_when: false
```

## Blocks

```yaml
- name: Deploy with error handling
  block:
    - name: Pull latest code
      git:
        repo: https://github.com/company/app.git
        dest: /opt/app
        
    - name: Run migrations
      command: /opt/app/migrate.sh
      
  rescue:
    - name: Rollback to previous version
      git:
        repo: https://github.com/company/app.git
        dest: /opt/app
        version: "{{ previous_version }}"
        
  always:
    - name: Clean up temp files
      file:
        path: /tmp/deploy
        state: absent
```

## Asynchronous Actions

```yaml
- name: Start background task
  command: /opt/scripts/background-task.sh
  async: 3600
  poll: 0
  register: background_task

- name: Check background task status
  async_status:
    jid: "{{ background_task.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 60
  delay: 10
```

## Strategies

```yaml
# Serial execution (rolling deployment)
- name: Rolling deployment
  hosts: webservers
  serial: 2  # 2 hosts at a time
  
# Free strategy
- name: Fast parallel execution
  hosts: all
  strategy: free
```

## Performance Optimization

```ini
# ansible.cfg
[defaults]
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /tmp/ansible_facts
forks = 50

[ssh_connection]
pipelining = True
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Deploy with Ansible

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Ansible
        run: pip install ansible
      - name: Setup SSH key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
      - name: Run Ansible playbook
        run: ansible-playbook -i inventory/production playbooks/deploy.yml
```

---

## 🎉 Congratulations!

You've completed the Ansible Zero to Hero course! You now have the knowledge to:

- ✅ Set up and configure Ansible
- ✅ Write playbooks and use modules
- ✅ Work with variables, facts, and templates
- ✅ Create reusable roles
- ✅ Secure secrets with Vault
- ✅ Handle errors gracefully
- ✅ Optimize performance
- ✅ Integrate with CI/CD pipelines

---

## 📚 Additional Resources

- [Official Ansible Documentation](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Ansible GitHub Repository](https://github.com/ansible/ansible)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

---

**Happy Automating! 🎉**

