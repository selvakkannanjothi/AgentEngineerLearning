# Loops (for, while) Tasks

## Problem Statements (With Input Data)

### 1) Run a suite of test IDs
**Task:** Loop through test IDs and print "Running <id>" for each.

**Input Data:**
- `test_ids = ["TC_01", "TC_02", "TC_03"]`

### 2) Print test IDs with index
**Task:** Loop with index using `enumerate()` and print "index: test_id".

**Input Data:**
- `test_ids = ["TC_01", "TC_02", "TC_03"]`

### 3) Retry an operation with a while loop
**Task:** Retry up to `max_attempts`, printing attempt number each time, stop early if `success` becomes True.

**Input Data:**
- `max_attempts = 4`
- succeeds on attempt 3 (simulate)

### 4) Stop at first failing status code
**Task:** Loop through status codes, stop immediately (break) at the first one that isn't 200.

**Input Data:**
- `statuses = [200, 200, 500, 200]`

### 5) Skip invalid scores while summing
**Task:** Loop through scores, skip (continue) any `None` values, and sum the valid ones.

**Input Data:**
- `scores = [0.8, None, 0.6, None, 0.9]`

### 6) Search with for...else
**Task:** Search for a target test ID in a list; print "Found" and break if found, else print "Not found" via the loop's `else`.

**Input Data:**
- `test_cases = ["TC_01", "TC_02", "TC_03"]`
- `target = "TC_09"`

### 7) Nested loop over suites and tests
**Task:** Loop over each suite, and within it loop over each test, printing "suite -> test".

**Input Data:**
- `suites = ["auth", "payments"]`
- `tests = ["create", "delete"]`

### 8) Filter passing scores with list comprehension
**Task:** Build a list of scores that are >= 0.7 using a comprehension.

**Input Data:**
- `scores = [0.9, 0.5, 0.72, 0.65, 0.88]`

---

## Questions and Answers

### 1) Run a suite of test IDs
**Question:** Loop through test IDs and print "Running <id>" for each.

**Input Data:**
- `test_ids = ["TC_01", "TC_02", "TC_03"]`

**Answer:**
```python
test_ids = ["TC_01", "TC_02", "TC_03"]

for test_id in test_ids:
    print(f"Running {test_id}")
```

### 2) Print test IDs with index
**Question:** Loop with index using `enumerate()` and print "index: test_id".

**Input Data:**
- `test_ids = ["TC_01", "TC_02", "TC_03"]`

**Answer:**
```python
test_ids = ["TC_01", "TC_02", "TC_03"]

for index, test_id in enumerate(test_ids):
    print(f"{index}: {test_id}")
# 0: TC_01
# 1: TC_02
# 2: TC_03
```

### 3) Retry an operation with a while loop
**Question:** Retry up to `max_attempts`, printing attempt number each time, stop early if `success` becomes True.

**Input Data:**
- `max_attempts = 4` (succeeds on attempt 3)

**Answer:**
```python
max_attempts = 4
attempt = 0
success = False

while attempt < max_attempts and not success:
    attempt += 1
    print(f"Attempt {attempt}")
    success = (attempt == 3)

print("Success" if success else "Failed after retries")
# Attempt 1
# Attempt 2
# Attempt 3
# Success
```

### 4) Stop at first failing status code
**Question:** Loop through status codes, stop immediately at the first one that isn't 200.

**Input Data:**
- `statuses = [200, 200, 500, 200]`

**Answer:**
```python
statuses = [200, 200, 500, 200]

for status in statuses:
    if status != 200:
        print(f"Stopping - failure detected: {status}")
        break
    print(f"OK: {status}")
# OK: 200
# OK: 200
# Stopping - failure detected: 500
```

### 5) Skip invalid scores while summing
**Question:** Loop through scores, skip any `None` values, and sum the valid ones.

**Input Data:**
- `scores = [0.8, None, 0.6, None, 0.9]`

**Answer:**
```python
scores = [0.8, None, 0.6, None, 0.9]
total = 0

for score in scores:
    if score is None:
        continue
    total += score

print(total)  # 2.3
```

### 6) Search with for...else
**Question:** Search for a target test ID in a list; print "Found" and break if found, else print "Not found" via the loop's `else`.

**Input Data:**
- `test_cases = ["TC_01", "TC_02", "TC_03"]`
- `target = "TC_09"`

**Answer:**
```python
test_cases = ["TC_01", "TC_02", "TC_03"]
target = "TC_09"

for tc in test_cases:
    if tc == target:
        print("Found")
        break
else:
    print("Not found")
# Not found
```

### 7) Nested loop over suites and tests
**Question:** Loop over each suite, and within it loop over each test, printing "suite -> test".

**Input Data:**
- `suites = ["auth", "payments"]`
- `tests = ["create", "delete"]`

**Answer:**
```python
suites = ["auth", "payments"]
tests = ["create", "delete"]

for suite in suites:
    for test in tests:
        print(f"{suite} -> {test}")
# auth -> create
# auth -> delete
# payments -> create
# payments -> delete
```

### 8) Filter passing scores with list comprehension
**Question:** Build a list of scores that are >= 0.7 using a comprehension.

**Input Data:**
- `scores = [0.9, 0.5, 0.72, 0.65, 0.88]`

**Answer:**
```python
scores = [0.9, 0.5, 0.72, 0.65, 0.88]
passed = [s for s in scores if s >= 0.7]
print(passed)  # [0.9, 0.72, 0.88]
```

---

## Self Assignments (No Answers)

### 1) Print squares of a range
**Question:** Loop through numbers 1 to 5 and print each number's square.

**Input Data:**
- range 1 to 5 inclusive

### 2) Poll job status until DONE
**Question:** Simulate polling a list of statuses one at a time with a while loop, printing "Polling..." until status equals "DONE".

**Input Data:**
- `statuses = ["RUNNING", "RUNNING", "RUNNING", "DONE"]`

### 3) Count PASS vs FAIL results
**Question:** Loop through a list of results and count how many are "PASS" vs "FAIL" using two counters.

**Input Data:**
- `results = ["PASS", "FAIL", "PASS", "PASS", "FAIL"]`

### 4) Break on first critical error
**Question:** Loop through a list of log severities and break as soon as you hit "CRITICAL", printing everything checked before it.

**Input Data:**
- `severities = ["INFO", "WARNING", "CRITICAL", "INFO"]`

### 5) Skip already-processed IDs
**Question:** Loop through a list of test IDs, skip any already present in a `processed` set, and print the ones actually run.

**Input Data:**
- `test_ids = ["TC_01", "TC_02", "TC_03", "TC_04"]`
- `processed = {"TC_02", "TC_04"}`

### 6) for...else to validate all fields present
**Question:** Loop through required fields checking each exists in a response dict; use `else` to print "All fields present" only if no `break` occurred.

**Input Data:**
- `required = ["id", "status", "timestamp"]`
- `response = {"id": 1, "status": "ok", "timestamp": "2026-07-07"}`

### 7) Nested loop for a grid of test combinations
**Question:** Loop over `browsers = ["chrome", "firefox"]` and `environments = ["staging", "prod"]`, printing every browser+environment combination.

**Input Data:**
- `browsers = ["chrome", "firefox"]`
- `environments = ["staging", "prod"]`

### 8) Build a dict comprehension from parallel lists
**Question:** Given `ids` and `results` lists of equal length, build a dict mapping id -> result using a comprehension with `zip()`.

**Input Data:**
- `ids = ["TC_01", "TC_02", "TC_03"]`
- `results = ["PASS", "FAIL", "PASS"]`
