# 👁️ Computer Vision - Zero to Hero Complete Guide

> **From Image Processing to Object Detection & Beyond**

---

## 🎯 Complete Computer Vision Mastery

**What You'll Build:**
- 📷 Image classification systems
- 🎯 Object detection (YOLO, Faster R-CNN)
- 🖼️ Image segmentation
- 👤 Face recognition
- 🎨 Image generation
- 🚀 Production CV systems

**Time:** 6-8 weeks | **Salary:** $120K-$200K+

---

## 📚 Quick Navigation

1. **Image Basics** - Loading, processing, augmentation
2. **CNNs Deep Dive** - ResNet, VGG, EfficientNet
3. **Object Detection** - YOLO, R-CNN, RetinaNet
4. **Segmentation** - U-Net, Mask R-CNN
5. **Face Recognition** - FaceNet, ArcFace
6. **Transfer Learning** - Fine-tuning pre-trained models
7. **Production** - Deployment, optimization

---

## Part 1: Image Fundamentals

### **Loading & Processing Images:**

```python
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image (OpenCV)
img_cv = cv2.imread('image.jpg')
img_cv_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# Load image (PIL)
img_pil = Image.open('image.jpg')
img_array = np.array(img_pil)

# Basic operations
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(img_cv, (224, 224))
cropped = img_cv[100:300, 100:300]

# Display
plt.imshow(img_cv_rgb)
plt.axis('off')
plt.show()
```

### **Data Augmentation:**

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import albumentations as A

# Keras augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    fill_mode='nearest'
)

# Albumentations (more powerful)
transform = A.Compose([
    A.Rotate(limit=45),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.GaussianBlur(blur_limit=(3, 7), p=0.2),
    A.CoarseDropout(max_holes=8, max_height=32, max_width=32, p=0.5),
])

augmented = transform(image=img_array)['image']
```

---

## Part 2: CNN Architectures

### **ResNet from Scratch:**

```python
import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, stride, 1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, 1, 1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 1, stride),
                nn.BatchNorm2d(out_channels)
            )
    
    def forward(self, x):
        out = torch.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = torch.relu(out)
        return out

class ResNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ResNet, self).__init__()
        
        self.conv1 = nn.Conv2d(3, 64, 7, 2, 3)
        self.bn1 = nn.BatchNorm2d(64)
        self.maxpool = nn.MaxPool2d(3, 2, 1)
        
        self.layer1 = self._make_layer(64, 64, 2, stride=1)
        self.layer2 = self._make_layer(64, 128, 2, stride=2)
        self.layer3 = self._make_layer(128, 256, 2, stride=2)
        self.layer4 = self._make_layer(256, 512, 2, stride=2)
        
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512, num_classes)
    
    def _make_layer(self, in_channels, out_channels, num_blocks, stride):
        layers = []
        layers.append(ResidualBlock(in_channels, out_channels, stride))
        for _ in range(1, num_blocks):
            layers.append(ResidualBlock(out_channels, out_channels))
        return nn.Sequential(*layers)
    
    def forward(self, x):
        x = torch.relu(self.bn1(self.conv1(x)))
        x = self.maxpool(x)
        
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        
        return x

# Usage
model = ResNet(num_classes=1000)
x = torch.randn(1, 3, 224, 224)
output = model(x)
print(output.shape)  # [1, 1000]
```

### **Using Pre-trained Models:**

```python
from torchvision import models, transforms
import torch

# Load pre-trained ResNet
model = models.resnet50(pretrained=True)
model.eval()

# Preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                       std=[0.229, 0.224, 0.225])
])

# Inference
from PIL import Image
img = Image.open('dog.jpg')
img_tensor = transform(img).unsqueeze(0)

with torch.no_grad():
    output = model(img_tensor)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top5_prob, top5_idx = torch.topk(probabilities, 5)

# Load ImageNet labels
import json
with open('imagenet_classes.json') as f:
    labels = json.load(f)

for prob, idx in zip(top5_prob, top5_idx):
    print(f"{labels[idx]}: {prob.item():.2%}")
```

---

## Part 3: Object Detection

### **YOLO (You Only Look Once):**

```python
import cv2
from ultralytics import YOLO

# Load YOLOv8
model = YOLO('yolov8n.pt')  # nano model

# Detect objects
img = cv2.imread('street.jpg')
results = model(img)

# Draw boxes
for result in results:
    boxes = result.boxes
    for box in boxes:
        # Get box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = box.conf[0]
        class_id = int(box.cls[0])
        label = model.names[class_id]
        
        # Draw
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f'{label} {confidence:.2f}',
                   (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX,
                   0.5, (0, 255, 0), 2)

cv2.imshow('Detections', img)
cv2.waitKey(0)
```

### **Training Custom YOLO:**

```python
from ultralytics import YOLO

# Load model
model = YOLO('yolov8n.pt')

# Train on custom dataset
# Dataset structure:
# dataset/
#   ├── train/
#   │   ├── images/
#   │   └── labels/
#   └── val/
#       ├── images/
#       └── labels/

model.train(
    data='dataset.yaml',  # Dataset config
    epochs=100,
    imgsz=640,
    batch=16,
    name='custom_yolo'
)

# Validate
metrics = model.val()

# Export
model.export(format='onnx')
```

### **Faster R-CNN:**

```python
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

# Load pre-trained model
model = fasterrcnn_resnet50_fpn(pretrained=True)

# Modify for custom classes
num_classes = 10  # Your number of classes + background
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

# Training loop
import torch
from torch.utils.data import DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

optimizer = torch.optim.SGD(model.parameters(), lr=0.005, momentum=0.9, weight_decay=0.0005)
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    for images, targets in train_loader:
        images = list(image.to(device) for image in images)
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]
        
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        
        optimizer.zero_grad()
        losses.backward()
        optimizer.step()
    
    lr_scheduler.step()
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {losses.item():.4f}')
```

---

## Part 4: Image Segmentation

### **U-Net Architecture:**

```python
import torch
import torch.nn as nn

class UNet(nn.Module):
    def __init__(self, in_channels=3, out_channels=1):
        super(UNet, self).__init__()
        
        # Encoder
        self.enc1 = self.conv_block(in_channels, 64)
        self.enc2 = self.conv_block(64, 128)
        self.enc3 = self.conv_block(128, 256)
        self.enc4 = self.conv_block(256, 512)
        
        # Bottleneck
        self.bottleneck = self.conv_block(512, 1024)
        
        # Decoder
        self.upconv4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.dec4 = self.conv_block(1024, 512)
        
        self.upconv3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.dec3 = self.conv_block(512, 256)
        
        self.upconv2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.dec2 = self.conv_block(256, 128)
        
        self.upconv1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.dec1 = self.conv_block(128, 64)
        
        self.out = nn.Conv2d(64, out_channels, 1)
        
        self.pool = nn.MaxPool2d(2)
    
    def conv_block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        enc1 = self.enc1(x)
        enc2 = self.enc2(self.pool(enc1))
        enc3 = self.enc3(self.pool(enc2))
        enc4 = self.enc4(self.pool(enc3))
        
        # Bottleneck
        bottleneck = self.bottleneck(self.pool(enc4))
        
        # Decoder
        dec4 = self.upconv4(bottleneck)
        dec4 = torch.cat([dec4, enc4], dim=1)
        dec4 = self.dec4(dec4)
        
        dec3 = self.upconv3(dec4)
        dec3 = torch.cat([dec3, enc3], dim=1)
        dec3 = self.dec3(dec3)
        
        dec2 = self.upconv2(dec3)
        dec2 = torch.cat([dec2, enc2], dim=1)
        dec2 = self.dec2(dec2)
        
        dec1 = self.upconv1(dec2)
        dec1 = torch.cat([dec1, enc1], dim=1)
        dec1 = self.dec1(dec1)
        
        return torch.sigmoid(self.out(dec1))

# Usage
model = UNet(in_channels=3, out_channels=1)
x = torch.randn(1, 3, 256, 256)
output = model(x)
print(output.shape)  # [1, 1, 256, 256]
```

---

## Part 5: Face Recognition

### **FaceNet Implementation:**

```python
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from PIL import Image

# Initialize models
mtcnn = MTCNN(image_size=160, margin=0, device='cuda')
resnet = InceptionResnetV1(pretrained='vggface2').eval()

# Detect and extract faces
img = Image.open('person.jpg')
faces = mtcnn(img)  # Returns cropped faces

# Get embeddings
if faces is not None:
    embeddings = resnet(faces.unsqueeze(0))
    print(f"Embedding shape: {embeddings.shape}")  # [1, 512]

# Face verification
def verify_faces(img1_path, img2_path, threshold=0.6):
    """Check if two images contain the same person"""
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    face1 = mtcnn(img1)
    face2 = mtcnn(img2)
    
    if face1 is None or face2 is None:
        return False, "Face not detected"
    
    emb1 = resnet(face1.unsqueeze(0))
    emb2 = resnet(face2.unsqueeze(0))
    
    # Calculate distance
    distance = (emb1 - emb2).norm().item()
    
    is_same = distance < threshold
    return is_same, distance

# Example
same, dist = verify_faces('person1.jpg', 'person2.jpg')
print(f"Same person: {same}, Distance: {dist:.4f}")
```

---

## Part 6: Transfer Learning

### **Fine-tuning Pre-trained Models:**

```python
import torch
import torch.nn as nn
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader

# Load pre-trained model
model = models.resnet50(pretrained=True)

# Freeze all layers except final
for param in model.parameters():
    param.requires_grad = False

# Replace final layer
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)  # 10 classes

# Only train final layer initially
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

# Data transforms
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Load dataset
train_dataset = datasets.ImageFolder('data/train', transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# Training
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
criterion = nn.CrossEntropyLoss()

# Phase 1: Train only final layer
for epoch in range(5):
    model.train()
    running_loss = 0.0
    
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f'Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}')

# Phase 2: Unfreeze and fine-tune all layers
for param in model.parameters():
    param.requires_grad = True

optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# Continue training...
```

---

## Part 7: Production Deployment

### **FastAPI Computer Vision API:**

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from torchvision import models, transforms
from PIL import Image
import io
import json

app = FastAPI(title="Computer Vision API")

# Load model at startup
@app.on_event("startup")
async def load_model():
    global model, transform, labels
    
    model = models.resnet50(pretrained=True)
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    with open('imagenet_labels.json') as f:
        labels = json.load(f)

@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    """Classify uploaded image"""
    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert('RGB')
    
    # Transform
    img_tensor = transform(image).unsqueeze(0)
    
    # Predict
    with torch.no_grad():
        outputs = model(img_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        top5_prob, top5_idx = torch.topk(probabilities, 5)
    
    # Format results
    results = []
    for prob, idx in zip(top5_prob, top5_idx):
        results.append({
            "class": labels[idx.item()],
            "probability": prob.item()
        })
    
    return JSONResponse(content={"predictions": results})

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    """Detect objects in image"""
    # Load YOLO or Faster R-CNN
    # Similar implementation
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 📚 Complete Projects

### **Project 1: Image Classifier**
- Build from scratch
- Train on custom dataset
- Deploy as web app

### **Project 2: Object Detector**
- Train YOLOv8
- Real-time detection
- Mobile deployment

### **Project 3: Face Recognition System**
- Face detection + recognition
- Database of known faces
- Production API

---

## 💼 Career Path

- **CV Engineer:** $110K-$150K
- **Senior CV Engineer:** $150K-$200K
- **Computer Vision Architect:** $200K-$300K+

---

## 🎯 Learning Path (6-8 weeks)

```
Week 1-2: CNNs & Image Processing
Week 3-4: Object Detection
Week 5-6: Segmentation & Face Recognition
Week 7-8: Transfer Learning & Production
```

---

*Computer Vision Complete Guide*
*From Image Processing to Production Systems*
*Career-ready in 6-8 weeks* 🚀

