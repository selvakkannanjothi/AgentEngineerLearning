# Loops (for, while) in Python - Complete Revision Notes

## 1) What is a loop?
A loop repeats a block of code multiple times — either a fixed number of times (over a known sequence) or until a condition changes, without writing the same statement over and over.

Example:
```python
test_ids = ["TC_01", "TC_02", "TC_03"]
for test_id in test_ids:
    print(f"Running {test_id}")
```

---

## 2) Why loops are needed (problem-first view)

Problem: you have 100 test cases to run, or need to keep retrying an API call until it succeeds. Writing that manually is impossible/unmaintainable.

Without loop:
```python
print("Running TC_01")
print("Running TC_02")
print("Running TC_03")
# ...repeat for every test case manually
```

With loop:
```python
test_ids = ["TC_01", "TC_02", "TC_03"]
for test_id in test_ids:
    print(f"Running {test_id}")
```

---

## 3) `for` loop — iterating over a known sequence
Use `for` when you know what you're iterating over (a list, string, range, dict, etc.) — a fixed, countable collection.

```python
for item in iterable:
    statement
```

### Over a list
```python
labels = ["SAFE", "TOXIC", "SPAM"]
for label in labels:
    print(label)
```

### Over a string (character by character)
```python
for char in "PASS":
    print(char)
```

### Over `range()`
```python
for i in range(5):        # 0,1,2,3,4
    print(i)

for i in range(1, 6):     # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2): # 0,2,4,6,8 (step=2)
    print(i)
```

### Over a dictionary
```python
config = {"timeout": 30, "retries": 3}
for key, value in config.items():
    print(f"{key} = {value}")
```

### With index using `enumerate()`
```python
tests = ["TC_01", "TC_02", "TC_03"]
for index, test in enumerate(tests):
    print(f"{index}: {test}")
# 0: TC_01
# 1: TC_02
# 2: TC_03
```

### Using `end=` in `print()` to control line endings
By default `print()` ends with a newline (`end="\n"`). Pass `end=` to print loop output on the same line instead of one per line.

```python
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4   (all on one line, space-separated)

for status in ["PASS", "PASS", "FAIL"]:
    print(status, end=" | ")
# PASS | PASS | FAIL |
```

---

## 4) `while` loop — repeating until a condition changes
Use `while` when you don't know in advance how many iterations are needed — it keeps running as long as the condition is True.

```python
while condition:
    statement
```

```python
retries = 0
max_retries = 3
success = False

while retries < max_retries and not success:
    print(f"Attempt {retries + 1}")
    retries += 1
    # pretend this attempt succeeds on try 2
    if retries == 2:
        success = True

print("Success" if success else "Failed after retries")
```

**Important:** the condition variable must change inside the loop, or it becomes an infinite loop.
```python
# Dangerous - infinite loop, count never changes
count = 0
while count < 5:
    print("stuck")
```

---

## 5) `while True` (loop without a condition) — handled entirely by `break`/`continue`
Sometimes there's no natural condition to put after `while` — you just want to loop forever until something inside the loop decides to stop, or skip, an iteration. `while True:` combined with `break` (to exit) and `continue` (to skip) is the standard pattern for this.

```python
while True:
    user_input = input("Enter prompt (or 'exit'): ")
    if user_input == "exit":
        break
    if len(user_input) < 3:
        print("Too short, try again")
        continue           # skip the rest of this iteration, loop again
    print(f"Processing: {user_input}")
```

Without `break`, `while True:` never ends on its own — it relies entirely on internal logic (usually an `if` + `break`) to terminate. `continue` inside it lets you re-loop without falling through to the rest of the body.

---

## 6) `break` — exit the loop immediately
```python
status_codes = [200, 200, 500, 200]
for code in status_codes:
    if code == 500:
        print("Error found, stopping")
        break
    print(f"Checked: {code}")
```

## 7) `continue` — skip to next iteration
```python
scores = [0.9, -1, 0.7, -1, 0.85]
for score in scores:
    if score == -1:
        continue  # skip invalid entries
    print(f"Valid score: {score}")
```

## 8) `pass` — no-op placeholder
```python
for code in [200, 404, 500]:
    if code == 200:
        pass  # TODO: handle success later
    else:
        print(f"Non-200: {code}")
```

---

## 9) `else` clause on loops (runs only if loop completes without `break`)
```python
test_cases = ["TC_01", "TC_02", "TC_03"]
target = "TC_05"

for tc in test_cases:
    if tc == target:
        print("Found")
        break
else:
    print("Not found in any test case")  # runs - loop finished without break
```

The same `else` behavior applies to `while` loops: the `else` block runs only if the `while` condition became False naturally (no `break` was hit).

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}")
    if attempts == 5:      # never true here, so break never happens
        break
else:
    print("Exhausted all attempts without success")  # runs - while ended normally
```

---

## 10) Nested loops
```python
suites = ["auth", "api"]
tests = ["login", "logout"]

for suite in suites:
    for test in tests:
        print(f"{suite} -> {test}")
# auth -> login
# auth -> logout
# api -> login
# api -> logout
```

---

## 11) List/dict comprehensions (compact loops)
```python
# List comprehension
scores = [0.9, 0.6, 0.85]
passed = [s for s in scores if s >= 0.7]
print(passed)  # [0.9, 0.85]

# Dict comprehension
labels = ["SAFE", "TOXIC", "SAFE"]
freq = {label: labels.count(label) for label in set(labels)}
print(freq)
```

---

## 12) Real-time usage examples (automation + AI testing)

### A) Run a suite of tests
```python
test_ids = ["TC_01", "TC_02", "TC_03"]
results = {}

for test_id in test_ids:
    # pretend to run test, get result
    result = "PASS" if test_id != "TC_02" else "FAIL"
    results[test_id] = result

print(results)
```

### B) Retry an API call until success or max attempts
```python
attempt = 0
max_attempts = 5
success = False

while attempt < max_attempts and not success:
    attempt += 1
    # simulate calling API - succeeds on 3rd try
    success = (attempt == 3)
    print(f"Attempt {attempt}: {'success' if success else 'retrying'}")
```

### C) Stop processing on first failure
```python
statuses = [200, 200, 500, 200]
for status in statuses:
    if status != 200:
        print("Stopping - failure detected")
        break
    print(f"OK: {status}")
```

### D) Skip invalid records while processing a batch
```python
records = [{"id": 1, "score": 0.9}, {"id": 2, "score": None}, {"id": 3, "score": 0.7}]
for record in records:
    if record["score"] is None:
        continue
    print(f"Record {record['id']}: {record['score']}")
```

### E) Poll a job status until it's done
```python
statuses = iter(["RUNNING", "RUNNING", "DONE"])  # simulated poll results

status = next(statuses)
while status != "DONE":
    print(f"Polling... status={status}")
    status = next(statuses)
print("Job finished")
```

---

## 13) `for` vs `while` (decision guide)

| Scenario | Use |
|----------|-----|
| Known collection/sequence (list, dict, range) | `for` |
| Fixed number of repetitions | `for` with `range()` |
| Unknown number of repetitions, condition-based | `while` |
| Retry logic until success/limit | `while` |
| Polling/waiting for external state change | `while` |

---

## 14) Common mistakes and fixes

1. Infinite `while` loop — forgetting to update the condition variable
```python
count = 0
while count < 5:
    print(count)
    count += 1  # must update, else infinite loop
```

2. Off-by-one errors with `range()`
```python
# range(5) gives 0-4, not 1-5
for i in range(1, 6):  # use this for 1 to 5 inclusive
    print(i)
```

3. Modifying a list while iterating over it directly
```python
items = [1, 2, 3, 4]
# for i in items:
#     if i % 2 == 0:
#         items.remove(i)  # BUG: skips elements, unpredictable

items = [i for i in items if i % 2 != 0]  # safe: build new list
```

4. Confusing `break` and `continue`
```python
# break -> exits loop entirely
# continue -> skips only current iteration, loop continues
```

5. Forgetting `for...else` only skips `else` if `break` happened (not on normal completion)
```python
for i in range(3):
    print(i)
else:
    print("Loop completed normally")  # always runs unless break happened
```

---

## 15) Quick cheat sheet

```python
# for over list/range/dict/string
for item in items:
for i in range(n):
for k, v in d.items():
for i, item in enumerate(items):

# while
while condition:
    ...

# while True with break
while True:
    if exit_condition:
        break

# control statements
break      # exit loop
continue   # skip to next iteration
pass       # no-op placeholder

# loop else (runs if no break)
for x in items:
    ...
else:
    ...

# comprehension
[x for x in items if condition]
{x: y for x, y in items}
```

---

## 16) Interview points to remember

- `for` = known/finite iterable; `while` = condition-based, unknown iteration count.
- `break` exits the loop completely; `continue` skips only the current iteration.
- Loop `else` runs only if the loop completes without hitting `break` — applies to both `for` and `while`.
- Never mutate a list while iterating over it directly — build a new list/comprehension instead.
- `while True` + `break`/`continue` is the standard pattern for "loop with no natural condition, controlled entirely from inside."
- `enumerate()` gives index + value together — cleaner than manual counters.
- `print(..., end=" ")` changes the line ending so loop output can print on one line instead of one-per-line.

---

## 17) Practice prompts (self-assignment)

1. Loop through a list of test IDs and print each with its index using `enumerate()`.
2. Write a `while` loop that retries an operation up to 3 times, printing attempt number.
3. Use `break` to stop processing a list of status codes at the first non-200 value.
4. Use `continue` to skip `None` values while summing a list of scores.
5. Write a `for...else` loop that searches for a target test ID and prints "not found" only if it never breaks.

---

## 18) Summary

- `for` loops iterate over known/finite sequences; `while` loops repeat based on a condition.
- `break` stops the loop entirely; `continue` skips to the next iteration; `pass` is a no-op.
- Loop `else` clause runs only when the loop finishes without `break`.
- Common uses: running test suites, retrying API calls, polling job status, filtering/skipping invalid records.
- Prefer comprehensions for simple transform/filter loops; use full loops when logic is more complex.