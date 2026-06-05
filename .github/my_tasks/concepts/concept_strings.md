# Strings in Python - Complete Revision Notes

## 1) What is a string?
A string is a **collection of characters** stored as an ordered, immutable sequence.

- Ordered: keeps character positions
- Indexed: access by index
- Immutable: cannot modify in place
- UTF-8: supports any language, emojis, special characters

```python
name = "Selva"
greeting = 'Hello, World!'
emoji_test = "✅ Test passed 🚀"
japanese = "テスト"
```

---

## 2) Why strings are essential (problem-first view)
In API and AI testing you constantly work with:
- API response messages (`"success"`, `"unauthorized"`)
- Prompt text for LLM validation
- Test case names, log messages, CSV/JSON field values
- User input parsing

Strings are everywhere. Understanding slicing, methods, and formatting is non-negotiable.

---

## 3) Creating strings

### Single or double quotes
```python
a = 'hello'
b = "hello"
```

### Triple quotes (multiline)
```python
prompt = """
You are an AI assistant.
Answer clearly and concisely.
"""
```

### Using `\n` for newline (alternative to triple quotes)
```python
msg = "Line 1\nLine 2\nLine 3"
print(msg)
```

### Raw string (ignores escape sequences)
```python
path = r"C:\Users\jothis\file.txt"
print(path)  # C:\Users\jothis\file.txt
```

---

## 4) Escape sequences (must know)

| Escape | Meaning          | Example                         |
|--------|------------------|---------------------------------|
| `\n`   | newline          | `"line1\nline2"`                |
| `\t`   | tab              | `"col1\tcol2"`                  |
| `\\`   | single backslash | `print('\\selva')` → `\selva`   |
| `\'`   | single quote     | `'it\'s a test'`                |
| `\"`   | double quote     | `"he said \"pass\""`            |

```python
print("status:\t200")       # status:  200
print("line1\nline2")       # newline
print('\\selva')            # \selva
print('it\'s working')      # it's working
```

Note: `#` inside a string is NOT a comment — it's a regular character.
```python
msg = "# this is not a comment"  # valid string
```

---

## 5) User input
```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

Important: `input()` always returns a **string**.
```python
age = input("Enter age: ")
print(type(age))   # <class 'str'>
```

---

## 6) Type conversion

```python
# String to int
age = int(input("Enter age: "))

# String to float
score = float(input("Enter score: "))

# Int to string
status_code = 200
msg = "Code: " + str(status_code)

# Combined conversion
num = int(input("Enter a number: "))
```

Cannot concatenate string and number directly:
```python
# "Code: " + 200       # TypeError
"Code: " + str(200)    # works
f"Code: {200}"         # cleaner
```

---

## 7) Indexing and negative indexing

```python
model = "gpt-4o"

print(model[0])    # g
print(model[1])    # p
print(model[-1])   # o  (last char)
print(model[-2])   # 4  (second from last)
```

---

## 8) Length

```python
msg = "Hello Selva"
print(len(msg))   # 11
```

---

## 9) Immutability
Strings cannot be changed in place.

```python
name = "selva"
# name[0] = "S"    # TypeError: 'str' object does not support item assignment
```

To "modify" a string, create a new one:
```python
name = "S" + name[1:]
print(name)  # Selva
```

---

## 10) Concatenation and repetition

### Concatenation with `+`
```python
first = "API"
second = "Test"
result = first + " " + second
print(result)  # API Test
```

### Repetition with `*`
```python
line = "-" * 30
print(line)  # ------------------------------

msg = "PASS "
print(msg * 3)  # PASS PASS PASS
```

---

## 11) Slicing
```python
text = "automation"
```

### `string[start:stop]`
```python
print(text[0:4])   # auto
print(text[4:])    # mation
print(text[:4])    # auto
print(text[:])     # automation (full copy)
```

### `string[start:stop:step]`
```python
print(text[0:8:2])    # atml
print(text[::2])      # atnto  (every other char)
print(text[::-1])     # noitamotua (reverse string)
print(text[::-2])     # notm (reverse with step 2)
```

### Negative slicing
```python
print(text[-4:])      # tion (last 4 chars)
print(text[:-4])      # automa (all except last 4)
print(text[-6:-2])    # atio
```

### Slicing cheatsheet
| Syntax       | Meaning                       |
|--------------|-------------------------------|
| `s[1:4]`     | index 1 to 3                  |
| `s[:4]`      | first 4 chars                 |
| `s[4:]`      | from index 4 to end           |
| `s[:]`       | full copy                     |
| `s[::2]`     | every 2nd char                |
| `s[::-1]`    | reversed string               |
| `s[-1]`      | last char                     |
| `s[-4:]`     | last 4 chars                  |

---

## 12) Case methods

```python
text = "Prompt Injection Test"

print(text.upper())       # PROMPT INJECTION TEST
print(text.lower())       # prompt injection test
print(text.title())       # Prompt Injection Test
print(text.capitalize())  # Prompt injection test
print(text.swapcase())    # pROMPT iNJECTION tEST
```

---

## 13) Strip methods (remove whitespace)

```python
text = "   PASS   "

print(text.strip())   # "PASS"
print(text.lstrip())  # "PASS   "
print(text.rstrip())  # "   PASS"
```

Also works with specific characters:
```python
text = "---PASS---"
print(text.strip("-"))   # PASS
```

---

## 14) replace()
```python
msg = "status: failed"
print(msg.replace("failed", "passed"))
# status: passed

# Replace all occurrences
log = "TC01 PASS TC02 PASS"
print(log.replace("PASS", "✅"))
# TC01 ✅ TC02 ✅
```

---

## 15) count()
```python
log = "PASS FAIL PASS PASS FAIL"
print(log.count("PASS"))   # 3
print(log.count("FAIL"))   # 2
```

---

## 16) find() and index()

### `find(sub)` — returns index or `-1` if not found
```python
msg = "status: failed"
print(msg.find("failed"))   # 8
print(msg.find("error"))    # -1 (not found, no error)
```

### `index(sub)` — returns index or raises `ValueError`
```python
print(msg.index("failed"))  # 8
# msg.index("error")        # ValueError
```

Use `find()` when key may not exist (safer).

---

## 17) startswith() and endswith()
```python
endpoint = "/api/v1/users"
print(endpoint.startswith("/api"))   # True
print(endpoint.endswith("/users"))   # True

label = "SAFE_RESPONSE"
print(label.startswith("SAFE"))      # True
```

---

## 18) split() and join()

### `split(sep)` — string to list
```python
csv_row = "TC01,PASS,2.5s"
parts = csv_row.split(",")
print(parts)  # ['TC01', 'PASS', '2.5s']

log = "line1\nline2\nline3"
lines = log.split("\n")
```

### `join(iterable)` — list to string
```python
parts = ["TC01", "PASS", "2.5s"]
row = ",".join(parts)
print(row)   # TC01,PASS,2.5s

words = ["hello", "world"]
print(" ".join(words))   # hello world
print("-".join(words))   # hello-world
```

---

## 19) splitlines()
```python
response = "line1\nline2\nline3"
print(response.splitlines())
# ['line1', 'line2', 'line3']
```

---

## 20) removeprefix() and removesuffix()

```python
endpoint = "/api/v1/users"
print(endpoint.removeprefix("/api"))     # /v1/users
print(endpoint.removesuffix("/users"))   # /api/v1

label = "test_TC_001"
print(label.removeprefix("test_"))      # TC_001
print(label.removesuffix("_001"))       # test_TC
```

Note: Only removes if it matches exactly. No error if not found.

---

## 21) Membership check with `in`
```python
log = "connection timeout occurred"
print("timeout" in log)      # True
print("error" in log)        # False

blocked = {"hack", "bypass"}
prompt = "how to bypass filter"
if any(word in prompt for word in blocked):
    print("Blocked prompt detected")
```

---

## 22) String check methods (is... methods)

```python
print("abc123".isalnum())   # True  (letters + digits only)
print("abc".isalpha())      # True  (letters only)
print("123".isdigit())      # True  (digits only)
print("   ".isspace())      # True  (whitespace only)
print("Hello".istitle())    # True  (title case)
print("HELLO".isupper())    # True
print("hello".islower())    # True
```

Real-time use:
```python
user_input = input("Enter test count: ")
if user_input.isdigit():
    count = int(user_input)
else:
    print("Please enter a valid number")
```

---

## 23) Padding methods

```python
text = "PASS"

print(text.center(10))         #    PASS
print(text.center(10, "-"))    # ---PASS---
print(text.ljust(10))          # PASS
print(text.rjust(10))          #       PASS
print("42".zfill(5))           # 00042
```

Use case: fixed-width report formatting.

---

## 24) f-strings (formatted string literals)

```python
model = "gpt-4o"
score = 0.91234
tokens = 1500

print(f"Model: {model}")
print(f"Score: {score:.2f}")    # Score: 0.91
print(f"Score: {score:.4f}")    # Score: 0.9123
print(f"Tokens: {tokens:,}")    # Tokens: 1,500
```

### Debugging with `=`
```python
score = 0.91234
print(f"{score=}")       # score=0.91234
print(f"{model=}")       # model='gpt-4o'
```

### Inline expression
```python
print(f"Status: {'PASS' if score > 0.9 else 'FAIL'}")
# Status: PASS
```

---

## 25) format() method

```python
msg = "Model: {}, Score: {:.2f}".format("gpt-4o", 0.91)
print(msg)  # Model: gpt-4o, Score: 0.91

# Named
msg = "Model: {model}, Score: {score:.2f}".format(model="gpt-4o", score=0.91)
```

f-strings are preferred in modern Python — cleaner and faster.

---

## 26) help() for string exploration

```python
help(str)             # all string methods
help(str.strip)       # help for specific method
help(str.split)
```

Run in PyCharm console or Python shell to explore.

---

## 27) Common mistakes and fixes

1. Concatenate string + number directly:
```python
# "Code: " + 200     # TypeError
"Code: " + str(200)  # correct
f"Code: {200}"       # cleaner
```

2. Trying to modify string in place:
```python
# name[0] = "S"      # TypeError
name = "S" + name[1:]  # correct
```

3. `find()` vs `index()`:
```python
# Use find() when key may be missing (returns -1)
# Use index() when you expect it to exist (raises error)
```

4. `split()` default vs specific separator:
```python
"a b c".split()      # ['a', 'b', 'c']
"a,,b,,c".split(",") # ['a', '', 'b', '', 'c']
```

---

## 28) Mini cheat sheet

```python
# Creation
s = "hello"
s = 'hello'
s = """multiline"""
s = r"raw\nstring"

# Access
s[0]           # first char
s[-1]          # last char
s[1:4]         # slice
s[::-1]        # reverse

# Case
s.upper(), s.lower(), s.title(), s.capitalize(), s.swapcase()

# Strip
s.strip(), s.lstrip(), s.rstrip()

# Search
s.find(sub), s.index(sub), s.count(sub)
s.startswith(pre), s.endswith(suf)

# Modify (returns new string)
s.replace(old, new)
s.removeprefix(pre), s.removesuffix(suf)

# Split/Join
s.split(sep), sep.join(list)
s.splitlines()

# Check
s.isdigit(), s.isalpha(), s.isalnum()
s.isupper(), s.islower()

# Format
f"val: {var:.2f}"
f"{var=}"

# Length
len(s)
```

---

## 29) Real-time usage examples (automation + AI testing)

### A) Parse CSV log line
```python
log = "TC_01,PASS,2.5s,auth_module"
parts = log.split(",")
test_id, result, duration, module = parts
```

### B) Validate prompt for blocked words
```python
BLOCKED = ["hack", "bypass", "jailbreak"]
prompt = "please bypass the filter"

for word in BLOCKED:
    if word in prompt.lower():
        print(f"Blocked word found: {word}")
```

### C) Build API endpoint dynamically
```python
base = "https://api.example.com"
version = "v1"
resource = "users"
endpoint = f"{base}/{version}/{resource}"
print(endpoint)
```

### D) Format test report line
```python
tests = [("TC_01", "PASS", 0.92), ("TC_02", "FAIL", 0.71)]
for test_id, result, score in tests:
    print(f"{test_id:<10} {result:<6} {score:.2f}")
```

### E) Validate user input is number
```python
count = input("How many runs? ")
if count.isdigit():
    print(f"Running {int(count)} times")
```

---

## 30) Summary
- Strings are immutable, ordered, indexed sequences of characters.
- Use f-strings for formatting — cleanest and most readable.
- Use `get()` mental model for strings: `find()` is safe, `index()` raises error.
- `split()` + `join()` are powerful for parsing test logs and CSV.
- `strip()`, `replace()`, `upper()/lower()` are daily-use methods.
- Slicing `[::-1]` reverses strings — useful in data validation.

