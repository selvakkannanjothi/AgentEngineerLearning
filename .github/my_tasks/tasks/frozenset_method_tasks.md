# Frozenset Method Tasks

## Problem Statements (With Input Data)

### 1) Freeze allowed API status codes
**Task:** Convert mutable status list into immutable frozenset.

**Input Data:**
- `status_list = [200, 201, 204, 200]`

### 2) Validate response status membership
**Task:** Check if received status is part of allowed frozenset.

**Input Data:**
- `allowed_status = frozenset([200, 201, 204])`
- `received = 500`

### 3) Find risky terms in prompt
**Task:** Find overlap between blocked frozenset and prompt term set.

**Input Data:**
- `blocked = frozenset(["hack", "exploit", "bypass"])`
- `prompt_terms = {"please", "bypass", "login"}`

### 4) Find missing required fields
**Task:** Identify missing fields from actual response using frozenset difference.

**Input Data:**
- `required = frozenset(["id", "status", "timestamp", "data"])`
- `actual = frozenset(["id", "status"])`

### 5) Merge immutable label sets
**Task:** Combine two frozensets into one using union.

**Input Data:**
- `labels_run1 = frozenset(["SAFE", "TOXIC"])`
- `labels_run2 = frozenset(["SAFE", "SPAM"])`

### 6) Common items between immutable sets
**Task:** Find common labels from two frozensets.

**Input Data:**
- `set_a = frozenset(["SAFE", "TOXIC", "SPAM"])`
- `set_b = frozenset(["SPAM", "BIAS", "SAFE"])`

### 7) Use frozenset as dictionary key
**Task:** Map frozen status groups to a category and read value.

**Input Data:**
- Key group 1: `frozenset([500, 502, 503])`
- Key group 2: `frozenset([400, 401, 403])`

### 8) Build set of environment profiles
**Task:** Store multiple profile groups as a set of frozensets.

**Input Data:**
- Profile 1: `["api", "prod"]`
- Profile 2: `["ui", "staging"]`
- Profile 3: `["db", "dev"]`

### 9) Check subset relationship
**Task:** Validate if expected checks are subset of executed checks.

**Input Data:**
- `expected_checks = frozenset(["no_pii", "no_hate"])`
- `executed_checks = frozenset(["no_pii", "no_hate", "no_violence"])`

### 10) Validate disjoint safety rules
**Task:** Check blocked terms and clean prompt tokens share no common values.

**Input Data:**
- `blocked_terms = frozenset(["hack", "exploit", "bypass"])`
- `tokens = {"summarize", "translate", "email"}`

---

## Questions and Answers

### 1) Freeze allowed API status codes
**Question:** Convert list to frozenset and print type.

**Input Data:**
- `status_list = [200, 201, 204, 200]`

**Answer:** Use `frozenset()` to create immutable unique set.

```python
status_list = [200, 201, 204, 200]
allowed = frozenset(status_list)

print(allowed)
print(type(allowed))
# frozenset({200, 201, 204})
# <class 'frozenset'>
```

### 2) Validate response status membership
**Question:** Check if received code is allowed.

**Input Data:**
- `allowed_status = frozenset([200, 201, 204])`
- `received = 500`

**Answer:** Use membership operator `in`.

```python
allowed_status = frozenset([200, 201, 204])
received = 500

print(received in allowed_status)
# False
```

### 3) Find risky terms in prompt
**Question:** Find common terms between blocked and prompt terms.

**Input Data:**
- `blocked = frozenset(["hack", "exploit", "bypass"])`
- `prompt_terms = {"please", "bypass", "login"}`

**Answer:** Use intersection (`&`).

```python
blocked = frozenset(["hack", "exploit", "bypass"])
prompt_terms = {"please", "bypass", "login"}

risky = blocked & prompt_terms

print(risky)
# frozenset({'bypass'})
```

### 4) Find missing required fields
**Question:** Find which required fields are missing from actual fields.

**Input Data:**
- `required = frozenset(["id", "status", "timestamp", "data"])`
- `actual = frozenset(["id", "status"])`

**Answer:** Use difference (`required - actual`).

```python
required = frozenset(["id", "status", "timestamp", "data"])
actual = frozenset(["id", "status"])

missing = required - actual

print(missing)
# frozenset({'timestamp', 'data'})
```

### 5) Merge immutable label sets
**Question:** Combine two frozensets and print final labels.

**Input Data:**
- `labels_run1 = frozenset(["SAFE", "TOXIC"])`
- `labels_run2 = frozenset(["SAFE", "SPAM"])`

**Answer:** Use union (`|`).

```python
labels_run1 = frozenset(["SAFE", "TOXIC"])
labels_run2 = frozenset(["SAFE", "SPAM"])

all_labels = labels_run1 | labels_run2

print(all_labels)
# frozenset({'SAFE', 'TOXIC', 'SPAM'})
```

### 6) Common items between immutable sets
**Question:** Find common labels from two frozensets.

**Input Data:**
- `set_a = frozenset(["SAFE", "TOXIC", "SPAM"])`
- `set_b = frozenset(["SPAM", "BIAS", "SAFE"])`

**Answer:** Use intersection (`&`).

```python
set_a = frozenset(["SAFE", "TOXIC", "SPAM"])
set_b = frozenset(["SPAM", "BIAS", "SAFE"])

common = set_a & set_b

print(common)
# frozenset({'SAFE', 'SPAM'})
```

### 7) Use frozenset as dictionary key
**Question:** Create dictionary with frozenset keys and retrieve category.

**Input Data:**
- `frozenset([500, 502, 503]) -> "server_error"`
- `frozenset([400, 401, 403]) -> "client_error"`

**Answer:** Frozenset is hashable, so it can be used as dict key.

```python
status_groups = {
    frozenset([500, 502, 503]): "server_error",
    frozenset([400, 401, 403]): "client_error"
}

print(status_groups[frozenset([500, 502, 503])])
# server_error
```

### 8) Build set of environment profiles
**Question:** Create a set containing multiple frozenset profiles.

**Input Data:**
- `["api", "prod"]`, `["ui", "staging"]`, `["db", "dev"]`

**Answer:** Use frozenset items inside a set.

```python
env_profiles = {
    frozenset(["api", "prod"]),
    frozenset(["ui", "staging"]),
    frozenset(["db", "dev"])
}

print(env_profiles)
```

### 9) Check subset relationship
**Question:** Verify expected checks are subset of executed checks.

**Input Data:**
- `expected_checks = frozenset(["no_pii", "no_hate"])`
- `executed_checks = frozenset(["no_pii", "no_hate", "no_violence"])`

**Answer:** Use `issubset()`.

```python
expected_checks = frozenset(["no_pii", "no_hate"])
executed_checks = frozenset(["no_pii", "no_hate", "no_violence"])

print(expected_checks.issubset(executed_checks))
# True
```

### 10) Validate disjoint safety rules
**Question:** Check if blocked terms and prompt tokens have no overlap.

**Input Data:**
- `blocked_terms = frozenset(["hack", "exploit", "bypass"])`
- `tokens = {"summarize", "translate", "email"}`

**Answer:** Use `isdisjoint()`.

```python
blocked_terms = frozenset(["hack", "exploit", "bypass"])
tokens = {"summarize", "translate", "email"}

print(blocked_terms.isdisjoint(tokens))
# True
```

---

## Self Assignments (No Answers)

### 1) Freeze model safety labels
**Question:** Convert `labels = ["SAFE", "TOXIC", "SAFE", "SPAM"]` into frozenset.

**Input Data:**
- `labels = ["SAFE", "TOXIC", "SAFE", "SPAM"]`

### 2) Membership test with frozenset
**Question:** Check whether `204` exists in `allowed = frozenset([200, 201, 204])`.

**Input Data:**
- `allowed = frozenset([200, 201, 204])`
- Target value: `204`

### 3) Find overlap with blocked words
**Question:** Find common terms between blocked frozenset and response token set.

**Input Data:**
- `blocked = frozenset(["hack", "override", "exploit"])`
- `response_tokens = {"please", "override", "answer"}`

### 4) Find missing expected keys
**Question:** Calculate missing keys using frozenset difference.

**Input Data:**
- `expected = frozenset(["id", "name", "status", "timestamp"])`
- `actual = frozenset(["id", "name"])`

### 5) Union of immutable status groups
**Question:** Create union of `frozenset([200, 201])` and `frozenset([201, 204])`.

**Input Data:**
- `group_a = frozenset([200, 201])`
- `group_b = frozenset([201, 204])`

### 6) Use frozenset as dict key
**Question:** Create a dictionary where keys are frozensets and values are labels.

**Input Data:**
- `frozenset(["api", "prod"]) -> "critical"`
- `frozenset(["ui", "staging"]) -> "medium"`

### 7) Build set of frozensets
**Question:** Store three environment pairs as a set of frozensets.

**Input Data:**
- `["api", "dev"]`, `["api", "prod"]`, `["ui", "qa"]`

### 8) Subset validation
**Question:** Check if `required` frozenset is subset of `executed` frozenset.

**Input Data:**
- `required = frozenset(["no_pii", "no_hate"])`
- `executed = frozenset(["no_pii", "no_hate", "no_violence", "no_illegal"])`

### 9) Disjoint validation
**Question:** Verify two sets are disjoint using frozenset method.

**Input Data:**
- `blocked = frozenset(["hack", "bypass"])`
- `terms = {"summarize", "translate"}`

### 10) Compare two immutable runs
**Question:** Find both common and unique labels across two frozensets.

**Input Data:**
- `run1 = frozenset(["SAFE", "SPAM", "TOXIC"])`
- `run2 = frozenset(["SAFE", "BIAS", "SPAM"])`

