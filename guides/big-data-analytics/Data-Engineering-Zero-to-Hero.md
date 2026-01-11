# Data Engineering: Zero to Hero Guide
## Complete Modern Data Engineering Mastery

---

## 📚 Table of Contents

1. [Introduction to Data Engineering](#introduction)
2. [Data Engineering Fundamentals](#fundamentals)
3. [Programming Languages for DE](#programming)
4. [Data Collection & Ingestion](#ingestion)
5. [Data Storage Solutions](#storage)
6. [Data Processing](#processing)
7. [Data Pipelines & Orchestration](#pipelines)
8. [Big Data Technologies](#bigdata)
9. [Cloud Data Platforms](#cloud)
10. [Stream Processing](#streaming)
11. [Data Quality & Governance](#quality)
12. [Monitoring & Observability](#monitoring)
13. [Data Security & Compliance](#security)
14. [Best Practices & Patterns](#best-practices)
15. [Real-World Projects](#projects)
16. [Career Path & Skills](#career)

---

## 🎯 Introduction to Data Engineering {#introduction}

### What is Data Engineering?

**Data Engineering** is the practice of designing and building systems for collecting, storing, and analyzing data at scale. Data engineers create the infrastructure and tools that enable data scientists and analysts to work with data effectively.

```
Traditional Software Engineering
┌────────────────────────────────────┐
│  User Input → Processing → Output  │
└────────────────────────────────────┘

Data Engineering
┌─────────────────────────────────────────────────────────────────┐
│  Raw Data → Collect → Transform → Store → Process → Insights    │
└─────────────────────────────────────────────────────────────────┘
```

### The Data Engineering Lifecycle

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Generation │───▶│  Ingestion   │───▶│ Transformation│──▶│   Serving    │
│             │    │              │    │              │    │              │
│ • IoT       │    │ • Batch      │    │ • ETL/ELT    │    │ • Analytics  │
│ • APIs      │    │ • Streaming  │    │ • Data Prep  │    │ • ML/AI      │
│ • Databases │    │ • Real-time  │    │ • Validation │    │ • Dashboards │
│ • Files     │    │ • Scheduled  │    │ • Enrichment │    │ • APIs       │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                            │
                   ┌──────────────┐
                   │   Storage    │
                   │              │
                   │ • Data Lake  │
                   │ • Warehouse  │
                   │ • NoSQL      │
                   │ • Object     │
                   └──────────────┘
```

### Why Data Engineering Matters

- **Data Volume Growth**: 90% of world's data created in last 2 years
- **Business Intelligence**: Data-driven decisions are crucial
- **Machine Learning**: Models need clean, reliable data
- **Real-time Insights**: Businesses need instant analytics
- **Compliance**: GDPR, CCPA require proper data handling

### Data Engineer vs Data Scientist vs Data Analyst

```
┌─────────────────────────────────────────────────────────┐
│                Data Engineer                            │
├─────────────────────────────────────────────────────────┤
│  Focus: Infrastructure, pipelines, systems             │
│  Skills: Python, SQL, Docker, Cloud, ETL               │
│  Tools: Airflow, Spark, Kafka, AWS/GCP/Azure          │
│  Goal: Enable data access and reliability              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Data Scientist                          │
├─────────────────────────────────────────────────────────┤
│  Focus: Models, algorithms, insights                   │
│  Skills: Python, R, Statistics, ML, Domain expertise  │
│  Tools: Jupyter, scikit-learn, TensorFlow, PyTorch    │
│  Goal: Extract insights and build predictive models    │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                Data Analyst                            │
├─────────────────────────────────────────────────────────┤
│  Focus: Reporting, visualization, business insights    │
│  Skills: SQL, Excel, Tableau, Power BI, Statistics    │
│  Tools: Tableau, Power BI, Looker, Excel              │
│  Goal: Answer business questions with data             │
└─────────────────────────────────────────────────────────┘
```

---

## 📐 Data Engineering Fundamentals {#fundamentals}

### Core Concepts

**1. ETL vs ELT**

```
ETL (Extract, Transform, Load)
┌─────────┐    ┌───────────┐    ┌──────────┐
│ Extract │───▶│ Transform │───▶│   Load   │
└─────────┘    └───────────┘    └──────────┘
• Traditional approach
• Transform before loading
• Good for structured data
• Less storage needed

ELT (Extract, Load, Transform)
┌─────────┐    ┌──────────┐    ┌───────────┐
│ Extract │───▶│   Load   │───▶│ Transform │
└─────────┘    └──────────┘    └───────────┘
• Modern cloud approach
• Load first, transform later
• Good for big data
• More flexible
```

**2. Batch vs Stream Processing**

```
Batch Processing
• Process large volumes of data at scheduled intervals
• High latency, high throughput
• Examples: Daily reports, monthly analytics
• Tools: Apache Spark, Hadoop MapReduce

Stream Processing
• Process data as it arrives in real-time
• Low latency, continuous processing
• Examples: Fraud detection, real-time analytics
• Tools: Apache Kafka, Apache Storm, Apache Flink
```

**3. Data Warehouse vs Data Lake**

```
┌────────────────────────────────────────┐
│            Data Warehouse              │
├────────────────────────────────────────┤
│  • Structured data only                │
│  • Schema-on-write                     │
│  • High performance queries           │
│  • Expensive storage                   │
│  • Examples: Snowflake, Redshift      │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│             Data Lake                  │
├────────────────────────────────────────┤
│  • Any data format (structured,       │
│    semi-structured, unstructured)     │
│  • Schema-on-read                     │
│  • Cheap storage                      │
│  • Examples: AWS S3, Azure Data Lake  │
└────────────────────────────────────────┘
```

### Data Types and Formats

**Structured Data**
- Relational databases (MySQL, PostgreSQL)
- CSV files
- Excel spreadsheets

**Semi-Structured Data**
- JSON documents
- XML files
- Parquet files
- Avro files

**Unstructured Data**
- Text documents
- Images, videos
- Log files
- Social media posts

### Common File Formats

```python
# CSV - Simple, widely supported
import pandas as pd
df = pd.read_csv('data.csv')

# JSON - Human readable, nested data
import json
with open('data.json', 'r') as f:
    data = json.load(f)

# Parquet - Columnar, compressed, fast
df = pd.read_parquet('data.parquet')
df.to_parquet('output.parquet')

# Avro - Schema evolution, streaming
from avro import schema, datafile, io

# Delta Lake - ACID transactions, versioning
import delta
df.write.format("delta").save("delta-table")
```

---

## 💻 Programming Languages for Data Engineering {#programming}

### Python for Data Engineering

**Why Python?**
- Extensive libraries (pandas, numpy, boto3)
- Great for data manipulation
- Cloud SDK support
- Easy to learn and read

**Essential Python Libraries**

```python
# Data Manipulation
import pandas as pd
import numpy as np

# Database Connectivity
import psycopg2  # PostgreSQL
import pymongo   # MongoDB
import sqlite3   # SQLite

# Cloud SDKs
import boto3     # AWS
from google.cloud import bigquery  # GCP
from azure.identity import DefaultAzureCredential  # Azure

# Data Processing
import dask      # Parallel computing
from pyspark.sql import SparkSession  # Big data processing

# API and Web
import requests  # HTTP requests
from flask import Flask  # Web framework
import asyncio   # Async programming

# Data Validation
from pydantic import BaseModel
import great_expectations as ge
```

**Example: Data Pipeline with Python**

```python
import pandas as pd
import requests
from sqlalchemy import create_engine
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPipeline:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
    
    def extract_from_api(self, url):
        """Extract data from REST API"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Extracted {len(data)} records from API")
            return pd.DataFrame(data)
        except Exception as e:
            logger.error(f"API extraction failed: {e}")
            raise
    
    def transform_data(self, df):
        """Transform and clean data"""
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.fillna(0)
        
        # Data type conversions
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['amount'] = pd.to_numeric(df['amount'])
        
        # Add calculated fields
        df['year'] = df['created_at'].dt.year
        df['month'] = df['created_at'].dt.month
        
        logger.info(f"Transformed {len(df)} records")
        return df
    
    def load_to_database(self, df, table_name):
        """Load data to database"""
        try:
            df.to_sql(
                table_name, 
                self.engine, 
                if_exists='append', 
                index=False
            )
            logger.info(f"Loaded {len(df)} records to {table_name}")
        except Exception as e:
            logger.error(f"Database load failed: {e}")
            raise
    
    def run_pipeline(self, api_url, table_name):
        """Run complete ETL pipeline"""
        logger.info("Starting ETL pipeline")
        
        # Extract
        raw_data = self.extract_from_api(api_url)
        
        # Transform
        clean_data = self.transform_data(raw_data)
        
        # Load
        self.load_to_database(clean_data, table_name)
        
        logger.info("ETL pipeline completed successfully")

# Usage
pipeline = DataPipeline('postgresql://user:pass@localhost:5432/db')
pipeline.run_pipeline('https://api.example.com/data', 'sales_data')
```

### SQL Mastery for Data Engineers

**Advanced SQL Concepts**

```sql
-- Window Functions
SELECT 
    customer_id,
    order_date,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) as running_total,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) as rank_by_amount,
    LAG(amount, 1) OVER (PARTITION BY customer_id ORDER BY order_date) as previous_amount
FROM orders;

-- Common Table Expressions (CTEs)
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(amount) as total_sales
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
),
sales_growth AS (
    SELECT 
        month,
        total_sales,
        LAG(total_sales) OVER (ORDER BY month) as previous_month_sales,
        (total_sales - LAG(total_sales) OVER (ORDER BY month)) / 
        LAG(total_sales) OVER (ORDER BY month) * 100 as growth_rate
    FROM monthly_sales
)
SELECT * FROM sales_growth WHERE growth_rate > 10;

-- Data Quality Checks
SELECT 
    'duplicate_check' as check_name,
    COUNT(*) - COUNT(DISTINCT email) as duplicate_count
FROM users
UNION ALL
SELECT 
    'null_check' as check_name,
    COUNT(*) as null_count
FROM users 
WHERE email IS NULL
UNION ALL
SELECT 
    'format_check' as check_name,
    COUNT(*) as invalid_email_count
FROM users 
WHERE email NOT LIKE '%@%.%';

-- Dynamic SQL for Data Profiling
SELECT 
    column_name,
    data_type,
    COUNT(*) as total_records,
    COUNT(column_name) as non_null_records,
    COUNT(DISTINCT column_name) as distinct_values,
    COUNT(*) - COUNT(column_name) as null_count,
    (COUNT(*) - COUNT(column_name)) * 100.0 / COUNT(*) as null_percentage
FROM information_schema.columns 
CROSS JOIN your_table
GROUP BY column_name, data_type;
```

### Bash/Shell Scripting

```bash
#!/bin/bash
# data_pipeline.sh - Automated data processing script

# Set variables
DATA_DIR="/data/raw"
PROCESSED_DIR="/data/processed"
LOG_FILE="/logs/pipeline.log"
DATE=$(date +%Y%m%d)

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

# Check if directories exist
if [ ! -d "$DATA_DIR" ]; then
    log_message "ERROR: Data directory $DATA_DIR does not exist"
    exit 1
fi

log_message "Starting data pipeline for $DATE"

# Download data from S3
aws s3 sync s3://my-bucket/raw-data/ $DATA_DIR/ \
    --exclude "*" \
    --include "*.csv" \
    --include "*.json"

if [ $? -eq 0 ]; then
    log_message "Data download completed successfully"
else
    log_message "ERROR: Data download failed"
    exit 1
fi

# Process each CSV file
for file in $DATA_DIR/*.csv; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .csv)
        log_message "Processing file: $filename"
        
        # Run Python processing script
        python3 /scripts/process_data.py "$file" "$PROCESSED_DIR/${filename}_processed.csv"
        
        if [ $? -eq 0 ]; then
            log_message "Successfully processed: $filename"
            # Move original file to archive
            mv "$file" "/data/archive/${filename}_${DATE}.csv"
        else
            log_message "ERROR: Failed to process $filename"
        fi
    fi
done

# Upload processed data
aws s3 sync $PROCESSED_DIR/ s3://my-bucket/processed-data/ \
    --delete

log_message "Data pipeline completed for $DATE"

# Cleanup old files (keep last 7 days)
find /data/archive -name "*.csv" -mtime +7 -delete
find /logs -name "*.log" -mtime +30 -delete
```

---

## 📥 Data Collection & Ingestion {#ingestion}

### Data Sources

**1. Databases**
- OLTP systems (PostgreSQL, MySQL, Oracle)
- NoSQL (MongoDB, Cassandra, DynamoDB)
- Data warehouses (Snowflake, Redshift, BigQuery)

**2. APIs and Web Services**
- REST APIs
- GraphQL endpoints
- Web scraping
- Real-time feeds

**3. Files and Object Storage**
- CSV, JSON, Parquet files
- AWS S3, GCS, Azure Blob
- FTP/SFTP servers
- Network drives

**4. Streaming Sources**
- Message queues (Apache Kafka, RabbitMQ)
- IoT sensors
- Application logs
- Social media streams

### Batch Data Ingestion

**Example: Database to Data Lake ETL**

```python
import pandas as pd
from sqlalchemy import create_engine
import boto3
from datetime import datetime, timedelta
import logging

class BatchIngestionPipeline:
    def __init__(self, source_db_url, s3_bucket):
        self.source_engine = create_engine(source_db_url)
        self.s3_client = boto3.client('s3')
        self.bucket = s3_bucket
        self.logger = logging.getLogger(__name__)
    
    def extract_incremental_data(self, table_name, timestamp_column, last_run_time):
        """Extract data incrementally based on timestamp"""
        query = f"""
        SELECT * FROM {table_name}
        WHERE {timestamp_column} > '{last_run_time}'
        AND {timestamp_column} <= '{datetime.now()}'
        ORDER BY {timestamp_column}
        """
        
        df = pd.read_sql(query, self.source_engine)
        self.logger.info(f"Extracted {len(df)} records from {table_name}")
        return df
    
    def upload_to_s3(self, df, s3_key):
        """Upload DataFrame to S3 as Parquet"""
        # Convert to parquet in memory
        parquet_buffer = df.to_parquet(index=False)
        
        # Upload to S3
        self.s3_client.put_object(
            Bucket=self.bucket,
            Key=s3_key,
            Body=parquet_buffer
        )
        
        self.logger.info(f"Uploaded data to s3://{self.bucket}/{s3_key}")
    
    def run_incremental_load(self, table_config):
        """Run incremental load for a table"""
        table_name = table_config['name']
        timestamp_column = table_config['timestamp_column']
        last_run_time = table_config['last_run_time']
        
        # Extract incremental data
        df = self.extract_incremental_data(
            table_name, 
            timestamp_column, 
            last_run_time
        )
        
        if not df.empty:
            # Partition by date for better query performance
            df['partition_date'] = pd.to_datetime(df[timestamp_column]).dt.date
            
            # Upload each partition separately
            for date, group in df.groupby('partition_date'):
                s3_key = f"raw-data/{table_name}/year={date.year}/month={date.month:02d}/day={date.day:02d}/data.parquet"
                self.upload_to_s3(group.drop('partition_date', axis=1), s3_key)
        
        return df[timestamp_column].max() if not df.empty else last_run_time

# Configuration
tables_config = [
    {
        'name': 'orders',
        'timestamp_column': 'created_at',
        'last_run_time': '2024-01-01 00:00:00'
    },
    {
        'name': 'customers', 
        'timestamp_column': 'updated_at',
        'last_run_time': '2024-01-01 00:00:00'
    }
]

# Run pipeline
pipeline = BatchIngestionPipeline(
    'postgresql://user:pass@localhost:5432/ecommerce',
    'my-data-lake-bucket'
)

for table_config in tables_config:
    last_processed_time = pipeline.run_incremental_load(table_config)
    # Update last_run_time for next execution
    table_config['last_run_time'] = last_processed_time
```

### Real-time Data Ingestion with Apache Kafka

**Producer Example**

```python
from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

class EventProducer:
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None
        )
        self.topic = topic
    
    def produce_user_events(self):
        """Simulate user activity events"""
        user_actions = ['login', 'view_product', 'add_to_cart', 'purchase', 'logout']
        
        while True:
            event = {
                'user_id': random.randint(1, 1000),
                'action': random.choice(user_actions),
                'timestamp': datetime.now().isoformat(),
                'session_id': f"session_{random.randint(10000, 99999)}",
                'product_id': random.randint(1, 100) if random.random() > 0.3 else None,
                'amount': round(random.uniform(10, 1000), 2) if random.random() > 0.8 else None
            }
            
            # Use user_id as partition key for ordering
            self.producer.send(
                self.topic, 
                key=str(event['user_id']),
                value=event
            )
            
            print(f"Produced: {event}")
            time.sleep(random.uniform(0.1, 2))  # Random delay

# Usage
producer = EventProducer(['localhost:9092'], 'user-events')
producer.produce_user_events()
```

**Consumer Example**

```python
from kafka import KafkaConsumer
import json
from datetime import datetime
import boto3

class EventConsumer:
    def __init__(self, bootstrap_servers, topic, group_id):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=True
        )
        self.s3_client = boto3.client('s3')
        self.buffer = []
        self.buffer_size = 100
        
    def process_batch(self, events):
        """Process a batch of events"""
        # Transform events
        processed_events = []
        for event in events:
            processed_event = {
                **event,
                'processed_at': datetime.now().isoformat(),
                'hour': datetime.fromisoformat(event['timestamp']).hour
            }
            processed_events.append(processed_event)
        
        # Save to S3
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        key = f"events/raw/date={datetime.now().date()}/batch_{timestamp}.json"
        
        self.s3_client.put_object(
            Bucket='my-events-bucket',
            Key=key,
            Body=json.dumps(processed_events, indent=2)
        )
        
        print(f"Processed batch of {len(events)} events to s3://my-events-bucket/{key}")
    
    def consume_events(self):
        """Consume events with micro-batching"""
        for message in self.consumer:
            event = message.value
            self.buffer.append(event)
            
            # Process when buffer is full
            if len(self.buffer) >= self.buffer_size:
                self.process_batch(self.buffer)
                self.buffer = []

# Usage
consumer = EventConsumer(['localhost:9092'], 'user-events', 'analytics-group')
consumer.consume_events()
```

### API Data Ingestion

```python
import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import logging
from typing import List, Dict, Optional

class APIDataIngestion:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.logger = logging.getLogger(__name__)
    
    def make_request(self, endpoint: str, params: Dict = None, retries: int = 3) -> Optional[Dict]:
        """Make HTTP request with retry logic"""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                response.raise_for_status()
                return response.json()
            
            except requests.exceptions.RequestException as e:
                self.logger.warning(f"Request failed (attempt {attempt + 1}): {e}")
                if attempt == retries - 1:
                    self.logger.error(f"All retries failed for {url}")
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def paginated_fetch(self, endpoint: str, params: Dict = None) -> List[Dict]:
        """Fetch all data using pagination"""
        all_data = []
        page = 1
        params = params or {}
        
        while True:
            params['page'] = page
            params['limit'] = 100  # API limit
            
            response = self.make_request(endpoint, params)
            
            if not response or not response.get('data'):
                break
            
            all_data.extend(response['data'])
            
            # Check if more pages exist
            if len(response['data']) < params['limit']:
                break
            
            page += 1
            time.sleep(0.1)  # Rate limiting
        
        self.logger.info(f"Fetched {len(all_data)} records from {endpoint}")
        return all_data
    
    def fetch_orders(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch orders data for date range"""
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'status': 'all'
        }
        
        orders = self.paginated_fetch('orders', params)
        
        if orders:
            df = pd.DataFrame(orders)
            df['created_at'] = pd.to_datetime(df['created_at'])
            df['order_value'] = pd.to_numeric(df['order_value'])
            return df
        
        return pd.DataFrame()
    
    def incremental_sync(self, last_sync_time: datetime) -> pd.DataFrame:
        """Perform incremental sync since last sync time"""
        end_time = datetime.now()
        
        df = self.fetch_orders(
            start_date=last_sync_time.isoformat(),
            end_date=end_time.isoformat()
        )
        
        return df

# Usage
api_client = APIDataIngestion('https://api.ecommerce.com/v1', 'your-api-key')

# Full historical load
historical_data = api_client.fetch_orders('2024-01-01', '2024-12-31')

# Incremental load
last_sync = datetime.now() - timedelta(hours=1)
incremental_data = api_client.incremental_sync(last_sync)
```

---

## 🗄️ Data Storage Solutions {#storage}

### Relational Databases (OLTP)

**PostgreSQL for Transactional Data**

```sql
-- Create optimized table for high-frequency inserts
CREATE TABLE user_events (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    properties JSONB,
    session_id UUID NOT NULL
);

-- Indexes for performance
CREATE INDEX CONCURRENTLY idx_user_events_user_id_timestamp 
ON user_events (user_id, timestamp DESC);

CREATE INDEX CONCURRENTLY idx_user_events_event_type 
ON user_events (event_type);

-- JSONB index for property queries
CREATE INDEX CONCURRENTLY idx_user_events_properties_gin 
ON user_events USING GIN (properties);

-- Partitioning for large tables
CREATE TABLE user_events_2024_01 PARTITION OF user_events
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

-- Bulk insert optimization
COPY user_events (user_id, event_type, properties, session_id)
FROM '/path/to/data.csv'
WITH (FORMAT csv, HEADER true);
```

### NoSQL Databases

**MongoDB for Document Storage**

```python
from pymongo import MongoClient
from datetime import datetime
import pandas as pd

class MongoDataStore:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
    
    def insert_product_catalog(self, products_df):
        """Insert product catalog with nested data"""
        products = []
        for _, row in products_df.iterrows():
            product = {
                "product_id": row['product_id'],
                "name": row['name'],
                "category": {
                    "main": row['main_category'],
                    "sub": row['sub_category']
                },
                "pricing": {
                    "base_price": float(row['base_price']),
                    "currency": row['currency'],
                    "discount": float(row.get('discount', 0))
                },
                "attributes": {
                    "brand": row.get('brand'),
                    "color": row.get('color'),
                    "size": row.get('size'),
                    "weight": row.get('weight')
                },
                "inventory": {
                    "stock_level": int(row['stock_level']),
                    "warehouse": row['warehouse'],
                    "reorder_level": int(row.get('reorder_level', 10))
                },
                "metadata": {
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                    "active": bool(row.get('active', True))
                }
            }
            products.append(product)
        
        # Bulk insert
        result = self.db.products.insert_many(products)
        return len(result.inserted_ids)
    
    def create_indexes(self):
        """Create indexes for optimal query performance"""
        # Compound index for category filtering
        self.db.products.create_index([
            ("category.main", 1),
            ("category.sub", 1),
            ("pricing.base_price", 1)
        ])
        
        # Text index for search
        self.db.products.create_index([
            ("name", "text"),
            ("attributes.brand", "text")
        ])
        
        # TTL index for automatic deletion
        self.db.user_sessions.create_index(
            [("created_at", 1)], 
            expireAfterSeconds=3600  # 1 hour
        )
    
    def aggregate_sales_data(self):
        """Complex aggregation pipeline"""
        pipeline = [
            # Match orders from last 30 days
            {
                "$match": {
                    "order_date": {
                        "$gte": datetime.now() - pd.Timedelta(days=30)
                    }
                }
            },
            # Unwind order items
            {"$unwind": "$items"},
            
            # Group by product and calculate metrics
            {
                "$group": {
                    "_id": "$items.product_id",
                    "total_quantity": {"$sum": "$items.quantity"},
                    "total_revenue": {"$sum": {"$multiply": ["$items.price", "$items.quantity"]}},
                    "order_count": {"$sum": 1},
                    "avg_order_size": {"$avg": "$items.quantity"}
                }
            },
            
            # Lookup product details
            {
                "$lookup": {
                    "from": "products",
                    "localField": "_id",
                    "foreignField": "product_id",
                    "as": "product_info"
                }
            },
            
            # Sort by revenue
            {"$sort": {"total_revenue": -1}},
            
            # Limit to top 100
            {"$limit": 100}
        ]
        
        return list(self.db.orders.aggregate(pipeline))

# Usage
mongo_store = MongoDataStore('mongodb://localhost:27017', 'ecommerce')
mongo_store.create_indexes()

# Insert product data
products_df = pd.read_csv('products.csv')
inserted_count = mongo_store.insert_product_catalog(products_df)
print(f"Inserted {inserted_count} products")
```

### Data Warehouses

**Snowflake Data Warehouse**

```python
import snowflake.connector
import pandas as pd
from sqlalchemy import create_engine

class SnowflakeWarehouse:
    def __init__(self, account, user, password, warehouse, database, schema):
        self.connection_params = {
            'account': account,
            'user': user,
            'password': password,
            'warehouse': warehouse,
            'database': database,
            'schema': schema
        }
        
        self.engine = create_engine(
            f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}'
        )
    
    def create_fact_table(self):
        """Create optimized fact table"""
        create_table_sql = """
        CREATE OR REPLACE TABLE fact_sales (
            sale_id NUMBER AUTOINCREMENT PRIMARY KEY,
            date_key DATE NOT NULL,
            customer_key NUMBER NOT NULL,
            product_key NUMBER NOT NULL,
            store_key NUMBER NOT NULL,
            quantity NUMBER(10,2),
            unit_price NUMBER(10,2),
            total_amount NUMBER(12,2),
            discount_amount NUMBER(10,2),
            tax_amount NUMBER(10,2),
            created_timestamp TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
        )
        CLUSTER BY (date_key, customer_key);
        """
        
        with self.engine.connect() as conn:
            conn.execute(create_table_sql)
    
    def bulk_load_from_s3(self, s3_path, table_name):
        """Load data from S3 using COPY command"""
        copy_sql = f"""
        COPY INTO {table_name}
        FROM '{s3_path}'
        CREDENTIALS = (AWS_KEY_ID = 'your_key' AWS_SECRET_KEY = 'your_secret')
        FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1)
        ON_ERROR = 'SKIP_FILE';
        """
        
        with self.engine.connect() as conn:
            result = conn.execute(copy_sql)
            return result.fetchone()
    
    def create_materialized_view(self):
        """Create materialized view for fast analytics"""
        create_view_sql = """
        CREATE OR REPLACE MATERIALIZED VIEW mv_daily_sales AS
        SELECT 
            date_key,
            COUNT(*) as transaction_count,
            SUM(total_amount) as total_revenue,
            AVG(total_amount) as avg_order_value,
            SUM(quantity) as total_units_sold,
            COUNT(DISTINCT customer_key) as unique_customers
        FROM fact_sales
        GROUP BY date_key;
        """
        
        with self.engine.connect() as conn:
            conn.execute(create_view_sql)
    
    def optimize_table(self, table_name):
        """Optimize table performance"""
        optimize_sql = f"""
        -- Analyze table statistics
        ALTER TABLE {table_name} SET TABLE_STATS = TRUE;
        
        -- Cluster table
        ALTER TABLE {table_name} CLUSTER BY (date_key, customer_key);
        
        -- Optimize micro-partitions
        ALTER TABLE {table_name} SET ENABLE_SCHEMA_EVOLUTION = TRUE;
        """
        
        with self.engine.connect() as conn:
            conn.execute(optimize_sql)

# Usage
warehouse = SnowflakeWarehouse(
    account='your-account.snowflakecomputing.com',
    user='your-user',
    password='your-password',
    warehouse='COMPUTE_WH',
    database='ANALYTICS',
    schema='SALES'
)

warehouse.create_fact_table()
warehouse.bulk_load_from_s3('s3://my-bucket/sales-data/', 'fact_sales')
warehouse.create_materialized_view()
```

### Data Lakes

**AWS S3 Data Lake Architecture**

```python
import boto3
import pandas as pd
from datetime import datetime, timedelta
import pyarrow as pa
import pyarrow.parquet as pq

class S3DataLake:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key, region):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region
        )
        
    def write_partitioned_data(self, df, table_name, partition_cols):
        """Write data with partitioning for better query performance"""
        
        # Add partition columns if not exist
        if 'year' not in df.columns and 'date' in df.columns:
            df['year'] = pd.to_datetime(df['date']).dt.year
        if 'month' not in df.columns and 'date' in df.columns:
            df['month'] = pd.to_datetime(df['date']).dt.month
        if 'day' not in df.columns and 'date' in df.columns:
            df['day'] = pd.to_datetime(df['date']).dt.day
        
        # Group by partition columns
        for partition_values, group_df in df.groupby(partition_cols):
            # Create partition path
            partition_path = '/'.join([
                f"{col}={val}" for col, val in zip(partition_cols, partition_values)
            ])
            
            # Create S3 key
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            s3_key = f"data-lake/{table_name}/{partition_path}/data_{timestamp}.parquet"
            
            # Convert to parquet and upload
            parquet_buffer = group_df.drop(partition_cols, axis=1).to_parquet(index=False)
            
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=parquet_buffer,
                Metadata={
                    'table': table_name,
                    'partition': partition_path,
                    'records': str(len(group_df)),
                    'created_at': datetime.now().isoformat()
                }
            )
            
            print(f"Written {len(group_df)} records to s3://{self.bucket_name}/{s3_key}")
    
    def read_partitioned_data(self, table_name, filters=None):
        """Read partitioned data with optional filters"""
        prefix = f"data-lake/{table_name}/"
        
        # List all objects
        paginator = self.s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=self.bucket_name, Prefix=prefix)
        
        dataframes = []
        
        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    
                    # Apply partition filters
                    if filters and not self._matches_filters(key, filters):
                        continue
                    
                    # Read parquet file
                    response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
                    df = pd.read_parquet(response['Body'])
                    
                    # Extract partition values from path
                    partition_info = self._extract_partition_info(key)
                    for col, val in partition_info.items():
                        df[col] = val
                    
                    dataframes.append(df)
        
        if dataframes:
            return pd.concat(dataframes, ignore_index=True)
        else:
            return pd.DataFrame()
    
    def _matches_filters(self, key, filters):
        """Check if S3 key matches partition filters"""
        for col, val in filters.items():
            if f"{col}={val}" not in key:
                return False
        return True
    
    def _extract_partition_info(self, key):
        """Extract partition information from S3 key"""
        parts = key.split('/')
        partition_info = {}
        
        for part in parts:
            if '=' in part:
                col, val = part.split('=', 1)
                # Try to convert to appropriate type
                try:
                    if val.isdigit():
                        val = int(val)
                    elif val.replace('.', '').isdigit():
                        val = float(val)
                except:
                    pass
                partition_info[col] = val
        
        return partition_info
    
    def create_athena_table(self, table_name, schema, partition_cols):
        """Create Athena table for querying data lake"""
        
        # Build column definitions
        columns = []
        for col, dtype in schema.items():
            if col not in partition_cols:
                athena_type = self._pandas_to_athena_type(dtype)
                columns.append(f"`{col}` {athena_type}")
        
        columns_str = ',\n  '.join(columns)
        
        # Build partition definitions
        partitions = []
        for col in partition_cols:
            dtype = schema.get(col, 'string')
            athena_type = self._pandas_to_athena_type(dtype)
            partitions.append(f"`{col}` {athena_type}")
        
        partitions_str = ',\n  '.join(partitions)
        
        create_table_sql = f"""
        CREATE EXTERNAL TABLE `{table_name}` (
          {columns_str}
        )
        PARTITIONED BY (
          {partitions_str}
        )
        STORED AS PARQUET
        LOCATION 's3://{self.bucket_name}/data-lake/{table_name}/'
        TBLPROPERTIES ('has_encrypted_data'='false');
        """
        
        return create_table_sql
    
    def _pandas_to_athena_type(self, pandas_dtype):
        """Convert pandas dtype to Athena data type"""
        dtype_mapping = {
            'object': 'string',
            'int64': 'bigint',
            'int32': 'int',
            'float64': 'double',
            'float32': 'float',
            'bool': 'boolean',
            'datetime64[ns]': 'timestamp'
        }
        return dtype_mapping.get(str(pandas_dtype), 'string')

# Usage
data_lake = S3DataLake('my-data-lake-bucket', 'access-key', 'secret-key', 'us-east-1')

# Write partitioned sales data
sales_df = pd.read_csv('sales_data.csv')
data_lake.write_partitioned_data(sales_df, 'sales', ['year', 'month', 'day'])

# Read data with filters
filtered_data = data_lake.read_partitioned_data(
    'sales', 
    filters={'year': 2024, 'month': 1}
)

# Generate Athena table DDL
schema = {
    'sale_id': 'int64',
    'customer_id': 'int64', 
    'amount': 'float64',
    'date': 'datetime64[ns]',
    'year': 'int64',
    'month': 'int64',
    'day': 'int64'
}

create_table_sql = data_lake.create_athena_table('sales', schema, ['year', 'month', 'day'])
print(create_table_sql)
```

---

## ⚙️ Data Processing {#processing}

### Apache Spark for Big Data Processing

**Setting Up PySpark**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os

# Configure Spark
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

def create_spark_session(app_name="DataProcessing"):
    """Create optimized Spark session"""
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.sql.adaptive.skewJoin.enabled", "true") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.sql.parquet.compression.codec", "snappy") \
        .getOrCreate()
    
    # Set log level
    spark.sparkContext.setLogLevel("WARN")
    return spark

class SparkDataProcessor:
    def __init__(self):
        self.spark = create_spark_session()
    
    def read_from_sources(self):
        """Read from multiple data sources"""
        
        # Read from CSV
        customers_df = self.spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv("s3a://my-bucket/customers/*.csv")
        
        # Read from Parquet (partitioned)
        orders_df = self.spark.read \
            .parquet("s3a://my-bucket/orders/year=2024/")
        
        # Read from Delta Lake
        products_df = self.spark.read \
            .format("delta") \
            .load("s3a://my-bucket/products/")
        
        # Read from Database
        user_events_df = self.spark.read \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://localhost:5432/events") \
            .option("dbtable", "user_events") \
            .option("user", "user") \
            .option("password", "password") \
            .option("driver", "org.postgresql.Driver") \
            .load()
        
        return customers_df, orders_df, products_df, user_events_df
    
    def advanced_transformations(self, df):
        """Demonstrate advanced Spark transformations"""
        
        # Window functions
        from pyspark.sql.window import Window
        
        window_spec = Window.partitionBy("customer_id").orderBy("order_date")
        
        transformed_df = df \
            .withColumn("row_number", row_number().over(window_spec)) \
            .withColumn("running_total", sum("amount").over(window_spec)) \
            .withColumn("prev_order_amount", lag("amount", 1).over(window_spec)) \
            .withColumn("days_since_last_order", 
                       datediff(col("order_date"), 
                               lag("order_date", 1).over(window_spec))) \
            .withColumn("customer_lifetime_value", 
                       sum("amount").over(Window.partitionBy("customer_id"))) \
            .withColumn("order_rank", 
                       rank().over(Window.partitionBy("customer_id")
                                  .orderBy(desc("amount"))))
        
        # Complex aggregations
        summary_df = transformed_df.groupBy("customer_id") \
            .agg(
                count("*").alias("total_orders"),
                sum("amount").alias("total_spent"),
                avg("amount").alias("avg_order_value"),
                max("order_date").alias("last_order_date"),
                min("order_date").alias("first_order_date"),
                stddev("amount").alias("order_value_stddev"),
                collect_list("product_category").alias("categories_purchased")
            )
        
        # Add calculated columns
        final_df = summary_df \
            .withColumn("customer_tenure_days",
                       datediff(col("last_order_date"), col("first_order_date"))) \
            .withColumn("order_frequency", 
                       col("total_orders") / (col("customer_tenure_days") + 1)) \
            .withColumn("customer_segment",
                       when(col("total_spent") > 1000, "Premium")
                       .when(col("total_spent") > 500, "Standard")
                       .otherwise("Basic"))
        
        return final_df
    
    def data_quality_checks(self, df, table_name):
        """Comprehensive data quality validation"""
        
        total_records = df.count()
        
        quality_report = {
            'table_name': table_name,
            'total_records': total_records,
            'checks': {}
        }
        
        # Null checks
        for column in df.columns:
            null_count = df.filter(col(column).isNull()).count()
            null_percentage = (null_count / total_records) * 100
            
            quality_report['checks'][f'{column}_null_check'] = {
                'null_count': null_count,
                'null_percentage': round(null_percentage, 2),
                'status': 'PASS' if null_percentage < 5 else 'FAIL'
            }
        
        # Duplicate checks
        distinct_records = df.distinct().count()
        duplicate_count = total_records - distinct_records
        
        quality_report['checks']['duplicate_check'] = {
            'duplicate_count': duplicate_count,
            'duplicate_percentage': round((duplicate_count / total_records) * 100, 2),
            'status': 'PASS' if duplicate_count == 0 else 'WARN'
        }
        
        # Outlier detection (for numeric columns)
        numeric_columns = [field.name for field in df.schema.fields 
                          if isinstance(field.dataType, (IntegerType, DoubleType, FloatType))]
        
        for column in numeric_columns:
            stats = df.select(column).describe().collect()
            mean_val = float([row for row in stats if row[0] == 'mean'][0][1])
            stddev_val = float([row for row in stats if row[0] == 'stddev'][0][1])
            
            # Count values beyond 3 standard deviations
            outlier_count = df.filter(
                (col(column) > mean_val + 3 * stddev_val) |
                (col(column) < mean_val - 3 * stddev_val)
            ).count()
            
            quality_report['checks'][f'{column}_outlier_check'] = {
                'outlier_count': outlier_count,
                'outlier_percentage': round((outlier_count / total_records) * 100, 2),
                'status': 'PASS' if outlier_count < total_records * 0.01 else 'WARN'
            }
        
        return quality_report
    
    def optimize_and_write(self, df, output_path, partition_columns=None):
        """Optimize DataFrame and write with best practices"""
        
        # Optimize partitioning
        if partition_columns:
            # Repartition based on partition columns for better performance
            df = df.repartition(*[col(c) for c in partition_columns])
        else:
            # Auto-optimize partitions
            df = df.coalesce(200)  # Reasonable number of partitions
        
        # Cache if the DataFrame will be used multiple times
        df.cache()
        
        # Write with optimization
        writer = df.write \
            .mode("overwrite") \
            .option("compression", "snappy") \
            .option("maxRecordsPerFile", 1000000)
        
        if partition_columns:
            writer = writer.partitionBy(*partition_columns)
        
        writer.parquet(output_path)
        
        print(f"Data written to {output_path} with {df.rdd.getNumPartitions()} partitions")

# Example usage
processor = SparkDataProcessor()

# Read data
customers_df, orders_df, products_df, events_df = processor.read_from_sources()

# Join datasets
enriched_orders = orders_df \
    .join(customers_df, "customer_id", "inner") \
    .join(products_df, "product_id", "inner")

# Apply transformations
customer_analytics = processor.advanced_transformations(enriched_orders)

# Data quality checks
quality_report = processor.data_quality_checks(customer_analytics, "customer_analytics")
print(f"Data Quality Report: {quality_report}")

# Write optimized output
processor.optimize_and_write(
    customer_analytics, 
    "s3a://output-bucket/customer-analytics/",
    partition_columns=["customer_segment"]
)

# Don't forget to stop Spark session
processor.spark.stop()
```

### Pandas for Medium-Scale Processing

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import multiprocessing as mp
from functools import partial
import warnings
warnings.filterwarnings('ignore')

class PandasDataProcessor:
    def __init__(self, n_jobs=-1):
        self.n_jobs = n_jobs if n_jobs > 0 else mp.cpu_count()
    
    def chunk_processor(self, chunk, processing_func):
        """Process a chunk of data"""
        return processing_func(chunk)
    
    def parallel_apply(self, df, processing_func, chunk_size=10000):
        """Apply function in parallel using multiprocessing"""
        
        # Split DataFrame into chunks
        chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
        
        # Process chunks in parallel
        with mp.Pool(processes=self.n_jobs) as pool:
            func = partial(self.chunk_processor, processing_func=processing_func)
            results = pool.map(func, chunks)
        
        # Combine results
        return pd.concat(results, ignore_index=True)
    
    def memory_efficient_read_csv(self, filepath, chunk_size=50000, processing_func=None):
        """Read large CSV files in chunks"""
        chunks = []
        
        for chunk in pd.read_csv(filepath, chunksize=chunk_size):
            if processing_func:
                chunk = processing_func(chunk)
            chunks.append(chunk)
        
        return pd.concat(chunks, ignore_index=True)
    
    def advanced_feature_engineering(self, df):
        """Advanced feature engineering with pandas"""
        
        # Date features
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.dayofweek
            df['month'] = df['timestamp'].dt.month
            df['quarter'] = df['timestamp'].dt.quarter
            df['is_weekend'] = df['day_of_week'].isin([5, 6])
            df['is_business_hour'] = df['hour'].between(9, 17)
        
        # Rolling statistics
        if 'amount' in df.columns and 'customer_id' in df.columns:
            df = df.sort_values(['customer_id', 'timestamp'])
            
            # Rolling aggregations
            df['rolling_avg_7d'] = df.groupby('customer_id')['amount'].transform(
                lambda x: x.rolling(window=7, min_periods=1).mean()
            )
            df['rolling_std_7d'] = df.groupby('customer_id')['amount'].transform(
                lambda x: x.rolling(window=7, min_periods=1).std()
            )
            
            # Lag features
            df['amount_lag_1'] = df.groupby('customer_id')['amount'].shift(1)
            df['amount_lag_7'] = df.groupby('customer_id')['amount'].shift(7)
            
            # Customer metrics
            df['customer_total_spent'] = df.groupby('customer_id')['amount'].transform('sum')
            df['customer_avg_amount'] = df.groupby('customer_id')['amount'].transform('mean')
            df['customer_transaction_count'] = df.groupby('customer_id')['amount'].transform('count')
        
        # Categorical encoding
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        for col in categorical_columns:
            if col not in ['customer_id', 'timestamp']:  # Skip ID columns
                # Frequency encoding
                freq_map = df[col].value_counts().to_dict()
                df[f'{col}_frequency'] = df[col].map(freq_map)
                
                # Target encoding (if target column exists)
                if 'target' in df.columns:
                    target_mean = df.groupby(col)['target'].mean()
                    df[f'{col}_target_encoded'] = df[col].map(target_mean)
        
        return df
    
    def detect_anomalies(self, df, columns):
        """Detect anomalies using statistical methods"""
        anomalies = pd.DataFrame()
        
        for col in columns:
            if df[col].dtype in ['int64', 'float64']:
                # Z-score method
                z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
                z_anomalies = df[z_scores > 3].copy()
                z_anomalies['anomaly_type'] = 'z_score'
                z_anomalies['anomaly_column'] = col
                z_anomalies['anomaly_score'] = z_scores[z_scores > 3]
                
                # IQR method
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                iqr_anomalies = df[(df[col] < lower_bound) | (df[col] > upper_bound)].copy()
                iqr_anomalies['anomaly_type'] = 'iqr'
                iqr_anomalies['anomaly_column'] = col
                iqr_anomalies['anomaly_score'] = np.where(
                    iqr_anomalies[col] < lower_bound,
                    lower_bound - iqr_anomalies[col],
                    iqr_anomalies[col] - upper_bound
                )
                
                anomalies = pd.concat([anomalies, z_anomalies, iqr_anomalies])
        
        return anomalies.drop_duplicates()
    
    def create_data_summary(self, df):
        """Create comprehensive data summary"""
        summary = {
            'basic_info': {
                'rows': len(df),
                'columns': len(df.columns),
                'memory_usage_mb': df.memory_usage(deep=True).sum() / (1024 * 1024),
                'dtypes': df.dtypes.value_counts().to_dict()
            },
            'missing_data': {},
            'numeric_summary': {},
            'categorical_summary': {}
        }
        
        # Missing data analysis
        missing_data = df.isnull().sum()
        summary['missing_data'] = {
            col: {
                'count': int(missing_data[col]),
                'percentage': round((missing_data[col] / len(df)) * 100, 2)
            }
            for col in missing_data[missing_data > 0].index
        }
        
        # Numeric columns summary
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            summary['numeric_summary'][col] = {
                'mean': float(df[col].mean()),
                'std': float(df[col].std()),
                'min': float(df[col].min()),
                'max': float(df[col].max()),
                'median': float(df[col].median()),
                'q25': float(df[col].quantile(0.25)),
                'q75': float(df[col].quantile(0.75)),
                'unique_count': int(df[col].nunique()),
                'zero_count': int((df[col] == 0).sum())
            }
        
        # Categorical columns summary
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            value_counts = df[col].value_counts().head(10)
            summary['categorical_summary'][col] = {
                'unique_count': int(df[col].nunique()),
                'most_frequent': str(value_counts.index[0]) if len(value_counts) > 0 else None,
                'most_frequent_count': int(value_counts.iloc[0]) if len(value_counts) > 0 else 0,
                'top_values': value_counts.to_dict()
            }
        
        return summary

# Usage example
processor = PandasDataProcessor(n_jobs=4)

# Read large file efficiently
def preprocessing_func(chunk):
    # Clean data
    chunk = chunk.dropna()
    chunk['amount'] = pd.to_numeric(chunk['amount'], errors='coerce')
    return chunk

df = processor.memory_efficient_read_csv(
    'large_file.csv', 
    chunk_size=50000,
    processing_func=preprocessing_func
)

# Feature engineering
df_engineered = processor.advanced_feature_engineering(df)

# Parallel processing for complex operations
def complex_processing(chunk):
    # Simulate complex processing
    chunk['complex_feature'] = chunk['amount'] * np.log(chunk['customer_transaction_count'] + 1)
    return chunk

df_processed = processor.parallel_apply(df_engineered, complex_processing)

# Detect anomalies
anomalies = processor.detect_anomalies(df_processed, ['amount', 'complex_feature'])

# Generate summary
data_summary = processor.create_data_summary(df_processed)
print("Data Summary:", data_summary)
```

---

## 🔄 Data Pipelines & Orchestration {#pipelines}

### Apache Airflow for Workflow Orchestration

**Setting Up Airflow DAGs**

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.sensors.s3_key_sensor import S3KeySensor
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook
from datetime import datetime, timedelta
import pandas as pd
import logging

# Default arguments for DAG
default_args = {
    'owner': 'data-engineering-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

# Create DAG
dag = DAG(
    'sales_data_pipeline',
    default_args=default_args,
    description='Complete sales data processing pipeline',
    schedule_interval=timedelta(hours=1),  # Run hourly
    max_active_runs=1,
    tags=['sales', 'etl', 'production']
)

def extract_from_source_db(**context):
    """Extract data from source database"""
    execution_date = context['execution_date']
    start_time = execution_date - timedelta(hours=1)
    end_time = execution_date
    
    # Connect to source database
    postgres_hook = PostgresHook(postgres_conn_id='source_db')
    
    query = f"""
    SELECT 
        order_id,
        customer_id,
        product_id,
        quantity,
        price,
        order_date,
        status
    FROM orders 
    WHERE order_date BETWEEN '{start_time}' AND '{end_time}'
    AND status IN ('completed', 'shipped')
    """
    
    df = postgres_hook.get_pandas_df(query)
    
    # Save to S3 staging area
    s3_hook = S3Hook(aws_conn_id='aws_default')
    
    csv_buffer = df.to_csv(index=False)
    s3_key = f"staging/orders/{execution_date.strftime('%Y/%m/%d/%H')}/orders.csv"
    
    s3_hook.load_string(
        string_data=csv_buffer,
        key=s3_key,
        bucket_name='data-pipeline-bucket',
        replace=True
    )
    
    logging.info(f"Extracted {len(df)} records to s3://data-pipeline-bucket/{s3_key}")
    return s3_key

def validate_data_quality(**context):
    """Validate data quality before processing"""
    s3_key = context['task_instance'].xcom_pull(task_ids='extract_data')
    s3_hook = S3Hook(aws_conn_id='aws_default')
    
    # Read data from S3
    csv_content = s3_hook.read_key(s3_key, bucket_name='data-pipeline-bucket')
    df = pd.read_csv(pd.StringIO(csv_content))
    
    # Data quality checks
    quality_issues = []
    
    # Check for nulls in critical columns
    critical_columns = ['order_id', 'customer_id', 'product_id', 'quantity', 'price']
    for col in critical_columns:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            quality_issues.append(f"Found {null_count} null values in {col}")
    
    # Check for duplicates
    duplicate_count = df.duplicated(subset=['order_id']).sum()
    if duplicate_count > 0:
        quality_issues.append(f"Found {duplicate_count} duplicate order_ids")
    
    # Check data ranges
    if (df['quantity'] <= 0).any():
        quality_issues.append("Found invalid quantity values (<= 0)")
    
    if (df['price'] <= 0).any():
        quality_issues.append("Found invalid price values (<= 0)")
    
    # Fail if critical issues found
    if quality_issues:
        error_msg = "Data quality issues found: " + "; ".join(quality_issues)
        logging.error(error_msg)
        raise ValueError(error_msg)
    
    logging.info(f"Data quality validation passed for {len(df)} records")
    return True

def transform_data(**context):
    """Transform and enrich data"""
    s3_key = context['task_instance'].xcom_pull(task_ids='extract_data')
    s3_hook = S3Hook(aws_conn_id='aws_default')
    
    # Read data
    csv_content = s3_hook.read_key(s3_key, bucket_name='data-pipeline-bucket')
    df = pd.read_csv(pd.StringIO(csv_content))
    
    # Transformations
    df['total_amount'] = df['quantity'] * df['price']
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_day'] = df['order_date'].dt.day
    df['order_hour'] = df['order_date'].dt.hour
    
    # Enrichment - add customer and product info
    postgres_hook = PostgresHook(postgres_conn_id='source_db')
    
    # Get customer info
    customer_ids = df['customer_id'].unique().tolist()
    customer_query = f"""
    SELECT customer_id, customer_name, customer_segment, country
    FROM customers 
    WHERE customer_id IN ({','.join(map(str, customer_ids))})
    """
    customers_df = postgres_hook.get_pandas_df(customer_query)
    
    # Get product info
    product_ids = df['product_id'].unique().tolist()
    product_query = f"""
    SELECT product_id, product_name, category, subcategory, brand
    FROM products 
    WHERE product_id IN ({','.join(map(str, product_ids))})
    """
    products_df = postgres_hook.get_pandas_df(product_query)
    
    # Merge with master data
    df_enriched = df.merge(customers_df, on='customer_id', how='left')
    df_enriched = df_enriched.merge(products_df, on='product_id', how='left')
    
    # Save transformed data
    execution_date = context['execution_date']
    transformed_key = f"transformed/orders/{execution_date.strftime('%Y/%m/%d/%H')}/orders_transformed.parquet"
    
    parquet_buffer = df_enriched.to_parquet(index=False)
    s3_hook.load_bytes(
        bytes_data=parquet_buffer,
        key=transformed_key,
        bucket_name='data-pipeline-bucket',
        replace=True
    )
    
    logging.info(f"Transformed and saved {len(df_enriched)} records to s3://data-pipeline-bucket/{transformed_key}")
    return transformed_key

def load_to_warehouse(**context):
    """Load data to data warehouse"""
    transformed_key = context['task_instance'].xcom_pull(task_ids='transform_data')
    s3_hook = S3Hook(aws_conn_id='aws_default')
    postgres_hook = PostgresHook(postgres_conn_id='warehouse_db')
    
    # Read transformed data
    parquet_content = s3_hook.read_key(transformed_key, bucket_name='data-pipeline-bucket')
    df = pd.read_parquet(pd.BytesIO(parquet_content))
    
    # Create temporary table
    execution_date = context['execution_date']
    temp_table = f"temp_orders_{execution_date.strftime('%Y%m%d_%H%M%S')}"
    
    # Load to temporary table
    df.to_sql(
        temp_table,
        con=postgres_hook.get_sqlalchemy_engine(),
        if_exists='replace',
        index=False,
        method='multi',
        chunksize=1000
    )
    
    # Merge into main table (upsert)
    merge_query = f"""
    INSERT INTO fact_orders 
    SELECT * FROM {temp_table}
    ON CONFLICT (order_id) 
    DO UPDATE SET
        quantity = EXCLUDED.quantity,
        price = EXCLUDED.price,
        total_amount = EXCLUDED.total_amount,
        status = EXCLUDED.status,
        updated_at = CURRENT_TIMESTAMP;
    """
    
    postgres_hook.run(merge_query)
    
    # Drop temporary table
    postgres_hook.run(f"DROP TABLE {temp_table}")
    
    logging.info(f"Loaded {len(df)} records to data warehouse")

def update_data_catalog(**context):
    """Update data catalog with pipeline metadata"""
    execution_date = context['execution_date']
    
    # Update metadata table
    postgres_hook = PostgresHook(postgres_conn_id='warehouse_db')
    
    metadata_query = f"""
    INSERT INTO pipeline_runs (
        pipeline_name,
        run_date,
        status,
        records_processed,
        execution_time
    ) VALUES (
        'sales_data_pipeline',
        '{execution_date}',
        'SUCCESS',
        (SELECT COUNT(*) FROM fact_orders WHERE DATE(created_at) = '{execution_date.date()}'),
        CURRENT_TIMESTAMP
    )
    """
    
    postgres_hook.run(metadata_query)
    
    logging.info("Updated data catalog with pipeline metadata")

# Define tasks
# 1. Wait for source data
wait_for_data = S3KeySensor(
    task_id='wait_for_source_data',
    bucket_name='source-data-bucket',
    bucket_key='orders/{{ ds }}/ready.flag',
    aws_conn_id='aws_default',
    timeout=60 * 30,  # Wait up to 30 minutes
    poke_interval=60,  # Check every minute
    dag=dag
)

# 2. Extract data
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_from_source_db,
    dag=dag
)

# 3. Validate data quality
validate_task = PythonOperator(
    task_id='validate_data_quality',
    python_callable=validate_data_quality,
    dag=dag
)

# 4. Transform data
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

# 5. Load to warehouse
load_task = PythonOperator(
    task_id='load_to_warehouse',
    python_callable=load_to_warehouse,
    dag=dag
)

# 6. Update data catalog
catalog_task = PythonOperator(
    task_id='update_data_catalog',
    python_callable=update_data_catalog,
    dag=dag
)

# 7. Data quality check post-load
post_load_check = PostgresOperator(
    task_id='post_load_quality_check',
    postgres_conn_id='warehouse_db',
    sql="""
    SELECT 
        CASE 
            WHEN COUNT(*) > 0 THEN 'PASS'
            ELSE 'FAIL'
        END as status
    FROM fact_orders 
    WHERE DATE(created_at) = '{{ ds }}'
    AND total_amount > 0;
    """,
    dag=dag
)

# 8. Send success notification
success_notification = BashOperator(
    task_id='send_success_notification',
    bash_command="""
    echo "Sales data pipeline completed successfully for {{ ds }}" | 
    mail -s "Pipeline Success" data-team@company.com
    """,
    dag=dag
)

# Define task dependencies
wait_for_data >> extract_task >> validate_task >> transform_task >> load_task >> catalog_task >> post_load_check >> success_notification

# Set up failure notifications
def task_fail_alert(context):
    """Send alert on task failure"""
    task_instance = context.get('task_instance')
    dag_id = context.get('dag').dag_id
    
    subject = f"Airflow Alert: {dag_id} - {task_instance.task_id} Failed"
    html_content = f"""
    <h2>Task Failed</h2>
    <p><strong>DAG:</strong> {dag_id}</p>
    <p><strong>Task:</strong> {task_instance.task_id}</p>
    <p><strong>Execution Date:</strong> {context.get('execution_date')}</p>
    <p><strong>Error:</strong> {context.get('exception')}</p>
    """
    
    # Send email alert (configure email settings in airflow.cfg)
    send_email(['data-team@company.com'], subject, html_content)

# Apply failure callback to all tasks
for task in dag.tasks:
    task.on_failure_callback = task_fail_alert
```

### Modern Orchestration with Prefect

```python
from prefect import flow, task, get_run_logger
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from prefect.filesystems import S3
import pandas as pd
import boto3
from datetime import datetime, timedelta
from typing import List, Dict
import asyncio

@task(retries=3, retry_delay_seconds=60)
def extract_sales_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Extract sales data from source system"""
    logger = get_run_logger()
    
    # Simulate API call to source system
    import requests
    
    response = requests.get(
        "https://api.example.com/sales",
        params={
            "start_date": start_date,
            "end_date": end_date,
            "limit": 10000
        },
        headers={"Authorization": "Bearer your-token"}
    )
    
    data = response.json()
    df = pd.DataFrame(data['results'])
    
    logger.info(f"Extracted {len(df)} sales records")
    return df

@task
def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate data quality"""
    logger = get_run_logger()
    
    # Check for required columns
    required_columns = ['order_id', 'customer_id', 'amount', 'order_date']
    missing_columns = set(required_columns) - set(df.columns)
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Remove duplicates
    initial_count = len(df)
    df = df.drop_duplicates(subset=['order_id'])
    final_count = len(df)
    
    if initial_count != final_count:
        logger.warning(f"Removed {initial_count - final_count} duplicate records")
    
    # Check for nulls
    null_counts = df[required_columns].isnull().sum()
    if null_counts.sum() > 0:
        logger.warning(f"Null values found: {null_counts.to_dict()}")
        # Remove rows with nulls in critical columns
        df = df.dropna(subset=required_columns)
    
    logger.info(f"Validation complete. Final record count: {len(df)}")
    return df

@task
async def enrich_with_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Enrich sales data with customer information"""
    logger = get_run_logger()
    
    # Simulate async API calls for customer data
    async def get_customer_info(customer_id):
        # Simulate async HTTP request
        await asyncio.sleep(0.1)  # Simulate network delay
        return {
            "customer_id": customer_id,
            "segment": "Premium" if customer_id % 3 == 0 else "Standard",
            "country": "US" if customer_id % 2 == 0 else "UK"
        }
    
    # Get unique customer IDs
    customer_ids = df['customer_id'].unique()
    
    # Fetch customer data concurrently
    customer_tasks = [get_customer_info(cid) for cid in customer_ids]
    customer_data = await asyncio.gather(*customer_tasks)
    
    # Create customer DataFrame
    customer_df = pd.DataFrame(customer_data)
    
    # Merge with sales data
    enriched_df = df.merge(customer_df, on='customer_id', how='left')
    
    logger.info(f"Enriched {len(enriched_df)} records with customer data")
    return enriched_df

@task
def aggregate_metrics(df: pd.DataFrame) -> Dict:
    """Calculate business metrics"""
    logger = get_run_logger()
    
    metrics = {
        "total_revenue": float(df['amount'].sum()),
        "total_orders": int(len(df)),
        "avg_order_value": float(df['amount'].mean()),
        "unique_customers": int(df['customer_id'].nunique()),
        "revenue_by_segment": df.groupby('segment')['amount'].sum().to_dict(),
        "orders_by_country": df['country'].value_counts().to_dict(),
        "processing_timestamp": datetime.now().isoformat()
    }
    
    logger.info(f"Calculated metrics: {metrics}")
    return metrics

@task
def save_to_warehouse(df: pd.DataFrame, table_name: str = "fact_sales") -> str:
    """Save data to data warehouse"""
    logger = get_run_logger()
    
    # Save to S3 (simulating data warehouse)
    s3_client = boto3.client('s3')
    
    # Convert to parquet
    parquet_buffer = df.to_parquet(index=False)
    
    # Create S3 key with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    s3_key = f"warehouse/{table_name}/{timestamp}.parquet"
    
    # Upload to S3
    s3_client.put_object(
        Bucket='data-warehouse-bucket',
        Key=s3_key,
        Body=parquet_buffer
    )
    
    logger.info(f"Saved {len(df)} records to s3://data-warehouse-bucket/{s3_key}")
    return s3_key

@task
def update_metrics_dashboard(metrics: Dict) -> None:
    """Update business metrics dashboard"""
    logger = get_run_logger()
    
    # Simulate updating dashboard/monitoring system
    import json
    
    # Save metrics to monitoring system
    s3_client = boto3.client('s3')
    
    metrics_json = json.dumps(metrics, indent=2)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    s3_client.put_object(
        Bucket='metrics-bucket',
        Key=f"daily-metrics/{timestamp}.json",
        Body=metrics_json,
        ContentType='application/json'
    )
    
    logger.info("Updated metrics dashboard")

@flow(name="sales-data-pipeline", description="Complete sales data processing pipeline")
async def sales_pipeline(start_date: str = None, end_date: str = None):
    """Main pipeline flow"""
    logger = get_run_logger()
    
    # Set default dates if not provided
    if not start_date:
        start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.now().strftime('%Y-%m-%d')
    
    logger.info(f"Starting sales pipeline for {start_date} to {end_date}")
    
    # Extract data
    raw_data = extract_sales_data(start_date, end_date)
    
    # Validate data
    clean_data = validate_data(raw_data)
    
    # Enrich with customer data (async)
    enriched_data = await enrich_with_customer_data(clean_data)
    
    # Calculate metrics
    metrics = aggregate_metrics(enriched_data)
    
    # Save to warehouse and update dashboard in parallel
    warehouse_path = save_to_warehouse(enriched_data)
    update_metrics_dashboard(metrics)
    
    logger.info(f"Pipeline completed successfully. Data saved to {warehouse_path}")
    
    return {
        "status": "success",
        "records_processed": len(enriched_data),
        "warehouse_path": warehouse_path,
        "metrics": metrics
    }

# Create deployment
if __name__ == "__main__":
    # Create S3 storage for flow code
    s3_storage = S3(bucket_path="prefect-flows/sales-pipeline")
    
    deployment = Deployment.build_from_flow(
        flow=sales_pipeline,
        name="daily-sales-processing",
        storage=s3_storage,
        schedule=CronSchedule(cron="0 2 * * *"),  # Run daily at 2 AM
        work_pool_name="kubernetes-pool",
        tags=["sales", "production", "daily"]
    )
    
    deployment.apply()
```

---

---

## 🐘 Big Data Technologies {#bigdata}

### Apache Hadoop Ecosystem

**Hadoop Distributed File System (HDFS)**

```bash
# HDFS Commands
# List files
hdfs dfs -ls /user/data/

# Create directory
hdfs dfs -mkdir /user/data/sales

# Copy file from local to HDFS
hdfs dfs -put sales_data.csv /user/data/sales/

# Copy file from HDFS to local
hdfs dfs -get /user/data/sales/processed_data.csv ./

# Check file size and replication
hdfs dfs -du -h /user/data/sales/

# View file content
hdfs dfs -cat /user/data/sales/sales_data.csv | head -10

# Set replication factor
hdfs dfs -setrep 3 /user/data/sales/important_file.csv
```

**MapReduce with Python (MRJob)**

```python
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class SalesAnalysis(MRJob):
    
    def configure_args(self):
        super(SalesAnalysis, self).configure_args()
        self.add_passthru_arg('--min-amount', type=float, default=0,
                            help='Minimum sale amount to include')
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract_sales,
                  reducer=self.reducer_sum_by_customer),
            MRStep(mapper=self.mapper_format_output,
                  reducer=self.reducer_top_customers)
        ]
    
    def mapper_extract_sales(self, _, line):
        """Extract customer ID and sale amount"""
        # Parse CSV line: customer_id,product_id,amount,date
        fields = line.strip().split(',')
        
        if len(fields) == 4 and fields[0] != 'customer_id':  # Skip header
            try:
                customer_id = fields[0]
                amount = float(fields[2])
                
                if amount >= self.options.min_amount:
                    yield customer_id, amount
            except ValueError:
                pass  # Skip invalid lines
    
    def reducer_sum_by_customer(self, customer_id, amounts):
        """Sum total sales per customer"""
        total_amount = sum(amounts)
        yield None, (total_amount, customer_id)  # Use None key for global sorting
    
    def mapper_format_output(self, _, customer_data):
        """Prepare data for final sorting"""
        total_amount, customer_id = customer_data
        yield total_amount, customer_id
    
    def reducer_top_customers(self, total_amount, customer_ids):
        """Output top customers by total sales"""
        for customer_id in customer_ids:
            yield customer_id, total_amount

# Run locally
# python sales_analysis.py sales_data.csv --min-amount=100

# Run on Hadoop
# python sales_analysis.py -r hadoop hdfs:///user/data/sales/*.csv --min-amount=100
```

### Apache Kafka for Stream Processing

**Kafka Producer and Consumer**

```python
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
import json
import logging
from datetime import datetime
import threading
import time

class KafkaManager:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.bootstrap_servers = bootstrap_servers
        self.logger = logging.getLogger(__name__)
    
    def create_topic(self, topic_name, num_partitions=3, replication_factor=1):
        """Create Kafka topic"""
        admin_client = KafkaAdminClient(bootstrap_servers=self.bootstrap_servers)
        
        topic = NewTopic(
            name=topic_name,
            num_partitions=num_partitions,
            replication_factor=replication_factor
        )
        
        try:
            result = admin_client.create_topics([topic])
            self.logger.info(f"Created topic: {topic_name}")
        except TopicAlreadyExistsError:
            self.logger.info(f"Topic {topic_name} already exists")
    
    def produce_events(self, topic_name, events):
        """Produce events to Kafka topic"""
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: str(k).encode('utf-8') if k else None,
            # Performance settings
            acks='all',  # Wait for all replicas
            retries=3,
            batch_size=16384,
            linger_ms=10,  # Wait 10ms to batch messages
            buffer_memory=33554432
        )
        
        try:
            for event in events:
                # Use customer_id as partition key for ordering
                key = event.get('customer_id')
                future = producer.send(topic_name, key=key, value=event)
                
                # Optional: wait for confirmation
                future.get(timeout=10)
                
            producer.flush()  # Ensure all messages are sent
            self.logger.info(f"Produced {len(events)} events to {topic_name}")
            
        except Exception as e:
            self.logger.error(f"Failed to produce events: {e}")
        finally:
            producer.close()
    
    def consume_events(self, topic_name, group_id, auto_offset_reset='latest'):
        """Consume events from Kafka topic"""
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=self.bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit=True,
            auto_commit_interval_ms=1000,
            # Performance settings
            fetch_min_bytes=1,
            fetch_max_wait_ms=500,
            max_poll_records=500
        )
        
        try:
            self.logger.info(f"Starting to consume from {topic_name}")
            for message in consumer:
                yield {
                    'topic': message.topic,
                    'partition': message.partition,
                    'offset': message.offset,
                    'key': message.key.decode('utf-8') if message.key else None,
                    'value': message.value,
                    'timestamp': message.timestamp
                }
        except KeyboardInterrupt:
            self.logger.info("Consumer interrupted")
        finally:
            consumer.close()

# Real-time Analytics with Kafka Streams (Python equivalent)
class RealTimeAnalytics:
    def __init__(self, kafka_manager):
        self.kafka_manager = kafka_manager
        self.running = False
        self.metrics = {}
    
    def process_sales_stream(self):
        """Process sales events in real-time"""
        self.running = True
        
        # Consume from sales events topic
        for message in self.kafka_manager.consume_events('sales-events', 'analytics-group'):
            if not self.running:
                break
            
            event = message['value']
            self.update_metrics(event)
            
            # Produce aggregated metrics every 100 events
            if len(self.metrics) % 100 == 0:
                self.produce_metrics()
    
    def update_metrics(self, event):
        """Update real-time metrics"""
        customer_id = event.get('customer_id')
        amount = event.get('amount', 0)
        product_category = event.get('product_category', 'unknown')
        
        # Customer metrics
        if customer_id not in self.metrics:
            self.metrics[customer_id] = {
                'total_spent': 0,
                'order_count': 0,
                'categories': set()
            }
        
        self.metrics[customer_id]['total_spent'] += amount
        self.metrics[customer_id]['order_count'] += 1
        self.metrics[customer_id]['categories'].add(product_category)
    
    def produce_metrics(self):
        """Produce aggregated metrics"""
        metrics_events = []
        
        for customer_id, metrics in self.metrics.items():
            metric_event = {
                'customer_id': customer_id,
                'total_spent': metrics['total_spent'],
                'order_count': metrics['order_count'],
                'unique_categories': len(metrics['categories']),
                'avg_order_value': metrics['total_spent'] / metrics['order_count'],
                'timestamp': datetime.now().isoformat()
            }
            metrics_events.append(metric_event)
        
        self.kafka_manager.produce_events('customer-metrics', metrics_events)
    
    def stop(self):
        self.running = False

# Usage Example
kafka_mgr = KafkaManager(['localhost:9092'])

# Create topics
kafka_mgr.create_topic('sales-events', num_partitions=6)
kafka_mgr.create_topic('customer-metrics', num_partitions=3)

# Sample sales events
sample_events = [
    {
        'customer_id': 'cust_001',
        'product_id': 'prod_123',
        'product_category': 'Electronics',
        'amount': 299.99,
        'timestamp': datetime.now().isoformat()
    },
    {
        'customer_id': 'cust_002', 
        'product_id': 'prod_456',
        'product_category': 'Clothing',
        'amount': 79.99,
        'timestamp': datetime.now().isoformat()
    }
]

# Produce events
kafka_mgr.produce_events('sales-events', sample_events)

# Start real-time analytics
analytics = RealTimeAnalytics(kafka_mgr)
analytics_thread = threading.Thread(target=analytics.process_sales_stream)
analytics_thread.start()

# Let it run for a while
time.sleep(60)

# Stop analytics
analytics.stop()
analytics_thread.join()
```

### Apache Spark Advanced

**Spark Streaming with Kafka**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.streaming import StreamingContext
import json

# Create Spark session with Kafka support
spark = SparkSession.builder \
    .appName("RealTimeAnalytics") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .config("spark.sql.streaming.schemaInference", "true") \
    .getOrCreate()

# Define schema for incoming events
event_schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("product_category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])

# Read from Kafka stream
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sales-events") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON data
parsed_df = kafka_df.select(
    from_json(col("value").cast("string"), event_schema).alias("data")
).select("data.*")

# Real-time aggregations
# 1. Customer spending by window
customer_spending = parsed_df \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        "customer_id",
        window(col("timestamp"), "5 minutes", "1 minute")  # 5-minute windows, sliding every minute
    ) \
    .agg(
        sum("amount").alias("total_spent"),
        count("*").alias("transaction_count"),
        avg("amount").alias("avg_transaction"),
        countDistinct("product_category").alias("unique_categories")
    )

# 2. Product category trends
category_trends = parsed_df \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        "product_category",
        window(col("timestamp"), "10 minutes", "5 minutes")
    ) \
    .agg(
        sum("amount").alias("total_revenue"),
        count("*").alias("transaction_count"),
        countDistinct("customer_id").alias("unique_customers")
    )

# Write customer spending to console (for monitoring)
customer_query = customer_spending.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", False) \
    .start()

# Write category trends to Kafka for downstream processing
category_query = category_trends \
    .select(to_json(struct("*")).alias("value")) \
    .writeStream \
    .outputMode("update") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "category-trends") \
    .option("checkpointLocation", "/tmp/checkpoint-trends") \
    .start()

# Write detailed events to data lake (S3/HDFS)
lake_query = parsed_df \
    .withColumn("year", year(col("timestamp"))) \
    .withColumn("month", month(col("timestamp"))) \
    .withColumn("day", dayofmonth(col("timestamp"))) \
    .writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "s3a://data-lake/sales-events/") \
    .partitionBy("year", "month", "day") \
    .option("checkpointLocation", "/tmp/checkpoint-lake") \
    .start()

# Wait for streams to finish
customer_query.awaitTermination()
category_query.awaitTermination()
lake_query.awaitTermination()
```

---

## ☁️ Cloud Data Platforms {#cloud}

### AWS Data Engineering Stack

**AWS S3 Data Lake with Lambda Processing**

```python
import boto3
import json
import pandas as pd
from datetime import datetime
import logging

# Lambda function for S3 event processing
def lambda_handler(event, context):
    """Process S3 events for incoming data files"""
    
    s3_client = boto3.client('s3')
    glue_client = boto3.client('glue')
    sns_client = boto3.client('sns')
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            logger.info(f"Processing file: s3://{bucket}/{key}")
            
            # Check if it's a data file
            if key.endswith('.csv') or key.endswith('.json'):
                
                # Trigger Glue job for processing
                job_name = 'sales-data-processing'
                
                response = glue_client.start_job_run(
                    JobName=job_name,
                    Arguments={
                        '--s3_input_path': f's3://{bucket}/{key}',
                        '--s3_output_path': f's3://{bucket}/processed/',
                        '--job_bookmark': 'job-bookmark-enable'
                    }
                )
                
                logger.info(f"Started Glue job {job_name} with run ID: {response['JobRunId']}")
                
                # Send SNS notification
                sns_client.publish(
                    TopicArn='arn:aws:sns:us-east-1:123456789012:data-pipeline-notifications',
                    Subject=f'Data Processing Started',
                    Message=f'Started processing file: s3://{bucket}/{key}'
                )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Files processed successfully')
        }
        
    except Exception as e:
        logger.error(f"Error processing files: {str(e)}")
        
        # Send error notification
        sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:123456789012:data-pipeline-alerts',
            Subject=f'Data Processing Error',
            Message=f'Error processing files: {str(e)}'
        )
        
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

# AWS Glue ETL Job
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME', 's3_input_path', 's3_output_path'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
input_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [args['s3_input_path']],
        "recurse": True
    },
    format="csv",
    format_options={
        "withHeader": True,
        "separator": ","
    }
)

# Data transformations
# Convert to Spark DataFrame for complex operations
df = input_dyf.toDF()

# Data cleaning and transformation
df_cleaned = df.filter(df.amount > 0) \
    .filter(df.customer_id.isNotNull()) \
    .withColumn("processed_date", current_date()) \
    .withColumn("year", year(col("order_date"))) \
    .withColumn("month", month(col("order_date"))) \
    .withColumn("quarter", quarter(col("order_date")))

# Convert back to DynamicFrame
output_dyf = DynamicFrame.fromDF(df_cleaned, glueContext, "cleaned_data")

# Write to S3 in Parquet format with partitioning
glueContext.write_dynamic_frame.from_options(
    frame=output_dyf,
    connection_type="s3",
    connection_options={
        "path": args['s3_output_path'],
        "partitionKeys": ["year", "month"]
    },
    format="glueparquet",
    format_options={
        "compression": "snappy"
    }
)

job.commit()
```

**Amazon Kinesis Data Streams**

```python
import boto3
import json
import time
from datetime import datetime
import threading
import random

class KinesisDataProcessor:
    def __init__(self, stream_name, region='us-east-1'):
        self.stream_name = stream_name
        self.kinesis_client = boto3.client('kinesis', region_name=region)
        self.running = False
    
    def create_stream(self, shard_count=1):
        """Create Kinesis stream"""
        try:
            self.kinesis_client.create_stream(
                StreamName=self.stream_name,
                ShardCount=shard_count
            )
            
            # Wait for stream to be active
            waiter = self.kinesis_client.get_waiter('stream_exists')
            waiter.wait(StreamName=self.stream_name)
            
            print(f"Stream {self.stream_name} created successfully")
            
        except self.kinesis_client.exceptions.ResourceInUseException:
            print(f"Stream {self.stream_name} already exists")
    
    def put_record(self, data, partition_key):
        """Put single record to stream"""
        response = self.kinesis_client.put_record(
            StreamName=self.stream_name,
            Data=json.dumps(data),
            PartitionKey=str(partition_key)
        )
        return response
    
    def put_records_batch(self, records):
        """Put multiple records to stream"""
        kinesis_records = []
        
        for record in records:
            kinesis_record = {
                'Data': json.dumps(record['data']),
                'PartitionKey': str(record['partition_key'])
            }
            kinesis_records.append(kinesis_record)
        
        # Kinesis put_records supports up to 500 records per request
        batch_size = 500
        responses = []
        
        for i in range(0, len(kinesis_records), batch_size):
            batch = kinesis_records[i:i+batch_size]
            
            response = self.kinesis_client.put_records(
                Records=batch,
                StreamName=self.stream_name
            )
            responses.append(response)
        
        return responses
    
    def consume_records(self, shard_iterator_type='TRIM_HORIZON'):
        """Consume records from stream"""
        
        # Get stream description
        stream_desc = self.kinesis_client.describe_stream(StreamName=self.stream_name)
        shard_id = stream_desc['StreamDescription']['Shards'][0]['ShardId']
        
        # Get shard iterator
        shard_iterator_response = self.kinesis_client.get_shard_iterator(
            StreamName=self.stream_name,
            ShardId=shard_id,
            ShardIteratorType=shard_iterator_type
        )
        
        shard_iterator = shard_iterator_response['ShardIterator']
        
        while self.running:
            try:
                # Get records
                response = self.kinesis_client.get_records(
                    ShardIterator=shard_iterator,
                    Limit=100
                )
                
                records = response['Records']
                
                if records:
                    for record in records:
                        data = json.loads(record['Data'])
                        print(f"Processed record: {data}")
                        yield data
                
                # Update shard iterator
                shard_iterator = response['NextShardIterator']
                
                # Sleep to avoid hitting rate limits
                time.sleep(1)
                
            except Exception as e:
                print(f"Error consuming records: {e}")
                break
    
    def start_consumer(self):
        """Start consuming records in background thread"""
        self.running = True
        consumer_thread = threading.Thread(target=self._consumer_loop)
        consumer_thread.start()
        return consumer_thread
    
    def stop_consumer(self):
        """Stop consuming records"""
        self.running = False
    
    def _consumer_loop(self):
        """Consumer loop for background processing"""
        for record in self.consume_records():
            if not self.running:
                break
            # Process record here
            self._process_record(record)
    
    def _process_record(self, record):
        """Process individual record"""
        # Implement your record processing logic here
        print(f"Processing: {record}")

# Usage example
kinesis_processor = KinesisDataProcessor('sales-stream')

# Create stream
kinesis_processor.create_stream(shard_count=2)

# Generate sample data
def generate_sales_events(count=100):
    events = []
    for i in range(count):
        event = {
            'data': {
                'event_id': f'evt_{i:06d}',
                'customer_id': f'cust_{random.randint(1, 1000):04d}',
                'product_id': f'prod_{random.randint(1, 100):03d}',
                'amount': round(random.uniform(10, 500), 2),
                'timestamp': datetime.now().isoformat()
            },
            'partition_key': f'cust_{random.randint(1, 1000):04d}'
        }
        events.append(event)
    return events

# Send data to stream
sample_events = generate_sales_events(1000)
responses = kinesis_processor.put_records_batch(sample_events)
print(f"Sent {len(sample_events)} events to stream")

# Start consuming
consumer_thread = kinesis_processor.start_consumer()

# Let it run for a while
time.sleep(30)

# Stop consumer
kinesis_processor.stop_consumer()
consumer_thread.join()
```

### Google Cloud Platform (GCP) Data Engineering

**BigQuery Data Processing**

```python
from google.cloud import bigquery
from google.cloud import storage
import pandas as pd
from datetime import datetime, timedelta
import logging

class GCPDataPipeline:
    def __init__(self, project_id, dataset_id):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.bq_client = bigquery.Client(project=project_id)
        self.storage_client = storage.Client(project=project_id)
        self.logger = logging.getLogger(__name__)
    
    def create_dataset(self):
        """Create BigQuery dataset"""
        dataset_id_full = f"{self.project_id}.{self.dataset_id}"
        dataset = bigquery.Dataset(dataset_id_full)
        dataset.location = "US"
        dataset.description = "Sales data analytics dataset"
        
        try:
            dataset = self.bq_client.create_dataset(dataset)
            self.logger.info(f"Created dataset {dataset_id_full}")
        except Exception as e:
            if "Already Exists" in str(e):
                self.logger.info(f"Dataset {dataset_id_full} already exists")
            else:
                raise e
    
    def create_tables(self):
        """Create BigQuery tables with optimized schema"""
        
        # Fact table for sales
        sales_schema = [
            bigquery.SchemaField("sale_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("customer_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("product_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("quantity", "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("unit_price", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("total_amount", "NUMERIC", mode="REQUIRED"),
            bigquery.SchemaField("sale_date", "DATE", mode="REQUIRED"),
            bigquery.SchemaField("sale_timestamp", "TIMESTAMP", mode="REQUIRED"),
            bigquery.SchemaField("product_category", "STRING"),
            bigquery.SchemaField("customer_segment", "STRING"),
            bigquery.SchemaField("created_at", "TIMESTAMP", mode="REQUIRED")
        ]
        
        # Create partitioned and clustered table
        table_id = f"{self.project_id}.{self.dataset_id}.fact_sales"
        table = bigquery.Table(table_id, schema=sales_schema)
        
        # Partition by sale_date for better query performance
        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="sale_date"
        )
        
        # Cluster by customer_segment and product_category
        table.clustering_fields = ["customer_segment", "product_category"]
        
        try:
            table = self.bq_client.create_table(table)
            self.logger.info(f"Created table {table_id}")
        except Exception as e:
            if "Already Exists" in str(e):
                self.logger.info(f"Table {table_id} already exists")
            else:
                raise e
    
    def load_data_from_gcs(self, gcs_uri, table_name, write_disposition="WRITE_APPEND"):
        """Load data from Google Cloud Storage to BigQuery"""
        
        table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"
        
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip header row
            autodetect=True,
            write_disposition=write_disposition
        )
        
        load_job = self.bq_client.load_table_from_uri(
            gcs_uri, table_id, job_config=job_config
        )
        
        load_job.result()  # Wait for job to complete
        
        destination_table = self.bq_client.get_table(table_id)
        self.logger.info(f"Loaded {destination_table.num_rows} rows to {table_id}")
    
    def run_analytics_query(self):
        """Run complex analytics query"""
        
        query = f"""
        WITH daily_sales AS (
            SELECT 
                sale_date,
                customer_segment,
                product_category,
                COUNT(*) as transaction_count,
                SUM(total_amount) as daily_revenue,
                AVG(total_amount) as avg_transaction_value,
                COUNT(DISTINCT customer_id) as unique_customers
            FROM `{self.project_id}.{self.dataset_id}.fact_sales`
            WHERE sale_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
            GROUP BY sale_date, customer_segment, product_category
        ),
        segment_performance AS (
            SELECT 
                customer_segment,
                SUM(daily_revenue) as total_revenue,
                AVG(daily_revenue) as avg_daily_revenue,
                SUM(transaction_count) as total_transactions,
                SUM(unique_customers) as total_customers,
                COUNT(DISTINCT sale_date) as active_days
            FROM daily_sales
            GROUP BY customer_segment
        )
        SELECT 
            customer_segment,
            total_revenue,
            avg_daily_revenue,
            total_transactions,
            total_customers,
            active_days,
            total_revenue / total_customers as revenue_per_customer,
            total_transactions / total_customers as transactions_per_customer
        FROM segment_performance
        ORDER BY total_revenue DESC
        """
        
        query_job = self.bq_client.query(query)
        results = query_job.result()
        
        # Convert to pandas DataFrame
        df = results.to_dataframe()
        return df
    
    def create_scheduled_query(self, query_name, query_sql, schedule="every 24 hours"):
        """Create scheduled query for regular data processing"""
        
        from google.cloud import bigquery_datatransfer
        
        transfer_client = bigquery_datatransfer.DataTransferServiceClient()
        
        parent = transfer_client.common_project_path(self.project_id)
        
        transfer_config = {
            "destination_dataset_id": self.dataset_id,
            "display_name": query_name,
            "data_source_id": "scheduled_query",
            "schedule": schedule,
            "params": {
                "query": query_sql,
                "write_disposition": "WRITE_APPEND"
            }
        }
        
        response = transfer_client.create_transfer_config(
            parent=parent,
            transfer_config=transfer_config
        )
        
        self.logger.info(f"Created scheduled query: {response.name}")
        return response
    
    def export_to_gcs(self, table_name, gcs_bucket, file_prefix):
        """Export BigQuery table to Google Cloud Storage"""
        
        table_id = f"{self.project_id}.{self.dataset_id}.{table_name}"
        destination_uri = f"gs://{gcs_bucket}/{file_prefix}_*.parquet"
        
        job_config = bigquery.ExtractJobConfig()
        job_config.destination_format = bigquery.DestinationFormat.PARQUET
        job_config.compression = bigquery.Compression.SNAPPY
        
        extract_job = self.bq_client.extract_table(
            table_id,
            destination_uri,
            job_config=job_config
        )
        
        extract_job.result()  # Wait for job to complete
        
        self.logger.info(f"Exported {table_name} to {destination_uri}")

# Usage
gcp_pipeline = GCPDataPipeline('my-project-id', 'sales_analytics')

# Setup
gcp_pipeline.create_dataset()
gcp_pipeline.create_tables()

# Load data
gcp_pipeline.load_data_from_gcs(
    'gs://my-data-bucket/sales-data/*.csv',
    'fact_sales'
)

# Run analytics
results_df = gcp_pipeline.run_analytics_query()
print("Analytics Results:")
print(results_df)

# Export results
gcp_pipeline.export_to_gcs('fact_sales', 'my-export-bucket', 'sales_export')
```

### Azure Data Engineering

**Azure Data Factory Pipelines**

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import *
import json

class AzureDataFactoryManager:
    def __init__(self, subscription_id, resource_group, factory_name):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.factory_name = factory_name
        
        # Authenticate
        self.credential = DefaultAzureCredential()
        self.adf_client = DataFactoryManagementClient(
            self.credential, 
            subscription_id
        )
    
    def create_linked_services(self):
        """Create linked services for data sources"""
        
        # Azure SQL Database linked service
        sql_db_linked_service = LinkedServiceResource(
            properties=AzureSqlDatabaseLinkedService(
                connection_string=SecureString(
                    value="Server=tcp:myserver.database.windows.net,1433;Database=mydb;User ID=myuser;Password=mypassword;Trusted_Connection=False;Encrypt=True;Connection Timeout=30;"
                )
            )
        )
        
        self.adf_client.linked_services.create_or_update(
            self.resource_group,
            self.factory_name,
            "AzureSqlDatabase1",
            sql_db_linked_service
        )
        
        # Azure Blob Storage linked service
        blob_storage_linked_service = LinkedServiceResource(
            properties=AzureBlobStorageLinkedService(
                connection_string=SecureString(
                    value="DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=mykey;EndpointSuffix=core.windows.net"
                )
            )
        )
        
        self.adf_client.linked_services.create_or_update(
            self.resource_group,
            self.factory_name,
            "AzureBlobStorage1",
            blob_storage_linked_service
        )
    
    def create_datasets(self):
        """Create datasets for source and sink"""
        
        # Source dataset (SQL Database)
        source_dataset = DatasetResource(
            properties=AzureSqlTableDataset(
                linked_service_name=LinkedServiceReference(
                    reference_name="AzureSqlDatabase1"
                ),
                table_name="sales_data"
            )
        )
        
        self.adf_client.datasets.create_or_update(
            self.resource_group,
            self.factory_name,
            "SourceDataset",
            source_dataset
        )
        
        # Sink dataset (Blob Storage)
        sink_dataset = DatasetResource(
            properties=DelimitedTextDataset(
                linked_service_name=LinkedServiceReference(
                    reference_name="AzureBlobStorage1"
                ),
                location=BlobStorageLocation(
                    container="data",
                    folder_path="processed"
                ),
                column_delimiter=",",
                first_row_as_header=True
            )
        )
        
        self.adf_client.datasets.create_or_update(
            self.resource_group,
            self.factory_name,
            "SinkDataset",
            sink_dataset
        )
    
    def create_pipeline(self):
        """Create data processing pipeline"""
        
        # Copy activity
        copy_activity = CopyActivity(
            name="CopyFromSQLToBlob",
            inputs=[DatasetReference(reference_name="SourceDataset")],
            outputs=[DatasetReference(reference_name="SinkDataset")],
            source=SqlSource(),
            sink=DelimitedTextSink()
        )
        
        # Data flow activity for transformations
        data_flow_activity = ExecuteDataFlowActivity(
            name="TransformData",
            data_flow=DataFlowReference(reference_name="TransformationDataFlow"),
            staging=DataFlowStagingInfo(
                linked_service=LinkedServiceReference(
                    reference_name="AzureBlobStorage1"
                )
            )
        )
        
        # Create pipeline
        pipeline = PipelineResource(
            activities=[copy_activity, data_flow_activity],
            parameters={
                "inputPath": ParameterSpecification(type="String"),
                "outputPath": ParameterSpecification(type="String")
            }
        )
        
        self.adf_client.pipelines.create_or_update(
            self.resource_group,
            self.factory_name,
            "SalesDataPipeline",
            pipeline
        )
    
    def create_trigger(self):
        """Create trigger to schedule pipeline"""
        
        trigger = ScheduleTriggerResource(
            properties=ScheduleTrigger(
                recurrence=ScheduleTriggerRecurrence(
                    frequency="Day",
                    interval=1,
                    start_time="2024-01-01T00:00:00Z",
                    time_zone="UTC",
                    schedule=RecurrenceSchedule(
                        hours=[2],  # Run at 2 AM
                        minutes=[0]
                    )
                ),
                pipelines=[
                    TriggerPipelineReference(
                        pipeline_reference=PipelineReference(
                            reference_name="SalesDataPipeline"
                        ),
                        parameters={
                            "inputPath": "sales/raw",
                            "outputPath": "sales/processed"
                        }
                    )
                ]
            )
        )
        
        self.adf_client.triggers.create_or_update(
            self.resource_group,
            self.factory_name,
            "DailyTrigger",
            trigger
        )
    
    def run_pipeline(self, pipeline_name, parameters=None):
        """Manually trigger pipeline run"""
        
        run_response = self.adf_client.pipelines.create_run(
            self.resource_group,
            self.factory_name,
            pipeline_name,
            parameters=parameters or {}
        )
        
        return run_response.run_id
    
    def monitor_pipeline_run(self, run_id):
        """Monitor pipeline run status"""
        
        pipeline_run = self.adf_client.pipeline_runs.get(
            self.resource_group,
            self.factory_name,
            run_id
        )
        
        return {
            'status': pipeline_run.status,
            'start_time': pipeline_run.run_start,
            'end_time': pipeline_run.run_end,
            'duration': pipeline_run.duration_in_ms
        }

# Usage
adf_manager = AzureDataFactoryManager(
    subscription_id="your-subscription-id",
    resource_group="my-resource-group",
    factory_name="my-data-factory"
)

# Setup pipeline components
adf_manager.create_linked_services()
adf_manager.create_datasets()
adf_manager.create_pipeline()
adf_manager.create_trigger()

# Run pipeline manually
run_id = adf_manager.run_pipeline("SalesDataPipeline")
print(f"Started pipeline run: {run_id}")

# Monitor run
import time
while True:
    status = adf_manager.monitor_pipeline_run(run_id)
    print(f"Pipeline status: {status['status']}")
    
    if status['status'] in ['Succeeded', 'Failed', 'Cancelled']:
        break
    
    time.sleep(30)
```

---

## 🌊 Stream Processing {#streaming}

### Apache Flink for Complex Event Processing

```python
# Note: This is pseudo-code as PyFlink has specific setup requirements
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.functions import MapFunction, FilterFunction, KeyedProcessFunction
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types
from pyflink.common.time import Time
import json

class EventEnrichmentFunction(MapFunction):
    """Enrich events with additional data"""
    
    def map(self, value):
        event = json.loads(value)
        
        # Add processing metadata
        event['processed_timestamp'] = time.time()
        event['processing_version'] = '1.0'
        
        # Enrich with business logic
        if event.get('amount', 0) > 1000:
            event['is_high_value'] = True
            event['priority'] = 'HIGH'
        else:
            event['is_high_value'] = False
            event['priority'] = 'NORMAL'
        
        return json.dumps(event)

class FraudDetectionFunction(KeyedProcessFunction):
    """Detect fraudulent patterns using state"""
    
    def __init__(self):
        self.transaction_count_state = None
        self.amount_sum_state = None
    
    def open(self, runtime_context):
        # Initialize state
        self.transaction_count_state = runtime_context.get_state(
            ValueStateDescriptor("transaction_count", Types.INT())
        )
        self.amount_sum_state = runtime_context.get_state(
            ValueStateDescriptor("amount_sum", Types.DOUBLE())
        )
    
    def process_element(self, value, ctx, out):
        event = json.loads(value)
        
        # Get current state
        current_count = self.transaction_count_state.value() or 0
        current_sum = self.amount_sum_state.value() or 0.0
        
        # Update state
        new_count = current_count + 1
        new_sum = current_sum + event.get('amount', 0)
        
        self.transaction_count_state.update(new_count)
        self.amount_sum_state.update(new_sum)
        
        # Fraud detection logic
        time_window_minutes = 10
        
        # Rule 1: Too many transactions in short time
        if new_count > 20:  # More than 20 transactions
            event['fraud_score'] = min(100, new_count * 2)
            event['fraud_reason'] = 'High transaction frequency'
            event['is_fraud_suspected'] = True
        
        # Rule 2: Unusually high spending
        elif new_sum > 10000:  # More than $10k in window
            event['fraud_score'] = min(100, new_sum / 100)
            event['fraud_reason'] = 'High spending amount'
            event['is_fraud_suspected'] = True
        
        else:
            event['fraud_score'] = 0
            event['is_fraud_suspected'] = False
        
        out.collect(json.dumps(event))
        
        # Set timer to clear state after time window
        ctx.timer_service().register_event_time_timer(
            ctx.timestamp() + Time.minutes(time_window_minutes).to_milliseconds()
        )
    
    def on_timer(self, timestamp, ctx, out):
        # Clear state after time window
        self.transaction_count_state.clear()
        self.amount_sum_state.clear()

def create_flink_pipeline():
    """Create Flink streaming pipeline"""
    
    # Create execution environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(4)
    env.enable_checkpointing(60000)  # Checkpoint every minute
    
    # Kafka consumer properties
    kafka_props = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'flink-fraud-detection'
    }
    
    # Create Kafka consumer
    kafka_consumer = FlinkKafkaConsumer(
        topics=['financial-transactions'],
        deserialization_schema=SimpleStringSchema(),
        properties=kafka_props
    )
    
    # Start from latest offset
    kafka_consumer.set_start_from_latest()
    
    # Create data stream
    transaction_stream = env.add_source(kafka_consumer)
    
    # Data processing pipeline
    processed_stream = transaction_stream \
        .map(EventEnrichmentFunction()) \
        .filter(lambda event: json.loads(event).get('amount', 0) > 0) \
        .key_by(lambda event: json.loads(event).get('customer_id')) \
        .process(FraudDetectionFunction())
    
    # Split stream based on fraud detection
    fraud_stream = processed_stream.filter(
        lambda event: json.loads(event).get('is_fraud_suspected', False)
    )
    
    normal_stream = processed_stream.filter(
        lambda event: not json.loads(event).get('is_fraud_suspected', False)
    )
    
    # Send fraud alerts to alert topic
    fraud_stream.add_sink(
        FlinkKafkaProducer(
            topic='fraud-alerts',
            serialization_schema=SimpleStringSchema(),
            producer_config=kafka_props
        )
    )
    
    # Send normal transactions to processed topic
    normal_stream.add_sink(
        FlinkKafkaProducer(
            topic='processed-transactions',
            serialization_schema=SimpleStringSchema(),
            producer_config=kafka_props
        )
    )
    
    # Execute pipeline
    env.execute("Fraud Detection Pipeline")

# Run the pipeline
if __name__ == "__main__":
    create_flink_pipeline()
```

### Real-time Analytics with Apache Druid

```python
import requests
import json
import pandas as pd
from datetime import datetime, timedelta

class DruidConnector:
    def __init__(self, broker_url='http://localhost:8082'):
        self.broker_url = broker_url
    
    def submit_ingestion_task(self, datasource_name, kafka_config):
        """Submit Kafka ingestion task to Druid"""
        
        task_spec = {
            "type": "kafka",
            "dataSchema": {
                "dataSource": datasource_name,
                "timestampSpec": {
                    "column": "timestamp",
                    "format": "iso"
                },
                "dimensionsSpec": {
                    "dimensions": [
                        "customer_id",
                        "product_category",
                        "event_type",
                        "country"
                    ]
                },
                "metricsSpec": [
                    {
                        "name": "count",
                        "type": "count"
                    },
                    {
                        "name": "total_amount",
                        "type": "doubleSum",
                        "fieldName": "amount"
                    },
                    {
                        "name": "unique_customers",
                        "type": "hyperUnique",
                        "fieldName": "customer_id"
                    }
                ],
                "granularitySpec": {
                    "type": "uniform",
                    "segmentGranularity": "hour",
                    "queryGranularity": "minute"
                }
            },
            "ioConfig": {
                "topic": kafka_config['topic'],
                "consumerProperties": kafka_config['consumer_properties'],
                "taskDuration": "PT1H",  # 1 hour
                "replicas": 2,
                "taskCount": 4
            },
            "tuningConfig": {
                "type": "kafka",
                "maxRowsPerSegment": 5000000,
                "intermediatePersistPeriod": "PT10M"
            }
        }
        
        response = requests.post(
            f"{self.broker_url}/druid/indexer/v1/task",
            json=task_spec,
            headers={'Content-Type': 'application/json'}
        )
        
        return response.json()
    
    def query_timeseries(self, datasource, start_time, end_time, granularity="minute"):
        """Run timeseries query"""
        
        query = {
            "queryType": "timeseries",
            "dataSource": datasource,
            "granularity": granularity,
            "intervals": [f"{start_time}/{end_time}"],
            "aggregations": [
                {
                    "type": "longSum",
                    "name": "total_events",
                    "fieldName": "count"
                },
                {
                    "type": "doubleSum", 
                    "name": "total_revenue",
                    "fieldName": "total_amount"
                },
                {
                    "type": "hyperUniqueCardinality",
                    "name": "unique_customers",
                    "fieldName": "unique_customers"
                }
            ],
            "postAggregations": [
                {
                    "type": "arithmetic",
                    "name": "avg_revenue_per_customer",
                    "fn": "/",
                    "fields": [
                        {"type": "fieldAccess", "fieldName": "total_revenue"},
                        {"type": "fieldAccess", "fieldName": "unique_customers"}
                    ]
                }
            ]
        }
        
        response = requests.post(
            f"{self.broker_url}/druid/v2/",
            json=query,
            headers={'Content-Type': 'application/json'}
        )
        
        return response.json()
    
    def query_top_n(self, datasource, dimension, metric, threshold=10):
        """Run TopN query for top customers, products, etc."""
        
        query = {
            "queryType": "topN",
            "dataSource": datasource,
            "dimension": dimension,
            "threshold": threshold,
            "metric": metric,
            "granularity": "all",
            "intervals": ["2024-01-01/2024-12-31"],
            "aggregations": [
                {
                    "type": "longSum",
                    "name": "total_events",
                    "fieldName": "count"
                },
                {
                    "type": "doubleSum",
                    "name": "total_amount",
                    "fieldName": "total_amount"
                }
            ]
        }
        
        response = requests.post(
            f"{self.broker_url}/druid/v2/",
            json=query,
            headers={'Content-Type': 'application/json'}
        )
        
        return response.json()
    
    def query_group_by(self, datasource, dimensions, filters=None):
        """Run GroupBy query with multiple dimensions"""
        
        query = {
            "queryType": "groupBy",
            "dataSource": datasource,
            "dimensions": dimensions,
            "granularity": "hour",
            "intervals": ["2024-01-01/2024-12-31"],
            "aggregations": [
                {
                    "type": "longSum",
                    "name": "event_count",
                    "fieldName": "count"
                },
                {
                    "type": "doubleSum",
                    "name": "revenue",
                    "fieldName": "total_amount"
                },
                {
                    "type": "hyperUniqueCardinality",
                    "name": "unique_customers",
                    "fieldName": "unique_customers"
                }
            ]
        }
        
        if filters:
            query["filter"] = filters
        
        response = requests.post(
            f"{self.broker_url}/druid/v2/",
            json=query,
            headers={'Content-Type': 'application/json'}
        )
        
        return response.json()

# Usage
druid = DruidConnector()

# Setup Kafka ingestion
kafka_config = {
    'topic': 'sales-events',
    'consumer_properties': {
        'bootstrap.servers': 'localhost:9092'
    }
}

# Start ingestion
ingestion_result = druid.submit_ingestion_task('sales_events', kafka_config)
print(f"Ingestion task submitted: {ingestion_result}")

# Real-time analytics queries
# 1. Revenue trend over time
revenue_trend = druid.query_timeseries(
    'sales_events',
    (datetime.now() - timedelta(hours=24)).isoformat(),
    datetime.now().isoformat(),
    granularity="PT5M"  # 5-minute intervals
)

print("Revenue Trend (Last 24 hours):")
for point in revenue_trend:
    print(f"{point['timestamp']}: ${point['result']['total_revenue']:.2f}")

# 2. Top customers by spending
top_customers = druid.query_top_n(
    'sales_events',
    'customer_id',
    'total_amount',
    threshold=20
)

print("\nTop 20 Customers by Revenue:")
for customer in top_customers[0]['result']:
    print(f"Customer {customer['customer_id']}: ${customer['total_amount']:.2f}")

# 3. Sales by product category and country
category_sales = druid.query_group_by(
    'sales_events',
    ['product_category', 'country'],
    filters={
        "type": "and",
        "fields": [
            {
                "type": "selector",
                "dimension": "event_type",
                "value": "purchase"
            },
            {
                "type": "bound",
                "dimension": "total_amount",
                "lower": "100"
            }
        ]
    }
)

print("\nSales by Category and Country (Orders > $100):")
for result in category_sales:
    event = result['event']
    print(f"{event['product_category']} - {event['country']}: "
          f"${event['revenue']:.2f} ({event['event_count']} orders)")
```

---

## ✅ Data Quality & Governance {#quality}

### Data Quality Framework with Great Expectations

```python
import great_expectations as ge
from great_expectations.data_context import DataContext
from great_expectations.checkpoint import SimpleCheckpoint
import pandas as pd
import logging
from datetime import datetime
from typing import Dict, List, Any

class DataQualityFramework:
    def __init__(self, context_root_dir="./great_expectations"):
        self.context = DataContext(context_root_dir=context_root_dir)
        self.logger = logging.getLogger(__name__)
    
    def create_expectation_suite(self, suite_name: str, data_asset_name: str):
        """Create a new expectation suite"""
        
        # Create suite
        suite = self.context.create_expectation_suite(
            expectation_suite_name=suite_name,
            overwrite_existing=True
        )
        
        return suite
    
    def define_sales_data_expectations(self, suite_name: str = "sales_data_quality"):
        """Define comprehensive expectations for sales data"""
        
        suite = self.create_expectation_suite(suite_name, "sales_data")
        
        # Create a validator
        validator = self.context.get_validator(
            batch_request=RuntimeBatchRequest(
                datasource_name="pandas_datasource",
                data_connector_name="default_runtime_data_connector_name",
                data_asset_name="sales_data",
                runtime_parameters={"batch_data": pd.DataFrame()}  # Empty for now
            ),
            expectation_suite_name=suite_name
        )
        
        # Column existence expectations
        validator.expect_table_columns_to_match_ordered_list(
            column_list=["order_id", "customer_id", "product_id", "quantity", 
                        "unit_price", "total_amount", "order_date", "status"]
        )
        
        # Data type expectations
        validator.expect_column_values_to_be_of_type("order_id", "str")
        validator.expect_column_values_to_be_of_type("customer_id", "str")
        validator.expect_column_values_to_be_of_type("quantity", "int")
        validator.expect_column_values_to_be_of_type("unit_price", "float")
        validator.expect_column_values_to_be_of_type("total_amount", "float")
        
        # Null value expectations
        validator.expect_column_values_to_not_be_null("order_id")
        validator.expect_column_values_to_not_be_null("customer_id")
        validator.expect_column_values_to_not_be_null("product_id")
        validator.expect_column_values_to_not_be_null("total_amount")
        
        # Uniqueness expectations
        validator.expect_column_values_to_be_unique("order_id")
        
        # Range expectations
        validator.expect_column_values_to_be_between("quantity", min_value=1, max_value=1000)
        validator.expect_column_values_to_be_between("unit_price", min_value=0.01, max_value=10000)
        validator.expect_column_values_to_be_between("total_amount", min_value=0.01, max_value=100000)
        
        # Set expectations
        validator.expect_column_values_to_be_in_set(
            "status", 
            ["pending", "confirmed", "shipped", "delivered", "cancelled"]
        )
        
        # Pattern expectations
        validator.expect_column_values_to_match_regex(
            "order_id",
            regex=r"^ORD-\d{8}-\d{6}$"  # Format: ORD-YYYYMMDD-HHMMSS
        )
        
        # Business logic expectations
        validator.expect_column_pair_values_A_to_be_greater_than_B(
            column_A="total_amount",
            column_B="unit_price",
            or_equal=True
        )
        
        # Date expectations
        validator.expect_column_values_to_be_between(
            "order_date",
            min_value="2020-01-01",
            max_value=datetime.now().strftime("%Y-%m-%d")
        )
        
        # Statistical expectations
        validator.expect_column_mean_to_be_between("total_amount", min_value=10, max_value=500)
        validator.expect_column_stdev_to_be_between("total_amount", min_value=1, max_value=200)
        
        # Save the suite
        validator.save_expectation_suite(discard_failed_expectations=False)
        
        return validator.get_expectation_suite()
    
    def validate_dataframe(self, df: pd.DataFrame, suite_name: str) -> Dict[str, Any]:
        """Validate dataframe against expectation suite"""
        
        # Create batch request
        batch_request = RuntimeBatchRequest(
            datasource_name="pandas_datasource",
            data_connector_name="default_runtime_data_connector_name",
            data_asset_name="sales_data",
            runtime_parameters={"batch_data": df},
            batch_identifiers={"batch_id": f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"}
        )
        
        # Get validator
        validator = self.context.get_validator(
            batch_request=batch_request,
            expectation_suite_name=suite_name
        )
        
        # Run validation
        validation_result = validator.validate()
        
        # Process results
        results_summary = {
            "success": validation_result.success,
            "statistics": validation_result.statistics,
            "results": []
        }
        
        for result in validation_result.results:
            result_dict = {
                "expectation_type": result.expectation_config.expectation_type,
                "success": result.success,
                "result": result.result
            }
            
            if not result.success:
                result_dict["failure_info"] = {
                    "observed_value": result.result.get("observed_value"),
                    "element_count": result.result.get("element_count"),
                    "missing_count": result.result.get("missing_count"),
                    "unexpected_count": result.result.get("unexpected_count")
                }
            
            results_summary["results"].append(result_dict)
        
        return results_summary
    
    def create_checkpoint(self, checkpoint_name: str, suite_names: List[str]):
        """Create checkpoint for automated validation"""
        
        checkpoint_config = {
            "name": checkpoint_name,
            "config_version": 1,
            "template_name": None,
            "run_name_template": f"{checkpoint_name}_%Y%m%d-%H%M%S",
            "expectation_suite_name": None,
            "batch_request": {},
            "action_list": [
                {
                    "name": "store_validation_result",
                    "action": {
                        "class_name": "StoreValidationResultAction"
                    }
                },
                {
                    "name": "store_evaluation_params",
                    "action": {
                        "class_name": "StoreEvaluationParametersAction"
                    }
                },
                {
                    "name": "update_data_docs",
                    "action": {
                        "class_name": "UpdateDataDocsAction"
                    }
                }
            ],
            "evaluation_parameters": {},
            "runtime_configuration": {},
            "validations": []
        }
        
        # Add validations for each suite
        for suite_name in suite_names:
            validation_config = {
                "batch_request": {
                    "datasource_name": "pandas_datasource",
                    "data_connector_name": "default_runtime_data_connector_name",
                    "data_asset_name": "sales_data"
                },
                "expectation_suite_name": suite_name
            }
            checkpoint_config["validations"].append(validation_config)
        
        # Create checkpoint
        checkpoint = SimpleCheckpoint(
            f"{checkpoint_name}_checkpoint",
            self.context,
            **checkpoint_config
        )
        
        return checkpoint
    
    def automated_data_profiling(self, df: pd.DataFrame, suite_name: str = "auto_profiled"):
        """Automatically profile data and create basic expectations"""
        
        # Create batch request
        batch_request = RuntimeBatchRequest(
            datasource_name="pandas_datasource",
            data_connector_name="default_runtime_data_connector_name",
            data_asset_name="auto_profiled_data",
            runtime_parameters={"batch_data": df}
        )
        
        # Get validator
        validator = self.context.get_validator(
            batch_request=batch_request,
            expectation_suite_name=suite_name,
            create_expectation_suite_with_name=suite_name
        )
        
        # Auto-profile the dataset
        profiler_config = {
            "ignored_columns": [],
            "not_null_only": False,
            "primary_or_compound_key": [],
            "semantic_types_dict": {},
            "table_expectations_only": False,
            "value_set_threshold": "MANY"
        }
        
        # This would normally use the UserConfigurableProfiler
        # For demonstration, we'll add some basic expectations
        
        for column in df.columns:
            # Null expectations
            null_percentage = df[column].isnull().sum() / len(df) * 100
            if null_percentage < 5:  # Less than 5% nulls
                validator.expect_column_values_to_not_be_null(column)
            
            # Type expectations
            if df[column].dtype in ['int64', 'int32']:
                validator.expect_column_values_to_be_of_type(column, "int")
                # Range expectations
                min_val, max_val = df[column].min(), df[column].max()
                validator.expect_column_values_to_be_between(
                    column, min_value=min_val, max_value=max_val
                )
            elif df[column].dtype in ['float64', 'float32']:
                validator.expect_column_values_to_be_of_type(column, "float")
                min_val, max_val = df[column].min(), df[column].max()
                validator.expect_column_values_to_be_between(
                    column, min_value=min_val, max_value=max_val
                )
            elif df[column].dtype == 'object':
                unique_count = df[column].nunique()
                if unique_count <= 20:  # Categorical with few values
                    unique_values = df[column].unique().tolist()
                    validator.expect_column_values_to_be_in_set(column, unique_values)
        
        # Save the suite
        validator.save_expectation_suite(discard_failed_expectations=False)
        
        return validator.get_expectation_suite()

# Data lineage tracking
class DataLineageTracker:
    def __init__(self):
        self.lineage_graph = {}
        self.logger = logging.getLogger(__name__)
    
    def track_data_flow(self, source: str, target: str, transformation: str, metadata: Dict = None):
        """Track data flow between source and target"""
        
        lineage_entry = {
            "source": source,
            "target": target,
            "transformation": transformation,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        if source not in self.lineage_graph:
            self.lineage_graph[source] = []
        
        self.lineage_graph[source].append(lineage_entry)
        
        self.logger.info(f"Tracked lineage: {source} -> {target} via {transformation}")
    
    def get_data_lineage(self, data_asset: str) -> List[Dict]:
        """Get lineage for a specific data asset"""
        
        lineage = []
        
        # Find as source
        if data_asset in self.lineage_graph:
            lineage.extend(self.lineage_graph[data_asset])
        
        # Find as target
        for source, flows in self.lineage_graph.items():
            for flow in flows:
                if flow["target"] == data_asset:
                    lineage.append(flow)
        
        return lineage
    
    def export_lineage_graph(self, format: str = "json") -> str:
        """Export lineage graph in various formats"""
        
        if format == "json":
            return json.dumps(self.lineage_graph, indent=2)
        elif format == "dot":
            # Generate DOT format for Graphviz
            dot_content = "digraph DataLineage {\n"
            for source, flows in self.lineage_graph.items():
                for flow in flows:
                    dot_content += f'  "{source}" -> "{flow["target"]}" [label="{flow["transformation"]}"];\n'
            dot_content += "}\n"
            return dot_content
        else:
            raise ValueError(f"Unsupported format: {format}")

# Usage examples
if __name__ == "__main__":
    # Initialize data quality framework
    dq_framework = DataQualityFramework()
    
    # Create sample sales data
    sample_data = pd.DataFrame({
        'order_id': ['ORD-20240101-120000', 'ORD-20240101-120001', 'ORD-20240101-120002'],
        'customer_id': ['CUST001', 'CUST002', 'CUST001'],
        'product_id': ['PROD001', 'PROD002', 'PROD003'],
        'quantity': [2, 1, 3],
        'unit_price': [25.50, 15.99, 30.00],
        'total_amount': [51.00, 15.99, 90.00],
        'order_date': ['2024-01-01', '2024-01-01', '2024-01-01'],
        'status': ['confirmed', 'shipped', 'confirmed']
    })
    
    # Define expectations
    suite = dq_framework.define_sales_data_expectations()
    print(f"Created expectation suite with {len(suite.expectations)} expectations")
    
    # Validate data
    validation_results = dq_framework.validate_dataframe(sample_data, "sales_data_quality")
    
    print(f"\nValidation Results:")
    print(f"Success: {validation_results['success']}")
    print(f"Total Expectations: {validation_results['statistics']['evaluated_expectations']}")
    print(f"Successful Expectations: {validation_results['statistics']['successful_expectations']}")
    print(f"Failed Expectations: {validation_results['statistics']['unsuccessful_expectations']}")
    
    # Track data lineage
    lineage_tracker = DataLineageTracker()
    
    lineage_tracker.track_data_flow(
        source="raw_orders_table",
        target="cleaned_orders_table", 
        transformation="data_cleaning_pipeline",
        metadata={"pipeline_version": "1.2.3", "records_processed": 1000}
    )
    
    lineage_tracker.track_data_flow(
        source="cleaned_orders_table",
        target="sales_analytics_table",
        transformation="aggregation_pipeline",
        metadata={"aggregation_type": "daily_summary"}
    )
    
    # Get lineage
    lineage = lineage_tracker.get_data_lineage("cleaned_orders_table")
    print(f"\nData Lineage for cleaned_orders_table:")
    for entry in lineage:
        print(f"  {entry['source']} -> {entry['target']} via {entry['transformation']}")
    
    # Export lineage graph
    lineage_json = lineage_tracker.export_lineage_graph("json")
    print(f"\nLineage Graph (JSON):\n{lineage_json}")

---

## 📊 Monitoring & Observability {#monitoring}

### Data Pipeline Monitoring

```python
import logging
import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import boto3
import requests
from dataclasses import dataclass
from enum import Enum

class PipelineStatus(Enum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    WARNING = "WARNING"
    CANCELLED = "CANCELLED"

@dataclass
class PipelineMetrics:
    pipeline_name: str
    start_time: datetime
    end_time: Optional[datetime]
    status: PipelineStatus
    records_processed: int
    records_failed: int
    duration_seconds: float
    error_message: Optional[str] = None
    data_quality_score: float = 100.0
    resource_usage: Dict[str, float] = None

class DataPipelineMonitor:
    def __init__(self, metrics_backend="cloudwatch"):
        self.metrics_backend = metrics_backend
        self.logger = logging.getLogger(__name__)
        
        if metrics_backend == "cloudwatch":
            self.cloudwatch = boto3.client('cloudwatch')
        elif metrics_backend == "prometheus":
            self.prometheus_gateway = "http://localhost:9091"
        
        self.active_pipelines = {}
    
    def start_pipeline_monitoring(self, pipeline_name: str) -> str:
        """Start monitoring a pipeline execution"""
        run_id = f"{pipeline_name}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        
        metrics = PipelineMetrics(
            pipeline_name=pipeline_name,
            start_time=datetime.now(),
            end_time=None,
            status=PipelineStatus.RUNNING,
            records_processed=0,
            records_failed=0,
            duration_seconds=0.0
        )
        
        self.active_pipelines[run_id] = metrics
        
        # Send start metric
        self._send_metric(f"pipeline.started", 1, {
            "pipeline_name": pipeline_name,
            "run_id": run_id
        })
        
        self.logger.info(f"Started monitoring pipeline {pipeline_name} with run_id {run_id}")
        return run_id
    
    def update_pipeline_metrics(self, run_id: str, **kwargs):
        """Update pipeline metrics during execution"""
        if run_id not in self.active_pipelines:
            raise ValueError(f"Pipeline run_id {run_id} not found")
        
        metrics = self.active_pipelines[run_id]
        
        # Update metrics
        if 'records_processed' in kwargs:
            metrics.records_processed = kwargs['records_processed']
            self._send_metric(f"pipeline.records_processed", kwargs['records_processed'], {
                "pipeline_name": metrics.pipeline_name,
                "run_id": run_id
            })
        
        if 'records_failed' in kwargs:
            metrics.records_failed = kwargs['records_failed']
            self._send_metric(f"pipeline.records_failed", kwargs['records_failed'], {
                "pipeline_name": metrics.pipeline_name,
                "run_id": run_id
            })
        
        if 'data_quality_score' in kwargs:
            metrics.data_quality_score = kwargs['data_quality_score']
            self._send_metric(f"pipeline.data_quality_score", kwargs['data_quality_score'], {
                "pipeline_name": metrics.pipeline_name,
                "run_id": run_id
            })
        
        if 'status' in kwargs:
            metrics.status = kwargs['status']
    
    def finish_pipeline_monitoring(self, run_id: str, status: PipelineStatus, error_message: str = None):
        """Finish monitoring a pipeline execution"""
        if run_id not in self.active_pipelines:
            raise ValueError(f"Pipeline run_id {run_id} not found")
        
        metrics = self.active_pipelines[run_id]
        metrics.end_time = datetime.now()
        metrics.status = status
        metrics.duration_seconds = (metrics.end_time - metrics.start_time).total_seconds()
        metrics.error_message = error_message
        
        # Send completion metrics
        self._send_metric(f"pipeline.completed", 1, {
            "pipeline_name": metrics.pipeline_name,
            "run_id": run_id,
            "status": status.value
        })
        
        self._send_metric(f"pipeline.duration_seconds", metrics.duration_seconds, {
            "pipeline_name": metrics.pipeline_name,
            "run_id": run_id
        })
        
        # Calculate success rate
        if metrics.records_processed > 0:
            success_rate = ((metrics.records_processed - metrics.records_failed) / 
                          metrics.records_processed) * 100
            
            self._send_metric(f"pipeline.success_rate", success_rate, {
                "pipeline_name": metrics.pipeline_name,
                "run_id": run_id
            })
        
        # Log completion
        if status == PipelineStatus.SUCCESS:
            self.logger.info(f"Pipeline {metrics.pipeline_name} completed successfully. "
                           f"Processed {metrics.records_processed} records in "
                           f"{metrics.duration_seconds:.2f} seconds")
        else:
            self.logger.error(f"Pipeline {metrics.pipeline_name} failed. "
                            f"Error: {error_message}")
        
        # Store for historical analysis
        self._store_pipeline_metrics(metrics)
        
        return metrics
    
    def _send_metric(self, metric_name: str, value: float, dimensions: Dict[str, str]):
        """Send metric to monitoring backend"""
        
        if self.metrics_backend == "cloudwatch":
            try:
                self.cloudwatch.put_metric_data(
                    Namespace='DataPipeline',
                    MetricData=[
                        {
                            'MetricName': metric_name,
                            'Value': value,
                            'Unit': 'Count' if 'count' in metric_name.lower() else 'None',
                            'Dimensions': [
                                {
                                    'Name': key,
                                    'Value': str(val)
                                } for key, val in dimensions.items()
                            ],
                            'Timestamp': datetime.now()
                        }
                    ]
                )
            except Exception as e:
                self.logger.error(f"Failed to send metric to CloudWatch: {e}")
        
        elif self.metrics_backend == "prometheus":
            # Send to Prometheus Pushgateway
            try:
                metric_data = {
                    'metric_name': metric_name,
                    'value': value,
                    'labels': dimensions,
                    'timestamp': datetime.now().isoformat()
                }
                
                response = requests.post(
                    f"{self.prometheus_gateway}/metrics/job/data_pipeline",
                    json=metric_data,
                    timeout=5
                )
                response.raise_for_status()
                
            except Exception as e:
                self.logger.error(f"Failed to send metric to Prometheus: {e}")
    
    def _store_pipeline_metrics(self, metrics: PipelineMetrics):
        """Store pipeline metrics for historical analysis"""
        
        # Store in database or data warehouse
        metrics_dict = {
            'pipeline_name': metrics.pipeline_name,
            'start_time': metrics.start_time.isoformat(),
            'end_time': metrics.end_time.isoformat() if metrics.end_time else None,
            'status': metrics.status.value,
            'records_processed': metrics.records_processed,
            'records_failed': metrics.records_failed,
            'duration_seconds': metrics.duration_seconds,
            'data_quality_score': metrics.data_quality_score,
            'error_message': metrics.error_message
        }
        
        # This could be sent to a database, S3, etc.
        self.logger.info(f"Stored metrics: {json.dumps(metrics_dict, indent=2)}")
    
    def get_pipeline_health_status(self, pipeline_name: str, hours: int = 24) -> Dict[str, Any]:
        """Get health status for a pipeline over the last N hours"""
        
        # This would typically query your metrics backend
        # For demo purposes, we'll simulate the response
        
        health_status = {
            'pipeline_name': pipeline_name,
            'time_period_hours': hours,
            'total_runs': 12,
            'successful_runs': 10,
            'failed_runs': 2,
            'success_rate': 83.33,
            'avg_duration_seconds': 1850.5,
            'avg_records_processed': 45000,
            'avg_data_quality_score': 97.5,
            'last_run_status': 'SUCCESS',
            'last_run_time': (datetime.now() - timedelta(hours=2)).isoformat(),
            'alerts': [
                {
                    'severity': 'WARNING',
                    'message': 'Data quality score dropped below 95%',
                    'timestamp': (datetime.now() - timedelta(hours=6)).isoformat()
                }
            ]
        }
        
        return health_status
    
    def setup_alerts(self, pipeline_name: str, alert_config: Dict[str, Any]):
        """Setup alerts for pipeline monitoring"""
        
        alerts = {
            'pipeline_name': pipeline_name,
            'alert_rules': [
                {
                    'name': 'Pipeline Failure',
                    'condition': 'status == FAILED',
                    'severity': 'CRITICAL',
                    'notification_channels': ['email', 'slack']
                },
                {
                    'name': 'High Failure Rate',
                    'condition': 'failure_rate > 10%',
                    'severity': 'WARNING',
                    'notification_channels': ['slack']
                },
                {
                    'name': 'Low Data Quality',
                    'condition': 'data_quality_score < 95',
                    'severity': 'WARNING',
                    'notification_channels': ['email']
                },
                {
                    'name': 'Long Runtime',
                    'condition': 'duration > 3600 seconds',
                    'severity': 'WARNING',
                    'notification_channels': ['slack']
                }
            ]
        }
        
        # Store alert configuration
        self.logger.info(f"Configured alerts for {pipeline_name}: {json.dumps(alerts, indent=2)}")
        return alerts

# Data freshness monitoring
class DataFreshnessMonitor:
    def __init__(self):
        self.freshness_checks = {}
        self.logger = logging.getLogger(__name__)
    
    def register_data_source(self, source_name: str, expected_frequency_minutes: int):
        """Register a data source for freshness monitoring"""
        self.freshness_checks[source_name] = {
            'expected_frequency_minutes': expected_frequency_minutes,
            'last_update': None,
            'status': 'UNKNOWN'
        }
        
        self.logger.info(f"Registered data source {source_name} with expected frequency "
                        f"{expected_frequency_minutes} minutes")
    
    def update_data_timestamp(self, source_name: str, timestamp: datetime = None):
        """Update the last seen timestamp for a data source"""
        if source_name not in self.freshness_checks:
            raise ValueError(f"Data source {source_name} not registered")
        
        timestamp = timestamp or datetime.now()
        self.freshness_checks[source_name]['last_update'] = timestamp
        self.freshness_checks[source_name]['status'] = 'FRESH'
        
        self.logger.info(f"Updated timestamp for {source_name}: {timestamp}")
    
    def check_data_freshness(self) -> Dict[str, Any]:
        """Check freshness of all registered data sources"""
        current_time = datetime.now()
        freshness_report = {
            'check_time': current_time.isoformat(),
            'sources': {}
        }
        
        for source_name, config in self.freshness_checks.items():
            if config['last_update'] is None:
                status = 'NO_DATA'
                staleness_minutes = float('inf')
            else:
                staleness_minutes = (current_time - config['last_update']).total_seconds() / 60
                
                if staleness_minutes <= config['expected_frequency_minutes'] * 1.5:  # 50% tolerance
                    status = 'FRESH'
                elif staleness_minutes <= config['expected_frequency_minutes'] * 3:
                    status = 'STALE'
                else:
                    status = 'VERY_STALE'
            
            freshness_report['sources'][source_name] = {
                'status': status,
                'last_update': config['last_update'].isoformat() if config['last_update'] else None,
                'staleness_minutes': staleness_minutes if staleness_minutes != float('inf') else None,
                'expected_frequency_minutes': config['expected_frequency_minutes']
            }
            
            # Update status
            self.freshness_checks[source_name]['status'] = status
        
        return freshness_report

# Usage examples
if __name__ == "__main__":
    # Pipeline monitoring
    monitor = DataPipelineMonitor(metrics_backend="cloudwatch")
    
    # Start monitoring a pipeline
    run_id = monitor.start_pipeline_monitoring("daily_sales_etl")
    
    try:
        # Simulate pipeline execution
        for i in range(1, 6):
            time.sleep(1)  # Simulate work
            
            # Update metrics during execution
            monitor.update_pipeline_metrics(
                run_id,
                records_processed=i * 1000,
                records_failed=i * 2,
                data_quality_score=99.5 - (i * 0.1)
            )
        
        # Finish successfully
        monitor.finish_pipeline_monitoring(run_id, PipelineStatus.SUCCESS)
        
    except Exception as e:
        # Finish with failure
        monitor.finish_pipeline_monitoring(
            run_id, 
            PipelineStatus.FAILED, 
            error_message=str(e)
        )
    
    # Get health status
    health = monitor.get_pipeline_health_status("daily_sales_etl")
    print(f"Pipeline Health: {json.dumps(health, indent=2)}")
    
    # Setup alerts
    alert_config = {
        'email_recipients': ['data-team@company.com'],
        'slack_channel': '#data-alerts'
    }
    
    monitor.setup_alerts("daily_sales_etl", alert_config)
    
    # Data freshness monitoring
    freshness_monitor = DataFreshnessMonitor()
    
    # Register data sources
    freshness_monitor.register_data_source("sales_api", 60)  # Expected every hour
    freshness_monitor.register_data_source("user_events", 5)  # Expected every 5 minutes
    
    # Simulate data updates
    freshness_monitor.update_data_timestamp("sales_api", datetime.now() - timedelta(minutes=30))
    freshness_monitor.update_data_timestamp("user_events", datetime.now() - timedelta(minutes=10))
    
    # Check freshness
    freshness_report = freshness_monitor.check_data_freshness()
    print(f"\nData Freshness Report: {json.dumps(freshness_report, indent=2)}")
```

### Dashboard and Alerting

```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json

class DataPipelineDashboard:
    def __init__(self):
        self.metrics_data = []
        
    def generate_pipeline_metrics_dashboard(self, pipeline_metrics: List[PipelineMetrics]):
        """Generate comprehensive dashboard for pipeline metrics"""
        
        # Convert metrics to DataFrame
        df = pd.DataFrame([
            {
                'pipeline_name': m.pipeline_name,
                'start_time': m.start_time,
                'duration_seconds': m.duration_seconds,
                'records_processed': m.records_processed,
                'records_failed': m.records_failed,
                'success_rate': ((m.records_processed - m.records_failed) / m.records_processed * 100) if m.records_processed > 0 else 0,
                'data_quality_score': m.data_quality_score,
                'status': m.status.value
            }
            for m in pipeline_metrics
        ])
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=[
                'Pipeline Success Rate Over Time',
                'Processing Volume Trends',
                'Data Quality Score Trends',
                'Pipeline Duration Analysis',
                'Pipeline Status Distribution',
                'Error Rate Trends'
            ],
            specs=[
                [{"type": "scatter"}, {"type": "bar"}],
                [{"type": "scatter"}, {"type": "box"}],
                [{"type": "pie"}, {"type": "scatter"}]
            ]
        )
        
        # 1. Success Rate Over Time
        fig.add_trace(
            go.Scatter(
                x=df['start_time'],
                y=df['success_rate'],
                mode='lines+markers',
                name='Success Rate %',
                line=dict(color='green')
            ),
            row=1, col=1
        )
        
        # 2. Processing Volume
        volume_by_pipeline = df.groupby('pipeline_name')['records_processed'].sum().reset_index()
        fig.add_trace(
            go.Bar(
                x=volume_by_pipeline['pipeline_name'],
                y=volume_by_pipeline['records_processed'],
                name='Records Processed',
                marker_color='blue'
            ),
            row=1, col=2
        )
        
        # 3. Data Quality Score
        fig.add_trace(
            go.Scatter(
                x=df['start_time'],
                y=df['data_quality_score'],
                mode='lines+markers',
                name='Data Quality Score',
                line=dict(color='orange')
            ),
            row=2, col=1
        )
        
        # 4. Duration Analysis
        for pipeline in df['pipeline_name'].unique():
            pipeline_data = df[df['pipeline_name'] == pipeline]
            fig.add_trace(
                go.Box(
                    y=pipeline_data['duration_seconds'],
                    name=pipeline,
                    boxpoints='all'
                ),
                row=2, col=2
            )
        
        # 5. Status Distribution
        status_counts = df['status'].value_counts()
        fig.add_trace(
            go.Pie(
                labels=status_counts.index,
                values=status_counts.values,
                name="Status Distribution"
            ),
            row=3, col=1
        )
        
        # 6. Error Rate Trends
        df['error_rate'] = (df['records_failed'] / df['records_processed'] * 100).fillna(0)
        fig.add_trace(
            go.Scatter(
                x=df['start_time'],
                y=df['error_rate'],
                mode='lines+markers',
                name='Error Rate %',
                line=dict(color='red')
            ),
            row=3, col=2
        )
        
        # Update layout
        fig.update_layout(
            height=1200,
            title="Data Pipeline Monitoring Dashboard",
            showlegend=False
        )
        
        # Save dashboard
        fig.write_html("pipeline_dashboard.html")
        fig.show()
        
        return fig
    
    def create_sla_report(self, pipeline_metrics: List[PipelineMetrics], sla_config: Dict[str, Any]):
        """Generate SLA compliance report"""
        
        sla_report = {
            'report_date': datetime.now().isoformat(),
            'sla_config': sla_config,
            'pipeline_sla_status': {}
        }
        
        for pipeline_name in set(m.pipeline_name for m in pipeline_metrics):
            pipeline_data = [m for m in pipeline_metrics if m.pipeline_name == pipeline_name]
            
            # Calculate SLA metrics
            total_runs = len(pipeline_data)
            successful_runs = len([m for m in pipeline_data if m.status == PipelineStatus.SUCCESS])
            success_rate = (successful_runs / total_runs * 100) if total_runs > 0 else 0
            
            avg_duration = np.mean([m.duration_seconds for m in pipeline_data])
            avg_quality_score = np.mean([m.data_quality_score for m in pipeline_data])
            
            # Check SLA compliance
            sla_config_for_pipeline = sla_config.get(pipeline_name, sla_config.get('default', {}))
            
            sla_status = {
                'success_rate': {
                    'actual': success_rate,
                    'target': sla_config_for_pipeline.get('min_success_rate', 95),
                    'compliant': success_rate >= sla_config_for_pipeline.get('min_success_rate', 95)
                },
                'avg_duration': {
                    'actual': avg_duration,
                    'target': sla_config_for_pipeline.get('max_duration_seconds', 3600),
                    'compliant': avg_duration <= sla_config_for_pipeline.get('max_duration_seconds', 3600)
                },
                'data_quality': {
                    'actual': avg_quality_score,
                    'target': sla_config_for_pipeline.get('min_quality_score', 95),
                    'compliant': avg_quality_score >= sla_config_for_pipeline.get('min_quality_score', 95)
                }
            }
            
            # Overall compliance
            overall_compliant = all(metric['compliant'] for metric in sla_status.values())
            sla_status['overall_compliant'] = overall_compliant
            
            sla_report['pipeline_sla_status'][pipeline_name] = sla_status
        
        return sla_report

class AlertManager:
    def __init__(self):
        self.notification_channels = {
            'email': self._send_email_alert,
            'slack': self._send_slack_alert,
            'pagerduty': self._send_pagerduty_alert
        }
    
    def send_alert(self, alert_type: str, severity: str, message: str, channels: List[str]):
        """Send alert to specified channels"""
        
        alert_payload = {
            'alert_type': alert_type,
            'severity': severity,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        for channel in channels:
            if channel in self.notification_channels:
                try:
                    self.notification_channels[channel](alert_payload)
                except Exception as e:
                    print(f"Failed to send alert to {channel}: {e}")
            else:
                print(f"Unknown notification channel: {channel}")
    
    def _send_email_alert(self, alert_payload: Dict[str, Any]):
        """Send email alert"""
        
        # Email configuration (use environment variables in production)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "alerts@company.com"
        sender_password = "your-app-password"
        recipient_emails = ["data-team@company.com"]
        
        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(recipient_emails)
        message["Subject"] = f"Data Pipeline Alert - {alert_payload['severity']}"
        
        body = f"""
        Alert Type: {alert_payload['alert_type']}
        Severity: {alert_payload['severity']}
        Timestamp: {alert_payload['timestamp']}
        
        Message:
        {alert_payload['message']}
        """
        
        message.attach(MIMEText(body, "plain"))
        
        # Send email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_emails, text)
            server.quit()
            
            print(f"Email alert sent successfully")
            
        except Exception as e:
            print(f"Failed to send email: {e}")
    
    def _send_slack_alert(self, alert_payload: Dict[str, Any]):
        """Send Slack alert"""
        
        webhook_url = "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
        
        # Create Slack message
        color = {
            'CRITICAL': '#ff0000',
            'WARNING': '#ffaa00',
            'INFO': '#0066cc'
        }.get(alert_payload['severity'], '#666666')
        
        slack_message = {
            "attachments": [
                {
                    "color": color,
                    "title": f"Data Pipeline Alert - {alert_payload['severity']}",
                    "fields": [
                        {
                            "title": "Alert Type",
                            "value": alert_payload['alert_type'],
                            "short": True
                        },
                        {
                            "title": "Timestamp",
                            "value": alert_payload['timestamp'],
                            "short": True
                        },
                        {
                            "title": "Message",
                            "value": alert_payload['message'],
                            "short": False
                        }
                    ]
                }
            ]
        }
        
        try:
            response = requests.post(
                webhook_url,
                json=slack_message,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()
            
            print(f"Slack alert sent successfully")
            
        except Exception as e:
            print(f"Failed to send Slack alert: {e}")
    
    def _send_pagerduty_alert(self, alert_payload: Dict[str, Any]):
        """Send PagerDuty alert"""
        
        pagerduty_url = "https://events.pagerduty.com/v2/enqueue"
        integration_key = "your-pagerduty-integration-key"
        
        if alert_payload['severity'] != 'CRITICAL':
            return  # Only send critical alerts to PagerDuty
        
        pagerduty_payload = {
            "routing_key": integration_key,
            "event_action": "trigger",
            "payload": {
                "summary": f"Data Pipeline Alert: {alert_payload['alert_type']}",
                "source": "data-pipeline-monitor",
                "severity": alert_payload['severity'].lower(),
                "custom_details": {
                    "message": alert_payload['message'],
                    "timestamp": alert_payload['timestamp']
                }
            }
        }
        
        try:
            response = requests.post(
                pagerduty_url,
                json=pagerduty_payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()
            
            print(f"PagerDuty alert sent successfully")
            
        except Exception as e:
            print(f"Failed to send PagerDuty alert: {e}")

# Usage examples
if __name__ == "__main__":
    # Create sample metrics data
    sample_metrics = []
    
    for i in range(30):  # 30 days of data
        for pipeline in ['daily_etl', 'hourly_streaming', 'weekly_analytics']:
            metrics = PipelineMetrics(
                pipeline_name=pipeline,
                start_time=datetime.now() - timedelta(days=29-i, hours=np.random.randint(0, 24)),
                end_time=datetime.now() - timedelta(days=29-i, hours=np.random.randint(0, 24)),
                status=PipelineStatus.SUCCESS if np.random.random() > 0.1 else PipelineStatus.FAILED,
                records_processed=np.random.randint(10000, 100000),
                records_failed=np.random.randint(0, 1000),
                duration_seconds=np.random.uniform(300, 3600),
                data_quality_score=np.random.uniform(95, 100)
            )
            sample_metrics.append(metrics)
    
    # Generate dashboard
    dashboard = DataPipelineDashboard()
    fig = dashboard.generate_pipeline_metrics_dashboard(sample_metrics)
    
    # Generate SLA report
    sla_config = {
        'default': {
            'min_success_rate': 95,
            'max_duration_seconds': 3600,
            'min_quality_score': 95
        },
        'daily_etl': {
            'min_success_rate': 98,
            'max_duration_seconds': 1800,
            'min_quality_score': 98
        }
    }
    
    sla_report = dashboard.create_sla_report(sample_metrics, sla_config)
    print(f"SLA Report: {json.dumps(sla_report, indent=2)}")
    
    # Test alerting
    alert_manager = AlertManager()
    
    alert_manager.send_alert(
        alert_type="Pipeline Failure",
        severity="CRITICAL",
        message="The daily_etl pipeline failed with database connection error",
        channels=['email', 'slack', 'pagerduty']
    )
```

---

## 🔐 Data Security & Compliance {#security}

### Data Encryption and Security

```python
import hashlib
import hmac
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import boto3
from datetime import datetime, timedelta
import json
import logging
from typing import Dict, List, Any, Optional

class DataEncryptionManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def generate_encryption_key(self, password: str, salt: bytes = None) -> bytes:
        """Generate encryption key from password"""
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def encrypt_data(self, data: str, key: bytes) -> bytes:
        """Encrypt data using Fernet symmetric encryption"""
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data
    
    def decrypt_data(self, encrypted_data: bytes, key: bytes) -> str:
        """Decrypt data using Fernet symmetric encryption"""
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode()
    
    def encrypt_pii_fields(self, data: Dict[str, Any], pii_fields: List[str], key: bytes) -> Dict[str, Any]:
        """Encrypt specified PII fields in a dictionary"""
        encrypted_data = data.copy()
        
        for field in pii_fields:
            if field in encrypted_data:
                original_value = str(encrypted_data[field])
                encrypted_value = self.encrypt_data(original_value, key)
                encrypted_data[field] = base64.b64encode(encrypted_value).decode()
                encrypted_data[f"{field}_encrypted"] = True
        
        return encrypted_data
    
    def decrypt_pii_fields(self, data: Dict[str, Any], pii_fields: List[str], key: bytes) -> Dict[str, Any]:
        """Decrypt specified PII fields in a dictionary"""
        decrypted_data = data.copy()
        
        for field in pii_fields:
            if field in decrypted_data and decrypted_data.get(f"{field}_encrypted"):
                encrypted_value = base64.b64decode(decrypted_data[field])
                original_value = self.decrypt_data(encrypted_value, key)
                decrypted_data[field] = original_value
                decrypted_data.pop(f"{field}_encrypted", None)
        
        return decrypted_data

class DataMaskingManager:
    """Handle data masking for non-production environments"""
    
    def __init__(self):
        self.masking_rules = {}
    
    def add_masking_rule(self, field_name: str, masking_type: str, **kwargs):
        """Add masking rule for a field"""
        self.masking_rules[field_name] = {
            'type': masking_type,
            'options': kwargs
        }
    
    def mask_email(self, email: str) -> str:
        """Mask email address"""
        if '@' not in email:
            return email
        
        local, domain = email.split('@', 1)
        if len(local) <= 2:
            masked_local = local[0] + '*'
        else:
            masked_local = local[0] + '*' * (len(local) - 2) + local[-1]
        
        return f"{masked_local}@{domain}"
    
    def mask_phone(self, phone: str) -> str:
        """Mask phone number"""
        digits_only = ''.join(filter(str.isdigit, phone))
        if len(digits_only) >= 4:
            return phone[:-4] + '****'
        return '****'
    
    def mask_credit_card(self, cc_number: str) -> str:
        """Mask credit card number"""
        digits_only = ''.join(filter(str.isdigit, cc_number))
        if len(digits_only) >= 4:
            return '*' * (len(digits_only) - 4) + digits_only[-4:]
        return '****'
    
    def mask_ssn(self, ssn: str) -> str:
        """Mask Social Security Number"""
        digits_only = ''.join(filter(str.isdigit, ssn))
        if len(digits_only) == 9:
            return f"***-**-{digits_only[-4:]}"
        return "***-**-****"
    
    def randomize_date(self, date_str: str, days_variance: int = 30) -> str:
        """Randomize date within specified variance"""
        try:
            original_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            random_days = os.urandom(1)[0] % (days_variance * 2 + 1) - days_variance
            new_date = original_date + timedelta(days=random_days)
            return new_date.isoformat()
        except:
            return date_str
    
    def apply_masking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply masking rules to data"""
        masked_data = data.copy()
        
        for field_name, rule in self.masking_rules.items():
            if field_name in masked_data:
                original_value = masked_data[field_name]
                
                if rule['type'] == 'email':
                    masked_data[field_name] = self.mask_email(str(original_value))
                elif rule['type'] == 'phone':
                    masked_data[field_name] = self.mask_phone(str(original_value))
                elif rule['type'] == 'credit_card':
                    masked_data[field_name] = self.mask_credit_card(str(original_value))
                elif rule['type'] == 'ssn':
                    masked_data[field_name] = self.mask_ssn(str(original_value))
                elif rule['type'] == 'date_randomize':
                    days_variance = rule['options'].get('days_variance', 30)
                    masked_data[field_name] = self.randomize_date(str(original_value), days_variance)
                elif rule['type'] == 'hash':
                    salt = rule['options'].get('salt', 'default_salt')
                    masked_data[field_name] = hashlib.sha256(f"{salt}{original_value}".encode()).hexdigest()[:10]
        
        return masked_data

class DataAccessManager:
    """Manage data access controls and audit logging"""
    
    def __init__(self):
        self.access_policies = {}
        self.access_logs = []
        self.logger = logging.getLogger(__name__)
    
    def create_access_policy(self, policy_name: str, resources: List[str], 
                           actions: List[str], users: List[str], 
                           conditions: Dict[str, Any] = None):
        """Create data access policy"""
        policy = {
            'policy_name': policy_name,
            'resources': resources,  # Tables, datasets, etc.
            'actions': actions,      # read, write, delete, etc.
            'users': users,          # List of authorized users
            'conditions': conditions or {},  # Time-based, IP-based, etc.
            'created_at': datetime.now().isoformat()
        }
        
        self.access_policies[policy_name] = policy
        self.logger.info(f"Created access policy: {policy_name}")
        
        return policy
    
    def check_access(self, user: str, resource: str, action: str, 
                    context: Dict[str, Any] = None) -> bool:
        """Check if user has access to perform action on resource"""
        
        context = context or {}
        
        for policy_name, policy in self.access_policies.items():
            # Check if resource matches
            resource_match = any(
                resource.startswith(res) or res == '*' 
                for res in policy['resources']
            )
            
            # Check if action is allowed
            action_match = action in policy['actions'] or '*' in policy['actions']
            
            # Check if user is authorized
            user_match = user in policy['users'] or '*' in policy['users']
            
            if resource_match and action_match and user_match:
                # Check conditions
                if self._check_conditions(policy.get('conditions', {}), context):
                    self._log_access(user, resource, action, 'GRANTED', policy_name, context)
                    return True
        
        self._log_access(user, resource, action, 'DENIED', None, context)
        return False
    
    def _check_conditions(self, conditions: Dict[str, Any], context: Dict[str, Any]) -> bool:
        """Check if access conditions are met"""
        
        # Time-based conditions
        if 'time_range' in conditions:
            current_hour = datetime.now().hour
            start_hour, end_hour = conditions['time_range']
            if not (start_hour <= current_hour <= end_hour):
                return False
        
        # IP-based conditions
        if 'allowed_ips' in conditions:
            user_ip = context.get('ip_address')
            if user_ip not in conditions['allowed_ips']:
                return False
        
        # Role-based conditions
        if 'required_roles' in conditions:
            user_roles = context.get('user_roles', [])
            if not any(role in user_roles for role in conditions['required_roles']):
                return False
        
        return True
    
    def _log_access(self, user: str, resource: str, action: str, 
                   result: str, policy: str, context: Dict[str, Any]):
        """Log access attempt"""
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user': user,
            'resource': resource,
            'action': action,
            'result': result,
            'policy': policy,
            'context': context
        }
        
        self.access_logs.append(log_entry)
        
        # In production, send to centralized logging system
        self.logger.info(f"Access {result}: {user} -> {action} on {resource}")
    
    def get_access_report(self, start_date: str = None, end_date: str = None) -> Dict[str, Any]:
        """Generate access report"""
        
        if start_date:
            start_dt = datetime.fromisoformat(start_date)
            filtered_logs = [
                log for log in self.access_logs 
                if datetime.fromisoformat(log['timestamp']) >= start_dt
            ]
        else:
            filtered_logs = self.access_logs
        
        if end_date:
            end_dt = datetime.fromisoformat(end_date)
            filtered_logs = [
                log for log in filtered_logs 
                if datetime.fromisoformat(log['timestamp']) <= end_dt
            ]
        
        report = {
            'report_period': {
                'start_date': start_date,
                'end_date': end_date
            },
            'total_access_attempts': len(filtered_logs),
            'granted_access': len([log for log in filtered_logs if log['result'] == 'GRANTED']),
            'denied_access': len([log for log in filtered_logs if log['result'] == 'DENIED']),
            'unique_users': len(set(log['user'] for log in filtered_logs)),
            'most_accessed_resources': {},
            'user_activity': {},
            'access_patterns': []
        }
        
        # Most accessed resources
        resource_counts = {}
        for log in filtered_logs:
            resource = log['resource']
            resource_counts[resource] = resource_counts.get(resource, 0) + 1
        
        report['most_accessed_resources'] = dict(
            sorted(resource_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        
        # User activity
        user_activity = {}
        for log in filtered_logs:
            user = log['user']
            if user not in user_activity:
                user_activity[user] = {'granted': 0, 'denied': 0}
            user_activity[user][log['result'].lower()] += 1
        
        report['user_activity'] = user_activity
        
        return report

class GDPRComplianceManager:
    """Manage GDPR compliance requirements"""
    
    def __init__(self):
        self.data_subjects = {}  # Track data subjects and their data
        self.processing_activities = []
        self.consent_records = {}
        self.logger = logging.getLogger(__name__)
    
    def register_data_subject(self, subject_id: str, personal_data: Dict[str, Any]):
        """Register a data subject and their personal data"""
        self.data_subjects[subject_id] = {
            'personal_data': personal_data,
            'registered_at': datetime.now().isoformat(),
            'consent_given': False,
            'data_locations': []  # Track where their data is stored
        }
        
        self.logger.info(f"Registered data subject: {subject_id}")
    
    def record_consent(self, subject_id: str, purpose: str, consent_given: bool, 
                      consent_method: str = None):
        """Record consent for data processing"""
        if subject_id not in self.consent_records:
            self.consent_records[subject_id] = []
        
        consent_record = {
            'purpose': purpose,
            'consent_given': consent_given,
            'consent_method': consent_method,
            'timestamp': datetime.now().isoformat()
        }
        
        self.consent_records[subject_id].append(consent_record)
        
        if subject_id in self.data_subjects:
            self.data_subjects[subject_id]['consent_given'] = consent_given
        
        self.logger.info(f"Recorded consent for {subject_id}: {purpose} = {consent_given}")
    
    def handle_data_subject_request(self, subject_id: str, request_type: str) -> Dict[str, Any]:
        """Handle data subject rights requests (GDPR Article 15-22)"""
        
        if subject_id not in self.data_subjects:
            return {'error': 'Data subject not found', 'status': 'failed'}
        
        response = {
            'subject_id': subject_id,
            'request_type': request_type,
            'processed_at': datetime.now().isoformat(),
            'status': 'completed'
        }
        
        if request_type == 'access':  # Right to access (Article 15)
            response['personal_data'] = self.data_subjects[subject_id]['personal_data']
            response['consent_records'] = self.consent_records.get(subject_id, [])
            response['data_locations'] = self.data_subjects[subject_id]['data_locations']
            
        elif request_type == 'rectification':  # Right to rectification (Article 16)
            response['message'] = 'Data rectification process initiated'
            # In practice, you would update the data here
            
        elif request_type == 'erasure':  # Right to erasure (Article 17)
            # Remove personal data
            del self.data_subjects[subject_id]
            if subject_id in self.consent_records:
                del self.consent_records[subject_id]
            
            response['message'] = 'Personal data erased successfully'
            # In practice, you would delete from all systems
            
        elif request_type == 'portability':  # Right to data portability (Article 20)
            response['portable_data'] = self.data_subjects[subject_id]['personal_data']
            response['format'] = 'JSON'
            
        elif request_type == 'object':  # Right to object (Article 21)
            response['message'] = 'Processing objection recorded'
            # Stop processing for marketing, etc.
            
        elif request_type == 'restrict':  # Right to restrict processing (Article 18)
            response['message'] = 'Processing restriction applied'
            # Implement processing restrictions
        
        self.logger.info(f"Processed {request_type} request for {subject_id}")
        return response
    
    def generate_compliance_report(self) -> Dict[str, Any]:
        """Generate GDPR compliance report"""
        
        total_subjects = len(self.data_subjects)
        consented_subjects = len([
            s for s in self.data_subjects.values() 
            if s['consent_given']
        ])
        
        report = {
            'report_date': datetime.now().isoformat(),
            'total_data_subjects': total_subjects,
            'consented_subjects': consented_subjects,
            'consent_rate': (consented_subjects / total_subjects * 100) if total_subjects > 0 else 0,
            'total_consent_records': sum(len(records) for records in self.consent_records.values()),
            'data_retention_status': 'compliant',  # Would check actual retention
            'processing_lawfulness': 'consent',
            'recommendations': []
        }
        
        # Add recommendations based on analysis
        if report['consent_rate'] < 100:
            report['recommendations'].append(
                "Review consent collection process for unconsented subjects"
            )
        
        return report

# Usage examples
if __name__ == "__main__":
    # Data encryption
    encryption_manager = DataEncryptionManager()
    
    # Generate encryption key
    password = "secure_password_123"
    key = encryption_manager.generate_encryption_key(password)
    
    # Sample customer data with PII
    customer_data = {
        'customer_id': 'CUST001',
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '+1-555-0123',
        'ssn': '123-45-6789',
        'address': '123 Main St, Anytown, USA',
        'purchase_amount': 299.99
    }
    
    # Encrypt PII fields
    pii_fields = ['name', 'email', 'phone', 'ssn', 'address']
    encrypted_data = encryption_manager.encrypt_pii_fields(customer_data, pii_fields, key)
    print(f"Encrypted data: {json.dumps(encrypted_data, indent=2)}")
    
    # Data masking for non-production
    masking_manager = DataMaskingManager()
    masking_manager.add_masking_rule('email', 'email')
    masking_manager.add_masking_rule('phone', 'phone')
    masking_manager.add_masking_rule('ssn', 'ssn')
    
    masked_data = masking_manager.apply_masking(customer_data)
    print(f"\nMasked data: {json.dumps(masked_data, indent=2)}")
    
    # Access control
    access_manager = DataAccessManager()
    
    # Create access policies
    access_manager.create_access_policy(
        'data_analysts_policy',
        resources=['customer_data', 'sales_data'],
        actions=['read'],
        users=['analyst1@company.com', 'analyst2@company.com'],
        conditions={
            'time_range': (9, 17),  # 9 AM to 5 PM
            'required_roles': ['analyst', 'data_scientist']
        }
    )
    
    # Check access
    context = {
        'ip_address': '192.168.1.100',
        'user_roles': ['analyst']
    }
    
    access_granted = access_manager.check_access(
        'analyst1@company.com',
        'customer_data',
        'read',
        context
    )
    print(f"\nAccess granted: {access_granted}")
    
    # Generate access report
    access_report = access_manager.get_access_report()
    print(f"\nAccess report: {json.dumps(access_report, indent=2)}")
    
    # GDPR compliance
    gdpr_manager = GDPRComplianceManager()
    
    # Register data subject
    gdpr_manager.register_data_subject('john.doe@example.com', customer_data)
    
    # Record consent
    gdpr_manager.record_consent(
        'john.doe@example.com',
        'marketing_communications',
        True,
        'web_form'
    )
    
    # Handle data subject request
    access_request = gdpr_manager.handle_data_subject_request(
        'john.doe@example.com',
        'access'
    )
    print(f"\nGDPR access request response: {json.dumps(access_request, indent=2)}")
    
    # Generate compliance report
    compliance_report = gdpr_manager.generate_compliance_report()
    print(f"\nGDPR compliance report: {json.dumps(compliance_report, indent=2)}")
```

---

## 💡 Best Practices & Patterns {#best-practices}

### Data Engineering Design Patterns

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Callable
import pandas as pd
import logging
from datetime import datetime
import asyncio
from dataclasses import dataclass
from enum import Enum
import json

# 1. Strategy Pattern for Data Processing
class ProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

class BatchProcessingStrategy(ProcessingStrategy):
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process data in batches"""
        # Apply batch transformations
        data['processed_at'] = datetime.now()
        data['processing_type'] = 'batch'
        return data.groupby('customer_id').agg({
            'amount': 'sum',
            'quantity': 'sum',
            'processed_at': 'first',
            'processing_type': 'first'
        }).reset_index()

class StreamProcessingStrategy(ProcessingStrategy):
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process data as stream"""
        # Apply stream transformations
        data['processed_at'] = datetime.now()
        data['processing_type'] = 'stream'
        # Real-time aggregations
        return data

class RealTimeProcessingStrategy(ProcessingStrategy):
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process data in real-time"""
        data['processed_at'] = datetime.now()
        data['processing_type'] = 'realtime'
        # Apply real-time transformations
        data['alert_triggered'] = data['amount'] > 1000
        return data

class DataProcessor:
    def __init__(self, strategy: ProcessingStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: ProcessingStrategy):
        self._strategy = strategy
    
    def process_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return self._strategy.process(data)

# 2. Factory Pattern for Data Sources
class DataSourceType(Enum):
    DATABASE = "database"
    API = "api"
    FILE = "file"
    STREAM = "stream"

class DataSource(ABC):
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def validate_connection(self) -> bool:
        pass

class DatabaseSource(DataSource):
    def __init__(self, connection_string: str, query: str):
        self.connection_string = connection_string
        self.query = query
    
    def validate_connection(self) -> bool:
        # Validate database connection
        return True
    
    def extract(self) -> pd.DataFrame:
        # Extract data from database
        return pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})

class APISource(DataSource):
    def __init__(self, endpoint: str, headers: Dict[str, str]):
        self.endpoint = endpoint
        self.headers = headers
    
    def validate_connection(self) -> bool:
        # Validate API endpoint
        return True
    
    def extract(self) -> pd.DataFrame:
        # Extract data from API
        return pd.DataFrame({'api_data': ['a', 'b', 'c']})

class FileSource(DataSource):
    def __init__(self, file_path: str, file_format: str):
        self.file_path = file_path
        self.file_format = file_format
    
    def validate_connection(self) -> bool:
        # Validate file exists
        return True
    
    def extract(self) -> pd.DataFrame:
        # Extract data from file
        return pd.DataFrame({'file_data': [1, 2, 3]})

class DataSourceFactory:
    @staticmethod
    def create_source(source_type: DataSourceType, **kwargs) -> DataSource:
        if source_type == DataSourceType.DATABASE:
            return DatabaseSource(
                kwargs.get('connection_string'),
                kwargs.get('query')
            )
        elif source_type == DataSourceType.API:
            return APISource(
                kwargs.get('endpoint'),
                kwargs.get('headers', {})
            )
        elif source_type == DataSourceType.FILE:
            return FileSource(
                kwargs.get('file_path'),
                kwargs.get('file_format', 'csv')
            )
        else:
            raise ValueError(f"Unknown source type: {source_type}")

# 3. Observer Pattern for Data Quality Monitoring
class DataQualityObserver(ABC):
    @abstractmethod
    def notify(self, data: pd.DataFrame, quality_metrics: Dict[str, Any]):
        pass

class EmailAlertObserver(DataQualityObserver):
    def notify(self, data: pd.DataFrame, quality_metrics: Dict[str, Any]):
        if quality_metrics['quality_score'] < 95:
            print(f"EMAIL ALERT: Data quality score is {quality_metrics['quality_score']}")

class MetricsLogger(DataQualityObserver):
    def notify(self, data: pd.DataFrame, quality_metrics: Dict[str, Any]):
        logging.info(f"Data Quality Metrics: {quality_metrics}")

class DataQualitySubject:
    def __init__(self):
        self._observers: List[DataQualityObserver] = []
    
    def attach(self, observer: DataQualityObserver):
        self._observers.append(observer)
    
    def detach(self, observer: DataQualityObserver):
        self._observers.remove(observer)
    
    def notify_observers(self, data: pd.DataFrame, quality_metrics: Dict[str, Any]):
        for observer in self._observers:
            observer.notify(data, quality_metrics)
    
    def check_quality(self, data: pd.DataFrame):
        # Calculate quality metrics
        quality_metrics = {
            'total_records': len(data),
            'null_count': data.isnull().sum().sum(),
            'duplicate_count': data.duplicated().sum(),
            'quality_score': 100 - (data.isnull().sum().sum() / len(data) * 100)
        }
        
        self.notify_observers(data, quality_metrics)
        return quality_metrics

# 4. Command Pattern for Pipeline Operations
class PipelineCommand(ABC):
    @abstractmethod
    def execute(self) -> Any:
        pass
    
    @abstractmethod
    def undo(self) -> Any:
        pass

class ExtractCommand(PipelineCommand):
    def __init__(self, source: DataSource):
        self.source = source
        self.extracted_data = None
    
    def execute(self) -> pd.DataFrame:
        self.extracted_data = self.source.extract()
        print(f"Extracted {len(self.extracted_data)} records")
        return self.extracted_data
    
    def undo(self):
        self.extracted_data = None
        print("Extract operation undone")

class TransformCommand(PipelineCommand):
    def __init__(self, data: pd.DataFrame, transformation_func: Callable):
        self.data = data
        self.transformation_func = transformation_func
        self.original_data = data.copy()
        self.transformed_data = None
    
    def execute(self) -> pd.DataFrame:
        self.transformed_data = self.transformation_func(self.data)
        print(f"Transformed data: {len(self.transformed_data)} records")
        return self.transformed_data
    
    def undo(self) -> pd.DataFrame:
        self.transformed_data = None
        print("Transform operation undone")
        return self.original_data

class LoadCommand(PipelineCommand):
    def __init__(self, data: pd.DataFrame, destination: str):
        self.data = data
        self.destination = destination
        self.loaded = False
    
    def execute(self):
        # Simulate loading data
        print(f"Loaded {len(self.data)} records to {self.destination}")
        self.loaded = True
    
    def undo(self):
        if self.loaded:
            print(f"Removed data from {self.destination}")
            self.loaded = False

class PipelineInvoker:
    def __init__(self):
        self.commands: List[PipelineCommand] = []
        self.executed_commands: List[PipelineCommand] = []
    
    def add_command(self, command: PipelineCommand):
        self.commands.append(command)
    
    def execute_pipeline(self):
        results = []
        for command in self.commands:
            try:
                result = command.execute()
                self.executed_commands.append(command)
                results.append(result)
            except Exception as e:
                print(f"Pipeline execution failed at {command.__class__.__name__}: {e}")
                self.rollback()
                raise
        return results
    
    def rollback(self):
        print("Rolling back pipeline...")
        for command in reversed(self.executed_commands):
            command.undo()
        self.executed_commands.clear()

# 5. Builder Pattern for Complex Pipelines
class PipelineBuilder:
    def __init__(self):
        self.source = None
        self.transformations = []
        self.destination = None
        self.quality_checks = []
        self.error_handling = None
    
    def with_source(self, source: DataSource):
        self.source = source
        return self
    
    def add_transformation(self, transformation: Callable):
        self.transformations.append(transformation)
        return self
    
    def with_destination(self, destination: str):
        self.destination = destination
        return self
    
    def add_quality_check(self, check: Callable):
        self.quality_checks.append(check)
        return self
    
    def with_error_handling(self, handler: Callable):
        self.error_handling = handler
        return self
    
    def build(self):
        return DataPipeline(
            source=self.source,
            transformations=self.transformations,
            destination=self.destination,
            quality_checks=self.quality_checks,
            error_handler=self.error_handling
        )

class DataPipeline:
    def __init__(self, source: DataSource, transformations: List[Callable],
                 destination: str, quality_checks: List[Callable],
                 error_handler: Callable = None):
        self.source = source
        self.transformations = transformations
        self.destination = destination
        self.quality_checks = quality_checks
        self.error_handler = error_handler
    
    def run(self):
        try:
            # Extract
            data = self.source.extract()
            
            # Transform
            for transformation in self.transformations:
                data = transformation(data)
            
            # Quality checks
            for check in self.quality_checks:
                if not check(data):
                    raise ValueError("Data quality check failed")
            
            # Load
            print(f"Loading {len(data)} records to {self.destination}")
            
            return data
            
        except Exception as e:
            if self.error_handler:
                self.error_handler(e)
            else:
                raise

# 6. Singleton Pattern for Configuration Management
class DataPipelineConfig:
    _instance = None
    _config = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_config(self, key: str, value: Any):
        self._config[key] = value
    
    def get_config(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)
    
    def load_from_file(self, config_file: str):
        # Load configuration from file
        self._config.update({
            'database_url': 'postgresql://localhost:5432/data',
            'max_batch_size': 10000,
            'retry_attempts': 3,
            'notification_email': 'data-team@company.com'
        })
```

### Performance Optimization Patterns

```python
import time
import functools
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading
import queue
import asyncio
from typing import Callable, Any, List
import pandas as pd
import numpy as np

# 1. Caching Pattern
class DataCache:
    def __init__(self, max_size: int = 1000, ttl_seconds: int = 3600):
        self.cache = {}
        self.access_times = {}
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        self.lock = threading.Lock()
    
    def get(self, key: str) -> Any:
        with self.lock:
            if key in self.cache:
                # Check TTL
                if time.time() - self.access_times[key] < self.ttl_seconds:
                    self.access_times[key] = time.time()  # Update access time
                    return self.cache[key]
                else:
                    # Expired
                    del self.cache[key]
                    del self.access_times[key]
            return None
    
    def put(self, key: str, value: Any):
        with self.lock:
            # Evict oldest if cache is full
            if len(self.cache) >= self.max_size:
                oldest_key = min(self.access_times, key=self.access_times.get)
                del self.cache[oldest_key]
                del self.access_times[oldest_key]
            
            self.cache[key] = value
            self.access_times[key] = time.time()

def cached(cache: DataCache):
    """Decorator for caching function results"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            key = f"{func.__name__}_{hash(str(args) + str(kwargs))}"
            
            # Try to get from cache
            result = cache.get(key)
            if result is not None:
                print(f"Cache hit for {func.__name__}")
                return result
            
            # Compute result
            print(f"Computing {func.__name__}")
            result = func(*args, **kwargs)
            
            # Store in cache
            cache.put(key, result)
            
            return result
        return wrapper
    return decorator

# 2. Connection Pooling Pattern
class ConnectionPool:
    def __init__(self, connection_factory: Callable, pool_size: int = 10):
        self.connection_factory = connection_factory
        self.pool = queue.Queue(maxsize=pool_size)
        self.active_connections = set()
        
        # Pre-populate pool
        for _ in range(pool_size):
            conn = self.connection_factory()
            self.pool.put(conn)
    
    def get_connection(self):
        """Get connection from pool"""
        try:
            conn = self.pool.get(timeout=30)  # 30 second timeout
            self.active_connections.add(conn)
            return conn
        except queue.Empty:
            raise Exception("Connection pool exhausted")
    
    def return_connection(self, conn):
        """Return connection to pool"""
        if conn in self.active_connections:
            self.active_connections.remove(conn)
            self.pool.put(conn)
    
    def close_all(self):
        """Close all connections"""
        while not self.pool.empty():
            conn = self.pool.get()
            if hasattr(conn, 'close'):
                conn.close()

# 3. Parallel Processing Pattern
class ParallelProcessor:
    def __init__(self, n_workers: int = None):
        self.n_workers = n_workers or mp.cpu_count()
    
    def process_chunks_multiprocessing(self, data: pd.DataFrame, 
                                     process_func: Callable, 
                                     chunk_size: int = 10000) -> pd.DataFrame:
        """Process data chunks using multiprocessing"""
        
        # Split data into chunks
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        
        # Process chunks in parallel
        with ProcessPoolExecutor(max_workers=self.n_workers) as executor:
            results = list(executor.map(process_func, chunks))
        
        # Combine results
        return pd.concat(results, ignore_index=True)
    
    def process_chunks_threading(self, data: List[Any], 
                               process_func: Callable) -> List[Any]:
        """Process data using threading (I/O bound tasks)"""
        
        with ThreadPoolExecutor(max_workers=self.n_workers) as executor:
            results = list(executor.map(process_func, data))
        
        return results
    
    async def process_chunks_async(self, data: List[Any], 
                                 async_process_func: Callable) -> List[Any]:
        """Process data using async/await"""
        
        semaphore = asyncio.Semaphore(self.n_workers)
        
        async def process_with_semaphore(item):
            async with semaphore:
                return await async_process_func(item)
        
        tasks = [process_with_semaphore(item) for item in data]
        results = await asyncio.gather(*tasks)
        
        return results

# 4. Circuit Breaker Pattern for Resilience
class CircuitBreakerState:
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, 
                 recovery_timeout: int = 60,
                 expected_exception: type = Exception):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitBreakerState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs) -> Any:
        if self.state == CircuitBreakerState.OPEN:
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = CircuitBreakerState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except self.expected_exception as e:
            self.on_failure()
            raise e
    
    def on_success(self):
        self.failure_count = 0
        self.state = CircuitBreakerState.CLOSED
    
    def on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitBreakerState.OPEN

# 5. Batch Processing Pattern
class BatchProcessor:
    def __init__(self, batch_size: int = 1000, max_wait_time: int = 30):
        self.batch_size = batch_size
        self.max_wait_time = max_wait_time
        self.batch = []
        self.last_batch_time = time.time()
    
    def add_item(self, item: Any, process_func: Callable = None):
        self.batch.append(item)
        
        # Process if batch is full or max wait time exceeded
        if (len(self.batch) >= self.batch_size or 
            time.time() - self.last_batch_time > self.max_wait_time):
            self.process_batch(process_func)
    
    def process_batch(self, process_func: Callable = None):
        if self.batch:
            if process_func:
                process_func(self.batch)
            else:
                print(f"Processing batch of {len(self.batch)} items")
            
            self.batch.clear()
            self.last_batch_time = time.time()

# Usage examples
if __name__ == "__main__":
    # Example usage of design patterns
    
    # 1. Strategy Pattern
    print("1. Strategy Pattern Example:")
    sample_data = pd.DataFrame({
        'customer_id': [1, 2, 3, 1, 2],
        'amount': [100, 200, 300, 150, 250],
        'quantity': [1, 2, 3, 1, 2]
    })
    
    processor = DataProcessor(BatchProcessingStrategy())
    batch_result = processor.process_data(sample_data)
    print(f"Batch processing result:\n{batch_result}")
    
    processor.set_strategy(StreamProcessingStrategy())
    stream_result = processor.process_data(sample_data)
    print(f"Stream processing result:\n{stream_result}")
    
    # 2. Factory Pattern
    print("\n2. Factory Pattern Example:")
    db_source = DataSourceFactory.create_source(
        DataSourceType.DATABASE,
        connection_string="postgresql://localhost/db",
        query="SELECT * FROM users"
    )
    
    api_source = DataSourceFactory.create_source(
        DataSourceType.API,
        endpoint="https://api.example.com/data",
        headers={"Authorization": "Bearer token"}
    )
    
    print(f"Created database source: {type(db_source).__name__}")
    print(f"Created API source: {type(api_source).__name__}")
    
    # 3. Observer Pattern
    print("\n3. Observer Pattern Example:")
    quality_subject = DataQualitySubject()
    quality_subject.attach(EmailAlertObserver())
    quality_subject.attach(MetricsLogger())
    
    # Add some null values to trigger quality alerts
    sample_data_with_nulls = sample_data.copy()
    sample_data_with_nulls.loc[0, 'amount'] = None
    sample_data_with_nulls.loc[1, 'customer_id'] = None
    
    quality_metrics = quality_subject.check_quality(sample_data_with_nulls)
    
    # 4. Command Pattern
    print("\n4. Command Pattern Example:")
    invoker = PipelineInvoker()
    
    # Add commands
    extract_cmd = ExtractCommand(db_source)
    transform_cmd = TransformCommand(
        sample_data, 
        lambda df: df.groupby('customer_id').sum().reset_index()
    )
    load_cmd = LoadCommand(sample_data, "warehouse_table")
    
    invoker.add_command(extract_cmd)
    invoker.add_command(transform_cmd)
    invoker.add_command(load_cmd)
    
    # Execute pipeline
    try:
        results = invoker.execute_pipeline()
        print("Pipeline executed successfully")
    except Exception as e:
        print(f"Pipeline failed: {e}")
    
    # 5. Builder Pattern
    print("\n5. Builder Pattern Example:")
    
    def sample_transformation(df):
        df['transformed'] = df['amount'] * 2
        return df
    
    def quality_check(df):
        return len(df) > 0 and df['amount'].notna().all()
    
    pipeline = (PipelineBuilder()
                .with_source(db_source)
                .add_transformation(sample_transformation)
                .add_quality_check(quality_check)
                .with_destination("output_table")
                .with_error_handling(lambda e: print(f"Error handled: {e}"))
                .build())
    
    try:
        result = pipeline.run()
        print("Builder pattern pipeline executed successfully")
    except Exception as e:
        print(f"Builder pattern pipeline failed: {e}")
    
    # 6. Performance Patterns
    print("\n6. Performance Patterns Example:")
    
    # Caching
    cache = DataCache(max_size=100, ttl_seconds=60)
    
    @cached(cache)
    def expensive_calculation(n):
        time.sleep(1)  # Simulate expensive operation
        return n * n
    
    # First call - computed
    result1 = expensive_calculation(5)
    
    # Second call - cached
    result2 = expensive_calculation(5)
    
    # Parallel processing
    def process_chunk(chunk):
        return chunk ** 2
    
    large_array = np.random.randint(0, 100, 10000)
    chunks = np.array_split(large_array, 4)
    
    processor = ParallelProcessor(n_workers=4)
    
    # Process with threading (simulated I/O bound)
    results = processor.process_chunks_threading(
        chunks, 
        lambda chunk: np.sum(chunk ** 2)
    )
    
    print(f"Parallel processing results: {results}")
    
    # Circuit breaker
    def unreliable_service():
        if np.random.random() < 0.7:  # 70% failure rate
            raise Exception("Service temporarily unavailable")
        return "Success!"
    
    circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=5)
    
    for i in range(10):
        try:
            result = circuit_breaker.call(unreliable_service)
            print(f"Call {i}: {result}")
        except Exception as e:
            print(f"Call {i}: Failed - {e}")
        time.sleep(1)

---

## 🎯 Real-World Projects {#projects}

### Project 1: E-commerce Analytics Platform

**Overview**: Build a complete data pipeline for e-commerce analytics with real-time dashboards.

**Architecture**:
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Website   │───▶│   Kafka     │───▶│   Spark     │───▶│ Data Lake   │
│   Events    │    │  Streams    │    │ Processing  │    │   (S3)      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                 │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────▼──────┐
│  Dashboard  │◄───│ Redshift    │◄───│   Airflow   │    │  Raw Data   │
│  (Tableau)  │    │Data Warehouse│    │ Scheduler   │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Implementation**:

```python
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import boto3
import pandas as pd
from sqlalchemy import create_engine
import requests
import json

# Define the DAG
default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'ecommerce_analytics_pipeline',
    default_args=default_args,
    description='Complete e-commerce analytics pipeline',
    schedule_interval=timedelta(hours=1),
    catchup=False,
    tags=['ecommerce', 'analytics', 'production']
)

def extract_user_events(**context):
    """Extract user events from various sources"""
    s3_client = boto3.client('s3')
    
    # Extract from web analytics API
    events_data = []
    
    # Simulate extracting from Google Analytics API
    ga_events = extract_google_analytics_data()
    events_data.extend(ga_events)
    
    # Extract from application database
    db_events = extract_database_events()
    events_data.extend(db_events)
    
    # Extract from mobile app events
    mobile_events = extract_mobile_events()
    events_data.extend(mobile_events)
    
    # Save to S3
    df = pd.DataFrame(events_data)
    
    execution_date = context['execution_date']
    s3_key = f"raw-events/date={execution_date.date()}/events.parquet"
    
    # Upload to S3
    parquet_buffer = df.to_parquet(index=False)
    s3_client.put_object(
        Bucket='ecommerce-data-lake',
        Key=s3_key,
        Body=parquet_buffer
    )
    
    return s3_key

def extract_google_analytics_data():
    """Extract data from Google Analytics API"""
    # Simulate Google Analytics API call
    return [
        {
            'event_type': 'page_view',
            'user_id': f'user_{i}',
            'page_url': f'/product/{i % 100}',
            'timestamp': datetime.now() - timedelta(hours=i),
            'session_id': f'session_{i // 10}',
            'source': 'google_analytics'
        }
        for i in range(1000)
    ]

def extract_database_events():
    """Extract events from application database"""
    engine = create_engine('postgresql://user:pass@localhost:5432/ecommerce')
    
    query = """
    SELECT 
        event_id,
        user_id,
        event_type,
        product_id,
        amount,
        timestamp,
        'database' as source
    FROM user_events 
    WHERE timestamp >= NOW() - INTERVAL '1 hour'
    """
    
    df = pd.read_sql(query, engine)
    return df.to_dict('records')

def extract_mobile_events():
    """Extract events from mobile analytics"""
    # Simulate mobile analytics API
    return [
        {
            'event_type': 'app_open',
            'user_id': f'mobile_user_{i}',
            'device_type': 'mobile',
            'timestamp': datetime.now() - timedelta(minutes=i),
            'source': 'mobile_app'
        }
        for i in range(500)
    ]

def transform_and_enrich_data(**context):
    """Transform and enrich the raw event data"""
    s3_client = boto3.client('s3')
    
    # Get the S3 key from previous task
    s3_key = context['task_instance'].xcom_pull(task_ids='extract_events')
    
    # Read data from S3
    response = s3_client.get_object(Bucket='ecommerce-data-lake', Key=s3_key)
    df = pd.read_parquet(response['Body'])
    
    # Data transformations
    df = transform_events_data(df)
    
    # Enrich with user data
    df = enrich_with_user_data(df)
    
    # Enrich with product data  
    df = enrich_with_product_data(df)
    
    # Calculate derived metrics
    df = calculate_derived_metrics(df)
    
    # Save transformed data
    execution_date = context['execution_date']
    transformed_key = f"transformed-events/date={execution_date.date()}/enriched_events.parquet"
    
    parquet_buffer = df.to_parquet(index=False)
    s3_client.put_object(
        Bucket='ecommerce-data-lake',
        Key=transformed_key,
        Body=parquet_buffer
    )
    
    return transformed_key

def transform_events_data(df):
    """Apply data transformations"""
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Extract time components
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6])
    
    # Clean and standardize data
    df['event_type'] = df['event_type'].str.lower().str.strip()
    df['user_id'] = df['user_id'].str.strip()
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['user_id', 'timestamp', 'event_type'])
    
    return df

def enrich_with_user_data(df):
    """Enrich events with user demographic data"""
    # Simulate user data lookup
    user_data = {
        f'user_{i}': {
            'age_group': '25-34' if i % 3 == 0 else '35-44',
            'country': 'US' if i % 2 == 0 else 'UK',
            'customer_segment': 'Premium' if i % 4 == 0 else 'Standard'
        }
        for i in range(1000)
    }
    
    # Merge with events
    df['age_group'] = df['user_id'].map(lambda x: user_data.get(x, {}).get('age_group', 'Unknown'))
    df['country'] = df['user_id'].map(lambda x: user_data.get(x, {}).get('country', 'Unknown'))
    df['customer_segment'] = df['user_id'].map(lambda x: user_data.get(x, {}).get('customer_segment', 'Standard'))
    
    return df

def enrich_with_product_data(df):
    """Enrich events with product information"""
    # For events that have product_id, add product details
    product_data = {
        f'product_{i}': {
            'category': 'Electronics' if i % 3 == 0 else 'Clothing',
            'price': round(20 + (i % 100) * 5, 2),
            'brand': f'Brand_{i % 10}'
        }
        for i in range(100)
    }
    
    df['product_category'] = df['product_id'].map(lambda x: product_data.get(str(x), {}).get('category') if pd.notna(x) else None)
    df['product_price'] = df['product_id'].map(lambda x: product_data.get(str(x), {}).get('price') if pd.notna(x) else None)
    df['product_brand'] = df['product_id'].map(lambda x: product_data.get(str(x), {}).get('brand') if pd.notna(x) else None)
    
    return df

def calculate_derived_metrics(df):
    """Calculate business metrics"""
    # Session-level metrics
    session_metrics = df.groupby('session_id').agg({
        'timestamp': ['min', 'max', 'count'],
        'event_type': lambda x: x.nunique()
    }).reset_index()
    
    session_metrics.columns = ['session_id', 'session_start', 'session_end', 'event_count', 'unique_event_types']
    session_metrics['session_duration_minutes'] = (
        (session_metrics['session_end'] - session_metrics['session_start']).dt.total_seconds() / 60
    )
    
    # Merge back to events
    df = df.merge(session_metrics, on='session_id', how='left')
    
    # User journey metrics
    df = df.sort_values(['user_id', 'timestamp'])
    df['event_sequence'] = df.groupby('user_id').cumcount() + 1
    df['time_since_last_event'] = df.groupby('user_id')['timestamp'].diff().dt.total_seconds()
    
    return df

def load_to_data_warehouse(**context):
    """Load transformed data to Redshift data warehouse"""
    s3_client = boto3.client('s3')
    
    # Get transformed data key
    transformed_key = context['task_instance'].xcom_pull(task_ids='transform_data')
    
    # Read transformed data
    response = s3_client.get_object(Bucket='ecommerce-data-lake', Key=transformed_key)
    df = pd.read_parquet(response['Body'])
    
    # Load to Redshift
    engine = create_engine('redshift+psycopg2://user:pass@cluster.redshift.amazonaws.com:5439/analytics')
    
    # Create fact table if not exists
    create_fact_table_sql = """
    CREATE TABLE IF NOT EXISTS fact_user_events (
        event_id VARCHAR(50),
        user_id VARCHAR(50),
        session_id VARCHAR(50),
        event_type VARCHAR(50),
        product_id VARCHAR(50),
        timestamp TIMESTAMP,
        hour INTEGER,
        day_of_week INTEGER,
        is_weekend BOOLEAN,
        age_group VARCHAR(20),
        country VARCHAR(10),
        customer_segment VARCHAR(20),
        product_category VARCHAR(50),
        product_price DECIMAL(10,2),
        session_duration_minutes DECIMAL(10,2),
        event_sequence INTEGER
    )
    DISTSTYLE KEY
    DISTKEY (user_id)
    SORTKEY (timestamp);
    """
    
    with engine.connect() as conn:
        conn.execute(create_fact_table_sql)
    
    # Insert data
    df.to_sql(
        'fact_user_events',
        engine,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=1000
    )
    
    print(f"Loaded {len(df)} events to data warehouse")

def create_aggregated_tables(**context):
    """Create aggregated tables for faster analytics"""
    engine = create_engine('redshift+psycopg2://user:pass@cluster.redshift.amazonaws.com:5439/analytics')
    
    # Daily aggregations
    daily_aggregation_sql = """
    CREATE TABLE IF NOT EXISTS daily_user_metrics AS
    SELECT 
        DATE(timestamp) as event_date,
        user_id,
        customer_segment,
        country,
        COUNT(*) as total_events,
        COUNT(DISTINCT session_id) as sessions,
        SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) as purchases,
        AVG(session_duration_minutes) as avg_session_duration
    FROM fact_user_events
    WHERE DATE(timestamp) = CURRENT_DATE - 1
    GROUP BY 1, 2, 3, 4;
    """
    
    # Product performance aggregation
    product_performance_sql = """
    CREATE TABLE IF NOT EXISTS daily_product_metrics AS
    SELECT 
        DATE(timestamp) as event_date,
        product_category,
        product_brand,
        COUNT(*) as total_interactions,
        COUNT(DISTINCT user_id) as unique_users,
        SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) as purchases,
        AVG(product_price) as avg_price
    FROM fact_user_events
    WHERE product_id IS NOT NULL 
    AND DATE(timestamp) = CURRENT_DATE - 1
    GROUP BY 1, 2, 3;
    """
    
    with engine.connect() as conn:
        conn.execute(daily_aggregation_sql)
        conn.execute(product_performance_sql)
    
    print("Created aggregated tables")

# Define tasks
extract_task = PythonOperator(
    task_id='extract_events',
    python_callable=extract_user_events,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_and_enrich_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_to_warehouse',
    python_callable=load_to_data_warehouse,
    dag=dag
)

aggregate_task = PythonOperator(
    task_id='create_aggregations',
    python_callable=create_aggregated_tables,
    dag=dag
)

# Data quality check
quality_check_sql = """
SELECT 
    COUNT(*) as total_events,
    COUNT(DISTINCT user_id) as unique_users,
    COUNT(DISTINCT session_id) as unique_sessions,
    MIN(timestamp) as earliest_event,
    MAX(timestamp) as latest_event
FROM fact_user_events
WHERE DATE(timestamp) = CURRENT_DATE - 1;
"""

quality_check_task = BashOperator(
    task_id='data_quality_check',
    bash_command=f'psql -h cluster.redshift.amazonaws.com -d analytics -c "{quality_check_sql}"',
    dag=dag
)

# Define dependencies
extract_task >> transform_task >> load_task >> aggregate_task >> quality_check_task
```

### Project 2: Real-Time Fraud Detection System

**Overview**: Build a real-time fraud detection system using streaming data.

**Architecture**:
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Transaction │───▶│   Kafka     │───▶│   Flink     │───▶│  Alerts     │
│   Events    │    │   Topic     │    │  Processor  │    │ Service     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                    ┌─────────────┐
                                    │  Features   │
                                    │   Store     │
                                    └─────────────┘
```

**Implementation**:

```python
from kafka import KafkaProducer, KafkaConsumer
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any
import redis
import logging
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

class FraudDetectionEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
        # Load pre-trained model
        self.fraud_model = joblib.load('fraud_detection_model.pkl')
        self.scaler = joblib.load('feature_scaler.pkl')
        
    def extract_features(self, transaction: Dict[str, Any]) -> Dict[str, float]:
        """Extract features for fraud detection"""
        user_id = transaction['user_id']
        amount = transaction['amount']
        merchant_id = transaction['merchant_id']
        timestamp = datetime.fromisoformat(transaction['timestamp'])
        
        features = {}
        
        # Transaction amount features
        features['amount'] = amount
        features['amount_log'] = np.log1p(amount)
        
        # Time-based features
        features['hour'] = timestamp.hour
        features['day_of_week'] = timestamp.weekday()
        features['is_weekend'] = timestamp.weekday() >= 5
        features['is_night'] = timestamp.hour < 6 or timestamp.hour > 22
        
        # User historical features (from Redis cache)
        user_features = self.get_user_features(user_id, timestamp)
        features.update(user_features)
        
        # Merchant features
        merchant_features = self.get_merchant_features(merchant_id, timestamp)
        features.update(merchant_features)
        
        # Velocity features
        velocity_features = self.calculate_velocity_features(user_id, timestamp, amount)
        features.update(velocity_features)
        
        return features
    
    def get_user_features(self, user_id: str, timestamp: datetime) -> Dict[str, float]:
        """Get user historical features from cache"""
        features = {}
        
        # Get user transaction history from Redis
        user_key = f"user:{user_id}:transactions"
        recent_transactions = self.redis_client.lrange(user_key, 0, 99)  # Last 100 transactions
        
        if recent_transactions:
            amounts = []
            merchants = set()
            
            for txn_json in recent_transactions:
                txn = json.loads(txn_json)
                txn_time = datetime.fromisoformat(txn['timestamp'])
                
                # Only consider recent transactions
                if (timestamp - txn_time).days <= 30:
                    amounts.append(txn['amount'])
                    merchants.add(txn['merchant_id'])
            
            if amounts:
                features['user_avg_amount'] = np.mean(amounts)
                features['user_std_amount'] = np.std(amounts)
                features['user_max_amount'] = np.max(amounts)
                features['user_transaction_count'] = len(amounts)
                features['user_unique_merchants'] = len(merchants)
            else:
                features.update({
                    'user_avg_amount': 0,
                    'user_std_amount': 0,
                    'user_max_amount': 0,
                    'user_transaction_count': 0,
                    'user_unique_merchants': 0
                })
        else:
            # New user
            features.update({
                'user_avg_amount': 0,
                'user_std_amount': 0,
                'user_max_amount': 0,
                'user_transaction_count': 0,
                'user_unique_merchants': 0,
                'is_new_user': 1
            })
        
        return features
    
    def get_merchant_features(self, merchant_id: str, timestamp: datetime) -> Dict[str, float]:
        """Get merchant features"""
        features = {}
        
        merchant_key = f"merchant:{merchant_id}:stats"
        merchant_stats = self.redis_client.hgetall(merchant_key)
        
        if merchant_stats:
            features['merchant_avg_amount'] = float(merchant_stats.get(b'avg_amount', 0))
            features['merchant_fraud_rate'] = float(merchant_stats.get(b'fraud_rate', 0))
            features['merchant_transaction_count'] = int(merchant_stats.get(b'transaction_count', 0))
        else:
            features.update({
                'merchant_avg_amount': 0,
                'merchant_fraud_rate': 0,
                'merchant_transaction_count': 0,
                'is_new_merchant': 1
            })
        
        return features
    
    def calculate_velocity_features(self, user_id: str, timestamp: datetime, amount: float) -> Dict[str, float]:
        """Calculate velocity-based features"""
        features = {}
        
        # Check transactions in different time windows
        windows = [
            ('1h', timedelta(hours=1)),
            ('24h', timedelta(hours=24)),
            ('7d', timedelta(days=7))
        ]
        
        for window_name, window_duration in windows:
            window_key = f"user:{user_id}:velocity:{window_name}"
            window_start = timestamp - window_duration
            
            # Get transactions in this window
            transactions = []
            for txn_json in self.redis_client.lrange(f"user:{user_id}:transactions", 0, -1):
                txn = json.loads(txn_json)
                txn_time = datetime.fromisoformat(txn['timestamp'])
                
                if window_start <= txn_time <= timestamp:
                    transactions.append(txn)
            
            # Calculate velocity features
            features[f'velocity_count_{window_name}'] = len(transactions)
            features[f'velocity_amount_{window_name}'] = sum(txn['amount'] for txn in transactions)
            
            if transactions:
                features[f'velocity_avg_amount_{window_name}'] = features[f'velocity_amount_{window_name}'] / len(transactions)
            else:
                features[f'velocity_avg_amount_{window_name}'] = 0
        
        return features
    
    def predict_fraud(self, features: Dict[str, float]) -> Dict[str, Any]:
        """Predict if transaction is fraudulent"""
        
        # Prepare feature vector
        feature_names = [
            'amount', 'amount_log', 'hour', 'day_of_week', 'is_weekend', 'is_night',
            'user_avg_amount', 'user_std_amount', 'user_max_amount', 'user_transaction_count',
            'user_unique_merchants', 'merchant_avg_amount', 'merchant_fraud_rate',
            'velocity_count_1h', 'velocity_amount_1h', 'velocity_count_24h', 'velocity_amount_24h'
        ]
        
        feature_vector = [features.get(name, 0) for name in feature_names]
        feature_vector = np.array(feature_vector).reshape(1, -1)
        
        # Scale features
        feature_vector_scaled = self.scaler.transform(feature_vector)
        
        # Predict
        fraud_score = self.fraud_model.decision_function(feature_vector_scaled)[0]
        is_fraud = self.fraud_model.predict(feature_vector_scaled)[0] == -1
        
        # Convert score to probability-like value (0-100)
        fraud_probability = max(0, min(100, (1 - fraud_score) * 50))
        
        return {
            'is_fraud': bool(is_fraud),
            'fraud_score': float(fraud_score),
            'fraud_probability': float(fraud_probability),
            'risk_level': self.categorize_risk(fraud_probability)
        }
    
    def categorize_risk(self, probability: float) -> str:
        """Categorize risk level based on probability"""
        if probability >= 80:
            return 'HIGH'
        elif probability >= 60:
            return 'MEDIUM'
        elif probability >= 40:
            return 'LOW'
        else:
            return 'VERY_LOW'
    
    def update_user_history(self, transaction: Dict[str, Any]):
        """Update user transaction history in Redis"""
        user_id = transaction['user_id']
        user_key = f"user:{user_id}:transactions"
        
        # Add new transaction to history
        self.redis_client.lpush(user_key, json.dumps(transaction))
        
        # Keep only last 100 transactions
        self.redis_client.ltrim(user_key, 0, 99)
        
        # Set expiration (30 days)
        self.redis_client.expire(user_key, 30 * 24 * 3600)
    
    def send_alert(self, transaction: Dict[str, Any], prediction: Dict[str, Any]):
        """Send fraud alert"""
        alert = {
            'alert_type': 'fraud_detection',
            'transaction_id': transaction['transaction_id'],
            'user_id': transaction['user_id'],
            'amount': transaction['amount'],
            'merchant_id': transaction['merchant_id'],
            'prediction': prediction,
            'timestamp': datetime.now().isoformat(),
            'severity': prediction['risk_level']
        }
        
        # Send to alerts topic
        self.producer.send('fraud-alerts', value=alert)
        
        self.logger.warning(f"Fraud alert sent for transaction {transaction['transaction_id']}: "
                          f"Risk {prediction['risk_level']} ({prediction['fraud_probability']:.1f}%)")
    
    def process_transaction(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single transaction for fraud detection"""
        
        # Extract features
        features = self.extract_features(transaction)
        
        # Predict fraud
        prediction = self.predict_fraud(features)
        
        # Update user history
        self.update_user_history(transaction)
        
        # Send alert if high risk
        if prediction['risk_level'] in ['HIGH', 'MEDIUM']:
            self.send_alert(transaction, prediction)
        
        # Return result
        result = {
            'transaction_id': transaction['transaction_id'],
            'processed_at': datetime.now().isoformat(),
            'prediction': prediction,
            'features': features
        }
        
        return result

class FraudDetectionConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'transactions',
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='fraud-detection-group'
        )
        self.fraud_engine = FraudDetectionEngine()
        self.logger = logging.getLogger(__name__)
    
    def run(self):
        """Run the fraud detection consumer"""
        self.logger.info("Starting fraud detection consumer...")
        
        try:
            for message in self.consumer:
                transaction = message.value
                
                try:
                    result = self.fraud_engine.process_transaction(transaction)
                    
                    # Log result
                    self.logger.info(f"Processed transaction {result['transaction_id']}: "
                                   f"Fraud probability {result['prediction']['fraud_probability']:.1f}%")
                    
                except Exception as e:
                    self.logger.error(f"Error processing transaction {transaction.get('transaction_id', 'unknown')}: {e}")
                    
        except KeyboardInterrupt:
            self.logger.info("Shutting down fraud detection consumer...")
        finally:
            self.consumer.close()

# Model training script
def train_fraud_model():
    """Train the fraud detection model"""
    
    # Load historical transaction data
    # This would typically come from your data warehouse
    df = pd.read_csv('historical_transactions.csv')
    
    # Feature engineering
    features = []
    labels = []
    
    for _, row in df.iterrows():
        # Extract features (same as in real-time processing)
        feature_dict = extract_historical_features(row)
        feature_vector = [feature_dict.get(name, 0) for name in feature_names]
        
        features.append(feature_vector)
        labels.append(row['is_fraud'])
    
    X = np.array(features)
    y = np.array(labels)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train model (using Isolation Forest for anomaly detection)
    model = IsolationForest(
        contamination=0.1,  # Assume 10% fraud rate
        random_state=42,
        n_estimators=100
    )
    
    model.fit(X_scaled[y == 0])  # Train on non-fraud transactions only
    
    # Save model and scaler
    joblib.dump(model, 'fraud_detection_model.pkl')
    joblib.dump(scaler, 'feature_scaler.pkl')
    
    print("Fraud detection model trained and saved")

if __name__ == "__main__":
    # Run fraud detection consumer
    consumer = FraudDetectionConsumer()
    consumer.run()
```

### Project 3: Data Lake Implementation on AWS

**Overview**: Build a serverless data lake using AWS services.

**Architecture**:
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Data       │───▶│     S3      │───▶│   Lambda    │───▶│    Glue     │
│ Sources     │    │ Data Lake   │    │  Trigger    │    │  Catalog    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                 │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────▼──────┐
│   Athena    │◄───│  QuickSight │◄───│   Redshift  │◄───│    ETL      │
│  Queries    │    │ Dashboard   │    │ Spectrum    │    │   Jobs      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

**Implementation**:

```python
import boto3
import json
import pandas as pd
from datetime import datetime
import logging
from typing import Dict, List, Any
import os

class AWSDataLake:
    def __init__(self, region='us-east-1'):
        self.region = region
        self.s3_client = boto3.client('s3', region_name=region)
        self.glue_client = boto3.client('glue', region_name=region)
        self.athena_client = boto3.client('athena', region_name=region)
        self.lambda_client = boto3.client('lambda', region_name=region)
        
        self.logger = logging.getLogger(__name__)
        
        # Configuration
        self.data_lake_bucket = 'my-company-data-lake'
        self.glue_database = 'data_lake_db'
        self.athena_output_bucket = 'my-company-athena-results'
    
    def setup_data_lake_infrastructure(self):
        """Set up the complete data lake infrastructure"""
        
        # Create S3 buckets
        self.create_s3_buckets()
        
        # Create Glue database
        self.create_glue_database()
        
        # Deploy Lambda functions
        self.deploy_lambda_functions()
        
        # Create Glue jobs
        self.create_glue_jobs()
        
        # Set up Athena workgroup
        self.create_athena_workgroup()
        
        self.logger.info("Data lake infrastructure setup complete")
    
    def create_s3_buckets(self):
        """Create S3 buckets for data lake"""
        buckets = [
            self.data_lake_bucket,
            self.athena_output_bucket,
            f'{self.data_lake_bucket}-logs'
        ]
        
        for bucket in buckets:
            try:
                self.s3_client.create_bucket(Bucket=bucket)
                
                # Enable versioning
                self.s3_client.put_bucket_versioning(
                    Bucket=bucket,
                    VersioningConfiguration={'Status': 'Enabled'}
                )
                
                # Set lifecycle policy
                lifecycle_config = {
                    'Rules': [
                        {
                            'ID': 'transition-to-ia',
                            'Status': 'Enabled',
                            'Filter': {'Prefix': 'raw-data/'},
                            'Transitions': [
                                {
                                    'Days': 30,
                                    'StorageClass': 'STANDARD_IA'
                                },
                                {
                                    'Days': 90,
                                    'StorageClass': 'GLACIER'
                                },
                                {
                                    'Days': 365,
                                    'StorageClass': 'DEEP_ARCHIVE'
                                }
                            ]
                        }
                    ]
                }
                
                self.s3_client.put_bucket_lifecycle_configuration(
                    Bucket=bucket,
                    LifecycleConfiguration=lifecycle_config
                )
                
                self.logger.info(f"Created S3 bucket: {bucket}")
                
            except Exception as e:
                if 'BucketAlreadyExists' not in str(e):
                    self.logger.error(f"Error creating bucket {bucket}: {e}")
    
    def create_glue_database(self):
        """Create Glue database for data catalog"""
        try:
            self.glue_client.create_database(
                DatabaseInput={
                    'Name': self.glue_database,
                    'Description': 'Data Lake catalog database'
                }
            )
            self.logger.info(f"Created Glue database: {self.glue_database}")
        except Exception as e:
            if 'AlreadyExistsException' not in str(e):
                self.logger.error(f"Error creating Glue database: {e}")
    
    def deploy_lambda_functions(self):
        """Deploy Lambda functions for data processing"""
        
        # S3 event processor Lambda
        lambda_code = self.create_s3_processor_lambda_code()
        
        function_name = 'data-lake-s3-processor'
        
        try:
            self.lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.9',
                Role='arn:aws:iam::ACCOUNT:role/lambda-execution-role',  # Replace with actual role ARN
                Handler='lambda_function.lambda_handler',
                Code={'ZipFile': lambda_code},
                Description='Process S3 events for data lake',
                Timeout=300,
                MemorySize=512,
                Environment={
                    'Variables': {
                        'GLUE_DATABASE': self.glue_database,
                        'DATA_LAKE_BUCKET': self.data_lake_bucket
                    }
                }
            )
            
            # Add S3 trigger
            self.s3_client.put_bucket_notification_configuration(
                Bucket=self.data_lake_bucket,
                NotificationConfiguration={
                    'LambdaConfigurations': [
                        {
                            'Id': 'data-lake-processor',
                            'LambdaFunctionArn': f'arn:aws:lambda:{self.region}:ACCOUNT:function:{function_name}',
                            'Events': ['s3:ObjectCreated:*'],
                            'Filter': {
                                'Key': {
                                    'FilterRules': [
                                        {
                                            'Name': 'prefix',
                                            'Value': 'raw-data/'
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            )
            
            self.logger.info(f"Created Lambda function: {function_name}")
            
        except Exception as e:
            self.logger.error(f"Error creating Lambda function: {e}")
    
    def create_s3_processor_lambda_code(self) -> bytes:
        """Create Lambda function code for S3 event processing"""
        code = '''
import boto3
import json
import urllib.parse
import os

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    glue_client = boto3.client('glue')
    
    glue_database = os.environ['GLUE_DATABASE']
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
        print(f"Processing file: s3://{bucket}/{key}")
        
        # Trigger Glue crawler based on file type
        if key.endswith('.csv'):
            table_name = key.split('/')[-2]  # Use directory name as table name
            
            # Create Glue table
            create_glue_table(glue_client, glue_database, table_name, bucket, key)
            
        # Trigger ETL job if needed
        if 'raw-data' in key:
            trigger_etl_job(glue_client, key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed S3 events')
    }

def create_glue_table(glue_client, database, table_name, bucket, key):
    try:
        glue_client.create_table(
            DatabaseName=database,
            TableInput={
                'Name': table_name,
                'StorageDescriptor': {
                    'Columns': [
                        {'Name': 'col1', 'Type': 'string'},
                        {'Name': 'col2', 'Type': 'string'}
                    ],
                    'Location': f's3://{bucket}/{"/".join(key.split("/")[:-1])}/',
                    'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
                    'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
                    'SerdeInfo': {
                        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                        'Parameters': {
                            'field.delim': ',',
                            'skip.header.line.count': '1'
                        }
                    }
                }
            }
        )
    except Exception as e:
        print(f"Error creating Glue table: {e}")

def trigger_etl_job(glue_client, s3_key):
    try:
        glue_client.start_job_run(
            JobName='data-lake-etl-job',
            Arguments={
                '--input_path': s3_key
            }
        )
    except Exception as e:
        print(f"Error triggering ETL job: {e}")
'''
        return code.encode('utf-8')
    
    def create_glue_jobs(self):
        """Create Glue ETL jobs"""
        
        job_script = '''
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_path'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [args['input_path']]
    },
    format="csv",
    format_options={
        "withHeader": True
    }
)

# Transform data
# Add your transformation logic here
transformed_df = df.apply_mapping([
    ("old_column", "string", "new_column", "string")
])

# Write to S3 in Parquet format
glueContext.write_dynamic_frame.from_options(
    frame=transformed_df,
    connection_type="s3",
    connection_options={
        "path": "s3://my-company-data-lake/processed-data/"
    },
    format="glueparquet"
)

job.commit()
'''
        
        try:
            self.glue_client.create_job(
                Name='data-lake-etl-job',
                Role='arn:aws:iam::ACCOUNT:role/glue-execution-role',  # Replace with actual role ARN
                Command={
                    'Name': 'glueetl',
                    'ScriptLocation': f's3://{self.data_lake_bucket}/scripts/etl_job.py',
                    'PythonVersion': '3'
                },
                DefaultArguments={
                    '--job-bookmark-option': 'job-bookmark-enable'
                },
                MaxRetries=1,
                Timeout=60,
                GlueVersion='3.0'
            )
            
            # Upload script to S3
            self.s3_client.put_object(
                Bucket=self.data_lake_bucket,
                Key='scripts/etl_job.py',
                Body=job_script
            )
            
            self.logger.info("Created Glue ETL job")
            
        except Exception as e:
            self.logger.error(f"Error creating Glue job: {e}")
    
    def create_athena_workgroup(self):
        """Create Athena workgroup for queries"""
        try:
            self.athena_client.create_work_group(
                Name='data-lake-workgroup',
                Description='Workgroup for data lake queries',
                Configuration={
                    'ResultConfigurationUpdates': {
                        'OutputLocation': f's3://{self.athena_output_bucket}/query-results/',
                        'EncryptionConfiguration': {
                            'EncryptionOption': 'SSE_S3'
                        }
                    },
                    'EnforceWorkGroupConfiguration': True
                }
            )
            self.logger.info("Created Athena workgroup")
        except Exception as e:
            if 'WorkGroupAlreadyExistsException' not in str(e):
                self.logger.error(f"Error creating Athena workgroup: {e}")
    
    def query_data_lake(self, query: str) -> List[Dict[str, Any]]:
        """Query data lake using Athena"""
        
        # Start query execution
        response = self.athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': self.glue_database
            },
            ResultConfiguration={
                'OutputLocation': f's3://{self.athena_output_bucket}/query-results/'
            },
            WorkGroup='data-lake-workgroup'
        )
        
        query_execution_id = response['QueryExecutionId']
        
        # Wait for query to complete
        while True:
            result = self.athena_client.get_query_execution(
                QueryExecutionId=query_execution_id
            )
            
            status = result['QueryExecution']['Status']['State']
            
            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                break
            
            time.sleep(1)
        
        if status != 'SUCCEEDED':
            raise Exception(f"Query failed with status: {status}")
        
        # Get query results
        results = self.athena_client.get_query_results(
            QueryExecutionId=query_execution_id
        )
        
        # Parse results
        rows = []
        columns = [col['Label'] for col in results['ResultSet']['ResultSetMetadata']['ColumnInfo']]
        
        for row in results['ResultSet']['Rows'][1:]:  # Skip header
            values = [col.get('VarCharValue', '') for col in row['Data']]
            rows.append(dict(zip(columns, values)))
        
        return rows
    
    def upload_data_to_lake(self, data: pd.DataFrame, table_name: str, partition_columns: List[str] = None):
        """Upload data to data lake with partitioning"""
        
        if partition_columns:
            # Create partitioned structure
            for partition_values, group_df in data.groupby(partition_columns):
                if not isinstance(partition_values, tuple):
                    partition_values = (partition_values,)
                
                # Create partition path
                partition_path = '/'.join([
                    f"{col}={val}" for col, val in zip(partition_columns, partition_values)
                ])
                
                # Save to S3
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
                s3_key = f"raw-data/{table_name}/{partition_path}/data_{timestamp}.parquet"
                
                parquet_buffer = group_df.drop(columns=partition_columns).to_parquet(index=False)
                
                self.s3_client.put_object(
                    Bucket=self.data_lake_bucket,
                    Key=s3_key,
                    Body=parquet_buffer
                )
        else:
            # Save without partitioning
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            s3_key = f"raw-data/{table_name}/data_{timestamp}.parquet"
            
            parquet_buffer = data.to_parquet(index=False)
            
            self.s3_client.put_object(
                Bucket=self.data_lake_bucket,
                Key=s3_key,
                Body=parquet_buffer
            )
        
        self.logger.info(f"Uploaded data to data lake: {table_name}")

# Usage example
if __name__ == "__main__":
    # Initialize data lake
    data_lake = AWSDataLake()
    
    # Set up infrastructure
    data_lake.setup_data_lake_infrastructure()
    
    # Upload sample data
    sample_data = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5],
        'product_id': [101, 102, 103, 104, 105],
        'amount': [100.0, 200.0, 150.0, 300.0, 75.0],
        'order_date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03'],
        'region': ['US', 'US', 'EU', 'EU', 'US']
    })
    
    # Upload with partitioning
    data_lake.upload_data_to_lake(
        sample_data, 
        'sales_data', 
        partition_columns=['order_date', 'region']
    )
    
    # Query data
    query = """
    SELECT region, SUM(amount) as total_sales
    FROM sales_data
    WHERE order_date >= '2024-01-01'
    GROUP BY region
    ORDER BY total_sales DESC
    """
    
    results = data_lake.query_data_lake(query)
    print(f"Query results: {results}")
```

---

## 🎓 Career Path & Skills {#career}

### Data Engineer Career Roadmap

**Entry Level (0-2 years)**
```
┌─────────────────────────────────────────────────────────┐
│                 Junior Data Engineer                    │
├─────────────────────────────────────────────────────────┤
│ Skills to Develop:                                      │
│ • SQL (Advanced)                                        │
│ • Python/Java basics                                    │
│ • ETL concepts                                          │
│ • Database fundamentals                                 │
│ • Basic cloud knowledge (AWS/GCP/Azure)               │
│ • Git version control                                   │
│ • Basic data modeling                                   │
│                                                         │
│ Typical Responsibilities:                               │
│ • Data extraction and basic transformations            │
│ • Writing SQL queries                                   │
│ • Data quality checks                                   │
│ • Documentation                                         │
│ • Supporting senior engineers                           │
│                                                         │
│ Salary Range: $60,000 - $85,000                        │
└─────────────────────────────────────────────────────────┘
```

**Mid Level (2-5 years)**
```
┌─────────────────────────────────────────────────────────┐
│                   Data Engineer                         │
├─────────────────────────────────────────────────────────┤
│ Skills to Master:                                       │
│ • Advanced Python/Scala/Java                          │
│ • Apache Spark                                          │
│ • Data warehouse design                                 │
│ • Cloud platforms (1-2 specializations)               │
│ • Workflow orchestration (Airflow)                     │
│ • Big data technologies (Kafka, Hadoop)               │
│ • Data security and governance                          │
│ • Performance optimization                              │
│                                                         │
│ Typical Responsibilities:                               │
│ • Design and build data pipelines                      │
│ • Data architecture decisions                           │
│ • Performance tuning                                    │
│ • Mentoring junior engineers                           │
│ • Cross-functional collaboration                        │
│                                                         │
│ Salary Range: $85,000 - $130,000                       │
└─────────────────────────────────────────────────────────┘
```

**Senior Level (5-8 years)**
```
┌─────────────────────────────────────────────────────────┐
│              Senior Data Engineer                       │
├─────────────────────────────────────────────────────────┤
│ Skills to Excel:                                        │
│ • System architecture design                            │
│ • Multiple cloud platforms                              │
│ • Advanced distributed systems                          │
│ • DataOps and MLOps                                     │
│ • Team leadership                                       │
│ • Business acumen                                       │
│ • Advanced security and compliance                      │
│ • Cost optimization                                     │
│                                                         │
│ Typical Responsibilities:                               │
│ • Lead complex data projects                           │
│ • Architecture design and reviews                       │
│ • Technical strategy development                        │
│ • Team coordination                                     │
│ • Stakeholder management                                │
│                                                         │
│ Salary Range: $130,000 - $180,000                      │
└─────────────────────────────────────────────────────────┘
```

**Expert Level (8+ years)**
```
┌─────────────────────────────────────────────────────────┐
│         Principal Data Engineer / Architect             │
├─────────────────────────────────────────────────────────┤
│ Skills to Lead:                                         │
│ • Enterprise architecture                               │
│ • Strategic technology planning                         │
│ • Advanced team management                              │
│ • Innovation and R&D                                    │
│ • Industry expertise                                    │
│ • Thought leadership                                    │
│ • Budget and resource management                        │
│ • Vendor relationships                                  │
│                                                         │
│ Typical Responsibilities:                               │
│ • Company-wide data strategy                           │
│ • Technology evaluation and selection                   │
│ • Team building and hiring                             │
│ • External representation (conferences, etc.)          │
│ • Innovation projects                                   │
│                                                         │
│ Salary Range: $180,000 - $300,000+                     │
└─────────────────────────────────────────────────────────┘
```

### Essential Skills Matrix

**Technical Skills**:

| Skill Category | Beginner | Intermediate | Advanced | Expert |
|----------------|----------|--------------|----------|--------|
| **SQL** | Basic queries, joins | Window functions, CTEs | Query optimization, complex analytics | Database tuning, advanced analytics |
| **Python** | Basic syntax, pandas | APIs, data processing | Advanced libraries, optimization | Framework development |
| **Cloud Platforms** | Basic services | Core data services | Multi-service architectures | Enterprise solutions |
| **Big Data** | Concepts understanding | Spark basics | Distributed processing | Architecture design |
| **Data Modeling** | Basic concepts | Star/snowflake schema | Advanced modeling | Enterprise data architecture |
| **DevOps** | Git basics | CI/CD pipelines | Infrastructure as code | Advanced automation |

**Soft Skills**:
- **Communication**: Explain technical concepts to non-technical stakeholders
- **Problem Solving**: Debug complex data issues and design solutions
- **Project Management**: Plan and execute data projects
- **Business Acumen**: Understand business requirements and translate to technical solutions
- **Collaboration**: Work effectively with data scientists, analysts, and engineers
- **Continuous Learning**: Stay updated with rapidly evolving technology landscape

### Certification Paths

**AWS Data Engineering**:
1. AWS Cloud Practitioner (foundational)
2. AWS Solutions Architect Associate
3. AWS Data Analytics Specialty
4. AWS Machine Learning Specialty

**Google Cloud Platform**:
1. Google Cloud Associate Cloud Engineer
2. Professional Data Engineer
3. Professional Cloud Architect
4. Professional Machine Learning Engineer

**Microsoft Azure**:
1. Azure Fundamentals
2. Azure Data Engineer Associate
3. Azure Solutions Architect Expert
4. Azure Data Scientist Associate

**Technology-Specific**:
- Databricks Certified Data Engineer
- Confluent Certified Developer for Apache Kafka
- Snowflake SnowPro Core Certification
- Cloudera Data Platform Generalist

### Building a Portfolio

**Essential Projects to Showcase**:

1. **End-to-End ETL Pipeline**
   - Data extraction from multiple sources
   - Transformation and cleansing
   - Loading to data warehouse
   - Monitoring and alerting

2. **Real-Time Data Processing**
   - Streaming data ingestion
   - Real-time analytics
   - Dashboard integration

3. **Data Lake Implementation**
   - Raw data storage
   - Data cataloging
   - Query optimization
   - Cost management

4. **ML Pipeline for Analytics**
   - Feature engineering pipeline
   - Model training automation
   - Model deployment
   - Performance monitoring

5. **Data Quality Framework**
   - Automated data validation
   - Quality metrics tracking
   - Issue detection and alerting
   - Data lineage tracking

### Interview Preparation

**Technical Interview Topics**:

1. **System Design Questions**:
   - Design a data pipeline for processing millions of events per day
   - Design a data warehouse for a retail company
   - Design a real-time recommendation system
   - Design a data lake architecture

2. **Coding Questions**:
   - SQL optimization problems
   - Python data processing challenges
   - Algorithm and data structure problems
   - Distributed systems concepts

3. **Scenario-Based Questions**:
   - How would you handle data quality issues?
   - How would you optimize a slow-running pipeline?
   - How would you ensure data security and compliance?
   - How would you design for scalability?

**Sample Interview Questions**:

**Beginner Level**:
- Explain the difference between OLTP and OLAP systems
- How would you handle duplicate records in a dataset?
- What is the difference between a data lake and data warehouse?
- Write a SQL query to find the second-highest salary

**Intermediate Level**:
- Design a data pipeline to process customer clickstream data
- How would you implement slowly changing dimensions (SCD)?
- Explain the CAP theorem and its implications for data systems
- How would you optimize a Spark job that's running slowly?

**Advanced Level**:
- Design a multi-petabyte data lake architecture
- How would you implement GDPR compliance in a data pipeline?
- Explain different consistency models in distributed systems
- Design a system to handle both batch and stream processing

### Networking and Community

**Professional Communities**:
- **Data Engineering Weekly** - Newsletter and community
- **dbt Community** - Modern data stack discussions
- **Apache Foundation** - Open source big data projects
- **Local Meetups** - Data engineering and analytics groups
- **Conferences** - Strata, DataEngConf, Modern Data Stack Conference

**Online Learning Resources**:
- **Courses**: DataCamp, Coursera, Udacity, Pluralsight
- **Books**: 
  - "Designing Data-Intensive Applications" by Martin Kleppmann
  - "The Data Warehouse Toolkit" by Ralph Kimball
  - "Stream Processing with Apache Kafka" by Guido Schmutz
- **YouTube Channels**: Data Engineering channels, conference talks
- **Blogs**: Engineering blogs from Netflix, Uber, Airbnb, Spotify

---

## 🏆 Conclusion & Next Steps

Congratulations! You've completed the comprehensive Data Engineering Zero to Hero guide. You now have the knowledge and tools to:

### ✅ What You've Learned

**Fundamentals**:
- ✅ Data engineering lifecycle and core concepts
- ✅ Programming languages (Python, SQL, Bash)
- ✅ Data collection and ingestion strategies
- ✅ Storage solutions (databases, data lakes, warehouses)

**Advanced Technologies**:
- ✅ Big data processing with Spark and Hadoop
- ✅ Stream processing with Kafka and Flink
- ✅ Cloud platforms (AWS, GCP, Azure)
- ✅ Workflow orchestration with Airflow

**Production Excellence**:
- ✅ Data quality and governance frameworks
- ✅ Security and compliance (GDPR, encryption)
- ✅ Monitoring and observability
- ✅ Performance optimization patterns

**Real-World Application**:
- ✅ Three complete production-ready projects
- ✅ Best practices and design patterns
- ✅ Career roadmap and skill development
- ✅ Interview preparation strategies

### 🎯 Your Next Steps

**Immediate Actions (Next 30 Days)**:
1. **Choose Your Specialization**: Pick one cloud platform (AWS/GCP/Azure) to master first
2. **Build Your First Project**: Start with the e-commerce analytics project
3. **Set Up Your Environment**: Install tools and create accounts
4. **Join Communities**: Connect with data engineering professionals
5. **Create Your Portfolio**: Document your learning journey

**Short-Term Goals (3-6 Months)**:
1. **Complete 2-3 Real Projects**: Build end-to-end data pipelines
2. **Get Certified**: Pursue relevant cloud/technology certifications
3. **Contribute to Open Source**: Participate in data engineering projects
4. **Network Actively**: Attend meetups and conferences
5. **Apply for Positions**: Target data engineering roles

**Long-Term Vision (1-2 Years)**:
1. **Specialize Further**: Deep dive into specific domains (ML, real-time, etc.)
2. **Lead Projects**: Take ownership of critical data infrastructure
3. **Mentor Others**: Share knowledge and help junior engineers
4. **Stay Current**: Keep up with emerging technologies and trends
5. **Build Expertise**: Become known for specific skills or domains

### 🌟 The Data Engineering Landscape

The field of data engineering is rapidly evolving with exciting opportunities:

**Emerging Trends**:
- **DataOps and MLOps**: Operational excellence for data and ML pipelines
- **Real-time Everything**: Increasing demand for real-time data processing
- **Serverless Data Processing**: Cloud-native, serverless data architectures
- **Data Mesh**: Decentralized data architecture paradigm
- **AI-Assisted Development**: AI tools helping with code generation and optimization

**High-Demand Skills**:
- Stream processing and real-time analytics
- Multi-cloud and hybrid cloud architectures
- Data governance and privacy compliance
- Performance optimization and cost management
- Leadership and cross-functional collaboration

**Industry Opportunities**:
- **Technology Companies**: Building scalable data platforms
- **Financial Services**: Risk management and regulatory compliance
- **Healthcare**: Patient data analytics and research
- **E-commerce**: Recommendation systems and personalization
- **Consulting**: Helping organizations modernize data architecture

### 💪 Stay Motivated

Remember, becoming an expert data engineer is a journey, not a destination. The field is constantly evolving, which makes it exciting but also means continuous learning is essential.

**Keys to Success**:
- **Practice Consistently**: Build something every week
- **Learn in Public**: Share your projects and learnings
- **Embrace Challenges**: Tackle problems slightly beyond your comfort zone
- **Focus on Fundamentals**: Strong basics enable rapid learning of new tools
- **Think Like an Engineer**: Always consider scalability, reliability, and maintainability

### 🚀 Final Words

Data engineering is one of the most rewarding and high-impact fields in technology. As a data engineer, you'll:

- **Enable Data-Driven Decisions**: Your work directly impacts business outcomes
- **Solve Complex Problems**: Tackle interesting technical challenges at scale
- **Work with Cutting-Edge Technology**: Use the latest tools and platforms
- **Collaborate Widely**: Work with diverse teams across the organization
- **Make a Real Impact**: See your data solutions drive business success

The journey from zero to hero in data engineering is challenging but incredibly rewarding. You have all the knowledge you need to get started. Now it's time to build, create, and innovate!

**Remember**: Every expert was once a beginner. Your journey to becoming a data engineering hero starts with the first line of code you write today.

Keep learning, keep building, and most importantly, keep pushing the boundaries of what's possible with data! 🌟

---

## 📚 Additional Resources

**Essential Reading**:
- [Designing Data-Intensive Applications](https://dataintensive.net/) by Martin Kleppmann
- [The Data Warehouse Toolkit](https://www.kimballgroup.com/) by Ralph Kimball
- [Building Analytics Teams](https://www.oreilly.com/library/view/building-analytics-teams/9781492024415/) by John K. Thompson

**Online Communities**:
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - Reddit community
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Newsletter
- [Modern Data Stack](https://www.moderndatastack.xyz/) - Community and resources

**Conferences & Events**:
- DataEngConf - Annual data engineering conference
- Strata Data Conference - O'Reilly's data conference  
- Data Council - Data engineering and science conference
- Local meetups and user groups

**YouTube Channels**:
- Seattle Data Guy
- Data Engineering
- Databricks
- Snowflake Inc.

**Podcasts**:
- The Analytics Engineering Podcast
- Data Engineering Podcast
- DataFramed
- Machine Learning Guide

The journey begins now. Go build something amazing! 🚀🎯

---

*"The best time to plant a tree was 20 years ago. The second best time is now."* - Start your data engineering journey today!