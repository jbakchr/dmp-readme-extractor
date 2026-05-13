# dmp-readme-extractor

A simple prototype for transforming research `readme.txt` files into structured, machine-actionable JSON.

---

## 🧠 Motivation

In research data management, important information about datasets is often stored in human-readable README files.  
While useful for humans, these files are difficult for machines to process automatically.

This project demonstrates how such a README can be transformed into **structured JSON**, making it easier to:

- Extract metadata programmatically  
- Integrate with other systems  
- Enable further automation  

👉 The goal is **not perfection**, but to show how easy it is to go from *text → structured data*.

---

## 🚀 What it does

Given a `readme.txt` file with structured headers like:

```

Title of the dataset:
Creators (include contact and ORCID):
Description:
Keywords:

```

This tool will:

1. Parse the file into sections  
2. Extract basic structured information (creators, keywords, files, etc.)  
3. Output a JSON file with a consistent structure  

---

## 📦 Example

### Input (readme.txt)

```

Title of the dataset:
Supporting data for ...

Creators (include contact and ORCID):
Cindy Jespersen, contact: ..., ORCID: ...

```

### Output (output.json)

```json
{
  "dataset": {
    "title": "Supporting data for ...",
    "version": "1"
  },
  "people": {
    "creators": [
      {
        "name": "Cindy Jespersen",
        "email": "...",
        "orcid": "..."
      }
    ]
  }
}
```

***

## 🏗️ Project structure

    dmp-readme-extractor/
    │
    ├── convert.py            # CLI entrypoint
    ├── requirements.txt
    │
    ├── src/
    │   ├── parser.py         # splits text into sections
    │   ├── extractor.py      # extracts structured fields
    │   ├── transformer.py    # builds final JSON output
    │   ├── schema.py         # (placeholder for future schema work)
    │   └── utils.py
    │
    ├── data/
    │   ├── input/
    │   │   └── readme.txt
    │   └── output/
    │       └── output.json

***

## ▶️ Usage

Run the converter from the project root:

```bash
python3 convert.py data/input/readme.txt data/output/output.json
```

After running, you’ll find:

    data/output/output.json

***

## ⚙️ How it works (simple pipeline)

    readme.txt
       ↓
    parse_sections()          → split into header-based sections
       ↓
    extract_structured_data() → extract fields (creators, keywords, etc.)
       ↓
    build_json_output()       → produce structured JSON

***

## ✅ Current capabilities

*   Parses structured README headers
*   Extracts:
    *   title
    *   version
    *   description
    *   creators (name, email, ORCID)
    *   contributors
    *   keywords
    *   file names
*   Outputs consistent JSON structure

***

## ⚠️ Limitations (by design)

This is a **prototype**, so:

*   Assumes reasonably well-structured README files
*   Uses simple parsing (no NLP / LLM yet)
*   Not fully compliant with any formal standard (e.g. maDMP)
*   Some fields are only partially structured

👉 The focus is **simplicity and clarity**, not completeness.

***

## 🔮 Future ideas

*   Improve parsing of creators and contributors
*   Add JSON schema validation (e.g. Pydantic)
*   Support more flexible / messy input formats
*   Introduce LLM-based extraction for harder cases
*   Align output with formal maDMP standards

***

## 💡 Why this matters

This prototype shows how easily we can move from:

> ❌ Static text documents  
> → ✅ Structured, machine-actionable data

Even a simple transformation like this can:

*   reduce manual work
*   improve consistency
*   enable automation in research workflows

***

## 👤 Authors

Prototype created to explore structured data extraction for research data management at DeIC by

- **Jakob Bech Petersen**: _Coordinator Sensitive Data_, Data Management
- **Jonas Bak Phillipson**: _Software Developer_, Udvikling og international engagement 