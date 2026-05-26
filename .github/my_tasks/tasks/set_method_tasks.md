# Set Method Tasks

## Problem Statements (With Input Data)

### 1) Remove duplicate test IDs
**Task:** Remove duplicates from a list of test IDs using a set.

**Input Data:**
- `test_ids = ["TC01", "TC02", "TC01", "TC03", "TC02"]`

### 2) Add a new blocked word
**Task:** Add one new blocked word to the set.

**Input Data:**
- `blocked_words = {"hack", "bypass", "exploit"}`
- Word to add: `"inject"`

### 3) Add multiple labels in one step
**Task:** Add a batch of new labels to the existing set.

**Input Data:**
- `labels = {"SAFE", "TOXIC"}`
- Labels to add: `["SPAM", "BIAS", "TOXIC"]`

### 4) Safely remove a value that may not exist
**Task:** Remove `"DEPRECATED"` from the endpoint set without risking error.

**Input Data:**
- `endpoints = {"/v1/login", "/v1/search", "/v1/orders"}`
- Value to remove: `"DEPRECATED"`

### 5) Find missing API response fields
**Task:** Identify which expected fields are missing from the actual response.

**Input Data:**
- `expected = {"id", "name", "email", "status"}`
- `actual = {"id", "name", "status"}`

### 6) Find common failures between two test runs
**Task:** Find which tests failed in both run1 and run2.

**Input Data:**
- `run1_failed = {"TC01", "TC03", "TC05"}`
- `run2_failed = {"TC03", "TC05", "TC07"}`

### 7) Collect all unique labels from two model runs
**Task:** Combine all unique labels from both runs.

**Input Data:**
- `run1 = {"SAFE", "TOXIC", "SPAM"}`
- `run2 = {"SAFE", "SPAM", "BIAS"}`

### 8) Find unexpected status codes
**Task:** Identify status codes not in the allowed set.

**Input Data:**
- `allowed = {200, 201, 204}`
- `received = {200, 500, 201, 403}`

### 9) Check if all expected labels are present
**Task:** Verify that `expected_labels` is a subset of `actual_labels`.

**Input Data:**
- `expected_labels = {"SAFE", "TOXIC"}`
- `actual_labels = {"SAFE", "TOXIC", "SPAM", "BIAS"}`

### 10) Check no blocked words appear in response
**Task:** Verify that no blocked words exist in the response tokens.

**Input Data:**
- `blocked = {"hack", "exploit", "bypass"}`
- `response_tokens = {"please", "summarize", "document"}`

---

## Questions and Answers

### 1) Remove duplicate test IDs
**Question:** Convert list to set to remove duplicates.

**Input Data:**
- `test_ids = ["TC01", "TC02", "TC01", "TC03", "TC02"]`

**Answer:** Use `set()` to auto-remove duplicates.

```python
test_ids = ["TC01", "TC02", "TC01", "TC03", "TC02"]
unique_ids = set(test_ids)

print(unique_ids)
# {'TC01', 'TC02', 'TC03'}
```

### 2) Add a new blocked word
**Question:** Add `"inject"` to the blocked words set.

**Input Data:**
- `blocked_words = {"hack", "bypass", "exploit"}`

**Answer:** Use `add(x)`.

```python
blocked_words = {"hack", "bypass", "exploit"}
blocked_words.add("inject")

print(blocked_words)
# {'hack', 'bypass', 'exploit', 'inject'}
```

### 3) Add multiple labels in one step
**Question:** Add `["SPAM", "BIAS", "TOXIC"]` to the labels set (no duplicates).

**Input Data:**
- `labels = {"SAFE", "TOXIC"}`

**Answer:** Use `update(iterable)`.

```python
labels = {"SAFE", "TOXIC"}
labels.update(["SPAM", "BIAS", "TOXIC"])

print(labels)
# {'SAFE', 'TOXIC', 'SPAM', 'BIAS'}
```

### 4) Safely remove a value that may not exist
**Question:** Remove `"DEPRECATED"` without error even if it doesn't exist.

**Input Data:**
- `endpoints = {"/v1/login", "/v1/search", "/v1/orders"}`

**Answer:** Use `discard(x)` instead of `remove(x)`.

```python
endpoints = {"/v1/login", "/v1/search", "/v1/orders"}
endpoints.discard("DEPRECATED")

print(endpoints)
# {'/v1/login', '/v1/search', '/v1/orders'}
```

### 5) Find missing API response fields
**Question:** Find which expected fields are not present in the actual response.

**Input Data:**
- `expected = {"id", "name", "email", "status"}`
- `actual = {"id", "name", "status"}`

**Answer:** Use set difference (`expected - actual`).

```python
expected = {"id", "name", "email", "status"}
actual = {"id", "name", "status"}

missing = expected - actual

print(missing)
# {'email'}
```

### 6) Find common failures between two test runs
**Question:** Find tests that failed in both runs.

**Input Data:**
- `run1_failed = {"TC01", "TC03", "TC05"}`
- `run2_failed = {"TC03", "TC05", "TC07"}`

**Answer:** Use set intersection (`&`).

```python
run1_failed = {"TC01", "TC03", "TC05"}
run2_failed = {"TC03", "TC05", "TC07"}

common_failures = run1_failed & run2_failed

print(common_failures)
# {'TC03', 'TC05'}
```

### 7) All unique labels from two model runs
**Question:** Combine all unique labels from both runs.

**Input Data:**
- `run1 = {"SAFE", "TOXIC", "SPAM"}`
- `run2 = {"SAFE", "SPAM", "BIAS"}`

**Answer:** Use set union (`|`).

```python
run1 = {"SAFE", "TOXIC", "SPAM"}
run2 = {"SAFE", "SPAM", "BIAS"}

all_labels = run1 | run2

print(all_labels)
# {'SAFE', 'TOXIC', 'SPAM', 'BIAS'}
```

### 8) Find unexpected status codes
**Question:** Identify which received codes are not in the allowed list.

**Input Data:**
- `allowed = {200, 201, 204}`
- `received = {200, 500, 201, 403}`

**Answer:** Use set difference (`received - allowed`).

```python
allowed = {200, 201, 204}
received = {200, 500, 201, 403}

unexpected = received - allowed

print(unexpected)
# {500, 403}
```

### 9) Check if all expected labels are present
**Question:** Verify expected labels are a subset of actual labels.

**Input Data:**
- `expected_labels = {"SAFE", "TOXIC"}`
- `actual_labels = {"SAFE", "TOXIC", "SPAM", "BIAS"}`

**Answer:** Use `issubset()`.

```python
expected_labels = {"SAFE", "TOXIC"}
actual_labels = {"SAFE", "TOXIC", "SPAM", "BIAS"}

result = expected_labels.issubset(actual_labels)

print(result)
# True
```

### 10) Check no blocked words appear in response
**Question:** Verify blocked words and response tokens have no overlap.

**Input Data:**
- `blocked = {"hack", "exploit", "bypass"}`
- `response_tokens = {"please", "summarize", "document"}`

**Answer:** Use `isdisjoint()`. Returns `True` if no common items.

```python
blocked = {"hack", "exploit", "bypass"}
response_tokens = {"please", "summarize", "document"}

is_safe = blocked.isdisjoint(response_tokens)

print(is_safe)
# True
```

---

## Self Assignments (No Answers)

### 1) Deduplicate status codes
**Question:** Remove duplicate status codes from the list and print as a set.

**Input Data:**
- `codes = [200, 404, 200, 500, 201, 404, 200]`

### 2) Add one new tag
**Question:** Add `"HALLUCINATION"` to the tags set.

**Input Data:**
- `tags = {"SAFE", "TOXIC", "SPAM"}`

### 3) Extend blocked words
**Question:** Add `["jailbreak", "exploit", "override"]` to blocked words set in one step.

**Input Data:**
- `blocked = {"hack", "bypass"}`

### 4) Remove expired endpoint safely
**Question:** Remove `"/v1/legacy"` without raising error if missing.

**Input Data:**
- `endpoints = {"/v1/login", "/v1/orders", "/v1/users"}`
- Value to remove: `"/v1/legacy"`

### 5) Find fields missing from response
**Question:** Find which expected fields are missing in the actual response.

**Input Data:**
- `expected = {"id", "score", "label", "timestamp"}`
- `actual = {"id", "score", "label"}`

### 6) Find tests failing in both runs
**Question:** Find tests that appear in both failed sets.

**Input Data:**
- `run1_fail = {"TC02", "TC04", "TC06"}`
- `run2_fail = {"TC04", "TC06", "TC08"}`

### 7) Combine all unique labels
**Question:** Collect all unique labels across two evaluation runs.

**Input Data:**
- `eval_1 = {"SAFE", "BIAS"}`
- `eval_2 = {"TOXIC", "BIAS", "SPAM"}`

### 8) Find codes that should not have passed
**Question:** Find codes in the received set that are not in the allowed set.

**Input Data:**
- `allowed = {200, 201, 204}`
- `received = {200, 201, 404, 503}`

### 9) Validate all required tags are covered
**Question:** Check if required tags are a subset of the produced tags.

**Input Data:**
- `required = {"SAFE", "SPAM"}`
- `produced = {"SAFE", "SPAM", "BIAS", "TOXIC"}`

### 10) Verify clean prompt
**Question:** Check that blocked terms and prompt tokens share nothing in common.

**Input Data:**
- `blocked = {"exploit", "bypass", "override"}`
- `prompt = {"explain", "summarize", "translate"}`

