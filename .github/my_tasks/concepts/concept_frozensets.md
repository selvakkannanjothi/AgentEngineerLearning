# Frozensets in Python - Complete Revision Notes

## 1) What is a frozenset?
A frozenset is an immutable version of a set.
- Unordered collection of unique values.
- No duplicate items.
- Immutable: cannot add, remove, or update items.
- Hashable: can be used as dictionary keys or inside another set.

Example:
```python
fs = frozenset(["safe", "toxic", "safe"])
print(fs)  # frozenset({'safe', 'toxic'})
```

---

## 2) Why frozenset is needed (problem-first view)
Use frozenset when values must never change at runtime.

Common real-world problem:
- You keep safety rules or allowed status codes in a normal set.
- Some code path accidentally modifies that set.
- Your validations become inconsistent.

Frozenset solution:
- Freeze rules/config once and prevent accidental mutations.

Example:
```python
ALLOWED_CODES = frozenset([200, 201, 204])
# ALLOWED_CODES.add(500)  # AttributeError
```

---

## 3) Creation syntax
### From list
```python
fs1 = frozenset([1, 2, 3])
```

### From tuple
```python
fs2 = frozenset((1, 2, 3))
```

### From set
```python
s = {1, 2, 3}
fs3 = frozenset(s)
```

### Empty frozenset
```python
empty_fs = frozenset()
```

---

## 4) What you can do with frozenset
### Membership check
```python
fs = frozenset(["PASS", "FAIL"])
print("PASS" in fs)  # True
```

### Iterate values
```python
for item in fs:
    print(item)
```

### Use read-only methods
```python
fs = frozenset([1, 2, 3])
print(len(fs))
print(fs.copy())
print(fs.issubset({1, 2, 3, 4}))
```

---

## 5) What you cannot do
Frozenset is immutable.

```python
fs = frozenset([1, 2, 3])
# fs.add(4)       # AttributeError
# fs.remove(1)    # AttributeError
# fs.discard(2)   # AttributeError
# fs.clear()      # AttributeError
```

---

## 6) Frozenset operations
All set operations work and return a new frozenset.

```python
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A | B)  # frozenset({1, 2, 3, 4, 5, 6})
print(A & B)  # frozenset({3, 4})
print(A - B)  # frozenset({1, 2})
print(A ^ B)  # frozenset({1, 2, 5, 6})
```

---

## 7) Frozenset comparison methods
```python
A = frozenset([1, 2])
B = frozenset([1, 2, 3])

print(A.issubset(B))    # True
print(B.issuperset(A))  # True
print(A.isdisjoint({5, 6}))  # True
```

---

## 8) Frozenset vs Set
- `set` -> mutable, not hashable.
- `frozenset` -> immutable, hashable.

```python
s = {1, 2, 3}
fs = frozenset([1, 2, 3])

s.add(4)  # works
# fs.add(4)  # error
```

---

## 9) Real-time usage examples (automation + AI testing)
### A) Fixed allowed status codes
```python
ALLOWED_STATUS = frozenset([200, 201, 204])
received = 201
print(received in ALLOWED_STATUS)  # True
```

### B) Frozen blocked prompt terms
```python
BLOCKED_TERMS = frozenset(["hack", "exploit", "bypass", "jailbreak"])
prompt_terms = {"please", "bypass", "this"}

risky = BLOCKED_TERMS & prompt_terms
print(risky)  # frozenset({'bypass'})
```

### C) Use frozenset as dictionary key
```python
severity_map = {
    frozenset([500, 502, 503]): "server_error",
    frozenset([400, 401, 403]): "client_error"
}

print(severity_map[frozenset([500, 502, 503])])  # server_error
```

### D) Set of sets (via frozenset)
```python
env_profiles = {
    frozenset(["api", "prod"]),
    frozenset(["ui", "staging"])
}

print(env_profiles)
```

### E) Immutable expected API fields
```python
EXPECTED_FIELDS = frozenset(["id", "status", "timestamp", "data"])
actual_fields = frozenset(["id", "status"])
missing = EXPECTED_FIELDS - actual_fields

print(missing)  # frozenset({'timestamp', 'data'})
```

---

## 10) Common mistakes and fixes
1. Trying to mutate frozenset
```python
# fs.add("x")  # not allowed
```
Fix: create a new one
```python
fs = frozenset([1, 2])
fs = fs | frozenset([3])
```

2. Confusing with tuple
- Tuple is ordered/position-based.
- Frozenset is unordered and unique-only.

3. Expecting index access
```python
# fs[0]  # invalid
```

---

## 11) Mini cheat sheet
```python
# Create
frozenset([1, 2, 3])
frozenset((1, 2, 3))
frozenset()

# Membership
x in fs

# Operations
A | B
A & B
A - B
A ^ B

# Comparisons
A.issubset(B)
A.issuperset(B)
A.isdisjoint(B)

# Built-ins
len(fs)
```

---

## 12) Practice prompts (self-assignment)
1. Create immutable allowed API status codes using frozenset.
2. Check if token `"unsafe"` exists in frozenset labels.
3. Find common terms between blocked frozenset and prompt words set.
4. Use frozenset as key in a dict for response category mapping.
5. Build a set of frozensets representing environment profiles.
6. Calculate missing fields using two frozensets and difference.

---

## 13) Summary
- Frozenset is immutable, unique, and unordered.
- Best for fixed rules/config and hashable set-like keys.
- Supports set algebra while preventing accidental data mutation.

