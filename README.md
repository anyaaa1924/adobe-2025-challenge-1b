Challenge 1b – Persona-Based Multi-Collection PDF Analyzer

This project is a submission for **Challenge 1b** of the **Adobe India Hackathon 2025**. It presents an advanced solution that extracts and ranks relevant content from multiple PDF document collections using persona-based context. The solution is designed to run **offline**, within resource limits, and produces structured JSON output conforming to expected schema.

---

 Problem Statement

Given a set of collections, each containing multiple PDFs, and an input JSON specifying a **persona** and a **job-to-be-done**, the solution must:

- Parse all PDFs in the collection
- Extract relevant content sections
- Rank sections based on relevance to the persona and task
- Refine these into subsections
- Output a structured JSON result with metadata, section ranks, and extracted text

---

## 🧠 Approach

The pipeline follows this structure:

1. **Input Parsing**  
   - Load persona and task from `challenge1b_input.json`.

2. **PDF Processing**  
   - Extract text per page using `PyMuPDF`.
   - Identify content-rich sections for ranking.

3. **Relevance Ranking**  
   - Use custom scoring logic (offline) to match sections against the persona-task context.
   - No internet or external APIs/models are used at runtime.

4. **Refined Subsection Generation**  
   - The most relevant pages are truncated or chunked to extract meaningful insights.
   - Summarized text is added to the final output.

5. **Output Generation**  
   - A JSON file `challenge1b_output.json` is created with:
     - Metadata
     - Ranked sections
     - Refined text excerpts

---


## 🧪 Sample Input Format

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_002",
    "test_case_name": "travel_planning_case"
  },
  "documents": [
    { "filename": "doc1.pdf", "title": "Guide to South France" },
    { "filename": "doc2.pdf", "title": "Local Transport Options" }
  ],
  "persona": {
    "role": "Travel Planner"
  },
  "job_to_be_done": {
    "task": "Plan a 4-day trip for 10 college friends to South of France"
  }
}


---

✅ Output JSON Format

{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a 4-day trip...",
    "timestamp": "2025-07-28T12:34:56.789Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "section_title": "Top Attractions in Nice",
      "importance_rank": 1,
      "page_number": 2
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "refined_text": "Nice is famous for...",
      "page_number": 2
    }
  ]
}


---

⚙️ How to Run

# Install dependencies
pip install -r requirements.txt

# Run analysis
python main.py

Dockerfile given


