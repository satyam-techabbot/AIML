| Signal                        | Weight |
| ----------------------------- | ------ |
| Summary semantic relevance    | 40%    |
| Skills relevance              | 40%    |
| Title relevance               | 15%    |
| Negative Penalities           | 5%     |


updated:
| Signal                     | Weight |
| -------------------------- | ------ |
| Summary semantic relevance | 55%    |
| Skills relevance           | 40%    |
| Negative penalties         | 5%     |


You are an AI job relevance evaluator.

Evaluate how relevant the Upwork job is for the candidate.

Candidate Profile:
Skills: Figma, React

Upwork Job:
Title: Senior UI/UX designer for Modern Webflow website

Summary:
We are looking for a website designer to redesign our current WordPress site into a modern website using Webflow.

Website examples are as follows:
https://www.louxibiza.com/
https://www.am-charter.com/

If you have professional knowledge of Webflow and website design, we would like to discuss this.

Skills:
Webflow, WordPress, Web Design, Responsive Design, Figma, UX & UI Design

Scoring Rules:
- Summary relevance = 55%
- Skills relevance = 40%
- Negative penalties = 5%

Return STRICT JSON:
{
  "skills_score": 0-100,
  "summary_score": 0-100,
  "penality_score": 0-100,
  "final_score": 0-100,
  "reason": "short explanation"
}














Improvement ideas:
- manage missing skills
- Calculate the importance weightage of skills in the skills of upwork jd according to the summary of jd of upwork
- define penality calculation on missing skills
- redefine the weightage of negative penality percentage in total scoring

If we have the importance weightage of skills in the skills of upwork jd according to the summary of jd of upwork, we can easily detect what the candidate lacks from getting relevant to the job. For example, if candidate has skills like figma and react but the jd skills has Webflow, WordPress, Web Design, Responsive Design, Figma, UX & UI Design and jd summary is saying to create a website so here the most important skill is wordpress as it is mainly used to create website while the candidate lacks the main skill. So, we will deduct the required amount from final score as in the name of penality_score