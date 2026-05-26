# Hashable and Unhashable Tasks

## Problem Statements (With Input Data)

### 1) Use tuple as dictionary key
**Task:** Store API response category using a tuple key.

**Input Data:**
- `key = ("GET", "/v1/users", 200)`
- `value = "success"`

### 2) Identify unhashable key issue
**Task:** Try using list as dict key and fix it.

**Input Data:**
- Bad key: `["GET", "/v1/users", 200]`

### 3) Use frozenset for nested set storage
**Task:** Store two groups inside one outer set.

**Input Data:**
- Group 1: `["api", "prod"]`
  - Group 2: `["ui", "staging"]`

### 4) Validate tuple hashability with mutable inner item
**Task:** Check why tuple with inner list fails as dict key.

**Input Data:**
- `bad_tuple = ("api", [200, 201])`

### 5) Fix unhashable tuple key
**Task:** Convert inner list to tuple and use as dict key.

**Input Data:**
- `fixed_tuple = ("api", (200, 201))`

### 6) Check hashability of multiple values
**Task:** Create utility function to test hashability.

**Input Data:**
- Values: `100`, `"PASS"`, `[1,2]`, `{1,2}`, `(1,2)`, `frozenset([1,2])`

### 7) Create set of immutable environment profiles
**Task:** Build outer set of profile pairs.

**Input Data:**
- Profiles: `["api", "dev"]`, `["api", "prod"]`, `["ui", "qa"]`

### 8) Compare hashable and unhashable in one example
**Task:** Separate valid and invalid values for set insertion.

**Input Data:**
- Values: `(1,2)`, `[1,2]`, `"ok"`, `{"a":1}`, `frozenset([3,4])`

### 9) Build immutable model config map
**Task:** Use tuple keys to map model config to mode.

**Input Data:**
- `("gpt-4o", 0.2, 1000) -> "stable"`
- `("gpt-4o", 0.8, 2000) -> "creative"`

### 10) Deduplicate immutable label groups
**Task:** Store label groups uniquely using set of frozensets.

**Input Data:**
- Group A: `["SAFE", "SPAM"]`
- Group B: `["SAFE", "SPAM"]`
- Group C: `["TOXIC", "BIAS"]`

---

## Questions and Answers

### 1) Use tuple as dictionary key
**Question:** Save category against tuple key.

**Input Data:**
- `key = ("GET", "/v1/users", 200)`
- `value = "success"`

**Answer:** Tuple is hashable here, so it works as key.

```python
key = ("GET", "/v1/users", 200)
response_map = {key: "success"}

print(response_map[key])
# success
```

### 2) Identify unhashable key issue
**Question:** Why does list fail as dict key, and how to fix?

**Input Data:**
- Bad key: `["GET", "/v1/users", 200]`

**Answer:** List is mutable and unhashable. Convert to tuple.

```python
bad_key = ["GET", "/v1/users", 200]
# response_map = {bad_key: "success"}  # TypeError

fixed_key = tuple(bad_key)
response_map = {fixed_key: "success"}
print(response_map[fixed_key])
# success
```

### 3) Use frozenset for nested set storage
**Question:** Store two groups in one outer set.

**Input Data:**
- Group 1: `["api", "prod"]`
- Group 2: `["ui", "staging"]`

**Answer:** Convert inner groups to frozenset.

```python
outer = {
    frozenset(["api", "prod"]),
    frozenset(["ui", "staging"])
}

print(outer)
```

### 4) Validate tuple hashability with mutable inner item
**Question:** Why does tuple with list fail as key?

**Input Data:**
- `bad_tuple = ("api", [200, 201])`

**Answer:** Tuple contains unhashable list, so tuple becomes unhashable.

```python
bad_tuple = ("api", [200, 201])
# d = {bad_tuple: "x"}  # TypeError
print("Tuple fails because inner list is unhashable")
```

### 5) Fix unhashable tuple key
**Question:** Make tuple key valid by using immutable inner type.

**Input Data:**
- `fixed_tuple = ("api", (200, 201))`

**Answer:** Inner tuple is hashable, so whole key works.

```python
fixed_tuple = ("api", (200, 201))
d = {fixed_tuple: "valid"}

print(d[fixed_tuple])
# valid
```

### 6) Check hashability of multiple values
**Question:** Build helper function and test values.

**Input Data:**
- `100`, `"PASS"`, `[1,2]`, `{1,2}`, `(1,2)`, `frozenset([1,2])`

**Answer:** Use `hash()` with try/except.

```python
def is_hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

values = [100, "PASS", [1, 2], {1, 2}, (1, 2), frozenset([1, 2])]
for v in values:
    print(v, "->", is_hashable(v))
```

### 7) Create set of immutable environment profiles
**Question:** Build set of profile pairs safely.

**Input Data:**
- `["api", "dev"]`, `["api", "prod"]`, `["ui", "qa"]`

**Answer:** Use frozenset for each profile.

```python
profiles = {
    frozenset(["api", "dev"]),
    frozenset(["api", "prod"]),
    frozenset(["ui", "qa"])
}

print(profiles)
```

### 8) Compare hashable and unhashable in one example
**Question:** Separate values by hashability.

**Input Data:**
- `(1,2)`, `[1,2]`, `"ok"`, `{"a":1}`, `frozenset([3,4])`

**Answer:** Categorize with helper.

```python
def is_hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

values = [(1, 2), [1, 2], "ok", {"a": 1}, frozenset([3, 4])]
hashable = [v for v in values if is_hashable(v)]
unhashable = [v for v in values if not is_hashable(v)]

print("Hashable:", hashable)
print("Unhashable:", unhashable)
```

### 9) Build immutable model config map
**Question:** Map immutable model configs to labels.

**Input Data:**
- `("gpt-4o", 0.2, 1000) -> "stable"`
- `("gpt-4o", 0.8, 2000) -> "creative"`

**Answer:** Use tuple keys in dictionary.

```python
config_mode = {
    ("gpt-4o", 0.2, 1000): "stable",
    ("gpt-4o", 0.8, 2000): "creative"
}

print(config_mode[("gpt-4o", 0.2, 1000)])
# stable
```

### 10) Deduplicate immutable label groups
**Question:** Keep only unique groups.

**Input Data:**
- Group A: `["SAFE", "SPAM"]`
- Group B: `["SAFE", "SPAM"]`
- Group C: `["TOXIC", "BIAS"]`

**Answer:** Use set of frozensets.

```python
label_groups = {
    frozenset(["SAFE", "SPAM"]),
    frozenset(["SAFE", "SPAM"]),
    frozenset(["TOXIC", "BIAS"])
}

print(len(label_groups))
# 2
```

---

## Self Assignments (No Answers)

### 1) Dict key conversion
**Question:** Use `(method, endpoint, code)` as dict key and fetch value.

**Input Data:**
- `("POST", "/v1/orders", 201) -> "created"`

### 2) Fix unhashable list key
**Question:** Attempt list key, then fix using tuple.

**Input Data:**
- `bad = ["POST", "/v1/orders", 201]`

### 3) Nested set problem
**Question:** Try creating set of sets and then fix with frozenset.

**Input Data:**
- `{1,2}`, `{3,4}`

### 4) Tuple inner mutability issue
**Question:** Test tuple key with inner list and explain why it fails.

**Input Data:**
- `("model", [0.2, 1000])`

### 5) Build hashability checker
**Question:** Write function to test hashability for 8 mixed values.

**Input Data:**
- `1`, `"a"`, `[1]`, `{1}`, `(1,)`, `(1,[2])`, `frozenset([1])`, `{"x":1}`

### 6) Deduplicate immutable config groups
**Question:** Use set of frozensets to keep unique groups only.

**Input Data:**
- `["api", "prod"]`, `["api", "prod"]`, `["ui", "qa"]`

### 7) Store frozenset keys in dict
**Question:** Map frozen field groups to validation profiles.

**Input Data:**
- `frozenset(["id", "status"]) -> "minimal"`
- `frozenset(["id", "status", "timestamp", "data"]) -> "full"`

### 8) Separate values by hashability
**Question:** Create two lists: hashable and unhashable.

**Input Data:**
- `values = [100, "ok", [1,2], {"a":1}, (1,2), frozenset([3,4]), {1,2}]`

### 9) Tuple key map for model configs
**Question:** Build dictionary using tuple config keys and print one result.

**Input Data:**
- `("gemini", 0.3, 1500) -> "balanced"`
- `("gpt-4o", 0.7, 2500) -> "creative"`

### 10) Prompt safety profile groups
**Question:** Create outer set containing immutable safety groups.

**Input Data:**
- `["no_pii", "no_hate"]`, `["no_violence", "no_illegal"]`

