# Flow Control (if/elif/else) Tasks

## Problem Statements (With Input Data)

### 1) Classify HTTP status code range
**Task:** Print whether a status code is Success, Client Error, Server Error, or Unknown.

**Input Data:**
- `status_code = 404`

### 2) Grade a test score with PASS/FAIL
**Task:** Assign PASS if score >= 0.7, else FAIL, using a ternary expression.

**Input Data:**
- `score = 0.65`

### 3) Check status code AND payload presence
**Task:** Print "Success with data" only if status is 200 and payload is non-empty.

**Input Data:**
- `status_code = 200`
- `payload = {}`

### 4) Classify LLM confidence into bands
**Task:** Classify confidence into HIGH (>=0.9), MEDIUM (>=0.6), LOW (below 0.6).

**Input Data:**
- `confidence = 0.75`

### 5) Retry decision based on result and attempt count
**Task:** Decide whether to retry, stop, or pass based on result and retry_count.

**Input Data:**
- `result = "FAIL"`
- `retry_count = 3`
- `max_retries = 3`

### 6) Validate a config value using truthy/falsy check
**Task:** Print "Config missing" if a config value is empty/None/0, else print the value.

**Input Data:**
- `timeout = 0`

### 7) Guard clause validation
**Task:** Write a function that returns an error message step-by-step (no response -> non-200 -> ok) using guard clauses.

**Input Data:**
- `response = {"status": 500}`

### 8) Combine multiple logical conditions
**Task:** Print "Retry allowed" only if status is 500 or 503, AND retry_count is less than 3.

**Input Data:**
- `status_code = 503`
- `retry_count = 1`

---

## Questions and Answers

### 1) Classify HTTP status code range
**Question:** Print whether the status code is Success (2xx), Client Error (4xx), Server Error (5xx), or Unknown.

**Input Data:**
- `status_code = 404`

**Answer:**
```python
status_code = 404

if 200 <= status_code < 300:
    print("Success")
elif 400 <= status_code < 500:
    print("Client Error")
elif 500 <= status_code < 600:
    print("Server Error")
else:
    print("Unknown")
# Client Error
```

### 2) Grade a test score with PASS/FAIL
**Question:** Assign PASS if score >= 0.7, else FAIL, using a ternary expression.

**Input Data:**
- `score = 0.65`

**Answer:**
```python
score = 0.65
result = "PASS" if score >= 0.7 else "FAIL"
print(result)  # FAIL
```

### 3) Check status code AND payload presence
**Question:** Print "Success with data" only if status is 200 and payload is non-empty.

**Input Data:**
- `status_code = 200`
- `payload = {}`

**Answer:**
```python
status_code = 200
payload = {}

if status_code == 200 and payload:
    print("Success with data")
else:
    print("Success but empty payload")  # this runs - payload is falsy
```

### 4) Classify LLM confidence into bands
**Question:** Classify confidence into HIGH (>=0.9), MEDIUM (>=0.6), LOW (below 0.6).

**Input Data:**
- `confidence = 0.75`

**Answer:**
```python
confidence = 0.75

if confidence >= 0.9:
    label = "HIGH"
elif confidence >= 0.6:
    label = "MEDIUM"
else:
    label = "LOW"

print(label)  # MEDIUM
```

### 5) Retry decision based on result and attempt count
**Question:** Decide whether to retry, stop, or pass based on result and retry_count.

**Input Data:**
- `result = "FAIL"`
- `retry_count = 3`
- `max_retries = 3`

**Answer:**
```python
result = "FAIL"
retry_count = 3
max_retries = 3

if result == "PASS":
    print("No action needed")
elif result == "FAIL" and retry_count < max_retries:
    print("Retrying test")
else:
    print("Marking as broken - manual review")
# Marking as broken - manual review
```

### 6) Validate a config value using truthy/falsy check
**Question:** Print "Config missing" if a config value is empty/None/0, else print the value.

**Input Data:**
- `timeout = 0`

**Answer:**
```python
timeout = 0

if not timeout:
    print("Config missing")
else:
    print(timeout)
# Config missing - 0 is falsy
```

### 7) Guard clause validation
**Question:** Write a function that returns an error message step-by-step using guard clauses.

**Input Data:**
- `response = {"status": 500}`

**Answer:**
```python
def check_response(response):
    if not response:
        return "No response received"
    if response.get("status") != 200:
        return "Non-200 status"
    return "OK"

print(check_response({"status": 500}))  # Non-200 status
```

### 8) Combine multiple logical conditions
**Question:** Print "Retry allowed" only if status is 500 or 503, AND retry_count is less than 3.

**Input Data:**
- `status_code = 503`
- `retry_count = 1`

**Answer:**
```python
status_code = 503
retry_count = 1

if (status_code == 500 or status_code == 503) and retry_count < 3:
    print("Retry allowed")
else:
    print("Retry not allowed")
# Retry allowed
```

---

## Self Assignments (No Answers)

### 1) Classify response time
**Question:** Print "Fast", "Moderate", or "Slow" based on response_time thresholds (<1s Fast, <3s Moderate, else Slow).

**Input Data:**
- `response_time = 2.4`

### 2) Ternary for pass/fail label
**Question:** Use a ternary expression to label a test as "STABLE" if flaky_count == 0, else "FLAKY".

**Input Data:**
- `flaky_count = 2`

### 3) Nested condition rewrite
**Question:** Rewrite a nested if (status == 200, then check payload) into a single combined condition using `and`.

**Input Data:**
- `status_code = 200`
- `payload = {"id": 5}`

### 4) Multi-band error severity
**Question:** Classify an error_code into "CRITICAL" (>=5000), "WARNING" (>=1000), "INFO" (below 1000).

**Input Data:**
- `error_code = 1500`

### 5) Retry-with-backoff decision
**Question:** Print "Retry" if attempt < max_attempts and last_result == "FAIL", else print "Stop".

**Input Data:**
- `attempt = 2`
- `max_attempts = 5`
- `last_result = "FAIL"`

### 6) Falsy check on API list response
**Question:** Given a list of test results, print "No results returned" if the list is empty, else print the count.

**Input Data:**
- `results = []`

### 7) Guard clause for missing fields
**Question:** Write a function using guard clauses that checks: if `data` is None return "No data", if `"id"` missing from data return "Missing id", else return "Valid".

**Input Data:**
- `data = {"name": "test"}`

### 8) Compound condition for alerting
**Question:** Print "ALERT" only if cpu_usage > 90 OR memory_usage > 90, AND the service is not already in maintenance mode.

**Input Data:**
- `cpu_usage = 95`
- `memory_usage = 40`
- `maintenance_mode = False`