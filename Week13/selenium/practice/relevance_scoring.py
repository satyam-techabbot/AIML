import json
from groq import Groq

client = Groq(
    api_key=""
)

candidate_skills = [
    "Figma",
    "React"
]

job_title = """
Senior UI/UX designer for Modern Webflow website
"""

job_summary = """
We are looking for a website designer to redesign our current WordPress site into a modern website using Webflow.

Website examples are as follows:
https://www.louxibiza.com/
https://www.am-charter.com/

If you have professional knowledge of Webflow and website design, we would like to discuss this.
"""

job_skills = [
    "Webflow",
    "WordPress",
    "Web Design",
    "Responsive Design",
    "Figma",
    "UX & UI Design"
]

prompt = f"""
You are an AI job relevance analyzer.

Your task is to analyze how relevant an Upwork job is for a candidate based ONLY on:
- candidate skills
- job summary
- job required skills

IMPORTANT RULES:

- Do NOT hallucinate matches
- A skill is matched ONLY if the candidate explicitly has that skill or a very closely related equivalent
- Do NOT assume candidate knows technologies not listed
- Do NOT calculate weighted final scores
- Do NOT perform arithmetic
- Return STRICT JSON only
- Do not include markdown
- Do not include explanations outside JSON
- Do not penalize unrelated candidate skills

Focus heavily on:
- semantic relevance
- important job skills
- missing critical skills

SCORING RULES:

- summary_relevance_score:
  How relevant the candidate skills are to the actual work described in the summary

- skills_relevance_score:
  How well the candidate skills match the listed job skills

- penalty_recommendation:
  Recommended penalty based ONLY on missing important skills

Penalty guidelines:
- missing critical/core implementation skill → high penalty
- missing secondary/helper skill → small penalty
- no important missing skills → low or zero penalty

CANDIDATE SKILLS:
{json.dumps(candidate_skills)}

UPWORK JOB TITLE:
{job_title}

UPWORK JOB SUMMARY:
{job_summary}

UPWORK JOB SKILLS:
{json.dumps(job_skills)}

Return STRICT JSON in this exact format:

{{
  "summary_relevance_score": 0-10,
  "skills_relevance_score": 0-10,
  "penalty_recommendation": 0-10,
  "important_job_skills": [
    {{
      "skill": "string",
      "importance": 0-10,
      "matched": true
    }}
  ],
  "matched_skills": ["string"],
  "missing_important_skills": ["string"],
  "reason": "short explanation"
}}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0,
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

content = response.choices[0].message.content

data = json.loads(content)

print(json.dumps(data, indent=2))

# deterministic backend scoring
final_score = (
    data["summary_relevance_score"] * 0.55
    + data["skills_relevance_score"] * 0.40
) - (
    data["penalty_recommendation"] * 0.05
)

final_score = max(0, min(10, round(final_score, 2)))

print("\nFinal Score:", final_score)