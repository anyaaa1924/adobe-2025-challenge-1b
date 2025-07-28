import json
import os
from datetime import datetime
from src.document_processor import extract_sections_from_pdfs
from src.ranker import rank_sections
from src.subsection_refiner import refine_subsections

def save_output(input_json, top_sections, refined_sections, output_file="challenge1b_output.json"):
    output_data = {
        "metadata": {
            "persona": input_json["persona"],
            "job_to_be_done": input_json["job"],
            "input_documents": list(set(
                section["document"] for section in top_sections if "document" in section
            )),
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [
            {
                "document": section.get("document", "unknown.pdf"),
                "page_number": section.get("page", None),
                "section_title": section.get("title", "Unknown Section"),
                "importance_rank": idx + 1
            }
            for idx, section in enumerate(top_sections)
        ],
        "subsection_analysis": [
            {
                "document": refined.get("document", "unknown.pdf"),
                "page_number": refined.get("page", None),
                "refined_text": refined.get("text", "")
            }
            for refined in refined_sections
        ]
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Output saved to {output_file}")

def main():
    # Load user config
    with open("sample_input.json", "r", encoding="utf-8") as f:
        input_json = json.load(f)

    document_dir = input_json.get("document_dir", "sample_docs")
    if not os.path.exists(document_dir):
        raise FileNotFoundError(f"❌ Directory '{document_dir}' not found.")

    # Step 1: Extract content from PDFs
    print("🔍 Extracting sections from PDFs...")
    sections = extract_sections_from_pdfs(document_dir)
    print(f"📄 Total sections extracted: {len(sections)}")

    # Step 2: Rank the sections
    print("📊 Ranking sections by relevance...")
    top_sections = rank_sections(sections, input_json["persona"], input_json["job"])

    # Step 3: Refine the top sections
    print("🔬 Refining sub-sections for deeper insight...")
    refined = refine_subsections(top_sections, input_json["persona"], input_json["job"])

    # Step 4: Preview & Save
    print("\n✅ Top relevant refined sections:\n")
    for i, r in enumerate(refined, 1):
        print(f"🔹 Section {i}: {r.get('section_title', 'Unknown Title')}")
        print(f"{r.get('text', '')[:500]}...\n")

    save_output(input_json, top_sections, refined)

if __name__ == "__main__":
    main()
