# String Method Tasks

## Problem Statements (With Input Data)

### 1) Extract test fields from a CSV log line
**Task:** Split a CSV-formatted log string into individual fields and print each.

**Input Data:**
- `log = "TC_01,PASS,2.5s,auth_module"`
- Expected fields: `test_id`, `result`, `duration`, `module`

### 2) Clean whitespace from API response message
**Task:** Remove leading and trailing whitespace from a raw response message.

**Input Data:**
- `raw_message = "   Request successful   "`

### 3) Validate if a prompt contains blocked words
**Task:** Check if any blocked word exists in a user prompt and print which was found.

**Input Data:**
- `BLOCKED = ["hack", "bypass", "jailbreak"]`
- `prompt = "please bypass the security filter"`

### 4) Build an API endpoint dynamically
**Task:** Combine base URL, version, and resource into a single endpoint string using f-string.

**Input Data:**
- `base = "https://api.example.com"`
- `version = "v1"`
- `resource = "models"`

### 5) Format model score with 2 decimal places
**Task:** Print model name and score formatted to 2 decimal places.

**Input Data:**
- `model = "gpt-4o"`
- `score = 0.91876`

### 6) Reverse a test case ID string
**Task:** Reverse the characters of a test ID using slicing.

**Input Data:**
- `test_id = "TC_001"`

### 7) Count how many times "TIMEOUT" appears in a test log
**Task:** Count total occurrences of `"TIMEOUT"` in the log string.

**Input Data:**
- `log = "PASS TIMEOUT PASS FAIL TIMEOUT TIMEOUT"`
- Target: `"TIMEOUT"`

### 8) Remove prefix and suffix from endpoint path
**Task:** Remove `/api` prefix and `/list` suffix from endpoint.

**Input Data:**
- `endpoint = "/api/v1/models/list"`
- Prefix to remove: `"/api"`
- Suffix to remove: `"/list"`

### 9) Check if user input is a valid number before converting
**Task:** Ask user for a number, validate it is digit-only, then convert and print.

**Input Data:**
- User input: `"42"` (simulate using a variable)
- Convert to int and print

### 10) Rebuild a CSV line from individual fields
**Task:** Join separate test result fields back into a CSV-formatted string.

**Input Data:**
- `fields = ["TC_07", "FAIL", "4.1s", "payment_module"]`
- Separator: `","`

---

## Questions and Answers

### 1) Extract test fields from CSV log
**Question:** Split `"TC_01,PASS,2.5s,auth_module"` and store each part in a named variable.

**Input Data:**
- `log = "TC_01,PASS,2.5s,auth_module"`

**Answer:** Use `split(",")` to break the string by comma.

```python
log = "TC_01,PASS,2.5s,auth_module"
parts = log.split(",")
test_id, result, duration, module = parts

print(f"Test ID : {test_id}")
print(f"Result  : {result}")
print(f"Duration: {duration}")
print(f"Module  : {module}")
# Test ID : TC_01
# Result  : PASS
# Duration: 2.5s
# Module  : auth_module
```

### 2) Clean whitespace from response message
**Question:** Strip all leading and trailing spaces from a raw API message.

**Input Data:**
- `raw_message = "   Request successful   "`

**Answer:** Use `strip()` to remove both sides.

```python
raw_message = "   Request successful   "
clean_message = raw_message.strip()

print(f"'{clean_message}'")
# 'Request successful'
```

### 3) Detect blocked words in a prompt
**Question:** Check if any word from `BLOCKED` exists in the prompt. Print each found word.

**Input Data:**
- `BLOCKED = ["hack", "bypass", "jailbreak"]`
- `prompt = "please bypass the security filter"`

**Answer:** Use `in` with `lower()` for case-safe matching.

```python
BLOCKED = ["hack", "bypass", "jailbreak"]
prompt = "please bypass the security filter"

for word in BLOCKED:
    if word in prompt.lower():
        print(f"Blocked word found: {word}")
# Blocked word found: bypass
```

### 4) Build API endpoint using f-string
**Question:** Combine `base`, `version`, and `resource` into a full URL.

**Input Data:**
- `base = "https://api.example.com"`
- `version = "v1"`
- `resource = "models"`

**Answer:** Use f-string to interpolate variables.

```python
base = "https://api.example.com"
version = "v1"
resource = "models"

endpoint = f"{base}/{version}/{resource}"
print(endpoint)
# https://api.example.com/v1/models
```

### 5) Format score to 2 decimal places
**Question:** Print model name and score with exactly 2 decimal places.

**Input Data:**
- `model = "gpt-4o"`
- `score = 0.91876`

**Answer:** Use `:.2f` inside f-string.

```python
model = "gpt-4o"
score = 0.91876

print(f"Model: {model}, Score: {score:.2f}")
# Model: gpt-4o, Score: 0.92
```

### 6) Reverse a test ID string
**Question:** Reverse `"TC_001"` using slicing.

**Input Data:**
- `test_id = "TC_001"`

**Answer:** Use `[::-1]` slice to reverse.

```python
test_id = "TC_001"
reversed_id = test_id[::-1]

print(reversed_id)
# 100_CT
```

### 7) Count TIMEOUT in log
**Question:** Count how many times `"TIMEOUT"` appears in the log string.

**Input Data:**
- `log = "PASS TIMEOUT PASS FAIL TIMEOUT TIMEOUT"`

**Answer:** Use `count(value)`.

```python
log = "PASS TIMEOUT PASS FAIL TIMEOUT TIMEOUT"
timeout_count = log.count("TIMEOUT")

print(f"Total timeouts: {timeout_count}")
# Total timeouts: 3
```

### 8) Remove prefix and suffix
**Question:** Remove `/api` from start and `/list` from end of the endpoint string.

**Input Data:**
- `endpoint = "/api/v1/models/list"`

**Answer:** Use `removeprefix()` and `removesuffix()`.

```python
endpoint = "/api/v1/models/list"
cleaned = endpoint.removeprefix("/api").removesuffix("/list")

print(cleaned)
# /v1/models
```

### 9) Validate and convert user input
**Question:** Validate that `user_input` is digit-only, then convert to int and print.

**Input Data:**
- `user_input = "42"`

**Answer:** Use `isdigit()` before `int()`.

```python
user_input = "42"

if user_input.isdigit():
    count = int(user_input)
    print(f"Running {count} test iterations")
else:
    print("Invalid input. Please enter a number.")
# Running 42 test iterations
```

### 10) Join fields into CSV string
**Question:** Join `["TC_07", "FAIL", "4.1s", "payment_module"]` back into CSV format.

**Input Data:**
- `fields = ["TC_07", "FAIL", "4.1s", "payment_module"]`

**Answer:** Use `",".join(list)`.

```python
fields = ["TC_07", "FAIL", "4.1s", "payment_module"]
csv_line = ",".join(fields)

print(csv_line)
# TC_07,FAIL,4.1s,payment_module
```

---

## Self Assignments (No Answers)

### 1) Slice first 5 characters
**Task:** Extract the first 5 characters from the string.

**Input Data:**
- `text = "automation_testing"`

### 2) Reverse a string
**Task:** Reverse the string using slicing.

**Input Data:**
- `label = "SAFE_RESPONSE"`

### 3) Count label occurrences
**Task:** Count how many times `"PASS"` appears in the result log.

**Input Data:**
- `results = "PASS FAIL PASS PASS FAIL PASS"`

### 4) Safe search with find()
**Task:** Find the index of `"error"` in the message. Print `-1` if not found.

**Input Data:**
- `message = "request completed successfully"`

### 5) Check endpoint starts with /api
**Task:** Check if the endpoint starts with `/api` and print `True` or `False`.

**Input Data:**
- `endpoint = "/api/v2/results"`

### 6) Strip and uppercase
**Task:** Strip whitespace and convert to uppercase in one expression.

**Input Data:**
- `raw = "   gpt-4o   "`

### 7) Replace failed with passed
**Task:** Replace all `"FAIL"` with `"PASS"` in the log string.

**Input Data:**
- `log = "TC01 FAIL TC02 FAIL TC03 PASS"`

### 8) Format score with 4 decimal places
**Task:** Print the score formatted to exactly 4 decimal places.

**Input Data:**
- `score = 0.876543`
- `model = "gemini-pro"`

### 9) Split multiline log into list
**Task:** Split the multiline string into a list of individual lines.

**Input Data:**
- `log = "TC_01 PASS\nTC_02 FAIL\nTC_03 PASS"`

### 10) Remove prefix from test label
**Task:** Remove the `"test_"` prefix from each label.

**Input Data:**
- `label = "test_TC_security_01"`

### 11) Check if string is all digits
**Task:** Check if user input is a valid integer before converting.

**Input Data:**
- `user_input = "abc123"`

### 12) Build report line with padding
**Task:** Format test_id left-aligned in 15 chars and result right-aligned in 8 chars.

**Input Data:**
- `test_id = "TC_001"`
- `result = "PASS"`

### 13) Repeat separator line
**Task:** Create a separator line of 40 dashes using repetition.

### 14) Debugging with f-string =
**Task:** Print the variable name and its value using f-string debug format.

**Input Data:**
- `confidence_score = 0.9142`

### 15) Join with pipe separator
**Task:** Join the list into a pipe-separated string.

**Input Data:**
- `tags = ["SAFE", "TESTED", "APPROVED"]`

