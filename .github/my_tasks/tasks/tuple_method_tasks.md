# Tuple Method Tasks

## Problem Statements (With Input Data)

### 1) Pack user details into a tuple
**Task:** Combine three separate variables into a single tuple.

**Input Data:**
- `name = "selva"`
- `age = 33`
- `role = "qa tester"`

### 2) Unpack test case metadata
**Task:** Extract each field from a tuple into separate variables and print them.

**Input Data:**
- `test_case = ("TC_01", "gpt-4o", 0.2, "SAFE")`
- Variables to unpack into: `test_id`, `model`, `temperature`, `expected`

### 3) Access specific items by index
**Task:** Print the first and last item from a response tuple.

**Input Data:**
- `response = ("TC_05", 200, 0.91, "PASS")`
- Access: first item and last item

### 4) Count failed statuses
**Task:** Count how many times `"FAIL"` appears in test results tuple.

**Input Data:**
- `results = ("PASS", "FAIL", "PASS", "FAIL", "PASS", "FAIL")`
- Target value: `"FAIL"`

### 5) Find first mismatch position
**Task:** Find the index of the first `"MISMATCH"` in validation results.

**Input Data:**
- `validations = ("OK", "OK", "MISMATCH", "OK", "MISMATCH")`
- Target value: `"MISMATCH"`

### 6) Extended unpack — capture middle values
**Task:** Unpack first and last item separately, and collect all middle values into a list.

**Input Data:**
- `pipeline = ("start", "preprocess", "tokenize", "embed", "end")`
- Variables: `first`, `*steps`, `last`

### 7) Convert list to tuple for safe config
**Task:** You have a mutable list of model settings. Convert it to a tuple to make it immutable.

**Input Data:**
- `model_config_list = ["gpt-4o", 0.2, 4096, "json"]`

### 8) Swap two values without temp variable
**Task:** Swap `actual` and `expected` using tuple unpacking.

**Input Data:**
- `actual = "FAIL"`
- `expected = "PASS"`

### 9) Unpack function return tuple
**Task:** Call a function that returns `(min, max, avg)` of response times and capture each value.

**Input Data:**
- `response_times = [180, 240, 150, 210]`
- Function returns: `min`, `max`, `average`

---

## Questions and Answers

### 1) Pack user details into a tuple
**Question:** Combine name, age, and role into a single tuple and print it.

**Input Data:**
- `name = "selva"`
- `age = 33`
- `role = "qa tester"`

**Answer:** Assign multiple values to one tuple variable (packing).

```python
name = "selva"
age = 33
role = "qa tester"

user_details = (name, age, role)
print(user_details)
# ('selva', 33, 'qa tester')
```

### 2) Unpack test case metadata
**Question:** Extract each field from the tuple into separate variables and print them.

**Input Data:**
- `test_case = ("TC_01", "gpt-4o", 0.2, "SAFE")`

**Answer:** Use unpacking — assign tuple to multiple variables in one line.

```python
test_case = ("TC_01", "gpt-4o", 0.2, "SAFE")

test_id, model, temperature, expected = test_case

print(f"ID: {test_id}")
print(f"Model: {model}")
print(f"Temperature: {temperature}")
print(f"Expected: {expected}")
# ID: TC_01
# Model: gpt-4o
# Temperature: 0.2
# Expected: SAFE
```

### 3) Access specific items by index
**Question:** Print the first and last item from the response tuple.

**Input Data:**
- `response = ("TC_05", 200, 0.91, "PASS")`

**Answer:** Use positive index for first item and `-1` for last item.

```python
response = ("TC_05", 200, 0.91, "PASS")

print(response[0])   # TC_05
print(response[-1])  # PASS
```

### 4) Count failed statuses
**Question:** Count how many times `"FAIL"` appears in the results tuple.

**Input Data:**
- `results = ("PASS", "FAIL", "PASS", "FAIL", "PASS", "FAIL")`

**Answer:** Use `count(value)`.

```python
results = ("PASS", "FAIL", "PASS", "FAIL", "PASS", "FAIL")
fail_count = results.count("FAIL")

print(fail_count)
# 3
```

### 5) Find first mismatch position
**Question:** Find the index of the first `"MISMATCH"` in the validation results.

**Input Data:**
- `validations = ("OK", "OK", "MISMATCH", "OK", "MISMATCH")`

**Answer:** Use `index(value)`.

```python
validations = ("OK", "OK", "MISMATCH", "OK", "MISMATCH")
first_mismatch = validations.index("MISMATCH")

print(first_mismatch)
# 2
```

### 6) Extended unpack — capture middle values
**Question:** Unpack first and last item separately, collect middle steps into a list.

**Input Data:**
- `pipeline = ("start", "preprocess", "tokenize", "embed", "end")`

**Answer:** Use `*` (star operator) to capture middle values.

```python
pipeline = ("start", "preprocess", "tokenize", "embed", "end")

first, *steps, last = pipeline

print(first)  # start
print(steps)  # ['preprocess', 'tokenize', 'embed']
print(last)   # end
```

### 7) Convert list to tuple for safe config
**Question:** Convert a mutable config list into an immutable tuple.

**Input Data:**
- `model_config_list = ["gpt-4o", 0.2, 4096, "json"]`

**Answer:** Use `tuple()` to convert.

```python
model_config_list = ["gpt-4o", 0.2, 4096, "json"]
model_config = tuple(model_config_list)

print(model_config)
print(type(model_config))
# ('gpt-4o', 0.2, 4096, 'json')
# <class 'tuple'>
```

### 8) Swap two values without temp variable
**Question:** Swap `actual` and `expected` using tuple unpacking in one line.

**Input Data:**
- `actual = "FAIL"`
- `expected = "PASS"`

**Answer:** Use tuple unpacking on right side first, then assign.

```python
actual = "FAIL"
expected = "PASS"

actual, expected = expected, actual

print(actual)    # PASS
print(expected)  # FAIL
```

### 9) Unpack function return tuple
**Question:** Call a function that returns `(min, max, avg)` and capture each value separately.

**Input Data:**
- `response_times = [180, 240, 150, 210]`

**Answer:** Unpack the returned tuple directly into named variables.

```python
def response_metrics(times):
    return min(times), max(times), sum(times) / len(times)

response_times = [180, 240, 150, 210]
min_time, max_time, avg_time = response_metrics(response_times)

print(f"Min: {min_time}")
print(f"Max: {max_time}")
print(f"Avg: {avg_time}")
# Min: 150
# Max: 240
# Avg: 195.0
```

---

## Self Assignments (No Answers)

### 1) Pack API response fields
**Question:** Pack `status_code`, `response_time`, and `label` into a single tuple and print it.

**Input Data:**
- `status_code = 200`
- `response_time = 145`
- `label = "SAFE"`

### 2) Unpack model run result
**Question:** Unpack the tuple into `run_id`, `model`, `score`, `verdict` and print each variable.

**Input Data:**
- `run_result = ("RUN_07", "gemini-pro", 0.87, "PASS")`

### 3) Access tuple by index
**Question:** Print only the first and last value from the tuple using indexing.

**Input Data:**
- `statuses = ("INIT", "RUNNING", "VALIDATING", "COMPLETE")`

### 4) Count timeout events
**Question:** Count how many times `"TIMEOUT"` appears and print the count.

**Input Data:**
- `events = ("PASS", "TIMEOUT", "PASS", "TIMEOUT", "FAIL", "TIMEOUT")`
- Target value: `"TIMEOUT"`

### 5) Find first error position
**Question:** Find the index of the first `"ERROR"`.

**Input Data:**
- `logs = ("OK", "OK", "ERROR", "OK", "ERROR")`
- Target value: `"ERROR"`

### 6) Extended unpack - capture middle runs
**Question:** Unpack first run and last run separately, and store all middle runs in `middle_runs`.

**Input Data:**
- `runs = ("run_1", "run_2", "run_3", "run_4", "run_5")`

### 7) Convert list to tuple
**Question:** Convert the given list into tuple and print both value and type.

**Input Data:**
- `payload_list = ["prompt", "gpt-4o", 0.1, 1024]`

### 8) Convert tuple to list for modification
**Question:** Convert the tuple to list, append `"json"`, and print the updated list.

**Input Data:**
- `config_tuple = ("gpt-4o", 0.2, 4096)`
- Value to append: `"json"`

### 9) Swap expected and actual
**Question:** Swap `expected` and `actual` using tuple unpacking and print both after swap.

**Input Data:**
- `expected = "PASS"`
- `actual = "FAIL"`

### 10) Unpack function return values
**Question:** Write a function that returns `(min, max, avg)` for the given tuple of latencies and unpack them.

**Input Data:**
- `latencies = (210, 180, 240, 150, 300)`

### 11) Single-item tuple check
**Question:** Create a single-item tuple for `model_name` and print its type.

**Input Data:**
- `model_name = "gpt-4o"`

### 12) Star-unpack only head and tail
**Question:** Extract `first_step` and collect the remaining steps into `remaining_steps`.

**Input Data:**
- `pipeline_steps = ("ingest", "clean", "chunk", "embed", "index")`
