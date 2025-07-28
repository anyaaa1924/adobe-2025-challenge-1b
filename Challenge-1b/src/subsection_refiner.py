def refine_subsections(sections, persona, job):
    refined = []
    for section in sections:
        # Simulated refinement — just truncating for now
        refined_text = section["text"][:300].strip().replace("\n", " ")
        refined.append({
            "document": section["document"],
            "page": section["page"],
            "text": refined_text,
            "section_title": section.get("title", "Unknown Section")
        })
    return refined
