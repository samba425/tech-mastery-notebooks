# LeetCode Solutions

A collection of LeetCode problems with detailed explanations and solutions in Python and JavaScript.

---

## 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table

### Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

**Constraints:**
- You may assume that each input would have exactly one solution
- You may not use the same element twice
- You can return the answer in any order
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

### Examples

```
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Real-World Analogy 🌍

Imagine you're at a grocery store with a $10 bill. You want to buy exactly 2 items that total $10. As you walk through the store:
- You see an item for $3, you remember "I need to find something for $7"
- You see an item for $5, you remember "I need to find something for $5"
- When you find that $5 item again (or another $5 item), you realize "Hey! I've seen this price before!"

This is exactly how our hash map solution works - we remember what we've seen and what we need!

### Approach 1: Brute Force ⚠️

**Idea:** Check every pair of numbers to see if they add up to the target.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

**When to use:** Only for very small arrays or when memory is extremely limited.

#### Python Implementation:
```python
def twoSum_bruteforce(nums, target):
    """Brute force approach - check all pairs"""
    n = len(nums)
    
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):  # Start from i+1 to avoid same element
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []

# Test
print(twoSum_bruteforce([2, 7, 11, 15], 9))  # Output: [0, 1]
```

#### JavaScript Implementation:
```javascript
function twoSum_bruteforce(nums, target) {
    const n = nums.length;
    
    // Check every possible pair
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {  // Start from i+1
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    
    return [];
}

// Test
console.log(twoSum_bruteforce([2, 7, 11, 15], 9));  // Output: [0, 1]
```

**Pros:** 
- Simple to understand
- No extra space needed
- Works on any input

**Cons:** 
- Very slow for large arrays (n² comparisons)
- Not acceptable for interviews

---

### Approach 2: Two-Pass Hash Map

**Idea:** First pass builds the hash map, second pass finds the complement.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**When to use:** When you want clear separation of concerns (build index, then search).

#### Python Implementation:
```python
def twoSum_twopass(nums, target):
    """Two-pass hash map approach"""
    # First pass: build the hash map
    seen = {}
    for i, num in enumerate(nums):
        seen[num] = i
    
    # Second pass: find the complement
    for i, num in enumerate(nums):
        complement = target - num
        # Check if complement exists AND it's not the same element
        if complement in seen and seen[complement] != i:
            return [i, seen[complement]]
    
    return []

# Test
print(twoSum_twopass([2, 7, 11, 15], 9))  # Output: [0, 1]
```

#### JavaScript Implementation:
```javascript
function twoSum_twopass(nums, target) {
    // First pass: build the hash map
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        seen.set(nums[i], i);
    }
    
    // Second pass: find the complement
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        // Check if complement exists AND it's not the same element
        if (seen.has(complement) && seen.get(complement) !== i) {
            return [i, seen.get(complement)];
        }
    }
    
    return [];
}

// Test
console.log(twoSum_twopass([2, 7, 11, 15], 9));  // Output: [0, 1]
```

**Pros:** 
- Clear two-step logic
- Still O(n) time complexity

**Cons:** 
- Two passes through the array
- Slightly more code
- Same space as one-pass approach

---

### Approach 3: One-Pass Hash Map (Optimal) ✅

**Idea:** Use a hash map to store numbers we've seen and their indices. For each number, check if its complement (target - current number) exists in the map.

**Time Complexity:** O(n) - Single pass through array  
**Space Complexity:** O(n) - Hash map storage

**Step-by-Step Process:**
1. Create an empty hash map
2. For each number in the array:
   - Calculate complement = target - current number
   - Check if complement exists in hash map
   - If yes: return [index of complement, current index]
   - If no: store current number and its index in hash map
3. Continue until pair is found

### Solution in Python 🐍

```python
def twoSum(nums, target):
    """
    Find two numbers in array that sum to target.
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List containing indices of the two numbers
    """
    # Dictionary to store number: index mapping
    seen = {}
    
    # Iterate through the array with index and value
    for i, num in enumerate(nums):
        # Calculate what number we need to reach target
        complement = target - num
        
        # Check if we've seen the complement before
        if complement in seen:
            # Found the pair! Return indices
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    # No solution found (won't happen per problem constraints)
    return []


# Test cases
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(twoSum([3, 3], 6))           # Output: [0, 1]
```

### Solution in JavaScript 🟨

```javascript
/**
 * Find two numbers in array that sum to target
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target sum
 * @return {number[]} - Indices of the two numbers
 */
function twoSum(nums, target) {
    // Map to store number: index mapping
    const seen = new Map();
    
    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        // Calculate what number we need to reach target
        const complement = target - num;
        
        // Check if we've seen the complement before
        if (seen.has(complement)) {
            // Found the pair! Return indices
            return [seen.get(complement), i];
        }
        
        // Store current number and its index
        seen.set(num, i);
    }
    
    // No solution found (won't happen per problem constraints)
    return [];
}

// Test cases
console.log(twoSum([2, 7, 11, 15], 9));  // Output: [0, 1]
console.log(twoSum([3, 2, 4], 6));        // Output: [1, 2]
console.log(twoSum([3, 3], 6));           // Output: [0, 1]
```

### Dry Run Example 📝

Let's trace through `nums = [2, 7, 11, 15]`, `target = 9`:

| Step | i | num | complement | seen (before) | Action | seen (after) |
|------|---|-----|------------|---------------|--------|--------------|
| 1 | 0 | 2 | 7 | {} | 7 not in seen, add 2 | {2: 0} |
| 2 | 1 | 7 | 2 | {2: 0} | 2 in seen! Return [0, 1] | - |

**Result:** `[0, 1]` ✓

### Key Insights 💡

1. **Hash Map is Key:** Trading space for time - we use extra memory to achieve O(n) time
2. **Single Pass:** We only need to go through the array once
3. **Complement Logic:** Instead of checking all pairs, we check if `target - current` exists
4. **Order Matters:** We store numbers as we see them, so we naturally find the first valid pair

### Common Mistakes to Avoid ⚠️

1. ❌ Using the same element twice (e.g., using index 0 twice)
2. ❌ Sorting the array first (this changes indices!)
3. ❌ Not handling duplicate numbers correctly
4. ❌ Returning values instead of indices

### Follow-up Question Answer

**Q: Can you come up with an algorithm that is less than O(n²) time complexity?**

**A:** Yes! The hash map approach above achieves O(n) time complexity, which is optimal for this problem. We can't do better than O(n) because we must examine each element at least once.

---

## 📊 Comparison of All Approaches

| Approach | Time | Space | Passes | Best Use Case |
|----------|------|-------|--------|---------------|
| **Brute Force** | O(n²) | O(1) | 1 | Very small arrays only |
| **Two-Pass Hash** | O(n) | O(n) | 2 | Learning/clarity |
| **One-Pass Hash** ✅ | O(n) | O(n) | 1 | **Production code** |

### Which Solution to Use?

**For Interviews:** Always use **Approach 3 (One-Pass Hash Map)** ✅
- Optimal time and space complexity
- Shows you understand hash maps
- Most efficient solution

**For Learning:** Start with **Approach 1 (Brute Force)**
- Easiest to understand
- Good starting point before optimization

**Alternative in Memory-Critical Systems:** Consider **Approach 1** if:
- Array is very small (< 100 elements)
- Memory is extremely limited
- O(n²) is acceptable for your use case

---

## 🎓 Additional Solutions (Advanced)

### Approach 4: Sorting + Two Pointers (Changes Indices!) ⚠️

**Note:** This approach only works if you **don't need to return indices**, because sorting changes the original positions.

**Time Complexity:** O(n log n) - due to sorting  
**Space Complexity:** O(n) - to store index mappings

#### Python Implementation:
```python
def twoSum_sorted(nums, target):
    """
    Sorting + Two Pointers approach
    Note: Returns values, not indices (or needs extra work for indices)
    """
    # Create list of (value, original_index) pairs
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
    # Sort by value
    indexed_nums.sort(key=lambda x: x[0])
    
    # Two pointers approach
    left = 0
    right = len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []

# Test
print(twoSum_sorted([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum_sorted([3, 2, 4], 6))       # Output: [1, 2]
```

#### JavaScript Implementation:
```javascript
function twoSum_sorted(nums, target) {
    // Create array of [value, originalIndex] pairs
    const indexedNums = nums.map((num, i) => [num, i]);
    
    // Sort by value
    indexedNums.sort((a, b) => a[0] - b[0]);
    
    // Two pointers approach
    let left = 0;
    let right = indexedNums.length - 1;
    
    while (left < right) {
        const currentSum = indexedNums[left][0] + indexedNums[right][0];
        
        if (currentSum === target) {
            // Return original indices in sorted order
            return [
                Math.min(indexedNums[left][1], indexedNums[right][1]),
                Math.max(indexedNums[left][1], indexedNums[right][1])
            ];
        } else if (currentSum < target) {
            left++;  // Need larger sum
        } else {
            right--;  // Need smaller sum
        }
    }
    
    return [];
}

// Test
console.log(twoSum_sorted([2, 7, 11, 15], 9));  // Output: [0, 1]
console.log(twoSum_sorted([3, 2, 4], 6));       // Output: [1, 2]
```

**How Two Pointers Works:**
```
Sorted array: [2, 7, 11, 15], target = 9

Step 1: left=0 (val=2), right=3 (val=15)
        2 + 15 = 17 > 9, move right left (too big)

Step 2: left=0 (val=2), right=2 (val=11)
        2 + 11 = 13 > 9, move right left

Step 3: left=0 (val=2), right=1 (val=7)
        2 + 7 = 9 = target ✓ Found it!
```

**Pros:**
- Good for finding pairs in general (without index requirement)
- Works well when array is already sorted
- No hash map needed

**Cons:**
- Slower than hash map (O(n log n) vs O(n))
- Extra complexity to track original indices
- Not the best solution for this specific problem

---

## 🎯 Summary: When to Use Each Approach

```
┌─────────────────────────────────────────────────────────┐
│  Problem Variation          →   Best Approach           │
├─────────────────────────────────────────────────────────┤
│  Return indices (original)  →   One-Pass Hash Map ✅    │
│  Return values only         →   Two Pointers (sorted)   │
│  Array already sorted       →   Two Pointers            │
│  Very small array (n < 50)  →   Brute Force             │
│  Teaching/Learning          →   Any approach            │
│  Interview/Production       →   One-Pass Hash Map ✅    │
└─────────────────────────────────────────────────────────┘
```

**Pro Interview Tip:** 
1. Start by explaining Brute Force (shows problem understanding)
2. Explain why it's not optimal (O(n²))
3. Propose One-Pass Hash Map (optimal solution)
4. Code the optimal solution
5. Mention Two Pointers as alternative (bonus points!)

---

## 📋 Template for New Problems

Copy the template below to add new LeetCode problems:

```markdown
---

## [NUMBER]. [PROBLEM NAME]

**Difficulty:** [Easy/Medium/Hard]  
**Topics:** [Topic1, Topic2, Topic3]

### Problem Statement

[Paste the problem description here]

**Constraints:**
- [Constraint 1]
- [Constraint 2]

### Examples

```
Example 1:
Input: [input]
Output: [output]
Explanation: [explanation]

Example 2:
Input: [input]
Output: [output]
```

### Real-World Analogy 🌍

[Explain the problem using a real-world scenario that's easy to understand]

### Approach: [APPROACH NAME] ✅

**Idea:** [Brief explanation of the approach]

**Time Complexity:** O(?)  
**Space Complexity:** O(?)

**Step-by-Step Process:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Solution in Python 🐍

```python
def solutionName(params):
    """
    [Brief description]
    
    Args:
        param1: [description]
        param2: [description]
    
    Returns:
        [description]
    """
    # Your solution here
    pass


# Test cases
print(solutionName(test1))  # Output: [expected]
print(solutionName(test2))  # Output: [expected]
```

### Solution in JavaScript 🟨

```javascript
/**
 * [Brief description]
 * @param {type} param1 - [description]
 * @param {type} param2 - [description]
 * @return {type} - [description]
 */
function solutionName(params) {
    // Your solution here
}

// Test cases
console.log(solutionName(test1));  // Output: [expected]
console.log(solutionName(test2));  // Output: [expected]
```

### Dry Run Example 📝

[Show step-by-step execution with a table or bullet points]

### Key Insights 💡

1. **[Insight 1]:** [Explanation]
2. **[Insight 2]:** [Explanation]
3. **[Insight 3]:** [Explanation]

### Common Mistakes to Avoid ⚠️

1. ❌ [Mistake 1]
2. ❌ [Mistake 2]
3. ❌ [Mistake 3]

```

---

## 🚀 Quick Add Guide

**To add a new problem quickly:**

1. **Copy** the template above (everything between the two `---` separators)
2. **Paste** it at the end of this file (before this guide section)
3. **Replace** all placeholders in `[brackets]` with actual content
4. **Fill in** the Python and JavaScript solutions
5. **Add** a real-world analogy to make it memorable
6. **Include** test cases and dry run examples

**Pro Tips:**
- Keep explanations simple and conversational
- Use emojis to make sections visually distinct
- Always include time/space complexity
- Add edge cases to test cases
- Number problems sequentially (1, 2, 3...)

**Common Topics to Tag:**
- Array, String, Hash Table, Two Pointers
- Stack, Queue, Linked List, Tree, Graph
- Binary Search, Sorting, Recursion, Backtracking
- Dynamic Programming, Greedy, Divide and Conquer
- Sliding Window, Heap, Trie, Union Find

---

