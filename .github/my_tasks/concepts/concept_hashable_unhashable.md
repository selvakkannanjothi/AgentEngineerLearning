# Hashable and Unhashable in Python - Complete Revision Notes

## 1) Problem statement (why this topic matters)
In automation and AI testing, we often use:
- `set` for unique values
- `dict` for key-value mappings

Common issue:
- Some data types cause `TypeError: unhashable type` when used in sets or dict keys.

Example problem:
```python
bad_key = ["api", "prod"]
cache = {bad_key: "profile_1"}  # TypeError
```

To avoid this, you must know hashable vs unhashable types.

---

## 2) What is hashable?
A value is hashable if:
1. It has a fixed hash value during its lifetime.
2. It can be compared for equality.

Hashable values can be used as:
- set elements
- dictionary keys

Example:
```python
d = {"status": 200}     # str key is hashable
s = {200, 201, 204}      # int items are hashable
```

---

## 3) What is unhashable?
Unhashable values do not have a stable hash (usually because they are mutable).

They cannot be used as:
- set elements
- dictionary keys

Example:
```python
# { [1, 2, 3] }        # TypeError: unhashable type: 'list'
# { {"a": 1} }        # TypeError: unhashable type: 'dict'
```

---

## 4) Common hashable types
- `int`, `float`, `bool`, `str`
- `bytes`
- `tuple` (only if all elements are hashable)
- `frozenset`
- `None`

Examples:
```python
ok = {
    100,
    "PASS",
    ("api", "prod"),
    frozenset(["safe", "toxic"])
}
```

---

## 5) Common unhashable types
- `list`
- `dict`
- `set`

Examples:
```python
# bad = {[1, 2], {"a": 1}, {1, 2}}  # TypeError
```

---

## 6) Tuple rule (important)
Tuple is hashable only if all items inside are hashable.

Works:
```python
key = ("api", 200, True)
d = {key: "ok"}
```

Fails:
```python
key = ("api", [200, 201])
# d = {key: "bad"}  # TypeError because inner list is unhashable
```

---

## 7) Why mutable types are unhashable
If an object can change, its hash could become inconsistent.
That breaks how Python stores and finds values in hash tables.

So Python restricts mutable types from being keys/set elements.

---

## 8) Nested sets: why frozenset is needed
Regular sets cannot be inside another set because `set` is unhashable.

Fails:
```python
a = {1, 2}
b = {3, 4}
# outer = {a, b}  # TypeError: unhashable type: 'set'
```

Works with `frozenset`:
```python
a = frozenset([1, 2])
b = frozenset([3, 4])
outer = {a, b}
print(outer)
```

---

## 9) Real-time usage examples (automation + AI testing)
### A) Cache API responses by immutable request signature
```python
request_signature = ("GET", "/v1/users", 200)
cache = {request_signature: "cached_result"}
```

### B) Deduplicate environment profiles
```python
env_profiles = {
    frozenset(["api", "prod"]),
    frozenset(["ui", "staging"])
}
```

### C) Model configuration mapping
```python
model_map = {
    ("gpt-4o", 0.2, 1000): "stable",
    ("gpt-4o", 0.8, 2000): "creative"
}
```

### D) Unsafe word groups as immutable keys
```python
risk_levels = {
    frozenset(["hack", "exploit"]): "high",
    frozenset(["bypass"]): "medium"
}
```

### E) Track unique immutable labels
```python
labels = {"SAFE", "TOXIC", "SPAM"}
```

---

## 10) How to check hashability quickly
Use `hash()` in try/except.

```python
def is_hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

print(is_hashable((1, 2)))      # True
print(is_hashable([1, 2]))      # False
print(is_hashable(frozenset([1, 2])))  # True
```

---

## 11) Common mistakes and fixes
1. Using list as dict key
```python
# d = {["api", "prod"]: "x"}  # error
```
Fix:
```python
d = {("api", "prod"): "x"}
```

2. Using set inside set
```python
# s = {{1, 2}, {3, 4}}  # error
```
Fix:
```python
s = {frozenset([1, 2]), frozenset([3, 4])}
```

3. Assuming tuple is always hashable
- Not true if tuple contains list/dict/set.

---

## 12) Mini cheat sheet
```python
# Hashable
1
"text"
(1, 2, 3)
frozenset([1, 2])

# Unhashable
[1, 2, 3]
{"a": 1}
{1, 2, 3}

# Use as dict keys/set elements only if hashable
```

---

## 13) Practice prompts (self-assignment)
1. Create a dict with tuple keys for `(method, endpoint)`.
2. Try using a list as key and observe the error.
3. Convert unhashable set groups to frozenset and store in outer set.
4. Write `is_hashable()` and test on 10 values.
5. Create tuple key that fails due to inner list, then fix it.

---

## 14) Summary
- Hashable values can be used in sets and as dict keys.
- Most mutable types are unhashable.
- `frozenset` and fully-hashable tuples are key tools for immutable keys.

