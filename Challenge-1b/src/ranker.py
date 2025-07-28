from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

def rank_sections(sections, persona, job):
    query = f"{persona}. {job}"
    query_emb = model.encode(query, convert_to_tensor=True)

    scored_sections = []
    for section in sections:
        section_emb = model.encode(section["text"], convert_to_tensor=True)
        score = util.cos_sim(query_emb, section_emb).item()
        section["score"] = score
        scored_sections.append(section)

    # Return top 3 by relevance
    top_sections = sorted(scored_sections, key=lambda x: x["score"], reverse=True)[:3]
    return top_sections
