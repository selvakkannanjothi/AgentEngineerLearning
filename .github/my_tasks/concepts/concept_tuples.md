# Tuples in Python - Complete Revision Notes

## 1) What is a tuple?
A tuple is an ordered collection of values.
- Ordered: keeps insertion order.
- Indexed: access items by position.
- Immutable: cannot change after creation.
- Allows duplicate values.
- Can contain mixed data types.

Example:
```python
user = (101, "jothis", "qa", True)
```

---

## 2) Why tuples are needed (problem-first view)
Use tuples when data should stay fixed.

Common problem with lists:
- You store test metadata in a list.
- Someone accidentally modifies value order or content.
- Test results become flaky/inconsistent.

Tuple solution:
- Store fixed records/config as tuple to prevent accidental changes.

Example:
```python
# Fixed test case metadata
case = ("toxicity_check", "gpt-4o", 0.2, "SAFE")
```

---

## 3) Tuple creation syntax
### Basic
```python
t1 = (1, 2, 3)
```

### Without parentheses (packing)
```python
t2 = 1, 2, 3
```

### Single-item tuple (important)
```python
a = (5,)   # tuple
b = (5)    # int, not tuple
```

### Empty tuple
```python
empty = ()
```

### Tuple from iterable
```python
t3 = tuple(["a", "b", "c"])
```

---

## 4) Accessing tuple values
### Indexing
```python
t = ("PASS", "FAIL", "SKIP")
print(t[0])   # PASS
print(t[-1])  # SKIP
```

### Slicing
```python
nums = (10, 20, 30, 40, 50)
print(nums[1:4])  # (20, 30, 40)
```

---

## 5) Tuple immutability
You cannot update, insert, or delete tuple items directly.

```python
t = (1, 2, 3)
# t[0] = 99      # TypeError
# t.append(4)    # AttributeError
```

Workaround if needed:
```python
t = (1, 2, 3)
modified = t + (4,)
print(modified)  # (1, 2, 3, 4)
```

---

## 6) Packing and unpacking
### Packing
```python
record = "TC_01", "PASS", 1.2
```

### Unpacking
```python
test_id, status, duration = record
```

### Extended unpacking
```python
first, *middle, last = (10, 20, 30, 40, 50)
print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

---

## 7) Returning multiple values from functions
Functions often return tuple values.

```python
def response_metrics(times):
    return min(times), max(times), sum(times) / len(times)

mn, mx, avg = response_metrics([120, 140, 100])
print(mn, mx, avg)  # 100 140 120.0
```

Why useful:
- One function can return related outputs neatly.
- Cleaner than returning a long list and indexing manually.

---

## 8) Tuple methods
Tuples have only two methods because they are immutable.

### `count(x)`
Returns how many times value appears.
```python
t = (200, 500, 200, 404, 200)
print(t.count(200))  # 3
```

### `index(x)`
Returns index of first matching value.
```python
t = ("PASS", "PASS", "FAIL")
print(t.index("FAIL"))  # 2
```

---

## 9) Useful built-in functions with tuples
```python
t = (5, 2, 9, 1)

print(len(t))      # 4
print(min(t))      # 1
print(max(t))      # 9
print(sum(t))      # 17
print(sorted(t))   # [1, 2, 5, 9]  (returns list)
```

Note:
- `sorted()` returns a list, not tuple.

---

## 10) Tuple vs List (decision guide)
Use tuple when:
- Data is fixed and should not change.
- You need hashable keys in dictionaries.
- You return multiple values from functions.

Use list when:
- Data changes often (append/remove/update/sort in place).
- You need dynamic collection behavior.

Quick rule:
- Tuple = fixed record.
- List = editable collection.

---

## 11) Real-time usage examples (automation + AI testing)
### A) Fixed HTTP success codes
```python
SUCCESS_CODES = (200, 201, 204)
if 201 in SUCCESS_CODES:
    print("Success")
```

### B) Coordinate pair from UI automation
```python
login_btn_pos = (120, 340)  # (x, y)
```

### C) Test case metadata
```python
case = ("prompt_injection", "gpt-4o", 0.0, "BLOCK")
```

### D) Tuple key in expected-result map
```python
expected = {
    ("admin", "delete"): "DENY",
    ("qa", "view"): "ALLOW"
}
```

### E) Model output ranking pairs
```python
scores = [("run_1", 0.88), ("run_2", 0.92), ("run_3", 0.85)]
best = sorted(scores, key=lambda x: x[1], reverse=True)
print(best[0])  # ('run_2', 0.92)
```

---

## 12) Nested tuples
```python
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])  # 3
```

Useful for:
- Fixed 2D points
- Immutable lookup tables

---

## 13) Mutability inside tuple (important interview point)
Tuple is immutable, but if it contains mutable object, that inner object can change.

```python
t = (1, [2, 3], 4)
t[1].append(5)
print(t)  # (1, [2, 3, 5], 4)
```

Reason:
- Tuple structure is fixed.
- Inner list object can still mutate.

---

## 14) Common mistakes and fixes
1. Single item tuple mistake
```python
x = (10)    # wrong for tuple
x = (10,)   # correct
```

2. Expecting tuple methods like list
```python
# t.append(5)  # invalid
```

3. Confusing reverse sort and reverse order
- Tuple has no `.sort()` or `.reverse()` methods.
- Use `sorted(t, reverse=True)` when needed.

---

## 15) Conversions
```python
# tuple -> list
items = ("a", "b", "c")
items_list = list(items)

# list -> tuple
nums_list = [1, 2, 3]
nums_tuple = tuple(nums_list)
```

Use case:
- Convert to list for editing, convert back to tuple for safety.

---

## 16) Performance note (practical)
- Tuples are generally a bit lighter and faster than lists for fixed data.
- Choose tuple mainly for data integrity/intent, not micro-optimization.

---

## 17) Mini cheat sheet
```python
# Create
(1, 2, 3)
(5,)

# Access
t[0]
t[-1]
t[1:3]

# Methods
t.count(x)
t.index(x)

# Built-ins
len(t), min(t), max(t), sum(t), sorted(t)

# Unpack
a, b, c = t
```

---

## 18) Practice prompts (self-assignment)
1. Create a tuple for test metadata: `(test_id, model, temperature, expected)`.
2. Given `(200, 200, 500, 404, 500)`, count `500`.
3. Unpack `(120, 260, 180.0)` into `min_time`, `max_time`, `avg_time`.
4. Use tuple as dict key for `(role, action)` permissions.
5. Convert list to tuple after finalizing test input data.

---

## 19) Summary
- Tuple is immutable, ordered, and index-based.
- Best for fixed records, constants, function multi-returns, and dict keys.
- Use list for dynamic data and tuple for protected/finalized data.

---

## 20) Packing and Unpacking (detailed)

### What is Packing?
Packing means combining multiple values into a single tuple variable.

```python
# With parentheses
user_details = ("selva", 33, "tester")

# Without parentheses (implicit packing)
user_details = "selva", 33, "tester"
```

Both produce the same result: one tuple from multiple values.

---

### What is Unpacking?
Unpacking means extracting tuple values into separate individual variables.

```python
user_details = ("selva", 33, "tester")

name, age, role = user_details

print(name)   # selva
print(age)    # 33
print(role)   # tester
```

Each variable receives the value at the matching position.

---

### Packing variables into a new tuple
You can also pack existing variables into a new tuple.

```python
name_1 = "sowmya"
age = 24
role = "gen ai tester"

user_details_2 = (name_1, age, role)
print(user_details_2)
# ('sowmya', 24, 'gen ai tester')
```

---

### Key rule for unpacking
Number of variables must exactly match number of tuple items.

Correct:
```python
a, b, c = (10, 20, 30)
```

Error:
```python
a, b = (10, 20, 30)    # ValueError: too many values to unpack
a, b, c, d = (10, 20)  # ValueError: not enough values to unpack
```

---

### Extended unpacking with * (star operator)
Use `*` to capture multiple values into a list when count is not fixed.

```python
first, *middle, last = (10, 20, 30, 40, 50)

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

Useful when:
- You want first and last items separately.
- Middle items count is variable.

---

### Real-time examples (automation + AI testing)

#### Unpack API response record
```python
response = ("TC_01", 200, 0.88)
test_id, status_code, confidence = response

print(f"Test: {test_id}, Status: {status_code}, Score: {confidence}")
```

#### Unpack function return values
```python
def response_metrics(times):
    return min(times), max(times), sum(times) / len(times)

mn, mx, avg = response_metrics([120, 140, 100])
print(mn, mx, avg)  # 100 140 120.0
```

#### Pack model config and pass to function
```python
model_config = ("gpt-4o", 0.2, 1000)

def run_model(model, temperature, max_tokens):
    print(f"Model: {model}, Temp: {temperature}, Tokens: {max_tokens}")

run_model(*model_config)
# Model: gpt-4o, Temp: 0.2, Tokens: 1000
```

Note: `*model_config` unpacks tuple into positional arguments.

---

### Swap variables using unpacking
```python
a = "PASS"
b = "FAIL"

a, b = b, a

print(a)  # FAIL
print(b)  # PASS
```

No temp variable needed — Python unpacks right side first, then assigns.

---

### Quick summary
| Term       | What it does                                | Example                          |
|------------|---------------------------------------------|----------------------------------|
| Packing    | Multiple values → one tuple                 | `t = "a", "b", "c"`             |
| Unpacking  | One tuple → multiple variables              | `a, b, c = t`                   |
| Extended   | Capture variable-count middle values        | `first, *mid, last = t`         |
| Swap       | Exchange two values without temp variable   | `a, b = b, a`                   |

---

## 21) Extended Unpacking (extra revision)

Extended unpacking means using `*` in assignment to capture multiple remaining values.

### Core patterns
```python
# first item + middle items + last item
first, *middle, last = (1, 2, 3, 4, 5)

# all except last
*head, last = (10, 20, 30, 40)

# first + all remaining
first, *tail = ("a", "b", "c")
```

### What each variable gets
```python
first, *middle, last = (10, 20, 30, 40, 50)

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

Important:
- Starred target (`*middle`) always becomes a `list`.
- Works with tuples, lists, and strings.

### String example
```python
first, *mid, last = "python"
print(first)  # p
print(mid)    # ['y', 't', 'h', 'o']
print(last)   # n
```

### Real-time test flow example
```python
flow = ("TC_09", "setup", "api_call", "assert", "cleanup", "PASS")

test_id, *steps, result = flow

print(test_id)  # TC_09
print(steps)    # ['setup', 'api_call', 'assert', 'cleanup']
print(result)   # PASS
```

### Common mistakes
```python
# Invalid: more than one starred variable
# a, *b, *c = (1, 2, 3)

# Invalid: variable count mismatch without star
# a, b = (1, 2, 3)
```

### Quick memory rule
- `*` means: "collect remaining values here".
- Use it when number of middle values can vary.
