# Agent Memory - Learning Context

## Who I am
- Name: Selva (Jothis)
- Background: Automation tester with Selenium Java, API Testing, Cypress, JavaScript
- Goal: Learn Python from scratch to transition into AI Testing and understand LLM foundations
- Editor: PyCharm on Windows

---

## My 4-Step Learning Workflow
Every new topic follows this exact pattern - always follow it proactively:

1. **Learn** → Explain the topic with problem-first approach and real-time examples (automation/AI testing context)
2. **Concepts** → Save full revision notes to `.github/my_tasks/concepts/concept_<topic>.md`
3. **Tasks** → Create practice tasks (Problem Statements + Q&A + Self Assignments) to `.github/my_tasks/tasks/<topic>_method_tasks.md`
4. **Quick Notes** → Append one-liner summary to `.github/my_notes.txt` under `Topic: <TopicName>`

---

## File Structure
```
.github/
    my_notes.txt                          # Quick revision - one-liners per method/concept
    my_tasks/
        concepts/
            concepts_list.md              # Full list revision notes
            concept_tuples.md             # Full tuple revision notes
            concept_sets.md               # Full sets revision notes
            concept_frozensets.md         # Full frozenset revision notes
            concept_hashable_unhashable.md # Hashable vs unhashable concepts
            concept_strings.md            # Full strings revision notes
            concept_dictionary.md         # Full dictionary revision notes
            concept_flow_control.md       # Full flow control (if/elif/else) revision notes
            concept_loops.md              # Full loops (for/while) revision notes
        tasks/
            list_method_tasks.md          # List practice tasks (Q&A + self-assignments)
            tuple_method_tasks.md         # Tuple practice tasks (Q&A + self-assignments)
            set_method_tasks.md           # Set practice tasks (Q&A + self-assignments)
            frozenset_method_tasks.md     # Frozenset practice tasks
            hashable_unhashable_method_tasks.md # Hashable practice tasks
            string_method_tasks.md        # String practice tasks
            dictionary_method_tasks.md    # Dictionary practice tasks
            flow_control_method_tasks.md  # Flow control practice tasks
            loops_method_tasks.md         # Loop practice tasks
demo.py                                   # Active practice/scratch file
AGENTS.md                                 # This file - agent memory
```

---

## Topics Completed

### Phase 1: Python Fundamentals
- [x] Lists - methods, examples, tasks, notes
- [x] Tuples - immutability, packing, unpacking, extended unpacking, tasks, notes
- [x] Sets - set operations, methods, comparison methods, tasks, notes
- [x] Frozensets - immutable sets, hashable, tasks, notes
- [x] Hashable & Unhashable - what makes a type usable as dict key or set element
- [x] Strings - methods, slicing, formatting, f-strings, tasks, notes
- [x] Dictionaries - methods, access patterns, iteration, tasks, notes
- [x] Program flow control (if/elif/else) - conditions, logical operators, truthy/falsy, ternary, tasks, notes
- [x] Loops (for, while, comprehensions) - iteration, break/continue, loop-else, nested loops, tasks, notes
- [ ] Functions and lambda expressions
- [ ] Working with files and data (read/write, JSON, CSV)
- [ ] Regular expressions for text processing
- [ ] Errors, exception handling, and debugging
- [ ] OOP essentials (classes, objects, inheritance, polymorphism)

### Phase 2 onwards
- [ ] Python modules and imports
- [ ] OS module
- [ ] pip and virtual environments
- [ ] LLM Foundations
- [ ] OpenAI API
- [ ] MCP (Model Context Protocol)
- [ ] Prompt Engineering
- [ ] Google Gemini
- [ ] LangChain
- [ ] Embeddings and Vector Stores
- [ ] RAG (Retrieval-Augmented Generation)
- [ ] Advanced Projects (LangGraph, ArXiv, SerpAPI)

---

## Teaching Style Preferences
- Always start with **problem statement first** (why do we need this)
- Use **automation + AI testing** context in all examples (API statuses, prompts, test cases, model runs)
- Keep examples practical: test queues, response codes, LLM labels, token usage
- After explaining a topic, proactively offer to create concept file + task file + update notes
- Format tasks file with 3 sections: Problem Statements (With Input Data), Questions and Answers, Self Assignments (No Answers)
- Format concept file with numbered sections matching `concept_tuples.md` style

---

## Key Concepts Already Explained (with extra detail)
- f-strings: `f"value is {var}"` - avoid string + int concat errors
- `sort(reverse=True)` vs `reverse()` - sort by value vs flip current order
- Tuple immutability vs variable rebinding - reassigning variable is not mutation
- Packing and unpacking - `a, b, c = tuple` and `first, *mid, last = tuple`
- Extended unpacking `*` - starred variable always becomes a list
- `remove()` vs `discard()` in sets - discard is safe (no KeyError)
- `Final` type hint for constants - prevents accidental reassignment

