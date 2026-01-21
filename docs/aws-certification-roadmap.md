# AWS Certification Roadmap - From Beginner to Architect

## 🎯 Your Learning Path

```
┌─────────────────────────────────────────────────────────────┐
│                   AWS Certification Journey                  │
└─────────────────────────────────────────────────────────────┘

    START HERE ⭐
         ↓
┌──────────────────────────┐
│ AWS Cloud Practitioner   │  ← YOU ARE HERE
│ CLF-C02                  │
│ Duration: 2-4 weeks      │
│ Difficulty: ⭐           │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Solutions Architect      │  ← NEXT STEP
│ Associate (SAA-C03)      │
│ Duration: 6-8 weeks      │
│ Difficulty: ⭐⭐⭐        │
└────────────┬─────────────┘
             ↓
    ┌────────┴────────┐
    ↓                 ↓
┌──────────┐   ┌──────────────┐
│Developer │   │ SysOps Admin │
│Associate │   │ Associate    │
│DVA-C02   │   │ SOA-C02      │
└──────────┘   └──────────────┘
    │                 │
    └────────┬────────┘
             ↓
┌──────────────────────────┐
│ Solutions Architect      │
│ Professional (SAP-C02)   │
│ Difficulty: ⭐⭐⭐⭐⭐    │
└──────────────────────────┘
```

---

## 📅 Detailed Study Timeline

### Phase 1: Cloud Practitioner (Weeks 1-4)

#### Week 1: Cloud Fundamentals
**Monday-Tuesday: Cloud Concepts**
- [ ] What is cloud computing?
- [ ] Benefits of cloud (6 advantages)
- [ ] Deployment models (Public, Private, Hybrid)
- [ ] Service models (IaaS, PaaS, SaaS)
- [ ] AWS Global Infrastructure

**Study Time:** 1-2 hours/day  
**Resources:**
- AWS Skill Builder: Cloud Practitioner Essentials
- AWS Cloud Practitioner guide (in this repo)
- Videos: FreeCodeCamp AWS Cloud Practitioner course

**Practice:**
- [ ] Quiz yourself on cloud concepts
- [ ] Create AWS Free Tier account

---

**Wednesday-Thursday: Security & IAM**
- [ ] Shared Responsibility Model ⭐⭐⭐
- [ ] IAM (Users, Groups, Roles, Policies)
- [ ] MFA setup
- [ ] Root user best practices
- [ ] AWS compliance programs

**Hands-On:**
- [ ] Create IAM users and groups
- [ ] Set up MFA on root account
- [ ] Create IAM role for EC2
- [ ] Write simple IAM policy

---

**Friday-Sunday: Core Services Part 1**
- [ ] EC2 basics
- [ ] EC2 pricing models
- [ ] S3 storage classes
- [ ] AWS Lambda intro
- [ ] VPC basics

**Hands-On:**
- [ ] Launch t2.micro EC2 instance
- [ ] Create S3 bucket and upload file
- [ ] Create simple Lambda function
- [ ] Explore VPC console

**Weekend Practice:** 20 practice questions

---

#### Week 2: Core AWS Services

**Monday-Tuesday: Storage & Databases**
- [ ] S3 deep dive
- [ ] EBS, EFS, Storage Gateway
- [ ] RDS vs Aurora
- [ ] DynamoDB basics
- [ ] Redshift overview

**Hands-On:**
- [ ] Create lifecycle policy for S3
- [ ] Launch RDS MySQL instance
- [ ] Create DynamoDB table

---

**Wednesday-Thursday: Networking & Content Delivery**
- [ ] VPC components (subnets, route tables, IGW)
- [ ] Security Groups vs NACLs
- [ ] Route 53 basics
- [ ] CloudFront CDN
- [ ] ELB types overview

**Hands-On:**
- [ ] Create VPC with public/private subnet
- [ ] Configure security group
- [ ] Create CloudFront distribution

---

**Friday-Sunday: Additional Services**
- [ ] CloudWatch monitoring
- [ ] CloudFormation basics
- [ ] SNS and SQS
- [ ] Elastic Beanstalk
- [ ] AWS support plans

**Practice:** 40 practice questions over weekend

---

#### Week 3: Billing & Advanced Concepts

**Monday-Tuesday: Cost Management**
- [ ] AWS pricing models
- [ ] Free Tier limits
- [ ] AWS Budgets
- [ ] Cost Explorer
- [ ] Billing Dashboard
- [ ] Consolidated billing

**Hands-On:**
- [ ] Create budget alert
- [ ] Explore Cost Explorer
- [ ] Use AWS Pricing Calculator

---

**Wednesday-Thursday: Security Deep Dive**
- [ ] AWS WAF
- [ ] AWS Shield
- [ ] GuardDuty
- [ ] AWS Artifact
- [ ] CloudTrail
- [ ] AWS Config

---

**Friday-Sunday: Review & Practice**
- [ ] Review all notes
- [ ] Take 2-3 full practice exams
- [ ] Focus on weak areas
- [ ] Read AWS whitepapers overview

**Target:** 80%+ on practice exams

---

#### Week 4: Final Preparation

**Monday-Wednesday: Practice Exams**
- [ ] Practice exam #1 (identify gaps)
- [ ] Review incorrect answers thoroughly
- [ ] Practice exam #2
- [ ] Practice exam #3

**Daily:** Review one domain in detail

---

**Thursday-Friday: Final Review**
- [ ] Review all flashcards
- [ ] Skim through notes
- [ ] No new topics (just review)
- [ ] Get good sleep

---

**Saturday: EXAM DAY! 🎯**
- [ ] Review quick cheatsheet (1 hour before)
- [ ] Arrive 15 minutes early
- [ ] Take breaks if needed
- [ ] Stay calm and confident

---

### Phase 2: Solutions Architect Associate (Weeks 5-12)

#### Week 5-6: Foundation + Advanced IAM

**Week 5 Focus:**
- [ ] Review Cloud Practitioner concepts
- [ ] IAM policies deep dive
- [ ] Cross-account access
- [ ] IAM best practices
- [ ] AWS Organizations
- [ ] Service Control Policies (SCPs)

**Hands-On:**
- [ ] Create custom IAM policies
- [ ] Set up cross-account role
- [ ] Configure AWS Organizations

**Study Time:** 2-3 hours/day

---

**Week 6 Focus:**
- [ ] VPC architecture
- [ ] Multi-tier VPC design
- [ ] VPC peering
- [ ] Transit Gateway
- [ ] VPN and Direct Connect
- [ ] Route 53 routing policies

**Hands-On:**
- [ ] Build 3-tier VPC architecture
- [ ] Configure VPC peering
- [ ] Set up Site-to-Site VPN

**Weekend:** 50 practice questions

---

#### Week 7-8: Compute & Storage

**Week 7 Focus:**
- [ ] EC2 instance types (detailed)
- [ ] Auto Scaling policies
- [ ] ELB (ALB, NLB, GLB)
- [ ] Lambda advanced
- [ ] ECS/EKS basics
- [ ] Elastic Beanstalk

**Hands-On:**
- [ ] Deploy app with Auto Scaling + ALB
- [ ] Create Lambda with API Gateway
- [ ] Deploy containerized app on ECS

---

**Week 8 Focus:**
- [ ] S3 advanced features
- [ ] S3 replication (CRR, SRR)
- [ ] EBS volume types
- [ ] EFS use cases
- [ ] Storage Gateway
- [ ] AWS Backup

**Hands-On:**
- [ ] Configure S3 CRR
- [ ] Set up EFS for multiple EC2
- [ ] Create automated backup plan

**Practice:** 100 questions this week

---

#### Week 9-10: Databases & Caching

**Week 9 Focus:**
- [ ] RDS Multi-AZ vs Read Replicas
- [ ] Aurora architecture
- [ ] Aurora Serverless
- [ ] DynamoDB deep dive
- [ ] DynamoDB Streams & DAX
- [ ] ElastiCache (Redis vs Memcached)

**Hands-On:**
- [ ] RDS with Multi-AZ and Read Replicas
- [ ] Create DynamoDB with GSI
- [ ] Set up ElastiCache cluster

---

**Week 10 Focus:**
- [ ] Redshift architecture
- [ ] Neptune (graph DB)
- [ ] DocumentDB
- [ ] Database migration strategies
- [ ] DMS (Database Migration Service)

**Hands-On:**
- [ ] Design database architecture for scenarios
- [ ] Practice database selection decisions

**Practice:** Architecture design scenarios

---

#### Week 11: Security & Compliance

**Monday-Tuesday:**
- [ ] Encryption (at rest & in transit)
- [ ] KMS (Key Management Service)
- [ ] Secrets Manager
- [ ] Parameter Store
- [ ] Certificate Manager

**Wednesday-Thursday:**
- [ ] AWS WAF advanced
- [ ] GuardDuty setup
- [ ] Security Hub
- [ ] Macie for S3
- [ ] Inspector

**Friday-Sunday:**
- [ ] Well-Architected Framework (all pillars)
- [ ] Security best practices
- [ ] Compliance programs
- [ ] Practice: 75 questions

---

#### Week 12: Review & Practice

**Monday-Wednesday:**
- [ ] Full practice exam #1
- [ ] Review all incorrect answers
- [ ] Full practice exam #2
- [ ] Deep dive weak areas

**Thursday-Friday:**
- [ ] Full practice exam #3
- [ ] Quick review of all services
- [ ] Architecture pattern review
- [ ] No new material

**Target:** 85%+ on practice exams

**Weekend:**
- [ ] Light review only
- [ ] Read exam tips
- [ ] Rest well

**Monday: EXAM DAY! 🎯**

---

## 📊 Study Tracker Template

### Daily Log:

```markdown
## Date: ___________

### Topics Covered:
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3

### Hands-On Completed:
- [ ] Lab 1
- [ ] Lab 2

### Practice Questions:
- Attempted: ___/___
- Score: ___%
- Weak areas: ___________

### Time Spent: ___ hours

### Notes:
- Key takeaway 1
- Key takeaway 2
- Questions to research

### Tomorrow's Goals:
1. 
2. 
3. 
```

---

## 🎯 Weekly Milestones

### Cloud Practitioner Milestones:

| Week | Milestone | Success Criteria |
|------|-----------|------------------|
| 1 | Understand basics | Explain 6 cloud benefits |
| 2 | Know core services | Describe 20+ services |
| 3 | Master billing | Use cost tools |
| 4 | Exam ready | 80%+ on practice |

### Solutions Architect Milestones:

| Week | Milestone | Success Criteria |
|------|-----------|------------------|
| 5-6 | Network architecture | Design 3-tier VPC |
| 7-8 | Compute & storage | Deploy HA application |
| 9-10 | Database expertise | Choose right DB for scenarios |
| 11 | Security mastery | Design secure architecture |
| 12 | Exam ready | 85%+ on practice |

---

## 📚 Resource Library

### Free Resources:

**Official AWS:**
- ✅ [AWS Skill Builder](https://skillbuilder.aws) - Free courses
- ✅ [AWS Documentation](https://docs.aws.amazon.com)
- ✅ [AWS Whitepapers](https://aws.amazon.com/whitepapers)
- ✅ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
- ✅ [AWS Free Tier](https://aws.amazon.com/free)

**YouTube Channels:**
- ✅ FreeCodeCamp - AWS Cloud Practitioner course
- ✅ AWS Events - Official channel
- ✅ StephaneCloud - Exam tips

**Practice:**
- ✅ AWS Skill Builder practice exams
- ✅ ExamTopics (community questions - use cautiously)

---

### Paid Resources (Recommended):

**Courses ($10-50):**
- ⭐⭐⭐ [Stephane Maarek (Udemy)](https://www.udemy.com/user/stephane-maarek)
  - Cloud Practitioner: $12-15
  - Solutions Architect: $12-15
  - Best for: Clear explanations, regular updates

- ⭐⭐⭐ [Adrian Cantrill](https://learn.cantrill.io)
  - Solutions Architect: $40
  - Best for: Deep technical understanding

- ⭐⭐ [A Cloud Guru / Pluralsight](https://acloudguru.com)
  - Subscription: $35/month
  - Best for: Multiple certifications

**Practice Exams ($15-30):**
- ⭐⭐⭐ [Tutorials Dojo](https://tutorialsdojo.com)
  - Excellent explanations
  - Very similar to real exam
  - $15 per exam set

- ⭐⭐ [Whizlabs](https://www.whizlabs.com)
  - Good variety
  - More questions
  - $20-30

---

## 🧠 Study Techniques

### Active Learning:

**1. Feynman Technique:**
```
1. Learn a concept
2. Teach it to someone (or write it out)
3. Identify gaps in understanding
4. Review and simplify
```

**2. Spaced Repetition:**
```
Day 1: Learn new topic
Day 3: Review topic
Day 7: Review again
Day 14: Final review
```

**3. Hands-On Practice:**
```
For EVERY service:
1. Read documentation
2. Watch tutorial
3. Build it yourself
4. Break it and fix it
5. Teach someone
```

---

### Memory Aids:

**Service Categories (SCND):**
- **S**torage: S3, EBS, EFS, Storage Gateway
- **C**ompute: EC2, Lambda, ECS, Elastic Beanstalk
- **N**etwork: VPC, Route 53, CloudFront, ELB
- **D**atabase: RDS, DynamoDB, Redshift, ElastiCache

**Security CIA:**
- **C**onfidentiality (Encryption, IAM)
- **I**ntegrity (Versioning, MFA Delete)
- **A**vailability (Multi-AZ, Backups)

---

## 💡 Exam Tips

### Question Patterns:

**Pattern 1: Scenario-Based**
```
"A company needs to..."
"An application requires..."

Strategy:
1. Identify requirements (HA, cost, performance)
2. Eliminate options that don't meet requirements
3. Choose BEST option (not just possible)
```

**Pattern 2: Service Selection**
```
"Which service should be used for..."

Strategy:
1. Understand service use cases
2. Look for keywords
3. Eliminate wrong service categories
```

**Pattern 3: Best Practices**
```
"What is the MOST secure/cost-effective way..."

Strategy:
1. Apply Well-Architected principles
2. Choose managed services when possible
3. Follow AWS recommendations
```

---

### Red Flags:

❌ "Use root account for..." → WRONG  
❌ "Store credentials in code..." → WRONG  
❌ "Make S3 bucket public for..." → Usually WRONG  
❌ "Use single AZ for production..." → WRONG  
❌ "No encryption needed..." → Usually WRONG  

---

## ✅ Pre-Exam Checklist

### 1 Week Before:
- [ ] Scoring 80%+ consistently on practice exams
- [ ] Reviewed all incorrect answers
- [ ] Read Well-Architected Framework
- [ ] Hands-on with core services
- [ ] Scheduled exam date

### 1 Day Before:
- [ ] Light review only (no cramming)
- [ ] Reviewed exam format
- [ ] Prepared two IDs
- [ ] Good night's sleep (8 hours)
- [ ] Healthy meal planned

### Exam Day:
- [ ] Wake up 2 hours before exam
- [ ] Light breakfast
- [ ] Review quick cheatsheet (30 min)
- [ ] Arrive 15 minutes early
- [ ] Stay calm and confident

---

## 🎯 After Certification

### Immediate Actions:
1. ✅ Download certificate from AWS Certification portal
2. ✅ Add to LinkedIn (with badge from Credly)
3. ✅ Update resume
4. ✅ Share achievement (optional)

### Keep Learning:
- Build real projects
- Contribute to open source
- Write blog posts about learnings
- Help others prepare
- Stay updated with AWS announcements

### Next Certifications:
```
After Cloud Practitioner:
→ Solutions Architect Associate (recommended)

After Solutions Architect:
→ Developer Associate OR SysOps Admin
→ Then: Solutions Architect Professional
```

---

## 📞 Support & Community

### Where to Ask Questions:
- **AWS re:Post** - Official AWS forum
- **Reddit:** r/AWSCertifications
- **LinkedIn:** AWS study groups
- **Discord:** Cloud career communities

### Study Groups:
- Find study partners online
- Join local AWS meetups
- Create accountability partners

---

## 🚀 Motivation

### Remember:
```
"The expert in anything was once a beginner."
```

### Your Progress Tracker:

```
☐ Started learning (You are here!)
☐ Completed Week 1
☐ Completed Week 2
☐ First practice exam
☐ 50% on practice exams
☐ 70% on practice exams
☐ 80% on practice exams
☐ PASSED CLOUD PRACTITIONER! 🎉
☐ Started SAA prep
☐ PASSED SOLUTIONS ARCHITECT! 🚀
```

---

**You've got this! Start with Cloud Practitioner, build confidence, then tackle Solutions Architect. Consistency is key! 💪**

---

*Last Updated: January 2026*
