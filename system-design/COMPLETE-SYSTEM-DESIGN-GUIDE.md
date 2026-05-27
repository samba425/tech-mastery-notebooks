# 🚀 Complete System Design Guide - From Zero to Hero

> **Master system design interviews and build scalable systems like FAANG engineers**

## How to Use This Guide

- Read one section at a time and summarize key trade-offs in your own words.
- For each case study, follow this order: requirements -> estimation -> HLD -> deep dive -> bottlenecks.
- Time-box interview practice to 45 minutes and keep 5 minutes for wrap-up trade-offs.
- Maintain a design journal with one architecture diagram per day.

## 📚 Table of Contents

1. [System Design Fundamentals](#1-system-design-fundamentals)
2. [Core Components](#2-core-components)
3. [Design Patterns & Architectures](#3-design-patterns--architectures)
4. [Real-World System Designs](#4-real-world-system-designs)
5. [Advanced Topics](#5-advanced-topics)
6. [Interview Preparation](#6-interview-preparation)

---

## 1. System Design Fundamentals

**Section goal:** Build a strong foundation in reliability, scale, consistency, and data flow trade-offs.

### 1.1 Key Concepts

#### Scalability
**Definition:** A system's ability to handle growth in users, data, and traffic without service degradation.

```
Vertical Scaling (Scale Up):          Horizontal Scaling (Scale Out):
┌─────────────┐                      ┌────┐ ┌────┐ ┌────┐ ┌────┐
│             │                      │ S1 │ │ S2 │ │ S3 │ │ S4 │
│   16 CPU    │                      │2CPU│ │2CPU│ │2CPU│ │2CPU│
│   64GB RAM  │                      │4GB │ │4GB │ │4GB │ │4GB │
│   2TB SSD   │                      └────┘ └────┘ └────┘ └────┘
│             │                      
└─────────────┘                      ← Load Balancer distributes →
                                     ✅ More reliable, no single point
❌ Limited ceiling                   ✅ Linear cost growth
❌ Single point of failure           ✅ Better fault tolerance
❌ Expensive at scale                
```

**Trade-offs:**
- **Vertical scaling:** Simpler to start, but limited by machine size and single-node risk.
- **Horizontal scaling:** Better long-term elasticity and resilience, but adds distributed-system complexity.

#### Availability
**Definition:** Percentage of time system is operational.

```
Availability Levels (SLA):

99%       → 3.65 days downtime/year     (Consumer apps)
99.9%     → 8.76 hours downtime/year    (Business apps)
99.99%    → 52.56 minutes downtime/year (Critical systems)
99.999%   → 5.26 minutes downtime/year  (Financial, healthcare)
99.9999%  → 31.5 seconds downtime/year  (Emergency services)

Formula: Availability = Uptime / (Uptime + Downtime) × 100%
```

#### CAP Theorem
**Definition:** In the presence of network partitions, a distributed system can prioritize either strong consistency or high availability.

```
         Consistency (C)
              ▲
              │
              │
              │
 Partition ◄──┼──► Availability
Tolerance (P) │       (A)

Pick 2:
├─ CA: Single-node or tightly-coupled systems (not partition tolerant at distributed scale)
├─ CP: Prioritize correctness (e.g., critical state systems)
└─ AP: Prioritize uptime and graceful degradation (eventual consistency)

In distributed systems, P is required → Choose between C and A
```

### 1.2 Load Balancing

```
               ┌──────────────┐
               │Load Balancer │
               │  (HAProxy)   │
               └──────┬───────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   ┌────▼───┐    ┌───▼────┐    ┌───▼────┐
   │Server 1│    │Server 2│    │Server 3│
   │Port:80 │    │Port:80 │    │Port:80 │
   └────────┘    └────────┘    └────────┘

Algorithms:
├─ Round Robin: Distribute evenly (S1→S2→S3→S1...)
├─ Least Connections: Route to server with fewest active connections
├─ IP Hash: Same client → same server (session affinity)
├─ Weighted: More powerful servers get more traffic
└─ Least Response Time: Route to fastest server
```

**Health Checks:**
```python
# HAProxy health check configuration
backend web_servers
    balance roundrobin
    option httpchk GET /health
    http-check expect status 200
    server web1 192.168.1.10:80 check inter 2s
    server web2 192.168.1.11:80 check inter 2s
    server web3 192.168.1.12:80 check inter 2s
```

### 1.3 Caching Strategies

```
┌────────┐     ┌────────┐     ┌──────────┐     ┌──────────┐
│ Client │────►│  CDN   │────►│App Server│────►│ Database │
└────────┘     └────────┘     └──────────┘     └──────────┘
                   ▲               ▲
                   │               │
              Edge Cache      Application
              (Static)         Cache (Redis)

Cache Hierarchy:
1. Browser Cache (100ms)
2. CDN Cache (10-50ms)
3. Application Cache (1-5ms)
4. Database Cache (5-10ms)
```

**Cache Invalidation Strategies:**

```
1. Time-to-Live (TTL):
   SET user:123 "{data}" EX 3600  # Expires in 1 hour
   
2. Write-Through:
   Write → Cache → Database (both updated synchronously)
   
3. Write-Back:
   Write → Cache → Database (async)
   
4. Write-Around:
   Write → Database (cache updated on read miss)

5. Cache-Aside (Lazy Loading):
   Read → Check Cache → If miss, load from DB → Update cache
```

### 1.4 Database Design

#### SQL vs NoSQL Decision Tree

```
                    Start
                      │
           ┌──────────▼───────────┐
           │Need ACID guarantees?│
           └──────────┬───────────┘
                 Yes  │  No
              ┌───────┴────────┐
              │                │
         ┌────▼─────┐    ┌─────▼──────┐
         │   SQL    │    │Complex data│
         │(Postgres)│    │structures? │
         └──────────┘    └─────┬──────┘
                           Yes │  No
                         ┌─────┴────────┐
                         │              │
                    ┌────▼──────┐  ┌────▼─────┐
                    │  NoSQL    │  │Key-Value │
                    │(MongoDB)  │  │(Redis)   │
                    └───────────┘  └──────────┘

Use Cases:
├─ PostgreSQL: Banking, e-commerce orders, user management
├─ MongoDB: Content management, catalogs, real-time analytics
├─ Cassandra: Time-series data, IoT, logging
├─ Redis: Session storage, real-time leaderboards, caching
└─ DynamoDB: Serverless applications, high-throughput workloads
```

#### Database Sharding

```
User Sharding (Horizontal Partitioning):

Hash-based Sharding:
user_id % 4 determines shard

Users 1-25M       Users 25-50M      Users 50-75M      Users 75-100M
┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│ Shard 0  │      │ Shard 1  │      │ Shard 2  │      │ Shard 3  │
│          │      │          │      │          │      │          │
│ user_id  │      │ user_id  │      │ user_id  │      │ user_id  │
│ % 4 = 0  │      │ % 4 = 1  │      │ % 4 = 2  │      │ % 4 = 3  │
└──────────┘      └──────────┘      └──────────┘      └──────────┘

Range-based Sharding:
├─ A-G → Shard 1
├─ H-N → Shard 2
├─ O-T → Shard 3
└─ U-Z → Shard 4

Geographic Sharding:
├─ US-East → Shard 1
├─ US-West → Shard 2
├─ EU → Shard 3
└─ Asia → Shard 4
```

### 1.5 Message Queues

```
           Publishers                Message Queue                Consumers
           
┌──────────┐                    ┌─────────────────┐         ┌──────────┐
│ Service A│───┐               │  Kafka/RabbitMQ │         │Consumer 1│
└──────────┘   │               │                 │    ┌───►│(Email)   │
               │  Messages     │ ┌─┐ ┌─┐ ┌─┐ ┌─┐│    │    └──────────┘
┌──────────┐   ├──────────────►│ │1│ │2│ │3│ │4││────┤
│ Service B│───┘               │ └─┘ └─┘ └─┘ └─┘│    │    ┌──────────┐
└──────────┘                   │   Queue Topic   │    └───►│Consumer 2│
                               └─────────────────┘         │(SMS)     │
                                                            └──────────┘

Benefits:
✅ Async processing
✅ Decoupling services
✅ Load leveling
✅ Fault tolerance
✅ Scalability
```

---

## 2. Core Components

**Section goal:** Understand the responsibilities and failure modes of each building block.

### 2.1 API Gateway

```
┌─────────┐
│ Clients │
└────┬────┘
     │
     ▼
┌─────────────────────┐
│   API Gateway       │  ← Single entry point
│  (Kong/AWS API GW)  │
│                     │
│ ✓ Authentication    │
│ ✓ Rate Limiting     │
│ ✓ Request Routing   │
│ ✓ Load Balancing    │
│ ✓ Caching          │
│ ✓ Logging          │
└──────┬──────────────┘
       │
   ┌───┴────┬────────┬────────┐
   │        │        │        │
┌──▼──┐  ┌─▼──┐  ┌──▼──┐  ┌──▼──┐
│User │  │Order│  │Pay  │  │Notif│
│Svc  │  │Svc  │  │Svc  │  │Svc  │
└─────┘  └────┘  └─────┘  └─────┘
```

### 2.2 Service Mesh

```
         Control Plane (Istio/Linkerd)
              ┌─────────────┐
              │   Config    │
              │  Telemetry  │
              └──────┬──────┘
                     │
     ┌───────────────┼───────────────┐
     │               │               │
┌────▼──────┐  ┌────▼──────┐  ┌─────▼─────┐
│Service A  │  │Service B  │  │Service C  │
│┌─────────┐│  │┌─────────┐│  │┌─────────┐│
││Sidecar  ││  ││Sidecar  ││  ││Sidecar  ││
││(Envoy)  ││◄─┤│(Envoy)  ││◄─┤│(Envoy)  ││
│└─────────┘│  │└─────────┘│  │└─────────┘│
└───────────┘  └───────────┘  └───────────┘

Features:
- Service discovery
- Load balancing
- Failure recovery
- Metrics & monitoring
- A/B testing
- Canary deployments
```

### 2.3 Content Delivery Network (CDN)

```
Global CDN Distribution:

        Origin Server
        (US-East)
            │
    ┌───────┼───────┐
    │       │       │
┌───▼──┐ ┌──▼──┐ ┌──▼──┐
│ CDN  │ │ CDN │ │ CDN │
│US-W  │ │ EU  │ │Asia │
└───┬──┘ └──┬──┘ └──┬──┘
    │       │       │
Users in   Users   Users
Americas   in EU   in Asia

Response Time:
Without CDN: 200-500ms
With CDN: 10-50ms (90% improvement)
```

---

## 3. Design Patterns & Architectures

**Section goal:** Learn when to choose each architecture pattern and what trade-offs it introduces.

### 3.1 Microservices Architecture

```
┌────────────────────────────────────────────────────────┐
│              API Gateway (Kong)                        │
└───────────┬────────────────────────────────────────────┘
            │
    ┌───────┼───────┬────────┬────────┐
    │       │       │        │        │
┌───▼──┐ ┌──▼──┐ ┌──▼───┐ ┌─▼────┐ ┌─▼────┐
│User  │ │Order│ │Invent│ │Paymt │ │Notif │
│Svc   │ │Svc  │ │ory   │ │Svc   │ │Svc   │
└───┬──┘ └──┬──┘ └──┬───┘ └─┬────┘ └─┬────┘
    │       │       │        │        │
┌───▼───────▼───────▼────────▼────────▼───┐
│        Message Bus (Kafka/RabbitMQ)     │
└─────────────────────────────────────────┘
    │       │       │        │        │
┌───▼──┐ ┌──▼──┐ ┌──▼───┐ ┌─▼────┐ ┌─▼────┐
│UserDB│ │Order│ │Invent│ │Paymt │ │Notif │
│      │ │DB   │ │DB    │ │DB    │ │DB    │
└──────┘ └─────┘ └──────┘ └──────┘ └──────┘

Principles:
✓ Independent deployment
✓ Database per service
✓ Async communication
✓ Fault isolation
✓ Technology diversity
```

### 3.2 Event-Driven Architecture

```
Event Producers → Event Bus → Event Consumers

┌────────────┐        ┌─────────────┐        ┌────────────┐
│Order       │─Event─►│             │─Event─►│Inventory   │
│Service     │        │   Kafka     │        │Service     │
└────────────┘        │   Topics    │        └────────────┘
                      │             │
┌────────────┐        │             │        ┌────────────┐
│Payment     │─Event─►│  - orders   │─Event─►│Email       │
│Service     │        │  - payments │        │Service     │
└────────────┘        │  - shipping │        └────────────┘
                      └─────────────┘

Event Flow:
1. User places order
2. Order Created event → Kafka
3. Inventory Service consumes → Reserves items
4. Payment Service processes → Payment Confirmed event
5. Email Service sends confirmation
6. Shipping Service prepares shipment

Benefits:
- Loose coupling
- Scalability
- Event replay
- Audit trail
```

### 3.3 CQRS (Command Query Responsibility Segregation)

```
         Commands (Write)              Queries (Read)
              │                              │
              ▼                              ▼
      ┌──────────────┐              ┌──────────────┐
      │ Write Model  │              │  Read Model  │
      │ (PostgreSQL) │              │  (MongoDB)   │
      └──────┬───────┘              └──────▲───────┘
             │                             │
             │      Event Stream           │
             └────────►Kafka───────────────┘
                       │
                       ▼
               ┌──────────────┐
               │Event Store   │
               │(Audit Trail) │
               └──────────────┘

Use Cases:
- E-commerce (complex writes, simple reads)
- Banking (audit trail required)
- Analytics (read-heavy workload)
```

---

## 4. Real-World System Designs

**Section goal:** Practice complete interview-style designs using realistic constraints.

### 4.1 Design URL Shortener (like bit.ly)

**Requirements:**
- 100M URLs/month
- 10:1 read:write ratio
- URLs expire after 5 years
- Custom aliases supported

**Clarifying questions to ask in interviews:**
- Is custom alias uniqueness global or per user?
- Do we need analytics (click geography, referrer, device)?
- Do we support preview/safety checks for malicious URLs?

**Capacity Estimation:**
```
Write: 100M/month = 40 URLs/sec
Read: 400 URLs/sec
Storage: 100M × 12 months × 5 years = 6B URLs
        6B × 500 bytes = 3TB
```

**High-Level Design:**
```
┌────────┐         ┌──────────────┐         ┌──────────┐
│ Client │────────►│ Load Balancer│────────►│App Server│
└────────┘         └──────────────┘         └────┬─────┘
                                                  │
                                    ┌─────────────┼─────────────┐
                                    │             │             │
                               ┌────▼───┐    ┌───▼────┐   ┌────▼────┐
                               │ Redis  │    │Database│   │ Counter │
                               │ Cache  │    │(NoSQL) │   │ Service │
                               └────────┘    └────────┘   └─────────┘

URL Generation Algorithm:
1. Base62 Encoding: [a-zA-Z0-9] = 62^7 = 3.5 trillion URLs
2. Hash: MD5(long_url) → Take first 7 chars
3. Counter: Auto-increment counter → Base62 encode

Database Schema:
{
  "short_url": "abc123",
  "long_url": "https://example.com/very/long/url",
  "user_id": "user123",
  "created_at": "2024-01-01",
  "expires_at": "2029-01-01",
  "click_count": 1523
}
```

### 4.2 Design Instagram

**Requirements:**
- 500M daily active users
- 100M photos/day
- Read-heavy (100:1)
- Low latency

**Interview focus points:**
- Feed fan-out strategy choice (write, read, or hybrid) and why.
- Media storage + CDN invalidation approach.
- Ranking pipeline boundaries (online vs offline features).

**Architecture:**
```
             ┌────────────┐
             │   CDN      │ ← Images, videos
             └────────────┘
                   ▲
                   │
┌────────┐    ┌────┴────────┐    ┌──────────────┐
│ Client │───►│API Gateway  │───►│ App Servers  │
└────────┘    └─────────────┘    └──────┬───────┘
                                         │
                    ┌────────────────────┼────────────────┐
                    │                    │                │
              ┌─────▼─────┐       ┌─────▼─────┐   ┌──────▼──────┐
              │  Redis    │       │ PostgreSQL│   │Object Store │
              │  Cache    │       │(Metadata) │   │    (S3)     │
              └───────────┘       └───────────┘   └─────────────┘
                                         │
                                  ┌──────▼──────┐
                                  │  Cassandra  │
                                  │(News Feed)  │
                                  └─────────────┘

Data Model:
Users: PostgreSQL (ACID for followers/following)
Photos: S3 (object storage)
Feed: Cassandra (time-series, high write throughput)
Cache: Redis (hot data, trending)

News Feed Generation:
1. Fan-out on write (for celebrities)
2. Fan-out on read (for normal users)
3. Hybrid approach (balance)
```

### 4.3 Design Netflix

**Requirements:**
- 200M subscribers
- 1B hours watched/day
- 4K streaming
- Global availability

**Interview focus points:**
- Encoding pipeline throughput and storage lifecycle policy.
- Adaptive bitrate fallback behavior in poor networks.
- Regional failover and content licensing constraints.

**Architecture:**
```
                      ┌─────────────┐
                      │   AWS S3    │ ← Video Storage
                      └──────┬──────┘
                             │
                      ┌──────▼──────┐
                      │   Encoding  │ ← Multiple resolutions
                      │   Service   │   (360p, 720p, 1080p, 4K)
                      └──────┬──────┘
                             │
                 ┌───────────▼────────────┐
                 │   CDN (CloudFront)     │ ← Edge locations
                 └────────────────────────┘
                            │
     ┌──────────────────────┼──────────────────────┐
     │                      │                      │
┌────▼────┐          ┌─────▼─────┐         ┌──────▼──────┐
│ Client  │          │ Recommend │         │ Playback    │
│(Browser)│          │ Engine    │         │ Service     │
└─────────┘          │(ML Model) │         │(ABR)        │
                     └───────────┘         └─────────────┘

Adaptive Bitrate Streaming (ABR):
Network Speed → Video Quality
- Slow: 360p (0.7 Mbps)
- Medium: 720p (3 Mbps)
- Fast: 1080p (5 Mbps)
- Very Fast: 4K (25 Mbps)
```

### 4.4 Design Uber

**Requirements:**
- Real-time matching
- 15M daily rides
- Location tracking
- Payment processing

**Interview focus points:**
- Geo-indexing strategy and update frequency.
- Dispatch fairness vs ETA optimization trade-off.
- Idempotency and exactly-once behavior for ride/payment events.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│              API Gateway + Load Balancer               │
└───────────┬────────────────────────────────────────────┘
            │
    ┌───────┼───────┬────────┬────────┬────────┐
    │       │       │        │        │        │
┌───▼──┐ ┌──▼──┐ ┌──▼───┐ ┌─▼────┐ ┌─▼────┐ ┌─▼────┐
│User  │ │Driver│ │Match │ │Trip  │ │Paymt │ │Notif │
│Svc   │ │Svc   │ │Eng   │ │Svc   │ │Svc   │ │Svc   │
└───┬──┘ └──┬───┘ └──┬───┘ └─┬────┘ └─┬────┘ └─┬────┘
    │       │        │        │        │        │
    └───────┴────────┴────────┴────────┴────────┘
                     │
              ┌──────▼──────┐
              │  Kafka      │ ← Event Stream
              └──────┬──────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
    ┌────▼────┐ ┌───▼────┐ ┌────▼────┐
    │Location │ │Surge   │ │Analytics│
    │Tracking │ │Pricing │ │Service  │
    └─────────┘ └────────┘ └─────────┘

Geo-spatial Database:
- QuadTree for driver location indexing
- PostGIS for proximity queries
- Redis Geo for real-time updates

Matching Algorithm:
1. Get user location
2. Query nearby drivers (radius: 5km)
3. Filter by availability, rating
4. Calculate ETA for each driver
5. Assign closest driver
6. Send push notification
```

---

## 5. Advanced Topics

**Section goal:** Strengthen distributed systems depth for senior-level interviews.

### 5.1 Consistent Hashing

```
Traditional Hash: server = hash(key) % N
Problem: Adding/removing servers causes massive redistribution

Consistent Hashing: Hash Ring

        0°
        │
    ┌───┴───┐
   S1       S3
  ┌─┘       └─┐
 K1          K3
 ││          ││
 └┘          └┘
90°  S2 ─── K2   270°
 ││          ││
 K4          K5
  └─┐       ┌─┘
   S4       S5
    └───┬───┘
        │
       180°

Add Server → Only affects immediate neighbors
Remove Server → Minimal key redistribution

Virtual Nodes: Each server → 150 positions (balanced load)
```

### 5.2 Rate Limiting

```
Algorithm Options:

1. Token Bucket:
   ┌────────────┐
   │  Bucket    │
   │ [🪙🪙🪙]   │ ← Refill: R tokens/second
   │ Capacity:N │
   └────────────┘
   Request → Consume 1 token
   If empty → Reject (429 Too Many Requests)

2. Leaky Bucket:
   Requests → Queue → Process at fixed rate

3. Fixed Window:
   Limit: 100 requests/hour
   Window: 00:00-01:00
   
4. Sliding Window Log:
   Track timestamp of each request
   Count requests in last N seconds

Implementation (Redis):
INCR rate_limit:user123
EXPIRE rate_limit:user123 60
IF count > 100 THEN REJECT
```

### 5.3 Distributed Locking

```
Redlock Algorithm (Redis):

┌────────┐   ┌────────┐   ┌────────┐
│Redis 1 │   │Redis 2 │   │Redis 3 │
└───┬────┘   └───┬────┘   └───┬────┘
    │            │            │
    │ SET lock:resource "token" NX PX 30000
    │            │            │
    ✓            ✓            ✓
    
Acquire lock if N/2 + 1 replicas succeed
Hold lock with TTL (auto-release on failure)
Release explicitly when done

Use Cases:
- Job scheduling
- Resource allocation
- Leader election
```

---

## 6. Interview Preparation

**Section goal:** Build a repeatable communication framework for 45-60 minute interviews.

### 6.1 Interview Framework

```
┌────────────────────────────────────────┐
│  1. REQUIREMENTS (5 min)               │
│  ─────────────────────────────────────│
│  Functional:                           │
│  - Core features                       │
│  - User actions                        │
│                                        │
│  Non-functional:                       │
│  - Scale (users, QPS)                  │
│  - Performance (latency)               │
│  - Availability (SLA)                  │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│  2. CAPACITY ESTIMATION (5 min)        │
│  ─────────────────────────────────────│
│  - Traffic (requests/sec)              │
│  - Storage (TB/year)                   │
│  - Bandwidth (GB/sec)                  │
│  - Cache size                          │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│  3. API DESIGN (5 min)                 │
│  ─────────────────────────────────────│
│  POST /api/v1/posts                    │
│  GET  /api/v1/posts/:id                │
│  GET  /api/v1/feed                     │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│  4. HIGH-LEVEL DESIGN (15 min)         │
│  ─────────────────────────────────────│
│  Draw architecture diagram             │
│  - Clients                             │
│  - Load balancers                      │
│  - Application servers                 │
│  - Databases                           │
│  - Caches                              │
│  - CDN                                 │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│  5. DEEP DIVE (20 min)                 │
│  ─────────────────────────────────────│
│  - Database schema                     │
│  - Sharding strategy                   │
│  - Caching policy                      │
│  - Failure scenarios                   │
│  - Monitoring                          │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│  6. WRAP UP (5 min)                    │
│  ─────────────────────────────────────│
│  - Bottlenecks                         │
│  - Trade-offs made                     │
│  - Future improvements                 │
└────────────────────────────────────────┘
```

### 6.2 Common Mistakes to Avoid

❌ **Don't:**
- Jump into implementation
- Assume requirements
- Ignore scale/numbers
- Forget about failures
- Overcomplicate initially
- Skip trade-off discussion

✅ **Do:**
- Clarify requirements
- Start simple, iterate
- Consider trade-offs
- Think about edge cases
- Communicate clearly
- Call out assumptions explicitly

### 6.3 Estimation Cheat Sheet

```
Time:
1M seconds ≈ 12 days
1B seconds ≈ 32 years

Storage:
Character: 1 byte
Integer: 4-8 bytes
Timestamp: 8 bytes
Text (avg): 100-500 bytes
Image: 200 KB
Video (1 min): 50 MB

Latency:
L1 cache: 0.5 ns
RAM: 100 ns
SSD: 100 μs
Network (DC): 500 μs
HDD: 10 ms
Network (inter-city): 100 ms
```

---

## 📚 Recommended Resources

### Books
- **Designing Data-Intensive Applications** by Martin Kleppmann
- **System Design Interview** by Alex Xu (Volumes 1 & 2)
- **Web Scalability for Startup Engineers** by Artur Ejsmont

### Practice
- **LeetCode** - System design explore cards
- **SystemDesign.one** - Real-world examples
- **ByteByteGo** - Visual system design

### Companies' Engineering Blogs
- Netflix Tech Blog
- Uber Engineering
- Airbnb Engineering
- Instagram Engineering
- Discord Engineering

---

## 🎯 Interview Checklist

Before your interview:
- [ ] Understand CAP theorem
- [ ] Know load balancing algorithms
- [ ] Master caching strategies
- [ ] Understand database sharding
- [ ] Practice capacity estimation
- [ ] Draw 10+ system diagrams
- [ ] Review FAANG system designs
- [ ] Understand trade-offs

**Good luck with your system design interviews! 🚀**
