# Approach Explanation

## Overview

This solution extracts and prioritizes relevant document sections tailored to a specific persona and job-to-be-done using lightweight NLP techniques. The approach is designed to be generic, CPU-efficient, and effective across multiple domains.

## 1. Document Parsing

We use `pdfplumber` to extract text by page, maintaining page numbers and structural markers (headings, bullet points, section titles). Each document is converted into a list of sections containing: page number, section title, and text.

## 2. Persona & Job Embedding

We use a SentenceTransformer model (quantized `all-MiniLM-L6-v2`) to encode the persona description and job-to-be-done into a vector. This forms our "intent vector" representing what content is relevant.

## 3. Section Relevance Ranking

Each document section is embedded and scored using cosine similarity with the intent vector. The top N sections across documents are ranked by relevance and returned.

## 4. Sub-section Refinement

Each top section is further broken down into finer sub-sections (based on newline separation and headings). These sub-chunks are re-ranked against the intent vector, and top refined snippets are selected.

## 5. Output Format

We generate a structured JSON containing metadata, selected sections (with page numbers and importance rank), and refined sub-sections with improved granularity.

## Constraints Handling

- CPU-only execution
- Total model size < 1GB
- Execution within 60 seconds for 3–5 PDFs

This architecture ensures modularity, robustness, and generalizability across diverse personas, documents, and tasks.
