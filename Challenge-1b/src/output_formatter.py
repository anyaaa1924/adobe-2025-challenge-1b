import json
from datetime import datetime

def format_output(input_json, top_sections, refined_subsections):
    output = {
        "metadata": {
            "input_documents": input_json["document_dir"],
            "persona": input_json["persona"],
            "job_to_be_done": input_json["job"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for section in top_sections:
        output["extracted_sections"].append({
            "document": section["document"],
            "page_number": section["page_number"],
            "section_title": section["section_title"],
            "importance_rank": section["importance_rank"]
        })

    for sub in refined_subsections:
        output["subsection_analysis"].append({
            "document": sub["document"],
            "page_number": sub["page_number"],
            "refined_text": sub["refined_text"]
        })

    with open("challenge1b_output.json", "w") as f:
        json.dump(output, f, indent=4)

    print("✅ Output saved to challenge1b_output.json")
