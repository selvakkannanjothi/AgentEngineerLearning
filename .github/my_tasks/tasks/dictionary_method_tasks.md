# Dictionary Method Tasks

## Problem Statements (With Input Data)

### 1) Store and retrieve API response data
**Task:** Create a dictionary for API response and access values safely.

**Input Data:**
- `status = 200`
- `message = "ok"`
- `user_id = 101`

### 2) Update test configuration
**Task:** Add and update multiple config values in one operation.

**Input Data:**
- `config = {"host": "localhost"}`
- New values: `{"port": 8080, "timeout": 30}`

### 3) Count test label frequencies
**Task:** Count how many times each label appears.

**Input Data:**
- `labels = ["SAFE", "TOXIC", "SAFE", "SPAM", "SAFE"]`

### 4) Safely access optional fields
**Task:** Retrieve values that may or may not exist in the dictionary.

**Input Data:**
- `response = {"status": 200, "data": {"id": 10}}`
- Fields to get: `"error"`, `"timestamp"`

### 5) Group test results by module
**Task:** Organize test results by their module name.

**Input Data:**
- `tests = [{"module": "auth", "result": "PASS"}, {"module": "api", "result": "FAIL"}, {"module": "auth", "result": "SKIP"}]`

### 6) Remove old cache values
**Task:** Remove and retrieve a value, then clear unused entries.

**Input Data:**
- `cache = {"user_123": "active", "user_456": "inactive"}`
- Remove: `"user_456"`

### 7) Validate required API response fields
**Task:** Check if all expected fields are present in the response.

**Input Data:**
- `expected = {"id", "status", "timestamp"}`
- `response = {"id": 1, "status": "ok"}`

### 8) Create test case template
**Task:** Generate a template dict for all test cases with None defaults.

**Input Data:**
- `fields = ["test_id", "module", "result", "duration"]`

### 9) Merge baseline and custom config
**Task:** Combine default config with user overrides.

**Input Data:**
- `defaults = {"timeout": 30, "retries": 3, "debug": False}`
- `overrides = {"timeout": 60}`

### 10) Track model run metrics
**Task:** Store and iterate through model performance data by run ID.

**Input Data:**
- `run_1 = {"model": "gpt-4o", "tokens": 1200, "score": 0.92}`
- `run_2 = {"model": "gemini", "tokens": 980, "score": 0.88}`

---

## Questions and Answers

### 1) Store and retrieve API response data
**Question:** Create a dictionary for an API response and retrieve the status code.

**Input Data:**
- `status = 200`
- `message = "ok"`
- `user_id = 101`

**Answer:** Create dict with key-value pairs and access with `get()` for safety.

```python
response = {
    "status": status,
    "message": message,
    "user_id": user_id
}

print(response.get("status"))        # 200
print(response.get("error", "N/A"))  # N/A (field doesn't exist)
```

### 2) Update test configuration
**Question:** Add initial config, then update multiple values at once.

**Input Data:**
- `config = {"host": "localhost"}`
- New values: `{"port": 8080, "timeout": 30}`

**Answer:** Use `update()` for bulk add/update.

```python
config = {"host": "localhost"}
config.update({"port": 8080, "timeout": 30})

print(config)
# {'host': 'localhost', 'port': 8080, 'timeout': 30}
```

### 3) Count test label frequencies
**Question:** Count how many times each label appears in a list.

**Input Data:**
- `labels = ["SAFE", "TOXIC", "SAFE", "SPAM", "SAFE"]`

**Answer:** Use `get()` to increment count, or `setdefault()`.

```python
labels = ["SAFE", "TOXIC", "SAFE", "SPAM", "SAFE"]
freq = {}

for label in labels:
    freq[label] = freq.get(label, 0) + 1

print(freq)
# {'SAFE': 3, 'TOXIC': 1, 'SPAM': 1}
```

### 4) Safely access optional fields
**Question:** Retrieve fields that may not exist, with sensible defaults.

**Input Data:**
- `response = {"status": 200, "data": {"id": 10}}`
- Fields to get: `"error"`, `"timestamp"`

**Answer:** Use `get(key, default)` for missing fields.

```python
response = {"status": 200, "data": {"id": 10}}

status = response.get("status", 0)
error = response.get("error", "No error")
timestamp = response.get("timestamp", "unknown")

print(status)     # 200
print(error)      # No error
print(timestamp)  # unknown
```

### 5) Group test results by module
**Question:** Organize test results into separate lists by module name.

**Input Data:**
- `tests = [{"module": "auth", "result": "PASS"}, {"module": "api", "result": "FAIL"}, {"module": "auth", "result": "SKIP"}]`

**Answer:** Use `setdefault()` to create list on first encounter.

```python
tests = [
    {"module": "auth", "result": "PASS"},
    {"module": "api", "result": "FAIL"},
    {"module": "auth", "result": "SKIP"}
]

by_module = {}
for test in tests:
    module = test["module"]
    by_module.setdefault(module, []).append(test)

print(by_module)
# {'auth': [{'module': 'auth', 'result': 'PASS'}, {'module': 'auth', 'result': 'SKIP'}],
#  'api': [{'module': 'api', 'result': 'FAIL'}]}
```

### 6) Remove old cache values
**Question:** Remove a specific cached entry and retrieve its value, then clear optional entries.

**Input Data:**
- `cache = {"user_123": "active", "user_456": "inactive"}`

**Answer:** Use `pop()` to remove and return value.

```python
cache = {"user_123": "active", "user_456": "inactive"}

removed_value = cache.pop("user_456")
print(removed_value)  # inactive
print(cache)          # {'user_123': 'active'}

# Pop non-existent with default
old_value = cache.pop("user_789", "not_found")
print(old_value)      # not_found
```

### 7) Validate required API response fields
**Question:** Check if all expected fields are present in the response.

**Input Data:**
- `expected = {"id", "status", "timestamp"}`
- `response = {"id": 1, "status": "ok"}`

**Answer:** Use set difference to find missing fields.

```python
expected = {"id", "status", "timestamp"}
response = {"id": 1, "status": "ok"}

missing = expected - set(response.keys())
print(missing)  # {'timestamp'}

if missing:
    print(f"Missing fields: {missing}")
else:
    print("All fields present")
```

### 8) Create test case template
**Question:** Generate a template dictionary with None values for all required fields.

**Input Data:**
- `fields = ["test_id", "module", "result", "duration"]`

**Answer:** Use `fromkeys()` to create template.

```python
fields = ["test_id", "module", "result", "duration"]
template = dict.fromkeys(fields, None)

print(template)
# {'test_id': None, 'module': None, 'result': None, 'duration': None}

# Use template for new test case
template["test_id"] = "TC_01"
template["module"] = "auth"
```

### 9) Merge baseline and custom config
**Question:** Combine default config with user overrides (overrides take priority).

**Input Data:**
- `defaults = {"timeout": 30, "retries": 3, "debug": False}`
- `overrides = {"timeout": 60}`

**Answer:** Use merge operator (Py 3.9+) or dict unpacking.

```python
defaults = {"timeout": 30, "retries": 3, "debug": False}
overrides = {"timeout": 60}

# Method 1: Merge operator (Python 3.9+)
config = defaults | overrides
print(config)
# {'timeout': 60, 'retries': 3, 'debug': False}

# Method 2: dict unpacking
config = {**defaults, **overrides}
print(config)
# {'timeout': 60, 'retries': 3, 'debug': False}
```

### 10) Track model run metrics
**Question:** Store model run data and display formatted results.

**Input Data:**
- `run_1 = {"model": "gpt-4o", "tokens": 1200, "score": 0.92}`
- `run_2 = {"model": "gemini", "tokens": 980, "score": 0.88}`

**Answer:** Store in dict and iterate with `items()`.

```python
runs = {}
runs["run_1"] = {"model": "gpt-4o", "tokens": 1200, "score": 0.92}
runs["run_2"] = {"model": "gemini", "tokens": 980, "score": 0.88}

for run_id, metrics in runs.items():
    print(f"{run_id}: model={metrics['model']}, tokens={metrics['tokens']}, score={metrics['score']}")

# run_1: model=gpt-4o, tokens=1200, score=0.92
# run_2: model=gemini, tokens=980, score=0.88
```

---

## Self Assignments (No Answers)

### 1) Store LLM response metadata
**Question:** Create a dictionary storing prompt, model, temperature, and response score. Retrieve the temperature value safely.

**Input Data:**
- `prompt = "Classify this text"`
- `model = "gpt-4o"`
- `temperature = 0.2`
- `score = 0.91`

### 2) Build dynamic test config
**Question:** Start with empty dict, add `timeout` and `retries` one by one, then update with `max_failures` and `debug_mode` at once.

**Input Data:**
- Initial: empty
- First: `timeout = 30`, `retries = 3`
- Then add: `max_failures = 5`, `debug_mode = True`

### 3) Count API status codes
**Question:** Given a list of status codes, create a frequency dict showing how many of each code appeared.

**Input Data:**
- `codes = [200, 200, 404, 500, 200, 404, 200]`

### 4) Find missing test fields
**Question:** You have expected test fields and an actual test dict. Find which fields are missing.

**Input Data:**
- `expected = {"test_id", "module", "priority", "tags"}`
- `actual = {"test_id": "TC_01", "module": "auth"}`

### 5) Extract defaults safely
**Question:** Retrieve `debug`, `verbose`, and `trace_level` from config dict with defaults (False, False, "info").

**Input Data:**
- `config = {"timeout": 30, "debug": True}`

### 6) Organize tests by priority
**Question:** Group test cases by their priority level (HIGH, MEDIUM, LOW).

**Input Data:**
- `tests = [{"id": "TC_01", "priority": "HIGH"}, {"id": "TC_02", "priority": "LOW"}, {"id": "TC_03", "priority": "HIGH"}]`

### 7) Remove stale cache entries
**Question:** Remove `"cache_key_old"` from cache and store the popped value. Also safely pop a non-existent key with a default.

**Input Data:**
- `cache = {"cache_key_new": "data1", "cache_key_old": "data2"}`

### 8) Create run result template
**Question:** Generate a template dict for tracking run results with fields: `run_id`, `status`, `duration`, `error_msg`, all starting as None.

**Input Data:**
- Fields needed: `run_id`, `status`, `duration`, `error_msg`

### 9) Merge user input with program defaults
**Question:** Start with default settings, then override with user-provided settings. User only provided the `retries` value.

**Input Data:**
- `defaults = {"timeout": 60, "retries": 3, "log_level": "INFO"}`
- `user_settings = {"retries": 5}`

### 10) Display model performance summary
**Question:** Create a dict of model runs, iterate through it, and print formatted summary for each run showing model name and score.

**Input Data:**
- Three runs: each with `model` and `score` keys
- run_alpha: model="gpt-4o", score=0.95
- run_beta: model="gemini", score=0.89
- run_gamma: model="claude", score=0.92


