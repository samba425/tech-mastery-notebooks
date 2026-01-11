# Event-Driven Architecture: Zero to Hero Guide
## Complete Modern Event-Driven Systems Mastery

---

## 📚 Table of Contents

1. [Introduction to Event-Driven Architecture](#introduction)
2. [Core Concepts & Fundamentals](#fundamentals)
3. [Event Design Patterns](#patterns)
4. [Message Brokers Deep Dive](#brokers)
5. [Apache Kafka Mastery](#kafka)
6. [RabbitMQ Complete Guide](#rabbitmq)
7. [Event Sourcing](#event-sourcing)
8. [CQRS Pattern](#cqrs)
9. [Saga Pattern](#saga)
10. [Event Streaming & Real-time Processing](#streaming)
11. [Microservices Event Communication](#microservices)
12. [Testing Event-Driven Systems](#testing)
13. [Monitoring & Observability](#monitoring)
14. [Security & Best Practices](#security)
15. [Real-World Projects](#projects)

---

## 🎯 Introduction to Event-Driven Architecture {#introduction}

### What is Event-Driven Architecture (EDA)?

**Event-Driven Architecture** is a software design pattern where the flow of the application is determined by events - state changes, user actions, sensor outputs, or messages from other systems.

```
Traditional Request-Response
┌─────────┐     Request     ┌─────────┐     Request     ┌─────────┐
│Client A │ ──────────────▶ │Service B│ ──────────────▶ │Service C│
└─────────┘                 └─────────┘                 └─────────┘
     ▲                                                         │
     │                       Response                          │
     └─────────────────────────────────────────────────────────┘

Event-Driven Architecture
┌─────────┐     Event       ┌─────────────────┐     Event      ┌─────────┐
│Service A│ ──────────────▶ │  Event Broker   │ ─────────────▶ │Service B│
└─────────┘                 │   (Kafka/      │                └─────────┘
                            │   RabbitMQ)    │                      │
                            └─────────────────┘                      │
                                     │                               │
                                     ▼                               ▼
                               ┌─────────┐                     ┌─────────┐
                               │Service C│                     │Service D│
                               └─────────┘                     └─────────┘
```

### Why Event-Driven Architecture?

**Benefits**:
- ✅ **Loose Coupling**: Services don't know about each other directly
- ✅ **Scalability**: Handle millions of events per second
- ✅ **Resilience**: Failure in one service doesn't crash others
- ✅ **Real-time Processing**: Immediate response to business events
- ✅ **Extensibility**: Easy to add new consumers without changing producers
- ✅ **Audit Trail**: Complete history of all system events

**Use Cases**:
- E-commerce order processing
- Financial transaction processing
- IoT sensor data processing
- User activity tracking
- Real-time analytics and monitoring
- Microservices communication

### Event-Driven vs Traditional Architecture

```
┌─────────────────────────────────────────────────────────┐
│           Traditional Synchronous                      │
├─────────────────────────────────────────────────────────┤
│  Pros:                          Cons:                   │
│  ✅ Simple to understand        ❌ Tight coupling       │
│  ✅ Immediate consistency       ❌ Poor scalability     │
│  ✅ Easy debugging              ❌ Single point failure │
│  ✅ Transactional integrity     ❌ Blocking operations  │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│           Event-Driven Asynchronous                    │
├─────────────────────────────────────────────────────────┤
│  Pros:                          Cons:                   │
│  ✅ Loose coupling              ❌ Eventual consistency │
│  ✅ High scalability            ❌ Complex debugging    │
│  ✅ Fault tolerance             ❌ Message ordering     │
│  ✅ Real-time processing        ❌ Duplicate handling   │
│  ✅ Easy to extend              ❌ Complex transactions │
└─────────────────────────────────────────────────────────┘
```

---

## 📐 Core Concepts & Fundamentals {#fundamentals}

### Event Components

**1. Events**
```javascript
// Domain Event Example
{
  "eventId": "evt_12345678",
  "eventType": "OrderPlaced",
  "eventVersion": "1.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "source": "order-service",
  "data": {
    "orderId": "ORD-001",
    "customerId": "CUST-123",
    "items": [
      {
        "productId": "PROD-456",
        "quantity": 2,
        "price": 29.99
      }
    ],
    "totalAmount": 59.98,
    "currency": "USD"
  },
  "metadata": {
    "correlationId": "corr_87654321",
    "userId": "user_999",
    "traceId": "trace_555"
  }
}
```

**2. Event Types**

```
┌─────────────────────────────────────────────────────┐
│                Domain Events                        │
├─────────────────────────────────────────────────────┤
│  • Business state changes                           │
│  • Examples: OrderPlaced, UserRegistered,          │
│    PaymentProcessed                                 │
│  • Past tense naming                                │
│  • Immutable once published                        │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│               Integration Events                     │
├─────────────────────────────────────────────────────┤
│  • System-to-system communication                  │
│  • Examples: UserSyncRequired, DataExportReady     │
│  • Technical events for integration                │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│               Notification Events                    │
├─────────────────────────────────────────────────────┤
│  • User notifications and alerts                   │
│  • Examples: EmailSent, NotificationDelivered      │
│  • Usually terminal events                         │
└─────────────────────────────────────────────────────┘
```

### Event Flow Patterns

**1. Publish-Subscribe (Pub/Sub)**

```
Publisher ──────┐
                ▼
              ┌─────────┐
              │ Message │
              │ Broker  │
              └─────────┘
                │   │   │
                ▼   ▼   ▼
        Subscriber A B C
```

**2. Event Streaming**

```
Events Flow ────▶ ┌─────────┐ ────▶ Consumer 1
                  │ Stream  │ 
                  │ Broker  │ ────▶ Consumer 2
                  └─────────┘
                      │
                      ▼ (Persistent Log)
                  Event History
```

**3. Message Queuing**

```
Producer ────▶ ┌─────────┐ ────▶ Consumer
               │  Queue  │
               │ (FIFO)  │ ────▶ Consumer
               └─────────┘
```

### Event Delivery Guarantees

```
┌─────────────────────────────────────────────────────┐
│            At-Most-Once                             │
├─────────────────────────────────────────────────────┤
│  • Message delivered 0 or 1 times                  │
│  • No duplicates, but possible message loss        │
│  • Use for: Non-critical data, telemetry          │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│            At-Least-Once                            │
├─────────────────────────────────────────────────────┤
│  • Message delivered 1 or more times               │
│  • No message loss, but possible duplicates        │
│  • Use for: Critical data with idempotent consumers │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│            Exactly-Once                             │
├─────────────────────────────────────────────────────┤
│  • Message delivered exactly 1 time                │
│  • No duplicates, no message loss                  │
│  • Use for: Financial transactions, critical data  │
│  • Most complex to implement                       │
└─────────────────────────────────────────────────────┘
```

---

## 🎨 Event Design Patterns {#patterns}

### 1. Event Notification Pattern

**Purpose**: Notify other systems that something interesting happened.

```javascript
// Publisher (Order Service)
class OrderService {
  async createOrder(orderData) {
    try {
      // Create order
      const order = await this.repository.create(orderData)
      
      // Publish event notification
      await this.eventPublisher.publish('order.created', {
        eventId: uuid(),
        eventType: 'OrderCreated',
        timestamp: new Date().toISOString(),
        data: {
          orderId: order.id,
          customerId: order.customerId,
          totalAmount: order.totalAmount
        }
      })
      
      return order
      
    } catch (error) {
      // Publish failure event
      await this.eventPublisher.publish('order.creation.failed', {
        eventId: uuid(),
        eventType: 'OrderCreationFailed',
        timestamp: new Date().toISOString(),
        data: {
          customerId: orderData.customerId,
          error: error.message
        }
      })
      throw error
    }
  }
}

// Subscriber (Email Service)
class EmailService {
  async handleOrderCreated(event) {
    const { orderId, customerId } = event.data
    
    // Get customer details
    const customer = await this.customerService.getCustomer(customerId)
    
    // Send confirmation email
    await this.emailSender.send({
      to: customer.email,
      subject: `Order Confirmation - ${orderId}`,
      template: 'order-confirmation',
      data: { order: event.data, customer }
    })
    
    console.log(`Order confirmation email sent for ${orderId}`)
  }
}
```

### 2. Event-Carried State Transfer

**Purpose**: Include enough data in the event so consumers don't need to call back.

```javascript
// Rich event with complete data
{
  "eventType": "CustomerUpdated",
  "eventId": "evt_98765",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "customerId": "CUST-123",
    "changes": {
      "email": {
        "oldValue": "old@example.com",
        "newValue": "new@example.com"
      },
      "address": {
        "oldValue": {
          "street": "123 Old St",
          "city": "Old City"
        },
        "newValue": {
          "street": "456 New Ave", 
          "city": "New City"
        }
      }
    },
    // Include current complete state
    "currentState": {
      "customerId": "CUST-123",
      "name": "John Doe",
      "email": "new@example.com",
      "phone": "+1-555-0123",
      "address": {
        "street": "456 New Ave",
        "city": "New City",
        "zipCode": "12345"
      },
      "preferences": {
        "newsletter": true,
        "smsNotifications": false
      }
    }
  }
}

// Consumer can process without additional calls
class ReportingService {
  async handleCustomerUpdated(event) {
    const { customerId, currentState, changes } = event.data
    
    // Update local cache with complete customer state
    await this.customerCache.set(customerId, currentState)
    
    // Log changes for audit
    await this.auditLog.record({
      entity: 'customer',
      entityId: customerId,
      changes: changes,
      timestamp: event.timestamp
    })
    
    // No need to call customer service!
  }
}
```

### 3. Event Sourcing Pattern

**Purpose**: Store all changes as events, derive current state by replaying events.

```javascript
class EventStore {
  constructor() {
    this.events = new Map() // In production: use database
  }
  
  async append(streamId, events) {
    if (!this.events.has(streamId)) {
      this.events.set(streamId, [])
    }
    
    const stream = this.events.get(streamId)
    
    // Add version numbers to events
    events.forEach((event, index) => {
      event.version = stream.length + index + 1
      event.streamId = streamId
      event.timestamp = event.timestamp || new Date().toISOString()
    })
    
    stream.push(...events)
    return events[events.length - 1].version
  }
  
  async getEvents(streamId, fromVersion = 0) {
    const stream = this.events.get(streamId) || []
    return stream.filter(event => event.version > fromVersion)
  }
  
  async getAllEvents() {
    const allEvents = []
    for (const [streamId, events] of this.events) {
      allEvents.push(...events)
    }
    return allEvents.sort((a, b) => a.timestamp.localeCompare(b.timestamp))
  }
}

class OrderAggregate {
  constructor(orderId) {
    this.orderId = orderId
    this.version = 0
    this.status = 'draft'
    this.items = []
    this.totalAmount = 0
    this.customerId = null
    this.uncommittedEvents = []
  }
  
  // Command handlers that produce events
  create(customerId, items) {
    if (this.version > 0) {
      throw new Error('Order already exists')
    }
    
    const event = {
      eventType: 'OrderCreated',
      data: {
        orderId: this.orderId,
        customerId,
        items,
        totalAmount: items.reduce((sum, item) => sum + item.price * item.quantity, 0)
      }
    }
    
    this.applyEvent(event)
    this.uncommittedEvents.push(event)
  }
  
  addItem(productId, quantity, price) {
    if (this.status !== 'draft') {
      throw new Error('Cannot add items to non-draft order')
    }
    
    const event = {
      eventType: 'ItemAdded',
      data: {
        orderId: this.orderId,
        productId,
        quantity,
        price
      }
    }
    
    this.applyEvent(event)
    this.uncommittedEvents.push(event)
  }
  
  confirm() {
    if (this.status !== 'draft') {
      throw new Error('Order not in draft status')
    }
    
    if (this.items.length === 0) {
      throw new Error('Cannot confirm empty order')
    }
    
    const event = {
      eventType: 'OrderConfirmed',
      data: {
        orderId: this.orderId,
        confirmedAt: new Date().toISOString()
      }
    }
    
    this.applyEvent(event)
    this.uncommittedEvents.push(event)
  }
  
  // Event handlers that update state
  applyEvent(event) {
    switch (event.eventType) {
      case 'OrderCreated':
        this.customerId = event.data.customerId
        this.items = [...event.data.items]
        this.totalAmount = event.data.totalAmount
        this.status = 'draft'
        break
        
      case 'ItemAdded':
        this.items.push({
          productId: event.data.productId,
          quantity: event.data.quantity,
          price: event.data.price
        })
        this.totalAmount += event.data.price * event.data.quantity
        break
        
      case 'OrderConfirmed':
        this.status = 'confirmed'
        break
        
      default:
        console.warn(`Unknown event type: ${event.eventType}`)
    }
    
    this.version = event.version || this.version + 1
  }
  
  // Rebuild state from events
  static async fromHistory(orderId, eventStore) {
    const events = await eventStore.getEvents(`order-${orderId}`)
    const order = new OrderAggregate(orderId)
    
    events.forEach(event => order.applyEvent(event))
    
    return order
  }
  
  // Save uncommitted events
  async save(eventStore) {
    if (this.uncommittedEvents.length === 0) return
    
    await eventStore.append(`order-${this.orderId}`, this.uncommittedEvents)
    this.uncommittedEvents = []
  }
}

// Usage example
const eventStore = new EventStore()

// Create new order
const order = new OrderAggregate('ORD-001')
order.create('CUST-123', [
  { productId: 'PROD-1', quantity: 2, price: 29.99 }
])
order.addItem('PROD-2', 1, 49.99)
order.confirm()

// Save events
await order.save(eventStore)

// Rebuild from events later
const rebuiltOrder = await OrderAggregate.fromHistory('ORD-001', eventStore)
console.log('Rebuilt order status:', rebuiltOrder.status)
console.log('Rebuilt order total:', rebuiltOrder.totalAmount)
```

### 4. Event Choreography vs Orchestration

**Choreography (Decentralized)**

```javascript
// Each service knows what to do when events happen
class PaymentService {
  async handleOrderConfirmed(event) {
    const { orderId, totalAmount, customerId } = event.data
    
    try {
      // Process payment
      const payment = await this.processPayment(customerId, totalAmount)
      
      // Publish success event
      await this.eventPublisher.publish('payment.processed', {
        eventType: 'PaymentProcessed',
        data: {
          orderId,
          paymentId: payment.id,
          amount: totalAmount,
          status: 'successful'
        }
      })
      
    } catch (error) {
      // Publish failure event
      await this.eventPublisher.publish('payment.failed', {
        eventType: 'PaymentFailed',
        data: {
          orderId,
          amount: totalAmount,
          error: error.message
        }
      })
    }
  }
}

class InventoryService {
  async handleOrderConfirmed(event) {
    const { orderId, items } = event.data
    
    try {
      // Reserve inventory
      await this.reserveInventory(items)
      
      await this.eventPublisher.publish('inventory.reserved', {
        eventType: 'InventoryReserved',
        data: { orderId, items }
      })
      
    } catch (error) {
      await this.eventPublisher.publish('inventory.reservation.failed', {
        eventType: 'InventoryReservationFailed', 
        data: { orderId, items, error: error.message }
      })
    }
  }
}
```

**Orchestration (Centralized)**

```javascript
class OrderProcessOrchestrator {
  async handleOrderConfirmed(event) {
    const { orderId, customerId, items, totalAmount } = event.data
    
    try {
      // Step 1: Reserve inventory
      const inventoryResult = await this.inventoryService.reserve(items)
      
      if (!inventoryResult.success) {
        throw new Error(`Inventory reservation failed: ${inventoryResult.error}`)
      }
      
      // Step 2: Process payment
      const paymentResult = await this.paymentService.charge(customerId, totalAmount)
      
      if (!paymentResult.success) {
        // Compensate: Release inventory
        await this.inventoryService.release(items)
        throw new Error(`Payment failed: ${paymentResult.error}`)
      }
      
      // Step 3: Ship order
      const shippingResult = await this.shippingService.ship(orderId)
      
      if (!shippingResult.success) {
        // Compensate: Refund and release inventory
        await this.paymentService.refund(paymentResult.paymentId)
        await this.inventoryService.release(items)
        throw new Error(`Shipping failed: ${shippingResult.error}`)
      }
      
      // Success: Publish completion event
      await this.eventPublisher.publish('order.processing.completed', {
        eventType: 'OrderProcessingCompleted',
        data: {
          orderId,
          paymentId: paymentResult.paymentId,
          shippingId: shippingResult.shippingId
        }
      })
      
    } catch (error) {
      await this.eventPublisher.publish('order.processing.failed', {
        eventType: 'OrderProcessingFailed',
        data: { orderId, error: error.message }
      })
    }
  }
}
```

---

## 📨 Message Brokers Deep Dive {#brokers}

### Broker Comparison

```
┌─────────────────────────────────────────────────────────┐
│                    Apache Kafka                         │
├─────────────────────────────────────────────────────────┤
│  • High throughput, low latency                        │
│  • Horizontal scaling                                   │
│  • Event streaming & replay                             │
│  • Complex setup                                        │
│  • Best for: High-volume, real-time data              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                     RabbitMQ                           │
├─────────────────────────────────────────────────────────┤
│  • Easy to use, flexible routing                      │
│  • Rich feature set                                    │
│  • Good for traditional messaging                      │
│  • Limited scalability                                 │
│  • Best for: Complex routing, moderate volume          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                   Amazon SQS/SNS                       │
├─────────────────────────────────────────────────────────┤
│  • Fully managed, serverless                          │
│  • High availability                                   │
│  • Good integration with AWS                           │
│  • Limited features                                    │
│  • Best for: AWS-native applications                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                    Apache Pulsar                       │
├─────────────────────────────────────────────────────────┤
│  • Multi-tenancy support                               │
│  • Geo-replication                                     │
│  • Unified messaging & streaming                       │
│  • Relatively new                                      │
│  • Best for: Multi-tenant, geo-distributed apps       │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Apache Kafka Mastery {#kafka}

### Kafka Architecture Deep Dive

```
┌─────────────────────────────────────────────────────────────────┐
│                        Kafka Cluster                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  Broker 1   │  │  Broker 2   │  │  Broker 3   │             │
│  │  (Leader)   │  │ (Follower)  │  │ (Follower)  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                     │
│         ▼                ▼                ▼                     │
│    Topic: orders    Topic: users    Topic: payments            │
│    ┌─────────┐     ┌─────────┐     ┌─────────┐                 │
│    │Part 0   │     │Part 0   │     │Part 0   │                 │
│    │Part 1   │     │Part 1   │     │Part 1   │                 │
│    │Part 2   │     │Part 2   │     │Part 2   │                 │
│    └─────────┘     └─────────┘     └─────────┘                 │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                    ┌─────────────────┐
                    │    ZooKeeper    │
                    │   (Metadata)    │
                    └─────────────────┘
```

### Advanced Kafka Producer

```python
from kafka import KafkaProducer
from kafka.partitioner import RoundRobinPartitioner, Murmur2Partitioner
import json
import time
import logging
from datetime import datetime
from typing import Dict, Any, Optional, Callable
import uuid
import hashlib

class AdvancedKafkaProducer:
    def __init__(self, 
                 bootstrap_servers: list,
                 client_id: str = "advanced-producer",
                 acks: str = "all",
                 retries: int = 10,
                 batch_size: int = 16384,
                 linger_ms: int = 10,
                 compression_type: str = "snappy",
                 enable_idempotence: bool = True):
        
        self.logger = logging.getLogger(__name__)
        
        # Producer configuration for high reliability and performance
        config = {
            'bootstrap_servers': bootstrap_servers,
            'client_id': client_id,
            'acks': acks,  # 'all' = wait for all replicas
            'retries': retries,
            'max_in_flight_requests_per_connection': 5,
            'enable_idempotence': enable_idempotence,
            'batch_size': batch_size,
            'linger_ms': linger_ms,
            'compression_type': compression_type,
            'buffer_memory': 33554432,  # 32MB
            'key_serializer': lambda k: k.encode('utf-8') if k else None,
            'value_serializer': lambda v: json.dumps(v).encode('utf-8')
        }
        
        self.producer = KafkaProducer(**config)
        
        # Metrics tracking
        self.sent_count = 0
        self.error_count = 0
        self.start_time = time.time()
    
    def send_event(self, 
                   topic: str, 
                   event_data: Dict[str, Any],
                   key: str = None,
                   headers: Dict[str, bytes] = None,
                   partition: int = None,
                   callback: Callable = None) -> bool:
        """Send event with comprehensive error handling and metrics"""
        
        try:
            # Enrich event with metadata
            enriched_event = self._enrich_event(event_data)
            
            # Determine partition key for ordering
            if key is None and 'entityId' in event_data:
                key = str(event_data['entityId'])
            
            # Add standard headers
            event_headers = {
                'source': 'order-service',
                'contentType': 'application/json',
                'eventId': enriched_event['eventId'],
                'timestamp': str(int(time.time() * 1000))
            }
            
            if headers:
                event_headers.update(headers)
            
            # Convert headers to bytes
            event_headers_bytes = {
                k: v.encode('utf-8') if isinstance(v, str) else v 
                for k, v in event_headers.items()
            }
            
            # Send message
            future = self.producer.send(
                topic=topic,
                key=key,
                value=enriched_event,
                partition=partition,
                headers=event_headers_bytes
            )
            
            # Add callback for success/failure tracking
            if callback:
                future.add_callback(callback)
            
            future.add_callback(self._on_success)
            future.add_errback(self._on_error)
            
            self.sent_count += 1
            
            if self.sent_count % 1000 == 0:
                self._log_metrics()
            
            return True
            
        except Exception as e:
            self.error_count += 1
            self.logger.error(f"Failed to send event to {topic}: {e}")
            return False
    
    def _enrich_event(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Enrich event with standard metadata"""
        
        enriched = event_data.copy()
        
        # Add standard fields if not present
        if 'eventId' not in enriched:
            enriched['eventId'] = str(uuid.uuid4())
        
        if 'timestamp' not in enriched:
            enriched['timestamp'] = datetime.now().isoformat()
        
        if 'eventVersion' not in enriched:
            enriched['eventVersion'] = '1.0'
        
        # Add checksum for data integrity
        event_str = json.dumps(enriched, sort_keys=True)
        enriched['checksum'] = hashlib.sha256(event_str.encode()).hexdigest()
        
        return enriched
    
    def send_batch_events(self, topic: str, events: list) -> Dict[str, int]:
        """Send multiple events efficiently"""
        
        results = {'success': 0, 'failed': 0}
        
        for event in events:
            if self.send_event(topic, event):
                results['success'] += 1
            else:
                results['failed'] += 1
        
        # Flush to ensure all messages are sent
        self.producer.flush()
        
        return results
    
    def _on_success(self, record_metadata):
        """Handle successful send"""
        self.logger.debug(f"Event sent to {record_metadata.topic} "
                         f"partition {record_metadata.partition} "
                         f"offset {record_metadata.offset}")
    
    def _on_error(self, exception):
        """Handle send failure"""
        self.error_count += 1
        self.logger.error(f"Failed to send event: {exception}")
    
    def _log_metrics(self):
        """Log producer metrics"""
        runtime = time.time() - self.start_time
        rate = self.sent_count / runtime if runtime > 0 else 0
        
        self.logger.info(f"Producer metrics - Sent: {self.sent_count}, "
                        f"Errors: {self.error_count}, Rate: {rate:.2f}/sec")
    
    def close(self):
        """Close producer and flush remaining messages"""
        self.producer.flush(timeout=30)
        self.producer.close()
        self._log_metrics()

# Usage
producer = AdvancedKafkaProducer(
    bootstrap_servers=['localhost:9092'],
    client_id='order-service-producer'
)

# Send single event
order_event = {
    'eventType': 'OrderCreated',
    'entityId': 'ORD-123',
    'data': {
        'orderId': 'ORD-123',
        'customerId': 'CUST-456',
        'totalAmount': 99.99
    }
}

success = producer.send_event('orders', order_event, key='ORD-123')

# Send batch events
batch_events = [
    {'eventType': 'ItemViewed', 'data': {'productId': f'PROD-{i}'}}
    for i in range(100)
]

batch_results = producer.send_batch_events('user-activity', batch_events)
print(f"Batch results: {batch_results}")

producer.close()
```

### Advanced Kafka Consumer

```python
from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata
import json
import time
import logging
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Callable, List
import signal
import sys
from dataclasses import dataclass
from enum import Enum

class ConsumerState(Enum):
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"

@dataclass
class ProcessingResult:
    success: bool
    error_message: str = None
    processing_time_ms: float = 0
    retry_count: int = 0

class AdvancedKafkaConsumer:
    def __init__(self, 
                 topics: List[str],
                 bootstrap_servers: List[str],
                 group_id: str,
                 auto_offset_reset: str = 'latest',
                 enable_auto_commit: bool = False,
                 max_poll_records: int = 500,
                 session_timeout_ms: int = 30000,
                 heartbeat_interval_ms: int = 10000,
                 max_poll_interval_ms: int = 300000):
        
        self.topics = topics
        self.group_id = group_id
        self.logger = logging.getLogger(__name__)
        self.state = ConsumerState.STOPPED
        self.message_handlers = {}
        self.error_handlers = {}
        
        # Consumer configuration
        config = {
            'bootstrap_servers': bootstrap_servers,
            'group_id': group_id,
            'auto_offset_reset': auto_offset_reset,
            'enable_auto_commit': enable_auto_commit,
            'max_poll_records': max_poll_records,
            'session_timeout_ms': session_timeout_ms,
            'heartbeat_interval_ms': heartbeat_interval_ms,
            'max_poll_interval_ms': max_poll_interval_ms,
            'key_deserializer': lambda k: k.decode('utf-8') if k else None,
            'value_deserializer': lambda m: json.loads(m.decode('utf-8'))
        }
        
        self.consumer = KafkaConsumer(*topics, **config)
        
        # Processing metrics
        self.processed_count = 0
        self.error_count = 0
        self.start_time = time.time()
        
        # Thread pool for parallel processing
        self.executor = ThreadPoolExecutor(max_workers=10)
        
        # Graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def register_handler(self, event_type: str, handler: Callable[[Dict[str, Any]], ProcessingResult]):
        """Register event handler"""
        self.message_handlers[event_type] = handler
        self.logger.info(f"Registered handler for {event_type}")
    
    def register_error_handler(self, error_type: type, handler: Callable[[Exception, Dict[str, Any]], None]):
        """Register error handler"""
        self.error_handlers[error_type] = handler
        self.logger.info(f"Registered error handler for {error_type.__name__}")
    
    def start(self):
        """Start consuming messages"""
        self.state = ConsumerState.RUNNING
        self.logger.info(f"Starting consumer for topics: {self.topics}")
        
        try:
            while self.state == ConsumerState.RUNNING:
                # Poll for messages
                message_batch = self.consumer.poll(timeout_ms=1000, max_records=100)
                
                if message_batch:
                    self._process_batch(message_batch)
                
                # Commit offsets manually
                self._commit_offsets()
                
        except Exception as e:
            self.logger.error(f"Consumer error: {e}")
            self.state = ConsumerState.STOPPED
        
        finally:
            self.consumer.close()
            self.executor.shutdown(wait=True)
            self._log_final_metrics()
    
    def _process_batch(self, message_batch: Dict[TopicPartition, List]):
        """Process batch of messages with parallelization"""
        
        futures = []
        
        for topic_partition, messages in message_batch.items():
            for message in messages:
                # Submit to thread pool for parallel processing
                future = self.executor.submit(self._process_message, message)
                futures.append((future, message))
        
        # Wait for all messages to be processed
        for future, message in futures:
            try:
                result = future.result(timeout=30)  # 30 second timeout
                
                if result.success:
                    self.processed_count += 1
                else:
                    self.error_count += 1
                    self._handle_processing_error(message, result.error_message)
                
            except Exception as e:
                self.error_count += 1
                self.logger.error(f"Processing timeout or error: {e}")
                self._handle_processing_error(message, str(e))
    
    def _process_message(self, message) -> ProcessingResult:
        """Process individual message"""
        
        start_time = time.time()
        
        try:
            # Extract event information
            event_data = message.value
            event_type = event_data.get('eventType')
            event_id = event_data.get('eventId', 'unknown')
            
            self.logger.debug(f"Processing event {event_id} of type {event_type}")
            
            # Find appropriate handler
            if event_type in self.message_handlers:
                handler = self.message_handlers[event_type]
                
                # Add message metadata to event
                event_data['_metadata'] = {
                    'topic': message.topic,
                    'partition': message.partition,
                    'offset': message.offset,
                    'timestamp': message.timestamp,
                    'headers': {k: v.decode('utf-8') for k, v in (message.headers or [])}
                }
                
                # Call handler
                result = handler(event_data)
                
                if isinstance(result, ProcessingResult):
                    processing_time = (time.time() - start_time) * 1000
                    result.processing_time_ms = processing_time
                    return result
                else:
                    # Assume success if handler doesn't return ProcessingResult
                    return ProcessingResult(
                        success=True,
                        processing_time_ms=(time.time() - start_time) * 1000
                    )
            else:
                self.logger.warning(f"No handler registered for event type: {event_type}")
                return ProcessingResult(
                    success=False,
                    error_message=f"No handler for event type: {event_type}"
                )
        
        except Exception as e:
            processing_time = (time.time() - start_time) * 1000
            self.logger.error(f"Error processing event: {e}")
            
            # Call error handler if registered
            error_type = type(e)
            if error_type in self.error_handlers:
                self.error_handlers[error_type](e, event_data)
            
            return ProcessingResult(
                success=False,
                error_message=str(e),
                processing_time_ms=processing_time
            )
    
    def _handle_processing_error(self, message, error_message: str):
        """Handle processing errors with retry logic"""
        
        # Extract retry count from headers
        retry_count = 0
        if message.headers:
            for key, value in message.headers:
                if key == 'retry-count':
                    retry_count = int(value.decode('utf-8'))
        
        max_retries = 3
        
        if retry_count < max_retries:
            # Send to retry topic
            retry_event = message.value.copy()
            retry_event['_retry'] = {
                'count': retry_count + 1,
                'error': error_message,
                'original_topic': message.topic,
                'original_partition': message.partition,
                'original_offset': message.offset
            }
            
            # Send to retry topic (you'd need a retry producer)
            self.logger.info(f"Sending message to retry queue (attempt {retry_count + 1})")
            
        else:
            # Send to dead letter queue
            dlq_event = message.value.copy()
            dlq_event['_deadLetter'] = {
                'reason': error_message,
                'finalRetryCount': retry_count,
                'originalTopic': message.topic,
                'failedAt': datetime.now().isoformat()
            }
            
            self.logger.error(f"Message sent to dead letter queue after {retry_count} retries")
    
    def _commit_offsets(self):
        """Manually commit offsets"""
        try:
            self.consumer.commit()
        except Exception as e:
            self.logger.error(f"Failed to commit offsets: {e}")
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        self.logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.state = ConsumerState.STOPPED
    
    def _log_final_metrics(self):
        """Log final processing metrics"""
        runtime = time.time() - self.start_time
        rate = self.processed_count / runtime if runtime > 0 else 0
        error_rate = (self.error_count / (self.processed_count + self.error_count) * 100) if (self.processed_count + self.error_count) > 0 else 0
        
        self.logger.info(f"Consumer metrics - Processed: {self.processed_count}, "
                        f"Errors: {self.error_count}, Rate: {rate:.2f}/sec, "
                        f"Error Rate: {error_rate:.2f}%")
    
    def pause_consumption(self):
        """Pause message consumption"""
        self.state = ConsumerState.PAUSED
        self.consumer.pause(*self.consumer.assignment())
        self.logger.info("Consumer paused")
    
    def resume_consumption(self):
        """Resume message consumption"""
        self.state = ConsumerState.RUNNING
        self.consumer.resume(*self.consumer.assignment())
        self.logger.info("Consumer resumed")

# Event handlers
def handle_order_created(event_data: Dict[str, Any]) -> ProcessingResult:
    """Handle OrderCreated event"""
    try:
        order_id = event_data['data']['orderId']
        customer_id = event_data['data']['customerId']
        
        # Simulate processing
        print(f"Processing order {order_id} for customer {customer_id}")
        time.sleep(0.1)  # Simulate work
        
        return ProcessingResult(success=True)
        
    except Exception as e:
        return ProcessingResult(success=False, error_message=str(e))

def handle_payment_processed(event_data: Dict[str, Any]) -> ProcessingResult:
    """Handle PaymentProcessed event"""
    try:
        payment_id = event_data['data']['paymentId']
        amount = event_data['data']['amount']
        
        print(f"Processing payment {payment_id} for amount ${amount}")
        
        # Simulate payment processing
        if amount > 10000:  # Simulate fraud detection
            raise Exception(f"Suspicious transaction amount: ${amount}")
        
        return ProcessingResult(success=True)
        
    except Exception as e:
        return ProcessingResult(success=False, error_message=str(e))

def handle_database_error(error: Exception, event_data: Dict[str, Any]):
    """Handle database connection errors"""
    print(f"Database error occurred while processing event {event_data.get('eventId', 'unknown')}: {error}")
    # Could implement retry logic, circuit breaker, etc.

def handle_validation_error(error: Exception, event_data: Dict[str, Any]):
    """Handle validation errors"""
    print(f"Validation error for event {event_data.get('eventId', 'unknown')}: {error}")
    # Could send to validation error topic

# Usage
consumer = AdvancedKafkaConsumer(
    topics=['orders', 'payments'],
    bootstrap_servers=['localhost:9092'],
    group_id='order-processing-service'
)

# Register event handlers
consumer.register_handler('OrderCreated', handle_order_created)
consumer.register_handler('PaymentProcessed', handle_payment_processed)

# Register error handlers
consumer.register_error_handler(ConnectionError, handle_database_error)
consumer.register_error_handler(ValueError, handle_validation_error)

# Start consuming
consumer.start()
```

### Kafka Streams Processing

```python
# Note: This is conceptual as kafka-streams-python isn't as mature as Java version
# In production, consider using Java for Kafka Streams or Python with confluent-kafka
import json
import time
from kafka import KafkaConsumer, KafkaProducer
from collections import defaultdict, deque
from typing import Dict, Any, Callable, Optional
from datetime import datetime, timedelta
import threading

class KafkaStreamsProcessor:
    def __init__(self, application_id: str, bootstrap_servers: List[str]):
        self.application_id = application_id
        self.bootstrap_servers = bootstrap_servers
        self.topology = []
        self.state_stores = {}
        self.logger = logging.getLogger(__name__)
        
        # Processing state
        self.running = False
        self.consumers = {}
        self.producers = {}
        
    def stream(self, topics: List[str], name: str = "stream"):
        """Create a stream from topics"""
        stream = KStream(self, topics, name)
        return stream
    
    def table(self, topic: str, name: str = "table"):
        """Create a table from topic"""
        table = KTable(self, topic, name)
        return table
    
    def create_state_store(self, name: str, store_type: str = "memory"):
        """Create a state store for stateful operations"""
        if store_type == "memory":
            self.state_stores[name] = {}
        else:
            raise ValueError(f"Store type {store_type} not supported")
    
    def start(self):
        """Start the streams application"""
        self.running = True
        self.logger.info(f"Starting streams application: {self.application_id}")
        
        # Start consumers for each topology node
        for node in self.topology:
            consumer_thread = threading.Thread(target=node.run)
            consumer_thread.start()

class KStream:
    def __init__(self, processor: KafkaStreamsProcessor, topics: List[str], name: str):
        self.processor = processor
        self.topics = topics
        self.name = name
        
    def filter(self, predicate: Callable[[Dict[str, Any]], bool], name: str = "filter"):
        """Filter events based on predicate"""
        filter_node = FilterNode(self, predicate, name)
        self.processor.topology.append(filter_node)
        return KStream(self.processor, [f"{self.name}-{name}"], f"{self.name}-{name}")
    
    def map(self, mapper: Callable[[Dict[str, Any]], Dict[str, Any]], name: str = "map"):
        """Transform events using mapper function"""
        map_node = MapNode(self, mapper, name)
        self.processor.topology.append(map_node)
        return KStream(self.processor, [f"{self.name}-{name}"], f"{self.name}-{name}")
    
    def group_by_key(self):
        """Group events by key for aggregation"""
        return KGroupedStream(self)
    
    def to(self, topic: str):
        """Send events to output topic"""
        sink_node = SinkNode(self, topic)
        self.processor.topology.append(sink_node)

class KGroupedStream:
    def __init__(self, stream: KStream):
        self.stream = stream
    
    def aggregate(self, 
                  initializer: Callable[[], Any],
                  aggregator: Callable[[Any, Dict[str, Any]], Any],
                  window_size_ms: int = 60000,
                  store_name: str = "aggregate-store"):
        """Perform windowed aggregation"""
        
        # Create state store for aggregation
        self.stream.processor.create_state_store(store_name)
        
        agg_node = AggregateNode(
            self.stream, 
            initializer, 
            aggregator,
            window_size_ms,
            store_name
        )
        
        self.stream.processor.topology.append(agg_node)
        return KTable(self.stream.processor, f"{self.stream.name}-aggregated", "aggregated-table")

class ProcessingNode:
    def __init__(self, stream: KStream, name: str):
        self.stream = stream
        self.name = name
        self.processor = stream.processor
        
    def run(self):
        """Run the processing node"""
        consumer = KafkaConsumer(
            *self.stream.topics,
            bootstrap_servers=self.processor.bootstrap_servers,
            group_id=f"{self.processor.application_id}-{self.name}",
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            enable_auto_commit=False
        )
        
        producer = KafkaProducer(
            bootstrap_servers=self.processor.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
        try:
            while self.processor.running:
                message_batch = consumer.poll(timeout_ms=1000)
                
                for partition, messages in message_batch.items():
                    for message in messages:
                        self.process_record(message, producer)
                
                consumer.commit()
            
        finally:
            consumer.close()
            producer.close()
    
    def process_record(self, message, producer):
        """Process individual record - to be implemented by subclasses"""
        pass

class FilterNode(ProcessingNode):
    def __init__(self, stream: KStream, predicate: Callable, name: str):
        super().__init__(stream, name)
        self.predicate = predicate
        self.output_topic = f"{stream.name}-{name}"
    
    def process_record(self, message, producer):
        event_data = message.value
        
        if self.predicate(event_data):
            producer.send(self.output_topic, key=message.key, value=event_data)

class MapNode(ProcessingNode):
    def __init__(self, stream: KStream, mapper: Callable, name: str):
        super().__init__(stream, name)
        self.mapper = mapper
        self.output_topic = f"{stream.name}-{name}"
    
    def process_record(self, message, producer):
        event_data = message.value
        transformed_data = self.mapper(event_data)
        
        producer.send(self.output_topic, key=message.key, value=transformed_data)

class AggregateNode(ProcessingNode):
    def __init__(self, stream: KStream, initializer: Callable, 
                 aggregator: Callable, window_size_ms: int, store_name: str):
        super().__init__(stream, f"aggregate-{store_name}")
        self.initializer = initializer
        self.aggregator = aggregator
        self.window_size_ms = window_size_ms
        self.store_name = store_name
        self.windows = defaultdict(lambda: defaultdict(lambda: self.initializer()))
        self.output_topic = f"{stream.name}-aggregated"
    
    def process_record(self, message, producer):
        event_data = message.value
        key = message.key or "null"
        
        # Calculate window
        window_start = (message.timestamp // self.window_size_ms) * self.window_size_ms
        
        # Update aggregation
        current_value = self.windows[window_start][key]
        new_value = self.aggregator(current_value, event_data)
        self.windows[window_start][key] = new_value
        
        # Emit aggregated result
        result = {
            'windowStart': window_start,
            'windowEnd': window_start + self.window_size_ms,
            'key': key,
            'value': new_value,
            'eventTime': datetime.now().isoformat()
        }
        
        producer.send(self.output_topic, key=key, value=result)

class SinkNode(ProcessingNode):
    def __init__(self, stream: KStream, output_topic: str):
        super().__init__(stream, "sink")
        self.output_topic = output_topic
    
    def process_record(self, message, producer):
        producer.send(self.output_topic, key=message.key, value=message.value)

# Usage example
def create_order_processing_stream():
    """Create a Kafka Streams topology for order processing"""
    
    # Create streams processor
    streams = KafkaStreamsProcessor(
        application_id="order-processing-app",
        bootstrap_servers=['localhost:9092']
    )
    
    # Create stream from orders topic
    orders_stream = streams.stream(['orders'])
    
    # Filter for confirmed orders only
    confirmed_orders = orders_stream.filter(
        lambda event: event['data']['status'] == 'confirmed',
        name="filter-confirmed"
    )
    
    # Enrich with customer information
    enriched_orders = confirmed_orders.map(
        lambda event: enrich_order_with_customer(event),
        name="enrich-customer"
    )
    
    # Calculate real-time aggregations
    order_aggregations = enriched_orders.group_by_key().aggregate(
        initializer=lambda: {'count': 0, 'totalAmount': 0.0, 'avgAmount': 0.0},
        aggregator=lambda acc, event: {
            'count': acc['count'] + 1,
            'totalAmount': acc['totalAmount'] + event['data']['totalAmount'],
            'avgAmount': (acc['totalAmount'] + event['data']['totalAmount']) / (acc['count'] + 1)
        },
        window_size_ms=60000,  # 1-minute windows
        store_name="order-aggregations"
    )
    
    # Send enriched orders to processed topic
    enriched_orders.to('processed-orders')
    
    # Send aggregations to analytics topic
    order_aggregations.to('order-analytics')
    
    return streams

def enrich_order_with_customer(event):
    """Enrich order event with customer information"""
    # In real implementation, this would lookup customer data
    event['data']['customerInfo'] = {
        'segment': 'premium',
        'region': 'us-east'
    }
    return event

# Run the stream processing
if __name__ == "__main__":
    streams_app = create_order_processing_stream()
    streams_app.start()
```

---

## 🐰 RabbitMQ Complete Guide {#rabbitmq}

### RabbitMQ Architecture & Exchange Types

```
┌─────────────────────────────────────────────────────────────────┐
│                      RabbitMQ Broker                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐        │
│  │  Exchange   │    │  Exchange   │    │  Exchange   │        │
│  │   (Topic)   │    │  (Direct)   │    │  (Fanout)   │        │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘        │
│         │                  │                  │               │
│         ▼                  ▼                  ▼               │
│  ┌─────────────────────────────────────────────────────┐      │
│  │                    Queues                           │      │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │      │
│  │  │Queue A  │  │Queue B  │  │Queue C  │             │      │
│  │  └─────────┘  └─────────┘  └─────────┘             │      │
│  └─────────────────────────────────────────────────────┘      │
│         │            │            │                           │
└─────────┼────────────┼────────────┼───────────────────────────┘
          ▼            ▼            ▼
    Consumer 1   Consumer 2   Consumer 3
```

**Exchange Types**:

1. **Direct Exchange**: Routes messages based on exact routing key match
2. **Topic Exchange**: Routes messages based on routing key patterns (wildcards)
3. **Fanout Exchange**: Broadcasts messages to all bound queues
4. **Headers Exchange**: Routes based on message headers

### Complete RabbitMQ Implementation

```python
import pika
import json
import logging
import time
from datetime import datetime
from typing import Dict, Any, List, Callable, Optional
import threading
from dataclasses import dataclass
from enum import Enum
import uuid

class ExchangeType(Enum):
    DIRECT = "direct"
    TOPIC = "topic"
    FANOUT = "fanout"
    HEADERS = "headers"

@dataclass
class QueueConfig:
    name: str
    durable: bool = True
    exclusive: bool = False
    auto_delete: bool = False
    arguments: Dict[str, Any] = None

@dataclass
class ExchangeConfig:
    name: str
    exchange_type: ExchangeType
    durable: bool = True
    auto_delete: bool = False
    arguments: Dict[str, Any] = None

class RabbitMQManager:
    def __init__(self, 
                 host: str = 'localhost',
                 port: int = 5672,
                 username: str = 'guest',
                 password: str = 'guest',
                 virtual_host: str = '/'):
        
        self.connection_params = pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host=virtual_host,
            credentials=pika.PlainCredentials(username, password),
            heartbeat=600,
            blocked_connection_timeout=300,
        )
        
        self.logger = logging.getLogger(__name__)
        self.connection = None
        self.channel = None
    
    def connect(self):
        """Establish connection to RabbitMQ"""
        try:
            self.connection = pika.BlockingConnection(self.connection_params)
            self.channel = self.connection.channel()
            self.logger.info("Connected to RabbitMQ")
        except Exception as e:
            self.logger.error(f"Failed to connect to RabbitMQ: {e}")
            raise
    
    def disconnect(self):
        """Close connection to RabbitMQ"""
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            self.logger.info("Disconnected from RabbitMQ")
    
    def declare_exchange(self, config: ExchangeConfig):
        """Declare an exchange"""
        if not self.channel:
            self.connect()
        
        self.channel.exchange_declare(
            exchange=config.name,
            exchange_type=config.exchange_type.value,
            durable=config.durable,
            auto_delete=config.auto_delete,
            arguments=config.arguments
        )
        
        self.logger.info(f"Declared exchange: {config.name} ({config.exchange_type.value})")
    
    def declare_queue(self, config: QueueConfig):
        """Declare a queue"""
        if not self.channel:
            self.connect()
        
        result = self.channel.queue_declare(
            queue=config.name,
            durable=config.durable,
            exclusive=config.exclusive,
            auto_delete=config.auto_delete,
            arguments=config.arguments
        )
        
        self.logger.info(f"Declared queue: {config.name}")
        return result
    
    def bind_queue(self, queue_name: str, exchange_name: str, routing_key: str = ""):
        """Bind queue to exchange"""
        if not self.channel:
            self.connect()
        
        self.channel.queue_bind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=routing_key
        )
        
        self.logger.info(f"Bound queue {queue_name} to exchange {exchange_name} with key '{routing_key}'")

class RabbitMQPublisher:
    def __init__(self, manager: RabbitMQManager):
        self.manager = manager
        self.logger = logging.getLogger(__name__)
        
        # Message properties
        self.properties = pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
            timestamp=int(time.time()),
            message_id=str(uuid.uuid4())
        )
    
    def publish_event(self, 
                     exchange: str,
                     routing_key: str,
                     event_data: Dict[str, Any],
                     headers: Dict[str, str] = None) -> bool:
        """Publish event to exchange"""
        
        try:
            if not self.manager.channel:
                self.manager.connect()
            
            # Enrich event with metadata
            enriched_event = {
                **event_data,
                'publishedAt': datetime.now().isoformat(),
                'publisher': 'order-service'
            }
            
            # Set message properties
            properties = pika.BasicProperties(
                delivery_mode=2,  # Persistent
                timestamp=int(time.time()),
                message_id=str(uuid.uuid4()),
                headers=headers or {},
                content_type='application/json'
            )
            
            # Publish message
            self.manager.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=json.dumps(enriched_event),
                properties=properties,
                mandatory=True  # Return message if no queue can handle it
            )
            
            self.logger.info(f"Published event to {exchange} with routing key '{routing_key}'")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to publish event: {e}")
            return False
    
    def publish_with_confirmation(self, exchange: str, routing_key: str, event_data: Dict[str, Any]) -> bool:
        """Publish with publisher confirmation for guaranteed delivery"""
        
        try:
            if not self.manager.channel:
                self.manager.connect()
            
            # Enable publisher confirmations
            self.manager.channel.confirm_delivery()
            
            result = self.publish_event(exchange, routing_key, event_data)
            
            if result:
                self.logger.info("Message delivery confirmed by broker")
                return True
            else:
                self.logger.error("Message delivery not confirmed")
                return False
                
        except pika.exceptions.UnroutableError:
            self.logger.error("Message was returned as unroutable")
            return False
        except Exception as e:
            self.logger.error(f"Publication failed: {e}")
            return False

class RabbitMQConsumer:
    def __init__(self, manager: RabbitMQManager, queue_name: str):
        self.manager = manager
        self.queue_name = queue_name
        self.logger = logging.getLogger(__name__)
        self.handlers = {}
        self.running = False
        
        # Consumer configuration
        self.prefetch_count = 10  # QoS
        
    def register_handler(self, event_type: str, handler: Callable[[Dict[str, Any]], bool]):
        """Register event handler"""
        self.handlers[event_type] = handler
        self.logger.info(f"Registered handler for {event_type}")
    
    def start_consuming(self):
        """Start consuming messages"""
        if not self.manager.channel:
            self.manager.connect()
        
        # Set QoS to limit unacknowledged messages
        self.manager.channel.basic_qos(prefetch_count=self.prefetch_count)
        
        # Set up consumer
        self.manager.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self._on_message,
            auto_ack=False  # Manual acknowledgment
        )
        
        self.running = True
        self.logger.info(f"Starting to consume from {self.queue_name}")
        
        try:
            self.manager.channel.start_consuming()
        except KeyboardInterrupt:
            self.logger.info("Consumer interrupted by user")
            self.stop_consuming()
        except Exception as e:
            self.logger.error(f"Consumer error: {e}")
        finally:
            self.manager.disconnect()
    
    def stop_consuming(self):
        """Stop consuming messages"""
        self.running = False
        if self.manager.channel:
            self.manager.channel.stop_consuming()
        self.logger.info("Stopped consuming")
    
    def _on_message(self, channel, method, properties, body):
        """Handle incoming message"""
        try:
            # Parse message
            event_data = json.loads(body.decode('utf-8'))
            event_type = event_data.get('eventType', 'unknown')
            event_id = event_data.get('eventId', 'unknown')
            
            self.logger.info(f"Processing event {event_id} of type {event_type}")
            
            # Find and call handler
            if event_type in self.handlers:
                start_time = time.time()
                
                try:
                    success = self.handlers[event_type](event_data)
                    processing_time = (time.time() - start_time) * 1000
                    
                    if success:
                        # Acknowledge message
                        channel.basic_ack(delivery_tag=method.delivery_tag)
                        self.logger.info(f"Successfully processed event {event_id} in {processing_time:.2f}ms")
                    else:
                        # Reject and requeue
                        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
                        self.logger.error(f"Handler returned False for event {event_id}")
                
                except Exception as handler_error:
                    # Check retry count
                    retry_count = self._get_retry_count(properties)
                    max_retries = 3
                    
                    if retry_count < max_retries:
                        # Reject and requeue for retry
                        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
                        self.logger.warning(f"Handler failed for event {event_id} (retry {retry_count + 1}/{max_retries}): {handler_error}")
                    else:
                        # Send to dead letter queue
                        self._send_to_dlq(event_data, str(handler_error))
                        channel.basic_ack(delivery_tag=method.delivery_tag)
                        self.logger.error(f"Event {event_id} sent to DLQ after {max_retries} retries")
            else:
                self.logger.warning(f"No handler for event type {event_type}")
                channel.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge unknown events
                
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in message: {e}")
            channel.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge malformed messages
            
        except Exception as e:
            self.logger.error(f"Unexpected error processing message: {e}")
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    
    def _get_retry_count(self, properties) -> int:
        """Get retry count from message headers"""
        if properties.headers and 'x-retry-count' in properties.headers:
            return int(properties.headers['x-retry-count'])
        return 0
    
    def _send_to_dlq(self, event_data: Dict[str, Any], error_message: str):
        """Send failed message to dead letter queue"""
        dlq_event = {
            **event_data,
            '_dlq': {
                'reason': error_message,
                'failedAt': datetime.now().isoformat(),
                'originalQueue': self.queue_name
            }
        }
        
        # Publish to DLQ (you'd need a DLQ publisher)
        self.logger.info(f"Sending event {event_data.get('eventId')} to DLQ")

# E-commerce Event System Example
class EcommerceEventSystem:
    def __init__(self):
        self.rabbitmq = RabbitMQManager()
        self.rabbitmq.connect()
        
        self._setup_topology()
        
    def _setup_topology(self):
        """Set up RabbitMQ exchanges, queues, and bindings"""
        
        # Exchanges
        self.rabbitmq.declare_exchange(ExchangeConfig(
            name="orders",
            exchange_type=ExchangeType.TOPIC
        ))
        
        self.rabbitmq.declare_exchange(ExchangeConfig(
            name="notifications", 
            exchange_type=ExchangeType.FANOUT
        ))
        
        self.rabbitmq.declare_exchange(ExchangeConfig(
            name="payments",
            exchange_type=ExchangeType.DIRECT
        ))
        
        # Queues
        queues = [
            QueueConfig(name="order-created", durable=True),
            QueueConfig(name="order-confirmed", durable=True),
            QueueConfig(name="payment-processing", durable=True),
            QueueConfig(name="inventory-updates", durable=True),
            QueueConfig(name="email-notifications", durable=True),
            QueueConfig(name="sms-notifications", durable=True),
            QueueConfig(
                name="order-created-dlq", 
                durable=True,
                arguments={'x-message-ttl': 86400000}  # 24 hours TTL
            )
        ]
        
        for queue_config in queues:
            self.rabbitmq.declare_queue(queue_config)
        
        # Bindings
        bindings = [
            ("order-created", "orders", "order.created"),
            ("order-confirmed", "orders", "order.confirmed"),
            ("payment-processing", "orders", "order.confirmed"),
            ("inventory-updates", "orders", "order.*"),
            ("email-notifications", "notifications", ""),
            ("sms-notifications", "notifications", "")
        ]
        
        for queue, exchange, routing_key in bindings:
            self.rabbitmq.bind_queue(queue, exchange, routing_key)
    
    def create_publisher(self, service_name: str) -> RabbitMQPublisher:
        """Create a publisher for a service"""
        return RabbitMQPublisher(self.rabbitmq)
    
    def create_consumer(self, queue_name: str) -> RabbitMQConsumer:
        """Create a consumer for a queue"""
        return RabbitMQConsumer(self.rabbitmq, queue_name)

# Event handlers
def handle_order_created(event_data: Dict[str, Any]) -> bool:
    """Handle order created event"""
    try:
        order_id = event_data['data']['orderId']
        customer_id = event_data['data']['customerId']
        
        # Validate order data
        if not order_id or not customer_id:
            raise ValueError("Missing required order fields")
        
        # Process order creation
        print(f"Processing order creation: {order_id} for customer {customer_id}")
        
        # Simulate processing time
        time.sleep(0.1)
        
        return True  # Success
        
    except Exception as e:
        print(f"Error handling order created: {e}")
        return False  # Will trigger retry

def handle_payment_processing(event_data: Dict[str, Any]) -> bool:
    """Handle payment processing"""
    try:
        order_id = event_data['data']['orderId']
        amount = event_data['data']['totalAmount']
        
        print(f"Processing payment for order {order_id}: ${amount}")
        
        # Simulate payment processing
        if amount > 5000:  # Simulate failure for large amounts
            raise Exception("Payment gateway timeout")
        
        time.sleep(0.2)  # Simulate processing
        
        return True
        
    except Exception as e:
        print(f"Payment processing failed: {e}")
        return False

def handle_email_notification(event_data: Dict[str, Any]) -> bool:
    """Handle email notification"""
    try:
        event_type = event_data.get('eventType')
        
        if event_type == 'OrderCreated':
            print(f"Sending order confirmation email for {event_data['data']['orderId']}")
        elif event_type == 'PaymentProcessed':
            print(f"Sending payment confirmation email for {event_data['data']['orderId']}")
        
        # Simulate email sending
        time.sleep(0.05)
        
        return True
        
    except Exception as e:
        print(f"Email notification failed: {e}")
        return False

# Usage example
if __name__ == "__main__":
    # Set up event system
    event_system = EcommerceEventSystem()
    
    # Create publisher
    publisher = event_system.create_publisher("order-service")
    
    # Create consumers
    order_consumer = event_system.create_consumer("order-created")
    payment_consumer = event_system.create_consumer("payment-processing")
    email_consumer = event_system.create_consumer("email-notifications")
    
    # Register handlers
    order_consumer.register_handler("OrderCreated", handle_order_created)
    payment_consumer.register_handler("OrderConfirmed", handle_payment_processing)
    email_consumer.register_handler("OrderCreated", handle_email_notification)
    email_consumer.register_handler("PaymentProcessed", handle_email_notification)
    
    # Start consumers in separate threads
    consumer_threads = []
    
    for consumer in [order_consumer, payment_consumer, email_consumer]:
        thread = threading.Thread(target=consumer.start_consuming)
        thread.start()
        consumer_threads.append(thread)
    
    # Simulate order events
    time.sleep(1)  # Let consumers start
    
    for i in range(5):
        # Order created event
        order_created_event = {
            'eventType': 'OrderCreated',
            'eventId': f'evt-{i:03d}',
            'data': {
                'orderId': f'ORD-{i:03d}',
                'customerId': f'CUST-{i % 3:03d}',
                'totalAmount': 100.0 + i * 50,
                'items': [
                    {'productId': f'PROD-{i}', 'quantity': 1, 'price': 100.0 + i * 50}
                ]
            }
        }
        
        publisher.publish_event(
            exchange="orders",
            routing_key="order.created",
            event_data=order_created_event
        )
        
        # Order confirmed event (triggers payment)
        order_confirmed_event = {
            'eventType': 'OrderConfirmed',
            'eventId': f'evt-confirm-{i:03d}',
            'data': {
                'orderId': f'ORD-{i:03d}',
                'customerId': f'CUST-{i % 3:03d}',
                'totalAmount': 100.0 + i * 50
            }
        }
        
        publisher.publish_event(
            exchange="orders",
            routing_key="order.confirmed", 
            event_data=order_confirmed_event
        )
        
        time.sleep(0.5)
    
    # Let consumers process messages
    time.sleep(5)
    
    # Stop consumers
    for consumer in [order_consumer, payment_consumer, email_consumer]:
        consumer.stop_consuming()
    
    # Wait for threads to finish
    for thread in consumer_threads:
        thread.join()
    
    event_system.rabbitmq.disconnect()
```

### Advanced RabbitMQ Patterns

```python
# Dead Letter Exchange (DLX) Setup
class DeadLetterManager:
    def __init__(self, manager: RabbitMQManager):
        self.manager = manager
        self.logger = logging.getLogger(__name__)
    
    def setup_dlx_topology(self, main_queue: str, dlx_name: str):
        """Set up dead letter exchange topology"""
        
        # Create DLX
        self.manager.declare_exchange(ExchangeConfig(
            name=dlx_name,
            exchange_type=ExchangeType.DIRECT
        ))
        
        # Create DLQ
        dlq_name = f"{main_queue}-dlq"
        self.manager.declare_queue(QueueConfig(
            name=dlq_name,
            durable=True,
            arguments={
                'x-message-ttl': 86400000,  # Messages expire after 24 hours
            }
        ))
        
        # Bind DLQ to DLX
        self.manager.bind_queue(dlq_name, dlx_name, main_queue)
        
        # Update main queue to use DLX
        self.manager.channel.queue_delete(queue=main_queue)  # Delete existing
        self.manager.declare_queue(QueueConfig(
            name=main_queue,
            durable=True,
            arguments={
                'x-dead-letter-exchange': dlx_name,
                'x-dead-letter-routing-key': main_queue,
                'x-max-retries': 3
            }
        ))
        
        self.logger.info(f"Set up DLX topology for {main_queue}")

# Priority Queue Pattern
class PriorityQueueManager:
    def __init__(self, manager: RabbitMQManager):
        self.manager = manager
    
    def create_priority_queue(self, queue_name: str, max_priority: int = 10):
        """Create a priority queue"""
        self.manager.declare_queue(QueueConfig(
            name=queue_name,
            durable=True,
            arguments={'x-max-priority': max_priority}
        ))
    
    def publish_with_priority(self, exchange: str, routing_key: str, 
                            event_data: Dict[str, Any], priority: int):
        """Publish message with priority"""
        if not self.manager.channel:
            self.manager.connect()
        
        properties = pika.BasicProperties(
            delivery_mode=2,
            priority=priority
        )
        
        self.manager.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(event_data),
            properties=properties
        )

# Delayed Message Pattern
class DelayedMessageManager:
    def __init__(self, manager: RabbitMQManager):
        self.manager = manager
    
    def setup_delayed_exchange(self, exchange_name: str):
        """Set up exchange for delayed messages"""
        # Requires rabbitmq-delayed-message-exchange plugin
        self.manager.declare_exchange(ExchangeConfig(
            name=exchange_name,
            exchange_type=ExchangeType.DIRECT,
            arguments={'x-delayed-type': 'direct'}
        ))
    
    def publish_delayed_message(self, exchange: str, routing_key: str,
                               event_data: Dict[str, Any], delay_seconds: int):
        """Publish message with delay"""
        if not self.manager.channel:
            self.manager.connect()
        
        properties = pika.BasicProperties(
            delivery_mode=2,
            headers={'x-delay': delay_seconds * 1000}  # Delay in milliseconds
        )
        
        self.manager.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(event_data),
            properties=properties
        )

# Usage examples for advanced patterns
if __name__ == "__main__":
    rabbitmq = RabbitMQManager()
    
    # Dead letter setup
    dlx_manager = DeadLetterManager(rabbitmq)
    dlx_manager.setup_dlx_topology("orders", "orders-dlx")
    
    # Priority queue setup
    priority_manager = PriorityQueueManager(rabbitmq)
    priority_manager.create_priority_queue("priority-orders", max_priority=10)
    
    # Delayed message setup
    delayed_manager = DelayedMessageManager(rabbitmq)
    delayed_manager.setup_delayed_exchange("delayed-orders")
    
    # Publish high priority order
    high_priority_order = {
        'eventType': 'UrgentOrder',
        'data': {'orderId': 'URGENT-001', 'priority': 'high'}
    }
    
    priority_manager.publish_with_priority(
        "orders", "order.urgent", high_priority_order, priority=10
    )
    
    # Publish delayed reminder
    reminder_event = {
        'eventType': 'CartAbandonmentReminder',
        'data': {'customerId': 'CUST-123', 'cartId': 'CART-456'}
    }
    
    delayed_manager.publish_delayed_message(
        "delayed-orders", "reminder.cart", reminder_event, delay_seconds=3600  # 1 hour delay
    )
    
    rabbitmq.disconnect()
```

---

## 📚 Event Sourcing Deep Dive {#event-sourcing}

### Complete Event Store Implementation

```python
from abc import ABC, abstractmethod
import json
import sqlite3
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional, Type
import logging
from dataclasses import dataclass, asdict
from enum import Enum
import asyncio
import threading

@dataclass
class Event:
    event_id: str
    stream_id: str
    event_type: str
    event_data: Dict[str, Any]
    event_version: int
    timestamp: str
    metadata: Dict[str, Any] = None
    
    def to_dict(self):
        return asdict(self)

class EventStore(ABC):
    @abstractmethod
    async def append_events(self, stream_id: str, events: List[Event], expected_version: int = -1) -> int:
        pass
    
    @abstractmethod
    async def read_events(self, stream_id: str, from_version: int = 0, to_version: int = None) -> List[Event]:
        pass
    
    @abstractmethod
    async def read_all_events(self, from_position: int = 0, max_count: int = 1000) -> List[Event]:
        pass

class SQLiteEventStore(EventStore):
    def __init__(self, db_path: str = "eventstore.db"):
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)
        self._init_database()
        self._lock = threading.Lock()
    
    def _init_database(self):
        """Initialize database schema"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id TEXT UNIQUE NOT NULL,
                    stream_id TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    event_data TEXT NOT NULL,
                    event_version INTEGER NOT NULL,
                    timestamp TEXT NOT NULL,
                    metadata TEXT,
                    global_position INTEGER
                );
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_stream_version 
                ON events(stream_id, event_version);
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_event_type 
                ON events(event_type);
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON events(timestamp);
            """)
            
            conn.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS idx_stream_version_unique 
                ON events(stream_id, event_version);
            """)
    
    async def append_events(self, stream_id: str, events: List[Event], expected_version: int = -1) -> int:
        """Append events to stream with optimistic concurrency control"""
        
        with self._lock:
            with sqlite3.connect(self.db_path) as conn:
                # Check current version
                cursor = conn.execute(
                    "SELECT MAX(event_version) FROM events WHERE stream_id = ?",
                    (stream_id,)
                )
                result = cursor.fetchone()
                current_version = result[0] if result[0] is not None else -1
                
                # Optimistic concurrency check
                if expected_version != -1 and current_version != expected_version:
                    raise ValueError(f"Concurrency conflict: expected version {expected_version}, "
                                   f"but current version is {current_version}")
                
                # Insert events
                for i, event in enumerate(events):
                    new_version = current_version + i + 1
                    event.event_version = new_version
                    
                    conn.execute("""
                        INSERT INTO events 
                        (event_id, stream_id, event_type, event_data, event_version, timestamp, metadata)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        event.event_id,
                        stream_id,
                        event.event_type,
                        json.dumps(event.event_data),
                        new_version,
                        event.timestamp,
                        json.dumps(event.metadata) if event.metadata else None
                    ))
                
                self.logger.info(f"Appended {len(events)} events to stream {stream_id}")
                return current_version + len(events)
    
    async def read_events(self, stream_id: str, from_version: int = 0, to_version: int = None) -> List[Event]:
        """Read events from stream"""
        
        query = "SELECT * FROM events WHERE stream_id = ? AND event_version >= ?"
        params = [stream_id, from_version]
        
        if to_version is not None:
            query += " AND event_version <= ?"
            params.append(to_version)
        
        query += " ORDER BY event_version ASC"
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(query, params)
            rows = cursor.fetchall()
        
        events = []
        for row in rows:
            event = Event(
                event_id=row['event_id'],
                stream_id=row['stream_id'],
                event_type=row['event_type'],
                event_data=json.loads(row['event_data']),
                event_version=row['event_version'],
                timestamp=row['timestamp'],
                metadata=json.loads(row['metadata']) if row['metadata'] else None
            )
            events.append(event)
        
        return events
    
    async def read_all_events(self, from_position: int = 0, max_count: int = 1000) -> List[Event]:
        """Read all events across all streams"""
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT * FROM events 
                WHERE id > ?
                ORDER BY id ASC
                LIMIT ?
            """, (from_position, max_count))
            
            rows = cursor.fetchall()
        
        events = []
        for row in rows:
            event = Event(
                event_id=row['event_id'],
                stream_id=row['stream_id'],
                event_type=row['event_type'],
                event_data=json.loads(row['event_data']),
                event_version=row['event_version'],
                timestamp=row['timestamp'],
                metadata=json.loads(row['metadata']) if row['metadata'] else None
            )
            events.append(event)
        
        return events

# Aggregate Base Class
class AggregateRoot(ABC):
    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self.version = -1
        self.uncommitted_events: List[Event] = []
    
    @abstractmethod
    def apply_event(self, event: Event):
        """Apply event to change aggregate state"""
        pass
    
    def raise_event(self, event_type: str, event_data: Dict[str, Any], metadata: Dict[str, Any] = None):
        """Raise a new domain event"""
        event = Event(
            event_id=str(uuid.uuid4()),
            stream_id=f"{self.__class__.__name__}-{self.aggregate_id}",
            event_type=event_type,
            event_data=event_data,
            event_version=self.version + len(self.uncommitted_events) + 1,
            timestamp=datetime.now().isoformat(),
            metadata=metadata
        )
        
        self.uncommitted_events.append(event)
        self.apply_event(event)
    
    def mark_events_as_committed(self):
        """Mark uncommitted events as committed"""
        self.version += len(self.uncommitted_events)
        self.uncommitted_events.clear()
    
    @classmethod
    async def from_history(cls, aggregate_id: str, event_store: EventStore):
        """Rebuild aggregate from event history"""
        stream_id = f"{cls.__name__}-{aggregate_id}"
        events = await event_store.read_events(stream_id)
        
        aggregate = cls(aggregate_id)
        
        for event in events:
            aggregate.apply_event(event)
            aggregate.version = event.event_version
        
        return aggregate

# Example: Order Aggregate with Complex Business Logic
class OrderStatus(Enum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float
    
    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price

class OrderAggregate(AggregateRoot):
    def __init__(self, order_id: str):
        super().__init__(order_id)
        self.customer_id: Optional[str] = None
        self.items: List[OrderItem] = []
        self.status = OrderStatus.DRAFT
        self.shipping_address: Optional[Dict[str, str]] = None
        self.created_at: Optional[datetime] = None
        self.confirmed_at: Optional[datetime] = None
        self.shipped_at: Optional[datetime] = None
    
    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self.items)
    
    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)
    
    # Command methods (business operations)
    def create_order(self, customer_id: str, shipping_address: Dict[str, str]):
        if self.status != OrderStatus.DRAFT or self.customer_id is not None:
            raise ValueError("Order already created")
        
        self.raise_event("OrderCreated", {
            "orderId": self.aggregate_id,
            "customerId": customer_id,
            "shippingAddress": shipping_address,
            "createdAt": datetime.now().isoformat()
        })
    
    def add_item(self, product_id: str, quantity: int, unit_price: float):
        if self.status != OrderStatus.DRAFT:
            raise ValueError(f"Cannot add items to order in status {self.status.value}")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if unit_price <= 0:
            raise ValueError("Unit price must be positive")
        
        self.raise_event("ItemAdded", {
            "orderId": self.aggregate_id,
            "productId": product_id,
            "quantity": quantity,
            "unitPrice": unit_price
        })
    
    def remove_item(self, product_id: str):
        if self.status != OrderStatus.DRAFT:
            raise ValueError(f"Cannot remove items from order in status {self.status.value}")
        
        # Check if item exists
        item_exists = any(item.product_id == product_id for item in self.items)
        if not item_exists:
            raise ValueError(f"Product {product_id} not in order")
        
        self.raise_event("ItemRemoved", {
            "orderId": self.aggregate_id,
            "productId": product_id
        })
    
    def confirm_order(self):
        if self.status != OrderStatus.DRAFT:
            raise ValueError(f"Cannot confirm order in status {self.status.value}")
        
        if not self.items:
            raise ValueError("Cannot confirm empty order")
        
        if self.total_amount <= 0:
            raise ValueError("Order total must be positive")
        
        self.raise_event("OrderConfirmed", {
            "orderId": self.aggregate_id,
            "totalAmount": self.total_amount,
            "totalItems": self.total_items,
            "confirmedAt": datetime.now().isoformat()
        })
    
    def process_payment(self, payment_id: str, amount: float):
        if self.status != OrderStatus.CONFIRMED:
            raise ValueError(f"Cannot process payment for order in status {self.status.value}")
        
        if abs(amount - self.total_amount) > 0.01:  # Allow small floating point differences
            raise ValueError(f"Payment amount {amount} doesn't match order total {self.total_amount}")
        
        self.raise_event("PaymentProcessed", {
            "orderId": self.aggregate_id,
            "paymentId": payment_id,
            "amount": amount,
            "processedAt": datetime.now().isoformat()
        })
    
    def ship_order(self, carrier: str, tracking_number: str):
        if self.status != OrderStatus.PAID:
            raise ValueError(f"Cannot ship order in status {self.status.value}")
        
        self.raise_event("OrderShipped", {
            "orderId": self.aggregate_id,
            "carrier": carrier,
            "trackingNumber": tracking_number,
            "shippedAt": datetime.now().isoformat()
        })
    
    def cancel_order(self, reason: str):
        if self.status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED, OrderStatus.CANCELLED]:
            raise ValueError(f"Cannot cancel order in status {self.status.value}")
        
        self.raise_event("OrderCancelled", {
            "orderId": self.aggregate_id,
            "reason": reason,
            "cancelledAt": datetime.now().isoformat(),
            "refundAmount": self.total_amount if self.status == OrderStatus.PAID else 0
        })
    
    # Event handlers (state mutations)
    def apply_event(self, event: Event):
        event_type = event.event_type
        data = event.event_data
        
        if event_type == "OrderCreated":
            self.customer_id = data["customerId"]
            self.shipping_address = data["shippingAddress"]
            self.created_at = datetime.fromisoformat(data["createdAt"])
            self.status = OrderStatus.DRAFT
            
        elif event_type == "ItemAdded":
            item = OrderItem(
                product_id=data["productId"],
                quantity=data["quantity"],
                unit_price=data["unitPrice"]
            )
            # Check if item already exists and update quantity
            existing_item = next((i for i in self.items if i.product_id == data["productId"]), None)
            if existing_item:
                existing_item.quantity += data["quantity"]
            else:
                self.items.append(item)
                
        elif event_type == "ItemRemoved":
            self.items = [item for item in self.items if item.product_id != data["productId"]]
            
        elif event_type == "OrderConfirmed":
            self.status = OrderStatus.CONFIRMED
            self.confirmed_at = datetime.fromisoformat(data["confirmedAt"])
            
        elif event_type == "PaymentProcessed":
            self.status = OrderStatus.PAID
            
        elif event_type == "OrderShipped":
            self.status = OrderStatus.SHIPPED
            self.shipped_at = datetime.fromisoformat(data["shippedAt"])
            
        elif event_type == "OrderCancelled":
            self.status = OrderStatus.CANCELLED
            
        else:
            self.logger.warning(f"Unknown event type: {event_type}")

class OrderRepository:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.logger = logging.getLogger(__name__)
    
    async def save(self, order: OrderAggregate, expected_version: int = -1) -> None:
        """Save order aggregate"""
        if not order.uncommitted_events:
            return
        
        try:
            stream_id = f"Order-{order.aggregate_id}"
            new_version = await self.event_store.append_events(
                stream_id, 
                order.uncommitted_events,
                expected_version
            )
            
            order.mark_events_as_committed()
            
            self.logger.info(f"Saved order {order.aggregate_id} at version {new_version}")
            
        except Exception as e:
            self.logger.error(f"Failed to save order {order.aggregate_id}: {e}")
            raise
    
    async def get_by_id(self, order_id: str) -> Optional[OrderAggregate]:
        """Get order by ID"""
        try:
            order = await OrderAggregate.from_history(order_id, self.event_store)
            
            if order.version == -1:  # No events found
                return None
            
            return order
            
        except Exception as e:
            self.logger.error(f"Failed to load order {order_id}: {e}")
            raise

# Event Projections (Read Models)
class ProjectionManager:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
        self.projections = {}
        self.logger = logging.getLogger(__name__)
        self.last_processed_position = 0
    
    def register_projection(self, name: str, projection_class: Type['Projection']):
        """Register a projection"""
        self.projections[name] = projection_class()
        self.logger.info(f"Registered projection: {name}")
    
    async def rebuild_all_projections(self):
        """Rebuild all projections from scratch"""
        self.logger.info("Rebuilding all projections...")
        
        # Clear all projections
        for projection in self.projections.values():
            projection.reset()
        
        # Process all events
        events = await self.event_store.read_all_events(from_position=0, max_count=10000)
        
        for event in events:
            self.apply_event_to_projections(event)
        
        self.logger.info(f"Rebuilt {len(self.projections)} projections from {len(events)} events")
    
    async def update_projections(self):
        """Update projections with new events"""
        events = await self.event_store.read_all_events(
            from_position=self.last_processed_position,
            max_count=1000
        )
        
        for event in events:
            self.apply_event_to_projections(event)
            self.last_processed_position = max(self.last_processed_position, event.event_version)
        
        if events:
            self.logger.info(f"Updated projections with {len(events)} new events")
    
    def apply_event_to_projections(self, event: Event):
        """Apply event to all relevant projections"""
        for projection in self.projections.values():
            try:
                projection.handle_event(event)
            except Exception as e:
                self.logger.error(f"Error applying event {event.event_id} to projection: {e}")

class Projection(ABC):
    @abstractmethod
    def handle_event(self, event: Event):
        pass
    
    @abstractmethod
    def reset(self):
        pass

class OrderSummaryProjection(Projection):
    """Projection for order summary statistics"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.orders = {}
        self.customer_stats = {}
        self.product_stats = {}
    
    def handle_event(self, event: Event):
        event_type = event.event_type
        data = event.event_data
        
        if event_type == "OrderCreated":
            order_id = data["orderId"]
            customer_id = data["customerId"]
            
            self.orders[order_id] = {
                "orderId": order_id,
                "customerId": customer_id,
                "status": "draft",
                "totalAmount": 0,
                "itemCount": 0,
                "createdAt": data["createdAt"]
            }
            
            # Update customer stats
            if customer_id not in self.customer_stats:
                self.customer_stats[customer_id] = {
                    "totalOrders": 0,
                    "totalSpent": 0,
                    "firstOrderDate": data["createdAt"]
                }
        
        elif event_type == "ItemAdded":
            order_id = data["orderId"]
            product_id = data["productId"]
            quantity = data["quantity"]
            unit_price = data["unitPrice"]
            
            if order_id in self.orders:
                self.orders[order_id]["totalAmount"] += quantity * unit_price
                self.orders[order_id]["itemCount"] += quantity
                
                # Update product stats
                if product_id not in self.product_stats:
                    self.product_stats[product_id] = {
                        "totalQuantitySold": 0,
                        "totalRevenue": 0,
                        "orderCount": 0
                    }
                
                self.product_stats[product_id]["totalQuantitySold"] += quantity
                self.product_stats[product_id]["totalRevenue"] += quantity * unit_price
                self.product_stats[product_id]["orderCount"] += 1
        
        elif event_type == "OrderConfirmed":
            order_id = data["orderId"]
            if order_id in self.orders:
                self.orders[order_id]["status"] = "confirmed"
                self.orders[order_id]["confirmedAt"] = data["confirmedAt"]
        
        elif event_type == "PaymentProcessed":
            order_id = data["orderId"]
            if order_id in self.orders:
                self.orders[order_id]["status"] = "paid"
                
                # Update customer stats
                customer_id = self.orders[order_id]["customerId"]
                if customer_id in self.customer_stats:
                    self.customer_stats[customer_id]["totalOrders"] += 1
                    self.customer_stats[customer_id]["totalSpent"] += self.orders[order_id]["totalAmount"]
    
    def get_order_summary(self, order_id: str) -> Optional[Dict[str, Any]]:
        """Get order summary"""
        return self.orders.get(order_id)
    
    def get_customer_stats(self, customer_id: str) -> Optional[Dict[str, Any]]:
        """Get customer statistics"""
        return self.customer_stats.get(customer_id)
    
    def get_top_products(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get top-selling products"""
        sorted_products = sorted(
            self.product_stats.items(),
            key=lambda x: x[1]["totalRevenue"],
            reverse=True
        )
        
        return [
            {"productId": product_id, **stats} 
            for product_id, stats in sorted_products[:limit]
        ]

# Usage Example
async def event_sourcing_example():
    """Complete event sourcing example"""
    
    # Initialize event store
    event_store = SQLiteEventStore("orders.db")
    repository = OrderRepository(event_store)
    
    # Create new order
    order = OrderAggregate("ORD-001")
    order.create_order("CUST-123", {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "zipCode": "12345"
    })
    
    # Add items
    order.add_item("PROD-001", 2, 29.99)
    order.add_item("PROD-002", 1, 49.99)
    
    # Confirm order
    order.confirm_order()
    
    # Save order (persist events)
    await repository.save(order)
    
    # Process payment
    order.process_payment("PAY-001", order.total_amount)
    await repository.save(order)
    
    print(f"Order {order.aggregate_id} total: ${order.total_amount}")
    print(f"Order status: {order.status.value}")
    
    # Rebuild from events
    rebuilt_order = await repository.get_by_id("ORD-001")
    print(f"Rebuilt order status: {rebuilt_order.status.value}")
    print(f"Rebuilt order total: ${rebuilt_order.total_amount}")
    
    # Set up projections
    projection_manager = ProjectionManager(event_store)
    projection_manager.register_projection("order_summary", OrderSummaryProjection)
    
    await projection_manager.rebuild_all_projections()
    
    # Query projections
    order_summary_projection = projection_manager.projections["order_summary"]
    summary = order_summary_projection.get_order_summary("ORD-001")
    print(f"Order summary: {json.dumps(summary, indent=2)}")

# Run the example
if __name__ == "__main__":
    asyncio.run(event_sourcing_example())
```

---

## 🔄 CQRS Pattern Implementation {#cqrs}

### CQRS with Event Sourcing

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union
import json
import logging
from datetime import datetime
import asyncio
from dataclasses import dataclass

# Command side (Write Model)
class Command(ABC):
    pass

@dataclass
class CreateOrderCommand(Command):
    order_id: str
    customer_id: str
    shipping_address: Dict[str, str]

@dataclass
class AddItemToOrderCommand(Command):
    order_id: str
    product_id: str
    quantity: int
    unit_price: float

@dataclass
class ConfirmOrderCommand(Command):
    order_id: str

class CommandHandler(ABC):
    @abstractmethod
    async def handle(self, command: Command) -> Any:
        pass

class OrderCommandHandler(CommandHandler):
    def __init__(self, order_repository: OrderRepository, event_publisher):
        self.repository = order_repository
        self.event_publisher = event_publisher
        self.logger = logging.getLogger(__name__)
    
    async def handle(self, command: Command) -> Any:
        if isinstance(command, CreateOrderCommand):
            return await self._handle_create_order(command)
        elif isinstance(command, AddItemToOrderCommand):
            return await self._handle_add_item(command)
        elif isinstance(command, ConfirmOrderCommand):
            return await self._handle_confirm_order(command)
        else:
            raise ValueError(f"Unknown command type: {type(command)}")
    
    async def _handle_create_order(self, command: CreateOrderCommand) -> OrderAggregate:
        # Check if order already exists
        existing_order = await self.repository.get_by_id(command.order_id)
        if existing_order:
            raise ValueError(f"Order {command.order_id} already exists")
        
        # Create new order
        order = OrderAggregate(command.order_id)
        order.create_order(command.customer_id, command.shipping_address)
        
        # Save order
        await self.repository.save(order)
        
        # Publish domain events
        await self._publish_uncommitted_events(order)
        
        return order
    
    async def _handle_add_item(self, command: AddItemToOrderCommand) -> OrderAggregate:
        # Load order
        order = await self.repository.get_by_id(command.order_id)
        if not order:
            raise ValueError(f"Order {command.order_id} not found")
        
        # Add item
        order.add_item(command.product_id, command.quantity, command.unit_price)
        
        # Save order
        await self.repository.save(order, expected_version=order.version)
        
        # Publish events
        await self._publish_uncommitted_events(order)
        
        return order
    
    async def _handle_confirm_order(self, command: ConfirmOrderCommand) -> OrderAggregate:
        # Load order
        order = await self.repository.get_by_id(command.order_id)
        if not order:
            raise ValueError(f"Order {command.order_id} not found")
        
        # Confirm order
        order.confirm_order()
        
        # Save order
        await self.repository.save(order, expected_version=order.version)
        
        # Publish events
        await self._publish_uncommitted_events(order)
        
        return order
    
    async def _publish_uncommitted_events(self, order: OrderAggregate):
        """Publish domain events to message broker"""
        for event in order.uncommitted_events:
            await self.event_publisher.publish(
                topic="domain-events",
                event_type=event.event_type,
                event_data=event.event_data,
                metadata=event.metadata
            )

# Query side (Read Model)
class Query(ABC):
    pass

@dataclass
class GetOrderQuery(Query):
    order_id: str

@dataclass
class GetCustomerOrdersQuery(Query):
    customer_id: str
    limit: int = 10
    offset: int = 0

@dataclass
class GetOrdersByStatusQuery(Query):
    status: str
    limit: int = 10

class QueryHandler(ABC):
    @abstractmethod
    async def handle(self, query: Query) -> Any:
        pass

class OrderQueryHandler(QueryHandler):
    def __init__(self, read_model_store):
        self.read_model_store = read_model_store
        self.logger = logging.getLogger(__name__)
    
    async def handle(self, query: Query) -> Any:
        if isinstance(query, GetOrderQuery):
            return await self._handle_get_order(query)
        elif isinstance(query, GetCustomerOrdersQuery):
            return await self._handle_get_customer_orders(query)
        elif isinstance(query, GetOrdersByStatusQuery):
            return await self._handle_get_orders_by_status(query)
        else:
            raise ValueError(f"Unknown query type: {type(query)}")
    
    async def _handle_get_order(self, query: GetOrderQuery) -> Optional[Dict[str, Any]]:
        return await self.read_model_store.get_order(query.order_id)
    
    async def _handle_get_customer_orders(self, query: GetCustomerOrdersQuery) -> List[Dict[str, Any]]:
        return await self.read_model_store.get_customer_orders(
            query.customer_id, 
            query.limit, 
            query.offset
        )
    
    async def _handle_get_orders_by_status(self, query: GetOrdersByStatusQuery) -> List[Dict[str, Any]]:
        return await self.read_model_store.get_orders_by_status(query.status, query.limit)

# Read Model Store (Optimized for Queries)
class ReadModelStore:
    def __init__(self, db_connection_string: str):
        self.connection_string = db_connection_string
        self.logger = logging.getLogger(__name__)
        self._init_read_model_tables()
    
    def _init_read_model_tables(self):
        """Initialize read model tables optimized for queries"""
        # This would create denormalized tables optimized for specific queries
        pass
    
    async def get_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        """Get order with all related data in one query"""
        # Simulated query that joins order, customer, and product data
        return {
            "orderId": order_id,
            "customer": {
                "customerId": "CUST-123",
                "name": "John Doe",
                "email": "john@example.com"
            },
            "items": [
                {
                    "productId": "PROD-001",
                    "productName": "Widget",
                    "quantity": 2,
                    "unitPrice": 29.99,
                    "totalPrice": 59.98
                }
            ],
            "totalAmount": 59.98,
            "status": "confirmed",
            "createdAt": "2024-01-15T10:00:00Z"
        }
    
    async def get_customer_orders(self, customer_id: str, limit: int, offset: int) -> List[Dict[str, Any]]:
        """Get orders for customer with pagination"""
        # Optimized query with denormalized data
        return [
            {
                "orderId": f"ORD-{i:03d}",
                "totalAmount": 100.0 + i * 25,
                "status": "paid",
                "itemCount": i + 1,
                "createdAt": f"2024-01-{i+1:02d}T10:00:00Z"
            }
            for i in range(limit)
        ]
    
    async def get_orders_by_status(self, status: str, limit: int) -> List[Dict[str, Any]]:
        """Get orders by status"""
        return [
            {
                "orderId": f"ORD-{status.upper()}-{i:03d}",
                "customerId": f"CUST-{i:03d}",
                "totalAmount": 150.0 + i * 30,
                "status": status,
                "createdAt": f"2024-01-15T{10+i:02d}:00:00Z"
            }
            for i in range(min(limit, 5))
        ]

# Read Model Event Handlers (Eventually Consistent)
class ReadModelEventHandler:
    def __init__(self, read_model_store: ReadModelStore):
        self.read_model_store = read_model_store
        self.logger = logging.getLogger(__name__)
    
    async def handle_order_created(self, event: Event):
        """Update read model when order is created"""
        data = event.event_data
        
        # Insert into denormalized order table
        order_record = {
            "order_id": data["orderId"],
            "customer_id": data["customerId"],
            "status": "draft",
            "total_amount": 0,
            "item_count": 0,
            "created_at": data["createdAt"],
            "updated_at": event.timestamp
        }
        
        # In real implementation, this would update the database
        self.logger.info(f"Updated read model for order creation: {data['orderId']}")
    
    async def handle_item_added(self, event: Event):
        """Update read model when item is added"""
        data = event.event_data
        order_id = data["orderId"]
        
        # Update order totals in read model
        # This would be an UPDATE query in real implementation
        self.logger.info(f"Updated read model for item addition to order: {order_id}")
    
    async def handle_order_confirmed(self, event: Event):
        """Update read model when order is confirmed"""
        data = event.event_data
        order_id = data["orderId"]
        
        # Update status in read model
        self.logger.info(f"Updated read model for order confirmation: {order_id}")

# CQRS Bus (Mediator Pattern)
class CQRSBus:
    def __init__(self):
        self.command_handlers = {}
        self.query_handlers = {}
        self.logger = logging.getLogger(__name__)
    
    def register_command_handler(self, command_type: Type[Command], handler: CommandHandler):
        self.command_handlers[command_type] = handler
    
    def register_query_handler(self, query_type: Type[Query], handler: QueryHandler):
        self.query_handlers[query_type] = handler
    
    async def send_command(self, command: Command) -> Any:
        """Send command to appropriate handler"""
        command_type = type(command)
        
        if command_type not in self.command_handlers:
            raise ValueError(f"No handler registered for command {command_type.__name__}")
        
        handler = self.command_handlers[command_type]
        
        self.logger.info(f"Sending command: {command_type.__name__}")
        
        try:
            result = await handler.handle(command)
            self.logger.info(f"Command {command_type.__name__} handled successfully")
            return result
        except Exception as e:
            self.logger.error(f"Command {command_type.__name__} failed: {e}")
            raise
    
    async def send_query(self, query: Query) -> Any:
        """Send query to appropriate handler"""
        query_type = type(query)
        
        if query_type not in self.query_handlers:
            raise ValueError(f"No handler registered for query {query_type.__name__}")
        
        handler = self.query_handlers[query_type]
        
        self.logger.info(f"Sending query: {query_type.__name__}")
        
        try:
            result = await handler.handle(query)
            self.logger.info(f"Query {query_type.__name__} handled successfully")
            return result
        except Exception as e:
            self.logger.error(f"Query {query_type.__name__} failed: {e}")
            raise

# Complete CQRS Example
async def cqrs_example():
    """Complete CQRS example with event sourcing"""
    
    # Set up components
    event_store = SQLiteEventStore("cqrs_orders.db")
    order_repository = OrderRepository(event_store)
    read_model_store = ReadModelStore("sqlite:///read_model.db")
    
    # Set up CQRS bus
    bus = CQRSBus()
    
    # Register handlers
    order_command_handler = OrderCommandHandler(order_repository, None)
    order_query_handler = OrderQueryHandler(read_model_store)
    
    bus.register_command_handler(CreateOrderCommand, order_command_handler)
    bus.register_command_handler(AddItemToOrderCommand, order_command_handler)
    bus.register_command_handler(ConfirmOrderCommand, order_command_handler)
    
    bus.register_query_handler(GetOrderQuery, order_query_handler)
    bus.register_query_handler(GetCustomerOrdersQuery, order_query_handler)
    bus.register_query_handler(GetOrdersByStatusQuery, order_query_handler)
    
    # Command side (Write operations)
    print("=== Command Side (Write Operations) ===")
    
    # Create order
    create_command = CreateOrderCommand(
        order_id="ORD-CQRS-001",
        customer_id="CUST-123",
        shipping_address={
            "street": "123 Main St",
            "city": "Anytown",
            "zipCode": "12345"
        }
    )
    
    order = await bus.send_command(create_command)
    print(f"Created order: {order.aggregate_id}")
    
    # Add items
    add_item_command = AddItemToOrderCommand(
        order_id="ORD-CQRS-001",
        product_id="PROD-001",
        quantity=2,
        unit_price=29.99
    )
    
    await bus.send_command(add_item_command)
    print("Added item to order")
    
    # Confirm order
    confirm_command = ConfirmOrderCommand(order_id="ORD-CQRS-001")
    await bus.send_command(confirm_command)
    print("Confirmed order")
    
    # Query side (Read operations)
    print("\n=== Query Side (Read Operations) ===")
    
    # Get order details
    get_order_query = GetOrderQuery(order_id="ORD-CQRS-001")
    order_details = await bus.send_query(get_order_query)
    print(f"Order details: {json.dumps(order_details, indent=2)}")
    
    # Get customer orders
    customer_orders_query = GetCustomerOrdersQuery(customer_id="CUST-123", limit=5)
    customer_orders = await bus.send_query(customer_orders_query)
    print(f"Customer orders: {len(customer_orders)} orders")
    
    # Get orders by status
    status_query = GetOrdersByStatusQuery(status="confirmed", limit=10)
    confirmed_orders = await bus.send_query(status_query)
    print(f"Confirmed orders: {len(confirmed_orders)} orders")

if __name__ == "__main__":
    asyncio.run(cqrs_example())
```

---

## ⚖️ Saga Pattern for Distributed Transactions {#saga}

### Orchestration-Based Saga

```python
from enum import Enum
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass
import asyncio
import json
import logging
from datetime import datetime, timedelta
import uuid

class SagaStepStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    COMPENSATED = "compensated"

@dataclass
class SagaStep:
    step_id: str
    name: str
    action: Callable
    compensation: Callable
    status: SagaStepStatus = SagaStepStatus.PENDING
    result: Any = None
    error: str = None

class SagaStatus(Enum):
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    COMPENSATING = "compensating"
    COMPENSATED = "compensated"

class SagaOrchestrator:
    def __init__(self, saga_id: str, saga_name: str):
        self.saga_id = saga_id
        self.saga_name = saga_name
        self.steps: List[SagaStep] = []
        self.status = SagaStatus.RUNNING
        self.start_time = datetime.now()
        self.end_time: Optional[datetime] = None
        self.context: Dict[str, Any] = {}
        self.logger = logging.getLogger(__name__)
    
    def add_step(self, name: str, action: Callable, compensation: Callable) -> 'SagaOrchestrator':
        """Add step to saga"""
        step = SagaStep(
            step_id=str(uuid.uuid4()),
            name=name,
            action=action,
            compensation=compensation
        )
        self.steps.append(step)
        return self
    
    async def execute(self) -> bool:
        """Execute saga steps"""
        self.logger.info(f"Starting saga {self.saga_name} ({self.saga_id})")
        
        try:
            # Execute steps sequentially
            for i, step in enumerate(self.steps):
                self.logger.info(f"Executing step {i+1}/{len(self.steps)}: {step.name}")
                
                try:
                    # Execute step action
                    step.result = await step.action(self.context)
                    step.status = SagaStepStatus.COMPLETED
                    
                    self.logger.info(f"Step {step.name} completed successfully")
                    
                except Exception as e:
                    step.status = SagaStepStatus.FAILED
                    step.error = str(e)
                    
                    self.logger.error(f"Step {step.name} failed: {e}")
                    
                    # Start compensation
                    await self._compensate_completed_steps(i)
                    
                    self.status = SagaStatus.COMPENSATED
                    self.end_time = datetime.now()
                    
                    return False
            
            # All steps completed successfully
            self.status = SagaStatus.COMPLETED
            self.end_time = datetime.now()
            
            duration = (self.end_time - self.start_time).total_seconds()
            self.logger.info(f"Saga {self.saga_name} completed successfully in {duration:.2f} seconds")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Saga {self.saga_name} failed with unexpected error: {e}")
            self.status = SagaStatus.FAILED
            self.end_time = datetime.now()
            return False
    
    async def _compensate_completed_steps(self, failed_step_index: int):
        """Execute compensation actions for completed steps"""
        self.logger.info(f"Starting compensation for {failed_step_index} completed steps")
        self.status = SagaStatus.COMPENSATING
        
        # Compensate in reverse order
        for i in range(failed_step_index - 1, -1, -1):
            step = self.steps[i]
            
            if step.status == SagaStepStatus.COMPLETED:
                try:
                    self.logger.info(f"Compensating step: {step.name}")
                    await step.compensation(step.result, self.context)
                    step.status = SagaStepStatus.COMPENSATED
                    
                    self.logger.info(f"Step {step.name} compensated successfully")
                    
                except Exception as e:
                    self.logger.error(f"Compensation failed for step {step.name}: {e}")
                    # Continue with other compensations
    
    def get_status(self) -> Dict[str, Any]:
        """Get saga execution status"""
        return {
            "sagaId": self.saga_id,
            "sagaName": self.saga_name,
            "status": self.status.value,
            "startTime": self.start_time.isoformat(),
            "endTime": self.end_time.isoformat() if self.end_time else None,
            "duration": (self.end_time - self.start_time).total_seconds() if self.end_time else None,
            "steps": [
                {
                    "stepId": step.step_id,
                    "name": step.name,
                    "status": step.status.value,
                    "error": step.error
                }
                for step in self.steps
            ]
        }

# E-commerce Order Processing Saga Example
class OrderProcessingSaga:
    def __init__(self, order_service, inventory_service, payment_service, shipping_service):
        self.order_service = order_service
        self.inventory_service = inventory_service
        self.payment_service = payment_service
        self.shipping_service = shipping_service
        self.logger = logging.getLogger(__name__)
    
    async def create_order_saga(self, order_data: Dict[str, Any]) -> SagaOrchestrator:
        """Create saga for order processing"""
        
        saga_id = f"saga-{order_data['orderId']}"
        saga = SagaOrchestrator(saga_id, "OrderProcessing")
        
        # Step 1: Create Order
        saga.add_step(
            name="CreateOrder",
            action=self._create_order,
            compensation=self._cancel_order
        )
        
        # Step 2: Reserve Inventory
        saga.add_step(
            name="ReserveInventory", 
            action=self._reserve_inventory,
            compensation=self._release_inventory
        )
        
        # Step 3: Process Payment
        saga.add_step(
            name="ProcessPayment",
            action=self._process_payment,
            compensation=self._refund_payment
        )
        
        # Step 4: Ship Order
        saga.add_step(
            name="ShipOrder",
            action=self._ship_order,
            compensation=self._cancel_shipment
        )
        
        # Initialize context with order data
        saga.context = order_data.copy()
        
        return saga
    
    async def _create_order(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Step 1: Create order"""
        result = await self.order_service.create_order({
            'orderId': context['orderId'],
            'customerId': context['customerId'],
            'items': context['items']
        })
        
        # Update context with created order
        context['createdOrder'] = result
        
        return result
    
    async def _cancel_order(self, order_result: Dict[str, Any], context: Dict[str, Any]):
        """Compensation 1: Cancel order"""
        await self.order_service.cancel_order(order_result['orderId'])
        self.logger.info(f"Cancelled order {order_result['orderId']}")
    
    async def _reserve_inventory(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Step 2: Reserve inventory"""
        result = await self.inventory_service.reserve_items({
            'orderId': context['orderId'],
            'items': context['items']
        })
        
        context['reservationId'] = result['reservationId']
        
        return result
    
    async def _release_inventory(self, reservation_result: Dict[str, Any], context: Dict[str, Any]):
        """Compensation 2: Release inventory"""
        await self.inventory_service.release_reservation(context['reservationId'])
        self.logger.info(f"Released inventory reservation {context['reservationId']}")
    
    async def _process_payment(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Step 3: Process payment"""
        result = await self.payment_service.charge({
            'orderId': context['orderId'],
            'customerId': context['customerId'],
            'amount': context['totalAmount'],
            'paymentMethod': context['paymentMethod']
        })
        
        context['paymentId'] = result['paymentId']
        context['chargeId'] = result['chargeId']
        
        return result
    
    async def _refund_payment(self, payment_result: Dict[str, Any], context: Dict[str, Any]):
        """Compensation 3: Refund payment"""
        await self.payment_service.refund({
            'paymentId': context['paymentId'],
            'chargeId': context['chargeId'],
            'amount': context['totalAmount']
        })
        self.logger.info(f"Refunded payment {context['paymentId']}")
    
    async def _ship_order(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Step 4: Ship order"""
        result = await self.shipping_service.ship_order({
            'orderId': context['orderId'],
            'items': context['items'],
            'shippingAddress': context['shippingAddress']
        })
        
        context['shippingId'] = result['shippingId']
        context['trackingNumber'] = result['trackingNumber']
        
        return result
    
    async def _cancel_shipment(self, shipping_result: Dict[str, Any], context: Dict[str, Any]):
        """Compensation 4: Cancel shipment"""
        await self.shipping_service.cancel_shipment(context['shippingId'])
        self.logger.info(f"Cancelled shipment {context['shippingId']}")

# Mock Services for Demo
class MockOrderService:
    async def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0.1)  # Simulate processing time
        return {"orderId": order_data['orderId'], "status": "created"}
    
    async def cancel_order(self, order_id: str):
        await asyncio.sleep(0.1)
        print(f"Order {order_id} cancelled")

class MockInventoryService:
    async def reserve_items(self, request: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0.2)
        
        # Simulate occasional inventory shortage
        if request['orderId'] == 'ORD-FAIL-INVENTORY':
            raise Exception("Insufficient inventory")
        
        return {"reservationId": f"RES-{request['orderId']}", "status": "reserved"}
    
    async def release_reservation(self, reservation_id: str):
        await asyncio.sleep(0.1)
        print(f"Released reservation {reservation_id}")

class MockPaymentService:
    async def charge(self, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0.3)
        
        # Simulate payment failure for high amounts
        if payment_data['amount'] > 10000:
            raise Exception("Payment declined - amount too high")
        
        payment_id = f"PAY-{payment_data['orderId']}"
        charge_id = f"CHG-{str(uuid.uuid4())[:8]}"
        
        return {
            "paymentId": payment_id,
            "chargeId": charge_id,
            "status": "charged"
        }
    
    async def refund(self, refund_data: Dict[str, Any]):
        await asyncio.sleep(0.2)
        print(f"Refunded payment {refund_data['paymentId']} amount ${refund_data['amount']}")

class MockShippingService:
    async def ship_order(self, shipping_data: Dict[str, Any]) -> Dict[str, Any]:
        await asyncio.sleep(0.4)
        
        # Simulate shipping failure
        if shipping_data['orderId'] == 'ORD-FAIL-SHIPPING':
            raise Exception("Shipping service unavailable")
        
        return {
            "shippingId": f"SHIP-{shipping_data['orderId']}",
            "trackingNumber": f"TRK{random.randint(100000, 999999)}",
            "status": "shipped"
        }
    
    async def cancel_shipment(self, shipping_id: str):
        await asyncio.sleep(0.1)
        print(f"Cancelled shipment {shipping_id}")

# Saga Manager for Multiple Sagas
class SagaManager:
    def __init__(self):
        self.active_sagas: Dict[str, SagaOrchestrator] = {}
        self.completed_sagas: Dict[str, SagaOrchestrator] = {}
        self.logger = logging.getLogger(__name__)
    
    async def start_saga(self, saga: SagaOrchestrator) -> bool:
        """Start executing a saga"""
        self.active_sagas[saga.saga_id] = saga
        
        try:
            success = await saga.execute()
            
            # Move to completed
            self.completed_sagas[saga.saga_id] = saga
            del self.active_sagas[saga.saga_id]
            
            return success
            
        except Exception as e:
            self.logger.error(f"Saga {saga.saga_id} failed with error: {e}")
            saga.status = SagaStatus.FAILED
            self.completed_sagas[saga.saga_id] = saga
            del self.active_sagas[saga.saga_id]
            return False
    
    def get_saga_status(self, saga_id: str) -> Optional[Dict[str, Any]]:
        """Get status of a saga"""
        if saga_id in self.active_sagas:
            return self.active_sagas[saga_id].get_status()
        elif saga_id in self.completed_sagas:
            return self.completed_sagas[saga_id].get_status()
        else:
            return None
    
    def get_active_sagas(self) -> List[Dict[str, Any]]:
        """Get all active sagas"""
        return [saga.get_status() for saga in self.active_sagas.values()]

# Complete Example Usage
async def saga_example():
    """Complete saga pattern example"""
    
    # Initialize services
    order_service = MockOrderService()
    inventory_service = MockInventoryService() 
    payment_service = MockPaymentService()
    shipping_service = MockShippingService()
    
    # Initialize saga processor
    saga_processor = OrderProcessingSaga(
        order_service, inventory_service, payment_service, shipping_service
    )
    
    # Initialize saga manager
    saga_manager = SagaManager()
    
    # Test successful saga
    print("=== Testing Successful Order Processing Saga ===")
    
    order_data_success = {
        'orderId': 'ORD-SUCCESS-001',
        'customerId': 'CUST-123',
        'items': [
            {'productId': 'PROD-001', 'quantity': 2, 'price': 29.99},
            {'productId': 'PROD-002', 'quantity': 1, 'price': 49.99}
        ],
        'totalAmount': 109.97,
        'paymentMethod': 'credit_card',
        'shippingAddress': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zipCode': '12345'
        }
    }
    
    success_saga = await saga_processor.create_order_saga(order_data_success)
    success_result = await saga_manager.start_saga(success_saga)
    
    print(f"Success saga result: {success_result}")
    print(f"Success saga status: {json.dumps(success_saga.get_status(), indent=2)}")
    
    # Test failed saga (payment failure)
    print("\n=== Testing Failed Saga with Compensation ===")
    
    order_data_fail = {
        'orderId': 'ORD-FAIL-001',
        'customerId': 'CUST-456', 
        'items': [
            {'productId': 'PROD-003', 'quantity': 1, 'price': 15000.00}  # High amount will fail
        ],
        'totalAmount': 15000.00,
        'paymentMethod': 'credit_card',
        'shippingAddress': {
            'street': '456 Oak Ave',
            'city': 'Other Town',
            'zipCode': '67890'
        }
    }
    
    fail_saga = await saga_processor.create_order_saga(order_data_fail)
    fail_result = await saga_manager.start_saga(fail_saga)
    
    print(f"Fail saga result: {fail_result}")
    print(f"Fail saga status: {json.dumps(fail_saga.get_status(), indent=2)}")
    
    # Test inventory failure
    print("\n=== Testing Inventory Failure Saga ===")
    
    inventory_fail_data = {
        'orderId': 'ORD-FAIL-INVENTORY',
        'customerId': 'CUST-789',
        'items': [
            {'productId': 'PROD-004', 'quantity': 100, 'price': 25.00}
        ],
        'totalAmount': 2500.00,
        'paymentMethod': 'credit_card',
        'shippingAddress': {
            'street': '789 Pine St',
            'city': 'Inventory Town', 
            'zipCode': '11111'
        }
    }
    
    inventory_fail_saga = await saga_processor.create_order_saga(inventory_fail_data)
    inventory_fail_result = await saga_manager.start_saga(inventory_fail_saga)
    
    print(f"Inventory fail saga result: {inventory_fail_result}")
    print(f"Inventory fail saga status: {json.dumps(inventory_fail_saga.get_status(), indent=2)}")

# Choreography-Based Saga (Alternative Pattern)
class ChoreographySaga:
    """Saga using choreography where each service knows what to do next"""
    
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher
        self.logger = logging.getLogger(__name__)
    
    # Order Service Handler
    async def handle_order_create_requested(self, event: Dict[str, Any]):
        """Handle order creation request"""
        try:
            order_data = event['data']
            
            # Create order
            order = await self._create_order(order_data)
            
            # Publish success event
            await self.event_publisher.publish('order.created', {
                'orderId': order['orderId'],
                'customerId': order['customerId'],
                'items': order['items'],
                'totalAmount': order['totalAmount']
            })
            
        except Exception as e:
            # Publish failure event
            await self.event_publisher.publish('order.creation.failed', {
                'orderId': order_data['orderId'],
                'error': str(e)
            })
    
    # Inventory Service Handler  
    async def handle_order_created(self, event: Dict[str, Any]):
        """Handle order created event (inventory service)"""
        try:
            order_data = event['data']
            
            # Reserve inventory
            reservation = await self._reserve_inventory(order_data['items'])
            
            # Publish success event
            await self.event_publisher.publish('inventory.reserved', {
                'orderId': order_data['orderId'],
                'reservationId': reservation['reservationId'],
                'items': order_data['items']
            })
            
        except Exception as e:
            # Publish failure event - triggers order cancellation
            await self.event_publisher.publish('inventory.reservation.failed', {
                'orderId': order_data['orderId'],
                'error': str(e)
            })
    
    # Payment Service Handler
    async def handle_inventory_reserved(self, event: Dict[str, Any]):
        """Handle inventory reserved event (payment service)"""
        try:
            order_data = event['data']
            
            # Process payment
            payment = await self._process_payment(order_data)
            
            # Publish success event
            await self.event_publisher.publish('payment.processed', {
                'orderId': order_data['orderId'],
                'paymentId': payment['paymentId'],
                'amount': payment['amount']
            })
            
        except Exception as e:
            # Publish failure event - triggers compensation
            await self.event_publisher.publish('payment.failed', {
                'orderId': order_data['orderId'],
                'error': str(e)
            })
    
    # Compensation Handlers
    async def handle_payment_failed(self, event: Dict[str, Any]):
        """Handle payment failure - compensate inventory"""
        order_id = event['data']['orderId']
        
        # Release inventory reservation
        await self.event_publisher.publish('inventory.release.requested', {
            'orderId': order_id,
            'reason': 'payment_failed'
        })
    
    async def handle_inventory_reservation_failed(self, event: Dict[str, Any]):
        """Handle inventory failure - compensate order"""
        order_id = event['data']['orderId']
        
        # Cancel order
        await self.event_publisher.publish('order.cancel.requested', {
            'orderId': order_id,
            'reason': 'inventory_unavailable'
        })

# Performance testing and metrics
import time
import random

async def test_saga_performance():
    """Test saga performance under load"""
    
    # Mock services
    order_service = MockOrderService()
    inventory_service = MockInventoryService()
    payment_service = MockPaymentService()
    shipping_service = MockShippingService()
    
    saga_processor = OrderProcessingSaga(
        order_service, inventory_service, payment_service, shipping_service
    )
    
    saga_manager = SagaManager()
    
    # Generate test orders
    orders = []
    for i in range(100):
        order_data = {
            'orderId': f'ORD-PERF-{i:03d}',
            'customerId': f'CUST-{i % 20:03d}',  # 20 different customers
            'items': [
                {
                    'productId': f'PROD-{random.randint(1, 50):03d}',
                    'quantity': random.randint(1, 5),
                    'price': round(random.uniform(10, 200), 2)
                }
            ],
            'totalAmount': 0,  # Will be calculated
            'paymentMethod': 'credit_card',
            'shippingAddress': {
                'street': f'{i+1} Test St',
                'city': 'Test City',
                'zipCode': f'{12345 + i:05d}'
            }
        }
        
        # Calculate total
        order_data['totalAmount'] = sum(
            item['quantity'] * item['price'] for item in order_data['items']
        )
        
        orders.append(order_data)
    
    # Execute sagas concurrently
    start_time = time.time()
    
    tasks = []
    for order_data in orders:
        saga = await saga_processor.create_order_saga(order_data)
        task = asyncio.create_task(saga_manager.start_saga(saga))
        tasks.append(task)
    
    # Wait for all sagas to complete
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = time.time()
    duration = end_time - start_time
    
    # Calculate metrics
    successful = sum(1 for result in results if result is True)
    failed = sum(1 for result in results if result is False or isinstance(result, Exception))
    
    print(f"\n=== Saga Performance Test Results ===")
    print(f"Total sagas: {len(orders)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {successful / len(orders) * 100:.1f}%")
    print(f"Total duration: {duration:.2f} seconds")
    print(f"Throughput: {len(orders) / duration:.2f} sagas/second")
    print(f"Average duration per saga: {duration / len(orders) * 1000:.2f} ms")

if __name__ == "__main__":
    # Run examples
    print("Running Saga Pattern Examples...")
    asyncio.run(saga_example())
    
    print("\nRunning Performance Test...")
    asyncio.run(test_saga_performance())
```

---

## 🧪 Testing Event-Driven Systems {#testing}

### Unit Testing for Event-Driven Components

```python
import unittest
from unittest.mock import Mock, AsyncMock, patch
import json
from datetime import datetime
import pytest
import asyncio

class TestOrderAggregate(unittest.TestCase):
    def setUp(self):
        self.order = OrderAggregate("TEST-ORDER-001")
    
    def test_create_order(self):
        """Test order creation"""
        customer_id = "CUST-123"
        shipping_address = {"street": "123 Test St", "city": "Test City"}
        
        self.order.create_order(customer_id, shipping_address)
        
        # Verify state changes
        self.assertEqual(self.order.customer_id, customer_id)
        self.assertEqual(self.order.shipping_address, shipping_address)
        self.assertEqual(self.order.status, OrderStatus.DRAFT)
        
        # Verify event was raised
        self.assertEqual(len(self.order.uncommitted_events), 1)
        event = self.order.uncommitted_events[0]
        self.assertEqual(event.event_type, "OrderCreated")
        self.assertEqual(event.event_data["customerId"], customer_id)
    
    def test_add_item(self):
        """Test adding item to order"""
        # Create order first
        self.order.create_order("CUST-123", {"street": "123 Test St"})
        
        # Add item
        self.order.add_item("PROD-001", 2, 29.99)
        
        # Verify state
        self.assertEqual(len(self.order.items), 1)
        item = self.order.items[0]
        self.assertEqual(item.product_id, "PROD-001")
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.unit_price, 29.99)
        self.assertEqual(self.order.total_amount, 59.98)
        
        # Verify events
        self.assertEqual(len(self.order.uncommitted_events), 2)
        self.assertEqual(self.order.uncommitted_events[1].event_type, "ItemAdded")
    
    def test_cannot_add_item_to_confirmed_order(self):
        """Test that items cannot be added to confirmed order"""
        # Create and confirm order
        self.order.create_order("CUST-123", {"street": "123 Test St"})
        self.order.add_item("PROD-001", 1, 29.99)
        self.order.confirm_order()
        
        # Try to add item - should fail
        with self.assertRaises(ValueError) as context:
            self.order.add_item("PROD-002", 1, 19.99)
        
        self.assertIn("Cannot add items to order in status confirmed", str(context.exception))
    
    def test_event_sourcing_rebuild(self):
        """Test rebuilding order from events"""
        # Create order and perform actions
        self.order.create_order("CUST-123", {"street": "123 Test St"})
        self.order.add_item("PROD-001", 2, 29.99)
        self.order.add_item("PROD-002", 1, 49.99)
        self.order.confirm_order()
        
        # Get events
        events = self.order.uncommitted_events
        
        # Rebuild order from events
        rebuilt_order = OrderAggregate("TEST-ORDER-001")
        for event in events:
            rebuilt_order.apply_event(event)
        
        # Verify rebuilt state matches original
        self.assertEqual(rebuilt_order.status, self.order.status)
        self.assertEqual(rebuilt_order.total_amount, self.order.total_amount)
        self.assertEqual(len(rebuilt_order.items), len(self.order.items))

class TestEventPublisher(unittest.TestCase):
    def setUp(self):
        self.event_publisher = Mock()
    
    @patch('kafka.KafkaProducer')
    def test_publish_event(self, mock_producer):
        """Test event publishing"""
        # Setup mock
        mock_producer_instance = Mock()
        mock_producer.return_value = mock_producer_instance
        mock_future = Mock()
        mock_producer_instance.send.return_value = mock_future
        
        # Create real publisher
        from your_event_module import KafkaEventPublisher
        publisher = KafkaEventPublisher(['localhost:9092'])
        
        # Publish event
        event_data = {
            'eventType': 'OrderCreated',
            'data': {'orderId': 'TEST-001'}
        }
        
        publisher.publish('orders', event_data)
        
        # Verify send was called
        mock_producer_instance.send.assert_called_once()
        call_args = mock_producer_instance.send.call_args
        
        self.assertEqual(call_args[1]['topic'], 'orders')
        sent_data = json.loads(call_args[1]['value'])
        self.assertEqual(sent_data['eventType'], 'OrderCreated')

# Integration Testing
@pytest.mark.asyncio
class TestEventIntegration:
    async def test_end_to_end_order_flow(self):
        """Test complete order flow with real message broker"""
        
        # Setup test environment
        event_store = SQLiteEventStore(":memory:")  # In-memory for testing
        repository = OrderRepository(event_store)
        
        # Create order
        order = OrderAggregate("INTEGRATION-001")
        order.create_order("CUST-999", {"street": "999 Test Ave"})
        order.add_item("PROD-999", 1, 99.99)
        order.confirm_order()
        
        # Save order
        await repository.save(order)
        
        # Verify order was saved
        loaded_order = await repository.get_by_id("INTEGRATION-001")
        
        assert loaded_order is not None
        assert loaded_order.status == OrderStatus.CONFIRMED
        assert loaded_order.total_amount == 99.99
    
    async def test_saga_compensation(self):
        """Test saga compensation flow"""
        
        # Mock services that will fail at payment step
        order_service = AsyncMock()
        inventory_service = AsyncMock()
        payment_service = AsyncMock()
        shipping_service = AsyncMock()
        
        # Configure mocks
        order_service.create_order.return_value = {"orderId": "TEST-001", "status": "created"}
        inventory_service.reserve_items.return_value = {"reservationId": "RES-001"}
        payment_service.charge.side_effect = Exception("Payment declined")
        
        # Create saga
        saga_processor = OrderProcessingSaga(
            order_service, inventory_service, payment_service, shipping_service
        )
        
        order_data = {
            'orderId': 'TEST-001',
            'customerId': 'CUST-TEST',
            'items': [{'productId': 'PROD-TEST', 'quantity': 1, 'price': 50.0}],
            'totalAmount': 50.0,
            'paymentMethod': 'credit_card',
            'shippingAddress': {'street': 'Test St'}
        }
        
        saga = await saga_processor.create_order_saga(order_data)
        
        # Execute saga (should fail at payment and compensate)
        result = await saga.execute()
        
        # Verify compensation was called
        assert result is False
        assert saga.status == SagaStatus.COMPENSATED
        
        # Verify service calls
        order_service.create_order.assert_called_once()
        inventory_service.reserve_items.assert_called_once()
        payment_service.charge.assert_called_once()
        
        # Verify compensation calls
        inventory_service.release_reservation.assert_called_once()
        order_service.cancel_order.assert_called_once()

# Contract Testing for Event Schemas
class TestEventContracts(unittest.TestCase):
    def test_order_created_event_schema(self):
        """Test OrderCreated event schema compliance"""
        
        event = {
            "eventId": "evt-123",
            "eventType": "OrderCreated",
            "timestamp": "2024-01-15T10:00:00Z",
            "data": {
                "orderId": "ORD-001",
                "customerId": "CUST-123",
                "totalAmount": 99.99,
                "currency": "USD"
            }
        }
        
        # Schema validation
        required_fields = ["eventId", "eventType", "timestamp", "data"]
        for field in required_fields:
            self.assertIn(field, event, f"Missing required field: {field}")
        
        # Data field validation
        data_required_fields = ["orderId", "customerId", "totalAmount"]
        for field in data_required_fields:
            self.assertIn(field, event["data"], f"Missing required data field: {field}")
        
        # Type validation
        self.assertIsInstance(event["data"]["totalAmount"], (int, float))
        self.assertIsInstance(event["data"]["orderId"], str)
    
    def test_event_backward_compatibility(self):
        """Test that new event versions are backward compatible"""
        
        # Old version event
        old_event = {
            "eventType": "OrderCreated",
            "data": {
                "orderId": "ORD-001",
                "customerId": "CUST-123"
            }
        }
        
        # New version event with additional fields
        new_event = {
            "eventType": "OrderCreated",
            "eventVersion": "2.0",  # New field
            "data": {
                "orderId": "ORD-001",
                "customerId": "CUST-123",
                "customerSegment": "premium"  # New field
            }
        }
        
        # Both should be processable by consumers
        self.assertTrue(self._can_process_order_created_event(old_event))
        self.assertTrue(self._can_process_order_created_event(new_event))
    
    def _can_process_order_created_event(self, event):
        """Simulate event processing"""
        try:
            # Required fields check
            assert "orderId" in event["data"]
            assert "customerId" in event["data"]
            return True
        except:
            return False

# Load Testing for Event Systems
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

class EventSystemLoadTester:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher
        self.metrics = {
            'events_sent': 0,
            'events_failed': 0,
            'total_latency_ms': 0,
            'max_latency_ms': 0,
            'min_latency_ms': float('inf')
        }
    
    async def generate_load(self, events_per_second: int, duration_seconds: int):
        """Generate load on event system"""
        
        total_events = events_per_second * duration_seconds
        delay_between_events = 1.0 / events_per_second
        
        print(f"Generating {events_per_second} events/second for {duration_seconds} seconds")
        print(f"Total events: {total_events}")
        
        start_time = time.time()
        
        for i in range(total_events):
            event_start_time = time.time()
            
            try:
                # Generate event
                event = {
                    'eventId': f'load-test-{i:06d}',
                    'eventType': 'LoadTestEvent',
                    'timestamp': datetime.now().isoformat(),
                    'data': {
                        'sequenceNumber': i,
                        'timestamp': time.time(),
                        'payload': 'test-data' * 10  # Some payload
                    }
                }
                
                # Publish event
                await self.event_publisher.publish('load-test', event)
                
                # Calculate latency
                latency_ms = (time.time() - event_start_time) * 1000
                
                # Update metrics
                self.metrics['events_sent'] += 1
                self.metrics['total_latency_ms'] += latency_ms
                self.metrics['max_latency_ms'] = max(self.metrics['max_latency_ms'], latency_ms)
                self.metrics['min_latency_ms'] = min(self.metrics['min_latency_ms'], latency_ms)
                
            except Exception as e:
                self.metrics['events_failed'] += 1
                print(f"Failed to send event {i}: {e}")
            
            # Control rate
            await asyncio.sleep(delay_between_events)
        
        total_duration = time.time() - start_time
        
        # Print results
        self._print_load_test_results(total_duration)
    
    def _print_load_test_results(self, duration: float):
        """Print load test results"""
        total_events = self.metrics['events_sent'] + self.metrics['events_failed']
        success_rate = self.metrics['events_sent'] / total_events * 100 if total_events > 0 else 0
        avg_latency = self.metrics['total_latency_ms'] / self.metrics['events_sent'] if self.metrics['events_sent'] > 0 else 0
        throughput = total_events / duration
        
        print(f"\n=== Load Test Results ===")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Total events: {total_events}")
        print(f"Events sent: {self.metrics['events_sent']}")
        print(f"Events failed: {self.metrics['events_failed']}")
        print(f"Success rate: {success_rate:.2f}%")
        print(f"Throughput: {throughput:.2f} events/second")
        print(f"Latency - Avg: {avg_latency:.2f}ms, Min: {self.metrics['min_latency_ms']:.2f}ms, Max: {self.metrics['max_latency_ms']:.2f}ms")

# Chaos Testing for Resilience
class ChaosTestRunner:
    def __init__(self, event_system):
        self.event_system = event_system
        self.logger = logging.getLogger(__name__)
    
    async def test_broker_failure(self):
        """Test system behavior when message broker fails"""
        print("=== Chaos Test: Broker Failure ===")
        
        try:
            # Send events normally
            for i in range(10):
                await self.event_system.publish('test-topic', {
                    'eventType': 'TestEvent',
                    'data': {'id': i}
                })
            
            print("Normal operation completed")
            
            # Simulate broker failure
            print("Simulating broker failure...")
            # In real test, you would stop Kafka/RabbitMQ container
            
            # Try to send events during failure
            failed_sends = 0
            for i in range(10, 20):
                try:
                    await self.event_system.publish('test-topic', {
                        'eventType': 'TestEvent',
                        'data': {'id': i}
                    })
                except:
                    failed_sends += 1
            
            print(f"Failed to send {failed_sends}/10 events during broker failure")
            
            # Simulate broker recovery
            print("Simulating broker recovery...")
            # In real test, you would restart the broker
            
            # Resume sending events
            for i in range(20, 30):
                await self.event_system.publish('test-topic', {
                    'eventType': 'TestEvent',
                    'data': {'id': i}
                })
            
            print("Recovery operation completed")
            
        except Exception as e:
            self.logger.error(f"Chaos test failed: {e}")
    
    async def test_consumer_failure(self):
        """Test system behavior when consumers fail"""
        print("=== Chaos Test: Consumer Failure ===")
        
        # This would simulate consumer failures and test:
        # - Message redelivery
        # - Dead letter queues
        # - Circuit breaker behavior
        # - System recovery
        
        pass
    
    async def test_network_partition(self):
        """Test system behavior during network partitions"""
        print("=== Chaos Test: Network Partition ===")
        
        # This would simulate network partitions and test:
        # - Message ordering guarantees
        # - Duplicate detection
        # - Eventual consistency
        # - Split-brain scenarios
        
        pass

# Property-Based Testing for Event Schemas
from hypothesis import given, strategies as st
import hypothesis

class TestEventProperties:
    @given(
        order_id=st.text(min_size=1, max_size=50),
        customer_id=st.text(min_size=1, max_size=50),
        amount=st.floats(min_value=0.01, max_value=100000, allow_nan=False, allow_infinity=False)
    )
    def test_order_creation_properties(self, order_id, customer_id, amount):
        """Property-based test for order creation"""
        
        # Create order
        order = OrderAggregate(order_id)
        
        # This should never fail regardless of input
        try:
            order.create_order(customer_id, {"street": "Test St"})
            
            # Properties that should always hold
            assert order.customer_id == customer_id
            assert order.status == OrderStatus.DRAFT
            assert len(order.uncommitted_events) == 1
            assert order.uncommitted_events[0].event_type == "OrderCreated"
            
        except Exception as e:
            # Log any unexpected failures
            print(f"Unexpected failure with inputs: order_id={order_id}, customer_id={customer_id}, amount={amount}")
            print(f"Error: {e}")
            raise

# Event Consumer Testing Helper
class TestEventConsumer:
    def __init__(self):
        self.received_events = []
        self.processing_errors = []
    
    async def handle_event(self, event_data: Dict[str, Any]) -> bool:
        """Test event handler that records events"""
        try:
            self.received_events.append({
                'event': event_data,
                'received_at': datetime.now().isoformat()
            })
            
            # Simulate processing
            await asyncio.sleep(0.01)
            
            return True
            
        except Exception as e:
            self.processing_errors.append({
                'event': event_data,
                'error': str(e),
                'failed_at': datetime.now().isoformat()
            })
            return False
    
    def assert_received_event(self, event_type: str, timeout_seconds: int = 5):
        """Assert that an event of specific type was received"""
        start_time = time.time()
        
        while time.time() - start_time < timeout_seconds:
            for received in self.received_events:
                if received['event'].get('eventType') == event_type:
                    return received['event']
            time.sleep(0.1)
        
        raise AssertionError(f"Event {event_type} not received within {timeout_seconds} seconds")
    
    def assert_event_count(self, expected_count: int):
        """Assert expected number of events received"""
        actual_count = len(self.received_events)
        assert actual_count == expected_count, f"Expected {expected_count} events, got {actual_count}"
    
    def clear(self):
        """Clear received events"""
        self.received_events.clear()
        self.processing_errors.clear()

# Usage example for testing
if __name__ == "__main__":
    # Run unit tests
    print("Running unit tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run integration tests
    print("\nRunning integration tests...")
    pytest.main([__file__ + "::TestEventIntegration", "-v"])
    
    # Run load tests
    print("\nRunning load tests...")
    async def run_load_test():
        # Mock event publisher for load testing
        mock_publisher = AsyncMock()
        load_tester = EventSystemLoadTester(mock_publisher)
        await load_tester.generate_load(events_per_second=100, duration_seconds=10)
    
    asyncio.run(run_load_test())
```

---

## 🏆 Congratulations!

You've completed the Event-Driven Architecture Zero to Hero guide! You now have mastery over:

### ✅ What You've Accomplished

**Fundamentals**:
- ✅ Event-driven architecture concepts and patterns
- ✅ Event design and schema best practices
- ✅ Message delivery guarantees and trade-offs
- ✅ Choreography vs orchestration patterns

**Message Brokers**:
- ✅ Apache Kafka advanced producer and consumer implementations
- ✅ RabbitMQ complete setup with exchange types and patterns
- ✅ Dead letter queues, priority queues, and delayed messages
- ✅ Performance optimization and monitoring

**Advanced Patterns**:
- ✅ Event Sourcing with complete aggregate implementation
- ✅ CQRS pattern with separate read/write models
- ✅ Saga pattern for distributed transactions
- ✅ Event streaming and real-time processing

**Production Excellence**:
- ✅ Comprehensive testing strategies (unit, integration, chaos)
- ✅ Monitoring and observability for event systems
- ✅ Security and compliance considerations
- ✅ Performance optimization and scalability patterns

**Real-World Applications**:
- ✅ Complete e-commerce platform implementation
- ✅ Real-time fraud detection system
- ✅ Microservices communication patterns
- ✅ Load testing and performance analysis

### 🚀 Your Event-Driven Architecture Journey

**Immediate Next Steps (Next 30 Days)**:
1. **Choose Your Message Broker**: Start with either Kafka or RabbitMQ based on your use case
2. **Build Your First Event-Driven System**: Implement the e-commerce example
3. **Practice Event Sourcing**: Build an aggregate with event sourcing
4. **Set Up Monitoring**: Implement observability for your event systems
5. **Join Communities**: Connect with event-driven architecture practitioners

**Advanced Goals (3-6 Months)**:
1. **Master Both Patterns**: Learn both choreography and orchestration
2. **Implement CQRS**: Build a system with separate read/write models
3. **Production Deployment**: Deploy event-driven system to cloud
4. **Performance Tuning**: Optimize for high throughput and low latency
5. **Contribute to Open Source**: Participate in event-driven projects

**Expert Level (1-2 Years)**:
1. **Design Large-Scale Systems**: Architect enterprise event-driven platforms
2. **Multi-Cloud Events**: Implement cross-cloud event streaming
3. **Event-Driven Microservices**: Build complete microservices architecture
4. **Thought Leadership**: Share knowledge through blogs and conferences
5. **Innovation**: Contribute to next-generation event technologies

### 🌟 The Event-Driven Future

Event-driven architecture is becoming the foundation for:

- **Real-time Everything**: Instant responses and analytics
- **Serverless Computing**: Event-triggered function execution
- **IoT and Edge Computing**: Massive scale sensor data processing
- **AI and ML Pipelines**: Event-driven model training and inference
- **Digital Transformation**: Modernizing legacy enterprise systems

**High-Demand Skills in EDA**:
- Event streaming and real-time processing
- Event-driven microservices architecture
- Cross-cloud event integration
- Event sourcing and CQRS patterns
- Event system security and compliance

### 💫 Keep Building!

Event-driven architecture enables some of the most innovative and scalable systems in the world. Companies like Netflix, LinkedIn, Uber, and Amazon have built their platforms on event-driven principles.

As an event-driven architecture expert, you'll:
- **Build Reactive Systems**: Create systems that respond instantly to changes
- **Enable Real-time Business**: Help organizations make real-time decisions
- **Scale to Global Levels**: Design systems handling millions of events per second
- **Drive Innovation**: Enable new business models and capabilities

**Remember**: Every large-scale system today is event-driven. Master these patterns, and you'll be ready to build the future of software architecture!

The world of events awaits your expertise. Start building amazing event-driven systems today! 🚀⚡

---

**"The best way to predict the future is to build it with events."** - Unknown

Keep streaming, keep building, keep innovating! 🌟