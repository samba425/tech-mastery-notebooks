# Load Balancing & High Availability: Zero to Hero Guide
## Complete System Reliability and Scalability Mastery

---

## 📚 Table of Contents

1. [Introduction to Load Balancing & HA](#introduction)
2. [Load Balancer Types & Algorithms](#types)
3. [High Availability Fundamentals](#ha-fundamentals)
4. [Session Management Strategies](#sessions)
5. [Failover & Recovery Strategies](#failover)
6. [Health Checks & Monitoring](#health-checks)
7. [Cloud Load Balancing Solutions](#cloud-solutions)
8. [Database High Availability](#database-ha)
9. [Caching for High Availability](#caching-ha)
10. [Disaster Recovery Planning](#disaster-recovery)
11. [Real-World Implementations](#real-world)
12. [Best Practices & Patterns](#best-practices)

---

## 🎯 Introduction to Load Balancing & High Availability {#introduction}

### What is Load Balancing?

**Load Balancing** distributes incoming network traffic across multiple servers to ensure optimal resource utilization, minimize response times, and avoid server overload.

```
Without Load Balancer (Single Point of Failure)
┌─────────┐                    ┌─────────────┐
│ Client  │─────────────────── │   Server    │ ← All traffic here!
└─────────┘                    │ (Overloaded)│
                               └─────────────┘
❌ Problems:
• Server overload
• Single point of failure  
• Poor scalability
• Downtime during maintenance

With Load Balancer (Distributed & Resilient)
┌─────────┐     ┌──────────────┐     ┌─────────────┐
│ Client  │────▶│Load Balancer │────▶│ Server 1    │
└─────────┘     └──────┬───────┘     └─────────────┘
                       │              ┌─────────────┐
                       ├─────────────▶│ Server 2    │
                       │              └─────────────┘
                       │              ┌─────────────┐
                       └─────────────▶│ Server 3    │
                                      └─────────────┘
✅ Benefits:
• Distributed load
• High availability
• Horizontal scaling
• Zero-downtime deployments
```

### What is High Availability?

**High Availability (HA)** is the ability of a system to remain operational and accessible for extended periods, typically measured as a percentage of uptime.

```
┌─────────────────────────────────────────────────────┐
│              Availability Levels                    │
├─────────────────────────────────────────────────────┤
│  90.0% (Basic)      = 36.5 days downtime/year      │
│  99.0% (Good)       = 3.65 days downtime/year      │  
│  99.9% (Great)      = 8.76 hours downtime/year     │
│  99.99% (Excellent) = 52.6 minutes downtime/year   │
│  99.999% (Elite)    = 5.26 minutes downtime/year   │
└─────────────────────────────────────────────────────┘
```

### Load Balancing + High Availability Architecture

```
                    Internet
                        │
              ┌─────────▼─────────┐
              │   DNS/CDN        │ ← Global load balancing
              │   (CloudFlare)   │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │  Load Balancer   │ ← Application load balancing
              │   (NGINX/HAProxy)│
              └─────┬───┬───┬─────┘
                    │   │   │
        ┌───────────▼─┐ │ ┌─▼───────────┐
        │   App       │ │ │   App       │ ← Redundant app instances
        │ Instance 1  │ │ │ Instance 2  │
        └─────────────┘ │ └─────────────┘
                        │
                ┌───────▼───────┐
                │   App         │
                │ Instance 3    │
                └───────────────┘
                        │
              ┌─────────▼─────────┐
              │  Database Cluster │ ← Database high availability
              │ Primary + Replica │
              └───────────────────┘
```

---

## ⚖️ Load Balancer Types & Algorithms {#types}

### Load Balancer Types

**Layer 4 (Transport Layer) Load Balancing**
- **Operates at**: TCP/UDP level
- **Decisions based on**: IP addresses and ports
- **Performance**: Very fast (no content inspection)
- **Use cases**: High-throughput applications, TCP-based services

**Layer 7 (Application Layer) Load Balancing**
- **Operates at**: HTTP/HTTPS level
- **Decisions based on**: Content, headers, URLs, cookies
- **Performance**: Slower (content inspection required)
- **Use cases**: Web applications, microservices, API gateways

```
┌─────────────────────────────────────────────────────┐
│              Layer 4 Load Balancer                  │
├─────────────────────────────────────────────────────┤
│  Client IP: 192.168.1.100:54321                    │
│  ↓                                                  │
│  Load Balancer decides based on:                   │
│  • Source IP                                        │
│  • Destination port                                 │
│  • Protocol (TCP/UDP)                              │
│  ↓                                                  │
│  Routes to: Server 2:8080                         │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│              Layer 7 Load Balancer                  │
├─────────────────────────────────────────────────────┤
│  HTTP Request:                                      │
│  GET /api/users/123                                 │
│  Host: api.example.com                              │
│  User-Agent: Mozilla...                            │
│  ↓                                                  │
│  Load Balancer decides based on:                   │
│  • URL path (/api/users → users service)          │
│  • Host header                                     │
│  • HTTP method                                     │
│  • Cookies/Sessions                                │
│  ↓                                                  │
│  Routes to: Users Service on Server 1             │
└─────────────────────────────────────────────────────┘
```

### Load Balancing Algorithms

```python
import random
import time
import hashlib
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod
import logging

@dataclass
class Server:
    id: str
    host: str
    port: int
    weight: int = 1
    active_connections: int = 0
    is_healthy: bool = True
    last_health_check: float = 0
    avg_response_time_ms: float = 0

class LoadBalancingAlgorithm(ABC):
    @abstractmethod
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        pass

class RoundRobinAlgorithm(LoadBalancingAlgorithm):
    def __init__(self):
        self.current_index = 0
    
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        healthy_servers = [s for s in servers if s.is_healthy]
        
        if not healthy_servers:
            return None
        
        # Select next server in rotation
        server = healthy_servers[self.current_index % len(healthy_servers)]
        self.current_index += 1
        
        return server

class WeightedRoundRobinAlgorithm(LoadBalancingAlgorithm):
    def __init__(self):
        self.current_weights = {}
    
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        healthy_servers = [s for s in servers if s.is_healthy]
        
        if not healthy_servers:
            return None
        
        # Initialize weights if needed
        for server in healthy_servers:
            if server.id not in self.current_weights:
                self.current_weights[server.id] = 0
        
        # Increase all current weights
        for server in healthy_servers:
            self.current_weights[server.id] += server.weight
        
        # Find server with highest current weight
        selected_server = max(healthy_servers, key=lambda s: self.current_weights[s.id])
        
        # Reduce selected server's current weight by total weight
        total_weight = sum(s.weight for s in healthy_servers)
        self.current_weights[selected_server.id] -= total_weight
        
        return selected_server

class LeastConnectionsAlgorithm(LoadBalancingAlgorithm):
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        healthy_servers = [s for s in servers if s.is_healthy]
        
        if not healthy_servers:
            return None
        
        # Select server with least active connections
        return min(healthy_servers, key=lambda s: s.active_connections)

class IPHashAlgorithm(LoadBalancingAlgorithm):
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        healthy_servers = [s for s in servers if s.is_healthy]
        
        if not healthy_servers:
            return None
        
        # Use client IP for consistent routing
        client_ip = client_info.get('client_ip', '0.0.0.0')
        hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        
        server_index = hash_value % len(healthy_servers)
        return healthy_servers[server_index]

class ResponseTimeAlgorithm(LoadBalancingAlgorithm):
    def select_server(self, servers: List[Server], client_info: Dict[str, Any] = None) -> Optional[Server]:
        healthy_servers = [s for s in servers if s.is_healthy]
        
        if not healthy_servers:
            return None
        
        # Select server with best response time
        return min(healthy_servers, key=lambda s: s.avg_response_time_ms)

# Advanced Load Balancer Implementation
class AdvancedLoadBalancer:
    def __init__(self, algorithm: LoadBalancingAlgorithm):
        self.algorithm = algorithm
        self.servers: List[Server] = []
        self.health_check_interval = 30  # seconds
        self.circuit_breakers = {}
        self.logger = logging.getLogger(__name__)
        
        # Metrics
        self.total_requests = 0
        self.failed_requests = 0
        
        # Start health checking
        self._start_health_checks()
    
    def add_server(self, host: str, port: int, weight: int = 1):
        """Add server to load balancer"""
        server = Server(
            id=f"{host}:{port}",
            host=host,
            port=port,
            weight=weight
        )
        self.servers.append(server)
        
        # Initialize circuit breaker
        self.circuit_breakers[server.id] = CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=60
        )
        
        self.logger.info(f"Added server: {server.id}")
    
    async def route_request(self, request_data: Dict[str, Any], client_ip: str) -> Optional[str]:
        """Route request to appropriate server"""
        
        client_info = {'client_ip': client_ip}
        
        # Select server using algorithm
        server = self.algorithm.select_server(self.servers, client_info)
        
        if not server:
            self.failed_requests += 1
            self.logger.error("No healthy servers available")
            return None
        
        # Check circuit breaker
        circuit_breaker = self.circuit_breakers[server.id]
        if not circuit_breaker.can_request():
            self.logger.warning(f"Circuit breaker open for {server.id}")
            # Try another server
            fallback_servers = [s for s in self.servers if s.id != server.id and s.is_healthy]
            if fallback_servers:
                server = self.algorithm.select_server(fallback_servers, client_info)
            else:
                return None
        
        # Track connection
        server.active_connections += 1
        self.total_requests += 1
        
        try:
            # Simulate request processing
            start_time = time.time()
            response = await self._forward_request(server, request_data)
            
            # Update metrics
            response_time = (time.time() - start_time) * 1000
            server.avg_response_time_ms = (server.avg_response_time_ms + response_time) / 2
            
            # Mark successful request
            circuit_breaker.record_success()
            
            return response
            
        except Exception as e:
            # Mark failed request
            circuit_breaker.record_failure()
            self.failed_requests += 1
            self.logger.error(f"Request failed on {server.id}: {e}")
            return None
        
        finally:
            server.active_connections = max(0, server.active_connections - 1)
    
    async def _forward_request(self, server: Server, request_data: Dict[str, Any]) -> str:
        """Forward request to server"""
        import aiohttp
        
        url = f"http://{server.host}:{server.port}/api"
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=request_data, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise Exception(f"Server returned status {response.status}")
    
    async def _check_server_health(self, server: Server) -> bool:
        """Check if server is healthy"""
        try:
            health_url = f"http://{server.host}:{server.port}/health"
            
            async with aiohttp.ClientSession() as session:
                async with session.get(health_url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    server.last_health_check = time.time()
                    
                    if response.status == 200:
                        health_data = await response.json()
                        server.is_healthy = health_data.get('status') == 'healthy'
                    else:
                        server.is_healthy = False
                        
        except Exception as e:
            server.is_healthy = False
            self.logger.warning(f"Health check failed for {server.id}: {e}")
        
        return server.is_healthy
    
    def _start_health_checks(self):
        """Start periodic health checks"""
        async def health_check_loop():
            while True:
                for server in self.servers:
                    await self._check_server_health(server)
                
                await asyncio.sleep(self.health_check_interval)
        
        asyncio.create_task(health_check_loop())
    
    def get_status(self) -> Dict[str, Any]:
        """Get load balancer status"""
        healthy_servers = [s for s in self.servers if s.is_healthy]
        
        return {
            'total_servers': len(self.servers),
            'healthy_servers': len(healthy_servers),
            'total_requests': self.total_requests,
            'failed_requests': self.failed_requests,
            'success_rate': ((self.total_requests - self.failed_requests) / self.total_requests * 100) if self.total_requests > 0 else 100,
            'servers': [
                {
                    'id': s.id,
                    'healthy': s.is_healthy,
                    'active_connections': s.active_connections,
                    'avg_response_time_ms': s.avg_response_time_ms
                }
                for s in self.servers
            ]
        }

# Circuit Breaker Pattern for Resilience
class CircuitBreakerState:
    CLOSED = "CLOSED"
    OPEN = "OPEN" 
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = CircuitBreakerState.CLOSED
    
    def can_request(self) -> bool:
        """Check if request is allowed"""
        if self.state == CircuitBreakerState.CLOSED:
            return True
        elif self.state == CircuitBreakerState.OPEN:
            # Check if recovery timeout has passed
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = CircuitBreakerState.HALF_OPEN
                return True
            return False
        else:  # HALF_OPEN
            return True
    
    def record_success(self):
        """Record successful request"""
        if self.state == CircuitBreakerState.HALF_OPEN:
            self.state = CircuitBreakerState.CLOSED
        
        self.failure_count = 0
    
    def record_failure(self):
        """Record failed request"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitBreakerState.OPEN
        elif self.state == CircuitBreakerState.HALF_OPEN:
            self.state = CircuitBreakerState.OPEN
```

---

## 📋 Session Management Strategies {#sessions}

### Sticky Sessions vs Session Replication

```python
import redis
import json
import hashlib
import uuid
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self, strategy: str = "redis"):
        self.strategy = strategy
        
        if strategy == "redis":
            self.redis_client = redis.Redis(
                host='localhost', 
                port=6379, 
                decode_responses=True,
                socket_keepalive=True,
                socket_keepalive_options={}
            )
    
    # 1. Stateless Sessions (JWT)
    def create_stateless_session(self, user_data: Dict[str, Any]) -> str:
        """Create JWT token for stateless sessions"""
        import jwt
        
        payload = {
            'user_id': user_data['user_id'],
            'username': user_data['username'],
            'roles': user_data.get('roles', []),
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=24)
        }
        
        token = jwt.encode(payload, 'secret-key', algorithm='HS256')
        return token
    
    def validate_stateless_session(self, token: str) -> Optional[Dict[str, Any]]:
        """Validate JWT token"""
        import jwt
        
        try:
            payload = jwt.decode(token, 'secret-key', algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    # 2. Distributed Sessions (Redis)
    async def create_distributed_session(self, user_data: Dict[str, Any]) -> str:
        """Create session stored in Redis"""
        session_id = str(uuid.uuid4())
        
        session_data = {
            'user_id': user_data['user_id'],
            'username': user_data['username'],
            'created_at': datetime.now().isoformat(),
            'last_accessed': datetime.now().isoformat(),
            'user_agent': user_data.get('user_agent'),
            'ip_address': user_data.get('ip_address')
        }
        
        # Store in Redis with TTL
        self.redis_client.setex(
            f"session:{session_id}",
            3600 * 24,  # 24 hours
            json.dumps(session_data)
        )
        
        return session_id
    
    async def get_distributed_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get session from Redis"""
        session_key = f"session:{session_id}"
        
        session_data_json = self.redis_client.get(session_key)
        if not session_data_json:
            return None
        
        session_data = json.loads(session_data_json)
        
        # Update last accessed time
        session_data['last_accessed'] = datetime.now().isoformat()
        self.redis_client.setex(session_key, 3600 * 24, json.dumps(session_data))
        
        return session_data
    
    async def invalidate_session(self, session_id: str):
        """Invalidate session"""
        self.redis_client.delete(f"session:{session_id}")
    
    # 3. Sticky Sessions (IP Affinity)
    class StickySessionManager:
        def __init__(self, servers: List[Server]):
            self.servers = servers
            self.client_server_mapping = {}
        
        def get_server_for_client(self, client_ip: str) -> Server:
            """Get consistent server for client IP"""
            if client_ip in self.client_server_mapping:
                server_id = self.client_server_mapping[client_ip]
                server = next((s for s in self.servers if s.id == server_id), None)
                
                if server and server.is_healthy:
                    return server
            
            # Assign new server using consistent hashing
            hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
            healthy_servers = [s for s in self.servers if s.is_healthy]
            
            if healthy_servers:
                server_index = hash_value % len(healthy_servers)
                selected_server = healthy_servers[server_index]
                self.client_server_mapping[client_ip] = selected_server.id
                return selected_server
            
            return None
    
    # 4. Session Replication
    class SessionReplicator:
        def __init__(self, redis_nodes: List[str]):
            self.redis_clients = [
                redis.Redis.from_url(node, decode_responses=True) 
                for node in redis_nodes
            ]
        
        async def replicate_session(self, session_id: str, session_data: Dict[str, Any]):
            """Replicate session across multiple Redis instances"""
            session_key = f"session:{session_id}"
            session_json = json.dumps(session_data)
            
            # Write to all Redis instances
            for client in self.redis_clients:
                try:
                    client.setex(session_key, 3600 * 24, session_json)
                except Exception as e:
                    print(f"Failed to replicate to Redis node: {e}")
        
        async def get_replicated_session(self, session_id: str) -> Optional[Dict[str, Any]]:
            """Get session with fallback to other replicas"""
            session_key = f"session:{session_id}"
            
            # Try each Redis instance until we find the session
            for client in self.redis_clients:
                try:
                    session_data_json = client.get(session_key)
                    if session_data_json:
                        return json.loads(session_data_json)
                except Exception as e:
                    print(f"Failed to read from Redis node: {e}")
                    continue
            
            return None
```

---

## 🛡️ Failover & Recovery Strategies {#failover}

### Automatic Failover Implementation

```python
import asyncio
import time
import logging
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import aiohttp
from abc import ABC, abstractmethod

class FailoverStrategy(Enum):
    ACTIVE_PASSIVE = "active_passive"
    ACTIVE_ACTIVE = "active_active"
    ROLLING_FAILOVER = "rolling_failover"

@dataclass
class HealthCheckConfig:
    endpoint: str = "/health"
    interval_seconds: int = 30
    timeout_seconds: int = 5
    failure_threshold: int = 3
    success_threshold: int = 2
    expected_status_code: int = 200
    expected_response_contains: Optional[str] = None

class FailoverManager:
    def __init__(self, strategy: FailoverStrategy = FailoverStrategy.ACTIVE_PASSIVE):
        self.strategy = strategy
        self.primary_servers: List[Server] = []
        self.secondary_servers: List[Server] = []
        self.health_check_config = HealthCheckConfig()
        self.logger = logging.getLogger(__name__)
        
        # Failover state
        self.is_failed_over = False
        self.failover_timestamp = None
        self.current_active_servers = []
        
        # Start monitoring
        self._start_monitoring()
    
    def add_primary_server(self, host: str, port: int):
        """Add primary server"""
        server = Server(id=f"primary-{host}:{port}", host=host, port=port)
        self.primary_servers.append(server)
        self._update_active_servers()
        
        self.logger.info(f"Added primary server: {server.id}")
    
    def add_secondary_server(self, host: str, port: int):
        """Add secondary server"""
        server = Server(id=f"secondary-{host}:{port}", host=host, port=port)
        self.secondary_servers.append(server)
        
        self.logger.info(f"Added secondary server: {server.id}")
    
    def _update_active_servers(self):
        """Update list of currently active servers based on strategy"""
        if self.strategy == FailoverStrategy.ACTIVE_PASSIVE:
            if not self.is_failed_over:
                self.current_active_servers = [s for s in self.primary_servers if s.is_healthy]
            else:
                self.current_active_servers = [s for s in self.secondary_servers if s.is_healthy]
        
        elif self.strategy == FailoverStrategy.ACTIVE_ACTIVE:
            self.current_active_servers = [
                s for s in (self.primary_servers + self.secondary_servers) 
                if s.is_healthy
            ]
    
    async def _check_server_health(self, server: Server) -> bool:
        """Comprehensive server health check"""
        consecutive_failures = getattr(server, 'consecutive_failures', 0)
        consecutive_successes = getattr(server, 'consecutive_successes', 0)
        
        try:
            health_url = f"http://{server.host}:{server.port}{self.health_check_config.endpoint}"
            
            timeout = aiohttp.ClientTimeout(total=self.health_check_config.timeout_seconds)
            
            async with aiohttp.ClientSession(timeout=timeout) as session:
                start_time = time.time()
                
                async with session.get(health_url) as response:
                    response_time = (time.time() - start_time) * 1000
                    response_text = await response.text()
                    
                    # Check status code
                    status_ok = response.status == self.health_check_config.expected_status_code
                    
                    # Check response content if specified
                    content_ok = True
                    if self.health_check_config.expected_response_contains:
                        content_ok = self.health_check_config.expected_response_contains in response_text
                    
                    # Check response time
                    response_ok = response_time < 5000  # 5 second max
                    
                    if status_ok and content_ok and response_ok:
                        consecutive_successes += 1
                        consecutive_failures = 0
                        
                        # Mark healthy if enough consecutive successes
                        if consecutive_successes >= self.health_check_config.success_threshold:
                            server.is_healthy = True
                        
                        server.avg_response_time_ms = response_time
                        
                    else:
                        consecutive_failures += 1
                        consecutive_successes = 0
                        
                        # Mark unhealthy if enough consecutive failures
                        if consecutive_failures >= self.health_check_config.failure_threshold:
                            server.is_healthy = False
        
        except Exception as e:
            consecutive_failures += 1
            consecutive_successes = 0
            
            if consecutive_failures >= self.health_check_config.failure_threshold:
                server.is_healthy = False
            
            self.logger.warning(f"Health check failed for {server.id}: {e}")
        
        finally:
            server.consecutive_failures = consecutive_failures
            server.consecutive_successes = consecutive_successes
            server.last_health_check = time.time()
        
        return server.is_healthy
    
    async def _monitor_and_failover(self):
        """Monitor servers and perform failover if needed"""
        while True:
            # Check health of all servers
            health_tasks = [
                self._check_server_health(server) 
                for server in (self.primary_servers + self.secondary_servers)
            ]
            
            await asyncio.gather(*health_tasks)
            
            # Check if failover is needed
            await self._evaluate_failover_conditions()
            
            await asyncio.sleep(self.health_check_config.interval_seconds)
    
    async def _evaluate_failover_conditions(self):
        """Evaluate whether failover is needed"""
        healthy_primaries = [s for s in self.primary_servers if s.is_healthy]
        healthy_secondaries = [s for s in self.secondary_servers if s.is_healthy]
        
        if self.strategy == FailoverStrategy.ACTIVE_PASSIVE:
            # Failover to secondary if no healthy primaries
            if not healthy_primaries and healthy_secondaries and not self.is_failed_over:
                await self._perform_failover()
            
            # Failback to primary if they're healthy again
            elif healthy_primaries and self.is_failed_over:
                await self._perform_failback()
        
        # Update active servers
        self._update_active_servers()
    
    async def _perform_failover(self):
        """Perform failover to secondary servers"""
        self.is_failed_over = True
        self.failover_timestamp = datetime.now()
        
        self.logger.critical("FAILOVER: Switching to secondary servers")
        
        # Notify monitoring systems
        await self._send_failover_alert("Failover to secondary servers initiated")
        
        # Update load balancer configuration
        self._update_active_servers()
        
        # Perform any additional failover tasks
        await self._execute_failover_hooks()
    
    async def _perform_failback(self):
        """Perform failback to primary servers"""
        self.logger.info("FAILBACK: Primary servers healthy, switching back")
        
        # Wait for a stabilization period
        await asyncio.sleep(30)  # Wait 30 seconds before failback
        
        # Double-check primary health
        health_tasks = [self._check_server_health(s) for s in self.primary_servers]
        await asyncio.gather(*health_tasks)
        
        healthy_primaries = [s for s in self.primary_servers if s.is_healthy]
        
        if healthy_primaries:
            self.is_failed_over = False
            self.failover_timestamp = None
            
            self.logger.info("FAILBACK: Successfully switched back to primary servers")
            
            await self._send_failover_alert("Failback to primary servers completed")
            self._update_active_servers()
    
    async def _send_failover_alert(self, message: str):
        """Send alert about failover events"""
        alert_data = {
            'timestamp': datetime.now().isoformat(),
            'message': message,
            'primary_servers_healthy': [s.is_healthy for s in self.primary_servers],
            'secondary_servers_healthy': [s.is_healthy for s in self.secondary_servers],
            'is_failed_over': self.is_failed_over
        }
        
        # Send to monitoring system (Slack, email, etc.)
        self.logger.critical(f"FAILOVER ALERT: {message}")
        print(f"ALERT: {json.dumps(alert_data, indent=2)}")
    
    async def _execute_failover_hooks(self):
        """Execute custom failover logic"""
        # Example: Update DNS records, notify dependent services, etc.
        hooks = [
            self._update_dns_records,
            self._notify_dependent_services,
            self._scale_up_secondary_resources
        ]
        
        for hook in hooks:
            try:
                await hook()
            except Exception as e:
                self.logger.error(f"Failover hook failed: {e}")
    
    async def _update_dns_records(self):
        """Update DNS to point to secondary servers"""
        # Implementation would use DNS API (Route53, CloudFlare, etc.)
        self.logger.info("DNS records updated for failover")
    
    async def _notify_dependent_services(self):
        """Notify other services about failover"""
        # Send notifications to dependent services
        self.logger.info("Dependent services notified of failover")
    
    async def _scale_up_secondary_resources(self):
        """Scale up secondary infrastructure"""
        # Auto-scale secondary resources to handle traffic
        self.logger.info("Secondary resources scaled up")
    
    def _start_monitoring(self):
        """Start health monitoring"""
        asyncio.create_task(self._monitor_and_failover())
    
    def get_failover_status(self) -> Dict[str, Any]:
        """Get current failover status"""
        return {
            'strategy': self.strategy.value,
            'is_failed_over': self.is_failed_over,
            'failover_timestamp': self.failover_timestamp.isoformat() if self.failover_timestamp else None,
            'active_servers': len(self.current_active_servers),
            'primary_servers': {
                'total': len(self.primary_servers),
                'healthy': len([s for s in self.primary_servers if s.is_healthy])
            },
            'secondary_servers': {
                'total': len(self.secondary_servers),
                'healthy': len([s for s in self.secondary_servers if s.is_healthy])
            }
        }

# Database Failover Example
class DatabaseFailoverManager:
    def __init__(self):
        self.primary_db = None
        self.replica_dbs = []
        self.current_db = None
        self.is_failed_over = False
        self.logger = logging.getLogger(__name__)
    
    async def setup_database_cluster(self, primary_dsn: str, replica_dsns: List[str]):
        """Setup database cluster with primary and replicas"""
        
        # Connect to primary
        self.primary_db = await asyncpg.create_pool(primary_dsn, max_size=50)
        self.current_db = self.primary_db
        
        # Connect to replicas
        for replica_dsn in replica_dsns:
            replica_pool = await asyncpg.create_pool(replica_dsn, max_size=20)
            self.replica_dbs.append(replica_pool)
        
        # Start health monitoring
        asyncio.create_task(self._monitor_database_health())
    
    async def execute_query(self, query: str, *args, read_only: bool = False) -> Any:
        """Execute query with automatic failover"""
        
        # Use replica for read-only queries if available
        if read_only and self.replica_dbs:
            for replica_db in self.replica_dbs:
                try:
                    async with replica_db.acquire() as conn:
                        return await conn.fetch(query, *args)
                except Exception:
                    continue
        
        # Use current database (primary or failed-over)
        try:
            async with self.current_db.acquire() as conn:
                if read_only:
                    return await conn.fetch(query, *args)
                else:
                    return await conn.execute(query, *args)
        
        except Exception as e:
            self.logger.error(f"Database query failed: {e}")
            
            # Attempt failover if not already failed over
            if not self.is_failed_over and self.replica_dbs:
                await self._perform_database_failover()
                
                # Retry query on new primary
                try:
                    async with self.current_db.acquire() as conn:
                        return await conn.execute(query, *args)
                except Exception as retry_error:
                    self.logger.error(f"Query failed even after failover: {retry_error}")
                    raise
            else:
                raise
    
    async def _monitor_database_health(self):
        """Monitor database health and trigger failover"""
        while True:
            try:
                # Check primary database health
                async with self.primary_db.acquire() as conn:
                    await conn.execute("SELECT 1")
                    
                # Primary is healthy
                if self.is_failed_over:
                    self.logger.info("Primary database recovered, considering failback...")
                    # Implement failback logic here
            
            except Exception as e:
                self.logger.warning(f"Primary database health check failed: {e}")
                
                if not self.is_failed_over:
                    await self._perform_database_failover()
            
            await asyncio.sleep(10)  # Check every 10 seconds
    
    async def _perform_database_failover(self):
        """Perform database failover"""
        if not self.replica_dbs:
            self.logger.error("No replica databases available for failover")
            return
        
        self.logger.critical("Performing database failover...")
        
        # Find healthiest replica
        best_replica = None
        
        for replica_db in self.replica_dbs:
            try:
                async with replica_db.acquire() as conn:
                    await conn.execute("SELECT 1")
                    best_replica = replica_db
                    break
            except Exception:
                continue
        
        if best_replica:
            self.current_db = best_replica
            self.is_failed_over = True
            self.logger.critical("Database failover completed")
            
            # In production, promote replica to primary
            await self._promote_replica_to_primary(best_replica)
        else:
            self.logger.error("No healthy replica found for failover")
    
    async def _promote_replica_to_primary(self, replica_db):
        """Promote replica to primary (PostgreSQL example)"""
        # This would typically involve:
        # 1. Stop replication on the replica
        # 2. Update application configuration
        # 3. Update DNS/load balancer
        # 4. Notify monitoring systems
        
        self.logger.info("Promoted replica to primary role")

# Load Balancer with Failover
class HighAvailabilityLoadBalancer:
    def __init__(self):
        self.load_balancer = AdvancedLoadBalancer(RoundRobinAlgorithm())
        self.failover_manager = FailoverManager(FailoverStrategy.ACTIVE_PASSIVE)
        self.logger = logging.getLogger(__name__)
    
    async def setup_ha_cluster(self, primary_servers: List[tuple], secondary_servers: List[tuple]):
        """Setup high availability cluster"""
        
        # Add primary servers
        for host, port in primary_servers:
            self.load_balancer.add_server(host, port)
            self.failover_manager.add_primary_server(host, port)
        
        # Add secondary servers
        for host, port in secondary_servers:
            self.failover_manager.add_secondary_server(host, port)
        
        self.logger.info("HA cluster setup completed")
    
    async def handle_request(self, request_data: Dict[str, Any], client_ip: str) -> Optional[str]:
        """Handle request with HA support"""
        
        # Update load balancer servers based on failover status
        active_servers = self.failover_manager.current_active_servers
        self.load_balancer.servers = active_servers
        
        # Route request
        response = await self.load_balancer.route_request(request_data, client_ip)
        
        # Handle response
        if response is None:
            # All servers failed, emergency response
            return await self._handle_total_failure()
        
        return response
    
    async def _handle_total_failure(self) -> str:
        """Handle complete system failure"""
        self.logger.critical("Total system failure - all servers unavailable")
        
        # Return maintenance page
        return json.dumps({
            "error": "Service temporarily unavailable",
            "message": "We're working to restore service. Please try again in a few minutes.",
            "status": "maintenance",
            "retry_after": 300  # 5 minutes
        })
```

---

## 🏗️ Real-World High Availability Implementations {#real-world}

### AWS High Availability Setup

```python
import boto3
import json
import time
from typing import Dict, List, Any, Optional

class AWSHighAvailabilityStack:
    def __init__(self, region: str = 'us-east-1'):
        self.region = region
        self.ec2 = boto3.client('ec2', region_name=region)
        self.elb = boto3.client('elbv2', region_name=region)
        self.autoscaling = boto3.client('autoscaling', region_name=region)
        self.route53 = boto3.client('route53')
        self.cloudwatch = boto3.client('cloudwatch', region_name=region)
        
    def create_multi_az_infrastructure(self):
        """Create multi-AZ infrastructure for high availability"""
        
        # 1. Create VPC across multiple Availability Zones
        vpc_config = {
            "CidrBlock": "10.0.0.0/16",
            "EnableDnsHostnames": True,
            "EnableDnsSupport": True
        }
        
        # 2. Create subnets in different AZs
        availability_zones = ['us-east-1a', 'us-east-1b', 'us-east-1c']
        
        subnet_configs = []
        for i, az in enumerate(availability_zones):
            subnet_configs.append({
                "AvailabilityZone": az,
                "CidrBlock": f"10.0.{i+1}.0/24",
                "MapPublicIpOnLaunch": True
            })
        
        # 3. Create Application Load Balancer
        alb_config = {
            "Name": "ha-app-loadbalancer",
            "Scheme": "internet-facing",
            "Type": "application",
            "IpAddressType": "ipv4",
            "Subnets": [],  # Subnet IDs from above
            "SecurityGroups": []  # Security group IDs
        }
        
        # 4. Create Auto Scaling Group
        autoscaling_config = {
            "AutoScalingGroupName": "ha-app-asg",
            "MinSize": 2,
            "MaxSize": 10,
            "DesiredCapacity": 3,
            "HealthCheckType": "ELB",
            "HealthCheckGracePeriod": 300,
            "DefaultCooldown": 300,
            "AvailabilityZones": availability_zones
        }
        
        return {
            "vpc_config": vpc_config,
            "subnet_configs": subnet_configs,
            "alb_config": alb_config,
            "autoscaling_config": autoscaling_config
        }
    
    def setup_health_checks_and_scaling(self):
        """Setup comprehensive health checks and auto-scaling"""
        
        # Health check configuration
        health_check_config = {
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckPath": "/health",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 2,
            "UnhealthyThresholdCount": 3,
            "Matcher": {"HttpCode": "200"}
        }
        
        # Auto-scaling policies
        scaling_policies = [
            {
                "PolicyName": "scale-up-cpu",
                "PolicyType": "TargetTrackingScaling",
                "TargetTrackingScalingPolicies": {
                    "TargetValue": 70.0,  # 70% CPU utilization
                    "PredefinedMetricSpecification": {
                        "PredefinedMetricType": "ASGAverageCPUUtilization"
                    },
                    "ScaleOutCooldown": 300,
                    "ScaleInCooldown": 300
                }
            },
            {
                "PolicyName": "scale-up-requests",
                "PolicyType": "TargetTrackingScaling", 
                "TargetTrackingScalingPolicies": {
                    "TargetValue": 1000.0,  # 1000 requests per target
                    "PredefinedMetricSpecification": {
                        "PredefinedMetricType": "ALBRequestCountPerTarget"
                    }
                }
            }
        ]
        
        return {
            "health_check": health_check_config,
            "scaling_policies": scaling_policies
        }
    
    def create_multi_region_setup(self):
        """Create multi-region setup with Route53"""
        
        # Route53 health checks and failover
        route53_config = {
            "HostedZoneId": "your-hosted-zone-id",
            "RecordSets": [
                {
                    "Name": "api.example.com",
                    "Type": "A",
                    "SetIdentifier": "us-east-1",
                    "Failover": "PRIMARY",
                    "AliasTarget": {
                        "DNSName": "us-east-1-alb.elb.amazonaws.com",
                        "EvaluateTargetHealth": True
                    },
                    "HealthCheckId": "health-check-us-east-1"
                },
                {
                    "Name": "api.example.com", 
                    "Type": "A",
                    "SetIdentifier": "us-west-2",
                    "Failover": "SECONDARY",
                    "AliasTarget": {
                        "DNSName": "us-west-2-alb.elb.amazonaws.com",
                        "EvaluateTargetHealth": True
                    },
                    "HealthCheckId": "health-check-us-west-2"
                }
            ]
        }
        
        return route53_config

# Kubernetes High Availability
class KubernetesHAManager:
    def __init__(self, kubectl_config: str):
        self.kubectl_config = kubectl_config
        
    def create_ha_deployment_manifests(self):
        """Create Kubernetes manifests for HA deployment"""
        
        # 1. Deployment with multiple replicas and anti-affinity
        deployment_manifest = {
            "apiVersion": "apps/v1",
            "kind": "Deployment", 
            "metadata": {
                "name": "ha-web-app",
                "labels": {"app": "web-app"}
            },
            "spec": {
                "replicas": 3,
                "selector": {"matchLabels": {"app": "web-app"}},
                "template": {
                    "metadata": {"labels": {"app": "web-app"}},
                    "spec": {
                        # Pod anti-affinity for distribution across nodes
                        "affinity": {
                            "podAntiAffinity": {
                                "preferredDuringSchedulingIgnoredDuringExecution": [
                                    {
                                        "weight": 100,
                                        "podAffinityTerm": {
                                            "labelSelector": {
                                                "matchExpressions": [
                                                    {
                                                        "key": "app",
                                                        "operator": "In",
                                                        "values": ["web-app"]
                                                    }
                                                ]
                                            },
                                            "topologyKey": "kubernetes.io/hostname"
                                        }
                                    }
                                ]
                            }
                        },
                        "containers": [
                            {
                                "name": "web-app",
                                "image": "my-app:latest",
                                "ports": [{"containerPort": 8080}],
                                "resources": {
                                    "requests": {
                                        "memory": "256Mi",
                                        "cpu": "250m"
                                    },
                                    "limits": {
                                        "memory": "512Mi", 
                                        "cpu": "500m"
                                    }
                                },
                                "livenessProbe": {
                                    "httpGet": {
                                        "path": "/health",
                                        "port": 8080
                                    },
                                    "initialDelaySeconds": 30,
                                    "periodSeconds": 10
                                },
                                "readinessProbe": {
                                    "httpGet": {
                                        "path": "/ready",
                                        "port": 8080
                                    },
                                    "initialDelaySeconds": 5,
                                    "periodSeconds": 5
                                }
                            }
                        ]
                    }
                }
            }
        }
        
        # 2. Service for load balancing
        service_manifest = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": "ha-web-app-service"
            },
            "spec": {
                "selector": {"app": "web-app"},
                "ports": [
                    {
                        "protocol": "TCP",
                        "port": 80,
                        "targetPort": 8080
                    }
                ],
                "type": "ClusterIP"
            }
        }
        
        # 3. Horizontal Pod Autoscaler
        hpa_manifest = {
            "apiVersion": "autoscaling/v2",
            "kind": "HorizontalPodAutoscaler",
            "metadata": {
                "name": "ha-web-app-hpa"
            },
            "spec": {
                "scaleTargetRef": {
                    "apiVersion": "apps/v1",
                    "kind": "Deployment",
                    "name": "ha-web-app"
                },
                "minReplicas": 3,
                "maxReplicas": 20,
                "metrics": [
                    {
                        "type": "Resource",
                        "resource": {
                            "name": "cpu",
                            "target": {
                                "type": "Utilization",
                                "averageUtilization": 70
                            }
                        }
                    },
                    {
                        "type": "Resource", 
                        "resource": {
                            "name": "memory",
                            "target": {
                                "type": "Utilization",
                                "averageUtilization": 80
                            }
                        }
                    }
                ]
            }
        }
        
        return {
            "deployment": deployment_manifest,
            "service": service_manifest,
            "hpa": hpa_manifest
        }

# Complete HA Example
async def ha_example():
    """Complete high availability example"""
    
    # Create load balancer
    lb = AdvancedLoadBalancer(WeightedRoundRobinAlgorithm())
    
    # Add servers with different weights
    lb.add_server("192.168.1.10", 8080, weight=3)  # More powerful server
    lb.add_server("192.168.1.11", 8080, weight=2)
    lb.add_server("192.168.1.12", 8080, weight=1)
    
    # Setup failover
    failover_manager = FailoverManager(FailoverStrategy.ACTIVE_PASSIVE)
    
    # Add primary and secondary servers
    failover_manager.add_primary_server("192.168.1.10", 8080)
    failover_manager.add_primary_server("192.168.1.11", 8080)
    
    failover_manager.add_secondary_server("192.168.1.20", 8080)
    failover_manager.add_secondary_server("192.168.1.21", 8080)
    
    # Setup database failover
    db_failover = DatabaseFailoverManager()
    await db_failover.setup_database_cluster(
        primary_dsn="postgresql://primary:5432/db",
        replica_dsns=[
            "postgresql://replica1:5432/db",
            "postgresql://replica2:5432/db"
        ]
    )
    
    # Setup session management
    session_manager = SessionManager(strategy="redis")
    
    # Simulate load for 30 seconds
    print("Running HA system simulation...")
    
    for i in range(30):
        # Simulate multiple concurrent requests
        tasks = []
        
        for j in range(10):  # 10 concurrent requests
            request_data = {
                'user_id': f'user_{j}',
                'action': 'get_data',
                'timestamp': time.time()
            }
            
            task = lb.route_request(request_data, f'192.168.1.{100 + j}')
            tasks.append(task)
        
        # Execute requests
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Count successes and failures
        successes = sum(1 for r in results if r is not None and not isinstance(r, Exception))
        failures = len(results) - successes
        
        print(f"Second {i+1}: {successes} successful, {failures} failed requests")
        
        await asyncio.sleep(1)
    
    # Print final status
    status = lb.get_status()
    failover_status = failover_manager.get_failover_status()
    
    print(f"\nFinal Load Balancer Status: {json.dumps(status, indent=2)}")
    print(f"Final Failover Status: {json.dumps(failover_status, indent=2)}")

if __name__ == "__main__":
    asyncio.run(ha_example())
```

---

## 🎯 Best Practices Summary {#best-practices}

### High Availability Checklist
- ✅ **Multiple Availability Zones**: Deploy across different AZs/regions
- ✅ **Auto-scaling**: Configure horizontal and vertical scaling
- ✅ **Health Checks**: Implement comprehensive health monitoring
- ✅ **Circuit Breakers**: Prevent cascading failures
- ✅ **Graceful Degradation**: Maintain core functionality during failures
- ✅ **Database Replication**: Master-slave or master-master setup
- ✅ **Load Balancing**: Distribute traffic effectively
- ✅ **Disaster Recovery**: Regular backups and recovery procedures

### Load Balancing Best Practices
- ✅ **Choose Right Algorithm**: Based on application characteristics
- ✅ **Health Monitoring**: Regular health checks with proper thresholds
- ✅ **Session Handling**: Stateless design or proper session management
- ✅ **SSL Termination**: Handle SSL at load balancer level
- ✅ **Rate Limiting**: Implement per-client rate limiting
- ✅ **Monitoring & Alerting**: Track performance and availability metrics
- ✅ **Regular Testing**: Practice failover scenarios
- ✅ **Documentation**: Maintain runbooks for common scenarios

### Disaster Recovery Planning
1. **RTO (Recovery Time Objective)**: Maximum acceptable downtime
2. **RPO (Recovery Point Objective)**: Maximum acceptable data loss
3. **Backup Strategy**: Regular automated backups with testing
4. **Failover Procedures**: Documented and practiced procedures
5. **Communication Plan**: Stakeholder notification procedures

---

## 🏆 Congratulations!

You now have comprehensive knowledge of:

- ✅ **Load Balancing**: All algorithms, types, and implementations
- ✅ **High Availability**: Failover strategies and architectures  
- ✅ **Session Management**: Stateless, sticky, and distributed approaches
- ✅ **Real-World Implementations**: AWS, Kubernetes, and custom solutions
- ✅ **Monitoring & Recovery**: Health checks, disaster recovery, and best practices

**Career Impact**: These skills are essential for:
- **DevOps Engineer** roles ($90k-150k)
- **Site Reliability Engineer** positions ($120k-200k)
- **Solutions Architect** roles ($130k-250k)
- **Principal Engineer** positions ($200k+)

Keep building resilient, scalable systems! 🚀⚡

---

*"Availability is not just about keeping systems running; it's about ensuring business continuity and customer trust."*

Build systems that never sleep! 💪🌟