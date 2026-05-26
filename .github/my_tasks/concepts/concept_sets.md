# Sets in Python - Complete Revision Notes

## 1) What is a set?
A set is an unordered collection of unique values.
- Unordered: no fixed index position.
- Unique: duplicates are removed automatically.
- Mutable: can add/remove items.
- Best for membership checks and set algebra.

Example:
```python
tags = {"safe", "unsafe", "safe"}
print(tags)  # {'safe', 'unsafe'}
```

---

## 2) Why sets are needed (problem-first view)
Use sets when duplicates are not allowed and you need fast lookups.

Common real-world problems:
- Remove duplicate test IDs.
- Check whether value exists in allowed/blocked set.
- Compare expected vs actual fields quickly.

Set solution:
- Guarantees uniqueness.
- Supports operations like union/intersection/difference.

---

## 3) Set creation syntax
### Basic set
```python
s1 = {1, 2, 3}
```

### From list (duplicates removed)
```python
s2 = set([1, 2, 2, 3])
print(s2)  # {1, 2, 3}
```

### Empty set (important)
```python
empty_set = set()
```

Note:
```python
empty_dict = {}  # this is dict, not set
```

---

## 4) Accessing values in a set
Sets are unordered, so no indexing/slicing.

```python
colors = {"red", "green", "blue"}
# colors[0]  # TypeError
```

How to read values:
- Iterate with loop.
- Convert to list if indexing is needed.

```python
for c in colors:
    print(c)
```

---

## 5) `add(x)`
Adds one item to the set.

```python
statuses = {"PASS", "FAIL"}
statuses.add("SKIP")
print(statuses)
```

If item already exists, no duplication happens.

---

## 6) `update(iterable)`
Adds multiple items from iterable.

```python
statuses = {"PASS"}
statuses.update(["FAIL", "SKIP", "PASS"])
print(statuses)  # {'PASS', 'FAIL', 'SKIP'}
```

---

## 7) `remove(x)`
Removes item by value.

```python
codes = {200, 404, 500}
codes.remove(404)
print(codes)
```

Important:
- Raises `KeyError` if item does not exist.

---

## 8) `discard(x)`
Removes item if present.

```python
codes = {200, 404, 500}
codes.discard(401)  # no error
print(codes)
```

Difference from `remove()`:
- `discard()` is safe if value may be missing.

---

## 9) `pop()`
Removes and returns an arbitrary item.

```python
items = {"a", "b", "c"}
removed = items.pop()
print(removed)
print(items)
```

Important:
- Not predictable order.

---

## 10) `clear()`
Removes all items from set.

```python
items = {1, 2, 3}
items.clear()
print(items)  # set()
```

---

## 11) `copy()`
Returns a shallow copy of set.

```python
original = {"tc1", "tc2"}
working = original.copy()
working.add("tc3")

print(original)  # {'tc1', 'tc2'}
print(working)   # {'tc1', 'tc2', 'tc3'}
```

---

## 12) Set operations (most important)
Let:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union (`|`)
All unique items from both sets.
```python
print(A | B)  # {1, 2, 3, 4, 5, 6}
```

### Intersection (`&`)
Common items.
```python
print(A & B)  # {3, 4}
```

### Difference (`-`)
Items in first set but not second.
```python
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
```

### Symmetric difference (`^`)
Items in either set, but not both.
```python
print(A ^ B)  # {1, 2, 5, 6}
```

---

## 13) Membership checks
Fast lookup with `in`.

```python
SUCCESS_CODES = {200, 201, 204}

if 201 in SUCCESS_CODES:
    print("Success")
```

---

## 14) Useful set comparison methods
```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))    # True
print(B.issuperset(A))  # True
print(A.isdisjoint({5, 6}))  # True
```

Use cases:
- Validate expected fields are present (`subset`).
- Check no overlap in blocked/allowed words (`isdisjoint`).

---

## 15) Frozen set (`frozenset`)
Immutable version of set.

```python
fs = frozenset([1, 2, 3])
print(fs)
# fs.add(4)  # AttributeError
```

Use when:
- You need set-like structure that must not change.
- You need hashable set-like object for dict keys.

---

## 16) Real-time usage examples (automation + AI testing)
### A) Remove duplicate test IDs
```python
test_ids = ["TC01", "TC02", "TC01", "TC03"]
unique_ids = set(test_ids)
print(unique_ids)
```

### B) Find missing API fields
```python
expected = {"id", "name", "email", "status"}
actual = {"id", "name", "status"}

missing = expected - actual
print(missing)  # {'email'}
```

### C) Detect risky prompt words
```python
blocked_words = {"hack", "bypass", "exploit"}
prompt_words = {"please", "bypass", "login"}

risky = blocked_words & prompt_words
print(risky)  # {'bypass'}
```

### D) Compare labels from two model runs
```python
run1 = {"SAFE", "TOXIC", "SPAM"}
run2 = {"SAFE", "SPAM", "BIAS"}

print("Common:", run1 & run2)
print("Only run1:", run1 - run2)
print("Only run2:", run2 - run1)
```

### E) Validate expected status codes
```python
allowed = {200, 201, 204}
received = {200, 500}

unexpected = received - allowed
print(unexpected)  # {500}
```

---

## 17) Common mistakes and fixes
1. Creating empty set incorrectly
```python
x = {}       # dict
x = set()    # set
```

2. Expecting order from set
```python
s = {"a", "b", "c"}
# s[0]  # invalid
```

3. Using `remove()` when value may not exist
```python
# s.remove("missing")  # KeyError
s.discard("missing")    # safe
```

4. Assuming `pop()` removes "last" item
- Sets are unordered, so `pop()` removes arbitrary item.

---

## 18) Mini cheat sheet
```python
# Create
{1, 2, 3}
set([1, 2, 2, 3])
set()

# Add
s.add(x)
s.update(iterable)

# Remove
s.remove(x)
s.discard(x)
s.pop()
s.clear()

# Copy
new_s = s.copy()

# Operations
A | B   # union
A & B   # intersection
A - B   # difference
A ^ B   # symmetric difference

# Checks
x in s
A.issubset(B)
B.issuperset(A)
A.isdisjoint(B)
```

---

## 19) Practice prompts (self-assignment)
1. Remove duplicate endpoints from a list using `set()`.
2. Add one blocked word using `add()`.
3. Add multiple tags using `update()`.
4. Safely remove optional value using `discard()`.
5. Count missing fields using `expected - actual`.
6. Find common failed tests from two sets using `&`.
7. Get all unique labels from two model runs using `|`.
8. Check if expected labels are subset of actual labels.
9. Use `isdisjoint()` to verify no blocked words appear.
10. Create `frozenset` for fixed allowed status codes.

---

## 20) Summary
- Set stores unique values only.
- Best for deduplication, membership checks, and comparisons.
- Core operations: add/remove, union/intersection/difference.
- Use `discard()` for safe removal and `frozenset` for immutable set-like data.

