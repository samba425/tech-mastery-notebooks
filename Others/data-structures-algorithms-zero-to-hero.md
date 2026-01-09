# Data Structures & Algorithms: Zero to Hero Guide
## Complete Beginner's Journey to DSA Mastery

---

## 📚 Table of Contents

1. [Introduction to DSA](#introduction)
2. [Why Learn DSA?](#why-learn)
3. [Time & Space Complexity](#complexity)
4. [Arrays & Strings](#arrays-strings)
5. [Linked Lists](#linked-lists)
6. [Stacks & Queues](#stacks-queues)
7. [Recursion & Backtracking](#recursion)
8. [Trees](#trees)
9. [Graphs](#graphs)
10. [Hashing](#hashing)
11. [Heaps & Priority Queues](#heaps)
12. [Sorting Algorithms](#sorting)
13. [Searching Algorithms](#searching)
14. [Dynamic Programming](#dynamic-programming)
15. [Greedy Algorithms](#greedy)
16. [Two Pointers & Sliding Window](#two-pointers)
17. [Bit Manipulation](#bit-manipulation)
18. [Advanced Data Structures](#advanced)
19. [Interview Preparation](#interview-prep)
20. [Practice Roadmap](#practice-roadmap)
21. [Visual Diagram Index](#visual-index)

---

## 🎨 Visual Diagram Index {#visual-index}

**This guide contains 60+ detailed ASCII diagrams and visualizations!**

### **Data Structure Visualizations:**

#### **1. Arrays & Strings:**
```
Index:  0    1    2    3    4
Array: [10] [20] [30] [40] [50]
        ↑
     Access in O(1)
```

#### **2. Linked List Structure:**
```
Singly Linked List:
[10 | •]→[20 | •]→[30 | •]→[40 | X]
 Head                        Tail

Doubly Linked List:
null←[1]⇄[2]⇄[3]⇄[4]→null

Circular:
[1]→[2]→[3]→[4]→(back to 1)
```

#### **3. Stack (LIFO):**
```
Push Operations:
|   |     |   |     | 30|     | 40|
|   | →   | 10| →   | 20| →   | 30|
|___| →   |___|     | 10|     | 20|
                    |___|     | 10|
                              |___|
Top ↑
```

#### **4. Queue (FIFO):**
```
Front                        Rear
  10  →  20  →  30  →  40
  
Dequeue ←                → Enqueue
```

#### **5. Binary Tree:**
```
           10           ← Root
         /    \
       5       15       ← Level 1
      / \     /  \
     3   7   12   20    ← Level 2 (Leaves)
```

#### **6. Binary Search Tree:**
```
BST Property: Left < Root < Right

           50
         /    \
       30      70
      /  \    /  \
    20   40  60   80
```

#### **7. Heap (Min-Heap):**
```
      1           ← Minimum at root
    /   \
   3     2
  / \   /
 5   4 8

Parent ≤ Children
```

#### **8. Graph (Adjacency List):**
```
Undirected Graph:
    A ---- B
    |      |
    |      |
    C ---- D

Adjacency List:
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C]
```

#### **9. Trie (Prefix Tree):**
```
Words: "cat", "can", "car"

        root
         |
         c
         |
         a
       / | \
      t  n  r
      *  *  *
      
(* = end of word)
```

#### **10. Fenwick Tree:**
```
Array:     [3, 2, -1, 6, 5, 4, -3, 3]
Index:      1  2   3  4  5  6   7  8

Tree Structure:
        8[1..8]
       /        \
    4[1..4]    12[9..12]
   /     \     
  2[1,2] 6[5,6]
  / \    / \   
 1   3  5   7  

Each node stores sum of a range
```

---

### **Algorithm Visualizations:**

#### **11. Binary Search:**
```
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

Step 1: left=0, right=7, mid=3
        arr[3] = 7 → Found! ✅

        L           M           R
        ↓           ↓           ↓
        1   3   5   7   9  11  13  15
```

#### **12. Bubble Sort Animation:**
```
[5, 3, 8, 4, 2]

Pass 1:
[3, 5, 8, 4, 2] (5 > 3, swap)
[3, 5, 8, 4, 2] (5 < 8, no swap)
[3, 5, 4, 8, 2] (8 > 4, swap)
[3, 5, 4, 2, 8] (8 > 2, swap) ← 8 in position

Pass 2:
[3, 4, 5, 2, 8] → continues...

Final: [2, 3, 4, 5, 8] ✅
```

#### **13. Merge Sort Tree:**
```
                [5, 3, 8, 4, 2]
                /              \
        [5, 3, 8]              [4, 2]
        /       \              /    \
    [5, 3]     [8]          [4]    [2]
    /   \                            
  [5]   [3]                          

Merge up:
[3, 5] ← merge [5], [3]
[3, 5, 8] ← merge [3, 5], [8]
[2, 4] ← merge [4], [2]
[2, 3, 4, 5, 8] ← merge [3, 5, 8], [2, 4]
```

#### **14. DFS vs BFS:**
```
Tree:
        1
       / \
      2   3
     / \   \
    4   5   6

DFS (Preorder): 1 → 2 → 4 → 5 → 3 → 6
    Go deep first!
    
    1
    ↓
    2
   ↙↓
  4  5

BFS (Level Order): 1 → 2 → 3 → 4 → 5 → 6
    Go wide first!
    
    Level 0: [1]
    Level 1: [2, 3]
    Level 2: [4, 5, 6]
```

#### **15. Dijkstra's Algorithm:**
```
Graph:
    A --4--> B
    |        |
    2        5
    |        |
    v        v
    C --8--> D --2--> E

Starting from A:

Step 1: A=0, visit A
  Update: B=4, C=2

Step 2: Visit C (smallest)
  Update: D=10, E=12

Step 3: Visit B
  Update: D=9 (better!)

Final distances:
A: 0
B: 4
C: 2
D: 9
E: 11
```

#### **16. Two Pointers Pattern:**
```
Finding pair with target sum:

arr = [1, 2, 3, 4, 5, 6], target = 7

    L                 R
    ↓                 ↓
    1   2   3   4   5   6
    
1 + 6 = 7 ✅ Found!

If sum < target: L++
If sum > target: R--
```

#### **17. Sliding Window:**
```
Find max sum of subarray size k=3:

arr = [1, 3, 2, 5, 1, 2]

Window 1: [1, 3, 2] = 6
         ↓ ↓ ↓

Window 2: [3, 2, 5] = 10 ✅
           ↓ ↓ ↓

Window 3: [2, 5, 1] = 8
             ↓ ↓ ↓

Max = 10
```

#### **18. Backtracking Tree (Permutations):**
```
Generate permutations of [1,2,3]:

                    []
         /          |          \
       [1]         [2]         [3]
      /   \       /   \       /   \
   [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
     |     |     |     |     |     |
 [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]

Each path = one permutation
```

#### **19. Dynamic Programming Table (LCS):**
```
Longest Common Subsequence
text1 = "abcde", text2 = "ace"

    ""  a  c  e
""   0  0  0  0
a    0  1  1  1
b    0  1  1  1
c    0  1  2  2
d    0  1  2  2
e    0  1  2  3  ← Answer

LCS = "ace" with length 3
```

#### **20. Kadane's Algorithm (Max Subarray):**
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum tracking:
-2 → 1 (restart)
 1 → 1
-2 (1-3) → 4 (restart)
 4 → 4
 3 (4-1) → 3
 5 (3+2) → 5
 6 (5+1) → 6 ← max_sum ✅
 1 (6-5) → 1
 5 (1+4) → 5

Subarray: [4, -1, 2, 1] = 6
```

---

### **Problem-Solving Flow Diagrams:**

#### **21. Pattern Recognition Flowchart:**
```
START: Got a problem
    |
    v
Is it Array/String?
    |
    ├─YES─→ Need subarray/substring?
    |           |
    |           ├─Contiguous? → SLIDING WINDOW
    |           └─Not contiguous? → TWO POINTERS
    |
    ├─YES─→ Need pairs/triplets?
    |           |
    |           ├─Sorted? → TWO POINTERS
    |           └─Unsorted? → HASH MAP
    |
    v
Is it Tree?
    |
    ├─YES─→ Level order? → BFS
    |       Path problems? → DFS
    |
    v
Is it Graph?
    |
    ├─YES─→ Shortest path? → BFS/Dijkstra
    |       Connected? → UNION FIND
    |
    v
Need optimal solution?
    |
    ├─Overlapping subproblems? → DP
    └─Greedy choice? → GREEDY
```

#### **22. Binary Search Decision Tree:**
```
Binary Search Variations:

                Binary Search
                /           \
        Find Element    Find Boundary
            |               /        \
        Standard    First Occurrence  Last Occurrence
                            |              |
                    Template with      Template with
                     right = mid       left = mid + 1
```

#### **23. DP Problem Classification:**
```
DP Problem Types:

├─ 1D DP
│  ├─ Fibonacci
│  ├─ Climbing Stairs
│  └─ House Robber
│
├─ 2D DP
│  ├─ Grid Path (Unique Paths)
│  ├─ LCS (Longest Common Subsequence)
│  └─ Edit Distance
│
├─ Knapsack Type
│  ├─ 0/1 Knapsack
│  ├─ Unbounded Knapsack
│  └─ Subset Sum
│
├─ String DP
│  ├─ Palindrome Problems
│  ├─ Word Break
│  └─ Regex Matching
│
└─ Advanced
   ├─ State Machine DP
   ├─ Bitmask DP
   └─ DP on Trees
```

#### **24. Recursion Call Stack:**
```
fibonacci(5)
    |
    ├─ fibonacci(4)
    |      |
    |      ├─ fibonacci(3)
    |      |      |
    |      |      ├─ fibonacci(2) → 1
    |      |      └─ fibonacci(1) → 1
    |      |
    |      └─ fibonacci(2) → 1
    |
    └─ fibonacci(3)
           |
           ├─ fibonacci(2) → 1
           └─ fibonacci(1) → 1

Stack depth = 5 levels
Time without memo: O(2^n)
```

#### **25. Complexity Comparison Graph:**
```
Time Complexity Growth:

Operations for n=100:

O(1)       →  1       ████
O(log n)   →  7       ████████
O(n)       →  100     ████████████████████
O(n log n) →  664     ████████████████████████████
O(n²)      →  10,000  ████████████████████████████████████
O(2ⁿ)      →  💀      (Age of universe)

         Fast ←──────────────────→ Slow
```

---

### **Interview Flow Diagrams:**

#### **26. Problem-Solving Framework:**
```
┌─────────────────────────────────────┐
│ 1. CLARIFY (2-3 min)                │
│    • Ask questions                   │
│    • Understand I/O                  │
│    • Check constraints              │
└──────────────┬──────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 2. EXAMPLES (3-4 min)                │
│    • Walk through 2-3 cases          │
│    • Include edge cases              │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 3. BRUTE FORCE (2-3 min)             │
│    • State naive solution            │
│    • Analyze complexity              │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 4. OPTIMIZE (5-7 min)                │
│    • Look for patterns               │
│    • Consider data structures        │
│    • Draw diagrams                   │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 5. CODE (15 min)                     │
│    • Write clean code                │
│    • Handle edge cases               │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 6. TEST (5-7 min)                    │
│    • Walk through examples           │
│    • Check edge cases                │
│    • Fix bugs                        │
└──────────────┬───────────────────────┘
               ↓
┌──────────────────────────────────────┐
│ 7. ANALYZE (2 min)                   │
│    • State time complexity           │
│    • State space complexity          │
└──────────────────────────────────────┘
```

#### **27. Time Management Diagram:**
```
45-Minute Interview Timeline:

0─────────3────────7─────10───────17────────32───────40─43─45
│         │        │      │        │         │        │  │  │
│ Clarify │Examples│Brute │Optimize│  Code   │  Test  │A│Q │
│         │        │Force │        │         │        │n│u │
│         │        │      │        │         │        │a│e │
│         │        │      │        │         │        │l│s │
│         │        │      │        │         │        │y│t │
└─────────┴────────┴──────┴────────┴─────────┴────────┴─┴──┘
   3min     4min    3min   7min     15min     8min   3m 2m

⚠️ Warning zones:
• 20+ min and not coding → Too slow!
• 35+ min and code not done → Rush mode!
```

---

### **Master Theorem Visualization:**

#### **28. Master Theorem Decision Tree:**
```
T(n) = aT(n/b) + f(n)
    |
    ├─ Calculate: c = log_b(a)
    |
    ├─ Compare f(n) with n^c
    |
    ├─ Case 1: f(n) = O(n^k), k < c
    │         → T(n) = Θ(n^c)
    │         Example: T(n) = 8T(n/2) + n²
    │         → O(n³)
    |
    ├─ Case 2: f(n) = Θ(n^c log^k n)
    │         → T(n) = Θ(n^c log^(k+1) n)
    │         Example: T(n) = 2T(n/2) + n
    │         → O(n log n) ✅ Merge Sort
    |
    └─ Case 3: f(n) = Ω(n^k), k > c
              → T(n) = Θ(f(n))
              Example: T(n) = 2T(n/2) + n²
              → O(n²)
```

---

### **Matrix Operations:**

#### **29. Spiral Matrix Traversal:**
```
Matrix:
┌─────────────┐
│ 1 → 2 → 3 │ ① Right
│           ↓ │
│ 4   5   6 │ ② Down
│ ↑       ↓ │
│ 7 ← 8 ← 9 │ ③ Left, ④ Up
└───────────┘

Boundaries move inward:
top++, right--, bottom--, left++
```

#### **30. Matrix Rotation 90°:**
```
Original:       Transpose:      Reverse Rows:
[1, 2, 3]      [1, 4, 7]       [7, 4, 1]
[4, 5, 6]  →   [2, 5, 8]   →   [8, 5, 2]
[7, 8, 9]      [3, 6, 9]       [9, 6, 3]

Step 1: Swap across diagonal
Step 2: Reverse each row
Result: 90° clockwise! ✅
```

---

## 📋 **Diagram Summary:**

### **Total Visual Elements: 60+ detailed diagrams**

**By Category:**
- 🏗️ Data Structure Diagrams: 10
- ⚙️ Algorithm Visualizations: 10
- 🎯 Problem-Solving Flows: 7
- 📊 Complexity Charts: 3
- 🎤 Interview Guides: 2
- 🧮 Math/Theory: 3
- 📐 Matrix Operations: 5
- 🔍 Search Patterns: 5
- 🌳 Tree Diagrams: 5
- 🎨 Miscellaneous: 10+

**Diagram Types:**
- ✅ ASCII Art Structures
- ✅ Step-by-step Animations
- ✅ Flow Charts
- ✅ Decision Trees
- ✅ Comparison Tables
- ✅ Timeline Diagrams
- ✅ Recursion Trees
- ✅ State Machines
- ✅ Grid Visualizations
- ✅ Graph Representations

**Every major concept has:**
- 📝 Written explanation
- 🎨 Visual diagram
- 💻 Code example
- 🔍 Step-by-step trace
- ✅ Verification/testing

---

*All diagrams are text-based (ASCII) for maximum compatibility!*
*Works in any text editor, terminal, or markdown viewer!*

---

## 🎯 Introduction to DSA {#introduction}

**Data Structures & Algorithms (DSA)** is the foundation of computer science and software engineering.

### What are Data Structures?

**Data Structures** are ways to organize and store data efficiently.

Think of it like organizing your closet:
- 🗄️ **Array** = Drawers in a row (indexed storage)
- 📚 **Stack** = Pile of books (last in, first out)
- 🎫 **Queue** = Line at ticket counter (first in, first out)
- 🌳 **Tree** = Family tree (hierarchical)
- 🗺️ **Graph** = Road map (connections)

### What are Algorithms?

**Algorithms** are step-by-step procedures to solve problems.

Like following a recipe:
```
Recipe for Tea:
1. Boil water
2. Add tea leaves
3. Add sugar
4. Strain
5. Serve

This is an ALGORITHM! 🍵
```

---

## 💡 Why Learn DSA? {#why-learn}

### For Careers:

✅ **Tech Interviews** - Google, Microsoft, Amazon, Meta all test DSA  
✅ **Problem Solving** - Build logical thinking  
✅ **Code Efficiency** - Write faster, optimized code  
✅ **System Design** - Foundation for scalable systems  
✅ **Higher Salary** - DSA skills = Better pay! 💰  

### Real-World Applications:

| Data Structure | Real-World Use |
|----------------|----------------|
| **Arrays** | Image pixels, sensor data |
| **Linked Lists** | Browser history, music playlists |
| **Stacks** | Undo/Redo, browser back button |
| **Queues** | Print job queue, message queue |
| **Trees** | File system, DOM in HTML |
| **Graphs** | Social networks, Google Maps |
| **Hash Tables** | Database indexing, caching |
| **Heaps** | Priority scheduling, Dijkstra |

---

## ⏱️ Time & Space Complexity {#complexity}

### Big O Notation - How Fast is Your Code?

**Big O** measures how performance changes as input size grows.

### Common Time Complexities (Best to Worst):

```
O(1)         - Constant     🚀 Fastest
O(log n)     - Logarithmic  ⚡ Very Fast
O(n)         - Linear       ✅ Good
O(n log n)   - Linearithmic 👍 Acceptable
O(n²)        - Quadratic    ⚠️ Slow
O(n³)        - Cubic        🐌 Very Slow
O(2ⁿ)        - Exponential  💀 Extremely Slow
O(n!)        - Factorial    ☠️ Impossibly Slow
```

### Visual Comparison:

```
Time taken for n=100:

O(1)       →  1 operation       ████
O(log n)   →  7 operations      ████████
O(n)       →  100 operations    ████████████████████
O(n log n) →  664 operations    █████████████████████████████
O(n²)      →  10,000 ops        ████████████████████████████████████████████
O(2ⁿ)      →  1.27×10³⁰ ops     💀 (Age of universe operations)
```

### Examples:

#### O(1) - Constant Time
```python
def get_first_element(arr):
    return arr[0]  # Always 1 operation

# Same time for 10 items or 1 million items!
```

#### O(n) - Linear Time
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:           # Loop through all n elements
        if num > max_val:
            max_val = num
    return max_val

# 100 items → 100 operations
# 1000 items → 1000 operations
```

#### O(n²) - Quadratic Time
```python
def print_pairs(arr):
    for i in arr:              # n iterations
        for j in arr:          # n iterations for each i
            print(i, j)        # n × n = n²

# 10 items → 100 operations
# 100 items → 10,000 operations
```

#### O(log n) - Logarithmic Time
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 1000 items → ~10 operations (dividing by 2 each time)
# 1,000,000 items → ~20 operations
```

### Space Complexity:

**Space Complexity** measures memory usage.

```python
# O(1) Space - Constant
def sum_array(arr):
    total = 0              # 1 variable
    for num in arr:
        total += num
    return total

# O(n) Space - Linear
def create_copy(arr):
    new_arr = []
    for num in arr:        # Creating new array of size n
        new_arr.append(num)
    return new_arr
```

---

## 📊 Arrays & Strings {#arrays-strings}

### Arrays - The Foundation

**Array** = Collection of elements stored in contiguous memory.

```
Index:  0    1    2    3    4
Array: [10] [20] [30] [40] [50]
       ↑
    Access in O(1) time!
```

### Array Operations:

| Operation | Time Complexity | Example |
|-----------|----------------|---------|
| **Access** | O(1) | `arr[3]` |
| **Search** | O(n) | Find 30 in array |
| **Insert (end)** | O(1) | Add to last position |
| **Insert (middle)** | O(n) | Shift elements |
| **Delete (end)** | O(1) | Remove last |
| **Delete (middle)** | O(n) | Shift elements |

### Common Array Problems:

---

#### Problem 1: **Two Sum** (Leetcode #1)

**Problem:** Find two numbers that add up to target.

```python
def two_sum(nums, target):
    """
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
    """
    
    # Approach 1: Brute Force - O(n²)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    # Approach 2: Hash Map - O(n) ✅ Better!
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

**Visualization:**
```
nums = [2, 7, 11, 15], target = 9

Step 1: num = 2, complement = 7
        seen = {2: 0}

Step 2: num = 7, complement = 2
        2 is in seen! ✅
        Return [0, 1]
```

---

#### Problem 2: **Maximum Subarray** (Kadane's Algorithm)

**Problem:** Find contiguous subarray with largest sum.

```python
def max_subarray(nums):
    """
    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6 (subarray [4, -1, 2, 1])
    """
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend existing subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example:
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
```

**Step-by-step:**
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

i=1: current=-2+1=-1, but 1 is better → current=1, max=1
i=2: current=1-3=-2, better to take 1 → current=-2, max=1
i=3: current=-2+4=2, but 4 is better → current=4, max=4
i=4: current=4-1=3 → current=3, max=4
i=5: current=3+2=5 → current=5, max=5
i=6: current=5+1=6 → current=6, max=6 ✅
i=7: current=6-5=1 → current=1, max=6
i=8: current=1+4=5 → current=5, max=6

Answer: 6
```

---

#### Problem 3: **Rotate Array**

```python
def rotate(nums, k):
    """
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    """
    n = len(nums)
    k = k % n  # Handle k > n
    
    # Reverse entire array
    nums.reverse()
    # Reverse first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse remaining elements
    nums[k:] = reversed(nums[k:])
    
    return nums

# Example:
print(rotate([1,2,3,4,5,6,7], 3))  # [5,6,7,1,2,3,4]
```

**Visualization:**
```
Original: [1, 2, 3, 4, 5, 6, 7]

Step 1 - Reverse all:
[7, 6, 5, 4, 3, 2, 1]

Step 2 - Reverse first k=3:
[5, 6, 7, 4, 3, 2, 1]

Step 3 - Reverse remaining:
[5, 6, 7, 1, 2, 3, 4] ✅
```

---

### Strings - Arrays of Characters

Strings are immutable in most languages!

#### Problem 4: **Valid Palindrome**

```python
def is_palindrome(s):
    """
    Input: "A man, a plan, a canal: Panama"
    Output: True
    """
    # Clean string: only alphanumeric, lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two pointers
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
```

---

#### Problem 5: **Longest Substring Without Repeating Characters**

```python
def length_of_longest_substring(s):
    """
    Input: "abcabcbb"
    Output: 3 (substring "abc")
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character repeats, remove from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example:
print(length_of_longest_substring("abcabcbb"))  # 3
```

**Visualization:**
```
s = "abcabcbb"

Window: [a]bc → length=1
Window: [ab]c → length=2
Window: [abc]abcbb → length=3 ✅
Window: abc[a] → 'a' repeats! Remove from left
Window: bc[a]bcbb → length=3
Window: bca[b] → 'b' repeats! Remove...
... and so on

Max length = 3
```

---

## 🔗 Linked Lists {#linked-lists}

### What is a Linked List?

A sequence of nodes where each node contains data and a reference to the next node.

```
Single Linked List:

[10 | •]→[20 | •]→[30 | •]→[40 | X]
 Head                        Tail
 
Each box is a Node:
- Left side: Data
- Right side: Pointer to next node
- X = null (end of list)
```

### Types of Linked Lists:

#### 1. **Singly Linked List**
```
[1]→[2]→[3]→[4]→null
```

#### 2. **Doubly Linked List**
```
null←[1]⇄[2]⇄[3]⇄[4]→null
```

#### 3. **Circular Linked List**
```
[1]→[2]→[3]→[4]→(back to 1)
```

### Node Implementation:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("null")

# Usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 → 20 → 30 → null
```

### Linked List Operations:

| Operation | Time | Space |
|-----------|------|-------|
| **Access** | O(n) | O(1) |
| **Search** | O(n) | O(1) |
| **Insert at head** | O(1) | O(1) |
| **Insert at tail** | O(n) | O(1) |
| **Delete at head** | O(1) | O(1) |
| **Delete at tail** | O(n) | O(1) |

### Common Linked List Problems:

---

#### Problem 6: **Reverse Linked List**

```python
def reverse_list(head):
    """
    Input: 1→2→3→4→5→null
    Output: 5→4→3→2→1→null
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    return prev  # New head

# Visualization:
"""
Initial: 1→2→3→4→5→null

Step 1: null←1  2→3→4→5→null
        prev  curr

Step 2: null←1←2  3→4→5→null
              prev curr

Step 3: null←1←2←3  4→5→null
                 prev curr

Continue until current is null...
"""
```

---

#### Problem 7: **Detect Cycle in Linked List** (Floyd's Algorithm)

```python
def has_cycle(head):
    """
    Floyd's Tortoise and Hare Algorithm
    """
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps
        
        if slow == fast:           # They met!
            return True
    
    return False

# Visualization:
"""
No Cycle:
1→2→3→4→5→null
Slow and Fast never meet

With Cycle:
1→2→3→4→5
     ↑     ↓
     8←7←6

Slow: 1→2→3→4→5→6→7→8→3→4...
Fast: 1→3→5→7→3→5→7→3...
Eventually they meet! ✅
"""
```

---

#### Problem 8: **Merge Two Sorted Lists**

```python
def merge_two_lists(l1, l2):
    """
    Input: l1 = 1→2→4, l2 = 1→3→4
    Output: 1→1→2→3→4→4
    """
    dummy = Node(0)
    current = dummy
    
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next

# Step by step:
"""
l1: 1→2→4
l2: 1→3→4

Compare 1 and 1 → Take l1's 1 → Result: 1
Compare 2 and 1 → Take l2's 1 → Result: 1→1
Compare 2 and 3 → Take l1's 2 → Result: 1→1→2
Compare 4 and 3 → Take l2's 3 → Result: 1→1→2→3
Compare 4 and 4 → Take l1's 4 → Result: 1→1→2→3→4
Attach l2's 4 → Result: 1→1→2→3→4→4 ✅
"""
```

---

## 📚 Stacks & Queues {#stacks-queues}

### Stack - LIFO (Last In, First Out)

Like a stack of plates! 🍽️

```
Operations:
Push 10:  |   |     |   |     | 30|     | 40|
          |   | →   | 10| →   | 20| →   | 30|
          |___| →   |___|     | 10|     | 20|
                              |___|     | 10|
                                        |___|
                                        
Pop:  Remove 40 (top element)
Peek: Look at 40 without removing
```

### Stack Implementation:

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())   # 30
print(stack.peek())  # 20
```

### Stack Problems:

---

#### Problem 9: **Valid Parentheses**

```python
def is_valid(s):
    """
    Input: "({[]})"
    Output: True
    
    Input: "({[})"
    Output: False
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

# Visualization:
"""
s = "({[]})"

char='(' → Push → Stack: ['(']
char='{' → Push → Stack: ['(', '{']
char='[' → Push → Stack: ['(', '{', '[']
char=']' → Pop '[' → Matches! → Stack: ['(', '{']
char='}' → Pop '{' → Matches! → Stack: ['(']
char=')' → Pop '(' → Matches! → Stack: []

Stack empty → Valid! ✅
"""
```

---

#### Problem 10: **Evaluate Reverse Polish Notation**

```python
def eval_rpn(tokens):
    """
    Input: ["2", "1", "+", "3", "*"]
    Output: 9 (because (2 + 1) * 3 = 9)
    """
    stack = []
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]

# Example:
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
```

---

### Queue - FIFO (First In, First Out)

Like a line at a ticket counter! 🎫

```
Enqueue (Add):
Front                        Rear
  10  →  20  →  30  →  40

Dequeue (Remove):
Remove 10 from front
Front           Rear
  20  →  30  →  40
```

### Queue Implementation:

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())  # 10 (first in, first out)
```

---

## 🔄 Recursion & Backtracking {#recursion}

### What is Recursion?

**Recursion** = Function calling itself!

```python
def countdown(n):
    if n == 0:              # Base case
        print("Blast off! 🚀")
        return
    print(n)
    countdown(n - 1)        # Recursive call

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Blast off! 🚀
```

### Recursion Visualization:

```
countdown(3)
    ↓
    print(3)
    countdown(2)
        ↓
        print(2)
        countdown(1)
            ↓
            print(1)
            countdown(0)
                ↓
                print("Blast off!")
                return
            ← return
        ← return
    ← return
```

### Classic Recursion Problems:

---

#### Problem 11: **Factorial**

```python
def factorial(n):
    """
    5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Visualization:
"""
factorial(5)
= 5 × factorial(4)
= 5 × (4 × factorial(3))
= 5 × (4 × (3 × factorial(2)))
= 5 × (4 × (3 × (2 × factorial(1))))
= 5 × (4 × (3 × (2 × 1)))
= 5 × (4 × (3 × 2))
= 5 × (4 × 6)
= 5 × 24
= 120 ✅
"""
```

---

#### Problem 12: **Fibonacci**

```python
def fibonacci(n):
    """
    Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    Each number is sum of previous two
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Better approach with memoization:
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Visualization:
"""
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /     \      /    \
        fib(3)  fib(2) fib(2) fib(1)
        /   \    /  \   /  \
    fib(2) fib(1) ... ... ...
    
Without memo: O(2ⁿ) - Very slow!
With memo: O(n) - Fast! ✅
"""
```

---

#### Problem 13: **Generate All Permutations** (Backtracking)

```python
def permute(nums):
    """
    Input: [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    """
    result = []
    
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()  # Backtrack!
    
    backtrack([], nums)
    return result

# Visualization:
"""
Start: []
       ├── Choose 1: [1]
       │   ├── Choose 2: [1,2]
       │   │   └── Choose 3: [1,2,3] ✅
       │   └── Choose 3: [1,3]
       │       └── Choose 2: [1,3,2] ✅
       ├── Choose 2: [2]
       │   └── ... (similar)
       └── Choose 3: [3]
           └── ... (similar)
"""
```

---

## 🌳 Trees {#trees}

### Binary Tree Structure:

```
           10           ← Root
         /    \
       5       15       ← Level 1
      / \     /  \
     3   7   12   20    ← Level 2 (Leaves)
```

### Binary Tree Node:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Tree Traversals:

#### 1. **Inorder (Left → Root → Right)**

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# For above tree: [3, 5, 7, 10, 12, 15, 20]
```

#### 2. **Preorder (Root → Left → Right)**

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# For above tree: [10, 5, 3, 7, 15, 12, 20]
```

#### 3. **Postorder (Left → Right → Root)**

```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# For above tree: [3, 7, 5, 12, 20, 15, 10]
```

#### 4. **Level Order (BFS)**

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# For above tree: [[10], [5, 15], [3, 7, 12, 20]]
```

### Binary Search Tree (BST):

**Property:** Left < Root < Right

```
BST Example:
           50
         /    \
       30      70
      /  \    /  \
    20   40  60   80

For any node:
- All left subtree values < node value
- All right subtree values > node value
```

#### Problem 14: **Validate BST**

```python
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))
```

#### Problem 15: **Lowest Common Ancestor**

```python
def lowest_common_ancestor(root, p, q):
    """
    Find LCA of two nodes in BST
    
    Example:     6
               /   \
              2     8
             / \   / \
            0   4 7   9
               / \
              3   5
    
    LCA(2, 8) = 6
    LCA(2, 4) = 2
    """
    if not root:
        return None
    
    # Both nodes in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # Both nodes in right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Split point - this is LCA!
    return root
```

#### Problem 16: **Maximum Depth**

```python
def max_depth(root):
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

# Visualization:
"""
        3         ← Depth 1
       / \
      9   20      ← Depth 2
         /  \
        15   7    ← Depth 3

max_depth = 3
"""
```

---

## 🗺️ Graphs {#graphs}

### What is a Graph?

Collection of **nodes (vertices)** connected by **edges**.

```
Undirected Graph:
    A ---- B
    |      |
    |      |
    C ---- D

Directed Graph (Digraph):
    A --→ B
    ↑     ↓
    |     |
    C ←-- D
```

### Graph Representations:

#### 1. **Adjacency List** (Most Common)

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

#### 2. **Adjacency Matrix**

```python
#      A  B  C  D
#   A [0, 1, 1, 0]
#   B [1, 0, 0, 1]
#   C [1, 0, 0, 1]
#   D [0, 1, 1, 0]

matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```

### Graph Traversals:

#### 1. **DFS (Depth-First Search)** - Go Deep!

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Example:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')  # Output: A B D E F C
```

**Visualization:**
```
Start at A
    A
   / \
  B   C
 / \   \
D   E   F

DFS path: A → B → D (backtrack) → E → F (backtrack) → C
```

#### 2. **BFS (Breadth-First Search)** - Go Wide!

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited

bfs(graph, 'A')  # Output: A B C D E F
```

**Visualization:**
```
Level 0: A
Level 1: B, C
Level 2: D, E, F

BFS visits level by level!
```

### Graph Problems:

#### Problem 17: **Number of Islands**

```python
def num_islands(grid):
    """
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3 (three islands)
    """
    if not grid:
        return 0
    
    def dfs(i, j):
        if (i < 0 or i >= len(grid) or 
            j < 0 or j >= len(grid[0]) or 
            grid[i][j] != '1'):
            return
        
        grid[i][j] = '0'  # Mark as visited
        
        # Visit all 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                islands += 1
    
    return islands
```

#### Problem 18: **Clone Graph**

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    if not node:
        return None
    
    clones = {}
    
    def dfs(node):
        if node in clones:
            return clones[node]
        
        clone = Node(node.val)
        clones[node] = clone
        
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)
```

---

## #️⃣ Hashing {#hashing}

### Hash Table (Dictionary/Map)

Maps **keys** to **values** in O(1) time!

```
Hash Table:
Key → Hash Function → Index → Value

"apple" → hash("apple") → 3 → $1.50
"banana" → hash("banana") → 7 → $0.75
```

### Hash Set - Only Keys

```python
# Add, search, delete in O(1) average time
seen = set()
seen.add(10)
seen.add(20)
print(10 in seen)  # True, O(1)
```

### Hash Map Problems:

#### Problem 19: **Group Anagrams**

```python
def group_anagrams(strs):
    """
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    from collections import defaultdict
    
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort word to get key
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    
    return list(anagrams.values())

# Example:
# "eat" → sorted → "aet" → key
# "tea" → sorted → "aet" → same key!
# "bat" → sorted → "abt" → different key
```

#### Problem 20: **LRU Cache**

```python
from collections import OrderedDict

class LRUCache:
    """
    Least Recently Used Cache
    """
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move to end (mark as recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)

# Usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)      # returns 1
cache.put(3, 3)   # evicts key 2
cache.get(2)      # returns -1 (not found)
```

---

## 🏔️ Heaps & Priority Queues {#heaps}

### What is a Heap?

Special tree where parent is always smaller (min-heap) or larger (max-heap) than children.

```
Min Heap:              Max Heap:
      1                      100
    /   \                  /     \
   3     2                50      80
  / \   /                /  \    /
 5   4 8               20   40  60

Parent ≤ Children     Parent ≥ Children
```

### Heap Implementation (Python):

```python
import heapq

# Min Heap (default in Python)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heap)              # [1, 5, 3]
print(heapq.heappop(heap))  # 1 (smallest)

# Max Heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

print(-heapq.heappop(max_heap))  # 5 (largest)
```

### Heap Problems:

#### Problem 21: **Kth Largest Element**

```python
def find_kth_largest(nums, k):
    """
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    """
    import heapq
    
    # Use min heap of size k
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

# Alternative: use max heap
def find_kth_largest_v2(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

#### Problem 22: **Merge K Sorted Lists**

```python
def merge_k_lists(lists):
    """
    Input: [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    """
    import heapq
    
    heap = []
    
    # Add first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

---

## 🔄 Sorting Algorithms {#sorting}

### Comparison of Sorting Algorithms:

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### 1. Bubble Sort - Simple but Slow

```python
def bubble_sort(arr):
    """
    Repeatedly swap adjacent elements if they're in wrong order
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

# Visualization:
"""
[5, 3, 8, 4, 2]

Pass 1:
[3, 5, 8, 4, 2] (5 > 3, swap)
[3, 5, 8, 4, 2] (5 < 8, no swap)
[3, 5, 4, 8, 2] (8 > 4, swap)
[3, 5, 4, 2, 8] (8 > 2, swap)

Pass 2:
[3, 4, 5, 2, 8]
...continues...

Final: [2, 3, 4, 5, 8]
"""
```

### 2. Quick Sort - Fast and Popular

```python
def quick_sort(arr):
    """
    Pick pivot, partition around it, recursively sort
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Visualization:
"""
[5, 3, 8, 4, 2]
Pivot = 4

Left (< 4): [3, 2]
Middle (= 4): [4]
Right (> 4): [5, 8]

Recursively sort:
Left: [2, 3]
Right: [5, 8]

Result: [2, 3] + [4] + [5, 8] = [2, 3, 4, 5, 8]
"""
```

### 3. Merge Sort - Guaranteed O(n log n)

```python
def merge_sort(arr):
    """
    Divide array, recursively sort, merge sorted halves
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Visualization:
"""
[5, 3, 8, 4, 2]

Split:
[5, 3, 8] [4, 2]
[5] [3, 8] [4] [2]
[5] [3] [8] [4] [2]

Merge:
[5] + [3] = [3, 5]
[3, 5] + [8] = [3, 5, 8]
[4] + [2] = [2, 4]
[3, 5, 8] + [2, 4] = [2, 3, 4, 5, 8]
"""
```

---

## 🔍 Searching Algorithms {#searching}

### 1. Linear Search - O(n)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Check every element one by one
# Works on unsorted arrays
```

### 2. Binary Search - O(log n) ⚡

```python
def binary_search(arr, target):
    """
    Only works on SORTED arrays!
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Visualization:
"""
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

Step 1: left=0, right=7, mid=3
        arr[3] = 7 → Found! ✅

If target = 11:
Step 1: left=0, right=7, mid=3
        arr[3] = 7 < 11 → search right half
Step 2: left=4, right=7, mid=5
        arr[5] = 11 → Found! ✅
"""
```

### Binary Search Variations:

#### Problem 23: **Find First and Last Position**

```python
def search_range(nums, target):
    """
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    """
    def find_first():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def find_last():
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    return [find_first(), find_last()]
```

---

## 🎯 Dynamic Programming {#dynamic-programming}

### What is Dynamic Programming?

**DP** = Recursion + Memoization (storing results)

**Key Insight:** Break problem into subproblems, solve once, reuse results!

### DP Approaches:

1. **Top-Down (Memoization)** - Recursion + cache
2. **Bottom-Up (Tabulation)** - Iterative, fill table

### Classic DP Problems:

#### Problem 24: **Climbing Stairs**

```python
def climb_stairs(n):
    """
    You can climb 1 or 2 steps at a time.
    How many ways to reach top?
    
    Input: n = 3
    Output: 3 (1+1+1, 1+2, 2+1)
    """
    # Approach 1: Recursion (Slow - O(2ⁿ))
    def climb_recursive(n):
        if n <= 2:
            return n
        return climb_recursive(n-1) + climb_recursive(n-2)
    
    # Approach 2: DP (Fast - O(n))
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Visualization:
"""
n=1: 1 way (1)
n=2: 2 ways (1+1, 2)
n=3: 3 ways (1+1+1, 1+2, 2+1)
n=4: 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)

Pattern: dp[n] = dp[n-1] + dp[n-2]
(Same as Fibonacci!)
"""
```

#### Problem 25: **Coin Change**

```python
def coin_change(coins, amount):
    """
    Find minimum coins needed to make amount
    
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 (5 + 5 + 1)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Visualization:
"""
coins = [1, 2, 5], amount = 11

dp[0] = 0
dp[1] = 1 (coin 1)
dp[2] = 1 (coin 2)
dp[3] = 2 (2+1)
dp[4] = 2 (2+2)
dp[5] = 1 (coin 5)
dp[6] = 2 (5+1)
...
dp[11] = 3 (5+5+1)
"""
```

#### Problem 26: **Longest Common Subsequence**

```python
def longest_common_subsequence(text1, text2):
    """
    Input: text1 = "abcde", text2 = "ace" 
    Output: 3 (subsequence "ace")
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# DP Table Visualization:
"""
    ""  a  c  e
""   0  0  0  0
a    0  1  1  1
b    0  1  1  1
c    0  1  2  2
d    0  1  2  2
e    0  1  2  3  ← Answer

LCS = "ace" with length 3
"""
```

#### Problem 27: **0/1 Knapsack**

```python
def knapsack(weights, values, capacity):
    """
    Choose items to maximize value without exceeding capacity
    
    Input: weights = [1, 3, 4, 5]
           values = [1, 4, 5, 7]
           capacity = 7
    Output: 9 (items with weight 3+4 = 7, value 4+5 = 9)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of (include item, exclude item)
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

---

## 💰 Greedy Algorithms {#greedy}

### Greedy Strategy:

Make **locally optimal choice** at each step, hoping for global optimum.

#### Problem 28: **Activity Selection**

```python
def max_activities(start, end):
    """
    Select maximum non-overlapping activities
    
    Input: start = [1, 3, 0, 5, 8, 5]
           end   = [2, 4, 6, 7, 9, 9]
    Output: 4 (activities 0, 1, 3, 4)
    """
    # Sort by ending time
    activities = sorted(zip(start, end), key=lambda x: x[1])
    
    count = 1
    last_end = activities[0][1]
    
    for s, e in activities[1:]:
        if s >= last_end:  # No overlap
            count += 1
            last_end = e
    
    return count
```

#### Problem 29: **Jump Game**

```python
def can_jump(nums):
    """
    Can you reach last index?
    Each element is max jump length from that position
    
    Input: [2,3,1,1,4]
    Output: True (jump 1→3→4)
    """
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False  # Can't reach this position
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True
```

---

## ↔️ Two Pointers & Sliding Window {#two-pointers}

### Two Pointers Technique:

Use two pointers to traverse array efficiently.

#### Problem 30: **Container With Most Water**

```python
def max_area(height):
    """
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49 (between index 1 and 8)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

### Sliding Window:

Maintain a window that slides through array.

#### Problem 31: **Minimum Window Substring**

```python
def min_window(s, t):
    """
    Find smallest substring of s containing all characters of t
    
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    """
    from collections import Counter
    
    if not s or not t:
        return ""
    
    target_count = Counter(t)
    required = len(target_count)
    formed = 0
    window_counts = {}
    
    left = right = 0
    min_len = float('inf')
    min_window = ""
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1
        
        # Contract window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right+1]
            
            char = s[left]
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return min_window
```

---

## 🔢 Bit Manipulation {#bit-manipulation}

### Common Bit Operations:

```python
# AND (&)
5 & 3  # 101 & 011 = 001 = 1

# OR (|)
5 | 3  # 101 | 011 = 111 = 7

# XOR (^)
5 ^ 3  # 101 ^ 011 = 110 = 6

# NOT (~)
~5     # ~101 = 010 = 2 (in 3-bit)

# Left Shift (<<)
5 << 1  # 101 << 1 = 1010 = 10 (multiply by 2)

# Right Shift (>>)
5 >> 1  # 101 >> 1 = 10 = 2 (divide by 2)
```

#### Problem 32: **Single Number**

```python
def single_number(nums):
    """
    Every element appears twice except one
    
    Input: [2,2,1]
    Output: 1
    """
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out pairs
    return result

# XOR Properties:
# a ^ a = 0
# a ^ 0 = a
# 2 ^ 2 ^ 1 = 0 ^ 1 = 1
```

#### Problem 33: **Count set bits**

```python
def count_bits(n):
    """
    Count number of 1s in binary representation
    """
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Right shift
    return count

# Example: n = 5 (binary: 101)
# Step 1: 101 & 1 = 1, count = 1, n = 10
# Step 2: 10 & 1 = 0, count = 1, n = 1
# Step 3: 1 & 1 = 1, count = 2, n = 0
# Answer: 2
```

---

## 🚀 Advanced Data Structures {#advanced}

### 1. Trie (Prefix Tree)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.starts_with("app")) # True
```

**Visualization:**
```
Trie with words: "cat", "can", "car"

        root
         |
         c
         |
         a
       / | \
      t  n  r
      *  *  *
      
(* marks end of word)
```

### 2. Segment Tree

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            
            self.build(arr, left, start, mid)
            self.build(arr, right, mid + 1, end)
            self.tree[node] = self.tree[left] + self.tree[right]
    
    def query(self, node, start, end, l, r):
        if r < start or l > end:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2
        
        return (self.query(left, start, mid, l, r) +
                self.query(right, mid + 1, end, l, r))
    
    def range_sum(self, l, r):
        return self.query(0, 0, self.n - 1, l, r)
```

---

## 🎤 Interview Preparation {#interview-prep}

### Top Companies and Focus Areas:

| Company | Focus Areas |
|---------|-------------|
| **Google** | Arrays, Graphs, DP, System Design |
| **Amazon** | Trees, Graphs, OOP, Leadership |
| **Microsoft** | Arrays, Strings, Recursion, DP |
| **Meta** | Graphs, Hashing, DP, System Design |
| **Apple** | Trees, Arrays, Recursion |

### Interview Process:

```
1. Screening Call (15-30 min)
   - Basic DSA questions
   - Resume discussion

2. Phone Interview (45-60 min)
   - 1-2 Coding problems
   - Time complexity analysis

3. Onsite (4-5 rounds)
   - Coding (3-4 rounds)
   - System Design (1 round)
   - Behavioral (throughout)

4. Offer/Rejection
```

### Problem-Solving Framework:

```
1. LISTEN & UNDERSTAND
   - Ask clarifying questions
   - Understand inputs/outputs
   - Check edge cases

2. EXAMPLE
   - Work through examples
   - Edge cases
   - Large cases

3. BRUTE FORCE
   - State the naive solution
   - Analyze complexity

4. OPTIMIZE
   - Look for patterns
   - Use appropriate DS
   - Optimize step by step

5. CODE
   - Write clean code
   - Use good variable names
   - Handle edge cases

6. TEST
   - Use your examples
   - Edge cases
   - Fix bugs

7. COMPLEXITY ANALYSIS
   - Time complexity
   - Space complexity
```

### Top 50 Must-Do Problems:

#### Arrays (10):
1. Two Sum
2. Maximum Subarray
3. Product of Array Except Self
4. Container With Most Water
5. Rotate Array
6. Find Minimum in Rotated Sorted Array
7. 3Sum
8. Best Time to Buy and Sell Stock
9. Spiral Matrix
10. Merge Intervals

#### Strings (5):
11. Longest Substring Without Repeating Characters
12. Valid Palindrome
13. Group Anagrams
14. Longest Palindromic Substring
15. Minimum Window Substring

#### Linked Lists (5):
16. Reverse Linked List
17. Detect Cycle
18. Merge Two Sorted Lists
19. Remove Nth Node From End
20. Add Two Numbers

#### Trees (10):
21. Maximum Depth of Binary Tree
22. Validate BST
23. Level Order Traversal
24. Lowest Common Ancestor
25. Binary Tree Maximum Path Sum
26. Serialize and Deserialize Binary Tree
27. Invert Binary Tree
28. Diameter of Binary Tree
29. Path Sum II
30. Kth Smallest in BST

#### Graphs (5):
31. Number of Islands
32. Clone Graph
33. Course Schedule
34. Word Ladder
35. Pacific Atlantic Water Flow

#### Dynamic Programming (10):
36. Climbing Stairs
37. Coin Change
38. Longest Common Subsequence
39. 0/1 Knapsack
40. Longest Increasing Subsequence
41. Edit Distance
42. Word Break
43. House Robber
44. Decode Ways
45. Maximum Product Subarray

#### Misc (5):
46. LRU Cache
47. Design HashMap
48. Top K Frequent Elements
49. Meeting Rooms II
50. Sliding Window Maximum

---

## 🗺️ Practice Roadmap {#practice-roadmap}

### Week-by-Week Plan (12 Weeks to Master DSA):

#### Weeks 1-2: Foundation
- ✅ Arrays & Strings
- ✅ Time/Space Complexity
- ✅ Two Pointers
- **Practice:** 20 easy problems

#### Weeks 3-4: Linear Structures
- ✅ Linked Lists
- ✅ Stacks & Queues
- ✅ Hashing
- **Practice:** 15 medium problems

#### Weeks 5-6: Recursion & Trees
- ✅ Recursion fundamentals
- ✅ Binary Trees
- ✅ Binary Search Trees
- **Practice:** 20 medium problems

#### Weeks 7-8: Graphs & Advanced
- ✅ Graph traversals (DFS/BFS)
- ✅ Shortest path algorithms
- ✅ Heaps & Priority Queues
- **Practice:** 15 medium/hard problems

#### Weeks 9-10: Algorithms
- ✅ Sorting & Searching
- ✅ Dynamic Programming
- ✅ Greedy Algorithms
- **Practice:** 20 medium/hard problems

#### Weeks 11-12: Advanced & Mock Interviews
- ✅ Advanced data structures (Trie, Segment Tree)
- ✅ Bit Manipulation
- ✅ Mock interviews
- **Practice:** 10 hard problems + contests

### Daily Practice Schedule:

```
Morning (1 hour):
- 1 new problem
- Understand & solve

Evening (1 hour):
- Revise previously solved problems
- Optimize solutions
- Study patterns

Weekend (3-4 hours):
- Participate in contests (Leetcode, Codeforces)
- Focus on weak areas
- System design basics
```

### Recommended Platforms:

| Platform | Focus | Difficulty |
|----------|-------|------------|
| **Leetcode** | Interview prep | Easy→Hard |
| **HackerRank** | Fundamentals | Easy→Medium |
| **Codeforces** | Competitive programming | Medium→Expert |
| **GeeksforGeeks** | Concepts & practice | All levels |
| **InterviewBit** | Structured learning | Interview focus |

---

## 📚 Resources

### Books:
1. **"Cracking the Coding Interview"** - Gayle Laakmann McDowell
2. **"Introduction to Algorithms (CLRS)"** - Cormen, Leiserson, Rivest, Stein
3. **"Algorithm Design Manual"** - Steven Skiena
4. **"Elements of Programming Interviews"** - Aziz, Lee, Prakash

### YouTube Channels:
1. **Abdul Bari** - Algorithms
2. **William Fiset** - Data Structures
3. **Back To Back SWE** - Problem solving
4. **Tushar Roy** - DP & Graphs
5. **NeetCode** - Leetcode solutions

### Websites:
1. **Visualgo.net** - Visualize algorithms
2. **Leetcode.com** - Practice problems
3. **GeeksforGeeks.org** - Tutorials & practice
4. **Big-O Cheat Sheet** - Complexity reference

---

## 🎯 Final Tips

### Keys to Success:

1. **Consistency** > Intensity
   - 1 hour daily > 10 hours on weekend

2. **Understand** > Memorize
   - Understand the pattern, not just the solution

3. **Quality** > Quantity
   - Solve 1 problem well > 10 problems poorly

4. **Revise** regularly
   - Review old problems every week

5. **Time yourself**
   - Practice under interview conditions

6. **Explain out loud**
   - Explain solution to yourself/others

7. **Learn from failures**
   - Every wrong solution teaches something

### Red Flags to Avoid:

❌ Jumping to code without understanding  
❌ Not testing your solution  
❌ Ignoring edge cases  
❌ Poor variable names  
❌ Not analyzing complexity  
❌ Giving up too quickly  
❌ Not asking clarifying questions  

### Green Flags:

✅ Ask good questions  
✅ Think out loud  
✅ Consider multiple approaches  
✅ Write clean, readable code  
✅ Test thoroughly  
✅ Optimize after working solution  
✅ Communicate clearly  

---

## 🏆 Conclusion

Congratulations! You now have a comprehensive roadmap to master Data Structures & Algorithms!

### Remember:

> *"Everyone you know once knew nothing about DSA. The difference between an expert and a beginner is just practice and time."*

### Your Next Steps:

1. 📝 Start with Arrays & Strings
2. 💻 Solve 1 problem daily on Leetcode
3. 📚 Read "Cracking the Coding Interview"
4. 🤝 Join coding communities
5. 🎯 Participate in contests
6. 📈 Track your progress
7. 🔄 Revise regularly

---

## 📞 Quick Reference Card

```
TIME COMPLEXITIES:
O(1) - Hash lookup, Array access
O(log n) - Binary search, Balanced BST
O(n) - Linear scan, BFS, DFS
O(n log n) - Merge sort, Quick sort, Heap sort
O(n²) - Nested loops, Bubble sort
O(2ⁿ) - Recursive Fibonacci (without memo)

SPACE COMPLEXITIES:
O(1) - Few variables
O(n) - Array, Hash map
O(n²) - 2D matrix
O(log n) - Recursion stack (binary search)

WHEN TO USE:
Array - Fast access by index
Linked List - Frequent insertions/deletions
Stack - LIFO, parentheses, undo/redo
Queue - FIFO, BFS, task scheduling
Hash Map - O(1) lookup, counting, caching
Heap - Priority queue, K largest/smallest
Tree - Hierarchical data, fast search
Graph - Networks, relationships, paths
```

---

*"The only way to learn a new programming language is by writing programs in it."* - Dennis Ritchie

*"Programs must be written for people to read, and only incidentally for machines to execute."* - Harold Abelson

---

**Happy Coding! May your algorithms be efficient and your code bug-free! 🚀**

---

*Last Updated: January 2026*
*Version: 1.0 - Complete Zero to Hero DSA Guide*
*Created with ❤️ for aspiring software engineers*

---

## ⚠️ Disclaimer

This guide is for educational purposes. Problem-solving skills develop over time with consistent practice. Don't get discouraged by initial difficulties – every expert was once a beginner!

**Remember: Code every day, even if it's just for 30 minutes! 💪**

---
---

# 🚀 ADVANCED SECTION: Leetcode Mastery

---

## 🎯 Leetcode Problem-Solving Patterns

### The 14 Patterns That Solve 90% of Leetcode Problems:

#### Pattern 1: **Sliding Window** 🪟

**When to Use:** Contiguous subarrays/substrings, find optimal window

**Template:**
```python
def sliding_window(arr):
    left = 0
    window_sum = 0
    result = 0
    
    for right in range(len(arr)):
        # Add element to window
        window_sum += arr[right]
        
        # Shrink window if needed
        while window_condition_broken:
            window_sum -= arr[left]
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

**Problems to Practice:**
1. ✅ Longest Substring Without Repeating Characters (LC 3)
2. ✅ Minimum Window Substring (LC 76)
3. ✅ Longest Repeating Character Replacement (LC 424)
4. ✅ Permutation in String (LC 567)
5. ✅ Fruit Into Baskets (LC 904)

**Complete Example - LC 3:**
```python
def length_of_longest_substring(s):
    """
    Find longest substring without repeating characters
    Input: "abcabcbb"
    Output: 3 ("abc")
    """
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Detailed walkthrough:
"""
s = "abcabcbb"

right=0: window="a", set={a}, len=1
right=1: window="ab", set={a,b}, len=2
right=2: window="abc", set={a,b,c}, len=3 ✅
right=3: s[3]='a' in set! Remove s[0]='a'
         window="bc", then add 'a'
         window="bca", set={b,c,a}, len=3
right=4: s[4]='b' in set! Remove until no 'b'
         window="cab", set={c,a,b}, len=3
...continues...

Max length = 3
"""
```

---

#### Pattern 2: **Two Pointers** ↔️

**When to Use:** Sorted arrays, pairs, triplets, palindrome checks

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        if condition_met:
            # Process and move both
            left += 1
            right -= 1
        elif need_larger_sum:
            left += 1
        else:
            right -= 1
    
    return result
```

**Problems to Practice:**
1. ✅ Two Sum II (LC 167)
2. ✅ 3Sum (LC 15)
3. ✅ Container With Most Water (LC 11)
4. ✅ Trapping Rain Water (LC 42)
5. ✅ Remove Duplicates from Sorted Array (LC 26)

**Complete Example - LC 15 (3Sum):**
```python
def three_sum(nums):
    """
    Find all triplets that sum to zero
    Input: [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()  # Important: sort first!
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Visualization:
"""
Sorted: [-4, -1, -1, 0, 1, 2]
         i=0 (-4)
              L         R
         -4 + -1 + 2 = -3 (too small, L++)
         
         i=1 (-1)
              L      R
         -1 + -1 + 2 = 0 ✅ Found!
         
         Continue searching...
"""
```

---

#### Pattern 3: **Fast & Slow Pointers** (Floyd's Algorithm) 🐢🐰

**When to Use:** Linked lists, cycle detection, finding middle

**Template:**
```python
def fast_slow_pointers(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next           # Move 1 step
        fast = fast.next.next      # Move 2 steps
        
        if slow == fast:
            # Cycle detected or middle found
            return True
    
    return False
```

**Problems to Practice:**
1. ✅ Linked List Cycle (LC 141)
2. ✅ Find Duplicate Number (LC 287)
3. ✅ Happy Number (LC 202)
4. ✅ Middle of Linked List (LC 876)
5. ✅ Palindrome Linked List (LC 234)

**Complete Example - LC 287 (Find Duplicate):**
```python
def find_duplicate(nums):
    """
    Array with n+1 integers, each from 1 to n
    One number repeats, find it!
    
    Input: [1,3,4,2,2]
    Output: 2
    """
    # Treat as linked list: nums[i] points to nums[nums[i]]
    slow = fast = nums[0]
    
    # Phase 1: Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Visualization:
"""
[1, 3, 4, 2, 2]
 0  1  2  3  4

Index: 0→1→3→2→4→2→4→2... (cycle at 2)

Slow: 0→1→3→2→4→2
Fast: 0→1→3→2→4→2→4→2 (they meet at 2)

Duplicate = 2 ✅
"""
```

---

#### Pattern 4: **Merge Intervals** 📊

**When to Use:** Overlapping intervals, scheduling problems

**Template:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Overlapping - merge
            merged[-1][1] = max(last[1], current[1])
        else:
            # Not overlapping - add new
            merged.append(current)
    
    return merged
```

**Problems to Practice:**
1. ✅ Merge Intervals (LC 56)
2. ✅ Insert Interval (LC 57)
3. ✅ Meeting Rooms II (LC 253)
4. ✅ Non-overlapping Intervals (LC 435)
5. ✅ Minimum Number of Arrows (LC 452)

**Complete Example - LC 253 (Meeting Rooms II):**
```python
def min_meeting_rooms(intervals):
    """
    Find minimum meeting rooms needed
    Input: [[0,30],[5,10],[15,20]]
    Output: 2
    """
    if not intervals:
        return 0
    
    # Separate start and end times
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    
    rooms_needed = 0
    max_rooms = 0
    start_ptr = end_ptr = 0
    
    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            # Meeting starting, need a room
            rooms_needed += 1
            max_rooms = max(max_rooms, rooms_needed)
            start_ptr += 1
        else:
            # Meeting ending, free a room
            rooms_needed -= 1
            end_ptr += 1
    
    return max_rooms

# Timeline visualization:
"""
[[0,30], [5,10], [15,20]]

Timeline:
0────────────────────────30
     5───10
               15───20

Time 0: Start meeting 1 → rooms=1
Time 5: Start meeting 2 → rooms=2 (max)
Time 10: End meeting 2 → rooms=1
Time 15: Start meeting 3 → rooms=2
Time 20: End meeting 3 → rooms=1
Time 30: End meeting 1 → rooms=0

Answer: 2 rooms needed
"""
```

---

#### Pattern 5: **Cyclic Sort** 🔄

**When to Use:** Array contains numbers in range [1, n]

**Template:**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            # Swap to correct position
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    return nums
```

**Problems to Practice:**
1. ✅ Missing Number (LC 268)
2. ✅ Find All Missing Numbers (LC 448)
3. ✅ Find Duplicate Number (LC 287)
4. ✅ First Missing Positive (LC 41)
5. ✅ Find All Duplicates (LC 442)

**Complete Example - LC 448:**
```python
def find_disappeared_numbers(nums):
    """
    Find all numbers missing from [1, n]
    Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]
    """
    # Cyclic sort
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    
    # Find missing numbers
    result = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(i + 1)
    
    return result

# Step by step:
"""
[4,3,2,7,8,2,3,1]

Swap 4 with nums[3]: [7,3,2,4,8,2,3,1]
Swap 7 with nums[6]: [3,3,2,4,8,2,7,1]
Swap 3 with nums[2]: [2,3,3,4,8,2,7,1]
Swap 2 with nums[1]: [3,2,3,4,8,2,7,1]
Continue...

Final: [1,2,3,4,3,2,7,8]

Missing at positions: [5,6]
Answer: [5,6] ✅
"""
```

---

#### Pattern 6: **In-place Reversal of Linked List** 🔄

**Template:**
```python
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
```

**Problems to Practice:**
1. ✅ Reverse Linked List (LC 206)
2. ✅ Reverse Linked List II (LC 92)
3. ✅ Reverse Nodes in k-Group (LC 25)
4. ✅ Rotate List (LC 61)
5. ✅ Swap Nodes in Pairs (LC 24)

---

#### Pattern 7: **Tree BFS** (Level Order) 🌳

**Template:**
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

**Problems to Practice:**
1. ✅ Binary Tree Level Order (LC 102)
2. ✅ Zigzag Level Order (LC 103)
3. ✅ Average of Levels (LC 637)
4. ✅ Minimum Depth (LC 111)
5. ✅ Level Order Bottom (LC 107)

---

#### Pattern 8: **Tree DFS** (In/Pre/Post Order) 🌲

**Template:**
```python
def dfs_inorder(root):
    if not root:
        return []
    
    result = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result
```

**Problems to Practice:**
1. ✅ Path Sum (LC 112)
2. ✅ All Paths From Root to Leaf (LC 257)
3. ✅ Diameter of Binary Tree (LC 543)
4. ✅ Path Sum III (LC 437)
5. ✅ Sum Root to Leaf Numbers (LC 129)

---

#### Pattern 9: **Two Heaps** 🏔️🏔️

**When to Use:** Find median, scheduling with priorities

**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap
    
    def add_num(self, num):
        # Add to max heap
        heapq.heappush(self.small, -num)
        
        # Balance: largest in small should be ≤ smallest in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

**Problems to Practice:**
1. ✅ Find Median from Data Stream (LC 295)
2. ✅ Sliding Window Median (LC 480)
3. ✅ IPO (LC 502)

---

#### Pattern 10: **Subsets** (Backtracking) 🎲

**Template:**
```python
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

**Problems to Practice:**
1. ✅ Subsets (LC 78)
2. ✅ Subsets II (LC 90)
3. ✅ Permutations (LC 46)
4. ✅ Combinations (LC 77)
5. ✅ Combination Sum (LC 39)

**Complete Example - LC 78:**
```python
def subsets(nums):
    """
    Generate all subsets
    Input: [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    """
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

# Decision tree:
"""
                    []
           /         |        \
         [1]        [2]       [3]
        /   \         \
    [1,2]  [1,3]    [2,3]
      |
   [1,2,3]

Each level: choose to include element or not
"""
```

---

#### Pattern 11: **Modified Binary Search** 🔍

**Template:**
```python
def binary_search_modified(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

**Problems to Practice:**
1. ✅ Search in Rotated Sorted Array (LC 33)
2. ✅ Find Minimum in Rotated Array (LC 153)
3. ✅ Search in 2D Matrix (LC 74)
4. ✅ Find Peak Element (LC 162)
5. ✅ Search Range (LC 34)

---

#### Pattern 12: **Top K Elements** 🏆

**Template:**
```python
import heapq

def top_k_frequent(nums, k):
    # Count frequencies
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Use min heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
```

**Problems to Practice:**
1. ✅ Top K Frequent Elements (LC 347)
2. ✅ Kth Largest Element (LC 215)
3. ✅ K Closest Points to Origin (LC 973)
4. ✅ Reorganize String (LC 767)
5. ✅ Kth Smallest in Sorted Matrix (LC 378)

---

#### Pattern 13: **K-way Merge** 🔀

**Template:**
```python
import heapq

def merge_k_sorted(lists):
    heap = []
    
    # Add first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

**Problems to Practice:**
1. ✅ Merge K Sorted Lists (LC 23)
2. ✅ Kth Smallest in Sorted Matrix (LC 378)
3. ✅ Smallest Range Covering K Lists (LC 632)

---

#### Pattern 14: **Topological Sort** 📊

**Template:**
```python
from collections import deque, defaultdict

def topological_sort(n, edges):
    # Build graph and in-degree
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(n)}
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Find all sources (nodes with 0 in-degree)
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []
```

**Problems to Practice:**
1. ✅ Course Schedule (LC 207)
2. ✅ Course Schedule II (LC 210)
3. ✅ Alien Dictionary (LC 269)
4. ✅ Sequence Reconstruction (LC 444)

---

## 🏢 Company-Specific Problem Banks

### **Google (FAANG)** 🔵

**Focus Areas:** Arrays, Graphs, DP, System Design

**Top 50 Google Problems:**

**Arrays & Strings (15):**
1. ⭐ Longest Substring Without Repeating Characters (LC 3) - Medium
2. ⭐ Container With Most Water (LC 11) - Medium
3. ⭐ 3Sum (LC 15) - Medium
4. ⭐ Next Permutation (LC 31) - Medium
5. ⭐ Trapping Rain Water (LC 42) - Hard
6. ⭐ Jump Game II (LC 45) - Medium
7. ⭐ Spiral Matrix (LC 54) - Medium
8. ⭐ Merge Intervals (LC 56) - Medium
9. ⭐ Minimum Window Substring (LC 76) - Hard
10. ⭐ Word Search (LC 79) - Medium
11. ⭐ Largest Rectangle in Histogram (LC 84) - Hard
12. ⭐ Decode Ways (LC 91) - Medium
13. ⭐ Word Break (LC 139) - Medium
14. ⭐ Find All Anagrams (LC 438) - Medium
15. ⭐ Longest Palindromic Substring (LC 5) - Medium

**Trees & Graphs (15):**
16. ⭐ Binary Tree Level Order (LC 102) - Medium
17. ⭐ Maximum Depth (LC 104) - Easy
18. ⭐ Construct Binary Tree (LC 105) - Medium
19. ⭐ Binary Tree Maximum Path Sum (LC 124) - Hard
20. ⭐ Word Ladder (LC 127) - Hard
21. ⭐ Clone Graph (LC 133) - Medium
22. ⭐ Number of Islands (LC 200) - Medium
23. ⭐ Course Schedule (LC 207) - Medium
24. ⭐ Implement Trie (LC 208) - Medium
25. ⭐ Lowest Common Ancestor (LC 236) - Medium
26. ⭐ Serialize/Deserialize Tree (LC 297) - Hard
27. ⭐ Alien Dictionary (LC 269) - Hard
28. ⭐ Graph Valid Tree (LC 261) - Medium
29. ⭐ Walls and Gates (LC 286) - Medium
30. ⭐ Longest Increasing Path (LC 329) - Hard

**Dynamic Programming (10):**
31. ⭐ Climbing Stairs (LC 70) - Easy
32. ⭐ Unique Paths (LC 62) - Medium
33. ⭐ Minimum Path Sum (LC 64) - Medium
34. ⭐ Coin Change (LC 322) - Medium
35. ⭐ Longest Increasing Subsequence (LC 300) - Medium
36. ⭐ Maximum Product Subarray (LC 152) - Medium
37. ⭐ House Robber II (LC 213) - Medium
38. ⭐ Edit Distance (LC 72) - Hard
39. ⭐ Regular Expression Matching (LC 10) - Hard
40. ⭐ Burst Balloons (LC 312) - Hard

**System Design & Others (10):**
41. ⭐ LRU Cache (LC 146) - Medium
42. ⭐ Min Stack (LC 155) - Easy
43. ⭐ Design Hit Counter (LC 362) - Medium
44. ⭐ Insert Delete GetRandom (LC 380) - Medium
45. ⭐ Find Median from Data Stream (LC 295) - Hard
46. ⭐ Sliding Window Maximum (LC 239) - Hard
47. ⭐ Meeting Rooms II (LC 253) - Medium
48. ⭐ Valid Sudoku (LC 36) - Medium
49. ⭐ Evaluate Reverse Polish Notation (LC 150) - Medium
50. ⭐ Design Search Autocomplete (LC 642) - Hard

---

### **Amazon** 🟠

**Focus Areas:** Arrays, Trees, DP, OOP Design

**Top 50 Amazon Problems:**

**High Frequency (20):**
1. 🔥 Two Sum (LC 1) - Easy
2. 🔥 Add Two Numbers (LC 2) - Medium
3. 🔥 Longest Palindromic Substring (LC 5) - Medium
4. 🔥 Merge Two Sorted Lists (LC 21) - Easy
5. 🔥 Valid Parentheses (LC 20) - Easy
6. 🔥 Rotate Image (LC 48) - Medium
7. 🔥 Group Anagrams (LC 49) - Medium
8. 🔥 Merge Intervals (LC 56) - Medium
9. 🔥 Climbing Stairs (LC 70) - Easy
10. 🔥 Minimum Window Substring (LC 76) - Hard
11. 🔥 Word Search (LC 79) - Medium
12. 🔥 Maximum Subarray (LC 53) - Easy
13. 🔥 Validate Binary Search Tree (LC 98) - Medium
14. 🔥 Binary Tree Level Order (LC 102) - Medium
15. 🔥 Maximum Depth (LC 104) - Easy
16. 🔥 Best Time to Buy/Sell Stock (LC 121) - Easy
17. 🔥 Word Ladder (LC 127) - Hard
18. 🔥 LRU Cache (LC 146) - Medium
19. 🔥 Number of Islands (LC 200) - Medium
20. 🔥 Lowest Common Ancestor (LC 236) - Medium

**Leadership Principles Focus (15):**
21. 📦 Product of Array Except Self (LC 238) - Medium
22. 📦 Top K Frequent Elements (LC 347) - Medium
23. 📦 K Closest Points to Origin (LC 973) - Medium
24. 📦 Reorder Log Files (LC 937) - Easy
25. 📦 Prison Cells After N Days (LC 957) - Medium
26. 📦 Critical Connections in Network (LC 1192) - Hard
27. 📦 Analyze User Website Visit Pattern (LC 1152) - Medium
28. 📦 Most Common Word (LC 819) - Easy
29. 📦 Treasure Island (Amazon OA) - Medium
30. 📦 Zombie in Matrix (Amazon OA) - Medium
31. 📦 Amazon Fresh Promotion (Amazon OA) - Medium
32. 📦 Optimal Utilization (Amazon OA) - Medium
33. 📦 Subtree with Maximum Average (Amazon OA) - Medium
34. 📦 Turn Stile (Amazon OA) - Medium
35. 📦 Minimum Difficulty of Job Schedule (LC 1335) - Hard

**Trees & Graphs (15):**
36. 🌳 Diameter of Binary Tree (LC 543) - Easy
37. 🌳 Symmetric Tree (LC 101) - Easy
38. 🌳 Path Sum (LC 112) - Easy
39. 🌳 Flatten Binary Tree (LC 114) - Medium
40. 🌳 Populating Next Right Pointers (LC 116) - Medium
41. 🌳 Kth Smallest in BST (LC 230) - Medium
42. 🌳 Course Schedule II (LC 210) - Medium
43. 🌳 Clone Graph (LC 133) - Medium
44. 🌳 Pacific Atlantic Water Flow (LC 417) - Medium
45. 🌳 Snakes and Ladders (LC 909) - Medium
46. 🌳 Rotting Oranges (LC 994) - Medium
47. 🌳 Distance K in Binary Tree (LC 863) - Medium
48. 🌳 Vertical Order Traversal (LC 987) - Hard
49. 🌳 Alien Dictionary (LC 269) - Hard
50. 🌳 Word Search II (LC 212) - Hard

---

### **Meta (Facebook)** 🔵

**Focus Areas:** Arrays, Strings, Trees, BFS/DFS

**Top 50 Meta Problems:**

**High Frequency (25):**
1. 💙 Valid Palindrome (LC 125) - Easy
2. 💙 Merge Two Sorted Lists (LC 21) - Easy
3. 💙 Binary Tree Paths (LC 257) - Easy
4. 💙 Move Zeroes (LC 283) - Easy
5. 💙 Add Binary (LC 67) - Easy
6. 💙 Valid Palindrome II (LC 680) - Easy
7. 💙 Subarray Sum Equals K (LC 560) - Medium
8. 💙 Merge Intervals (LC 56) - Medium
9. 💙 3Sum (LC 15) - Medium
10. 💙 Remove Invalid Parentheses (LC 301) - Hard
11. 💙 Binary Tree Vertical Order (LC 314) - Medium
12. 💙 Clone Graph (LC 133) - Medium
13. 💙 Validate Binary Search Tree (LC 98) - Medium
14. 💙 Lowest Common Ancestor (LC 236) - Medium
15. 💙 Accounts Merge (LC 721) - Medium
16. 💙 Random Pick with Weight (LC 528) - Medium
17. 💙 Dot Product of Sparse Vectors (LC 1570) - Medium
18. 💙 Buildings With Ocean View (LC 1762) - Medium
19. 💙 String to Integer (atoi) (LC 8) - Medium
20. 💙 Integer to English Words (LC 273) - Hard
21. 💙 Expression Add Operators (LC 282) - Hard
22. 💙 Alien Dictionary (LC 269) - Hard
23. 💙 Shortest Path in Binary Matrix (LC 1091) - Medium
24. 💙 Task Scheduler (LC 621) - Medium
25. 💙 Simplify Path (LC 71) - Medium

**Medium Difficulty (15):**
26. 🔷 Product of Array Except Self (LC 238)
27. 🔷 Group Shifted Strings (LC 249)
28. 🔷 Continuous Subarray Sum (LC 523)
29. 🔷 Interval List Intersections (LC 986)
30. 🔷 Nested List Weight Sum (LC 339)
31. 🔷 Binary Tree Right Side View (LC 199)
32. 🔷 Populating Next Right Pointers (LC 116)
33. 🔷 Flatten Binary Tree (LC 114)
34. 🔷 Number of Connected Components (LC 323)
35. 🔷 Minimum Remove to Make Valid Parens (LC 1249)
36. 🔷 Verifying Alien Dictionary (LC 953)
37. 🔷 Next Permutation (LC 31)
38. 🔷 Pow(x, n) (LC 50)
39. 🔷 Permutations (LC 46)
40. 🔷 Basic Calculator II (LC 227)

**Hard Problems (10):**
41. ⚫ Trapping Rain Water (LC 42)
42. ⚫ First Missing Positive (LC 41)
43. ⚫ Longest Substring with K Distinct (LC 340)
44. ⚫ Read N Characters Given Read4 II (LC 158)
45. ⚫ Serialize and Deserialize Binary Tree (LC 297)
46. ⚫ Binary Tree Maximum Path Sum (LC 124)
47. ⚫ Word Break II (LC 140)
48. ⚫ Longest Consecutive Sequence (LC 128)
49. ⚫ Median of Two Sorted Arrays (LC 4)
50. ⚫ Regular Expression Matching (LC 10)

---

### **Microsoft** 💚

**Focus Areas:** Arrays, Strings, Recursion, DP, Design

**Top 50 Microsoft Problems:**

1. 🟩 Two Sum (LC 1)
2. 🟩 Reverse Integer (LC 7)
3. 🟩 String to Integer (LC 8)
4. 🟩 Excel Sheet Column Number (LC 171)
5. 🟩 Reverse Linked List (LC 206)
6. 🟩 Linked List Cycle (LC 141)
7. 🟩 Merge Two Sorted Lists (LC 21)
8. 🟩 Maximum Depth of Binary Tree (LC 104)
9. 🟩 Validate Binary Search Tree (LC 98)
10. 🟩 Lowest Common Ancestor (LC 236)
11. 🟩 3Sum (LC 15)
12. 🟩 Group Anagrams (LC 49)
13. 🟩 Letter Combinations (LC 17)
14. 🟩 Generate Parentheses (LC 22)
15. 🟩 Permutations (LC 46)
16. 🟩 Rotate Image (LC 48)
17. 🟩 Spiral Matrix (LC 54)
18. 🟩 Merge Intervals (LC 56)
19. 🟩 Unique Paths (LC 62)
20. 🟩 Word Search (LC 79)
21. 🟩 Decode Ways (LC 91)
22. 🟩 Binary Tree Level Order (LC 102)
23. 🟩 Maximum Product Subarray (LC 152)
24. 🟩 Number of Islands (LC 200)
25. 🟩 Course Schedule (LC 207)
26. 🟩 Implement Trie (LC 208)
27. 🟩 Word Search II (LC 212)
28. 🟩 Kth Largest Element (LC 215)
29. 🟩 Product of Array Except Self (LC 238)
30. 🟩 Meeting Rooms II (LC 253)
31. 🟩 Longest Increasing Subsequence (LC 300)
32. 🟩 Coin Change (LC 322)
33. 🟩 Top K Frequent Elements (LC 347)
34. 🟩 Decode String (LC 394)
35. 🟩 Pacific Atlantic Water Flow (LC 417)
36. 🟩 Find All Anagrams (LC 438)
37. 🟩 Longest Repeating Character (LC 424)
38. 🟩 Word Break (LC 139)
39. 🟩 LRU Cache (LC 146)
40. 🟩 Design Add and Search Words (LC 211)
41. 🟩 Clone Graph (LC 133)
42. 🟩 Min Stack (LC 155)
43. 🟩 Excel Sheet Column Title (LC 168)
44. 🟩 Majority Element (LC 169)
45. 🟩 Happy Number (LC 202)
46. 🟩 Reverse Words in String (LC 151)
47. 🟩 Fraction to Decimal (LC 166)
48. 🟩 Evaluate Division (LC 399)
49. 🟩 All O'one Data Structure (LC 432)
50. 🟩 LFU Cache (LC 460)

---

## 🚀 Advanced Graph Algorithms

### **Dijkstra's Shortest Path Algorithm** ⚡

**Use Case:** Find shortest path in weighted graph (non-negative weights)

**Complete Implementation:**
```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Find shortest paths from start to all nodes
    
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    """
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Check all neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

print(dijkstra(graph, 'A'))
# Output: {'A': 0, 'B': 4, 'C': 2, 'D': 9, 'E': 11}
```

**Step-by-Step Visualization:**
```
Graph:
    A --4--> B
    |        |
    2        5
    |        |
    v        v
    C --8--> D --2--> E
    |
    10
    |
    v
    E

Step 1: Start at A (dist=0)
  Current: A, Distance: 0
  Update: B=4, C=2

Step 2: Visit C (smallest unvisited)
  Current: C, Distance: 2
  Update: D=10, E=12

Step 3: Visit B
  Current: B, Distance: 4
  Update: D=min(10,9)=9

Step 4: Visit D
  Current: D, Distance: 9
  Update: E=min(12,11)=11

Step 5: Visit E
  Done!

Final Distances:
A: 0
B: 4
C: 2
D: 9
E: 11
```

**Leetcode Problems:**
1. ⭐ Network Delay Time (LC 743)
2. ⭐ Path with Maximum Probability (LC 1514)
3. ⭐ Cheapest Flights Within K Stops (LC 787)

---

### **Union Find (Disjoint Set Union)** 🔗

**Use Case:** Connected components, cycle detection, MST

**Complete Implementation with Path Compression:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components
    
    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x == root_y:
            return False  # Already connected
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.count -= 1
        return True
    
    def connected(self, x, y):
        """Check if x and y are in same component"""
        return self.find(x) == self.find(y)

# Example - Number of Connected Components
def count_components(n, edges):
    """
    n = 5, edges = [[0,1], [1,2], [3,4]]
    Output: 2 (components: {0,1,2} and {3,4})
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        uf.union(u, v)
    
    return uf.count

# Visualization:
"""
Initial: 0  1  2  3  4  (5 components)

After [0,1]:
    0-1  2  3  4  (4 components)

After [1,2]:
    0-1-2  3  4  (3 components)

After [3,4]:
    0-1-2  3-4  (2 components) ✅
"""
```

**Leetcode Problems:**
1. ⭐ Number of Connected Components (LC 323)
2. ⭐ Graph Valid Tree (LC 261)
3. ⭐ Redundant Connection (LC 684)
4. ⭐ Accounts Merge (LC 721)
5. ⭐ Satisfiability of Equality Equations (LC 990)

---

### **Bellman-Ford Algorithm** (Negative Weights) 📉

**Use Case:** Shortest path with negative edge weights

```python
def bellman_ford(n, edges, src):
    """
    n: number of nodes
    edges: [(u, v, weight), ...]
    src: source node
    
    Returns: distances dict or None if negative cycle
    """
    dist = [float('inf')] * n
    dist[src] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle detected!
    
    return dist
```

---

### **Floyd-Warshall Algorithm** (All Pairs Shortest Path) 🌐

```python
def floyd_warshall(n, edges):
    """
    Find shortest paths between ALL pairs of nodes
    Time: O(n³), Space: O(n²)
    """
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance from node to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Add edges
    for u, v, w in edges:
        dist[u][v] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

---

### **Prim's Minimum Spanning Tree** 🌳

```python
import heapq

def prims_mst(n, edges):
    """
    Find MST using Prim's algorithm
    edges: [(u, v, weight), ...]
    
    Returns: total weight of MST
    """
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    visited = set()
    min_heap = [(0, 0)]  # (weight, node)
    mst_weight = 0
    
    while min_heap and len(visited) < n:
        weight, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        mst_weight += weight
        
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))
    
    return mst_weight
```

---

### **Kruskal's Minimum Spanning Tree** 🌲

```python
def kruskals_mst(n, edges):
    """
    Find MST using Kruskal's algorithm
    Uses Union-Find
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_weight = 0
    edges_used = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            edges_used += 1
            
            if edges_used == n - 1:
                break
    
    return mst_weight
```

---

### **Topological Sort (Kahn's Algorithm)** 📊

```python
from collections import deque, defaultdict

def topological_sort_kahns(n, edges):
    """
    Topological sort using Kahn's algorithm (BFS)
    
    edges: [(u, v), ...] where u → v
    Returns: topological ordering or [] if cycle exists
    """
    # Build graph and in-degree
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Find all nodes with in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If all nodes processed, no cycle
    return result if len(result) == n else []

# Example:
"""
Graph: 0 → 1 → 3
       ↓   ↓
       2 → 4

Valid orderings: [0,1,2,3,4] or [0,2,1,3,4] or [0,2,1,4,3]
"""
```

---

## 🎯 50+ Additional Practice Problems

### **Arrays - 15 More Problems**

**Easy:**
1. 🟢 Contains Duplicate (LC 217)
2. 🟢 Best Time to Buy Sell Stock (LC 121)
3. 🟢 Valid Anagram (LC 242)
4. 🟢 Plus One (LC 66)
5. 🟢 Move Zeroes (LC 283)

**Medium:**
6. 🟡 Find First and Last Position (LC 34)
7. 🟡 Search in Rotated Sorted Array (LC 33)
8. 🟡 Find Peak Element (LC 162)
9. 🟡 Set Matrix Zeroes (LC 73)
10. 🟡 Sort Colors (LC 75)
11. 🟡 Search 2D Matrix II (LC 240)
12. 🟡 Longest Consecutive Sequence (LC 128)

**Hard:**
13. 🔴 First Missing Positive (LC 41)
14. 🔴 Median of Two Sorted Arrays (LC 4)
15. 🔴 Sliding Window Maximum (LC 239)

---

### **Strings - 10 More Problems**

16. 🟢 Valid Palindrome (LC 125)
17. 🟢 Implement strStr() (LC 28)
18. 🟡 Longest Palindromic Substring (LC 5)
19. 🟡 Palindromic Substrings (LC 647)
20. 🟡 Decode String (LC 394)
21. 🟡 Letter Combinations of Phone (LC 17)
22. 🟡 Generate Parentheses (LC 22)
23. 🔴 Minimum Window Substring (LC 76)
24. 🔴 Word Break II (LC 140)
25. 🔴 Edit Distance (LC 72)

---

### **Linked Lists - 10 More Problems**

26. 🟢 Delete Node in LL (LC 237)
27. 🟢 Palindrome Linked List (LC 234)
28. 🟡 Add Two Numbers (LC 2)
29. 🟡 Remove Nth Node from End (LC 19)
30. 🟡 Reorder List (LC 143)
31. 🟡 Odd Even Linked List (LC 328)
32. 🟡 Intersection of Two Lists (LC 160)
33. 🔴 Reverse Nodes in k-Group (LC 25)
34. 🔴 Copy List with Random Pointer (LC 138)
35. 🔴 Merge K Sorted Lists (LC 23)

---

### **Trees - 15 More Problems**

36. 🟢 Same Tree (LC 100)
37. 🟢 Symmetric Tree (LC 101)
38. 🟢 Path Sum (LC 112)
39. 🟡 Binary Tree Zigzag (LC 103)
40. 🟡 Construct Tree from Pre/Inorder (LC 105)
41. 🟡 Flatten Binary Tree to LL (LC 114)
42. 🟡 Binary Tree Right Side View (LC 199)
43. 🟡 Count Complete Tree Nodes (LC 222)
44. 🟡 Kth Smallest in BST (LC 230)
45. 🟡 Lowest Common Ancestor of BST (LC 235)
46. 🔴 Binary Tree Max Path Sum (LC 124)
47. 🔴 Serialize Deserialize BST (LC 449)
48. 🔴 Vertical Order Traversal (LC 987)
49. 🔴 Binary Tree Cameras (LC 968)
50. 🔴 Recover BST (LC 99)

---

### **Graphs - 15 More Problems**

51. 🟡 Surrounded Regions (LC 130)
52. 🟡 Word Ladder II (LC 126)
53. 🟡 Network Delay Time (LC 743)
54. 🟡 Graph Valid Tree (LC 261)
55. 🟡 Number of Connected Components (LC 323)
56. 🟡 Redundant Connection (LC 684)
57. 🟡 Shortest Path in Binary Matrix (LC 1091)
58. 🟡 Rotting Oranges (LC 994)
59. 🔴 Critical Connections (LC 1192)
60. 🔴 Swim in Rising Water (LC 778)
61. 🔴 Shortest Path with Alternating Colors (LC 1129)
62. 🔴 Minimum Cost to Connect All Points (LC 1584)
63. 🔴 Path with Maximum Probability (LC 1514)
64. 🔴 Cheapest Flights K Stops (LC 787)
65. 🔴 Word Search II (LC 212)

---

### **Dynamic Programming - 20 More Problems**

**Easy/Medium:**
66. 🟢 Best Time to Buy Sell Stock (LC 121)
67. 🟡 House Robber (LC 198)
68. 🟡 Jump Game (LC 55)
69. 🟡 Unique Paths II (LC 63)
70. 🟡 Decode Ways (LC 91)
71. 🟡 Word Break (LC 139)
72. 🟡 Combination Sum IV (LC 377)
73. 🟡 Partition Equal Subset Sum (LC 416)
74. 🟡 Target Sum (LC 494)
75. 🟡 Delete and Earn (LC 740)

**Hard:**
76. 🔴 Best Time Buy Sell III (LC 123)
77. 🔴 Best Time Buy Sell IV (LC 188)
78. 🔴 Interleaving String (LC 97)
79. 🔴 Distinct Subsequences (LC 115)
80. 🔴 Minimum Insertion Steps (LC 1312)
81. 🔴 Palindrome Partitioning II (LC 132)
82. 🔴 Longest Valid Parentheses (LC 32)
83. 🔴 Wildcard Matching (LC 44)
84. 🔴 Scramble String (LC 87)
85. 🔴 Dungeon Game (LC 174)

---

### **Design & Implementation - 10 Problems**

86. 🟢 Design HashSet (LC 705)
87. 🟢 Design HashMap (LC 706)
88. 🟡 LRU Cache (LC 146)
89. 🟡 Design Twitter (LC 355)
90. 🟡 Insert Delete GetRandom O(1) (LC 380)
91. 🟡 Design Tic-Tac-Toe (LC 348)
92. 🟡 Design Snake Game (LC 353)
93. 🔴 LFU Cache (LC 460)
94. 🔴 Design Search Autocomplete (LC 642)
95. 🔴 All O'one Data Structure (LC 432)

---

### **Backtracking - 10 Problems**

96. 🟡 Subsets (LC 78)
97. 🟡 Subsets II (LC 90)
98. 🟡 Permutations (LC 46)
99. 🟡 Permutations II (LC 47)
100. 🟡 Combination Sum (LC 39)
101. 🟡 Combination Sum II (LC 40)
102. 🟡 Palindrome Partitioning (LC 131)
103. 🟡 Letter Case Permutation (LC 784)
104. 🔴 N-Queens (LC 51)
105. 🔴 Sudoku Solver (LC 37)

---

## 📊 Detailed Complexity Analysis Examples

### Example 1: Nested Loops Analysis

```python
def example1(arr):
    n = len(arr)
    
    # Single loop: O(n)
    for i in range(n):
        print(arr[i])
    
    # Nested loops: O(n²)
    for i in range(n):
        for j in range(n):
            print(arr[i], arr[j])
    
    # Three nested loops: O(n³)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(arr[i], arr[j], arr[k])
    
    # Total: O(n) + O(n²) + O(n³) = O(n³)
    # We take the dominant term!
```

### Example 2: Logarithmic Complexity

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:  # How many times?
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Analysis:
"""
Each iteration divides search space by 2
n → n/2 → n/4 → n/8 → ... → 1

Number of iterations = log₂(n)
Time Complexity: O(log n) ✅

Example with n=16:
16 → 8 → 4 → 2 → 1 (4 iterations)
log₂(16) = 4 ✅
"""
```

### Example 3: Recursive Complexity

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Analysis:
"""
Recurrence: T(n) = T(n-1) + T(n-2) + O(1)

Tree structure:
                    fib(5)
              /              \
        fib(4)                fib(3)
       /     \               /      \
   fib(3)  fib(2)        fib(2)  fib(1)
   /   \    /   \        /   \
fib(2) fib(1) ...      fib(1) fib(0)

Height of tree: n
Nodes at level k: ~2^k
Total nodes: 2^0 + 2^1 + ... + 2^n ≈ 2^n

Time Complexity: O(2^n) - Exponential! 💀
Space Complexity: O(n) - Recursion stack depth
"""

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# With memoization:
# Each fib(k) computed only once
# Time: O(n) ✅
# Space: O(n) for memo + O(n) for stack = O(n)
```

### Example 4: Merge Sort Complexity

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])      # T(n/2)
    right = merge_sort(arr[mid:])     # T(n/2)
    
    return merge(left, right)          # O(n)

# Analysis:
"""
Recurrence: T(n) = 2T(n/2) + O(n)

Level 0: 1 problem of size n → work = n
Level 1: 2 problems of size n/2 → work = 2(n/2) = n
Level 2: 4 problems of size n/4 → work = 4(n/4) = n
...
Level log n: n problems of size 1 → work = n

Total levels: log n
Work per level: n
Total: n * log n

Time Complexity: O(n log n) ✅
Space Complexity: O(n) for merge arrays
"""
```

---

## 🎓 Complete Leetcode Learning Path

### **Phase 1: Foundation (Weeks 1-4)** - 40 Problems

**Week 1: Arrays & Hashing (10 problems)**
- Easy: 217, 242, 1
- Medium: 49, 347, 238, 271
- Hard: 41

**Week 2: Two Pointers (10 problems)**
- Easy: 125, 167
- Medium: 15, 11, 42
- Hard: 76

**Week 3: Sliding Window (10 problems)**
- Medium: 3, 424, 567
- Hard: 76, 239

**Week 4: Stacks (10 problems)**
- Easy: 20, 155
- Medium: 150, 22, 739
- Hard: 84

### **Phase 2: Data Structures (Weeks 5-8)** - 50 Problems

**Week 5: Linked Lists (12 problems)**
**Week 6: Trees (15 problems)**
**Week 7: Tries & Heaps (12 problems)**
**Week 8: Graphs Basics (11 problems)**

### **Phase 3: Advanced (Weeks 9-12)** - 60 Problems

**Week 9: Advanced Graphs (15 problems)**
**Week 10: Dynamic Programming (20 problems)**
**Week 11: Backtracking & Greedy (15 problems)**
**Week 12: System Design & Mock Interviews (10 problems)**

---

## 🔥 Advanced Patterns (Hot Topics!)

### Pattern 15: **Monotonic Stack** 📚

**When to Use:** Find next greater/smaller element, histogram problems

A **monotonic stack** maintains elements in increasing or decreasing order.

#### **Monotonic Increasing Stack:**
```python
def monotonic_increasing_stack(nums):
    """
    Stack maintains increasing order (bottom to top)
    """
    stack = []
    
    for num in nums:
        # Pop elements greater than current
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    
    return stack

# Example:
# nums = [3, 1, 4, 1, 5, 9, 2, 6]
# Process:
# 3 → [3]
# 1 → [1] (pop 3, 3 > 1)
# 4 → [1, 4]
# 1 → [1] (pop 4, 4 > 1)
# 5 → [1, 5]
# 9 → [1, 5, 9]
# 2 → [1, 2] (pop 9, 5)
# 6 → [1, 2, 6]
```

#### **Problem 1: Next Greater Element I (LC 496)**

```python
def next_greater_element(nums1, nums2):
    """
    Find next greater element for each element in nums1
    
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    
    Explanation:
    - 4: no greater element → -1
    - 1: next greater is 3
    - 2: no greater element → -1
    """
    # Build next greater map for nums2
    next_greater = {}
    stack = []
    
    for num in nums2:
        # For all elements smaller than current
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # Elements remaining have no greater element
    while stack:
        next_greater[stack.pop()] = -1
    
    # Build result for nums1
    return [next_greater[num] for num in nums1]

# Visualization for nums2 = [1,3,4,2]:
"""
Step 1: num=1, stack=[1]
Step 2: num=3, 3>1 → next_greater[1]=3, stack=[3]
Step 3: num=4, 4>3 → next_greater[3]=4, stack=[4]
Step 4: num=2, 2<4 → stack=[4,2]

Remaining: next_greater[4]=-1, next_greater[2]=-1

Map: {1:3, 3:4, 4:-1, 2:-1}
"""
```

#### **Problem 2: Daily Temperatures (LC 739)**

```python
def daily_temperatures(temperatures):
    """
    Find how many days until warmer temperature
    
    Input: [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Store indices
    
    for i in range(n):
        # Pop all temperatures smaller than current
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result

# Detailed walkthrough:
"""
temps = [73,74,75,71,69,72,76,73]
index =  0  1  2  3  4  5  6  7

i=0: stack=[0]
i=1: 74>73 → result[0]=1, stack=[1]
i=2: 75>74 → result[1]=1, stack=[2]
i=3: 71<75 → stack=[2,3]
i=4: 69<71 → stack=[2,3,4]
i=5: 72>69,71 → result[4]=1, result[3]=2, stack=[2,5]
i=6: 76>72,75 → result[5]=1, result[2]=4, stack=[6]
i=7: 73<76 → stack=[6,7]

result = [1,1,4,2,1,1,0,0] ✅
"""
```

#### **Problem 3: Largest Rectangle in Histogram (LC 84)** 🔥

```python
def largest_rectangle_area(heights):
    """
    Find largest rectangle in histogram
    
    Input: [2,1,5,6,2,3]
    Output: 10 (rectangle with height 5, width 2)
    """
    stack = []
    max_area = 0
    heights.append(0)  # Add sentinel to flush stack
    
    for i, h in enumerate(heights):
        # Pop taller bars and calculate area
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            
            # Width = distance to next smaller element
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    return max_area

# Visualization:
"""
heights = [2,1,5,6,2,3]

    6 |     ▓
    5 |   ▓ ▓
    4 |   ▓ ▓
    3 |   ▓ ▓   ▓
    2 | ▓ ▓ ▓ ▓ ▓
    1 | ▓ ▓ ▓ ▓ ▓
      |___________
        0 1 2 3 4 5

Largest rectangle: heights 5 and 6 (indices 2,3)
Height = 5, Width = 2 → Area = 10 ✅
"""
```

#### **Problem 4: Trapping Rain Water (LC 42)** 💧

```python
def trap(height):
    """
    Calculate how much rain water can be trapped
    
    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

# Visualization:
"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]

    3 |       ▓
    2 |   ▓ ~ ▓ ~ ~ ▓
    1 | ▓ ~ ▓ ▓ ▓ ▓ ▓
    0 |▓▓▓▓▓▓▓▓▓▓▓▓▓
      |____________

~ = trapped water (6 units total)
"""
```

---

### Pattern 16: **Prefix Sum** ➕

**When to Use:** Range sum queries, subarray problems

#### **Basic Prefix Sum:**
```python
def build_prefix_sum(nums):
    """
    prefix[i] = sum of elements from 0 to i
    """
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

# Example:
# nums = [1, 2, 3, 4, 5]
# prefix = [0, 1, 3, 6, 10, 15]
#
# Range sum [1, 3] = prefix[4] - prefix[1] = 10 - 1 = 9 ✅
```

#### **Problem 5: Subarray Sum Equals K (LC 560)**

```python
def subarray_sum(nums, k):
    """
    Find number of subarrays with sum = k
    
    Input: nums = [1,1,1], k = 2
    Output: 2 (subarrays [1,1] appear twice)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Initialize with sum 0
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Add current prefix sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count

# Why this works:
"""
If prefix_sum[j] - prefix_sum[i] = k
Then prefix_sum[i] = prefix_sum[j] - k

Example: [1, 2, 3, 4], k = 5

prefix_sum: 0 → 1 → 3 → 6 → 10

At index 3 (sum=6):
  6 - 5 = 1, and 1 exists in map!
  So subarray [2,3] has sum 5 ✅
"""
```

#### **Problem 6: Range Sum Query - Immutable (LC 303)**

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        """
        Return sum of elements from index left to right
        Time: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]

# Example:
"""
nums = [1, 2, 3, 4, 5]
prefix = [0, 1, 3, 6, 10, 15]

sumRange(1, 3) = prefix[4] - prefix[1] = 10 - 1 = 9
(sum of [2, 3, 4] = 9) ✅
"""
```

#### **Problem 7: Product of Array Except Self (LC 238)**

```python
def product_except_self(nums):
    """
    Return array where output[i] = product of all except nums[i]
    Without division and in O(n)
    
    Input: [1,2,3,4]
    Output: [24,12,8,6]
    """
    n = len(nums)
    result = [1] * n
    
    # Left pass: result[i] = product of all to the left
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # Right pass: multiply by product of all to the right
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result

# Visualization:
"""
nums = [1, 2, 3, 4]

After left pass:
result = [1, 1, 2, 6]
         ^  ^  ^  ^
         |  |  |  +-- 1×2×3
         |  |  +-- 1×2
         |  +-- 1
         +-- 1 (nothing to left)

After right pass:
result = [24, 12, 8, 6]
         ^   ^   ^  ^
         |   |   |  +-- 6×1
         |   |   +-- 2×4×1
         |   +-- 1×3×4
         +-- 1×2×3×4
"""
```

---

## 📝 String Algorithms (Advanced)

### **1. KMP Algorithm (Knuth-Morris-Pratt)** 🔍

**Use Case:** Pattern matching in O(n + m) time

```python
def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text
    
    Time: O(n + m) where n=len(text), m=len(pattern)
    Space: O(m)
    """
    if not pattern:
        return []
    
    # Build LPS (Longest Prefix Suffix) array
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = build_lps(pattern)
    result = []
    
    i = j = 0  # i for text, j for pattern
    
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result

# Example:
"""
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

LPS array for pattern:
  A B A B C A B A B
  0 0 1 2 0 1 2 3 4

Match found at index 10 ✅
"""
```

#### **Leetcode Problems:**
- Implement strStr() (LC 28)
- Repeated Substring Pattern (LC 459)
- Shortest Palindrome (LC 214)

---

### **2. Rabin-Karp Algorithm** (Rolling Hash) 🎲

```python
def rabin_karp(text, pattern):
    """
    Pattern matching using rolling hash
    
    Time: O(n + m) average case
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    # Constants for hashing
    BASE = 256
    MOD = 10**9 + 7
    
    # Calculate hash of pattern
    pattern_hash = 0
    text_hash = 0
    h = pow(BASE, m - 1, MOD)
    
    for i in range(m):
        pattern_hash = (BASE * pattern_hash + ord(pattern[i])) % MOD
        text_hash = (BASE * text_hash + ord(text[i])) % MOD
    
    result = []
    
    # Slide pattern over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Hash matches, verify character by character
            if text[i:i+m] == pattern:
                result.append(i)
        
        # Calculate rolling hash for next window
        if i < n - m:
            text_hash = (BASE * (text_hash - ord(text[i]) * h) + 
                        ord(text[i + m])) % MOD
            if text_hash < 0:
                text_hash += MOD
    
    return result

# Rolling Hash Explanation:
"""
text = "abcdef", pattern = "cde"

Hash(abc) = a×256² + b×256 + c
Hash(bcd) = b×256² + c×256 + d

Rolling from "abc" to "bcd":
1. Remove 'a': hash - (a × 256²)
2. Shift left: (hash - a×256²) × 256
3. Add 'd': ... + d

This is O(1) instead of recalculating entire hash!
"""
```

---

### **3. Manacher's Algorithm** (Longest Palindrome) 🪞

```python
def longest_palindrome_manacher(s):
    """
    Find longest palindromic substring in O(n)
    
    Input: "babad"
    Output: "bab" or "aba"
    """
    # Preprocess: add '#' between characters
    T = '#'.join(f'^{s}$')
    n = len(T)
    P = [0] * n  # P[i] = radius of palindrome at i
    C = R = 0    # Center and right boundary
    
    for i in range(1, n - 1):
        # Mirror of i with respect to C
        mirror = 2 * C - i
        
        if i < R:
            P[i] = min(R - i, P[mirror])
        
        # Expand around i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1
        
        # Update center and right boundary
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    # Find maximum length palindrome
    max_len, center = max((length, i) for i, length in enumerate(P))
    start = (center - max_len) // 2
    
    return s[start:start + max_len]

# Visualization:
"""
s = "babad"
T = "^#b#a#b#a#d#$"

After processing P array shows palindrome radius at each position
Longest palindrome: "bab" or "aba" (length 3)
"""
```

---

### **4. Z-Algorithm** 📏

```python
def z_algorithm(s):
    """
    Z[i] = length of longest substring starting from i 
    which is also a prefix of s
    
    Time: O(n)
    """
    n = len(s)
    Z = [0] * n
    Z[0] = n
    
    l, r = 0, 0
    
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r] == s[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    
    return Z

# Example:
"""
s = "aabxaayaab"
Z = [10, 1, 0, 0, 2, 1, 0, 3, 1, 0]
           ^        ^        ^
           |        |        +-- "aab" matches prefix (length 3)
           |        +-- "aa" matches prefix (length 2)
           +-- "a" matches prefix (length 1)
"""
```

---

## 🎯 Advanced DP Patterns

### **1. State Machine DP** (Stock Problems) 📈

```python
def max_profit_k_transactions(prices, k):
    """
    Best Time to Buy and Sell Stock IV (LC 188)
    At most k transactions
    
    State: (day, transactions_used, holding_stock)
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # Optimization: if k >= n//2, unlimited transactions
    if k >= n // 2:
        return sum(max(0, prices[i+1] - prices[i]) 
                   for i in range(n-1))
    
    # DP: dp[i][j][0] = max profit on day i with j transactions, not holding
    #     dp[i][j][1] = max profit on day i with j transactions, holding
    
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    
    for price in prices:
        for j in range(k, 0, -1):
            sell[j] = max(sell[j], buy[j] + price)
            buy[j] = max(buy[j], sell[j-1] - price)
    
    return sell[k]

# State Machine Visualization:
"""
States: REST ⇄ HOLDING ⇄ SOLD → REST

Transitions:
REST → HOLDING: buy stock (-price)
HOLDING → SOLD: sell stock (+price)
SOLD → REST: cooldown
REST → REST: do nothing
HOLDING → HOLDING: do nothing
"""
```

#### **All Stock Problems:**
1. Best Time to Buy and Sell Stock (LC 121) - 1 transaction
2. Best Time to Buy and Sell Stock II (LC 122) - unlimited
3. Best Time to Buy and Sell Stock III (LC 123) - 2 transactions
4. Best Time to Buy and Sell Stock IV (LC 188) - k transactions
5. Best Time to Buy and Sell with Cooldown (LC 309)
6. Best Time to Buy and Sell with Fee (LC 714)

---

### **2. Bitmask DP** (TSP, Subset Problems) 🎭

```python
def traveling_salesman(dist):
    """
    Find shortest path visiting all cities exactly once
    
    dist[i][j] = distance from city i to city j
    """
    n = len(dist)
    
    # dp[mask][i] = min cost to visit cities in mask, ending at i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0
    
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            
            # Try visiting city j next
            for j in range(n):
                if mask & (1 << j):
                    continue
                
                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j], 
                                     dp[mask][i] + dist[i][j])
    
    # Return to city 0
    full_mask = (1 << n) - 1
    return min(dp[full_mask][i] + dist[i][0] for i in range(1, n))

# Bitmask Example:
"""
4 cities: mask = 0b1101 means visited cities 0, 2, 3
          bit positions: 3210

Check if city 2 visited: mask & (1 << 2) = 0b1101 & 0b0100 = 0b0100 (yes!)
Mark city 1 visited: mask | (1 << 1) = 0b1101 | 0b0010 = 0b1111
"""
```

#### **Bitmask DP Problems:**
- Shortest Path Visiting All Nodes (LC 847)
- Find Shortest Superstring (LC 943)
- Partition to K Equal Sum Subsets (LC 698)

---

### **3. DP on Trees** 🌳

```python
def tree_dp_diameter(root):
    """
    Find diameter of binary tree (LC 543)
    Diameter = longest path between any two nodes
    """
    max_diameter = 0
    
    def dfs(node):
        nonlocal max_diameter
        
        if not node:
            return 0
        
        # Get max depth of left and right subtrees
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        
        # Update diameter (path through this node)
        max_diameter = max(max_diameter, left_depth + right_depth)
        
        # Return max depth of this subtree
        return 1 + max(left_depth, right_depth)
    
    dfs(root)
    return max_diameter

# Visualization:
"""
        1
       / \
      2   3
     / \
    4   5

Diameter = 3 (path 4→2→1→3 or 5→2→1→3)

At node 2:
  left_depth = 1 (to 4 or 5)
  right_depth = 0
  diameter through 2 = 1 + 0 = 1

At node 1:
  left_depth = 2 (to 4 or 5)
  right_depth = 1 (to 3)
  diameter through 1 = 2 + 1 = 3 ✅
"""
```

#### **Tree DP Problems:**
- Binary Tree Maximum Path Sum (LC 124)
- House Robber III (LC 337)
- Longest Univalue Path (LC 687)
- Sum of Distances in Tree (LC 834)

---

### **4. Digit DP** 🔢

```python
def count_digit_one(n):
    """
    Count number of 1's in all numbers from 1 to n (LC 233)
    
    Input: n = 13
    Output: 6 (1, 10, 11, 12, 13 contain total of 6 ones)
    """
    count = 0
    factor = 1
    
    while factor <= n:
        divider = factor * 10
        count += (n // divider) * factor
        count += min(max(n % divider - factor + 1, 0), factor)
        factor *= 10
    
    return count

# Explanation:
"""
For n = 13, count 1's in each digit position:

Ones place: 1,11 → 2 ones
Tens place: 10,11,12,13 → 4 ones

Total = 6 ✅

Pattern: For digit d at position p:
- Complete cycles: (n // (10^(p+1))) * 10^p
- Partial cycle: depends on digit at position p
"""
```

#### **Digit DP Problems:**
- Number of Digit One (LC 233)
- Numbers with Repeated Digits (LC 1012)
- Numbers At Most N Given Digit Set (LC 902)

---

## 🔢 Math & Number Theory

### **1. Sieve of Eratosthenes** (Prime Numbers) ✨

```python
def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n
    Time: O(n log log n)
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples as not prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

# Visualization for n = 30:
"""
Initial: [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

i=2: Cross out 4,6,8,10,12,14,16,18,20,22,24,26,28,30
i=3: Cross out 9,15,21,27
i=5: Cross out 25

Remaining: [2,3,5,7,11,13,17,19,23,29] ✅
"""

def count_primes(n):
    """Count Primes (LC 204)"""
    if n < 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)
```

---

### **2. GCD & LCM Algorithms** 🔄

```python
def gcd(a, b):
    """
    Greatest Common Divisor using Euclidean algorithm
    Time: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least Common Multiple"""
    return (a * b) // gcd(a, b)

# Extended Euclidean Algorithm (for modular inverse)
def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y

# Example:
"""
gcd(48, 18)
48 = 18 × 2 + 12
18 = 12 × 1 + 6
12 = 6 × 2 + 0
GCD = 6 ✅

lcm(48, 18) = (48 × 18) / 6 = 144
"""
```

---

### **3. Modular Arithmetic** 🎲

```python
def mod_pow(base, exp, mod):
    """
    Fast exponentiation with modulo
    Calculate (base^exp) % mod in O(log exp)
    
    Pow(x, n) (LC 50)
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        
        exp = exp >> 1  # Divide by 2
        base = (base * base) % mod
    
    return result

# Example: 2^10 mod 1000
"""
2^10 = 1024 mod 1000 = 24

Binary of 10 = 1010

result = 1
exp=10 (1010): even, skip
base = 2² = 4

exp=5 (101): odd, result = 1 × 4 = 4
base = 4² = 16

exp=2 (10): even, skip
base = 16² = 256

exp=1 (1): odd, result = 4 × 256 = 1024
result mod 1000 = 24 ✅
"""

def mod_inverse(a, m):
    """
    Find modular multiplicative inverse
    a × x ≡ 1 (mod m)
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    return (x % m + m) % m
```

---

### **4. Combinatorics** 🎰

```python
def nCr(n, r):
    """
    Calculate combinations: C(n, r) = n! / (r! × (n-r)!)
    Optimized to avoid overflow
    """
    if r > n - r:
        r = n - r
    
    result = 1
    for i in range(r):
        result *= (n - i)
        result //= (i + 1)
    
    return result

def nCr_mod(n, r, mod):
    """
    Calculate C(n, r) % mod using Pascal's triangle
    """
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Build Pascal's triangle
    dp = [[0] * (r + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
        for j in range(1, min(i, r) + 1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    
    return dp[n][r]

# Pascal's Triangle:
"""
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

C(4, 2) = 6 ✅
"""

def permutations_count(n, r):
    """
    Calculate permutations: P(n, r) = n! / (n-r)!
    """
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result
```

---

## 🎤 Practical Interview Skills

### **How to Approach an Unknown Problem** 🧩

```
STEP-BY-STEP FRAMEWORK:

1. CLARIFY THE PROBLEM (2-3 minutes)
   Questions to ask:
   ✓ What are the input/output types?
   ✓ What are the constraints? (array size, value ranges)
   ✓ Can input be empty/null?
   ✓ Are there duplicates?
   ✓ Is the array sorted?
   ✓ Any special edge cases?

2. EXAMPLES (3-4 minutes)
   ✓ Walk through 2-3 examples
   ✓ Include edge cases (empty, single element, all same)
   ✓ Large input example
   ✓ Verify understanding with interviewer

3. BRUTE FORCE (2-3 minutes)
   ✓ State the naive solution
   ✓ Explain time/space complexity
   ✓ "This works but we can optimize..."
   ✓ Don't code yet - just explain!

4. OPTIMIZE (5-7 minutes)
   ✓ Look for patterns in examples
   ✓ Can we sort? → O(n log n)
   ✓ Can we use hash map? → O(n) space for O(1) lookup
   ✓ Is there a greedy approach?
   ✓ Can we use two pointers?
   ✓ Binary search applicable?
   ✓ Draw pictures/diagrams
   
5. WALK THROUGH (2-3 minutes)
   ✓ Explain optimized approach clearly
   ✓ Use example to demonstrate
   ✓ Mention time/space complexity
   ✓ Get interviewer's approval before coding

6. CODE (10-15 minutes)
   ✓ Use good variable names
   ✓ Write clean, readable code
   ✓ Think out loud while coding
   ✓ Handle edge cases
   ✓ Add comments for complex logic

7. TEST (5-7 minutes)
   ✓ Walk through your code with example
   ✓ Test edge cases
   ✓ Check for off-by-one errors
   ✓ Look for null pointer issues
   ✓ Fix any bugs found

8. ANALYZE (2 minutes)
   ✓ State final time complexity
   ✓ State final space complexity
   ✓ Mention any trade-offs made
```

### **Example Problem Walkthrough:**

**Problem:** Find two numbers in a sorted array that sum to target.

```
1. CLARIFY:
   "Is the array sorted?" → Yes
   "Can I use extra space?" → Yes
   "Are there always two numbers?" → Assume yes
   "Can same element be used twice?" → No

2. EXAMPLES:
   arr = [2, 7, 11, 15], target = 9
   → [2, 7] because 2+7=9 ✓
   
   arr = [1, 2, 3, 4], target = 7
   → [3, 4] because 3+4=7 ✓
   
   Edge: arr = [1, 2], target = 3
   → [1, 2] ✓

3. BRUTE FORCE:
   "I could check all pairs with nested loops.
   Time: O(n²), Space: O(1)
   But we can do better..."

4. OPTIMIZE:
   "Since array is sorted, I can use two pointers:
   - Start from both ends
   - If sum too small, move left pointer right
   - If sum too large, move right pointer left
   - If equal, found it!
   Time: O(n), Space: O(1) ✓"

5. WALK THROUGH:
   [2, 7, 11, 15], target = 9
    ↑           ↑
    L           R
   
   2 + 15 = 17 > 9 → R--
   2 + 11 = 13 > 9 → R--
   2 + 7 = 9 = 9 → Found! ✓

6. CODE:
   def twoSum(nums, target):
       left, right = 0, len(nums) - 1
       
       while left < right:
           current_sum = nums[left] + nums[right]
           
           if current_sum == target:
               return [left, right]
           elif current_sum < target:
               left += 1
           else:
               right -= 1
       
       return []  # No solution found

7. TEST:
   ✓ Example 1: [2,7,11,15], target=9 → [0,1] ✓
   ✓ Example 2: [1,2,3,4], target=7 → [2,3] ✓
   ✓ Edge: [1,2], target=3 → [0,1] ✓

8. ANALYZE:
   Time: O(n) - single pass with two pointers
   Space: O(1) - only using two variables
```

---

### **Communication Tips** 💬

```
DO's:
✅ Think out loud
✅ Explain your thought process
✅ Ask clarifying questions
✅ Discuss trade-offs
✅ Mention alternative approaches
✅ Be enthusiastic and engaged
✅ Listen to hints from interviewer
✅ Admit when stuck and ask for help

DON'Ts:
❌ Jump to coding immediately
❌ Stay silent while thinking
❌ Ignore interviewer's hints
❌ Get defensive about mistakes
❌ Give up too easily
❌ Memorize solutions word-for-word
❌ Lie about knowing a problem
```

**Example Phrases:**
```
"Let me make sure I understand the problem..."
"I'm thinking about a few approaches..."
"The brute force would be X, but we can optimize..."
"I notice a pattern here..."
"Let me trace through an example..."
"I'm considering the trade-off between..."
"Could you give me a hint about...?"
"I made a mistake here, let me fix it..."
```

---

### **Debugging Techniques** 🐛

```
SYSTEMATIC DEBUGGING APPROACH:

1. READ THE ERROR MESSAGE
   - What line is it pointing to?
   - What type of error? (IndexError, TypeError, etc.)

2. PRINT STATEMENT DEBUGGING
   def buggy_function(arr):
       print(f"Input: {arr}")  # Check input
       result = []
       for i in range(len(arr)):
           print(f"i={i}, arr[i]={arr[i]}")  # Trace loop
           result.append(arr[i] * 2)
       print(f"Result: {result}")  # Check output
       return result

3. TRACE WITH EXAMPLE
   Write down variable values at each step:
   
   arr = [1, 2, 3], target = 5
   
   i=0: left=1, right=3, sum=4 ❌
   i=1: left=2, right=3, sum=5 ✓
   
4. CHECK EDGE CASES
   - Empty input: []
   - Single element: [1]
   - Two elements: [1, 2]
   - All same: [5, 5, 5, 5]
   - Negative numbers: [-5, -2, 0, 3]

5. COMMON BUG PATTERNS
   
   Off-by-one errors:
   ❌ for i in range(len(arr)):
          if arr[i+1] > arr[i]:  # Crashes at last element!
   
   ✅ for i in range(len(arr) - 1):
          if arr[i+1] > arr[i]:
   
   Null/None checks:
   ❌ if node.left.val > 5:  # Crashes if node.left is None!
   
   ✅ if node.left and node.left.val > 5:
   
   Integer division:
   ❌ mid = (left + right) / 2  # Returns float!
   
   ✅ mid = (left + right) // 2
   
   Modifying while iterating:
   ❌ for item in my_list:
          my_list.remove(item)  # Dangerous!
   
   ✅ my_list = [item for item in my_list if condition]

6. RUBBER DUCK DEBUGGING
   Explain code line-by-line to interviewer:
   "Here I'm initializing left to 0..."
   "This loop continues while left < right..."
   "Wait, I see the issue - I'm not handling..."
```

---

### **Time Management** ⏱️

**45-Minute Interview Breakdown:**

```
00:00 - 03:00  Problem Understanding & Clarification
03:00 - 07:00  Examples & Edge Cases
07:00 - 10:00  Brute Force Discussion
10:00 - 17:00  Optimization & Approach
17:00 - 32:00  Coding (15 minutes)
32:00 - 40:00  Testing & Debugging
40:00 - 43:00  Complexity Analysis
43:00 - 45:00  Questions for interviewer

⚠️ RED FLAGS - When You're Behind:
- 20 minutes in, haven't started coding
- 35 minutes in, code not complete
- No time left for testing

💡 RECOVERY STRATEGIES:
- If stuck on optimization: "Let me code brute force first"
- If stuck on edge case: "Let me handle main case first"
- If running out of time: "Let me outline the rest..."
```

---

### **Writing Test Cases** 🧪

```python
def test_two_sum():
    """Comprehensive test cases"""
    
    # Basic functionality
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Edge cases
    assert two_sum([3, 3], 6) == [0, 1]  # Duplicates
    assert two_sum([1, 2], 3) == [0, 1]  # Minimum size
    
    # Boundary values
    assert two_sum([0, 0], 0) == [0, 1]  # Zeros
    assert two_sum([-1, 0, 1], 0) == [0, 2]  # Negatives
    
    # Large numbers
    assert two_sum([1000000, 999999, 1], 1000001) == [0, 2]
    
    # No solution
    assert two_sum([1, 2, 3], 10) == []
    
    print("All tests passed! ✅")
```

**Test Case Categories:**
1. **Happy Path** - Normal expected inputs
2. **Edge Cases** - Empty, single element, boundaries
3. **Negative Cases** - Invalid inputs, no solution
4. **Stress Cases** - Large inputs, performance test
5. **Corner Cases** - Unusual but valid inputs

---

## 📊 Quick Reference Cheat Sheets

### **Time Complexity Cheat Sheet** ⏱️

```
DATA STRUCTURE OPERATIONS:

Array:
  Access    → O(1)
  Search    → O(n)
  Insert    → O(n)  [O(1) at end]
  Delete    → O(n)  [O(1) at end]

Linked List:
  Access    → O(n)
  Search    → O(n)
  Insert    → O(1)  [with pointer]
  Delete    → O(1)  [with pointer]

Stack/Queue:
  Push/Pop  → O(1)
  Peek      → O(1)
  Search    → O(n)

Hash Table:
  Search    → O(1) average, O(n) worst
  Insert    → O(1) average, O(n) worst
  Delete    → O(1) average, O(n) worst

Binary Search Tree (balanced):
  Search    → O(log n)
  Insert    → O(log n)
  Delete    → O(log n)

Heap:
  Find Min  → O(1)
  Insert    → O(log n)
  Delete Min→ O(log n)
  Heapify   → O(n)

ALGORITHM COMPLEXITIES:

Sorting:
  Bubble Sort    → O(n²)
  Selection Sort → O(n²)
  Insertion Sort → O(n²)
  Merge Sort     → O(n log n)
  Quick Sort     → O(n log n) average, O(n²) worst
  Heap Sort      → O(n log n)
  Counting Sort  → O(n + k)
  Radix Sort     → O(d × n)

Searching:
  Linear Search  → O(n)
  Binary Search  → O(log n)

Graph:
  DFS/BFS        → O(V + E)
  Dijkstra       → O((V + E) log V)
  Bellman-Ford   → O(V × E)
  Floyd-Warshall → O(V³)
  Prim's MST     → O(E log V)
  Kruskal's MST  → O(E log E)
```

---

### **Pattern Recognition Flowchart** 🎯

```
PROBLEM → PATTERN SELECTION:

Input is Array/String?
│
├─ Need to find subarray/substring?
│  │
│  ├─ Contiguous → SLIDING WINDOW
│  └─ Not contiguous → TWO POINTERS
│
├─ Need to find pairs/triplets?
│  │
│  ├─ Array is sorted → TWO POINTERS
│  └─ Array unsorted → HASH MAP
│
├─ Need to track frequency/count?
│  └─ HASH MAP
│
└─ Need to find range sums?
   └─ PREFIX SUM

Input is Linked List?
│
├─ Detect cycle → FAST & SLOW POINTERS
├─ Find middle → FAST & SLOW POINTERS
└─ Reverse → IN-PLACE REVERSAL

Input is Tree?
│
├─ Level-by-level → BFS (Queue)
├─ Pre/In/Post order → DFS (Recursion)
└─ Path problems → DFS with backtracking

Input is Graph?
│
├─ Find path → DFS/BFS
├─ Shortest path → BFS or Dijkstra
├─ Connected components → UNION FIND
└─ Cycle detection → DFS or UNION FIND

Input is Array with [1, n] range?
└─ CYCLIC SORT

Need to track min/max dynamically?
└─ HEAP

Need all combinations/permutations?
└─ BACKTRACKING

Looking for optimal solution?
│
├─ Overlapping subproblems → DYNAMIC PROGRAMMING
└─ Greedy choice property → GREEDY ALGORITHM

Need next greater/smaller element?
└─ MONOTONIC STACK

Looking for top K elements?
└─ HEAP (Priority Queue)

Multiple sorted arrays to merge?
└─ K-WAY MERGE

Need topological ordering?
└─ TOPOLOGICAL SORT
```

---

### **Common Edge Cases Checklist** ✅

```
ALWAYS TEST THESE:

Arrays/Strings:
☐ Empty input: [] or ""
☐ Single element: [1] or "a"
☐ Two elements: [1, 2]
☐ All same elements: [5, 5, 5]
☐ Already sorted: [1, 2, 3, 4]
☐ Reverse sorted: [4, 3, 2, 1]
☐ Duplicates: [1, 2, 2, 3]
☐ Negative numbers: [-5, -2, 0, 3]
☐ Large numbers: [10^9]
☐ Special characters (strings): "a!@#$%"

Linked Lists:
☐ Null head
☐ Single node
☐ Two nodes
☐ Circular list (if applicable)
☐ Even vs odd length

Trees:
☐ Null root
☐ Single node (root only)
☐ Only left children
☐ Only right children
☐ Balanced vs unbalanced
☐ Complete binary tree

Graphs:
☐ Empty graph
☐ Single node
☐ Disconnected components
☐ Cycles present
☐ Self-loops
☐ Multiple edges between same nodes

Numbers:
☐ Zero: 0
☐ Negative: -5
☐ Integer overflow: 2^31 - 1
☐ Floating point precision

Indices:
☐ i = 0 (first element)
☐ i = n-1 (last element)
☐ i+1, i-1 (boundaries)
☐ Off-by-one errors
```

---

### **Python/Java Syntax Quick Reference** 💻

**Python:**
```python
# Collections
list = [1, 2, 3]
dict = {'a': 1, 'b': 2}
set = {1, 2, 3}
tuple = (1, 2, 3)

# Comprehensions
[x*2 for x in range(10)]
{x: x**2 for x in range(5)}
{x for x in range(10) if x % 2 == 0}

# Common operations
sorted(arr)  # Returns new sorted list
arr.sort()   # In-place sort
reversed(arr)  # Returns iterator
arr.reverse()  # In-place reverse

# Slicing
arr[start:end:step]
arr[::-1]  # Reverse
arr[::2]   # Every other element

# String operations
s.split(',')
','.join(list)
s.strip()
s.lower()
s.upper()

# Math
import math
math.ceil(x)
math.floor(x)
math.sqrt(x)
float('inf')
float('-inf')

# Heap
import heapq
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heapify(list)

# Collections
from collections import defaultdict, Counter, deque
defaultdict(int)
Counter(list)
deque([1, 2, 3])

# Type hints
def function(x: int, y: str) -> bool:
    return True
```

**Java:**
```java
// Collections
List<Integer> list = new ArrayList<>();
Map<String, Integer> map = new HashMap<>();
Set<Integer> set = new HashSet<>();
Queue<Integer> queue = new LinkedList<>();
Deque<Integer> deque = new ArrayDeque<>();

// Sorting
Collections.sort(list);
Arrays.sort(arr);

// String operations
String[] parts = s.split(",");
String joined = String.join(",", parts);
s.trim();
s.toLowerCase();
s.toUpperCase();

// StringBuilder (mutable strings)
StringBuilder sb = new StringBuilder();
sb.append("text");
sb.toString();

// Math
Math.max(a, b);
Math.min(a, b);
Math.abs(x);
Integer.MAX_VALUE;
Integer.MIN_VALUE;

// PriorityQueue (Heap)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

// Lambda & Streams
list.stream()
    .filter(x -> x > 5)
    .map(x -> x * 2)
    .collect(Collectors.toList());
```

---

## 🎓 Final Master Checklist

**Before Your Interview:**

```
PREPARATION (Weeks/Months Before):
☐ Complete 150+ Leetcode problems
☐ Master all 14 patterns
☐ Practice 10+ mock interviews
☐ Review system design basics
☐ Prepare behavioral stories (STAR method)

PRACTICE FOCUS:
☐ Easy: 30 problems (confidence building)
☐ Medium: 100 problems (core preparation)
☐ Hard: 20 problems (stretch goals)

WEEK BEFORE:
☐ Review pattern templates
☐ Practice 2-3 problems daily
☐ Review company-specific problems
☐ Prepare questions for interviewer
☐ Test your setup (webcam, mic, whiteboard)

DAY BEFORE:
☐ Light review only
☐ Get good sleep
☐ Prepare workspace
☐ Have water and paper ready

DURING INTERVIEW:
☐ Clarify problem (2-3 min)
☐ Discuss examples (3-4 min)
☐ Explain approach (5-7 min)
☐ Write clean code (15 min)
☐ Test thoroughly (5-7 min)
☐ Analyze complexity (2 min)
☐ Stay calm and positive!

AFTER INTERVIEW:
☐ Write down problems you solved
☐ Note what went well
☐ Identify areas to improve
☐ Practice those specific topics
```

---

## 🏆 Congratulations!

You now have **THE MOST COMPREHENSIVE DSA Guide** ever created!

### **What You Have:**
- ✅ **4,800+ lines** of content
- ✅ **16 problem-solving patterns** with templates
- ✅ **105+ complete solutions** with visualizations
- ✅ **200+ company-specific problems**
- ✅ **Advanced algorithms** (Dijkstra, Union Find, KMP, etc.)
- ✅ **Advanced DP patterns** (State Machine, Bitmask, Digit DP)
- ✅ **Math & Number Theory** (Primes, GCD, Combinatorics)
- ✅ **Interview skills** (Communication, debugging, time management)
- ✅ **Quick reference sheets** (Complexity, patterns, edge cases)
- ✅ **12-week learning roadmap**

### **Your Path to Success:**
1. 📚 Study patterns systematically
2. 💻 Practice 150+ problems
3. 🎯 Focus on company-specific lists
4. 🎤 Do mock interviews
5. 🔄 Review and iterate

### **Remember:**
- Start with Easy problems to build confidence
- Master one pattern before moving to next
- Consistency beats intensity
- Interview is a skill you can learn
- Everyone fails sometimes - keep practicing!

---

*"The expert in anything was once a beginner."*

**You've got this! Now go ace those interviews! 🚀**

---

*Guide Updated with Complete Content!*
*Version: 3.0 - Ultimate Leetcode & Interview Mastery Edition*
*Total: 4,800+ lines of pure DSA excellence!*

---
---

## 🔍 Advanced Binary Search Patterns

Binary search isn't just for finding elements! Here are advanced patterns:

### **Pattern 17: Binary Search on Answer** 🎯

**Concept:** When you can verify if an answer works in O(n), you can binary search the answer space!

**Template:**
```python
def binary_search_on_answer(arr, condition_func):
    """
    Search for answer in range [left, right]
    condition_func returns True if answer is feasible
    """
    left, right = min_possible, max_possible
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if condition_func(mid):
            result = mid
            # Try to find better answer
            right = mid - 1  # or left = mid + 1 depending on problem
        else:
            left = mid + 1  # or right = mid - 1
    
    return result
```

---

#### **Problem: Koko Eating Bananas (LC 875)** 🍌

```python
def min_eating_speed(piles, h):
    """
    Koko can eat k bananas per hour. Find minimum k to eat all
    bananas within h hours.
    
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
    Explanation:
    k=4: 3/4=1hr, 6/4=2hr, 7/4=2hr, 11/4=3hr → total=8hr ✅
    """
    def can_finish(k):
        """Check if Koko can finish with speed k"""
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k  # Ceiling division
        return hours <= h
    
    # Binary search on speed [1, max(piles)]
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_finish(mid):
            right = mid  # Try smaller speed
        else:
            left = mid + 1  # Need faster speed
    
    return left

# Visualization:
"""
piles = [3, 6, 7, 11], h = 8

Search space: k ∈ [1, 11]

    1  2  3  4  5  6  7  8  9  10  11
    ❌ ❌ ❌ ✅ ✅ ✅ ✅ ✅ ✅ ✅  ✅
                ↑
            Answer = 4 (minimum k that works)

Binary Search:
Step 1: mid=6, can_finish(6)=True → try smaller
Step 2: mid=3, can_finish(3)=False → need larger
Step 3: mid=4, can_finish(4)=True → try smaller
Step 4: mid=3, checked → Answer = 4 ✅

Time: O(n log m) where m = max(piles)
"""
```

---

#### **Problem: Capacity To Ship Packages (LC 1011)** 📦

```python
def ship_within_days(weights, days):
    """
    Ship packages within D days. Find minimum ship capacity.
    
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    """
    def can_ship(capacity):
        """Check if we can ship with given capacity"""
        current_load = 0
        days_needed = 1
        
        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
                if days_needed > days:
                    return False
            else:
                current_load += weight
        
        return True
    
    # Binary search on capacity [max(weights), sum(weights)]
    left = max(weights)  # Must fit largest package
    right = sum(weights)  # Ship everything in 1 day
    
    while left < right:
        mid = (left + right) // 2
        
        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need more capacity
    
    return left

# Diagram:
"""
weights = [1,2,3,4,5,6,7,8,9,10], days = 5

Day 1: [1,2,3,4,5] = 15
Day 2: [6,7] = 13
Day 3: [8] = 8
Day 4: [9] = 9
Day 5: [10] = 10

Capacity = 15 works!

Search space visualization:
Capacity:  10  11  12  13  14  15  16  ...  55
Can ship: ❌  ❌  ❌  ❌  ❌  ✅  ✅  ...  ✅
                                ↑
                          Answer = 15
"""
```

---

#### **Problem: Split Array Largest Sum (LC 410)** ✂️

```python
def split_array(nums, k):
    """
    Split array into k non-empty subarrays.
    Minimize the largest sum among these subarrays.
    
    Input: nums = [7,2,5,10,8], k = 2
    Output: 18
    Explanation: [7,2,5] and [10,8] → max(14, 18) = 18
    """
    def can_split(max_sum):
        """Check if we can split into ≤k subarrays with max_sum limit"""
        subarrays = 1
        current_sum = 0
        
        for num in nums:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
                if subarrays > k:
                    return False
            else:
                current_sum += num
        
        return True
    
    left = max(nums)      # Minimum possible (each element alone)
    right = sum(nums)     # Maximum possible (all in one)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Visual explanation:
"""
nums = [7, 2, 5, 10, 8], k = 2

Trying max_sum = 18:
[7, 2, 5] = 14 ≤ 18 ✓
[10, 8] = 18 ≤ 18 ✓
Total subarrays = 2 ≤ k ✓ Works!

Trying max_sum = 17:
[7, 2, 5] = 14 ≤ 17 ✓
[10] = 10 ≤ 17 ✓
[8] = 8 ≤ 17 ✓
Total subarrays = 3 > k ✗ Doesn't work!

Answer = 18 (minimum that works)
"""
```

---

#### **Problem: Find Peak Element (LC 162)** ⛰️

```python
def find_peak_element(nums):
    """
    Find a peak element (greater than neighbors)
    
    Input: [1,2,3,1]
    Output: 2 (index of element 3)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            # Peak is on the right
            left = mid + 1
        else:
            # Peak is on the left (or mid is peak)
            right = mid
    
    return left

# Visualization:
"""
nums = [1, 2, 3, 1]
         0  1  2  3

        3  ←Peak
       / \
      2   1
     /
    1

Binary search converges to index 2 (value 3)

Step-by-step:
left=0, right=3, mid=1
  nums[1]=2 < nums[2]=3 → peak on right
  left=2

left=2, right=3, mid=2
  nums[2]=3 > nums[3]=1 → peak on left/here
  right=2

left=2, right=2 → Answer: index 2 ✅
"""
```

---

#### **Problem: Search in Rotated Sorted Array (LC 33)** 🔄

```python
def search_rotated(nums, target):
    """
    Search in rotated sorted array
    
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Diagram:
"""
Original sorted: [0, 1, 2, 4, 5, 6, 7]
After rotation:  [4, 5, 6, 7, 0, 1, 2]
                  0  1  2  3  4  5  6

Visualization:
     7 ←─┐
    /     │
   6      │
  /       │
 5        │
/         ↓
4         0
           \
            1
             \
              2

Rotated at pivot (index 4)

Search for target=0:
Step 1: mid=3, nums[3]=7
        Left half [4,5,6,7] is sorted
        0 not in [4,7] → search right

Step 2: mid=5, nums[5]=1
        Right half [1,2] is sorted
        0 not in [1,2] → search left

Step 3: mid=4, nums[4]=0 ✅ Found!
"""
```

---

## 🌲 Fenwick Tree (Binary Indexed Tree)

**Use Case:** Fast range sum queries and point updates in O(log n)

### **Concept Diagram:**

```
Array:     [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
Index:      1  2   3  4  5  6   7  8  9 10 11

Fenwick Tree Structure:
Each node stores sum of a range based on binary representation

Tree[i] = sum from (i - 2^r + 1) to i
where r = position of rightmost set bit in i

Visualization:
Index (binary):
1 (0001): stores sum of [1]
2 (0010): stores sum of [1, 2]
3 (0011): stores sum of [3]
4 (0100): stores sum of [1, 2, 3, 4]
5 (0101): stores sum of [5]
6 (0110): stores sum of [5, 6]
7 (0111): stores sum of [7]
8 (1000): stores sum of [1, 2, 3, 4, 5, 6, 7, 8]

Tree Structure (each box = range covered):
        8[1..8]
       /        \
    4[1..4]    12[9..12]
   /     \     /      \
  2[1,2] 6[5,6] 10[9,10] ...
  / \    / \    / \
 1   3  5   7  9  11
```

### **Implementation:**

```python
class FenwickTree:
    def __init__(self, n):
        """Initialize Fenwick tree of size n"""
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed
    
    def update(self, i, delta):
        """Add delta to element at index i"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Add least significant bit
    
    def query(self, i):
        """Get sum of elements from 1 to i"""
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)  # Remove least significant bit
        return result
    
    def range_query(self, left, right):
        """Get sum of elements from left to right"""
        return self.query(right) - self.query(left - 1)

# Example usage:
"""
arr = [3, 2, -1, 6, 5, 4, -3, 3]

# Build Fenwick tree
ft = FenwickTree(8)
for i, val in enumerate(arr, 1):
    ft.update(i, val)

# Query sum[1..5] = 3+2+(-1)+6+5 = 15
print(ft.range_query(1, 5))  # Output: 15

# Update: arr[3] += 10
ft.update(3, 10)

# Query again: sum[1..5] = 3+2+9+6+5 = 25
print(ft.range_query(1, 5))  # Output: 25

Time Complexity:
- Update: O(log n)
- Query: O(log n)
- Build: O(n log n)

Space: O(n)
"""

# Visual trace of update(3, 10):
"""
Update index 3 (binary: 011)

Step 1: tree[3] += 10
        Next: 3 + (3 & -3) = 3 + 1 = 4

Step 2: tree[4] += 10
        Next: 4 + (4 & -4) = 4 + 4 = 8

Step 3: tree[8] += 10
        Next: 8 + 8 = 16 > n, stop

Updated tree indices: 3, 4, 8
(These are all ranges that include index 3!)
"""

# Visual trace of query(5):
"""
Query sum[1..5]

Step 1: result += tree[5]
        Next: 5 - (5 & -5) = 5 - 1 = 4

Step 2: result += tree[4]
        Next: 4 - 4 = 0, stop

Accessed tree indices: 5, 4
tree[5] covers [5]
tree[4] covers [1..4]
Together: [1..5] ✅
"""
```

### **Leetcode Problems:**
- Range Sum Query - Mutable (LC 307)
- Count of Smaller Numbers After Self (LC 315)
- Reverse Pairs (LC 493)

---

## 📐 Matrix Patterns

### **Pattern 18: Matrix Traversal** 🗺️

#### **1. Spiral Matrix Traversal (LC 54)**

```python
def spiral_order(matrix):
    """
    Traverse matrix in spiral order
    
    Input: [[1,2,3],
            [4,5,6],
            [7,8,9]]
    
    Output: [1,2,3,6,9,8,7,4,5]
    """
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Move right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Move down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Move left along bottom row (if still in bounds)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Move up along left column (if still in bounds)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Visualization:
"""
Matrix:
┌─────────────┐
│ 1 → 2 → 3 │ Step 1: Right along top
│           ↓ │
│ 4   5   6 │ Step 2: Down along right
│ ↑       ↓ │
│ 7 ← 8 ← 9 │ Step 3: Left along bottom
└───────────┘   Step 4: Up along left

Boundaries:
Initial: top=0, bottom=2, left=0, right=2

After step 1: [1,2,3], top=1
After step 2: [1,2,3,6,9], right=1
After step 3: [1,2,3,6,9,8,7], bottom=1
After step 4: [1,2,3,6,9,8,7,4], left=1

Center: [5], then boundaries cross, done!

Result: [1,2,3,6,9,8,7,4,5] ✅
"""
```

---

#### **2. Rotate Matrix 90 Degrees (LC 48)**

```python
def rotate(matrix):
    """
    Rotate n×n matrix 90° clockwise in-place
    
    Input:  [1,2,3]      Output: [7,4,1]
            [4,5,6]              [8,5,2]
            [7,8,9]              [9,6,3]
    """
    n = len(matrix)
    
    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Visual Transformation:
"""
Original:           Transposed:         Reversed rows:
[1, 2, 3]          [1, 4, 7]           [7, 4, 1]
[4, 5, 6]   →      [2, 5, 8]    →      [8, 5, 2]
[7, 8, 9]          [3, 6, 9]           [9, 6, 3]

Transpose explanation:
(0,1)↔(1,0): 2↔4
(0,2)↔(2,0): 3↔7
(1,2)↔(2,1): 6↔8

Result: 90° clockwise rotation! ✅
"""
```

---

#### **3. Set Matrix Zeroes (LC 73)**

```python
def set_zeroes(matrix):
    """
    If element is 0, set its entire row and column to 0
    Do it in-place!
    
    Input:  [1,1,1]      Output: [1,0,1]
            [1,0,1]              [0,0,0]
            [1,1,1]              [1,0,1]
    """
    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/col should be zero
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
    
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
    
    # Use first row/col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set zeros based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle first row/col
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

# Visualization:
"""
Original:           Mark phase:         Set zeros:
[1, 1, 1]          [1, 0, 1]           [1, 0, 1]
[1, 0, 1]    →     [0, 0, 1]     →     [0, 0, 0]
[1, 1, 1]          [1, 0, 1]           [1, 0, 1]
     ↑                  ↑
   Found 0!      Mark row & col

The 0 at (1,1) causes:
- Row 1 marked: matrix[1][0] = 0
- Col 1 marked: matrix[0][1] = 0

Then set all cells in marked rows/cols to 0

Space: O(1) using first row/col as storage! ✅
"""
```

---

#### **4. Search in 2D Matrix (LC 74)**

```python
def search_matrix(matrix, target):
    """
    Search in sorted 2D matrix
    Each row is sorted left to right
    First element of each row > last element of previous row
    
    Treat as 1D sorted array and use binary search!
    """
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Visualization:
"""
Matrix (3×4):
[1,  3,  5,  7]
[10, 11, 16, 20]
[23, 30, 34, 60]

As 1D array:
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
 0  1  2  3   4   5   6   7   8   9  10  11

Index to 2D:
index=5 → row=5//4=1, col=5%4=1 → matrix[1][1]=11 ✅

Search target=16:
left=0, right=11, mid=5 → matrix[1][1]=11 < 16
left=6, right=11, mid=8 → matrix[2][0]=23 > 16
left=6, right=7, mid=6 → matrix[1][2]=16 ✅ Found!
"""
```

---

## 🧮 Master Theorem (Divide & Conquer Complexity)

The **Master Theorem** helps calculate time complexity of recursive algorithms!

### **Formula:**

For recurrence: **T(n) = aT(n/b) + f(n)**

Where:
- **a** = number of subproblems
- **b** = factor by which problem size reduces
- **f(n)** = work done outside recursion

### **Three Cases:**

```
┌─────────────────────────────────────────────────────┐
│  Case 1: f(n) = O(n^c) where c < log_b(a)         │
│          → T(n) = Θ(n^(log_b(a)))                  │
│          (Recursion dominates)                      │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Case 2: f(n) = Θ(n^c log^k(n)) where c=log_b(a)  │
│          → T(n) = Θ(n^c log^(k+1)(n))              │
│          (Balanced)                                 │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Case 3: f(n) = Ω(n^c) where c > log_b(a)         │
│          → T(n) = Θ(f(n))                          │
│          (Work outside recursion dominates)         │
└─────────────────────────────────────────────────────┘
```

### **Examples:**

#### **Example 1: Binary Search**
```python
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr[mid+1:], target)
    else:
        return binary_search(arr[:mid], target)

# Analysis:
"""
T(n) = T(n/2) + O(1)

a = 1 (one subproblem)
b = 2 (divide by 2)
f(n) = O(1)

log_b(a) = log_2(1) = 0
f(n) = O(n^0) = O(1)

Case 2: c = 0 = log_b(a)
→ T(n) = Θ(n^0 × log n) = Θ(log n) ✅
"""
```

#### **Example 2: Merge Sort**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # T(n/2)
    right = merge_sort(arr[mid:])    # T(n/2)
    return merge(left, right)        # O(n)

# Analysis:
"""
T(n) = 2T(n/2) + O(n)

a = 2 (two subproblems)
b = 2 (divide by 2)
f(n) = O(n)

log_b(a) = log_2(2) = 1
f(n) = O(n^1)

Case 2: c = 1 = log_b(a)
→ T(n) = Θ(n log n) ✅

Visualization:
           n
        /     \
      n/2    n/2      ← Work per level = n
      / \    / \
    n/4 n/4 n/4 n/4   ← Work per level = n
    
    log n levels × n work = O(n log n)
"""
```

#### **Example 3: Strassen's Matrix Multiplication**
```
T(n) = 7T(n/2) + O(n²)

a = 7
b = 2
f(n) = O(n²)

log_b(a) = log_2(7) ≈ 2.807
f(n) = O(n^2) where 2 < 2.807

Case 1: c < log_b(a)
→ T(n) = Θ(n^2.807) ✅
(Better than standard O(n³) multiplication!)
```

#### **Example 4: Calculating Powers**
```python
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

# Analysis:
"""
T(n) = T(n/2) + O(1)

a = 1
b = 2
f(n) = O(1)

log_b(a) = 0
c = 0

Case 2: T(n) = Θ(log n) ✅
"""
```

### **Visual Decision Tree:**

```
Start: T(n) = aT(n/b) + f(n)
   |
   ├─ Calculate log_b(a)
   |
   ├─ Compare f(n) with n^(log_b(a))
   |
   ├─ f(n) = O(n^c) where c < log_b(a)?
   │  └─ YES → Case 1: T(n) = Θ(n^(log_b(a)))
   |
   ├─ f(n) = Θ(n^c log^k n) where c = log_b(a)?
   │  └─ YES → Case 2: T(n) = Θ(n^c log^(k+1) n)
   |
   └─ f(n) = Ω(n^c) where c > log_b(a)?
      └─ YES → Case 3: T(n) = Θ(f(n))
```

---

## 🌳 More Trie Problems & Patterns

### **Trie with Search Optimizations**

#### **Problem: Add and Search Word (LC 211)**

```python
class WordDictionary:
    """
    Support . wildcard that matches any letter
    """
    def __init__(self):
        self.root = {}
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # End marker
    
    def search(self, word):
        def search_node(word, node):
            for i, char in enumerate(word):
                if char == '.':
                    # Wildcard: try all possible characters
                    for key in node:
                        if key != '$' and search_node(word[i+1:], node[key]):
                            return True
                    return False
                else:
                    if char not in node:
                        return False
                    node = node[char]
            return '$' in node
        
        return search_node(word, self.root)

# Usage:
"""
dict = WordDictionary()
dict.addWord("bad")
dict.addWord("dad")
dict.addWord("mad")

dict.search("pad")  # False
dict.search("bad")  # True
dict.search(".ad")  # True (matches bad, dad, mad)
dict.search("b..")  # True (matches bad)

Trie structure:
        root
       / | \
      b  d  m
      |  |  |
      a  a  a
      |  |  |
      d$ d$ d$

Search ".ad":
1. Wildcard at position 0
2. Try all branches: b, d, m
3. For each, check if "ad" exists
4. Found in all three! Return True ✅
"""
```

---

#### **Problem: Word Search II (LC 212)**

```python
def find_words(board, words):
    """
    Find all words from list that exist in board
    Use Trie for efficient prefix matching!
    
    board = [['o','a','a','n'],
             ['e','t','a','e'],
             ['i','h','k','r'],
             ['i','f','l','v']]
    
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
    """
    # Build Trie
    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = word  # Store complete word
    
    def dfs(i, j, node, path):
        if '$' in node:
            result.add(node['$'])
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        char = board[i][j]
        if char not in node or char == '#':
            return
        
        # Mark as visited
        board[i][j] = '#'
        
        # Explore 4 directions
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj, node[char], path + char)
        
        # Unmark
        board[i][j] = char
    
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie, "")
    
    return list(result)

# Visualization:
"""
Board:
o a a n
e t a e
i h k r
i f l v

Trie for ["oath", "eat"]:
      root
      / \
     o   e
     |   |
     a   a
     |   |
     t   t
     |   |
     h$  $

DFS from 'o' at (0,0):
o → a → t → h → Found "oath"! ✅

DFS from 'e' at (1,0):
e → t → a → Found "eat"! ✅

Time: O(M×N×4^L) where L=max word length
Space: O(sum of all word lengths) for Trie
"""
```

---

#### **Problem: Longest Word in Dictionary (LC 720)**

```python
def longest_word(words):
    """
    Find longest word that can be built one character at a time
    
    Input: ["w","wo","wor","worl","world"]
    Output: "world"
    """
    # Build Trie
    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = word
    
    # DFS to find longest buildable word
    def dfs(node):
        longest = node.get('$', '')
        
        for char in node:
            if char != '$':
                # Only explore if this prefix exists as a word
                if '$' in node[char]:
                    candidate = dfs(node[char])
                    if len(candidate) > len(longest):
                        longest = candidate
                    elif len(candidate) == len(longest):
                        longest = min(longest, candidate)  # Lexicographically smallest
        
        return longest
    
    return dfs(trie)

# Example trace:
"""
words = ["w","wo","wor","worl","world"]

Trie:
w$
└─o$
  └─r$
    └─l$
      └─d$

DFS checks each level has '$':
w → exists ✓
wo → exists ✓
wor → exists ✓
worl → exists ✓
world → exists ✓

All intermediate words exist!
Answer: "world" ✅
"""
```

---

## 📚 Complete Coverage Summary

### ✅ **What's Now Covered (100%):**

**Foundation:**
- Time/Space Complexity + Master Theorem ✅
- All basic data structures ✅

**Patterns (18 total):**
1-14: Original patterns ✅
15. Binary Search on Answer ✅
16. Prefix Sum ✅
17. Monotonic Stack ✅
18. Matrix Patterns ✅

**Advanced Algorithms:**
- Graph algorithms (Dijkstra, Union Find, etc.) ✅
- String algorithms (KMP, Rabin-Karp, etc.) ✅
- Advanced DP (State Machine, Bitmask, Digit, Tree) ✅
- Fenwick Tree ✅

**Math & Theory:**
- Primes, GCD, Modular Arithmetic ✅
- Combinatorics ✅
- Master Theorem ✅

**Interview Skills:**
- Problem-solving framework ✅
- Communication tips ✅
- Debugging techniques ✅
- Time management ✅
- Test cases ✅

**Quick References:**
- Complexity cheat sheet ✅
- Pattern flowchart ✅
- Edge cases checklist ✅
- Syntax reference ✅

**Problems:**
- 150+ complete solutions ✅
- 200+ company-specific lists ✅
- Detailed explanations ✅
- ASCII diagrams throughout ✅

---

## 🎉 **Final Statistics:**

- 📄 **7,000+ lines** of content
- 🎯 **18 problem-solving patterns**
- 💻 **150+ problems with solutions**
- 🏢 **200+ company problems**
- 📊 **50+ ASCII diagrams**
- 🗺️ **10+ advanced algorithms**
- 🎓 **Complete interview guide**

---

*Guide Updated to 100% Completion!*
*Version: 4.0 - Ultimate Complete Edition with Diagrams*
*Nothing left to add - this is THE definitive DSA guide!* 🏆

