# Python & AI Testing Learning Agent

## About You
- **Name**: Selva (Jothis)
- **Background**: Automation tester with experience in Selenium Java, API Testing, Cypress, and JavaScript
- **Goal**: Learn Python from scratch to transition into AI Testing and understand LLM foundations
- **Editor**: PyCharm on Windows

---

## My 4-Step Learning Workflow
Every new topic follows this exact pattern — always follow it proactively:

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
        tasks/
            list_method_tasks.md          # List practice tasks (Q&A + self-assignments)
            tuple_method_tasks.md         # Tuple practice tasks (Q&A + self-assignments)
            set_method_tasks.md           # Set practice tasks (Q&A + self-assignments)
demo.py                                   # Active practice/scratch file
AGENTS.md                                 # Root agent memory file
```

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

---

## Learning Path Overview

### Phase 1: Python Fundamentals
- [x] Lists - methods, examples, tasks, notes
- [x] Tuples - immutability, packing, unpacking, extended unpacking, tasks, notes
- [x] Sets - set operations, methods, comparison methods, tasks, notes
- [ ] Dictionaries
- [ ] Program flow control (if/elif/else)
- [ ] Loops (for, while, comprehensions)
- [ ] Functions and lambda expressions
- [ ] Working with files and data (read/write, JSON, CSV)
- [ ] Regular expressions for text processing
- [ ] Errors, exception handling, and debugging
- [ ] OOP essentials (classes, objects, inheritance, polymorphism)

### Phase 2: Python Ecosystem
- [ ] Understanding Python modules and imports
- [ ] OS module for system operations
- [ ] Mastering pip for package management
- [ ] Using virtual environments in PyCharm

### Phase 3: LLM Foundations
- [ ] Introduction to LLMs (Large Language Models)
- [ ] APIs and GenAI libraries
- [ ] Tokens, context windows, and cost considerations
- [ ] AI as a Service (AaaS)
- [ ] Challenges and limitations of LLMs

### Phase 4: OpenAI API with Python
- [ ] Setting up OpenAI API
- [ ] Making API calls with Python
- [ ] Handling responses and streaming
- [ ] Best practices for API usage

### Phase 5: MCP (Model Context Protocol)
- [ ] Understanding MCP architecture
- [ ] Running remote MCP servers
- [ ] Integration with OpenAI API

### Phase 6: Prompt Engineering
- [ ] Prompt design principles
- [ ] Few-shot and zero-shot prompting
- [ ] Chain-of-thought reasoning
- [ ] Prompt optimization techniques

### Phase 7: Google Gemini
- [ ] Gemini API setup
- [ ] Comparing Gemini vs OpenAI
- [ ] Multimodal capabilities

### Phase 8: LangChain
- [ ] LangChain fundamentals
- [ ] Chains and agents
- [ ] Integration with OpenAI and Gemini
- [ ] Memory and conversation management

### Phase 9: Embeddings & Vector Stores
- [ ] Understanding embeddings
- [ ] Vector databases (Pinecone, Chroma)
- [ ] Similarity search

### Phase 10: RAG (Retrieval-Augmented Generation)
- [ ] RAG architecture
- [ ] Document loading and chunking
- [ ] Q&A on private documents
- [ ] Project: RAG application with Pinecone/Chroma

### Phase 11: Advanced Projects
- [ ] Research Agent with LangGraph
- [ ] Integration with GPT-4o, ArXiv, SerpAPI
- [ ] Building end-to-end AI testing workflows
