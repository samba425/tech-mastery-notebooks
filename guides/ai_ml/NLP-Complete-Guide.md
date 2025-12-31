# 💬 Natural Language Processing (NLP) - Zero to Hero Complete Guide

> **From Text Processing to Large Language Models (LLMs)**

---

## 🎯 What You'll Learn

Complete NLP mastery from basics to state-of-the-art:

- 📝 Text preprocessing & tokenization
- 🔤 Word embeddings (Word2Vec, GloVe, FastText)
- 🧠 Sequence models (RNN, LSTM, GRU)
- 🤖 Transformers architecture
- 🎯 BERT, GPT, T5, and modern LLMs
- 🛠️ Fine-tuning pre-trained models
- 🚀 Production NLP applications
- 💼 Real-world projects

**Time:** 6-8 weeks to master
**Prerequisites:** Python, basic ML knowledge
**Career:** NLP Engineer ($110K-$180K+)

---

## 📚 Table of Contents

### **Part 1: Text Preprocessing (Week 1)**
1. Introduction to NLP
2. Text Cleaning
3. Tokenization
4. Stemming & Lemmatization
5. Stop Words Removal
6. N-grams

### **Part 2: Text Representation (Week 2)**
7. Bag of Words (BoW)
8. TF-IDF
9. Word2Vec
10. GloVe
11. FastText

### **Part 3: Sequence Models (Week 3)**
12. RNN for Text
13. LSTM for NLP
14. GRU
15. Bidirectional models
16. Attention Mechanism

### **Part 4: Transformers (Week 4-5)**
17. Transformer Architecture
18. BERT
19. GPT (GPT-2, GPT-3, GPT-4)
20. T5 & Other Models
21. Hugging Face Library

### **Part 5: NLP Tasks (Week 6)**
22. Text Classification
23. Named Entity Recognition (NER)
24. Sentiment Analysis
25. Question Answering
26. Text Summarization
27. Machine Translation

### **Part 6: LLMs & Fine-tuning (Week 7)**
28. Large Language Models
29. Prompt Engineering
30. Fine-tuning LLMs
31. RAG (Retrieval Augmented Generation)
32. LangChain for NLP

### **Part 7: Production (Week 8)**
33. NLP Pipelines
34. Model Deployment
35. Scaling NLP Systems
36. Real-World Applications

---

## Part 1: Text Preprocessing

---

## 1. Introduction to NLP

### **What is NLP?**

Natural Language Processing (NLP) is AI that enables computers to understand, interpret, and generate human language.

### **NLP Applications:**

```
Consumer Applications:
├── Chatbots & Virtual Assistants (Siri, Alexa)
├── Machine Translation (Google Translate)
├── Auto-complete & Auto-correct
├── Email spam filtering
└── Voice recognition

Business Applications:
├── Sentiment analysis (social media monitoring)
├── Customer support automation
├── Document classification
├── Information extraction
└── Content recommendation

Advanced Applications:
├── Question answering systems
├── Text summarization
├── Legal document analysis
├── Medical record processing
└── Code generation (GitHub Copilot)
```

### **NLP Pipeline:**

```
Raw Text
    ↓
Text Preprocessing
    ↓
Feature Extraction
    ↓
Model Training/Inference
    ↓
Post-processing
    ↓
Output (Classification, Generation, etc.)
```

---

## 2. Text Cleaning

### **Basic Text Cleaning:**

```python
import re
import string

def clean_text(text):
    """
    Basic text cleaning pipeline
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove mentions (@username)
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

# Example
text = "Check out https://example.com! Email me at user@email.com #NLP @john123"
cleaned = clean_text(text)
print(cleaned)
# Output: "check out email me at"
```

### **Advanced Cleaning:**

```python
import unicodedata

def advanced_clean_text(text):
    """
    Advanced text cleaning
    """
    # Remove accents
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove special characters but keep some punctuation
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Example
text = "<p>Café résumé naïve</p>"
cleaned = advanced_clean_text(text)
print(cleaned)
# Output: "Cafe resume naive"
```

---

## 3. Tokenization

### **Word Tokenization:**

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

text = "Hello! This is NLP. It's amazing."

# Word tokenization
words = word_tokenize(text)
print("Words:", words)
# Output: ['Hello', '!', 'This', 'is', 'NLP', '.', 'It', "'s", 'amazing', '.']

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)
# Output: ['Hello!', 'This is NLP.', "It's amazing."]
```

### **Advanced Tokenization (BPE, WordPiece):**

```python
from transformers import AutoTokenizer

# Using BERT tokenizer (WordPiece)
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

text = "Natural Language Processing"

# Tokenize
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)
# Output: ['natural', 'language', 'processing']

# Convert to IDs
token_ids = tokenizer.encode(text)
print("Token IDs:", token_ids)
# Output: [101, 3019, 2653, 6364, 102]

# Decode back
decoded = tokenizer.decode(token_ids)
print("Decoded:", decoded)
# Output: "[CLS] natural language processing [SEP]"
```

### **Subword Tokenization (Custom):**

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# Initialize tokenizer
tokenizer = Tokenizer(BPE())
tokenizer.pre_tokenizer = Whitespace()

# Train on corpus
trainer = BpeTrainer(vocab_size=5000, special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]"])
files = ["corpus.txt"]
tokenizer.train(files, trainer)

# Use tokenizer
output = tokenizer.encode("Hello world!")
print("Tokens:", output.tokens)
print("IDs:", output.ids)
```

---

## 4. Stemming & Lemmatization

### **Stemming:**

```python
from nltk.stem import PorterStemmer, SnowballStemmer

# Porter Stemmer
porter = PorterStemmer()

words = ["running", "runs", "ran", "runner", "easily", "fairly"]

print("Porter Stemmer:")
for word in words:
    print(f"{word} -> {porter.stem(word)}")

# Output:
# running -> run
# runs -> run
# ran -> ran
# runner -> runner
# easily -> easili
# fairly -> fairli
```

### **Lemmatization:**

```python
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

lemmatizer = WordNetLemmatizer()

# Simple lemmatization
words = ["running", "runs", "ran", "better", "geese"]

print("Lemmatization:")
for word in words:
    print(f"{word} -> {lemmatizer.lemmatize(word, pos='v')}")

# Output:
# running -> run
# runs -> run
# ran -> run
# better -> better
# geese -> goose

# Context-aware lemmatization
def get_wordnet_pos(tag):
    """Convert POS tag to WordNet format"""
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_text(text):
    """Lemmatize with POS tagging"""
    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    
    lemmatized = []
    for word, tag in pos_tags:
        wn_tag = get_wordnet_pos(tag)
        lemmatized.append(lemmatizer.lemmatize(word, pos=wn_tag))
    
    return ' '.join(lemmatized)

text = "The running dogs are better runners"
print(lemmatize_text(text))
# Output: "The run dog be good runner"
```

---

## Part 2: Text Representation

---

## 7. Bag of Words (BoW)

### **Basic BoW:**

```python
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love NLP and machine learning",
    "NLP is amazing for text processing",
    "Machine learning and deep learning are related"
]

# Create BoW
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

# Get feature names
print("Vocabulary:", vectorizer.get_feature_names_out())

# Get matrix
print("\nBoW Matrix:\n", bow_matrix.toarray())

# Document-term matrix
import pandas as pd
df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)
print("\n", df)
```

---

## 8. TF-IDF

### **Implementation:**

```python
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

documents = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "Cats and dogs are enemies"
]

# TF-IDF vectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

# Get feature names
feature_names = tfidf.get_feature_names_out()

# Display TF-IDF scores
for doc_idx, doc in enumerate(documents):
    print(f"\nDocument {doc_idx + 1}: {doc}")
    scores = tfidf_matrix[doc_idx].toarray()[0]
    
    # Get top 3 words
    top_indices = np.argsort(scores)[::-1][:3]
    for idx in top_indices:
        if scores[idx] > 0:
            print(f"  {feature_names[idx]}: {scores[idx]:.3f}")
```

### **TF-IDF from Scratch:**

```python
import math
from collections import Counter

def compute_tf(document):
    """Term Frequency"""
    words = document.lower().split()
    word_count = Counter(words)
    total_words = len(words)
    
    tf = {}
    for word, count in word_count.items():
        tf[word] = count / total_words
    
    return tf

def compute_idf(documents):
    """Inverse Document Frequency"""
    N = len(documents)
    idf = {}
    
    # Get all unique words
    all_words = set()
    for doc in documents:
        all_words.update(doc.lower().split())
    
    # Calculate IDF for each word
    for word in all_words:
        containing_docs = sum(1 for doc in documents if word in doc.lower().split())
        idf[word] = math.log(N / containing_docs)
    
    return idf

def compute_tfidf(documents):
    """TF-IDF Computation"""
    idf = compute_idf(documents)
    
    tfidf_docs = []
    for doc in documents:
        tf = compute_tf(doc)
        tfidf = {}
        
        for word, tf_value in tf.items():
            tfidf[word] = tf_value * idf[word]
        
        tfidf_docs.append(tfidf)
    
    return tfidf_docs

# Example
docs = [
    "The cat sat on the mat",
    "The dog sat on the log"
]

tfidf_scores = compute_tfidf(docs)
for i, scores in enumerate(tfidf_scores):
    print(f"Document {i+1}:")
    for word, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  {word}: {score:.3f}")
```

---

## 9. Word2Vec

### **Training Word2Vec:**

```python
from gensim.models import Word2Vec
import nltk
nltk.download('brown')
from nltk.corpus import brown

# Prepare corpus
sentences = brown.sents()[:10000]  # Use first 10k sentences

# Train Word2Vec
model = Word2Vec(
    sentences=sentences,
    vector_size=100,      # Embedding dimension
    window=5,             # Context window
    min_count=2,          # Minimum word frequency
    workers=4,            # Parallel processing
    sg=1                  # 1 for skip-gram, 0 for CBOW
)

# Get word vector
vector = model.wv['king']
print("Vector shape:", vector.shape)
print("First 10 dimensions:", vector[:10])

# Find similar words
similar = model.wv.most_similar('king', topn=5)
print("\nWords similar to 'king':")
for word, score in similar:
    print(f"  {word}: {score:.3f}")

# Word arithmetic
result = model.wv.most_similar(
    positive=['king', 'woman'],
    negative=['man'],
    topn=1
)
print(f"\nking - man + woman = {result[0][0]}")

# Similarity
similarity = model.wv.similarity('king', 'queen')
print(f"\nSimilarity(king, queen): {similarity:.3f}")
```

### **Word2Vec from Scratch:**

```python
import numpy as np
from collections import defaultdict

class SimpleWord2Vec:
    def __init__(self, embedding_dim=50, window_size=2, learning_rate=0.01):
        self.embedding_dim = embedding_dim
        self.window_size = window_size
        self.lr = learning_rate
        self.word2idx = {}
        self.idx2word = {}
        
    def build_vocab(self, sentences):
        """Build vocabulary from sentences"""
        vocab = set()
        for sentence in sentences:
            vocab.update(sentence)
        
        self.word2idx = {word: idx for idx, word in enumerate(vocab)}
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}
        self.vocab_size = len(vocab)
        
        # Initialize embeddings
        self.W1 = np.random.randn(self.vocab_size, self.embedding_dim) * 0.01
        self.W2 = np.random.randn(self.embedding_dim, self.vocab_size) * 0.01
    
    def get_training_data(self, sentences):
        """Generate training pairs (target, context)"""
        training_data = []
        
        for sentence in sentences:
            indices = [self.word2idx[word] for word in sentence]
            
            for i, target_idx in enumerate(indices):
                # Get context words
                start = max(0, i - self.window_size)
                end = min(len(indices), i + self.window_size + 1)
                
                for j in range(start, end):
                    if i != j:
                        context_idx = indices[j]
                        training_data.append((target_idx, context_idx))
        
        return training_data
    
    def softmax(self, x):
        """Numerical stable softmax"""
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()
    
    def forward(self, target_idx):
        """Forward pass"""
        # Input to hidden
        h = self.W1[target_idx]
        
        # Hidden to output
        u = np.dot(h, self.W2)
        y_pred = self.softmax(u)
        
        return h, y_pred
    
    def backward(self, target_idx, context_idx, h, y_pred):
        """Backward pass"""
        # Create one-hot vector for context
        y_true = np.zeros(self.vocab_size)
        y_true[context_idx] = 1
        
        # Calculate error
        error = y_pred - y_true
        
        # Update W2
        dW2 = np.outer(h, error)
        self.W2 -= self.lr * dW2
        
        # Update W1
        dW1 = np.dot(error, self.W2.T)
        self.W1[target_idx] -= self.lr * dW1
        
        # Calculate loss
        loss = -np.log(y_pred[context_idx] + 1e-10)
        return loss
    
    def train(self, sentences, epochs=100):
        """Train Word2Vec"""
        self.build_vocab(sentences)
        training_data = self.get_training_data(sentences)
        
        for epoch in range(epochs):
            total_loss = 0
            for target_idx, context_idx in training_data:
                h, y_pred = self.forward(target_idx)
                loss = self.backward(target_idx, context_idx, h, y_pred)
                total_loss += loss
            
            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")
    
    def get_vector(self, word):
        """Get word vector"""
        if word in self.word2idx:
            return self.W1[self.word2idx[word]]
        return None
    
    def most_similar(self, word, topn=5):
        """Find most similar words"""
        if word not in self.word2idx:
            return []
        
        word_vec = self.get_vector(word)
        similarities = {}
        
        for other_word in self.word2idx:
            if other_word != word:
                other_vec = self.get_vector(other_word)
                # Cosine similarity
                sim = np.dot(word_vec, other_vec) / (
                    np.linalg.norm(word_vec) * np.linalg.norm(other_vec)
                )
                similarities[other_word] = sim
        
        # Sort by similarity
        sorted_words = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:topn]

# Example usage
sentences = [
    ['the', 'cat', 'sat', 'on', 'mat'],
    ['the', 'dog', 'sat', 'on', 'log'],
    ['cats', 'and', 'dogs', 'play']
]

model = SimpleWord2Vec(embedding_dim=10, window_size=2)
model.train(sentences, epochs=100)

# Get similar words
similar = model.most_similar('cat', topn=3)
print("\nWords similar to 'cat':")
for word, sim in similar:
    print(f"  {word}: {sim:.3f}")
```

---

## Part 4: Transformers

---

## 17. Transformer Architecture

### **Understanding Transformers:**

```
┌─────────────────────────────────────┐
│      Transformer Architecture      │
├─────────────────────────────────────┤
│                                     │
│  Input Embeddings + Positional     │
│           Encoding                  │
│              ↓                      │
│  ┌───────────────────────┐         │
│  │   Encoder Block x N   │         │
│  │  ┌──────────────────┐│         │
│  │  │ Multi-Head       ││         │
│  │  │ Self-Attention   ││         │
│  │  └────────┬─────────┘│         │
│  │           ↓          │         │
│  │  ┌──────────────────┐│         │
│  │  │ Feed Forward     ││         │
│  │  └────────┬─────────┘│         │
│  └───────────┼──────────┘         │
│              ↓                      │
│  ┌───────────────────────┐         │
│  │   Decoder Block x N   │         │
│  │  ┌──────────────────┐│         │
│  │  │ Masked Multi-Head││         │
│  │  │ Self-Attention   ││         │
│  │  └────────┬─────────┘│         │
│  │  ┌──────────────────┐│         │
│  │  │ Encoder-Decoder  ││         │
│  │  │ Attention        ││         │
│  │  └────────┬─────────┘│         │
│  │  ┌──────────────────┐│         │
│  │  │ Feed Forward     ││         │
│  │  └────────┬─────────┘│         │
│  └───────────┼──────────┘         │
│              ↓                      │
│       Linear + Softmax              │
│              ↓                      │
│           Output                    │
└─────────────────────────────────────┘
```

### **Self-Attention from Scratch:**

```python
import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def self_attention(Q, K, V):
    """
    Self-attention mechanism
    
    Args:
        Q: Query matrix (seq_len, d_k)
        K: Key matrix (seq_len, d_k)
        V: Value matrix (seq_len, d_v)
    
    Returns:
        Output matrix, Attention weights
    """
    d_k = Q.shape[-1]
    
    # Calculate attention scores
    scores = np.matmul(Q, K.T) / np.sqrt(d_k)
    
    # Apply softmax
    attention_weights = softmax(scores)
    
    # Multiply by values
    output = np.matmul(attention_weights, V)
    
    return output, attention_weights

# Example
seq_len = 4
d_k = 8
d_v = 8

# Random Q, K, V matrices
Q = np.random.randn(seq_len, d_k)
K = np.random.randn(seq_len, d_k)
V = np.random.randn(seq_len, d_v)

output, attention = self_attention(Q, K, V)

print("Output shape:", output.shape)
print("Attention weights shape:", attention.shape)
print("\nAttention weights:\n", attention)
```

### **Multi-Head Attention:**

```python
class MultiHeadAttention:
    def __init__(self, d_model, num_heads):
        self.num_heads = num_heads
        self.d_model = d_model
        
        assert d_model % num_heads == 0
        
        self.depth = d_model // num_heads
        
        # Weight matrices
        self.W_q = np.random.randn(d_model, d_model) * 0.01
        self.W_k = np.random.randn(d_model, d_model) * 0.01
        self.W_v = np.random.randn(d_model, d_model) * 0.01
        self.W_o = np.random.randn(d_model, d_model) * 0.01
    
    def split_heads(self, x, batch_size):
        """Split into multiple heads"""
        x = x.reshape(batch_size, -1, self.num_heads, self.depth)
        return x.transpose(0, 2, 1, 3)
    
    def scaled_dot_product_attention(self, q, k, v, mask=None):
        """Calculate attention"""
        matmul_qk = np.matmul(q, k.transpose(0, 1, 3, 2))
        
        # Scale
        dk = k.shape[-1]
        scaled_attention_logits = matmul_qk / np.sqrt(dk)
        
        # Mask (optional)
        if mask is not None:
            scaled_attention_logits += (mask * -1e9)
        
        # Softmax
        attention_weights = softmax(scaled_attention_logits)
        
        output = np.matmul(attention_weights, v)
        
        return output, attention_weights
    
    def forward(self, q, k, v, mask=None):
        """Forward pass"""
        batch_size = q.shape[0]
        
        # Linear projections
        q = np.matmul(q, self.W_q)
        k = np.matmul(k, self.W_k)
        v = np.matmul(v, self.W_v)
        
        # Split heads
        q = self.split_heads(q, batch_size)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)
        
        # Attention
        scaled_attention, attention_weights = self.scaled_dot_product_attention(
            q, k, v, mask
        )
        
        # Concatenate heads
        scaled_attention = scaled_attention.transpose(0, 2, 1, 3)
        concat_attention = scaled_attention.reshape(batch_size, -1, self.d_model)
        
        # Final linear projection
        output = np.matmul(concat_attention, self.W_o)
        
        return output, attention_weights

# Example
d_model = 512
num_heads = 8
seq_len = 10
batch_size = 2

mha = MultiHeadAttention(d_model, num_heads)

# Random input
x = np.random.randn(batch_size, seq_len, d_model)

output, attention = mha.forward(x, x, x)
print("Output shape:", output.shape)
print("Attention shape:", attention.shape)
```

---

## 18. BERT (Bidirectional Encoder Representations from Transformers)

### **Using BERT with Hugging Face:**

```python
from transformers import BertTokenizer, BertModel, BertForSequenceClassification
import torch

# Load pre-trained BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Example text
text = "Natural Language Processing is amazing!"

# Tokenize
inputs = tokenizer(
    text,
    return_tensors='pt',
    padding=True,
    truncation=True,
    max_length=512
)

# Get embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Last hidden state
last_hidden = outputs.last_hidden_state
print("Shape:", last_hidden.shape)  # [batch_size, seq_len, hidden_size]

# [CLS] token embedding (sentence representation)
cls_embedding = last_hidden[:, 0, :]
print("CLS embedding shape:", cls_embedding.shape)  # [batch_size, hidden_size]
```

### **Fine-tuning BERT for Classification:**

```python
from transformers import BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

# Load dataset
dataset = load_dataset('imdb')

# Initialize model
model = BertForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels=2  # Binary classification
)

# Tokenize dataset
def tokenize_function(examples):
    return tokenizer(
        examples['text'],
        padding='max_length',
        truncation=True,
        max_length=512
    )

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=100,
    evaluation_strategy='epoch',
    save_strategy='epoch'
)

# Metrics
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average='weighted')
    return {'accuracy': acc, 'f1': f1}

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'].select(range(1000)),  # Use subset for demo
    eval_dataset=tokenized_datasets['test'].select(range(100)),
    compute_metrics=compute_metrics
)

# Train
trainer.train()

# Evaluate
results = trainer.evaluate()
print("Results:", results)
```

---

## 19. GPT (Generative Pre-trained Transformer)

### **Using GPT-2:**

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set padding token
tokenizer.pad_token = tokenizer.eos_token

# Generate text
def generate_text(prompt, max_length=100, temperature=0.7, top_k=50, top_p=0.95):
    """
    Generate text using GPT-2
    """
    # Encode input
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Example
prompt = "Artificial Intelligence will"
generated = generate_text(prompt, max_length=50)
print(generated)
```

### **Fine-tuning GPT-2:**

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token

# Prepare dataset
def load_dataset_for_training(file_path, tokenizer, block_size=128):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size
    )
    return dataset

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # GPT uses causal LM, not masked LM
)

# Load your custom dataset
train_dataset = load_dataset_for_training('train.txt', tokenizer)

# Training arguments
training_args = TrainingArguments(
    output_dir='./gpt2-finetuned',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    prediction_loss_only=True,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Fine-tune
trainer.train()

# Save
model.save_pretrained('./gpt2-finetuned')
tokenizer.save_pretrained('./gpt2-finetuned')
```

---

## Part 5: NLP Tasks

---

## 22. Text Classification

### **Complete Classification Pipeline:**

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Example: Sentiment classification
class TextClassificationDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    
    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item
    
    def __len__(self):
        return len(self.labels)

# Load data
df = pd.read_csv('sentiment_data.csv')  # columns: 'text', 'label'
texts = df['text'].tolist()
labels = df['label'].tolist()

# Split
train_texts, val_texts, train_labels, val_labels = train_test_split(
    texts, labels, test_size=0.2, random_state=42
)

# Initialize tokenizer and model
model_name = 'distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(set(labels))
)

# Tokenize
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=512)

# Create datasets
train_dataset = TextClassificationDataset(train_encodings, train_labels)
val_dataset = TextClassificationDataset(val_encodings, val_labels)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy='epoch',
    save_strategy='epoch',
    load_best_model_at_end=True,
)

# Define metrics
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
)

# Train
trainer.train()

# Evaluate
results = trainer.evaluate()
print("Evaluation results:", results)

# Predict
def predict(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return predictions.numpy()[0]

# Example
text = "This product is amazing! I love it!"
probs = predict(text)
print(f"Positive: {probs[1]:.2%}, Negative: {probs[0]:.2%}")
```

---

## 23. Named Entity Recognition (NER)

### **NER with Transformers:**

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load NER pipeline
ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple"
)

# Example text
text = "Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976."

# Extract entities
entities = ner_pipeline(text)

print("Named Entities:")
for entity in entities:
    print(f"  {entity['word']}: {entity['entity_group']} (confidence: {entity['score']:.2f})")

# Output:
# Apple Inc.: ORG (confidence: 0.99)
# Steve Jobs: PER (confidence: 0.99)
# Cupertino: LOC (confidence: 0.99)
# California: LOC (confidence: 0.99)
```

### **Training Custom NER Model:**

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
import torch

# Define label mapping
label_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC']
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for label, i in label2id.items()}

# Tokenize and align labels
def tokenize_and_align_labels(examples, tokenizer):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True,
        padding=True,
        max_length=512
    )
    
    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)  # Special tokens
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100)  # Sub-word tokens
            previous_word_idx = word_idx
        
        labels.append(label_ids)
    
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

# Load dataset and train (similar to classification)
```

---

## 24. Sentiment Analysis

### **Production-Ready Sentiment Analysis:**

```python
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch

class SentimentAnalyzer:
    def __init__(self, model_name='distilbert-base-uncased-finetuned-sst-2-english'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.eval()
    
    def analyze(self, text):
        """
        Analyze sentiment of text
        Returns: {'label': 'POSITIVE'/'NEGATIVE', 'score': float}
        """
        inputs = self.tokenizer(
            text,
            return_tensors='pt',
            truncation=True,
            padding=True,
            max_length=512
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        score, predicted = torch.max(probs, dim=1)
        
        label = 'POSITIVE' if predicted.item() == 1 else 'NEGATIVE'
        
        return {
            'label': label,
            'score': score.item(),
            'positive_score': probs[0][1].item(),
            'negative_score': probs[0][0].item()
        }
    
    def analyze_batch(self, texts):
        """Analyze multiple texts at once"""
        results = []
        for text in texts:
            results.append(self.analyze(text))
        return results

# Example usage
analyzer = SentimentAnalyzer()

texts = [
    "This movie was absolutely amazing!",
    "Worst experience ever. Very disappointed.",
    "It was okay, nothing special."
]

for text in texts:
    result = analyzer.analyze(text)
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} (confidence: {result['score']:.2%})")
    print()
```

---

## Part 7: Production

---

## 33. NLP Pipelines

### **Complete NLP Pipeline:**

```python
from typing import List, Dict
import spacy
from transformers import pipeline
import logging

class NLPPipeline:
    """
    Production-ready NLP pipeline
    """
    def __init__(self):
        # Load models
        self.nlp = spacy.load('en_core_web_sm')
        self.sentiment_analyzer = pipeline('sentiment-analysis')
        self.ner_pipeline = pipeline('ner', aggregation_strategy='simple')
        self.summarizer = pipeline('summarization')
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def preprocess(self, text: str) -> str:
        """Clean and normalize text"""
        # Lowercase
        text = text.lower()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def extract_entities(self, text: str) -> List[Dict]:
        """Extract named entities"""
        entities = self.ner_pipeline(text)
        return entities
    
    def analyze_sentiment(self, text: str) -> Dict:
        """Analyze sentiment"""
        result = self.sentiment_analyzer(text)[0]
        return result
    
    def summarize(self, text: str, max_length=130, min_length=30) -> str:
        """Summarize text"""
        if len(text.split()) < min_length:
            return text
        
        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return summary[0]['summary_text']
    
    def get_key_phrases(self, text: str) -> List[str]:
        """Extract key phrases using spaCy"""
        doc = self.nlp(text)
        
        # Extract noun chunks
        noun_chunks = [chunk.text for chunk in doc.noun_chunks]
        
        # Extract noun phrases with adjectives
        key_phrases = []
        for token in doc:
            if token.pos_ in ['NOUN', 'PROPN']:
                phrase = ' '.join([child.text for child in token.subtree])
                key_phrases.append(phrase)
        
        return list(set(noun_chunks + key_phrases))
    
    def process(self, text: str) -> Dict:
        """
        Complete NLP processing pipeline
        """
        self.logger.info("Starting NLP pipeline")
        
        # Preprocess
        clean_text = self.preprocess(text)
        self.logger.info("Preprocessing complete")
        
        # Extract entities
        entities = self.extract_entities(text)
        self.logger.info(f"Found {len(entities)} entities")
        
        # Sentiment analysis
        sentiment = self.analyze_sentiment(text)
        self.logger.info(f"Sentiment: {sentiment['label']}")
        
        # Summarization (if text is long)
        summary = self.summarize(text) if len(text.split()) > 50 else text
        self.logger.info("Summarization complete")
        
        # Key phrases
        key_phrases = self.get_key_phrases(text)
        self.logger.info(f"Extracted {len(key_phrases)} key phrases")
        
        return {
            'original_text': text,
            'clean_text': clean_text,
            'entities': entities,
            'sentiment': sentiment,
            'summary': summary,
            'key_phrases': key_phrases[:10]  # Top 10
        }

# Example usage
pipeline = NLPPipeline()

text = """
Apple Inc. announced today that Steve Jobs, their CEO, will present a new 
product in Cupertino, California next month. The announcement received 
positive feedback from investors and tech enthusiasts worldwide.
"""

result = pipeline.process(text)

print("=== NLP Pipeline Results ===\n")
print(f"Sentiment: {result['sentiment']}")
print(f"\nEntities: {result['entities']}")
print(f"\nSummary: {result['summary']}")
print(f"\nKey Phrases: {result['key_phrases']}")
```

---

## 34. Model Deployment (FastAPI)

### **Complete NLP API:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import torch
from transformers import pipeline
import uvicorn

app = FastAPI(title="NLP API", version="1.0")

# Load models at startup
@app.on_event("startup")
async def load_models():
    global sentiment_pipeline, ner_pipeline, qa_pipeline
    
    sentiment_pipeline = pipeline('sentiment-analysis')
    ner_pipeline = pipeline('ner', aggregation_strategy='simple')
    qa_pipeline = pipeline('question-answering')

# Request/Response models
class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

class Entity(BaseModel):
    word: str
    entity_group: str
    score: float

class QARequest(BaseModel):
    question: str
    context: str

class QAResponse(BaseModel):
    answer: str
    score: float

# Endpoints
@app.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: TextRequest):
    """Analyze text sentiment"""
    try:
        result = sentiment_pipeline(request.text)[0]
        return SentimentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ner", response_model=List[Entity])
async def extract_entities(request: TextRequest):
    """Extract named entities"""
    try:
        entities = ner_pipeline(request.text)
        return [Entity(**entity) for entity in entities]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/qa", response_model=QAResponse)
async def answer_question(request: QARequest):
    """Answer questions based on context"""
    try:
        result = qa_pipeline(
            question=request.question,
            context=request.context
        )
        return QAResponse(
            answer=result['answer'],
            score=result['score']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "models_loaded": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### **Docker Deployment:**

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download models
RUN python -c "from transformers import pipeline; \
    pipeline('sentiment-analysis'); \
    pipeline('ner'); \
    pipeline('question-answering')"

# Copy application
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  nlp-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - TRANSFORMERS_CACHE=/cache
    volumes:
      - model-cache:/cache
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G

volumes:
  model-cache:
```

---

## 📚 Learning Path Summary

### **Week-by-Week Plan:**

```
Week 1: Text Preprocessing
- Cleaning, tokenization, stemming/lemmatization
- BoW, TF-IDF
- Project: Build text preprocessing pipeline

Week 2: Word Embeddings
- Word2Vec, GloVe, FastText
- Semantic similarity
- Project: Word analogy system

Week 3: Sequence Models
- RNN, LSTM, GRU
- Sequence classification
- Project: Sentiment analyzer with LSTM

Week 4-5: Transformers
- Transformer architecture
- BERT, GPT
- Project: Text classifier with BERT

Week 6: NLP Tasks
- NER, QA, Summarization
- Multi-task learning
- Project: Complete NLP pipeline

Week 7: Fine-tuning & LLMs
- Fine-tuning techniques
- Prompt engineering
- Project: Custom chatbot

Week 8: Production
- API development
- Deployment
- Project: Production NLP service
```

---

## 💼 Career Path

**Entry Level:** NLP Engineer ($90K-$120K)
**Mid Level:** Senior NLP Engineer ($130K-$170K)
**Senior Level:** Principal NLP Engineer / Research Scientist ($180K-$250K+)

---

## 🎯 Next Steps

1. **Complete this guide** (8 weeks)
2. **Build 3 NLP projects**
3. **Contribute to Hugging Face**
4. **Apply for NLP roles**
5. **Keep learning latest models**

---

*NLP Complete Guide - From Zero to Hero*
*Master modern NLP from text preprocessing to LLMs*
*6-8 weeks | Career-ready NLP Engineer* 🚀

