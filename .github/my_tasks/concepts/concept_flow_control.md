# Flow Control (if/elif/else) in Python - Complete Revision Notes

## 1) What is flow control?
Flow control lets a program make decisions and run different code blocks depending on conditions, instead of executing every line top-to-bottom unconditionally.

Example:
```python
status_code = 404
if status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
```

**Indentation is very important:** Python uses indentation (whitespace), not braces `{}`, to define which statements belong to a block (the `if`, `elif`, `else`, `for`, `while`, function, etc.). All statements in the same block must be indented by the same amount (convention: 4 spaces). Mixing tabs/spaces or inconsistent indent levels raises an `IndentationError`.

```python
if status_code == 200:
    print("A")   # same indent - inside the if block
    print("B")   # same indent - inside the if block
print("C")       # no indent - outside the if block, always runs
```

---

## 2) Why flow control is needed (problem-first view)

Problem: an automation script gets an API status code back and must react differently depending on the value — pass, retry, or fail — not just print it.

Without flow control:
```python
status_code = 500
print("Test result")  # same message no matter what happened - useless
```

With flow control:
```python
status_code = 500
if status_code == 200:
    print("Test Passed")
elif status_code == 500:
    print("Server Error - Retry")
else:
    print("Unknown status - Investigate")
```

---

## 3) Basic `if` syntax
```python
if condition:
    # runs only if condition is True
    statement
```

Example:
```python
score = 0.85
if score > 0.8:
    print("High confidence")
```

---

## 4) `if / else`
```python
if condition:
    statement_a
else:
    statement_b
```

Example:
```python
response_time = 3.2
if response_time <= 2:
    print("Fast response")
else:
    print("Slow response")
```

---

## 5) `if / elif / else` (multiple conditions)
```python
if condition_1:
    statement_1
elif condition_2:
    statement_2
elif condition_3:
    statement_3
else:
    fallback_statement
```

Example:
```python
status_code = 404
if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code == 500:
    print("Server Error")
else:
    print("Unhandled status code")
```

- Conditions are checked top to bottom.
- The **first** True condition's block runs; the rest are skipped.
- `else` is optional — only runs if nothing above matched.

---

## 6) Comparison operators (used inside conditions)
| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

```python
tokens_used = 1200
if tokens_used >= 1000:
    print("Approaching token limit")
```

---

## 7) Logical operators (combine conditions)
| Operator | Meaning |
|----------|---------|
| `and` | True only if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Flips True/False |

```python
status_code = 200
response_time = 1.5

if status_code == 200 and response_time < 2:
    print("Fast and successful")

if status_code == 404 or status_code == 500:
    print("Failure status")

is_valid = False
if not is_valid:
    print("Invalid response")
```

### Short-circuit evaluation
When combining multiple `and`/`or` conditions, Python stops evaluating as soon as the overall result is already known — the remaining conditions are **not executed at all**.

- `and` — if the first condition is False, the whole expression is already False, so the rest are skipped.
- `or` — if the first condition is True, the whole expression is already True, so the rest are skipped.

```python
def is_logged_in():
    print("checked login")
    return False

def has_permission():
    print("checked permission")  # never printed - short-circuited
    return True

if is_logged_in() and has_permission():
    print("Access granted")
# checked login
# (has_permission() never runs because is_logged_in() was already False)
```

This matters in real code: put the cheapest/most-likely-to-fail condition first, and it's safe to rely on short circuiting to avoid errors, e.g.:
```python
data = None
if data and data.get("status") == 200:   # data.get(...) never runs if data is None/empty
    print("OK")
```

---

## 8) Truthy and Falsy values, and the Boolean type
Any value can be used directly in an `if` condition without comparing to `True`/`False`.

Falsy values: `0`, `0.0`, `""` (empty string), `[]`, `{}`, `set()`, `None`, `False`
Everything else is truthy.

```python
response = {}
if response:
    print("Has data")
else:
    print("Empty response")  # this runs - {} is falsy

username = ""
if username:
    print(f"Welcome {username}")
else:
    print("Username missing")  # this runs - "" is falsy
```

**Boolean is really an int under the hood:** the `bool` class is a subclass of `int`. `True` behaves as `1` and `False` behaves as `0` in arithmetic and comparisons.

```python
print(True == 1)    # True
print(False == 0)   # True
print(True + True)  # 2  - bool added like an int
print(isinstance(True, int))  # True - bool is an int subclass
```

---

## 9) Nested conditions
```python
status_code = 200
payload = {"id": 1}

if status_code == 200:
    if payload:
        print("Success with data")
    else:
        print("Success but empty payload")
else:
    print("Request failed")
```

Prefer combining with `and` when possible to avoid deep nesting:
```python
if status_code == 200 and payload:
    print("Success with data")
```

---

## 10) Ternary (conditional) expression
Compact one-line if/else for simple value assignment.

```python
score = 0.72
result = "PASS" if score >= 0.7 else "FAIL"
print(result)  # PASS
```

---

## 11) `pass` in conditions
`pass` is a no-op placeholder — used when a branch is syntactically required but there's nothing to do yet.

```python
status_code = 500
if status_code == 200:
    pass  # TODO: handle success later
else:
    print("Handle failure")
```

---

## 12) Real-time usage examples (automation + AI testing)

### A) API status validation
```python
status_code = 201
if status_code == 200 or status_code == 201:
    print("Request succeeded")
elif 400 <= status_code < 500:
    print("Client error")
elif status_code >= 500:
    print("Server error")
```

### B) LLM response confidence gating
```python
confidence = 0.62
if confidence >= 0.9:
    label = "HIGH"
elif confidence >= 0.6:
    label = "MEDIUM"
else:
    label = "LOW"
print(label)  # MEDIUM
```

### C) Test result triage
```python
result = "FAIL"
retry_count = 2

if result == "PASS":
    print("No action needed")
elif result == "FAIL" and retry_count < 3:
    print("Retrying test")
else:
    print("Marking as broken - manual review")
```

### D) Guard clause pattern (early exit)
```python
def check_response(response):
    if not response:
        return "No response received"
    if response.get("status") != 200:
        return "Non-200 status"
    return "OK"
```

---

## 13) Common mistakes and fixes

1. Using `=` instead of `==`
```python
# if status_code = 200:   # SyntaxError
if status_code == 200:    # correct
```

2. Forgetting that `elif` order matters (first True wins)
```python
score = 95
if score >= 50:
    print("Pass")   # this runs even though score also >= 90
elif score >= 90:
    print("Distinction")  # never reached - unreachable
```

3. Comparing with `is` instead of `==` for values
```python
# if status_code is 200:   # works by luck for small ints, unreliable
if status_code == 200:     # correct for value comparison
```
Use `is` only for identity checks like `is None`.

4. Deep nested ifs instead of combining with `and`
```python
# Avoid:
if a:
    if b:
        print("both true")
# Prefer:
if a and b:
    print("both true")
```

---

## 14) Quick cheat sheet

```python
# Basic
if condition:
    ...

# if/else
if condition:
    ...
else:
    ...

# if/elif/else
if condition_1:
    ...
elif condition_2:
    ...
else:
    ...

# Ternary
value = a if condition else b

# Combine conditions
if a and b:
if a or b:
if not a:

# Falsy check
if not response:  # empty dict/list/string/None/0/False
```

---

## 15) Interview points to remember

- Only the first True branch in an if/elif chain runs; rest are skipped.
- `elif` order matters — put more specific/narrow conditions before general ones.
- Use `==` for value equality, `is` for identity (mainly `is None`).
- Empty collections, `0`, `""`, and `None` are all falsy.
- `bool` is a subclass of `int` — `True == 1` and `False == 0`.
- `and`/`or` short-circuit — later conditions may never execute if the result is already decided.
- Indentation defines blocks in Python — inconsistent indentation is a syntax error, not just a style issue.
- Ternary expressions are for simple value assignment, not complex logic.
- Guard clauses (`if not x: return`) reduce nesting and improve readability.

---

## 16) Practice prompts (self-assignment)

1. Write an if/elif/else to classify an HTTP status code range (2xx, 4xx, 5xx).
2. Use a ternary to assign PASS/FAIL based on a score threshold.
3. Write nested conditions for checking status code AND payload presence, then rewrite using `and`.
4. Classify an LLM confidence score into HIGH/MEDIUM/LOW bands.
5. Write a guard-clause function that validates an API response step by step.

---

## 17) Summary

- Flow control decides which code block executes based on conditions.
- `if`, `elif`, `else` form a top-to-bottom decision chain — first True wins.
- Combine conditions with `and`/`or`/`not`; avoid unnecessary nesting.
- Falsy values (`0`, `""`, `[]`, `{}`, `None`, `False`) let you check emptiness directly.
- Ternary expressions give a compact one-liner for simple choices.
- Widely used for API status handling, confidence thresholds, and test result triage.