# Data Structures & Algorithms — Zero to Hero

> **One path, end to end:** theory → simple code → your session notebooks → FAANG-style problems.  
> All **49 labs** from your `Code Files & Session Notes` folder live under `system-design/dsa-labs/` and appear in the sidebar by phase.

---

## How to use this path

| Step | What to do | Time |
|------|------------|------|
| 1 | Read the **phase goal** below (5 min) | 5 min |
| 2 | Skim the **mini example** — type it once yourself | 15 min |
| 3 | Open the **lab notebook** in the sidebar and run every cell | 30–60 min |
| 4 | For depth (diagrams, proofs), use **Complete DSA Reference** in the sidebar | as needed |
| 5 | Log progress in `LEARNING-CHECKPOINTS.md` | 2 min |

**Language:** Python (matches your notebooks). JavaScript developers: same ideas; use the Complete DSA Reference for JS snippets where noted.

---

## Full curriculum (phases)

| Phase | Topics | Labs in sidebar |
|-------|--------|-----------------|
| **1 — Foundations** | Arrays, recursion, basic DP intro | 4 notebooks |
| **2 — Sorting & divide-conquer** | Bubble/insertion/selection, merge/quick, binary & ternary search | 14 notebooks |
| **3 — Linked lists** | Insert, search, reverse, merge, Floyd cycle | 7 notebooks |
| **4 — Stack & queue** | Array + linked-list implementations | 2 notebooks |
| **5 — Trees & BST** | Traversals, insert/search/delete, min value | 5 notebooks |
| **6 — Graphs** | BFS, DFS, Dijkstra | 3 notebooks |
| **7 — DP & greedy** | 0/1 & fractional knapsack, job sequencing, stairs, Huffman | 5 notebooks |
| **8 — Hashing** | Hash functions | 1 notebook |
| **9 — FAANG patterns** | Two pointers, top-K, arrays, parentheses, etc. | 9 notebooks |

**Deep reference:** [Complete DSA Reference](../guides/fundamentals/data-structures-algorithms-zero-to-hero.md) — 60+ ASCII diagrams, full complexity tables, interview bank.

**System design (after DSA):** [Complete System Design Guide](./COMPLETE-SYSTEM-DESIGN-GUIDE.md) → [Practice Track](./SYSTEM-DESIGN-PRACTICE-TRACK.md).

---

## Complexity cheat sheet (memorize this)

| Structure / algo | Access | Search | Insert | Delete | Notes |
|------------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) end | O(n) | cache-friendly |
| Linked list | O(n) | O(n) | O(1) if ptr | O(1) if ptr | no random access |
| Stack / queue | — | — | O(1) | O(1) | array or linked list |
| BST (balanced) | — | O(log n) | O(log n) | O(log n) | inorder → sorted |
| Hash table | — | O(1)* | O(1)* | O(1)* | *average |
| Heap | — | — | O(log n) | O(log n) | min/max at root |
| Merge sort | — | — | — | — | O(n log n), stable |
| Quick sort | — | — | — | — | O(n log n) avg |
| BFS / DFS | — | — | — | — | O(V + E) |
| Dijkstra | — | — | — | — | O((V+E) log V) with heap |

---

## Phase 1 — Foundations

**Goal:** Comfort with arrays, indexing, recursion, and the idea of memoization.

### Mini example — array + linear scan

```python
def max_value(arr: list[int]) -> int:
    if not arr:
        raise ValueError("empty array")
    best = arr[0]
    for x in arr[1:]:
        if x > best:
            best = x
    return best

print(max_value([2, 1, 8, 9, 12, 15]))  # 15
```

### Mini example — recursion (factorial)

```python
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Labs

- `Array Data Structure Implementation.ipynb`
- `Sum_Of_Natural_Numbers.ipynb`
- `Factorial Finding using Recursion with its Implementation.ipynb`
- `Fibonacci_Series_using_Dynamic_Programming.ipynb`

---

## Phase 2 — Sorting & divide-and-conquer

**Goal:** Know *when* to use each sort; implement merge/quick; binary search on sorted data.

### Mini example — binary search

```python
def binary_search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### Pattern

- **Comparison sorts** (bubble, insertion, selection): learning only — O(n²) in interviews use as warm-up.
- **Merge / quick sort**: divide-and-conquer templates for harder problems.
- **Binary / ternary search**: sorted arrays, answer-space search.

Open **Phase 2** in the sidebar for all sort and search labs.

---

## Phase 3 — Linked lists

**Goal:** Singly linked list insert (front/end/after), search, reverse, merge two sorted lists, Floyd cycle detection.

### Mini example — reverse (iterative)

```python
class Node:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.next = nxt

def reverse_head(head: Node | None) -> Node | None:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```

### Labs

All under **Phase 3 — Linked Lists** in the sidebar (insertion, search, FAANG merge/reverse/cycle).

---

## Phase 4 — Stack & queue

**Goal:** LIFO vs FIFO; implement with array (fixed size) and linked list.

### Mini example — valid parentheses (stack)

```python
def is_valid(s: str) -> bool:
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

### Labs

- `Implementation of Stack using array and linked list.ipynb`
- `Implementation of Queue using array and linked list.ipynb`
- Also: `FAANG Interview Question - Valid Parenthesis.ipynb` (Phase 9)

---

## Phase 5 — Trees & BST

**Goal:** Inorder / preorder / postorder; BST insert, search, delete; min node.

### Mini example — inorder traversal (recursive)

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

BST property: **left < root < right**. Use for O(log n) search when balanced.

### Labs

**Phase 5** in sidebar — traversals, insertion/inorder, search, delete, minimum value, unique BST count.

---

## Phase 6 — Graphs

**Goal:** Represent graph (adjacency list); BFS for shortest path in unweighted graphs; DFS for connectivity; Dijkstra for weighted shortest path.

### Mini example — BFS (unweighted)

```python
from collections import deque

def bfs(adj: dict[str, list[str]], start: str) -> list[str]:
    seen = {start}
    order = []
    q = deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v)
                q.append(v)
    return order
```

### Labs

- `BFS Coding Implementation.ipynb`
- `DFS Coding Implementation.ipynb`
- `Single Source Shortest Path- Dijkstra's algorithm Implementation.py`

---

## Phase 7 — DP & greedy

**Goal:** Recognize overlapping subproblems; 0/1 knapsack vs fractional (greedy); classic counting DP (stairs).

### Mini example — 0/1 knapsack (bottom-up)

```python
def knapsack_01(weights: list[int], values: list[int], cap: int) -> int:
    n = len(weights)
    dp = [0] * (cap + 1)
    for i in range(n):
        for w in range(cap, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[cap]
```

### Labs

Knapsack (0/1 and fractional), job sequencing, stairs, Huffman — **Phase 7** in sidebar.

---

## Phase 8 — Hashing

**Goal:** Hash function intuition; collision handling (chaining / open addressing); O(1) average lookup.

### Lab

- `Implementation_of_Hash_Functions.ipynb`

---

## Phase 9 — FAANG interview patterns

| Pattern | When to use | Example labs |
|---------|-------------|--------------|
| **Two pointers** | Sorted array, pair sum, partition | Two Pointers Problem, Sort Colors |
| **Sliding window** | Subarray with constraint | Best Time Buy/Sell (variant) |
| **Heap / top-K** | K largest/smallest | Top K frequent, K closest points |
| **Fast & slow pointers** | Cycle in linked list | Floyd's Cycle Detection |
| **Stack** | Matching brackets, monotonic stack | Valid Parenthesis |

Work through **Phase 9** labs after Phases 1–8. Time yourself: 25–35 min per medium problem.

---

## 8-week study plan

| Week | Focus | Target |
|------|-------|--------|
| 1 | Phase 1 + array habits | 4 labs + complexity notes |
| 2 | Phase 2 sorts + binary search | 8 labs |
| 3 | Phase 3 linked lists | 7 labs |
| 4 | Phase 4–5 stack, queue, trees | 7 labs |
| 5 | Phase 6 graphs | 3 labs + redraw BFS/DFS |
| 6 | Phase 7 DP/greedy | 5 labs |
| 7 | Phase 8–9 hashing + patterns | 10 labs |
| 8 | Mixed review + system design start | 5 old labs + 1 SD prompt |

---

## What was merged from your session notes

All files from `Code Files & Session Notes` are copied into:

`tech-mastery-notebooks/system-design/dsa-labs/`

Nothing was deleted from your original folder. The web app sidebar lists every notebook by phase so you have **one place** to learn DSA next to system design interviews.

---

## Next steps

1. Open **Phase 1 — Foundations** in the sidebar and run the array notebook.
2. Bookmark **Complete DSA Reference** for theory when a lab feels thin.
3. When comfortable with Phases 1–6, start [System Design Practice Track](./SYSTEM-DESIGN-PRACTICE-TRACK.md) (L1 prompts).

*Last updated: consolidated from 49 session notebooks into `system-design/dsa-labs/`.*
