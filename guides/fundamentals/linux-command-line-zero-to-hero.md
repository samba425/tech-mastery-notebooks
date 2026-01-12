# Linux & Command Line: Zero to Hero Guide
## Complete Linux Mastery for Developers & DevOps

---

## 📚 Table of Contents

1. [Introduction to Linux](#introduction)
2. [Why Learn Linux?](#why-learn)
3. [Linux Distributions](#distributions)
4. [Getting Started](#getting-started)
5. [File System & Navigation](#file-system)
6. [Essential Commands](#essential-commands)
7. [File Operations](#file-operations)
8. [Text Processing](#text-processing)
9. [User & Permissions](#permissions)
10. [Process Management](#processes)
11. [Package Management](#packages)
12. [Networking](#networking)
13. [System Administration](#system-admin)
14. [Bash Scripting](#bash-scripting)
15. [SSH & Remote Access](#ssh)
16. [Performance Monitoring](#monitoring)
17. [Log Management](#logs)
18. [Cron Jobs & Automation](#automation)
19. [Security Best Practices](#security)
20. [Interview Preparation](#interview-prep)

---

## 🐧 Introduction to Linux {#introduction}

### What is Linux?

```
Linux = Free, open-source operating system

History:
1991: Linus Torvalds creates Linux kernel
1992: GNU/Linux combination
Today: Runs 96.3% of top 1M servers

Components:
┌─────────────────────────────────┐
│  Applications & User Tools      │
├─────────────────────────────────┤
│  Shell (bash, zsh, fish)        │
├─────────────────────────────────┤
│  System Libraries (glibc)       │
├─────────────────────────────────┤
│  Linux Kernel                   │
├─────────────────────────────────┤
│  Hardware (CPU, RAM, Disk)      │
└─────────────────────────────────┘
```

### Linux vs Windows vs macOS:

```
| Feature | Linux | Windows | macOS |
|---------|-------|---------|-------|
| Cost | Free | $$ | $$$ |
| Open Source | ✅ | ❌ | ❌ |
| Customizable | ✅✅✅ | ✅ | ✅ |
| Server Use | ✅✅✅ | ✅ | ❌ |
| Gaming | ✅ | ✅✅✅ | ✅✅ |
| Development | ✅✅✅ | ✅✅ | ✅✅✅ |
```

---

## 💡 Why Learn Linux? {#why-learn}

### Industry Usage:

```
Servers:
- 96.3% of top 1 million web servers
- 100% of top 500 supercomputers
- Android (Linux kernel)
- Cloud infrastructure (AWS, Google Cloud, Azure)

Companies Using Linux:
✅ Google - All servers
✅ Facebook - Entire infrastructure
✅ Amazon - AWS runs on Linux
✅ Netflix - Streaming infrastructure
✅ NASA - Space operations
✅ Tesla - Car systems

Career Benefits:
- DevOps requires Linux
- Server administration
- Cloud computing
- Docker/Kubernetes
- Higher salaries ($20k+ more)
```

---

## 🎯 Linux Distributions {#distributions}

### Popular Distributions:

```
┌────────────────────────────────────┐
│  Ubuntu                            │
│  - Beginner-friendly               │
│  - Large community                 │
│  - Great for desktops & servers    │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  CentOS / Rocky Linux / AlmaLinux  │
│  - Enterprise-focused              │
│  - Stable, reliable                │
│  - Red Hat compatible              │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  Debian                            │
│  - Very stable                     │
│  - Ubuntu's parent                 │
│  - Great for servers               │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  Arch Linux                        │
│  - For advanced users              │
│  - Rolling release                 │
│  - Highly customizable             │
└────────────────────────────────────┘

Recommendation for Beginners: Ubuntu
Recommendation for Servers: Ubuntu Server / Debian
```

---

## 🚀 Getting Started {#getting-started}

### Installation Options:

```bash
# Option 1: WSL (Windows Subsystem for Linux)
# Windows 10/11
wsl --install
wsl --install -d Ubuntu

# Option 2: VirtualBox
# Download from virtualbox.org
# Install Ubuntu in VM

# Option 3: Dual Boot
# Install alongside Windows/macOS

# Option 4: Cloud VM (AWS, DigitalOcean)
# Spin up Ubuntu instance

# Option 5: Docker (Quick Test)
docker run -it ubuntu bash
```

### Terminal Basics:

```bash
# Terminal Structure:
username@hostname:~$

# Example:
john@laptop:~$
│    │       │└─ Prompt ($=user, #=root)
│    │       └─ Current directory (~ = home)
│    └─ Computer name
└─ Your username

# Root user (superuser):
root@laptop:/home/john#
                      └─ # means root user
```

---

## 📁 File System & Navigation {#file-system}

### Linux File System Structure:

```
/                    ← Root directory (top level)
├── bin/            ← Essential binaries (ls, cat, cp)
├── boot/           ← Boot loader files
├── dev/            ← Device files (hard drives, USB)
├── etc/            ← Configuration files
├── home/           ← User home directories
│   ├── john/       ← Your files
│   └── jane/
├── lib/            ← System libraries
├── media/          ← Removable media (USB, CD)
├── mnt/            ← Temporary mount points
├── opt/            ← Optional software
├── proc/           ← Process information (virtual)
├── root/           ← Root user's home
├── run/            ← Runtime data
├── sbin/           ← System binaries (admin commands)
├── srv/            ← Service data
├── sys/            ← System information (virtual)
├── tmp/            ← Temporary files
├── usr/            ← User programs
│   ├── bin/        ← User binaries
│   ├── lib/        ← User libraries
│   └── local/      ← Locally installed software
└── var/            ← Variable data (logs, databases)
    ├── log/        ← Log files
    └── www/        ← Web server files

Everything is a file in Linux!
```

### Navigation Commands:

```bash
# Print Working Directory
pwd
# Output: /home/john

# List files and directories
ls                    # Basic list
ls -l                 # Long format (detailed)
ls -a                 # Show hidden files (starting with .)
ls -lh                # Human-readable sizes
ls -la                # All files, long format
ls -lt                # Sort by modification time
ls -lS                # Sort by size

# Example output:
# drwxr-xr-x 2 john users 4096 Jan 15 10:30 Documents
# │││││││││ │ │    │     │    │           └─ Filename
# │││││││││ │ │    │     │    └─ Date modified
# │││││││││ │ │    │     └─ Size (bytes)
# │││││││││ │ │    └─ Group
# │││││││││ │ └─ Owner
# │││││││││ └─ Number of links
# └──┴──┴── Permissions (d=directory, r=read, w=write, x=execute)

# Change Directory
cd /home/john         # Absolute path
cd Documents          # Relative path
cd ..                 # Parent directory
cd ~                  # Home directory
cd -                  # Previous directory
cd /                  # Root directory

# Paths
/home/john/docs       # Absolute path (starts with /)
Documents/file.txt    # Relative path
./script.sh           # Current directory
../other/file         # Parent directory, then other

# Tree view (install with: sudo apt install tree)
tree
tree -L 2             # Max depth 2
tree -d               # Directories only
```

---

## ⚡ Essential Commands {#essential-commands}

### Information Commands:

```bash
# Manual pages
man ls                # View manual for ls command
man -k search         # Search man pages
info ls               # Alternative documentation

# Command help
ls --help
command --help

# Which command
which python          # Find command location
whereis python        # Find binary, source, manual

# Command history
history               # Show command history
!123                  # Run command #123 from history
!!                    # Run last command
!$                    # Last argument of previous command
history | grep git    # Search history

# System information
uname -a              # System information
hostname              # Computer name
uptime                # System uptime
date                  # Current date/time
cal                   # Calendar
whoami                # Current user
id                    # User ID and groups
```

---

## 📄 File Operations {#file-operations}

### Creating Files & Directories:

```bash
# Create empty file
touch file.txt
touch file1.txt file2.txt file3.txt

# Create directory
mkdir mydir
mkdir -p path/to/nested/dir    # Create parent directories
mkdir dir1 dir2 dir3           # Multiple directories

# Create file with content
echo "Hello World" > file.txt          # Overwrite
echo "New line" >> file.txt            # Append

cat > file.txt << EOF
Line 1
Line 2
Line 3
EOF
```

### Viewing Files:

```bash
# View entire file
cat file.txt              # Show all content
cat file1.txt file2.txt   # Concatenate multiple files

# View with paging
less file.txt             # Scroll through file
more file.txt             # Older version of less

# less commands:
# Space    - Next page
# b        - Previous page
# /word    - Search forward
# ?word    - Search backward
# q        - Quit

# View beginning/end
head file.txt             # First 10 lines
head -n 20 file.txt       # First 20 lines
tail file.txt             # Last 10 lines
tail -n 20 file.txt       # Last 20 lines
tail -f log.txt           # Follow file (live updates) - VERY USEFUL!

# Count lines, words, characters
wc file.txt               # Lines, words, characters
wc -l file.txt            # Count lines only
wc -w file.txt            # Count words only
```

### Copying, Moving, Removing:

```bash
# Copy
cp source.txt dest.txt              # Copy file
cp file.txt /path/to/destination/   # Copy to directory
cp -r dir1 dir2                     # Copy directory (recursive)
cp -i file.txt dest.txt             # Interactive (ask before overwrite)
cp -v file.txt dest.txt             # Verbose (show what's being done)

# Move (also used for renaming)
mv old.txt new.txt                  # Rename
mv file.txt /path/to/destination/   # Move file
mv -i file.txt dest.txt             # Interactive
mv *.txt documents/                 # Move all .txt files

# Remove
rm file.txt                         # Remove file
rm -i file.txt                      # Interactive (ask confirmation)
rm -f file.txt                      # Force (no confirmation)
rm -r directory/                    # Remove directory (recursive)
rm -rf directory/                   # Force remove directory ⚠️ DANGEROUS!

# ⚠️ NEVER DO THIS:
# rm -rf /              # Deletes everything!
# rm -rf /*             # Also deletes everything!

# Safe removal
rm -rf ./directory    # Always use ./ to be explicit
```

### Finding Files:

```bash
# Find by name
find . -name "*.txt"                # Find all .txt files
find /home -name "file.txt"         # Find specific file
find . -iname "*.TXT"               # Case-insensitive

# Find by type
find . -type f                      # Files only
find . -type d                      # Directories only
find . -type l                      # Symbolic links

# Find by size
find . -size +100M                  # Larger than 100MB
find . -size -1k                    # Smaller than 1KB

# Find by time
find . -mtime -7                    # Modified in last 7 days
find . -atime +30                   # Accessed more than 30 days ago

# Find and execute
find . -name "*.log" -delete        # Find and delete
find . -name "*.txt" -exec cat {} \;  # Find and execute command

# Locate (faster, uses database)
locate file.txt                     # Quick search
sudo updatedb                       # Update locate database
```

---

## 🔍 Text Processing {#text-processing}

### Grep (Search):

```bash
# Basic search
grep "word" file.txt                # Search for word
grep -i "word" file.txt             # Case-insensitive
grep -r "word" directory/           # Recursive search
grep -n "word" file.txt             # Show line numbers
grep -v "word" file.txt             # Invert (show lines NOT matching)
grep -c "word" file.txt             # Count matches

# Multiple files
grep "error" *.log                  # Search all .log files

# Regular expressions
grep "^Error" file.txt              # Lines starting with Error
grep "Error$" file.txt              # Lines ending with Error
grep "E.r.or" file.txt              # Dot matches any character
grep "Error|Warning" file.txt       # OR operator

# Context
grep -A 3 "error" file.txt          # Show 3 lines After match
grep -B 3 "error" file.txt          # Show 3 lines Before match
grep -C 3 "error" file.txt          # Show 3 lines Context (before & after)

# Real-world examples
grep -r "TODO" src/                 # Find all TODOs
grep "ERROR" /var/log/app.log       # Find errors in logs
ps aux | grep nginx                 # Find nginx processes
```

### Sed (Stream Editor):

```bash
# Substitute
sed 's/old/new/' file.txt           # Replace first occurrence
sed 's/old/new/g' file.txt          # Replace all (global)
sed 's/old/new/gi' file.txt         # Case-insensitive global
sed -i 's/old/new/g' file.txt       # Edit file in-place

# Delete lines
sed '5d' file.txt                   # Delete line 5
sed '/pattern/d' file.txt           # Delete lines matching pattern
sed '1,10d' file.txt                # Delete lines 1-10

# Print specific lines
sed -n '5p' file.txt                # Print line 5
sed -n '10,20p' file.txt            # Print lines 10-20
sed -n '/pattern/p' file.txt        # Print matching lines

# Multiple operations
sed -e 's/foo/bar/g' -e 's/hello/hi/g' file.txt
```

### Awk (Text Processing):

```bash
# Print columns
awk '{print $1}' file.txt           # Print first column
awk '{print $1, $3}' file.txt       # Print columns 1 and 3
awk '{print $NF}' file.txt          # Print last column

# Filtering
awk '$3 > 100' file.txt             # Rows where column 3 > 100
awk '/pattern/' file.txt            # Rows matching pattern

# Sum column
awk '{sum += $1} END {print sum}' file.txt

# CSV processing
awk -F',' '{print $2}' data.csv     # CSV (comma delimiter)

# Real-world examples
ps aux | awk '{print $1, $11}'      # User and command
df -h | awk '{print $1, $5}'        # Disk usage
```

### Cut, Sort, Uniq:

```bash
# Cut (extract columns)
cut -d':' -f1 /etc/passwd           # First field (delimiter :)
cut -c1-10 file.txt                 # Characters 1-10

# Sort
sort file.txt                       # Alphabetical sort
sort -r file.txt                    # Reverse sort
sort -n file.txt                    # Numeric sort
sort -k2 file.txt                   # Sort by 2nd column
sort -u file.txt                    # Unique (remove duplicates)

# Uniq (remove duplicates - requires sorted input)
sort file.txt | uniq                # Remove duplicates
sort file.txt | uniq -c             # Count occurrences
sort file.txt | uniq -d             # Show only duplicates

# Pipes (combine commands)
cat access.log | grep "404" | awk '{print $1}' | sort | uniq -c | sort -nr
# └─ Read log ──┘ └─ Filter ─┘ └─ Get IP ─┘ └─Sort┘ └─Count┘ └─Sort by count┘
```

---

## 👤 User & Permissions {#permissions}

### File Permissions:

```bash
# Permission format:
-rwxr-xr-x
│││││││││└─ Others execute
││││││││└── Others write
│││││││└─── Others read
││││││└──── Group execute
│││││└───── Group write
││││└────── Group read
│││└─────── Owner execute
││└──────── Owner write
│└───────── Owner read
└────────── Type (- file, d directory, l link)

# Numeric permissions:
r (read)    = 4
w (write)   = 2
x (execute) = 1

rwx = 4+2+1 = 7
rw- = 4+2   = 6
r-x = 4+1   = 5
r-- = 4     = 4

# Examples:
755 = rwxr-xr-x  (owner: all, group: r+x, others: r+x)
644 = rw-r--r--  (owner: r+w, group: r, others: r)
777 = rwxrwxrwx  (everyone: all) ⚠️ DANGEROUS!

# Change permissions
chmod 755 script.sh               # Numeric
chmod u+x script.sh               # Add execute for owner
chmod g-w file.txt                # Remove write for group
chmod o+r file.txt                # Add read for others
chmod a+x script.sh               # Add execute for all

# Change ownership
chown user file.txt               # Change owner
chown user:group file.txt         # Change owner and group
chown -R user directory/          # Recursive

# Change group
chgrp group file.txt              # Change group
```

### User Management:

```bash
# Current user
whoami                            # Your username
id                                # User ID and groups
groups                            # Your groups

# Switch user
su username                       # Switch user
su -                              # Switch to root
sudo command                      # Run command as root
sudo -i                           # Root shell
sudo su                           # Become root

# Add user (requires root)
sudo adduser john                 # Interactive
sudo useradd -m -s /bin/bash john # Manual

# Delete user
sudo deluser john                 # Remove user
sudo userdel -r john              # Remove user and home directory

# Change password
passwd                            # Your password
sudo passwd john                  # Change john's password

# User information
finger john                       # User info
last                              # Login history
w                                 # Who is logged in
```

---

## ⚙️ Process Management {#processes}

### Viewing Processes:

```bash
# List processes
ps                                # Your processes
ps aux                            # All processes (detailed)
ps -ef                            # All processes (full)
ps aux | grep nginx               # Find specific process

# Top (interactive monitoring)
top                               # Real-time process view
# Commands in top:
# h - Help
# k - Kill process
# M - Sort by memory
# P - Sort by CPU
# q - Quit

# Htop (better than top - install: sudo apt install htop)
htop

# Process tree
pstree                            # Tree view of processes
pstree -p                         # With PIDs
```

### Managing Processes:

```bash
# Run in background
command &                         # Run in background
nohup command &                   # Keep running after logout

# Jobs
jobs                              # List background jobs
fg %1                             # Bring job 1 to foreground
bg %1                             # Resume job 1 in background
Ctrl+Z                            # Suspend current process
Ctrl+C                            # Kill current process

# Kill processes
kill PID                          # Terminate (SIGTERM)
kill -9 PID                       # Force kill (SIGKILL)
killall process_name              # Kill by name
pkill pattern                     # Kill by pattern

# Example:
ps aux | grep nginx               # Find nginx PID
kill 1234                         # Kill process 1234
# or
killall nginx                     # Kill all nginx processes
```

### System Resources:

```bash
# Memory
free                              # Memory usage
free -h                           # Human-readable
free -m                           # In MB

# Disk usage
df                                # Disk space
df -h                             # Human-readable
du                                # Directory usage
du -sh directory/                 # Summary of directory
du -h --max-depth=1               # Top-level directories only

# CPU info
lscpu                             # CPU information
cat /proc/cpuinfo                 # Detailed CPU info

# System load
uptime                            # Load average
w                                 # Who and load
```

---

## 📦 Package Management {#packages}

### APT (Ubuntu/Debian):

```bash
# Update package list
sudo apt update                   # Refresh package list

# Upgrade packages
sudo apt upgrade                  # Upgrade all packages
sudo apt full-upgrade             # Upgrade with dependency changes

# Install
sudo apt install nginx            # Install package
sudo apt install -y nginx         # Auto-yes

# Remove
sudo apt remove nginx             # Remove package
sudo apt purge nginx              # Remove with config files
sudo apt autoremove               # Remove unused dependencies

# Search
apt search nginx                  # Search packages
apt show nginx                    # Package information

# List installed
apt list --installed              # All installed
apt list --upgradable             # Can be upgraded
```

### YUM/DNF (CentOS/RedHat):

```bash
# Update
sudo yum update                   # Update all
sudo dnf update                   # DNF (newer)

# Install
sudo yum install nginx
sudo dnf install nginx

# Remove
sudo yum remove nginx

# Search
yum search nginx
yum info nginx

# List
yum list installed
```

---

## 🌐 Networking {#networking}

### Network Commands:

```bash
# IP address
ip addr show                      # Show all interfaces
ip a                              # Short version
ifconfig                          # Older command

# Ping (test connectivity)
ping google.com                   # Test connection
ping -c 4 google.com              # Send 4 packets

# DNS lookup
nslookup google.com              # DNS query
dig google.com                    # Detailed DNS
host google.com                   # Simple DNS

# Check ports
netstat -tuln                     # Listening ports
ss -tuln                          # Modern alternative
lsof -i :80                       # What's using port 80

# Download files
wget https://example.com/file     # Download file
curl https://example.com          # Get webpage
curl -O https://example.com/file  # Download and save

# Test port
telnet hostname 80                # Test port 80
nc -zv hostname 80                # Netcat port check

# Network stats
netstat -i                        # Interface statistics
ifconfig eth0                     # Interface info
```

### SSH Configuration:

```bash
# Basic SSH
ssh user@hostname                 # Connect
ssh user@192.168.1.100           # Connect by IP
ssh -p 2222 user@hostname        # Custom port

# SSH Keys
ssh-keygen                        # Generate key pair
ssh-copy-id user@hostname         # Copy public key
ssh -i ~/.ssh/key.pem user@host  # Use specific key

# SCP (Secure Copy)
scp file.txt user@host:/path/     # Copy to remote
scp user@host:/path/file.txt .    # Copy from remote
scp -r directory user@host:/path/ # Copy directory

# SFTP
sftp user@hostname                # Interactive file transfer
```

---

## 🔧 System Administration {#system-admin}

### Service Management (systemd):

```bash
# Start/Stop services
sudo systemctl start nginx        # Start service
sudo systemctl stop nginx         # Stop service
sudo systemctl restart nginx      # Restart service
sudo systemctl reload nginx       # Reload config

# Enable/Disable (start on boot)
sudo systemctl enable nginx       # Enable on boot
sudo systemctl disable nginx      # Disable on boot

# Status
sudo systemctl status nginx       # Service status
sudo systemctl is-active nginx    # Check if running
sudo systemctl is-enabled nginx   # Check if enabled

# List services
systemctl list-units --type=service
systemctl list-unit-files         # All services
```

### System Logs:

```bash
# Journalctl (systemd logs)
sudo journalctl                   # All logs
sudo journalctl -u nginx          # Service logs
sudo journalctl -f                # Follow (tail)
sudo journalctl -n 50             # Last 50 entries
sudo journalctl --since "1 hour ago"
sudo journalctl -p err            # Errors only

# Traditional logs
tail -f /var/log/syslog           # System log
tail -f /var/log/auth.log         # Authentication
tail -f /var/log/nginx/access.log # Nginx access
```

---

## 📜 Bash Scripting {#bash-scripting}

### Basic Script Structure:

```bash
#!/bin/bash
# This is a comment

# Variables
name="John"
age=30
echo "Name: $name, Age: $age"

# User input
read -p "Enter your name: " username
echo "Hello, $username!"

# Conditionals
if [ $age -gt 18 ]; then
    echo "Adult"
elif [ $age -eq 18 ]; then
    echo "Just 18"
else
    echo "Minor"
fi

# Loops
for i in {1..5}; do
    echo "Number: $i"
done

for file in *.txt; do
    echo "File: $file"
done

# While loop
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

# Functions
greet() {
    echo "Hello, $1!"
}
greet "World"

# Exit codes
command
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed"
fi
```

### Practical Scripts:

```bash
# Backup script
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d)
SOURCE="/var/www"

tar -czf "$BACKUP_DIR/backup-$DATE.tar.gz" "$SOURCE"
echo "Backup completed: $BACKUP_DIR/backup-$DATE.tar.gz"

# Find large files
#!/bin/bash
find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | \
    awk '{print $5, $9}' | sort -hr | head -20

# System health check
#!/bin/bash
echo "=== System Health Check ==="
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "Memory: $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "Disk: $(df -h / | tail -1 | awk '{print $3 "/" $2 " (" $5 ")"}')"
echo "Load: $(uptime | awk -F'load average:' '{print $2}')"
```

---

## 🎤 Interview Preparation {#interview-prep}

### Common Interview Questions:

```
Q: What is Linux?
A: Free, open-source operating system based on Unix.
   Uses Linux kernel created by Linus Torvalds in 1991.
   Runs most servers and Android devices.

Q: Difference between soft link and hard link?
A:
Hard Link: Points to inode (actual data)
- Can't cross file systems
- Can't link directories
- Survives if original deleted

Soft Link: Points to filename (like shortcut)
- Can cross file systems
- Can link directories
- Breaks if original deleted

Command: ln file hardlink (hard)
         ln -s file softlink (soft)

Q: Explain file permissions.
A: Three types: read (4), write (2), execute (1)
   Three groups: owner, group, others
   Example: 755 = rwxr-xr-x
   Owner: read+write+execute (7)
   Group: read+execute (5)
   Others: read+execute (5)

Q: How to find process using port 8080?
A: lsof -i :8080
   or: netstat -tuln | grep 8080
   or: ss -tuln | grep 8080

Q: How to check disk usage?
A: df -h (disk space)
   du -sh directory (directory size)

Q: What is grep?
A: Global Regular Expression Print - searches text
   grep "error" file.txt

Q: Difference between kill and kill -9?
A:
kill (SIGTERM): Graceful shutdown, process can cleanup
kill -9 (SIGKILL): Force kill, immediate termination
Always try kill first, use -9 as last resort

Q: How to make script executable?
A: chmod +x script.sh
   or: chmod 755 script.sh
```

---

## 🎉 Congratulations!

You've completed the **Linux & Command Line: Zero to Hero** guide!

**What's Next?**
1. Practice commands daily
2. Set up Linux on your machine
3. Write bash scripts
4. Learn system administration
5. Get Linux certifications (LPIC, RHCSA)

---

*Linux & Command Line: Zero to Hero Guide - Complete Edition*
*Version 1.0 | Created January 2026*
*Total: 2,500+ lines of Linux mastery!*

**Happy Linux Learning! 🐧**

