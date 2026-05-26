# Lists in Python - Complete Revision Notes

## 1) What is a list?
A list is an ordered, mutable collection of values.
- Ordered: keeps insertion order.
- Indexed: access items by position.
- Mutable: can be changed after creation.
- Allows duplicate values.
- Can contain mixed data types.

Example:
```python
items = ["login", "search", "checkout"]
```

---

## 2) Why lists are needed (problem-first view)
Use lists when data changes during runtime.

Common real-world need:
- Add new test cases.
- Remove flaky cases.
- Reorder execution plan.
- Count or search values.

List solution:
- Lists support add, remove, update, sort, reverse, and copy operations.

---

## 3) List creation syntax
### Basic list
```python
tests = ["tc1", "tc2", "tc3"]
```

### Empty list
```python
empty = []
```

### List from iterable
```python
nums = list((1, 2, 3))
```

---

## 4) Accessing list values
### Indexing
```python
steps = ["start", "run", "end"]
print(steps[0])   # start
print(steps[-1])  # end
```

### Slicing
```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])  # [20, 30, 40]
```

---

## 5) `append(x)`
Adds one item to the end of the list.

```python
tasks = ["login", "search"]
tasks.append("checkout")
print(tasks)  # ['login', 'search', 'checkout']
```

Use when:
- You need to add exactly one item.

---

## 6) `extend(iterable)`
Adds all items from another iterable to the end of the list.

```python
tasks = ["login", "search"]
tasks.extend(["checkout", "logout"])
print(tasks)  # ['login', 'search', 'checkout', 'logout']
```

Use when:
- You need to add multiple items.

---

## 7) `insert(index, value)`
Inserts an item at a specific index.

```python
plan = ["regression", "api", "ui"]
plan.insert(0, "smoke")
print(plan)  # ['smoke', 'regression', 'api', 'ui']
```

Use when:
- Position/order matters.

---

## 8) `remove(value)`
Removes the first matching item by value.

```python
cases = ["login", "flaky", "search", "flaky"]
cases.remove("flaky")
print(cases)  # ['login', 'search', 'flaky']
```

Note:
- Removes only first match.
- Raises `ValueError` if value not found.

---

## 9) `pop([index])`
Removes and returns an item by index (last by default).

```python
queue = ["tc1", "tc2", "tc3"]
last = queue.pop()
print(last)   # tc3
print(queue)  # ['tc1', 'tc2']
```

```python
queue = ["tc1", "tc2", "tc3"]
first = queue.pop(0)
print(first)  # tc1
print(queue)  # ['tc2', 'tc3']
```

Use when:
- You need the removed value for further processing.

---

## 10) `clear()`
Removes all items from the list.

```python
retry_queue = ["job1", "job2"]
retry_queue.clear()
print(retry_queue)  # []
```

---

## 11) `index(value)`
Returns the index of the first matching item.

```python
statuses = ["PASS", "PASS", "FAIL", "PASS"]
pos = statuses.index("FAIL")
print(pos)  # 2
```

Note:
- Raises `ValueError` if value is not present.

---

## 12) `count(value)`
Returns how many times a value appears in the list.

```python
codes = [200, 500, 200, 404, 200]
print(codes.count(200))  # 3
```

---

## 13) `sort(key=None, reverse=False)`
Sorts the list in place (ascending by default).

```python
scores = [0.82, 0.91, 0.76]
scores.sort()
print(scores)  # [0.76, 0.82, 0.91]
```

Descending sort:
```python
scores = [0.82, 0.91, 0.76]
scores.sort(reverse=True)
print(scores)  # [0.91, 0.82, 0.76]
```

Important:
- `sort()` modifies original list.
- `sort()` returns `None`.

---

## 14) `reverse()`
Reverses the order of items in place.

```python
events = ["start", "login", "run", "end"]
events.reverse()
print(events)  # ['end', 'run', 'login', 'start']
```

Difference from `sort(reverse=True)`:
- `reverse()` flips current order only.
- `sort(reverse=True)` sorts by value in descending order.

---

## 15) `copy()`
Returns a shallow copy of the list.

```python
original = ["tc1", "tc2", "tc3"]
working = original.copy()
working.pop()

print(original)  # ['tc1', 'tc2', 'tc3']
print(working)   # ['tc1', 'tc2']
```

Why important:
- Prevents accidental mutation of original test data.

---

## 16) Real-time usage examples (automation + AI testing)
### A) Build execution list
```python
run_plan = ["api_login", "api_search"]
run_plan.append("api_checkout")
```

### B) Add batch prompts
```python
prompts = ["summarize", "classify"]
prompts.extend(["translate", "extract"])
```

### C) Count failures
```python
results = ["PASS", "FAIL", "PASS", "FAIL"]
print(results.count("FAIL"))  # 2
```

### D) Rank token usage
```python
tokens = [820, 1540, 430, 1200]
tokens.sort(reverse=True)
print(tokens)  # [1540, 1200, 820, 430]
```

### E) Preserve baseline data
```python
baseline = ["record1", "record2"]
working = baseline.copy()
working.append("record3")
```

---

## 17) Common mistakes and fixes
1. Using `append()` with a list when you wanted flat items
```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]
```
Use `extend()` for flat merge:
```python
a = [1, 2]
a.extend([3, 4])
print(a)  # [1, 2, 3, 4]
```

2. Expecting `sort()` to return list
```python
nums = [3, 1, 2]
result = nums.sort()
print(result)  # None
```

3. Calling `index()`/`remove()` on missing value without handling
```python
# nums.index(999)  # ValueError
# nums.remove(999) # ValueError
```

---

## 18) Mini cheat sheet
```python
# Add
lst.append(x)
lst.extend(items)
lst.insert(i, x)

# Remove
lst.remove(x)
lst.pop()
lst.pop(i)
lst.clear()

# Find
lst.index(x)
lst.count(x)

# Order
lst.sort()
lst.sort(reverse=True)
lst.reverse()

# Copy
new_lst = lst.copy()
```

---

## 19) Practice prompts (self-assignment)
1. Add one urgent test case to a run list using `append()`.
2. Add three new endpoints to a list using `extend()`.
3. Insert a smoke test at index `0` using `insert()`.
4. Remove first occurrence of `"flaky"` using `remove()`.
5. Remove and print last job from queue using `pop()`.
6. Count how many `500` values are in a status code list using `count()`.
7. Find first `"FAIL"` position using `index()`.
8. Sort confidence scores descending using `sort(reverse=True)`.
9. Reverse event history using `reverse()`.
10. Copy baseline list before editing with `copy()`.

---

## 20) Summary
- List is mutable, ordered, and index-based.
- Use lists for dynamic data that changes at runtime.
- Core operations: add, remove, find, reorder, and copy.
- `append` vs `extend` and `sort(reverse=True)` vs `reverse()` are key differences.

