#!/usr/bin/env python3
"""Generate REAL-WORLD-SYSTEM-DESIGN-50.md with HLD + LLD case studies."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "REAL-WORLD-SYSTEM-DESIGN-50.md"

HLD = [
    ("YouTube", "Video upload, transcode, CDN delivery, recommendations", "500h video/min upload; 2B+ users; read-heavy", "CP/AP hybrid", [
        ("Client", "Web, mobile, TV apps"),
        ("API Gateway", "Auth, rate limits, routing"),
        ("Upload Service", "Resumable multipart to object storage"),
        ("Transcode Pipeline", "Kafka workers: 360p–4K, thumbnails"),
        ("Metadata DB", "Sharding by video_id; Cassandra/Dynamo style"),
        ("CDN", "Edge caches for segments (HLS/DASH)"),
        ("Search", "Elasticsearch + inverted index"),
        ("Rec Engine", "Offline ML + online feature store"),
    ], "Upload → S3 → transcode queue → metadata write → CDN propagate → play via edge", "S3, Kafka, Cassandra, Redis, CDN, Bigtable-style index"),
    ("Netflix", "Global streaming with personalization", "200M+ subs; 15% internet traffic peak", "AP for playback, CP for billing", [
        ("Open Connect CDN", "ISP-local caches"),
        ("API Gateway", "Zuul / Envoy edge"),
        ("Playback", "ABR manifest, session state"),
        ("Encoding", "Per-title encoding farm"),
        ("Recommendations", "Spark offline + real-time events"),
        ("User/Billing", "Cassandra + regional isolation"),
    ], "Client → CDN hit → miss → origin → microservice → EVCache → Cassandra", "Zuul, Eureka, Cassandra, S3, Kafka, EVCache"),
    ("Uber", "Real-time ride matching and pricing", "15M+ trips/day; geo-heavy writes", "AP location, CP payments", [
        ("Mobile", "Rider + driver GPS streams"),
        ("Dispatch", "Geo index, ETA, matching"),
        ("Pricing", "Surge from supply/demand"),
        ("Trip Service", "State machine: requested→completed"),
        ("Payments", "Idempotent charges, wallets"),
        ("Maps", "Routing + traffic APIs"),
    ], "Rider request → geo query drivers → offer → accept → trip stream → payment saga", "Kafka, Redis Geo, PostgreSQL, Cassandra, PostGIS"),
    ("Amazon E-Commerce", "Catalog, cart, checkout, inventory", "Peak Prime Day millions OPS", "CP inventory & payments", [
        ("Storefront", "BFF for web/mobile"),
        ("Product Catalog", "Read-optimized, CDN"),
        ("Cart Service", "Session cart, merge on login"),
        ("Order Pipeline", "Saga: reserve→charge→fulfill"),
        ("Inventory", "Strong consistency per SKU-warehouse"),
        ("Search", "Inverted index + ranking"),
    ], "Browse → add cart → checkout → payment → warehouse allocation → ship events", "DynamoDB, S3, SQS/SNS, Elasticsearch, regional cells"),
    ("Instagram Feed", "Photo/video feed at scale", "2B+ MAU; fan-out heavy", "AP feed, CP for DMs optional", [
        ("Media", "S3 + CDN for images"),
        ("Post Service", "Write post metadata"),
        ("Fan-out Worker", "Push to followers' feeds"),
        ("Feed Cache", "Redis sorted sets per user"),
        ("Graph", "Follow relationships sharded"),
    ], "Post → async fan-out → timeline cache → read precomputed feed", "Cassandra, Redis, Memcached, Kafka, CDN"),
    ("Twitter / X Timeline", "Home timeline + search", "500M+ tweets/day historically", "Hybrid fan-out", [
        ("Tweet Service", "Write path durable log"),
        ("Timeline", "Fan-out on write vs read for celebrities"),
        ("Search", "Earlybird-style index"),
        ("Trending", "Stream processing counts"),
    ], "Tweet → Kafka → fan-out workers OR pull merge for celebs → cache timeline", "Manhattan, Redis, Kafka, Gizzard sharding"),
    ("WhatsApp", "E2E messaging at scale", "100B+ messages/day", "AP delivery, ordering per chat", [
        ("Connection", "WebSocket / MQTT gateways"),
        ("Message Store", "Per-chat log, retention"),
        ("Presence", "Online/offline, last seen"),
        ("Push", "APNs/FCM notification fanout"),
        ("Media", "Encrypted blob storage"),
    ], "Send → gateway → store → push to recipient devices → ack receipts", "Erlang/BEAM style, Cassandra, HBase, custom protocols"),
    ("TikTok / Short Video", "For You feed + upload", "1B+ users; ML ranking core", "AP feed", [
        ("Upload", "Short video ingest"),
        ("Transcode", "Fast vertical formats"),
        ("FYP Ranker", "Real-time features + models"),
        ("Social Graph", "Follow + interest signals"),
        ("CDN", "Edge playback"),
    ], "Upload → transcode → feature extraction → rank pool → serve feed", "Kubernetes, Flink, Redis, object storage, ML platform"),
    ("Spotify", "Music streaming + playlists", "600M+ users", "AP playback metadata", [
        ("Catalog", "Rights-aware track metadata"),
        ("Streaming", "Chunked audio CDN"),
        ("Playlists", "User + collaborative edits"),
        ("Recommendations", "Discover Weekly batch + online"),
        ("Social", "Listening activity (optional)"),
    ], "Play → CDN segment → sync listening state → rec models update", "Google Cloud, Cassandra, Kafka, microservices"),
    ("Airbnb", "Search, book, pay hosts", "Global listings", "CP booking", [
        ("Search", "Geo + filters + ranking"),
        ("Listing", "Photos, calendar availability"),
        ("Booking", "Double-book prevention"),
        ("Payments", "Split payouts, FX"),
        ("Reviews", "Two-sided trust"),
    ], "Search → reserve dates (lock) → pay guest → confirm host → messaging", "MySQL sharded, Elasticsearch, Kafka, Stripe"),
    ("Google Drive", "File sync and sharing", "Trillions of files", "CP metadata, AP sync conflict", [
        ("Sync Client", "Delta uploads, conflict resolution"),
        ("Metadata", "File tree per user"),
        ("Blob Store", "Chunked content-addressed"),
        ("Sharing ACL", "Permission propagation"),
        ("Search", "OCR + full-text index"),
    ], "Change → chunk diff → upload blobs → update metadata → notify collaborators", "Colossus/GFS style, Spanner metadata, Pub/Sub"),
    ("Google Maps", "Tiles, routing, traffic", "Billions of queries/day", "AP tiles, CP routing graphs", [
        ("Tile CDN", "Pre-rendered map tiles"),
        ("Routing", "Graph algorithms + live traffic"),
        ("Places", "POI search index"),
        ("Location", "Snap to road, ETA"),
    ], "Query → geohash tile fetch → route on graph → traffic-weighted ETA", "Bigtable, S2 geometry, distributed graph"),
    ("Stripe Payments", "Payment intents, webhooks", "Millions merchants", "CP money movement", [
        ("API", "Idempotent PaymentIntent"),
        ("Ledger", "Double-entry accounting"),
        ("Risk", "Fraud scoring real-time"),
        ("Connect", "Marketplace splits"),
        ("Webhooks", "At-least-once delivery"),
    ], "Create intent → auth/capture → ledger post → webhook retry queue", "Ruby/Go services, PostgreSQL, Kafka, Redis locks"),
    ("DoorDash / Uber Eats", "Food delivery marketplace", "Millions orders/day", "AP ETA, CP order state", [
        ("Restaurant", "Menu, hours, inventory"),
        ("Order", "State: placed→delivered"),
        ("Dispatch", "Dasher assignment geo"),
        ("Tracking", "Live location stream"),
    ], "Order → pay → match dasher → pickup → dropoff → settle", "Kafka, Redis, PostgreSQL, mobile push"),
    ("LinkedIn Feed", "Professional network feed", "900M+ members", "Fan-out + rank", [
        ("Profile", "Graph of connections"),
        ("Feed Mixer", "Posts + jobs + ads"),
        ("Messaging", "Real-time chat"),
        ("Search", "People + jobs index"),
    ], "Activity → Kafka → aggregation → rank → cache feed", "Espresso, Kafka, Voldemort, Hadoop"),
    ("Slack", "Workspace messaging", "Teams + channels", "AP messages, CP billing", [
        ("Workspace", "Multi-tenant isolation"),
        ("Channels", "Pub/sub per channel"),
        ("Search", "Message index"),
        ("Files", "Virus scan + storage"),
        ("Integrations", "Webhooks, bots"),
    ], "Message → gateway → channel fanout → persist → push/desktop", "Vitess/MySQL, Redis, Solr, S3"),
    ("Zoom", "Video meetings", "Millions concurrent meetings", "AP media, CP scheduling", [
        ("Signaling", "SDP, ICE, room join"),
        ("Media SFU/MCU", "Selective forwarding"),
        ("Recording", "Cloud mix to storage"),
        ("Calendar", "Meeting links"),
    ], "Join room → SFU route streams → adaptive bitrate per client", "AWS, custom UDP, Redis, Cassandra"),
    ("GitHub", "Git hosting + CI", "100M+ repos", "CP git refs", [
        ("Git Storage", "Packfiles, replication"),
        ("Web API", "PRs, issues, actions"),
        ("Actions", "Workflow runners queue"),
        ("Search", "Code search index"),
    ], "Push → receive pack → store → trigger webhooks/CI", "MySQL, Git object storage, Kubernetes workers"),
    ("Reddit", "Subreddit posts + comments", "Hot posts ranking", "AP votes, CP awards money", [
        ("Post Service", "Tree of comments"),
        ("Ranking", "Hot / top algorithms"),
        ("Vote", "Sharded counters"),
        ("Feed", "Subreddit subscriptions"),
    ], "Submit → store → async score → feed materialization", "PostgreSQL, Redis, Kafka, Cassandra"),
    ("Pinterest", "Visual discovery", "Image-heavy", "AP boards", [
        ("Pin", "Image + metadata"),
        ("Visual Search", "Embeddings index"),
        ("Home Feed", "Interest clusters"),
        ("Notification", "Repin events"),
    ], "Pin → CNN embedding → index → recommend similar", "HBase, Kafka, S3, TensorFlow"),
    ("Tinder Matching", "Geo-based swipe matching", "Real-time proximity", "AP discovery", [
        ("Profile", "Photos, preferences"),
        ("Geo Index", "Users within radius"),
        ("Match", "Mutual like detection"),
        ("Chat", "Post-match messaging"),
    ], "Swipe → record like → check mutual → create match channel", "Redis Geo, Cassandra, Kafka"),
    ("Coinbase Exchange", "Order book trading", "High-frequency matching", "CP matching engine", [
        ("API Gateway", "Auth, rate limits"),
        ("Matching Engine", "In-memory order book"),
        ("Wallet", "Hot/cold custody"),
        ("Ledger", "Immutable trade log"),
    ], "Order → match → settle → ledger append → websocket tick", "Kafka, PostgreSQL, in-memory book, HSM"),
    ("URL Shortener (bit.ly)", "Short links + analytics", "Billions redirects/month", "AP redirects", [
        ("Encode", "Base62 hash or counter"),
        ("Redirect", "302 with cache"),
        ("Analytics", "Click stream async"),
    ], "Create → store mapping → redirect lookup from edge cache", "Redis, SQL, CDN, Kafka clicks"),
    ("Pastebin", "Text paste hosting", "Read-heavy", "AP", [
        ("Paste API", "Create with TTL"),
        ("Object Store", "Large pastes"),
        ("CDN", "Popular pastes"),
    ], "POST content → key → GET by key", "S3, SQL metadata, CloudFront"),
    ("Web Crawler (Google)", "Discover and index web", "Trillions pages", "AP crawl frontier", [
        ("Frontier", "Priority URL queue"),
        ("Fetcher", "Politeness per host"),
        ("Parser", "Extract links + text"),
        ("Indexer", "Inverted index build"),
    ], "Seed URLs → fetch → parse → index → PageRank batch", "Bigtable, MapReduce, custom storage"),
    ("Notification System", "Multi-channel delivery", "Millions/sec peaks", "AP at-least-once", [
        ("API", "Template + payload"),
        ("Router", "Email/SMS/push/in-app"),
        ("Queue", "Per-channel workers"),
        ("Preferences", "User opt-in"),
    ], "Event → template render → channel queue → provider → retry DLQ", "Kafka, SQS, Redis, FCM/APNs"),
    ("Distributed Rate Limiter", "API protection", "Millions RPS", "AP counters", [
        ("Edge", "Token bucket local"),
        ("Redis Cluster", "Sliding window global"),
        ("Config", "Rules per API key"),
    ], "Request → check bucket → allow/deny 429", "Redis, Envoy sidecar"),
    ("Google Search", "Query billions of pages", "Sub-second latency", "AP index freshness", [
        ("Query Parser", "Intent, spelling"),
        ("Index Shards", "Inverted index parallel"),
        ("Ranking", "PageRank + ML"),
        ("Snippets", "Cached summaries"),
    ], "Query → shard fanout → merge top-K → rank → SERP", "Bigtable, MapReduce, Spanner ads"),
    ("Ticketmaster", "Concert ticket sales", "Spike traffic", "CP inventory", [
        ("Catalog", "Events, seats"),
        ("Inventory Lock", "Short TTL holds"),
        ("Checkout", "Payment queue"),
        ("Queue IT", "Virtual waiting room"),
    ], "Browse → hold seat → pay → confirm or release", "SQL, Redis locks, Kafka"),
    ("ChatGPT / LLM API", "Inference at scale", "Tokens/sec billing", "AP queueing", [
        ("API Gateway", "Auth, quotas"),
        ("Router", "Model selection"),
        ("GPU Pool", "Batch + streaming inference"),
        ("Context Store", "Conversation state"),
        ("Safety", "Moderation filters"),
    ], "Prompt → queue → GPU worker → stream tokens → log usage", "Kubernetes, vLLM, Redis, object storage"),
    ("Walmart Inventory", "Retail supply chain", "SKU-level accuracy", "CP stock", [
        ("POS Sync", "Store sales events"),
        ("Warehouse", "Pick/pack/ship"),
        ("Forecasting", "Replenishment ML"),
        ("Online OMS", "Order orchestration"),
    ], "Sale → decrement → threshold → replenishment order", "Kafka, SQL, data lake"),
    ("Facebook Social Graph", "Friends, posts, ads", "3B+ users", "AP", [
        ("Graph Store", "TAO-style layer"),
        ("News Feed", "Aggregator + ranker"),
        ("Ads", "Real-time auction"),
        ("Photos", "Haystack blob store"),
    ], "Post → graph fanout → rank → ad insert → deliver", "MySQL, Memcached, Scribe, Hive"),
    ("Apple iCloud", "Device backup + sync", "E2E encryption option", "CP sync metadata", [
        ("Device Sync", "Chunked encrypted backup"),
        ("Metadata", "File catalog"),
        ("CDN", "App/media delivery"),
    ], "Device change → encrypted chunk upload → manifest update", "Object storage, Cassandra, APNS"),
]

LLD = [
    ("Parking Lot", "Multi-floor parking, tickets, payments", "ParkingLot, Floor, Spot, Vehicle, Ticket, PaymentService"),
    ("Elevator System", "Multiple elevators, requests, scheduling", "Building, Elevator, Request, Scheduler (SCAN/LOOK)"),
    ("LRU Cache", "O(1) get/put eviction", "DLL + HashMap; Cache, Node"),
    ("Chess Game", "Rules, turns, checkmate", "Board, Piece hierarchy, Game, Player, MoveValidator"),
    ("Library Management", "Books, members, lending", "Book, Member, Loan, Catalog, FineCalculator"),
    ("ATM Machine", "Withdraw, deposit, PIN", "ATM, Card, Account, Transaction, CashDispenser"),
    ("Vending Machine", "Inventory, coins, change", "VendingMachine, Product, Slot, PaymentProcessor"),
    ("Hotel Booking", "Rooms, reservations", "Hotel, Room, Booking, Guest, AvailabilityService"),
    ("Movie Ticket Booking", "Seats, show, lock", "Cinema, Show, Seat, Booking, SeatLock (TTL)"),
    ("Food Delivery Order", "Restaurant order state", "Order, Item, DeliveryAgent, OrderState enum"),
    ("Snake and Ladder", "Board game simulation", "Board, Player, Dice, Snake, Ladder"),
    ("Deck of Cards", "Shuffle, deal", "Deck, Card, Suit, Rank, Hand"),
    ("Car Rental", "Vehicles, reservations", "Vehicle, Reservation, Customer, PricingStrategy"),
    ("Splitwise", "Expense splitting", "Expense, User, SplitStrategy (equal/exact/percent)"),
    ("Stock Exchange", "Order matching", "OrderBook, Order, Trade, MatchingEngine"),
    ("Logger Framework", "Levels, appenders", "Logger, Appender (File/Console), Formatter, LogLevel"),
    ("Task Scheduler", "Cron-like jobs", "Scheduler, Job, PriorityQueue, WorkerPool"),
    ("In-Memory Pub/Sub", "Topics, subscribers", "Broker, Topic, Subscriber, Message"),
    ("Design Twitter (LLD)", "Tweet, follow, timeline object model", "User, Tweet, TimelineService, GraphRepository"),
    ("Ride Sharing (LLD)", "Trip state for Uber-style", "Rider, Driver, Trip, Location, TripStatus"),
]

def box_diagram(components):
    lines = ["```", "┌─────────────┐     ┌──────────────────┐"]
    lines.append("│   Clients   │────▶│  API / Gateway   │")
    lines.append("└─────────────┘     └────────┬─────────┘")
    n = len(components)
    if n <= 4:
        row = "    ".join(f"┌──▼──┐" for _ in components[:4])
        lines.append("              " + row.replace("▼", "▼")[:60])
    lines.append("              │         Services Layer          │")
    for i, (name, desc) in enumerate(components):
        lines.append(f"              │  • {name}: {desc[:40]}")
    lines.append("              └────────┬────────────────────────┘")
    lines.append("                       │")
    lines.append("         ┌─────────────┼─────────────┐")
    lines.append("         ▼             ▼             ▼")
    lines.append("    ┌─────────┐   ┌─────────┐   ┌─────────┐")
    lines.append("    │ Cache   │   │   DB    │   │  Queue  │")
    lines.append("    └─────────┘   └─────────┘   └─────────┘")
    lines.append("```")
    return "\n".join(lines)

def hld_section(num, name, problem, scale, cap, components, flow, stack):
    slug = name.lower().replace(" ", "-").replace("/", "-")
    return f"""
---

## HLD {num}. {name}

**Problem:** {problem}  
**Scale:** {scale}  
**CAP lean:** {cap}

### Architecture diagram

{box_diagram(components)}

### End-to-end flow

{flow}

### Production-style stack

{stack}

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.

"""

def lld_section(num, name, problem, classes):
    return f"""
---

## LLD {num}. {name}

**Problem:** {problem}

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      {name}                              │
├─────────────────────────────────────────────────────────┤
│ Core types: {classes}                                   │
├─────────────────────────────────────────────────────────┤
│ Patterns: Strategy (pricing/rules), State (workflows),  │
│           Factory (piece/card creation), Observer (events)│
└─────────────────────────────────────────────────────────┘
```

### Responsibilities

| Class / Module | Responsibility |
|----------------|----------------|
| (parse from class list) | See entities above |

### Key operations

1. Define entities and enums (status, type).
2. Encapsulate rules in services (not fat controllers).
3. Expose interfaces for storage and notifications (DIP).
4. Write tests for state transitions and edge cases.

### Real-world link

Companies ask this to test **OOP modeling**, not distributed scale. Connect to HLD: e.g. Parking Lot → mall operator dashboard; Elevator → building management SaaS.

"""

def main():
    parts = ["""# Real-World System Design: 50 End-to-End Examples

> **HLD (32)** — Amazon, YouTube, Uber, Netflix, and global-scale systems with architecture diagrams and flows.  
> **LLD (18)** — Interview-class designs with object models and responsibilities.

Use with **High-Level Design (HLD)** and **Low-Level Design (LLD)** notebooks in the sidebar. For each case: requirements → estimate → diagram → deep dive → trade-offs (45 min).

---

## How to use this guide

| Step | HLD | LLD |
|------|-----|-----|
| 1 | Functional + non-functional requirements | Clarify actors and use cases |
| 2 | QPS, storage, bandwidth estimates | List entities and relationships |
| 3 | Draw boxes: clients, services, data | Classes, interfaces, patterns |
| 4 | One happy-path + one failure path | State machine or sequence for main flow |
| 5 | CAP choice, caching, sharding | SOLID + unit test scenarios |

---

## Part A — High-Level Design (32 systems)

"""]
    for i, args in enumerate(HLD, 1):
        parts.append(hld_section(i, *args))

    parts.append("\n---\n\n## Part B — Low-Level Design (18 systems)\n\n")
    for i, args in enumerate(LLD, 1):
        parts.append(lld_section(i, *args))

    parts.append("""
---

## Quick reference — all 50 topics

| # | System | Type |
|---|--------|------|
""")
    for i, (name, *_) in enumerate(HLD, 1):
        parts.append(f"| {i} | {name} | HLD |\n")
    for i, (name, *_) in enumerate(LLD, 1):
        parts.append(f"| {32 + i} | {name} | LLD |\n")

    parts.append("""
---

## Practice plan (10 weeks)

| Week | Focus | Count |
|------|-------|-------|
| 1–2 | Social & feed (Instagram, Twitter, LinkedIn, Reddit) | 4 HLD |
| 3 | Video (YouTube, Netflix, TikTok, Zoom) | 4 HLD |
| 4 | Marketplaces (Uber, Amazon, Airbnb, DoorDash) | 4 HLD |
| 5 | Messaging (WhatsApp, Slack) + payments (Stripe) | 3 HLD |
| 6 | Infrastructure (URL shortener, crawler, rate limiter, notifications) | 4 HLD |
| 7–8 | LLD classics (parking, elevator, LRU, chess, ATM, vending) | 8 LLD |
| 9 | LLD workflows (hotel, tickets, Splitwise, stock exchange) | 6 LLD |
| 10 | Mock interviews: 1 HLD + 1 LLD per session | 4+4 |

**Next:** Open **System Design Practice Track** for timed prompts and rubrics.
""")

    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} ({len(OUT.read_text())} chars)")

if __name__ == "__main__":
    main()