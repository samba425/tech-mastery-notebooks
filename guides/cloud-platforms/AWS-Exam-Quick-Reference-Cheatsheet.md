# AWS Certification Quick Reference Cheat Sheet

## 🎯 Use This For: Last 24 Hours Before Exam

*Print this out or keep it open for final review*

---

## ⚡ Super Quick Service Reference

### Compute
| Service | What | When | Cost |
|---------|------|------|------|
| **EC2** | Virtual servers | Need full control | Pay per hour |
| **Lambda** | Run code serverless | Event-driven, <15min | Pay per execution |
| **ECS/EKS** | Containers | Microservices | Pay for compute |
| **Fargate** | Serverless containers | No server management | Pay for vCPU/memory |
| **Elastic Beanstalk** | PaaS | Just deploy app | Pay for resources |
| **Lightsail** | Simple VPS | Simple websites | Fixed monthly |

### Storage
| Service | What | When | Durability/Availability |
|---------|------|------|------------------------|
| **S3 Standard** | Object storage | Frequent access | 11 9s / 99.99% |
| **S3 Standard-IA** | Infrequent access | Monthly access | 11 9s / 99.9% |
| **S3 One Zone-IA** | Single AZ | Non-critical | 11 9s / 99.5% |
| **S3 Glacier Instant** | Archive + instant | Quarterly access | 11 9s / 99.9% |
| **S3 Glacier Flexible** | Archive | Rarely, hours OK | 11 9s / 99.99% |
| **S3 Glacier Deep Archive** | Long-term archive | 7+ years | 11 9s / 99.99% |
| **EBS** | Block storage | EC2 hard drive | Replicates in AZ |
| **EFS** | File storage | Shared across EC2 | Multi-AZ |
| **Instance Store** | Ephemeral | Temporary/cache | Lost on stop |

### Database
| Service | Type | Best For |
|---------|------|----------|
| **RDS** | Relational | MySQL, PostgreSQL, SQL Server, Oracle |
| **Aurora** | Relational++ | 5x MySQL performance, auto-scaling |
| **DynamoDB** | NoSQL | Key-value, millisecond latency |
| **ElastiCache** | In-memory | Redis (complex) / Memcached (simple) |
| **Redshift** | Data warehouse | Analytics, OLAP, petabyte-scale |
| **DocumentDB** | Document | MongoDB compatible |
| **Neptune** | Graph | Social networks, recommendations |
| **QLDB** | Ledger | Immutable transaction log |
| **Timestream** | Time-series | IoT, DevOps metrics |

### Networking
| Service | Purpose | Use Case |
|---------|---------|----------|
| **VPC** | Private network | Your isolated network |
| **Route 53** | DNS | Domain names |
| **CloudFront** | CDN | Global content delivery |
| **ELB (ALB)** | Layer 7 LB | HTTP/HTTPS, path routing |
| **ELB (NLB)** | Layer 4 LB | TCP/UDP, high performance |
| **API Gateway** | API management | Create/publish APIs |
| **Direct Connect** | Dedicated link | On-prem to AWS (private) |
| **VPN** | Encrypted tunnel | On-prem to AWS (internet) |
| **Global Accelerator** | TCP/UDP accelerator | Gaming, IoT, low latency |
| **Transit Gateway** | Network hub | Connect multiple VPCs |

### Security
| Service | Purpose |
|---------|---------|
| **IAM** | Users, groups, roles, policies |
| **KMS** | Encryption key management |
| **Secrets Manager** | Store/rotate secrets |
| **WAF** | Web application firewall (Layer 7) |
| **Shield** | DDoS protection (Standard=free) |
| **GuardDuty** | Threat detection (ML-based) |
| **Macie** | Discover PII in S3 |
| **Inspector** | EC2 vulnerability scanning |
| **CloudTrail** | API audit logging |
| **Config** | Resource compliance |
| **Security Hub** | Central security view |
| **Certificate Manager** | SSL/TLS certificates (free) |

### Management
| Service | Purpose |
|---------|---------|
| **CloudWatch** | Monitoring, metrics, logs |
| **CloudFormation** | Infrastructure as Code (IaC) |
| **Trusted Advisor** | Best practice recommendations |
| **Systems Manager** | Operational insights |
| **Auto Scaling** | Automatic capacity adjustment |
| **Elastic Beanstalk** | PaaS application deployment |
| **OpsWorks** | Chef/Puppet managed |

### Application Integration
| Service | Pattern |
|---------|---------|
| **SQS** | Queue (decouple, asynchronous) |
| **SNS** | Pub/Sub (notifications) |
| **EventBridge** | Event bus (serverless events) |
| **Step Functions** | Workflow orchestration |
| **AppSync** | GraphQL API |

---

## 🔐 IAM Quick Reference

### IAM Components:
```
User     → Person or application
Group    → Collection of users
Role     → For AWS services (EC2, Lambda)
Policy   → JSON document with permissions
```

### Policy Evaluation:
```
1. Explicit DENY → Deny (wins always)
2. Explicit ALLOW → Allow
3. Default → Deny (implicit)
```

### Best Practices:
✅ Root account: MFA + lock away  
✅ Individual IAM users (no sharing)  
✅ Use groups for permissions  
✅ Use roles for EC2/Lambda  
✅ Least privilege principle  
✅ Rotate credentials (90 days)  
✅ Never store keys in code  

---

## 🏛️ VPC Quick Reference

### Components:
```
VPC               → Your private network (10.0.0.0/16)
Subnet            → Segment of VPC (AZ-specific)
Internet Gateway  → Connect to internet
NAT Gateway       → Private subnet internet access
Route Table       → Direct traffic
Security Group    → Instance firewall (stateful)
NACL              → Subnet firewall (stateless)
VPC Peering       → Connect two VPCs
VPC Endpoint      → Private connection to AWS services
```

### Security Group vs NACL:
| Feature | Security Group | NACL |
|---------|----------------|------|
| **Level** | Instance (ENI) | Subnet |
| **State** | Stateful | Stateless |
| **Rules** | Allow only | Allow + Deny |
| **Default** | Deny inbound | Allow all |

### 3-Tier VPC Pattern:
```
Public Subnet    → ELB, NAT Gateway
Private Subnet   → EC2 app servers
Private Subnet   → RDS database
```

---

## 💾 Storage Decision Tree

```
Need object storage?
├─ Frequent access → S3 Standard
├─ Monthly access → S3 Standard-IA
├─ Unknown pattern → S3 Intelligent-Tiering
├─ Archive (hours) → S3 Glacier Flexible
└─ Archive (years) → S3 Glacier Deep Archive

Need block storage?
├─ Persistent → EBS (gp3, io2)
└─ Temporary → Instance Store

Need file storage?
├─ Linux shared → EFS
└─ Windows shared → FSx for Windows
```

---

## 🗄️ Database Decision Tree

```
Structured data + SQL?
├─ Yes → Relational
│   ├─ Need Aurora perf? → Aurora
│   ├─ Standard workload? → RDS
│   └─ Analytics/DW? → Redshift
└─ No → NoSQL
    ├─ Key-value, fast? → DynamoDB
    ├─ In-memory cache? → ElastiCache
    ├─ Document store? → DocumentDB
    └─ Graph data? → Neptune
```

---

## 💰 EC2 Pricing Models

| Model | Commitment | Discount | Use Case |
|-------|------------|----------|----------|
| **On-Demand** | None | 0% | Unpredictable, dev/test |
| **Reserved** | 1-3 years | 75% | Steady state (databases) |
| **Spot** | None | 90% | Batch jobs, flexible |
| **Savings Plan** | 1-3 years | 72% | Flexible across types |
| **Dedicated Host** | Hourly | 0% | Licensing requirements |

**Exam Tip:**
- "Cost-effective + steady" = **Reserved**
- "Cost-effective + flexible" = **Spot**
- "Unpredictable" = **On-Demand**

---

## 📊 RDS High Availability

### Multi-AZ:
```
Purpose:  High availability
Replication:  Synchronous
Failover:  Automatic (1-2 min)
Standby:  Not readable
Region:  Same
Use:  Production databases
```

### Read Replicas:
```
Purpose:  Read scaling
Replication:  Asynchronous
Failover:  Manual promotion
Replicas:  Readable (up to 15)
Region:  Can be cross-region
Use:  Read-heavy workloads
```

**Exam Tip:**
- "Automatic failover" = **Multi-AZ**
- "Scale reads" = **Read Replicas**
- Can have both together!

---

## 🔒 Encryption Quick Reference

### At Rest:
```
S3:
- SSE-S3 (AWS manages keys)
- SSE-KMS (AWS KMS, audit trail)
- SSE-C (Customer provides keys)
- Client-side (Encrypt before upload)

EBS:
- Enable at creation (KMS)
- Can copy unencrypted → encrypted

RDS:
- Enable at creation (can't add later)
- Encrypts DB + backups + snapshots
```

### In Transit:
```
✅ HTTPS/TLS for web traffic
✅ SSL for RDS connections
✅ VPN for on-premises
✅ CloudFront HTTPS
```

---

## ⚡ Auto Scaling Policies

| Policy | When to Use |
|--------|-------------|
| **Target Tracking** | Maintain metric (e.g., CPU 50%) |
| **Step Scaling** | Different responses to thresholds |
| **Simple Scaling** | Single scaling action + cooldown |
| **Scheduled** | Predictable traffic patterns |
| **Predictive** | ML-based, scale ahead of time |

---

## 🌐 High Availability Patterns

### Multi-AZ (Same Region):
```
✅ RDS Multi-AZ
✅ ELB (inherently Multi-AZ)
✅ S3 (replicates across AZs)
✅ DynamoDB (replicates across AZs)
✅ EFS (spans multiple AZs)

Purpose: Protect against AZ failure
RTO: Minutes
```

### Multi-Region:
```
✅ S3 Cross-Region Replication
✅ RDS Read Replicas (cross-region)
✅ DynamoDB Global Tables
✅ CloudFront (global edge)

Purpose: Disaster recovery, low latency
RTO: Depends on DR strategy
```

---

## 🔄 Disaster Recovery Strategies

| Strategy | RTO | RPO | Cost |
|----------|-----|-----|------|
| **Backup & Restore** | Hours | Hours | $ |
| **Pilot Light** | 10-30 min | Minutes | $$ |
| **Warm Standby** | Minutes | Seconds | $$$ |
| **Multi-Site** | Real-time | Near-zero | $$$$ |

**Exam Tip:**
- "RTO 1 hour, RPO 15 min" = **Pilot Light** or **Warm Standby**
- "Minimize cost" = **Backup & Restore**
- "Zero downtime" = **Multi-Site**

---

## 📈 Caching Strategies

### Where to Cache:
```
1. CloudFront → Global edge caching (static content)
2. API Gateway → API response caching
3. ElastiCache → Database query caching
4. DAX → DynamoDB caching (microseconds)
5. Application → In-memory caching
```

### ElastiCache: Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data types** | Complex | Simple strings |
| **Persistence** | Yes | No |
| **Replication** | Yes (Multi-AZ) | No |
| **Backup** | Yes | No |
| **Pub/Sub** | Yes | No |
| **Use case** | Complex caching | Simple caching |

---

## 💰 Cost Optimization Checklist

### Compute:
- [ ] Right-size instances (CloudWatch)
- [ ] Use Auto Scaling (scale in)
- [ ] Reserved Instances (steady)
- [ ] Spot Instances (batch jobs)
- [ ] Graviton instances (40% cheaper)
- [ ] Lambda for sporadic workloads

### Storage:
- [ ] S3 lifecycle policies
- [ ] S3 Intelligent-Tiering
- [ ] Delete old snapshots
- [ ] Delete unattached volumes
- [ ] Use gp3 instead of gp2

### Database:
- [ ] Reserved Instances (RDS)
- [ ] Aurora Serverless (variable)
- [ ] DynamoDB On-Demand vs Provisioned
- [ ] Delete old snapshots

### Network:
- [ ] Keep traffic in same AZ
- [ ] Use VPC endpoints (avoid NAT)
- [ ] CloudFront for static content
- [ ] Compress data transfers

---

## 🎯 Exam Question Patterns

### Pattern: "Most cost-effective"
**Look for:**
- Serverless (Lambda, DynamoDB)
- S3 over EBS for storage
- Spot Instances
- Reserved Instances (steady workload)
- Right-sizing

### Pattern: "Highly available"
**Look for:**
- Multi-AZ
- Load Balancer
- Auto Scaling
- S3 (inherently HA)
- DynamoDB (inherently HA)

### Pattern: "Least operational overhead"
**Look for:**
- Managed services
- Serverless
- RDS over EC2+DB
- Elastic Beanstalk
- DynamoDB over self-managed

### Pattern: "Serverless"
**Must use:**
- Lambda (compute)
- DynamoDB (database)
- S3 (storage)
- API Gateway (API)
- No EC2, No RDS

### Pattern: "Decouple components"
**Use:**
- SQS (message queue)
- SNS (pub/sub)
- EventBridge (event bus)
- Step Functions (workflow)

---

## 📋 AWS Well-Architected Framework

### 5 Pillars (CROPS):

**1. Cost Optimization**
- Right-sizing
- Reserved capacity
- Serverless
- Monitor and analyze

**2. Reliability**
- Multi-AZ
- Auto Scaling
- Automated recovery
- Test recovery

**3. Operational Excellence**
- IaC (CloudFormation)
- Small, reversible changes
- Monitor and learn
- Anticipate failure

**4. Performance Efficiency**
- Serverless when possible
- Go global (CloudFront)
- Experiment with types
- Use managed services

**5. Security**
- IAM least privilege
- Enable traceability
- Encrypt data
- Automate security
- Prepare for incidents

---

## 🔢 Numbers to Remember

### S3:
```
- Durability: 11 9's (99.999999999%)
- Standard availability: 99.99%
- Max object size: 5 TB
- Max PUT size: 5 GB (use multipart)
- Lifecycle minimum: 30 days
```

### EC2:
```
- Instance store: Ephemeral (lost on stop)
- EBS: Persistent, AZ-specific
- Reserved: 1 or 3 years
- Spot: Up to 90% savings
```

### RDS:
```
- Read Replicas: Up to 15
- Multi-AZ: 1-2 min failover
- Backup retention: 0-35 days
- Automated backups: Daily + transaction logs
```

### Lambda:
```
- Max execution: 15 minutes
- Max memory: 10 GB
- Free tier: 1M requests/month
- Supports: Python, Node, Java, Go, .NET, Ruby
```

### DynamoDB:
```
- Single-digit millisecond latency
- Max item size: 400 KB
- Global Tables: Multi-region
- DynamoDB Streams: 24 hour retention
```

### VPC:
```
- Default: 5 VPCs per region (soft limit)
- CIDR blocks: /16 to /28
- Security Groups: Stateful
- NACLs: Stateless, numbered rules
```

---

## ⚠️ Common Exam Traps

### ❌ Wrong Answers Usually:
- Use root account for daily tasks
- Store credentials in code
- Single AZ for production
- No encryption for sensitive data
- Over-complicated solutions
- Manually manage what can be automated
- Use EC2 when serverless works
- Ignore cost optimization

### ✅ Right Answers Usually:
- Managed services (RDS, DynamoDB)
- Serverless when possible
- Multi-AZ for HA
- IAM roles (not users with keys)
- Encryption enabled
- Auto Scaling
- Least privilege
- CloudFormation (IaC)

---

## 🎯 Keyword → Solution Map

| Keyword | Solution |
|---------|----------|
| "Archive 7+ years" | S3 Glacier Deep Archive |
| "Real-time streaming" | Kinesis |
| "Serverless" | Lambda, DynamoDB, S3 |
| "SQL + managed" | RDS |
| "NoSQL + fast" | DynamoDB |
| "Global delivery" | CloudFront |
| "DNS" | Route 53 |
| "Monitor" | CloudWatch |
| "Audit API calls" | CloudTrail |
| "Decouple" | SQS, SNS |
| "In-memory cache" | ElastiCache |
| "Data warehouse" | Redshift |
| "Highly available" | Multi-AZ, ALB |
| "Cost-effective" | Serverless, Reserved, Spot |
| "Low latency global" | CloudFront, Global Accelerator |
| "Encrypt" | KMS, SSL/TLS |
| "Workflow" | Step Functions |
| "Event-driven" | Lambda, EventBridge |

---

## 📱 Mobile/Quick Scan Format

### Services in 10 Seconds:
```
COMPUTE:   EC2, Lambda, ECS, Fargate
STORAGE:   S3, EBS, EFS
DATABASE:  RDS, DynamoDB, Aurora, ElastiCache, Redshift
NETWORK:   VPC, Route 53, CloudFront, ELB, API Gateway
SECURITY:  IAM, KMS, WAF, Shield, GuardDuty
MANAGE:    CloudWatch, CloudFormation, Auto Scaling
INTEGRATE: SQS, SNS, EventBridge, Step Functions
```

### Decision in 10 Seconds:
```
Cost-effective?     → Serverless, Spot, Reserved
High availability?  → Multi-AZ, ALB, Auto Scaling
Performance?        → Caching, CDN, right instance type
Security?           → Encryption, IAM roles, private subnets
Decouple?          → SQS, SNS
Global?            → CloudFront, Route 53
```

---

## ✅ 1-Hour Before Exam Review

### Must Know Cold:
1. ✅ Shared Responsibility Model
2. ✅ IAM (users, groups, roles, policies)
3. ✅ EC2 pricing models
4. ✅ S3 storage classes
5. ✅ VPC (subnets, SG, NACL)
6. ✅ RDS Multi-AZ vs Read Replicas
7. ✅ High availability patterns
8. ✅ Well-Architected Framework

### Read Question Carefully:
- Watch for: **NOT**, **EXCEPT**, **LEAST**
- Keywords: cost-effective, highly available, serverless
- Eliminate 2 wrong answers first
- Choose BEST option (not just possible)

### Time Management:
- 90 min / 65 Q = 1.4 min/Q (Cloud Practitioner)
- 130 min / 65 Q = 2 min/Q (Solutions Architect)
- Flag hard questions, return later
- Review flagged questions before submit

---

## 🎉 Final Words

### You're Ready If:
✅ Practice exams: 80%+ (CCP) or 85%+ (SAA)  
✅ Can explain concepts simply  
✅ Know when to use each service  
✅ Understand trade-offs  
✅ Feel confident (not perfect)  

### On Exam Day:
```
BREATHE → READ CAREFULLY → ELIMINATE → CHOOSE BEST
```

### Remember:
**You don't need to be perfect. You just need to pass!**

**Good luck! You've got this! 🚀**

---

*Print this sheet and review the night before your exam!*
*Last-minute cramming isn't as important as staying calm and confident.*

---

*Last Updated: January 2026*
*Covers: CLF-C02 & SAA-C03*
