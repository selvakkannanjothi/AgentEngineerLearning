# List Method Tasks

## Problem Statements (With Input Data)

### 1) Build a prompt queue
**Task:** Add one urgent prompt and a batch of regular prompts.

**Input Data:**
- `prompt_queue = ["summarize report", "classify ticket"]`
- Urgent prompt: `"urgent: detect PII"`
- Regular prompts: `["translate feedback", "extract entities"]`

### 2) Place smoke test first
**Task:** Put smoke test at the top of the execution plan.

**Input Data:**
- `plan = ["regression_auth", "regression_search", "regression_payment"]`
- Item to insert: `"smoke_health_check"`
- Position: `0`

### 3) Clean endpoint list
**Task:** Remove deprecated endpoint and capture the last processed endpoint.

**Input Data:**
- `endpoints = ["/v1/login", "/v1/deprecated", "/v1/orders", "/v1/users"]`
- Value to remove: `"/v1/deprecated"`

### 4) Count hallucination tags
**Task:** Count total occurrences of `"hallucination"`.

**Input Data:**
- `review_tags = ["correct", "hallucination", "correct", "unsafe", "hallucination"]`
- Target label: `"hallucination"`

### 5) Find first timeout
**Task:** Find the index position of the first `"TIMEOUT"`.

**Input Data:**
- `statuses = ["PASS", "PASS", "TIMEOUT", "FAIL", "TIMEOUT"]`
- Target value: `"TIMEOUT"`

### 6) Sort token usage
**Task:** Sort token usage from highest to lowest.

**Input Data:**
- `token_usage = [820, 1540, 430, 1200]`
- Sort direction: descending

### 7) Reverse response history
**Task:** Convert oldest-first history to newest-first order.

**Input Data:**
- `responses = ["v1 draft", "v2 refined", "v3 final"]`

### 8) Preserve baseline copy
**Task:** Create a working copy and modify only the copy.

**Input Data:**
- `baseline_dataset = ["record_1", "record_2", "record_3"]`

### 9) Clear retry queue
**Task:** Empty the retry queue after processing.

**Input Data:**
- `retry_queue = ["job_101", "job_102", "job_103"]`

## Questions and Answers

### 1) Build a prompt queue
**Question:** You have a prompt queue. Add one urgent prompt, then add a batch of regular prompts.

**Input Data:**
- `prompt_queue = ["summarize report", "classify ticket"]`
- Urgent prompt: `"urgent: detect PII"`
- Regular prompts: `["translate feedback", "extract entities"]`

**Answer:** Use `append()` for one item and `extend()` for multiple items.

```python
prompt_queue = ["summarize report", "classify ticket"]

prompt_queue.append("urgent: detect PII")
prompt_queue.extend(["translate feedback", "extract entities"])

print(prompt_queue)
# ['summarize report', 'classify ticket', 'urgent: detect PII', 'translate feedback', 'extract entities']
```

### 2) Put smoke test first
**Question:** `smoke_health_check` must run before all other tests.

**Input Data:**
- `plan = ["regression_auth", "regression_search", "regression_payment"]`
- Item to insert: `"smoke_health_check"`
- Position: `0`

**Answer:** Use `insert(index, value)` to place an item at a specific position.

```python
plan = ["regression_auth", "regression_search", "regression_payment"]
plan.insert(0, "smoke_health_check")

print(plan)
# ['smoke_health_check', 'regression_auth', 'regression_search', 'regression_payment']
```

### 3) Remove invalid endpoint and capture last processed
**Question:** Remove `"/v1/deprecated"` from endpoint list, then remove and store the last endpoint.

**Input Data:**
- `endpoints = ["/v1/login", "/v1/deprecated", "/v1/orders", "/v1/users"]`
- Value to remove: `"/v1/deprecated"`

**Answer:** Use `remove()` to delete by value and `pop()` to remove and return an item.

```python
endpoints = ["/v1/login", "/v1/deprecated", "/v1/orders", "/v1/users"]

endpoints.remove("/v1/deprecated")
last_processed = endpoints.pop()

print(endpoints)      # ['/v1/login', '/v1/orders']
print(last_processed) # /v1/users
```

### 4) Count hallucination labels
**Question:** In model review tags, count total `"hallucination"` labels.

**Input Data:**
- `review_tags = ["correct", "hallucination", "correct", "unsafe", "hallucination"]`
- Target label: `"hallucination"`

**Answer:** Use `count(value)`.

```python
review_tags = ["correct", "hallucination", "correct", "unsafe", "hallucination"]
hallucination_count = review_tags.count("hallucination")

print(hallucination_count)
# 2
```

### 5) Find first timeout
**Question:** Find the position of the first `"TIMEOUT"` in result statuses.

**Input Data:**
- `statuses = ["PASS", "PASS", "TIMEOUT", "FAIL", "TIMEOUT"]`
- Target value: `"TIMEOUT"`

**Answer:** Use `index(value)`.

```python
statuses = ["PASS", "PASS", "TIMEOUT", "FAIL", "TIMEOUT"]
first_timeout_idx = statuses.index("TIMEOUT")

print(first_timeout_idx)
# 2
```

### 6) Sort token usage descending
**Question:** Sort token usage list from highest to lowest to identify costly calls.

**Input Data:**
- `token_usage = [820, 1540, 430, 1200]`
- Sort direction: descending

**Answer:** Use `sort(reverse=True)`.

```python
token_usage = [820, 1540, 430, 1200]
token_usage.sort(reverse=True)

print(token_usage)
# [1540, 1200, 820, 430]
```

### 7) Reverse response history
**Question:** Convert oldest-first model responses into newest-first order.

**Input Data:**
- `responses = ["v1 draft", "v2 refined", "v3 final"]`

**Answer:** Use `reverse()`.

```python
responses = ["v1 draft", "v2 refined", "v3 final"]
responses.reverse()

print(responses)
# ['v3 final', 'v2 refined', 'v1 draft']
```

### 8) Preserve baseline dataset
**Question:** Make test changes to a dataset list without changing the original baseline.

**Input Data:**
- `baseline_dataset = ["record_1", "record_2", "record_3"]`

**Answer:** Use `copy()` before mutation.

```python
baseline_dataset = ["record_1", "record_2", "record_3"]
working_dataset = baseline_dataset.copy()

working_dataset.pop()

print("Baseline:", baseline_dataset)  # ['record_1', 'record_2', 'record_3']
print("Working :", working_dataset)   # ['record_1', 'record_2']
```

### 9) Clear retry queue
**Question:** Retry queue should be emptied after successful reprocessing.

**Input Data:**
- `retry_queue = ["job_101", "job_102", "job_103"]`

**Answer:** Use `clear()`.

```python
retry_queue = ["job_101", "job_102", "job_103"]
retry_queue.clear()

print(retry_queue)
# []
```

## Try It Yourself (No Answers)

### 1) Prompt expansion task
**Question:** You have `prompts = ["summarize", "classify"]`. Add `"detect sentiment"` as one urgent item, then add `["rewrite", "translate"]` in one operation.

**Input Data:**
- `prompts = ["summarize", "classify"]`
- Urgent prompt: `"detect sentiment"`
- Additional prompts: `["rewrite", "translate"]`

### 2) Smoke-first run plan
**Question:** You have `run_plan = ["api_regression", "ui_regression", "db_regression"]`. Insert `"smoke_ping"` so it runs first.

**Input Data:**
- `run_plan = ["api_regression", "ui_regression", "db_regression"]`
- Item to insert: `"smoke_ping"`
- Position: `0`

### 3) Service cleanup
**Question:** You have `services = ["auth", "legacy", "orders", "billing"]`. Remove `"legacy"`, then remove and store the last service.

**Input Data:**
- `services = ["auth", "legacy", "orders", "billing"]`
- Value to remove: `"legacy"`

### 4) Unsafe label counter
**Question:** You have `labels = ["safe", "unsafe", "safe", "unsafe", "safe"]`. Count how many times `"unsafe"` appears.

**Input Data:**
- `labels = ["safe", "unsafe", "safe", "unsafe", "safe"]`
- Target value: `"unsafe"`

### 5) Top latency review
**Question:** You have `latencies = [420, 180, 250, 610]`. Sort from highest to lowest, then print only the top 3 values.

**Input Data:**
- `latencies = [420, 180, 250, 610]`
- Required output: top 3 highest values
