# Real-World System Design: 50 End-to-End Examples

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

**Tip:** Examples 1–20 are full deep dives (diagrams + flows). Examples 21–33 are compact references for quick review.

---

## HLD 1. YouTube (video platform)

**Requirements:** Upload, transcode, global playback, search, recommendations. Start playback in under 3 seconds.

**Scale:** ~500 hours of video uploaded per minute; billions of daily views; read:write roughly 100:1.

### Architecture diagram

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Web/TV   │  │ Mobile   │  │ Creator  │
│ App      │  │ App      │  │ Studio   │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     └─────────────┼─────────────┘
                   ▼
         ┌─────────────────────┐
         │   API Gateway       │
         │ auth, rate limits   │
         └──────────┬──────────┘
                    │
     ┌──────────────┼──────────────┬─────────────┐
     ▼              ▼              ▼             ▼
┌─────────┐  ┌───────────┐  ┌──────────┐  ┌──────────┐
│ Upload  │  │ Metadata  │  │ Search   │  │ Recommend│
│ Service │  │ Service   │  │ Service  │  │ Service  │
└────┬────┘  └─────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │              │             │
     ▼             ▼              ▼             ▼
┌─────────┐  ┌───────────┐  ┌──────────┐  ┌──────────┐
│ Object  │  │ Cassandra │  │Elastic-  │  │ Feature  │
│ Storage │  │ / SQL     │  │search    │  │ store +  │
│ (raw)   │  │ sharded   │  │          │  │ ML rank  │
└────┬────┘  └───────────┘  └──────────┘  └──────────┘
     │
     ▼
┌─────────────────────────────────────────┐
│ Transcode workers (Kafka consumers)      │
│ 4K → 1080p → 720p → 360p + thumbnails   │
└──────────────────┬──────────────────────┘
                   ▼
         ┌─────────────────────┐
         │ CDN (HLS/DASH)      │
         │ edge segment cache  │
         └─────────────────────┘
```

### End-to-end flow

1. **Upload:** Multipart upload to object storage; resume on failure.  
2. **Transcode:** Job queue produces renditions + thumbnails (parallel workers).  
3. **Metadata:** Write video_id, owner, titles, renditions JSON.  
4. **CDN warm:** Push popular segments to edge; long tail on demand.  
5. **Play:** Client fetches manifest → ABR picks chunk quality from bandwidth.  
6. **Recommend:** Offline batch + online signals (watch history, search).

### Capacity snapshot

| Metric | Estimate |
|--------|----------|
| Upload storage | Hundreds of TB/day (many renditions) |
| Read QPS | Millions (CDN absorbs most) |
| View counts | Eventual consistency OK (AP) |

### Production-style stack

Object storage, Kafka, distributed DB for metadata, Redis hot cache, CDN, search index, ML training + serving.

### Interview deep dives

- **Bottleneck:** Transcode farm and CDN egress on viral videos.  
- **ABR:** HLS/DASH manifests; switch quality without rebuffering.  
- **Viral video:** Separate hot path; regional cache pre-fill.


---

## HLD 2. Netflix (global streaming)

**Requirements:** 4K streaming worldwide, personalized home row, billing, 99.99% playback availability.

**Scale:** 200M+ subscribers; majority of traffic served from edge (Open Connect CDN).

### Architecture diagram

```
┌────────────┐  Smart TV / Mobile / Browser
└──────┬─────┘
       ▼
┌──────────────────┐     ┌─────────────────────┐
│ API Gateway      │────▶│ Microservices       │
│ (Zuul / Envoy)   │     │ User, Playback,     │
└────────┬─────────┘     │ Billing, Catalog    │
         │               └──────────┬──────────┘
         │                          │
         ▼                          ▼
┌──────────────────┐     ┌─────────────────────┐
│ Open Connect CDN │◀────│ Encoding pipeline   │
│ (ISP appliances) │     │ per-title, multi-bit│
└────────┬─────────┘     └──────────┬──────────┘
         │                          │
         ▼                          ▼
   Edge playback              Origin (S3) + Kafka
         │                          │
         └──────────┬───────────────┘
                    ▼
         ┌─────────────────────┐
         │ Cassandra + EVCache│
         │ Recommendations ML │
         └─────────────────────┘
```

### End-to-end flow

1. Client requests title → CDN serves manifest/segments if cached.  
2. On miss, origin + encoding renditions; ABR adjusts bitrate live.  
3. Viewing events → Kafka → recommendation features.  
4. Billing/subscription checks on entitlement (CP path).

### Production-style stack

Open Connect CDN, S3, Cassandra, EVCache (Redis fork), Kafka, Spark/Flink, hundreds of microservices.

### Interview deep dives

- **Per-title encoding** vs fixed ladder — storage vs quality trade-off.  
- **Regional licensing** — geo-fenced catalog.  
- **Chaos engineering** — Simian Army style failure injection.


---

## HLD 3. Uber (ride-sharing)

**Requirements:** Match rider to driver in seconds, live ETA, surge pricing, payments, trip history.

**Scale:** ~15M trips/day; ~300K+ location updates/sec at peak; shard by city/region.

### Architecture diagram

```
┌─────────────┐       ┌─────────────┐
│ Rider App   │       │ Driver App  │
└──────┬──────┘       └──────┬──────┘
       │    WebSocket / gRPC (GPS every ~4s)
       └──────────┬────────────┘
                  ▼
       ┌──────────────────────┐
       │ API + Real-time GW   │
       └──────────┬───────────┘
                  │
    ┌─────────────┼─────────────┬────────────┐
    ▼             ▼             ▼            ▼
┌────────┐  ┌──────────┐  ┌─────────┐  ┌─────────┐
│Dispatch│  │ Pricing  │  │ Trip    │  │ Payment │
│+ Geo   │  │ (surge)  │  │ Service │  │ Service │
└───┬────┘  └────┬─────┘  └────┬────┘  └────┬────┘
    │            │             │            │
    └────────────┴──────┬──────┴────────────┘
                        ▼
              ┌─────────────────┐
              │ Kafka (events)  │
              └────────┬────────┘
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │Redis Geo │  │PostgreSQL│  │Cassandra │
   │/ H3 grid │  │ trips $  │  │ trip log │
   └──────────┘  └──────────┘  └──────────┘
```

### End-to-end flow

1. Rider requests ride → **GEORADIUS** finds drivers (Redis Geo / H3, not full scan).  
2. Dispatch scores ETA, rating, acceptance → ping top N drivers.  
3. First accept → trip state machine; stream location to rider.  
4. Complete → idempotent payment; emit events for analytics.

### Interview deep dives

- **Surge:** demand/supply ratio per geohash, refresh every ~30s.  
- **Driver offline mid-trip:** timeout + reassign.  
- **Same driver double-booking:** optimistic lock on driver status.


---

## HLD 4. Amazon (e-commerce)

**Requirements:** Catalog browse, cart, checkout, inventory accuracy, search, fulfillment.

**Scale:** Prime Day spikes; regional **cells** isolate blast radius.

### Architecture diagram

```
┌────────┐     ┌─────────────┐     ┌─────────────────────────┐
│ Client │────▶│ Storefront  │────▶│ Domain services         │
└────────┘     │ BFF         │     │ Catalog, Cart, Order,   │
               └─────────────┘     │ Inventory, Payment, Ship│
                                   └───────────┬─────────────┘
                                               │
                    ┌──────────────────────────┼──────────────────┐
                    ▼                          ▼                  ▼
            ┌──────────────┐          ┌──────────────┐   ┌──────────────┐
            │ Search index │          │ Inventory DB │   │ Order saga   │
            │ (Elastic)    │          │ (strong per  │   │ SQS steps    │
            │              │          │ SKU-warehouse)│   │ reserve→ship │
            └──────────────┘          └──────────────┘   └──────────────┘
```

### End-to-end flow

1. Browse/search (read-heavy, cached catalog).  
2. Add to cart (session or logged-in merge).  
3. Checkout → **reserve inventory** (CP) → charge → warehouse pick/pack.  
4. Async notifications + shipment tracking events.

### Interview deep dives

- **Overselling:** Distributed locks / conditional writes on stock.  
- **Cart abandonment:** TTL + email recovery.  
- **Flash sales:** Queue or token for hot SKU checkout.


---

## HLD 5. Instagram (social feed)

**Requirements:** Post photos/video, follow graph, home feed, stories; read-heavy (~100:1).

**Scale:** Hundreds of millions of DAU; celebrity accounts with millions of followers.

### Architecture diagram

```
┌────────┐
│ Mobile │───▶ CDN (media) ───▶ S3 object store
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ API Gateway │────▶│ Post Service │────▶│ Fan-out workers │
└─────────────┘     └──────────────┘     │ (Kafka)         │
    │                    │               └────────┬────────┘
    ▼                    ▼                        ▼
┌─────────┐        ┌──────────┐          ┌──────────────┐
│ Graph   │        │ Metadata │          │ Feed cache   │
│ (follow)│        │ Postgres │          │ Redis ZSET   │
└─────────┘        └──────────┘          │ per user     │
                                         └──────────────┘
```

### Fan-out strategies

| Strategy | When | Trade-off |
|----------|------|-----------|
| Fan-out on write | Normal users | Fast read, heavy write |
| Fan-out on read | Celebrities | Cheap write, slow read for celeb posts |
| Hybrid | Production default | Complexity |

### End-to-end flow

Upload media → CDN → write post → fan-out to follower feed caches → home feed read from cache + rank.


---

## HLD 6. Twitter / X (home timeline)

**Requirements:** Post tweets (280 chars), home timeline under 500ms, search, trending, likes/retweets.

**Scale:** ~500M tweets/day (~6K/sec average, ~15K/sec peak); users follow ~200 accounts on average.

### Architecture diagram

```
┌────────┐
│ Client │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ API Gateway │────▶│ Tweet Service│────▶│ Fan-out workers │
└─────────────┘     └──────┬───────┘     │ (async, Kafka)  │
    │                      │             └────────┬────────┘
    ▼                      ▼                      ▼
┌─────────┐          ┌──────────┐          ┌──────────────┐
│ Search  │          │ Cassandra│          │ Timeline     │
│ index   │          │ tweets by│          │ Redis ZSET   │
│         │          │ user_id  │          │ per user_id  │
└─────────┘          └──────────┘          └──────────────┘
```

### Fan-out decision (critical interview topic)

| Author followers | Strategy | Why |
|------------------|----------|-----|
| &lt; ~10K | Fan-out **on write** | Push tweet_id into each follower's timeline cache |
| Celebrity (millions) | Fan-out **on read** | Avoid 50M+ writes per tweet; merge at read time |

### End-to-end flow

**Write:** POST tweet → persist → if normal user, fan-out to follower timeline keys (`ZADD` with timestamp score).  
**Read:** `ZREVRANGE` top N tweet IDs → batch hydrate tweet bodies → fetch celebrity tweets on demand → rank (recency + engagement) → return page.

### Capacity snapshot

| Item | Note |
|------|------|
| Timeline cache | Top ~800 tweet IDs per user in Redis |
| Storage | Partition tweets by `user_id` + time clustering |
| Search | Separate inverted index (Earlybird-style) |

### Production-style stack

Kafka, Cassandra, Redis/Manhattan, custom search, ML ranking (Cortex-style).

### Interview deep dives

- **Celebrity problem:** Hybrid fan-out is the standard answer.  
- **Hot key:** Trending topic → dedicated cache shard.  
- **Consistency:** Likes count eventual consistency is acceptable.


---

## HLD 7. WhatsApp (messaging)

**Requirements:** 1:1 and group chat, delivery/read receipts, media, **end-to-end encryption**, online status.

**Scale:** ~100B messages/day (~1.2M/sec); ~100M concurrent connections at peak.

### Architecture diagram

```
┌──────────────┐     ┌──────────────┐
│ User A phone │     │ User B phone │
└──────┬───────┘     └──────▲───────┘
       │ WebSocket (persistent)      │
       └──────────┬──────────────────┘
                  ▼
       ┌──────────────────────┐
       │ Connection gateway   │
       │ (millions of conns)  │
       └──────────┬───────────┘
                  │
       ┌──────────▼───────────┐
       │ Message router       │
       │ online? push : store │
       └──────────┬───────────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│Cassandra│ │ Redis   │ │ Media   │
│per-chat │ │sessions │ │ S3+CDN  │
│message  │ │presence │ │encrypted│
│log      │ │         │ │blobs    │
└─────────┘ └─────────┘ └─────────┘
```

### End-to-end flow

1. Client encrypts with **Signal protocol** (server sees ciphertext only).  
2. Gateway receives → route by recipient session (socket id from Redis).  
3. If online → deliver on WebSocket; else persist + **FCM/APNs** push.  
4. Recipient ack → update status: sent → delivered → read (blue ticks).

### E2E encryption (must mention in interview)

- Key exchange (X3DH / Double Ratchet) → per-message keys, forward secrecy.  
- Server stores encrypted payload + routing metadata only.

### Group chat (100K+ members)

Fan-out on write to members; batch delivery; message id deduplication; rate limits per sender.

### Production-style stack

Erlang/OTP-style concurrency, Cassandra (messages), Redis (presence), object storage for media.

### Interview deep dives

- **WebSocket vs polling:** Persistent connections for real-time.  
- **Ordering:** Per-`conversation_id` sequence, not global.  
- **Offline sync:** Client queues; delta sync on reconnect.


---

## HLD 8. TikTok (short-video + For You Page)

**Requirements:** Sub-minute vertical video, addictive **For You** feed (not just friends), upload, comments, live.

**Scale:** 1B+ MAU; ranking is the product — billions of impressions/day.

### Architecture diagram

```
┌────────┐
│ Mobile │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ API / Edge  │────▶│ Upload +     │────▶│ Transcode       │
└──────┬──────┘     │ transcode    │     │ (vertical 9:16) │
       │            └──────────────┘     └────────┬────────┘
       │                                         │
       ▼                                         ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ FYP Ranker  │◀────│ Feature      │     │ CDN playback    │
│ (ML online) │     │ store Flink  │     └─────────────────┘
└──────┬──────┘     └──────────────┘
       │
       ▼
┌─────────────┐
│ Candidate  │  → recall (millions) → rank (hundreds) → re-rank (dozens)
│ generation │
└─────────────┘
```

### FYP pipeline (core differentiator vs Instagram)

| Stage | What happens |
|-------|----------------|
| Recall | Pull candidate videos from pools (follow, trending, similar embeddings) |
| Rank | ML model scores watch probability, completion, like |
| Re-rank | Diversity, freshness, policy filters |
| Serve | Cache personalized page; prefetch next videos |

### End-to-end flow

1. **Upload:** Short clip → transcode → CV/NLP features (tags, audio).  
2. **Engagement events:** watch time, skip, like → stream to Flink.  
3. **FYP request:** Build user embedding + context → recall → rank → return 6–10 videos.  
4. **CDN:** Edge serves segments; aggressive prefetch on scroll.

### Production-style stack

Kubernetes, object storage, Flink/Kafka, vector DB for embeddings, GPU inference, global CDN.

### Interview deep dives

- **Cold start:** Explore vs exploit for new users and new creators.  
- **Moderation:** Human + ML before wide distribution.  
- **Latency:** Precompute candidate pools; rank in &lt;100ms where possible.


---

## HLD 9. Spotify (music streaming)

**Requirements:** Stream millions of licensed tracks, playlists, offline mode, Discover Weekly-style recommendations.

**Scale:** 600M+ users; catalog metadata huge; playback is CDN-heavy.

### Architecture diagram

```
┌────────┐
│ Client │ (mobile/desktop)
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ API / Auth  │────▶│ Catalog      │     │ Rights / geo    │
└──────┬──────┘     │ (track meta) │     │ restrictions    │
       │            └──────────────┘     └─────────────────┘
       ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Playback    │────▶│ CDN audio    │     │ Listening       │
│ session     │     │ segments     │     │ history → Kafka │
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                   ▼
                                          ┌─────────────────┐
                                          │ Batch + online  │
                                          │ recommendations │
                                          └─────────────────┘
```

### End-to-end flow

1. Search/browse catalog (metadata DB + cache).  
2. Start play → signed CDN URL for Ogg/AAC chunks.  
3. Heartbeat events (progress, skip) → feature pipeline.  
4. Discover Weekly: offline Spark job → personalized playlist per user.

### Interview deep dives

- **Licensing:** Track availability varies by country — edge checks.  
- **Offline:** Encrypted local cache with DRM constraints.  
- **Collaborative playlists:** CRDT or last-write-wins with versioning.


---

## HLD 10. Airbnb (marketplace)

**Requirements:** Search stays by geo/dates, calendar availability, booking without double-book, host payouts, reviews.

**Scale:** Millions of listings; search read-heavy; booking writes must be **consistent**.

### Architecture diagram

```
┌────────┐
│ Guest  │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Search      │────▶│ Elasticsearch│     │ Ranking ML      │
│ (geo+dates) │     │ + geo index  │     │ (quality, price)│
└──────┬──────┘     └──────────────┘     └─────────────────┘
       ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Booking     │────▶│ Inventory    │     │ Payments        │
│ service     │     │ lock dates   │     │ (Stripe Connect)│
└─────────────┘     │ (CP)         │     └─────────────────┘
                    └──────────────┘
```

### End-to-end flow

1. Search: geospatial query + filters → ranked listing IDs.  
2. Select dates → **transactional lock** on listing calendar row.  
3. Payment hold → confirm booking → notify host → messaging thread.  
4. Post-stay: reviews update trust scores.

### Interview deep dives

- **Double booking:** DB transaction or distributed lock on `(listing_id, date_range)`.  
- **Search freshness:** Index updates on calendar change (near real-time).  
- **Peak travel:** Cache popular cities; queue booking during spikes.


---

## HLD 11. Google Drive (file sync)

**Requirements:** Sync folders across devices, sharing with ACLs, conflict handling, full-text search.

**Scale:** Trillions of files; metadata strongly consistent; blobs content-addressed.

### Architecture diagram

```
┌──────────┐  ┌──────────┐
│ Desktop  │  │ Mobile   │  (sync clients)
└────┬─────┘  └────┬─────┘
     └──────┬──────┘
            ▼
     ┌──────────────┐
     │ Sync API     │ (changelog / revision tokens)
     └──────┬───────┘
            │
     ┌──────▼───────┐     ┌──────────────┐
     │ Metadata     │     │ Blob store   │
     │ (Spanner/SQL)│     │ chunk hashes │
     │ file tree    │     │ dedupe       │
     └──────────────┘     └──────────────┘
```

### End-to-end flow

1. Client computes chunk hashes → upload only changed chunks.  
2. Commit revision in metadata DB (atomic).  
3. Push notification to other clients → pull changelog.  
4. Conflict: keep both versions or last-writer-wins policy per file type.

### Interview deep dives

- **Deduplication:** Same hash = store once (saves exabytes).  
- **Sharing:** ACL graph on folder; propagate read vs edit.  
- **Large files:** Resumable uploads + parallel chunk pipeline.


---

## HLD 12. Google Maps

**Requirements:** Map tiles at all zoom levels, turn-by-turn routing, live traffic, places search, ETA.

**Scale:** Billions of routing queries/day; tiles are immutable and CDN-cached.

### Architecture diagram

```
┌────────┐
│ Client │
└───┬────┘
    ├──────────────────▶ Tile CDN (raster/vector tiles by z/x/y)
    │
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Routing API │────▶│ Road graph   │◀────│ Traffic stream  │
│ A* / CH     │     │ (partitioned)│     │ (probe + mobile)│
└─────────────┘     └──────────────┘     └─────────────────┘
    │
    ▼
┌─────────────┐
│ Places index│ (POI search)
└─────────────┘
```

### End-to-end flow

1. Pan/zoom map → fetch tile pyramid from CDN (cache hit &gt;99%).  
2. Route request → snap to graph → weight edges with traffic → return polyline + ETA.  
3. Reroute on deviation using cached subgraph + live updates.

### Interview deep dives

- **Contraction hierarchies:** Preprocess graph for fast long-distance routing.  
- **S2 cells:** Hilbert curve geospatial indexing.  
- **Traffic:** Blend historical + real-time probe data.


---

## HLD 13. Stripe (payments)

**Requirements:** Accept cards globally, idempotent APIs, refunds, Connect marketplaces, webhooks to merchants.

**Scale:** Millions of businesses; **correctness &gt; availability** for ledger.

### Architecture diagram

```
┌──────────────┐
│ Merchant app │
└──────┬───────┘
       ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Stripe API  │────▶│ PaymentIntent│────▶│ Card networks   │
│ Idempotency │     │ state machine│     │ (Visa/MC)       │
│-Key header  │     └──────┬───────┘     └─────────────────┘
└─────────────┘            │
                           ▼
                    ┌──────────────┐     ┌─────────────────┐
                    │ Ledger       │     │ Webhook worker  │
                    │ double-entry │     │ retry + DLQ     │
                    └──────────────┘     └─────────────────┘
```

### End-to-end flow

1. `POST /v1/payment_intents` with `Idempotency-Key` → create or return same result.  
2. Authorize → capture (or separate steps).  
3. Append immutable ledger entries (debit/credit).  
4. Emit `payment_intent.succeeded` webhook with exponential backoff.

### Interview deep dives

- **Idempotency:** Keys stored 24h; prevents double charge on retry.  
- **Connect:** Split transfers platform → connected accounts.  
- **PCI:** Card data tokenized; merchants never store PAN.


---

## HLD 14. DoorDash / Uber Eats (food delivery)

**Requirements:** Restaurant menus, order placement, dasher/courier dispatch, live tracking, ETA.

**Scale:** Millions of orders/day; three-sided marketplace (customer, restaurant, courier).

### Architecture diagram

```
┌─────────┐   ┌────────────┐   ┌─────────┐
│ Customer│   │ Restaurant │   │ Courier │
└────┬────┘   └─────┬──────┘   └────┬────┘
     └──────────────┼───────────────┘
                    ▼
            ┌───────────────┐
            │ Order service │ (state machine)
            └───────┬───────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
┌───────────┐ ┌─────────┐ ┌──────────┐
│ Dispatch  │ │ Payment │ │ Tracking │
│ geo match │ │         │ │ WebSocket│
└───────────┘ └─────────┘ └──────────┘
```

### Order state machine

`PLACED` → `CONFIRMED` → `PREPARING` → `PICKED_UP` → `DELIVERED` (with cancel/refund branches).

### End-to-end flow

1. Customer pays → restaurant tablet accepts → prep time estimate.  
2. Dispatch assigns courier (minimize wait: food ready ≈ courier arrival).  
3. Live GPS to customer app; push notifications on state changes.  
4. Settle restaurant + courier payouts.

### Interview deep dives

- **Batching:** Stack multiple orders per courier when efficient.  
- **ETA ML:** Features from kitchen load, traffic, distance.  
- **Inventory:** 86 unavailable items in real time.


---

## HLD 15. LinkedIn (professional feed)

**Requirements:** Connection graph, home feed (posts + articles), job recommendations, messaging, search people/jobs.

**Scale:** 900M+ members; feed mixes organic + ads + jobs.

### Architecture diagram

```
┌────────┐
│ Member │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Feed mixer  │◀────│ Activity     │     │ Graph service   │
│ (rank)      │     │ pipeline     │     │ (connections)   │
└──────┬──────┘     │ Kafka        │     └─────────────────┘
       │            └──────────────┘
       ▼
┌─────────────┐     ┌──────────────┐
│ Feed cache  │     │ Job matching │
│ Espresso    │     │ (separate)   │
└─────────────┘     └──────────────┘
```

### End-to-end flow

Connection posts → activity event → fan-out / aggregate → rank with professional signals (company, skills) → blend sponsored content → serve feed.

### Interview deep dives

- **Graph vs feed:** Graph stores edges; feed is materialized view.  
- **Virality:** Influencers use hybrid fan-out like Twitter.  
- **Jobs:** Separate retrieval + learning-to-rank pipeline.


---

## HLD 16. Slack (team messaging)

**Requirements:** Workspaces, channels, DMs, threads, file sharing, search, bots/webhooks.

**Scale:** Enterprise workspaces with 100K+ members in single channels (fan-out heavy).

### Architecture diagram

```
┌────────┐
│ Client │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐
│ Real-time   │────▶│ Channel      │
│ gateway     │     │ message store│
└─────────────┘     │ (sharded)    │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌─────────┐  ┌─────────┐  ┌─────────┐
        │ Search  │  │ Files   │  │ Webhooks│
        │ index   │  │ S3      │  │ to apps │
        └─────────┘  └─────────┘  └─────────┘
```

### End-to-end flow

Post to `#channel` → persist with `workspace_id` + `channel_id` shard key → push to online members → async index for search → trigger integrations.

### Interview deep dives

- **Multi-tenancy:** Hard isolate `workspace_id` in every query.  
- **Large channels:** Read receipts optional; pagination + cursoring.  
- **Compliance:** Retention policies, eDiscovery exports.


---

## HLD 17. Zoom (video meetings)

**Requirements:** Multi-party video, screen share, waiting room, cloud recording, webinar mode.

**Scale:** Millions of concurrent meetings; media is UDP/WebRTC, not HTTP CRUD.

### Architecture diagram

```
┌─────────┐     ┌─────────┐
│ Client A│     │ Client B│ ...
└────┬────┘     └────┬────┘
     │  Signaling (HTTPS/WebSocket)
     └────────┬──────┘
              ▼
       ┌──────────────┐
       │ Signaling    │ SDP offer/answer, ICE
       │ server       │
       └──────┬───────┘
              │ media (UDP)
              ▼
       ┌──────────────┐
       │ SFU          │ selective forward streams
       │ (not full    │ (each user sends 1 uplink)
       │  mesh)       │
       └──────────────┘
```

### SFU vs MCU

| Model | Behavior |
|-------|----------|
| **SFU** | Each client uploads once; server forwards to others (Zoom-style) |
| **MCU** | Server mixes one stream (expensive CPU) |

### End-to-end flow

1. Create meeting → room ID + join tokens.  
2. Clients exchange ICE candidates via signaling.  
3. Media flows through regional SFU cluster.  
4. Recording: compositor writes to object storage.

### Interview deep dives

- **NAT traversal:** STUN/TURN servers.  
- **Packet loss:** FEC, bitrate adaptation.  
- **Webinar:** One-to-many downlink optimization.


---

## HLD 18. GitHub

**Problem:** Git hosting + CI  
**Scale:** 100M+ repos  
**CAP lean:** CP git refs

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Git Storage: Packfiles, replication
              │  • Web API: PRs, issues, actions
              │  • Actions: Workflow runners queue
              │  • Search: Code search index
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Push → receive pack → store → trigger webhooks/CI

### Production-style stack

MySQL, Git object storage, Kubernetes workers

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 19. Reddit

**Problem:** Subreddit posts + comments  
**Scale:** Hot posts ranking  
**CAP lean:** AP votes, CP awards money

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Post Service: Tree of comments
              │  • Ranking: Hot / top algorithms
              │  • Vote: Sharded counters
              │  • Feed: Subreddit subscriptions
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Submit → store → async score → feed materialization

### Production-style stack

PostgreSQL, Redis, Kafka, Cassandra

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 20. Pinterest

**Problem:** Visual discovery  
**Scale:** Image-heavy  
**CAP lean:** AP boards

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Pin: Image + metadata
              │  • Visual Search: Embeddings index
              │  • Home Feed: Interest clusters
              │  • Notification: Repin events
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Pin → CNN embedding → index → recommend similar

### Production-style stack

HBase, Kafka, S3, TensorFlow

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 21. Tinder Matching

**Problem:** Geo-based swipe matching  
**Scale:** Real-time proximity  
**CAP lean:** AP discovery

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Profile: Photos, preferences
              │  • Geo Index: Users within radius
              │  • Match: Mutual like detection
              │  • Chat: Post-match messaging
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Swipe → record like → check mutual → create match channel

### Production-style stack

Redis Geo, Cassandra, Kafka

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 22. Coinbase Exchange

**Problem:** Order book trading  
**Scale:** High-frequency matching  
**CAP lean:** CP matching engine

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • API Gateway: Auth, rate limits
              │  • Matching Engine: In-memory order book
              │  • Wallet: Hot/cold custody
              │  • Ledger: Immutable trade log
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Order → match → settle → ledger append → websocket tick

### Production-style stack

Kafka, PostgreSQL, in-memory book, HSM

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 23. URL Shortener (bit.ly / TinyURL)

**Requirements:** Shorten long URLs, custom aliases, redirects, optional analytics, TTL.

**Scale:** 100M new URLs/month; **10:1 read:write**; redirects must be &lt;100ms.

### Architecture diagram

```
┌────────┐                    ┌────────┐
│ Create │──POST /shorten────▶│ App    │
└────────┘                    │ servers│
                              └───┬────┘
┌────────┐  GET /abc123       │
│ Browser│─────────────────────┤
└────────┘                    │
       ▲                      ▼
       │               ┌──────────────┐
       └─ 302 redirect │ Redis cache  │
                       │ short→long   │
                       └──────┬───────┘
                              │ miss
                              ▼
                       ┌──────────────┐
                       │ SQL / NoSQL  │
                       └──────────────┘
```

### ID generation options

| Method | Pros | Cons |
|--------|------|------|
| Auto-increment + Base62 | Simple, dense | Single DB bottleneck |
| MD5 hash truncated | Distributed | Collision handling |
| Snowflake-style ID | Scalable | Longer keys |

### Capacity (classic interview math)

- Writes: ~40/sec average  
- Reads: ~400/sec  
- 5 years storage: billions of rows → **sharded key-value** + CDN for hot links

### End-to-end flow

**Create:** Generate key → `INSERT` mapping → cache warm.  
**Redirect:** Cache lookup → 302 to long URL → async Kafka event for analytics.

### Interview deep dives

- **Custom alias:** Unique index on alias; reject conflicts.  
- **Expiration:** TTL in DB + cache eviction.  
- **Malware scan:** Async safety check before first redirect.


---

## HLD 24. Pastebin

**Problem:** Text paste hosting  
**Scale:** Read-heavy  
**CAP lean:** AP

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Paste API: Create with TTL
              │  • Object Store: Large pastes
              │  • CDN: Popular pastes
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

POST content → key → GET by key

### Production-style stack

S3, SQL metadata, CloudFront

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 25. Web Crawler (Google-scale)

**Requirements:** Discover URLs, respect `robots.txt`, politeness per host, dedupe, build search index.

**Scale:** Trillions of pages; fetch billions/day; index sharded globally.

### Architecture diagram

```
┌─────────────┐
│ URL frontier│ priority queue (importance, freshness)
└──────┬──────┘
       ▼
┌─────────────┐     ┌──────────────┐
│ Fetcher pool│────▶│ DNS + HTTP   │ rate limit per host
└──────┬──────┘     └──────────────┘
       ▼
┌─────────────┐     ┌──────────────┐
│ Parser      │────▶│ Link extract │
│ (HTML→text) │     │ + dedupe bloom│
└──────┬──────┘     └──────────────┘
       ▼
┌─────────────┐
│ Indexer     │ inverted index shards
└─────────────┘
```

### Politeness

- Max N concurrent requests per domain.  
- Backoff on 429/503.  
- Never overload small sites.

### End-to-end flow

Seed URLs → frontier → fetch → parse text/links → dedupe URL hash → push new links → batch **PageRank** offline → rank in serving.

### Interview deep dives

- **Duplicate detection:** URL canonicalization + content hash.  
- **Freshness:** Recrawl popular pages more often.  
- **Distributed:** Partition frontier by host hash.


---

## HLD 26. Notification System

**Problem:** Multi-channel delivery  
**Scale:** Millions/sec peaks  
**CAP lean:** AP at-least-once

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • API: Template + payload
              │  • Router: Email/SMS/push/in-app
              │  • Queue: Per-channel workers
              │  • Preferences: User opt-in
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Event → template render → channel queue → provider → retry DLQ

### Production-style stack

Kafka, SQS, Redis, FCM/APNs

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 27. Distributed Rate Limiter (Stripe, Twitter APIs)

**Requirements:** Limit requests per user/API key/IP; burst allowed; global accuracy across servers.

**Scale:** Millions RPS; must add &lt;1ms overhead.

### Algorithm comparison

| Algorithm | Behavior | Distributed? |
|-----------|----------|--------------|
| Token bucket | Smooth burst + refill rate | Yes (Redis INCR + TTL) |
| Fixed window | Count per minute | Boundary spike at rollover |
| Sliding window log | Accurate, memory heavy | Redis sorted sets |
| Sliding window counter | Approximate, efficient | Hybrid of fixed windows |

### Architecture diagram

```
Request ──▶ API Gateway / Envoy
              │
              ▼
        ┌─────────────┐
        │ Rate limit  │──▶ Redis cluster (key=user:123:window)
        │ middleware  │
        └─────────────┘
              │ allow
              ▼
        Backend services
```

### End-to-end flow

1. Hash `client_id` → Redis key.  
2. Increment counter in current window (or token decrement).  
3. If over limit → `429 Too Many Requests` + `Retry-After` header.  
4. Optional: local edge cache for coarse pre-filter.

### Interview deep dives

- **Race conditions:** Lua script in Redis for atomic check-and-increment.  
- **Multi-region:** Per-region limits or global Redis with latency trade-off.  
- **Fairness:** Separate buckets per endpoint tier.


---

## HLD 28. Google Search

**Requirements:** Sub-second results, spelling correction, ads, snippets, fresh news.

**Scale:** Index size in hundreds of billions of documents; query fan-out to many shards.

### Architecture diagram

```
User query "best pizza brooklyn"
         ▼
┌─────────────────┐
│ Query processor │ tokenize, spellfix, intent
└────────┬────────┘
         ▼
┌─────────────────┐
│ Index shards    │ parallel posting lists (inverted index)
│ (map-reduce     │
│  built)         │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Ranker          │ PageRank + 200+ ML signals
└────────┬────────┘
         ▼
┌─────────────────┐
│ SERP builder    │ snippets, ads auction, knowledge cards
└─────────────────┘
```

### Inverted index (must explain)

Word → list of `(doc_id, positions, boosts)`.  
Query "pizza" ∩ "brooklyn" → candidate doc set → score.

### End-to-end flow

1. Parse query → select shards by term hash.  
2. Each shard returns top-K doc IDs.  
3. Global merge + learning-to-rank.  
4. Build snippets from cached passage index.

### Interview deep dives

- **Crawling:** Tie to HLD 25 for index freshness.  
- **Ads:** Separate auction (AdWords) with budget pacing.  
- **Autocomplete:** Prefix index separate from full web index.


---

## HLD 29. Ticketmaster (high-spike sales)

**Requirements:** Seat map, temporary holds, payment under flash traffic, anti-bot.

**Scale:** Popular on-sale → millions hit in minutes; inventory must never oversell.

### Architecture diagram

```
┌────────┐
│ Users  │───▶ Virtual waiting room (token queue)
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐
│ Seat map    │────▶│ Hold service │
│ (read cache)│     │ TTL 5–10 min │
└─────────────┘     └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ Checkout     │ CP commit seat
                    └──────────────┘
```

### End-to-end flow

1. User passes queue → receives purchase token.  
2. Select seat → **atomic hold** in DB (`UPDATE ... WHERE status=available`).  
3. Pay within TTL → confirm; else release hold for others.

### Interview deep dives

- **Bots:** CAPTCHA, device fingerprint, rate limits.  
- **Queue-it pattern:** Smooth spike into manageable checkout rate.  
- **DB:** Row-level lock per seat or partition by section.


---

## HLD 30. ChatGPT / LLM API

**Requirements:** Chat completions, streaming tokens, context window, rate limits, safety filters, usage billing.

**Scale:** GPU-bound; queue during spikes; latency SLO for first token (TTFT).

### Architecture diagram

```
┌────────┐
│ Client │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ API Gateway │────▶│ Request      │────▶│ GPU inference   │
│ auth+quota  │     │ router       │     │ pool (vLLM)     │
└─────────────┘     └──────┬───────┘     │ batch + stream  │
                           │             └────────┬────────┘
                           ▼                      │
                    ┌──────────────┐              │ SSE tokens
                    │ Context store│◀─────────────┘
                    │ (conversation)│
                    └──────────────┘
```

### End-to-end flow

1. Validate API key + token budget.  
2. Load conversation context (KV cache on GPU when possible).  
3. Stream completion via SSE/WebSocket.  
4. Log prompt/completion tokens for billing; run moderation on input/output.

### Interview deep dives

- **KV cache:** Reuse prefix across turns for speed.  
- **Routing:** Small model for easy queries, large for hard.  
- **Backpressure:** 429 + queue when GPUs saturated.


---

## HLD 31. Walmart Inventory

**Problem:** Retail supply chain  
**Scale:** SKU-level accuracy  
**CAP lean:** CP stock

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • POS Sync: Store sales events
              │  • Warehouse: Pick/pack/ship
              │  • Forecasting: Replenishment ML
              │  • Online OMS: Order orchestration
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Sale → decrement → threshold → replenishment order

### Production-style stack

Kafka, SQL, data lake

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## HLD 32. Facebook (social graph + feed)

**Requirements:** Friend graph, news feed, photos, Messenger, ads with real-time auction.

**Scale:** 3B+ users; graph edges in trillions; feed ranking central product.

### Architecture diagram

```
┌────────┐
│ User   │
└───┬────┘
    ▼
┌─────────────┐     ┌──────────────┐
│ TAO / Graph │     │ News Feed    │
│ (friends)   │────▶│ aggregator   │
└─────────────┘     └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ Rank + inject│
                    │ ads (auction)│
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ Memcached    │
                    │ feed cache   │
                    └──────────────┘
        Photos ──▶ Haystack blob store + CDN
```

### End-to-end flow

1. User posts → write to DB → fan-out to friends' feed pools.  
2. Reader loads feed → merge stories → ML rank → insert sponsored slots (Vickrey-style auction).  
3. Photos served from blob store; metadata in graph layer.

### Interview deep dives

- **TAO:** Graph queries (friends of friends) optimized vs relational joins.  
- **Ads:** Separate real-time bidding; relevance + bid + quality score.  
- **Consistency:** Feed eventual consistency acceptable; payments/wallet CP.


---

## HLD 33. Apple iCloud

**Problem:** Device backup + sync  
**Scale:** E2E encryption option  
**CAP lean:** CP sync metadata

### Architecture diagram

```
┌─────────────┐     ┌──────────────────┐
│   Clients   │────▶│  API / Gateway   │
└─────────────┘     └────────┬─────────┘
              ┌──▼──┐    ┌──▼──┐    ┌──▼──┐
              │         Services Layer          │
              │  • Device Sync: Chunked encrypted backup
              │  • Metadata: File catalog
              │  • CDN: App/media delivery
              └────────┬────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Cache   │   │   DB    │   │  Queue  │
    └─────────┘   └─────────┘   └─────────┘
```

### End-to-end flow

Device change → encrypted chunk upload → manifest update

### Production-style stack

Object storage, Cassandra, APNS

### Interview deep dives

- **Bottleneck:** Identify hottest path (usually read path or fan-out).
- **Failure:** What happens when cache/DB/partition fails?
- **Evolution:** Start monolith → split by domain → add async where needed.


---

## Part B — Low-Level Design (20 systems)

**Deep dives:** LLD 1–6 and 19–20 (full class models). LLD 7–18 are structured outlines for practice.

---

## LLD 1. Parking Lot (Amazon, Microsoft, Google)

**Requirements:** Multiple floors; spot types (compact, large, handicapped); entry/exit gates; hourly/daily fees; track availability.

### Class diagram

```
ParkingLot
├── floors: List[Floor]
├── entry_gates / exit_gates: List[Gate]
├── park_vehicle(vehicle) → Ticket
├── unpark_vehicle(ticket) → void
└── calculate_fee(ticket) → Money

Floor
├── floor_number: int
├── spots: List[ParkingSpot]
└── find_available_spot(vehicle_type) → ParkingSpot?

ParkingSpot (abstract)
├── spot_id, is_available, parked_vehicle
├── CompactSpot | LargeSpot | HandicappedSpot

Vehicle (abstract)
├── license_plate, vehicle_type
└── Car | Truck | Motorcycle | Van

Ticket
├── ticket_id, entry_time, exit_time, spot, fee

PaymentStrategy (interface)
└── HourlyPayment | DailyPayment | MonthlyPass
```

### End-to-end flow

1. Vehicle enters → gate issues ticket → `find_available_spot` by type.  
2. Mark spot occupied; store ticket ↔ spot mapping.  
3. Exit → compute fee via strategy → payment → free spot.

### Patterns

Singleton (one lot), Factory (vehicles), Strategy (pricing), optional Observer (spot freed).

### Interview follow-ups

- Full lot → waiting queue (PriorityQueue).  
- Reservations → TTL + cron to release.  
- Concurrency → lock per floor or spot row.


---

## LLD 2. Elevator System (Google, Microsoft, Uber)

**Requirements:** Multiple elevators; hall calls (up/down); cabin floor buttons; minimize wait; capacity limits.

### Class diagram

```
ElevatorController
├── elevators: List[Elevator]
├── strategy: SchedulingStrategy
└── assign_elevator(request) → Elevator

Elevator
├── id, current_floor, direction (UP|DOWN|IDLE)
├── requests: PriorityQueue<Request>
├── capacity, current_load
└── move(), open_door(), add_request()

Request
├── source_floor, destination_floor, direction, timestamp

SchedulingStrategy
├── NearestCarStrategy
├── DirectionBasedStrategy (same direction first)
└── LoadBalancingStrategy
```

### SCAN / LOOK algorithm (example)

Elevator at floor 5 going **UP** with requests `[7, 3, 10, 2, 8]`:

1. Serve all UP stops in order: 7 → 8 → 10.  
2. Reverse direction; serve DOWN: 3 → 2.  
Minimizes direction changes (disk-scheduler analogy).

### State machine

`IDLE` → `MOVING_UP` / `MOVING_DOWN` → stop at floor → open/close doors → next request or `IDLE`.

### Interview follow-ups

- Fire alarm → **EmergencyState** (all cars to ground).  
- Morning rush → pre-position cars at lobby.  
- Starvation → max wait time boosts request priority.


---

## LLD 3. LRU Cache (Facebook, Amazon, Google)

**Requirements:** `get(key)` and `put(key, value)` in **O(1)**; evict least-recently-used when at capacity.

### Data structure diagram

```
HashMap<key, Node>          Doubly Linked List (MRU → LRU)
┌─────────────────┐         head ↔ node ↔ node ↔ tail
│ key1 → Node A   │────────▶  A ↔ B ↔ C
│ key2 → Node B   │
└─────────────────┘

Node: { key, value, prev, next }
```

### Operations

| Operation | Steps |
|-----------|--------|
| `get(k)` | Map lookup → move node to head → return value (or -1) |
| `put(k,v)` | If exists: update + move to head. Else: insert at head; if full, remove `tail` from list + map |

### Class design

```
class LRUCache:
    capacity: int
    map: Dict[K, Node]
    head, tail: Node

    get(key) -> value
    put(key, value) -> void
    _remove(node)
    _add_to_head(node)
```

### Interview follow-ups

- **Thread safety:** `ConcurrentHashMap` + lock striping or single lock.  
- **Distributed LRU:** Redis with `maxmemory-policy allkeys-lru` (approximate).  
- **TTL variant:** Store expiry per node; lazy delete on access.


---

## LLD 4. Chess Game (Amazon, Google)

**Requirements:** 8×8 board, two players, legal moves per piece, check/checkmate, turn enforcement.

### Class diagram

```
ChessGame
├── board: Board (8×8)
├── white, black: Player
├── current_turn: Color
├── status: ACTIVE | CHECK | CHECKMATE | STALEMATE
└── make_move(from, to) → bool

Board
└── cells[8][8]: Piece?

Piece (abstract)
├── color, position
└── get_valid_moves(board) → List[Move]
    ├── King, Queen, Rook, Bishop, Knight, Pawn

MoveValidator
└── is_valid(game, move), is_in_check(color), is_checkmate(color)
```

### End-to-end flow

1. `make_move` → piece-specific rules → path not blocked → not leaving king in check.  
2. Switch turn; detect check → only allow escape moves.  
3. No legal moves + in check → checkmate.

### Patterns

**Factory** for piece creation; **State** optional for game status; strategy per piece type for movement rules.

### Interview follow-ups

- Castling, en passant, pawn promotion as special cases.  
- Undo move: move history stack.  
- Online play: separate **GameService** from rules engine (HLD: matchmaking service).


---

## LLD 5. Library Management

**Problem:** Books, members, lending

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Library Management                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Book, Member, Loan, Catalog, FineCalculator                                   │
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


---

## LLD 6. ATM Machine

**Requirements:** Insert card, PIN auth, withdraw, deposit, balance, dispense cash, print receipt.

### Class diagram

```
ATM
├── card_reader, keypad, screen, cash_dispenser, printer
├── current_session: Session?
└── start_session(card) / end_session()

Session
├── account: Account (via bank API)
├── authenticate(pin) → bool
└── withdraw(amount) | deposit(amount) | get_balance()

BankService (interface)
└── validate_pin, debit, credit, get_balance

Transaction
├── id, type, amount, timestamp, status
```

### State machine

`IDLE` → `CARD_INSERTED` → `AUTHENTICATED` → (`TRANSACTION`) → `IDLE`  
Wrong PIN 3× → capture card.

### Interview follow-ups

- **Singleton** ATM hardware controller.  
- **Chain of responsibility** for transaction logging.  
- HLD: Bank core is CP; ATM is edge with offline queue (limited).


---

## LLD 7. Vending Machine

**Problem:** Inventory, coins, change

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Vending Machine                              │
├─────────────────────────────────────────────────────────┤
│ Core types: VendingMachine, Product, Slot, PaymentProcessor                                   │
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


---

## LLD 8. Hotel Booking

**Problem:** Rooms, reservations

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Hotel Booking                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Hotel, Room, Booking, Guest, AvailabilityService                                   │
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


---

## LLD 9. Movie Ticket Booking

**Problem:** Seats, show, lock

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Movie Ticket Booking                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Cinema, Show, Seat, Booking, SeatLock (TTL)                                   │
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


---

## LLD 10. Food Delivery Order

**Problem:** Restaurant order state

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Food Delivery Order                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Order, Item, DeliveryAgent, OrderState enum                                   │
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


---

## LLD 11. Snake and Ladder

**Problem:** Board game simulation

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Snake and Ladder                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Board, Player, Dice, Snake, Ladder                                   │
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


---

## LLD 12. Deck of Cards

**Problem:** Shuffle, deal

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Deck of Cards                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Deck, Card, Suit, Rank, Hand                                   │
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


---

## LLD 13. Car Rental

**Problem:** Vehicles, reservations

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Car Rental                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Vehicle, Reservation, Customer, PricingStrategy                                   │
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


---

## LLD 14. Splitwise

**Problem:** Expense splitting

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Splitwise                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Expense, User, SplitStrategy (equal/exact/percent)                                   │
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


---

## LLD 15. Stock Exchange

**Problem:** Order matching

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Stock Exchange                              │
├─────────────────────────────────────────────────────────┤
│ Core types: OrderBook, Order, Trade, MatchingEngine                                   │
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


---

## LLD 16. Logger Framework

**Problem:** Levels, appenders

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Logger Framework                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Logger, Appender (File/Console), Formatter, LogLevel                                   │
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


---

## LLD 17. Task Scheduler

**Problem:** Cron-like jobs

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      Task Scheduler                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Scheduler, Job, PriorityQueue, WorkerPool                                   │
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


---

## LLD 18. In-Memory Pub/Sub

**Problem:** Topics, subscribers

### Class diagram (conceptual)

```
┌─────────────────────────────────────────────────────────┐
│                      In-Memory Pub/Sub                              │
├─────────────────────────────────────────────────────────┤
│ Core types: Broker, Topic, Subscriber, Message                                   │
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


---

## LLD 19. Twitter (object model — pairs with HLD 6)

**Requirements:** Post tweet, follow user, build home timeline (in-memory or service boundaries).

### Class diagram

```
User
├── user_id, name
└── followers, following: Set<user_id>

Tweet
├── tweet_id, author_id, text, created_at
└── like(), retweet()

TimelineService
├── post_tweet(user, text)
├── get_home_timeline(user_id, page) → List[Tweet]
└── FanoutStrategy (interface)
    ├── FanoutOnWrite
    └── FanoutOnRead (for celebrities)

GraphRepository
├── follow(a,b), unfollow(a,b)
└── get_followers(user_id)
```

### How LLD connects to HLD 6

- **LLD:** Clean classes and fan-out strategy interface.  
- **HLD:** Redis/Cassandra/Kafka at scale — same boundaries, different storage.

### Interview follow-ups

- `get_home_timeline`: merge cached IDs + fetch celebrity tweets.  
- Pagination: cursor = last tweet_id score.


---

## LLD 20. Ride Sharing (pairs with HLD 3 Uber)

### Class diagram

```
Rider, Driver
├── id, name, rating
└── location: Location (lat, lon)

Trip
├── trip_id, rider, driver?
├── status: REQUESTED | ACCEPTED | IN_PROGRESS | COMPLETED | CANCELLED
├── fare: Money
└── accept(driver), start(), complete(), cancel()

DispatchService
├── find_drivers(location, radius) → List[Driver]
└── assign_driver(trip) → Driver

PricingService
└── calculate_fare(distance, time, surge_multiplier)

LocationService
└── update_driver_location(driver_id, loc)
```

### Trip state machine

```
REQUESTED → ACCEPTED → IN_PROGRESS → COMPLETED
     ↓           ↓
 CANCELLED   CANCELLED
```

### Interview follow-ups

- **Observer:** Notify rider on status change.  
- **Strategy:** Surge pricing plug-in.  
- HLD 3 adds geo-index, Kafka, payment idempotency.


---

## Quick reference — all 50 topics

| # | System | Type |
|---|--------|------|
| 1 | YouTube | HLD |
| 2 | Netflix | HLD |
| 3 | Uber | HLD |
| 4 | Amazon E-Commerce | HLD |
| 5 | Instagram Feed | HLD |
| 6 | Twitter / X Timeline | HLD |
| 7 | WhatsApp | HLD |
| 8 | TikTok / Short Video | HLD |
| 9 | Spotify | HLD |
| 10 | Airbnb | HLD |
| 11 | Google Drive | HLD |
| 12 | Google Maps | HLD |
| 13 | Stripe Payments | HLD |
| 14 | DoorDash / Uber Eats | HLD |
| 15 | LinkedIn Feed | HLD |
| 16 | Slack | HLD |
| 17 | Zoom | HLD |
| 18 | GitHub | HLD |
| 19 | Reddit | HLD |
| 20 | Pinterest | HLD |
| 21 | Tinder Matching | HLD |
| 22 | Coinbase Exchange | HLD |
| 23 | URL Shortener (bit.ly) | HLD |
| 24 | Pastebin | HLD |
| 25 | Web Crawler (Google) | HLD |
| 26 | Notification System | HLD |
| 27 | Distributed Rate Limiter | HLD |
| 28 | Google Search | HLD |
| 29 | Ticketmaster | HLD |
| 30 | ChatGPT / LLM API | HLD |
| 31 | Walmart Inventory | HLD |
| 32 | Facebook Social Graph | HLD |
| 33 | Apple iCloud | HLD |
| 33 | Parking Lot | LLD |
| 34 | Elevator System | LLD |
| 35 | LRU Cache | LLD |
| 36 | Chess Game | LLD |
| 37 | Library Management | LLD |
| 38 | ATM Machine | LLD |
| 39 | Vending Machine | LLD |
| 40 | Hotel Booking | LLD |
| 41 | Movie Ticket Booking | LLD |
| 42 | Food Delivery Order | LLD |
| 43 | Snake and Ladder | LLD |
| 44 | Deck of Cards | LLD |
| 45 | Car Rental | LLD |
| 46 | Splitwise | LLD |
| 47 | Stock Exchange | LLD |
| 48 | Logger Framework | LLD |
| 49 | Task Scheduler | LLD |
| 50 | In-Memory Pub/Sub | LLD |
| 51 | Design Twitter (LLD) | LLD |
| 52 | Ride Sharing (LLD) | LLD |

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
