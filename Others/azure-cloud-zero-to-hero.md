# Azure Cloud: Zero to Hero Guide
## Complete Microsoft Azure Mastery for Enterprise

---

## 📚 Table of Contents

1. [Introduction to Azure](#introduction)
2. [Azure Account Setup](#setup)
3. [Azure Portal & CLI](#portal)
4. [Compute Services](#compute)
5. [Storage Services](#storage)
6. [Networking](#networking)
7. [Databases](#databases)
8. [Azure App Service](#app-service)
9. [Azure Functions (Serverless)](#functions)
10. [Containers & Kubernetes](#containers)
11. [Identity & Security](#security)
12. [Monitoring & Logging](#monitoring)
13. [DevOps & CI/CD](#devops)
14. [Cost Management](#cost)
15. [Best Practices](#best-practices)
16. [Real-World Projects](#projects)

---

## 🎯 Introduction to Azure {#introduction}

### What is Microsoft Azure?

**Azure** is Microsoft's cloud computing platform offering 200+ services for computing, storage, databases, AI, and more.

```
┌────────────────────────────────────────────┐
│           Azure Cloud Platform             │
├────────────────────────────────────────────┤
│  ☁️  Compute    │  💾  Storage             │
│  🗄️  Databases  │  🌐  Networking          │
│  🤖  AI/ML      │  🔐  Security            │
│  📊  Analytics  │  🛠️  DevOps              │
│  🔌  IoT        │  🚀  Serverless          │
└────────────────────────────────────────────┘
```

### Azure vs AWS vs GCP

```
┌──────────────────────────────────────────────┐
│  Service Comparison                          │
├──────────────┬──────────┬──────────┬─────────┤
│  Service     │  Azure   │   AWS    │   GCP   │
├──────────────┼──────────┼──────────┼─────────┤
│  VM          │  VM      │   EC2    │Compute  │
│  Storage     │  Blob    │   S3     │Cloud St │
│  Database    │  SQL DB  │   RDS    │Cloud SQL│
│  Serverless  │ Functions│  Lambda  │Functions│
│  Container   │  AKS     │   EKS    │   GKE   │
│  AI/ML       │  ML      │SageMaker │  AI     │
└──────────────┴──────────┴──────────┴─────────┘
```

### Why Azure?

- ✅ **Enterprise Integration** - Seamless with Microsoft products
- ✅ **Hybrid Cloud** - On-premises + Cloud
- ✅ **Global Reach** - 60+ regions worldwide
- ✅ **Security & Compliance** - 90+ compliance certifications
- ✅ **AI & ML** - Industry-leading AI services

---

## 🔧 Azure Account Setup {#setup}

### Create Free Account

1. Visit: https://azure.microsoft.com/free
2. Sign up with Microsoft account
3. Get **$200 free credits** for 30 days
4. Access to **55+ always-free services**

**Free Services Include:**
- 750 hours of B1S Virtual Machines
- 5 GB Blob Storage
- 250 GB SQL Database
- 1 million Azure Functions requests
- Azure DevOps (5 users)

### Azure Subscriptions

```
Azure Account
└── Subscription 1 (Pay-as-you-go)
    ├── Resource Group 1
    │   ├── VM 1
    │   ├── Storage Account
    │   └── Database
    └── Resource Group 2
        └── App Service
```

**Subscription Types:**
- **Free Trial** - $200 credit for 30 days
- **Pay-As-You-Go** - Pay for what you use
- **Enterprise Agreement** - Discounts for large organizations
- **Student** - $100 credit for students

---

## 🖥️ Azure Portal & CLI {#portal}

### Azure Portal (Web UI)

**URL:** https://portal.azure.com

```
┌────────────────────────────────────┐
│  Azure Portal                      │
├────────────────────────────────────┤
│  📊 Dashboard                      │
│  🔍 Search bar (top)               │
│  📁 Resource Groups                │
│  💰 Cost Management                │
│  🔔 Notifications                  │
└────────────────────────────────────┘
```

### Azure CLI

**Install Azure CLI**

```bash
# macOS
brew install azure-cli

# Windows
# Download from https://aka.ms/installazurecliwindows

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

**Login & Basic Commands**

```bash
# Login to Azure
az login

# List subscriptions
az account list --output table

# Set active subscription
az account set --subscription "My Subscription"

# List resource groups
az group list --output table

# Create resource group
az group create --name myResourceGroup --location eastus

# List all resources
az resource list --output table

# Get help
az --help
az vm --help
```

### Azure PowerShell

```powershell
# Install Azure PowerShell
Install-Module -Name Az -AllowClobber -Scope CurrentUser

# Connect to Azure
Connect-AzAccount

# Get subscriptions
Get-AzSubscription

# Create resource group
New-AzResourceGroup -Name myResourceGroup -Location "East US"
```

---

## 💻 Compute Services {#compute}

### 1. Virtual Machines (IaaS)

**Create VM via CLI**

```bash
# Create Linux VM
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image Ubuntu2204 \
  --size Standard_B2s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --public-ip-sku Standard

# Open port 80 for web traffic
az vm open-port --port 80 --resource-group myResourceGroup --name myVM

# Get public IP
az vm show --resource-group myResourceGroup --name myVM --show-details \
  --query publicIps -o tsv

# SSH into VM
ssh azureuser@<PUBLIC_IP>
```

**VM Sizes**

```
┌──────────────────────────────────────────┐
│  VM Series                               │
├──────────────┬───────────────────────────┤
│  B-Series    │ Burstable (Dev/Test)     │
│  D-Series    │ General purpose          │
│  F-Series    │ Compute optimized        │
│  E-Series    │ Memory optimized         │
│  M-Series    │ Large memory (SAP)       │
│  N-Series    │ GPU (AI/ML)              │
└──────────────┴───────────────────────────┘
```

### 2. Virtual Machine Scale Sets (Auto-scaling)

```bash
# Create scale set
az vmss create \
  --resource-group myResourceGroup \
  --name myScaleSet \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --instance-count 2 \
  --vm-sku Standard_B2s

# Configure auto-scaling
az monitor autoscale create \
  --resource-group myResourceGroup \
  --resource myScaleSet \
  --resource-type Microsoft.Compute/virtualMachineScaleSets \
  --min-count 2 \
  --max-count 10 \
  --count 2

# Add scale-out rule (CPU > 70%)
az monitor autoscale rule create \
  --resource-group myResourceGroup \
  --autoscale-name myScaleSet \
  --condition "Percentage CPU > 70 avg 5m" \
  --scale out 1
```

### 3. Azure Batch (HPC)

For large-scale parallel computing jobs.

```bash
# Create Batch account
az batch account create \
  --name mybatchaccount \
  --resource-group myResourceGroup \
  --location eastus
```

---

## 💾 Storage Services {#storage}

### 1. Blob Storage (Object Storage)

**Create Storage Account**

```bash
# Create storage account
az storage account create \
  --name mystorageaccount123 \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2

# Get connection string
az storage account show-connection-string \
  --name mystorageaccount123 \
  --resource-group myResourceGroup \
  --query connectionString -o tsv

# Create container
az storage container create \
  --name mycontainer \
  --account-name mystorageaccount123

# Upload file
az storage blob upload \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --name myfile.txt \
  --file ./myfile.txt

# List blobs
az storage blob list \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --output table

# Download file
az storage blob download \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --name myfile.txt \
  --file ./downloaded.txt
```

**Blob Storage Tiers**

```
┌─────────────────────────────────────────┐
│  Hot     → Frequent access ($$$)        │
│  Cool    → Infrequent access ($$)       │
│  Archive → Rare access ($)              │
└─────────────────────────────────────────┘
```

**Using Azure SDK (Node.js)**

```javascript
const { BlobServiceClient } = require('@azure/storage-blob')

const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING
const blobServiceClient = BlobServiceClient.fromConnectionString(connectionString)

// Upload file
async function uploadFile(containerName, fileName, fileContent) {
  const containerClient = blobServiceClient.getContainerClient(containerName)
  const blockBlobClient = containerClient.getBlockBlobClient(fileName)
  
  await blockBlobClient.upload(fileContent, fileContent.length)
  console.log(`Uploaded ${fileName}`)
}

// Download file
async function downloadFile(containerName, fileName) {
  const containerClient = blobServiceClient.getContainerClient(containerName)
  const blockBlobClient = containerClient.getBlockBlobClient(fileName)
  
  const downloadResponse = await blockBlobClient.download()
  const content = await streamToBuffer(downloadResponse.readableStreamBody)
  
  return content.toString()
}

// List blobs
async function listBlobs(containerName) {
  const containerClient = blobServiceClient.getContainerClient(containerName)
  
  for await (const blob of containerClient.listBlobsFlat()) {
    console.log(`Blob: ${blob.name}`)
  }
}
```

### 2. File Storage (SMB File Shares)

```bash
# Create file share
az storage share create \
  --name myfileshare \
  --account-name mystorageaccount123

# Upload file to share
az storage file upload \
  --share-name myfileshare \
  --source ./myfile.txt \
  --account-name mystorageaccount123
```

### 3. Queue Storage (Message Queue)

```javascript
const { QueueServiceClient } = require('@azure/storage-queue')

const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING
const queueServiceClient = QueueServiceClient.fromConnectionString(connectionString)

// Create queue
async function createQueue(queueName) {
  const queueClient = queueServiceClient.getQueueClient(queueName)
  await queueClient.create()
}

// Send message
async function sendMessage(queueName, message) {
  const queueClient = queueServiceClient.getQueueClient(queueName)
  await queueClient.sendMessage(message)
}

// Receive messages
async function receiveMessages(queueName) {
  const queueClient = queueServiceClient.getQueueClient(queueName)
  const messages = await queueClient.receiveMessages()
  
  for (const message of messages.receivedMessageItems) {
    console.log(`Message: ${message.messageText}`)
    // Delete message after processing
    await queueClient.deleteMessage(message.messageId, message.popReceipt)
  }
}
```

### 4. Table Storage (NoSQL)

```javascript
const { TableClient } = require('@azure/data-tables')

const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING
const tableName = 'users'
const tableClient = TableClient.fromConnectionString(connectionString, tableName)

// Create table
await tableClient.createTable()

// Insert entity
await tableClient.createEntity({
  partitionKey: 'user',
  rowKey: '1',
  name: 'John Doe',
  email: 'john@example.com'
})

// Query entities
const entities = tableClient.listEntities()
for await (const entity of entities) {
  console.log(entity)
}
```

---

## 🌐 Networking {#networking}

### Virtual Network (VNet)

```bash
# Create virtual network
az network vnet create \
  --name myVNet \
  --resource-group myResourceGroup \
  --address-prefix 10.0.0.0/16 \
  --subnet-name mySubnet \
  --subnet-prefix 10.0.1.0/24

# Create Network Security Group (NSG)
az network nsg create \
  --name myNSG \
  --resource-group myResourceGroup

# Add rule to allow HTTP
az network nsg rule create \
  --name AllowHTTP \
  --nsg-name myNSG \
  --resource-group myResourceGroup \
  --priority 1000 \
  --source-address-prefixes '*' \
  --destination-port-ranges 80 \
  --access Allow \
  --protocol Tcp
```

### Load Balancer

```bash
# Create public IP
az network public-ip create \
  --name myPublicIP \
  --resource-group myResourceGroup \
  --sku Standard

# Create load balancer
az network lb create \
  --name myLoadBalancer \
  --resource-group myResourceGroup \
  --sku Standard \
  --public-ip-address myPublicIP \
  --frontend-ip-name myFrontEnd \
  --backend-pool-name myBackEndPool
```

### Application Gateway (Layer 7 Load Balancer)

- **Features:**
  - SSL termination
  - URL-based routing
  - WAF (Web Application Firewall)
  - Auto-scaling

---

## 🗄️ Databases {#databases}

### 1. Azure SQL Database

**Create SQL Database**

```bash
# Create SQL Server
az sql server create \
  --name myserver123 \
  --resource-group myResourceGroup \
  --location eastus \
  --admin-user sqladmin \
  --admin-password P@ssw0rd123!

# Configure firewall
az sql server firewall-rule create \
  --server myserver123 \
  --resource-group myResourceGroup \
  --name AllowAllAzure \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0

# Create database
az sql db create \
  --name myDatabase \
  --server myserver123 \
  --resource-group myResourceGroup \
  --service-objective S0
```

**Connect from Node.js**

```javascript
const sql = require('mssql')

const config = {
  user: 'sqladmin',
  password: 'P@ssw0rd123!',
  server: 'myserver123.database.windows.net',
  database: 'myDatabase',
  options: {
    encrypt: true,
    trustServerCertificate: false
  }
}

async function connectDB() {
  try {
    await sql.connect(config)
    const result = await sql.query`SELECT * FROM Users`
    console.log(result.recordset)
  } catch (err) {
    console.error(err)
  }
}
```

### 2. Azure Cosmos DB (NoSQL)

**Create Cosmos DB**

```bash
# Create Cosmos account
az cosmosdb create \
  --name mycosmosaccount123 \
  --resource-group myResourceGroup \
  --kind GlobalDocumentDB \
  --locations regionName=eastus failoverPriority=0

# Create database
az cosmosdb sql database create \
  --account-name mycosmosaccount123 \
  --resource-group myResourceGroup \
  --name myDatabase

# Create container
az cosmosdb sql container create \
  --account-name mycosmosaccount123 \
  --resource-group myResourceGroup \
  --database-name myDatabase \
  --name myContainer \
  --partition-key-path "/userId"
```

**Connect from Node.js**

```javascript
const { CosmosClient } = require('@azure/cosmos')

const endpoint = process.env.COSMOS_ENDPOINT
const key = process.env.COSMOS_KEY
const client = new CosmosClient({ endpoint, key })

const database = client.database('myDatabase')
const container = database.container('myContainer')

// Create item
async function createItem(item) {
  const { resource } = await container.items.create(item)
  console.log('Created:', resource)
}

// Query items
async function queryItems() {
  const { resources } = await container.items
    .query('SELECT * FROM c WHERE c.userId = "123"')
    .fetchAll()
  
  console.log(resources)
}

// Update item
async function updateItem(id, partitionKey, updates) {
  const { resource } = await container.item(id, partitionKey).replace(updates)
  console.log('Updated:', resource)
}
```

### 3. Azure Database for PostgreSQL/MySQL

```bash
# Create PostgreSQL server
az postgres server create \
  --name mypostgresserver123 \
  --resource-group myResourceGroup \
  --location eastus \
  --admin-user myadmin \
  --admin-password P@ssw0rd123! \
  --sku-name B_Gen5_1
```

---

## 🚀 Azure App Service {#app-service}

### Deploy Web App

**Create App Service**

```bash
# Create App Service plan
az appservice plan create \
  --name myAppServicePlan \
  --resource-group myResourceGroup \
  --sku B1 \
  --is-linux

# Create web app
az webapp create \
  --name mywebapp123 \
  --resource-group myResourceGroup \
  --plan myAppServicePlan \
  --runtime "NODE|18-lts"

# Deploy from local Git
az webapp deployment source config-local-git \
  --name mywebapp123 \
  --resource-group myResourceGroup

# Get deployment URL
az webapp deployment list-publishing-credentials \
  --name mywebapp123 \
  --resource-group myResourceGroup \
  --query scmUri -o tsv
```

**Deploy Node.js App**

```bash
# Initialize Git
git init
git add .
git commit -m "Initial commit"

# Add Azure remote
git remote add azure <GIT_URL>

# Deploy
git push azure main
```

**Environment Variables**

```bash
# Set app settings
az webapp config appsettings set \
  --name mywebapp123 \
  --resource-group myResourceGroup \
  --settings DATABASE_URL="..." JWT_SECRET="..."
```

---

## ⚡ Azure Functions (Serverless) {#functions}

### Create Function App

```bash
# Create storage account for functions
az storage account create \
  --name myfunctionstorage123 \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS

# Create Function App
az functionapp create \
  --name myfunctionapp123 \
  --resource-group myResourceGroup \
  --storage-account myfunctionstorage123 \
  --consumption-plan-location eastus \
  --runtime node \
  --runtime-version 18 \
  --functions-version 4
```

### HTTP Trigger Function

```bash
# Initialize Functions project
npm install -g azure-functions-core-tools@4
func init myFunctionProject --worker-runtime node --language typescript
cd myFunctionProject

# Create HTTP trigger
func new --name HttpTrigger --template "HTTP trigger"
```

**Function Code**

```typescript
// src/functions/HttpTrigger.ts
import { app, HttpRequest, HttpResponseInit, InvocationContext } from '@azure/functions'

export async function HttpTrigger(
  request: HttpRequest,
  context: InvocationContext
): Promise<HttpResponseInit> {
  context.log('HTTP trigger function processed a request')
  
  const name = request.query.get('name') || await request.text() || 'World'
  
  return {
    status: 200,
    jsonBody: {
      message: `Hello, ${name}!`,
      timestamp: new Date().toISOString()
    }
  }
}

app.http('HttpTrigger', {
  methods: ['GET', 'POST'],
  authLevel: 'anonymous',
  handler: HttpTrigger
})
```

### Timer Trigger (Scheduled Function)

```typescript
import { app, InvocationContext, Timer } from '@azure/functions'

export async function TimerTrigger(myTimer: Timer, context: InvocationContext): Promise<void> {
  context.log('Timer trigger function ran!', new Date().toISOString())
  
  // Your scheduled logic here
  await sendDailyReport()
}

app.timer('TimerTrigger', {
  schedule: '0 0 9 * * *', // Every day at 9 AM
  handler: TimerTrigger
})
```

### Blob Trigger

```typescript
import { app, InvocationContext } from '@azure/functions'

export async function BlobTrigger(blob: Buffer, context: InvocationContext): Promise<void> {
  context.log(`Blob trigger processed blob "${context.triggerMetadata.name}"`)
  context.log(`Size: ${blob.length} bytes`)
  
  // Process uploaded file
  await processImage(blob)
}

app.storageBlob('BlobTrigger', {
  path: 'uploads/{name}',
  connection: 'AzureWebJobsStorage',
  handler: BlobTrigger
})
```

**Deploy Function**

```bash
# Deploy to Azure
func azure functionapp publish myfunctionapp123
```

---

## 🐳 Containers & Kubernetes {#containers}

### Azure Container Instances (ACI)

```bash
# Run container
az container create \
  --name mycontainer \
  --resource-group myResourceGroup \
  --image mcr.microsoft.com/azuredocs/aci-helloworld \
  --dns-name-label mycontainer123 \
  --ports 80

# Get container status
az container show \
  --name mycontainer \
  --resource-group myResourceGroup \
  --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" \
  --out table
```

### Azure Kubernetes Service (AKS)

```bash
# Create AKS cluster
az aks create \
  --name myAKSCluster \
  --resource-group myResourceGroup \
  --node-count 2 \
  --node-vm-size Standard_B2s \
  --enable-managed-identity \
  --generate-ssh-keys

# Get credentials
az aks get-credentials \
  --name myAKSCluster \
  --resource-group myResourceGroup

# Verify connection
kubectl get nodes

# Deploy application
kubectl apply -f deployment.yaml
```

**Deployment Example**

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry.azurecr.io/myapp:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 80
```

---

## 🔐 Identity & Security {#security}

### Azure Active Directory (Azure AD)

**Register Application**

```bash
# Create app registration
az ad app create \
  --display-name MyApp \
  --sign-in-audience AzureADMyOrg

# Create service principal
az ad sp create-for-rbac \
  --name MyAppServicePrincipal \
  --role contributor \
  --scopes /subscriptions/{subscription-id}/resourceGroups/myResourceGroup
```

### Managed Identity

```bash
# Enable system-assigned identity for VM
az vm identity assign \
  --name myVM \
  --resource-group myResourceGroup

# Grant access to Key Vault
az keyvault set-policy \
  --name myKeyVault \
  --object-id <IDENTITY_PRINCIPAL_ID> \
  --secret-permissions get list
```

**Use Managed Identity in Code**

```javascript
const { DefaultAzureCredential } = require('@azure/identity')
const { SecretClient } = require('@azure/keyvault-secrets')

const credential = new DefaultAzureCredential()
const vaultUrl = 'https://mykeyvault.vault.azure.net'
const client = new SecretClient(vaultUrl, credential)

// Get secret
const secret = await client.getSecret('DatabasePassword')
console.log(secret.value)
```

### Azure Key Vault

```bash
# Create Key Vault
az keyvault create \
  --name mykeyvault123 \
  --resource-group myResourceGroup \
  --location eastus

# Add secret
az keyvault secret set \
  --vault-name mykeyvault123 \
  --name DatabasePassword \
  --value "P@ssw0rd123!"

# Get secret
az keyvault secret show \
  --vault-name mykeyvault123 \
  --name DatabasePassword \
  --query value -o tsv
```

---

## 📊 Monitoring & Logging {#monitoring}

### Application Insights

```bash
# Create Application Insights
az monitor app-insights component create \
  --app myAppInsights \
  --location eastus \
  --resource-group myResourceGroup
```

**Integrate with Node.js**

```javascript
const appInsights = require('applicationinsights')

appInsights.setup(process.env.APPLICATIONINSIGHTS_CONNECTION_STRING)
  .setAutoDependencyCorrelation(true)
  .setAutoCollectRequests(true)
  .setAutoCollectPerformance(true)
  .setAutoCollectExceptions(true)
  .setAutoCollectDependencies(true)
  .setAutoCollectConsole(true)
  .start()

const client = appInsights.defaultClient

// Track custom event
client.trackEvent({ name: 'UserLogin', properties: { userId: '123' } })

// Track metric
client.trackMetric({ name: 'OrderValue', value: 99.99 })

// Track exception
client.trackException({ exception: new Error('Something went wrong') })
```

### Azure Monitor

```bash
# Create alert rule
az monitor metrics alert create \
  --name HighCPUAlert \
  --resource-group myResourceGroup \
  --scopes /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU is over 80%"
```

---

## 🔄 DevOps & CI/CD {#devops}

### Azure DevOps Pipeline

```yaml
# azure-pipelines.yml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  azureSubscription: 'MyAzureSubscription'
  webAppName: 'mywebapp123'

stages:
- stage: Build
  jobs:
  - job: BuildJob
    steps:
    - task: NodeTool@0
      inputs:
        versionSpec: '18.x'
    
    - script: |
        npm install
        npm run build
        npm test
      displayName: 'Install, Build, Test'
    
    - task: ArchiveFiles@2
      inputs:
        rootFolderOrFile: '$(System.DefaultWorkingDirectory)'
        includeRootFolder: false
        archiveType: 'zip'
        archiveFile: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip'
    
    - task: PublishBuildArtifacts@1
      inputs:
        PathtoPublish: '$(Build.ArtifactStagingDirectory)'
        ArtifactName: 'drop'

- stage: Deploy
  dependsOn: Build
  jobs:
  - deployment: DeployWeb
    environment: 'production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureWebApp@1
            inputs:
              azureSubscription: '$(azureSubscription)'
              appType: 'webAppLinux'
              appName: '$(webAppName)'
              package: '$(Pipeline.Workspace)/drop/$(Build.BuildId).zip'
```

### GitHub Actions with Azure

```yaml
# .github/workflows/azure.yml
name: Deploy to Azure

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm install
    
    - name: Build
      run: npm run build
    
    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}
    
    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'mywebapp123'
        package: .
```

---

## 💰 Cost Management {#cost}

### Monitor Costs

```bash
# View cost analysis
az consumption usage list \
  --start-date 2024-01-01 \
  --end-date 2024-01-31

# Create budget
az consumption budget create \
  --budget-name MyMonthlyBudget \
  --amount 100 \
  --time-grain Monthly \
  --category Cost \
  --start-date 2024-01-01 \
  --end-date 2024-12-31
```

### Cost Optimization Tips

```
✅ Use Reserved Instances (save up to 72%)
✅ Auto-shutdown dev/test VMs
✅ Right-size resources
✅ Use Azure Hybrid Benefit
✅ Delete unused resources
✅ Use Spot VMs for non-critical workloads
```

---

## ✅ Best Practices {#best-practices}

### 1. Resource Naming Convention

```
{resource-type}-{workload}-{environment}-{region}-{instance}

Examples:
- vm-web-prod-eastus-01
- st-logs-dev-westus-01
- sql-orders-prod-eastus-01
```

### 2. Use Resource Groups Wisely

```
Development RG  → Dev resources
Production RG   → Prod resources
Shared RG       → Shared services
```

### 3. Implement RBAC

```bash
# Assign role to user
az role assignment create \
  --role "Contributor" \
  --assignee user@example.com \
  --resource-group myResourceGroup
```

### 4. Tag Resources

```bash
az resource tag \
  --tags Environment=Production Owner=TeamA \
  --resource-group myResourceGroup \
  --name myVM \
  --resource-type Microsoft.Compute/virtualMachines
```

---

## 🎯 Real-World Projects {#projects}

### Project 1: Scalable Web App
- App Service for frontend
- Azure SQL for database
- Blob Storage for files
- Application Insights for monitoring
- Azure AD for authentication

### Project 2: Serverless API
- Azure Functions for API
- Cosmos DB for data
- API Management gateway
- Key Vault for secrets
- DevOps CI/CD pipeline

### Project 3: Containerized Microservices
- AKS cluster
- Azure Container Registry
- Load Balancer
- Azure Monitor
- Log Analytics

---

## 🏆 Congratulations!

You've mastered Azure Cloud! You can now:

- ✅ Deploy and manage Azure resources
- ✅ Build scalable applications
- ✅ Implement security best practices
- ✅ Set up CI/CD pipelines
- ✅ Optimize costs
- ✅ Monitor and troubleshoot

**Next Steps:**
- Get Azure certifications (AZ-900, AZ-104, AZ-204)
- Build real-world projects
- Learn Azure Architecture patterns
- Explore AI/ML services

Keep building in the cloud! ☁️🚀
