# Dictionaries in Python - Complete Revision Notes

## 1) What is a dictionary?
A dictionary is a key-value mapping collection.
- Mutable: can add/remove/update items
- Insertion-ordered: keeps insertion order (Python 3.7+)
- Indexed by key (not position): access by meaningful names
- Keys must be unique and hashable
- Can contain mixed value types

Example:
```python
response = {"status": 200, "message": "ok", "user_id": 101}
```

---

## 2) Why dictionaries are needed (problem-first view)

Problem with lists/tuples:
- Store API response values in a list: `[200, "ok", 101]`
- Must remember positions: `item[0]`, `item[1]`, `item[2]`
- Hard to read, error-prone

Dictionary solution:
- Store with meaningful keys: `{"status": 200, "message": "ok", "user_id": 101}`
- Access by meaning: `response["status"]`, `response["message"]`
- Self-documenting and readable

Example:
```python
# List approach (unclear)
test_result = ["TC_01", "PASS", 2.5]
print(test_result[2])  # what is 2.5?

# Dict approach (clear)
test_result = {"id": "TC_01", "status": "PASS", "duration": 2.5}
print(test_result["duration"])  # obviously the duration
```

---

## 3) Dictionary creation syntax

### Basic
```python
d1 = {"key": "value", "key2": "value2"}
```

### Empty dictionary
```python
d2 = {}
```

### Using dict() constructor
```python
d3 = dict(name="Selva", role="QA")
```

### From list of tuples
```python
pairs = [("a", 1), ("b", 2)]
d4 = dict(pairs)
```

---

## 4) Accessing dictionary values

### Direct access (strict)
```python
d = {"status": 200, "message": "ok"}
print(d["status"])      # 200
# print(d["code"])      # KeyError
```

### `get(key, default=None)` (safe)
```python
print(d.get("status"))          # 200
print(d.get("code"))            # None
print(d.get("code", "N/A"))     # N/A
```

### Membership check `in`
```python
if "status" in d:
    print("exists")
```

---

## 5) Adding and updating values

### Direct assignment
```python
d = {}
d["status"] = 200      # add
d["status"] = 404      # update
```

### `update(dict)` bulk add/update
```python
d = {"status": 200}
d.update({"message": "ok", "code": 0})
print(d)  # {'status': 200, 'message': 'ok', 'code': 0}
```

### `setdefault(key, default)` smart add
If key exists → returns value.  
If not → adds key with default.

```python
counts = {}
counts.setdefault("PASS", 0)  # adds PASS: 0
counts.setdefault("PASS", 0)  # returns 0
counts["PASS"] += 1
print(counts)  # {'PASS': 1}
```

---

## 6) Removing values

### `pop(key[, default])` remove and return
```python
d = {"status": 200, "message": "ok"}
msg = d.pop("message")
print(msg)      # ok
print(d)        # {'status': 200}

code = d.pop("code", "not_found")  # safe with default
print(code)     # not_found
```

### `popitem()` remove last pair
```python
d = {"a": 1, "b": 2, "c": 3}
k, v = d.popitem()
print(d)  # {'a': 1, 'b': 2}
```

### `del d[key]`
```python
del d["status"]
```

### `clear()`
```python
d.clear()  # {}
```

---

## 7) Iterating through dictionary

### `keys()` iterate through keys
```python
d = {"status": 200, "message": "ok"}
for key in d.keys():
    print(key)
# status
# message
```

### `values()` iterate through values
```python
for value in d.values():
    print(value)
# 200
# ok
```

### `items()` iterate through key-value pairs (most useful)
```python
for key, value in d.items():
    print(f"{key}: {value}")
# status: 200
# message: ok
```

---

## 8) Create defaults and templates

### `fromkeys(iterable, value)` create template
```python
fields = ["id", "status", "message"]
template = dict.fromkeys(fields, None)
print(template)
# {'id': None, 'status': None, 'message': None}
```

### `copy()` shallow copy
```python
original = {"a": 1, "b": 2}
working = original.copy()
working["a"] = 99
print(original)  # {'a': 1, 'b': 2}  unchanged
```

---

## 9) Other useful operations

### `len()` count items
```python
d = {"a": 1, "b": 2}
print(len(d))  # 2
```

### Merge dictionaries (Python 3.9+)
```python
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 2}
```

---

## 10) Dictionary comprehension
```python
# Create dict from list
items = ["a", "b", "c"]
d = {item: len(item) for item in items}
print(d)  # {'a': 1, 'b': 1, 'c': 1}

# Transform values
scores = {"TC_01": 0.85, "TC_02": 0.92}
doubled = {k: v * 2 for k, v in scores.items()}
print(doubled)  # {'TC_01': 1.7, 'TC_02': 1.84}
```

---

## 11) Real-time usage examples (automation + AI testing)

### A) API response safe access
```python
response = {"status": 200, "data": {"id": 10}}
status = response.get("status", 0)
error = response.get("error", "No error")
```

### B) Count label frequencies
```python
labels = ["SAFE", "TOXIC", "SAFE", "SPAM"]
freq = {}
for label in labels:
    freq[label] = freq.get(label, 0) + 1
print(freq)  # {'SAFE': 2, 'TOXIC': 1, 'SPAM': 1}
```

### C) Track test results by ID
```python
results = {}
results["TC_01"] = "PASS"
results["TC_02"] = "FAIL"
results.update({"TC_03": "SKIP", "TC_04": "PASS"})
```

### D) Group tests by module
```python
tests = [
    {"module": "auth", "status": "PASS"},
    {"module": "api", "status": "FAIL"},
    {"module": "auth", "status": "SKIP"}
]

by_module = {}
for test in tests:
    module = test["module"]
    by_module.setdefault(module, []).append(test)

print(by_module)
# {'auth': [...], 'api': [...]}
```

### E) Validate expected fields
```python
expected_fields = {"id", "status", "timestamp"}
response = {"id": 1, "status": "ok"}

missing = expected_fields - set(response.keys())
if missing:
    print(f"Missing: {missing}")  # Missing: {'timestamp'}
```

### F) Check key existence and default
```python
config = {"timeout": 30, "retries": 3}
debug = config.get("debug", False)  # defaults to False
```

---

## 12) Nested dictionaries
```python
user = {
    "id": 101,
    "profile": {
        "name": "Selva",
        "role": "QA"
    }
}

print(user["profile"]["name"])  # Selva
```

Useful for:
- API responses with nested structure
- Complex test metadata

---

## 13) Dictionary vs other collections (decision guide)

| Collection | Ordered | Unique | Access | Mutable | Use case |
|-----------|---------|--------|--------|---------|----------|
| list | Yes | No | Index | Yes | Dynamic data |
| tuple | Yes | No | Index | No | Fixed data |
| set | No | Yes | Membership | Yes | Unique items |
| frozenset | No | Yes | Membership | No | Immutable set |
| dict | Yes (3.7+) | Keys only | Key | Yes | Key-value mapping |

---

## 14) Common mistakes and fixes

1. Using unhashable key (list, dict, set)
```python
# d[[1, 2]] = "value"  # TypeError
d[(1, 2)] = "value"    # use tuple instead
```

2. Forgetting `get()` with missing key
```python
# value = d["missing"]  # KeyError
value = d.get("missing", "default")  # safe
```

3. Thinking `copy()` copies nested objects
```python
d1 = {"a": [1, 2]}
d2 = d1.copy()
d2["a"].append(3)
print(d1["a"])  # [1, 2, 3]  (affected!)
# Use copy.deepcopy() for full copy
```

---

## 15) Quick cheat sheet

```python
# Create
d = {"key": "value"}
d = dict(key="value")
d = dict.fromkeys(["id", "status"], None)

# Access
d["key"]
d.get("key", "default")
"key" in d

# Add/update
d["key"] = "value"
d.update({"k2": "v2"})
d.setdefault("key", "default")

# Remove
d.pop("key", "default")
del d["key"]
d.clear()

# Iterate
for k in d.keys()
for v in d.values()
for k, v in d.items()

# Utilities
len(d)
d.copy()
d1 | d2  # merge (Py 3.9+)
```

---

## 16) Learning priority (recommended order)

1. **Access:** `dict[key]`, `get()`, `in`
2. **Add/update:** `=`, `update()`, `setdefault()`
3. **Remove:** `pop()`, `del`, `clear()`
4. **Iterate:** `items()`, `keys()`, `values()`
5. **Copy/template:** `copy()`, `fromkeys()`
6. Other: `len()`, merge, `popitem()`, comprehension

---

## 17) Common patterns you'll use daily

### Pattern 1: Safe retrieval with fallback
```python
value = response.get("field", "default")
```

### Pattern 2: Count occurrences
```python
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

### Pattern 3: Group by key
```python
grouped = {}
for record in records:
    key = record["category"]
    grouped.setdefault(key, []).append(record)
```

### Pattern 4: Validate keys
```python
required = {"id", "status"}
missing = required - set(d.keys())
```

### Pattern 5: Merge with defaults
```python
defaults = {"timeout": 30, "retries": 3}
config = {**defaults, **user_config}
```

---

## 18) Interview points to remember

- Dictionary is mutable but keys must be hashable/immutable
- Order preserved since Python 3.7
- `dict[key]` for sure-exists keys, `get()` for uncertain
- `items()` is most useful iteration method
- Shallow copy with `copy()` — nested objects still shared
- `setdefault()` combines check + add in one call

---

## 19) Practice prompts (self-assignment)

1. Create a dict mapping test IDs to results.
2. Safely check if a field exists and retrieve with default.
3. Count frequency of model labels from a list.
4. Merge two config dicts with priority order.
5. Validate API response has all required fields.
6. Group API responses by status code.
7. Update nested dict values without overwriting others.
8. Iterate dict and print formatted key-value pairs.

---

## 20) Summary

- Dictionary is key-value collection, mutable, insertion-ordered
- Best for mapping/lookup scenarios (API responses, configs, results)
- Learn access → modify → iterate progression
- Use `get()` for safe access, `items()` for iteration
- Keys must be hashable (str, int, tuple, frozenset)
- Very powerful and widely used in Python automation/AI code


