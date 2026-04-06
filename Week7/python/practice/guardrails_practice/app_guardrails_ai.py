from guardrails import Guard
from pydantic import BaseModel, Field
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq (
    api_key=api_key
)

class ResponseSchema(BaseModel):
    answer: str = Field(description="Final answer to the user")
    safe: bool = Field(description="Whether the response is safe")

guard = Guard.for_pydantic(output_class=ResponseSchema)
prompt = """
You are a helpful and safe assistant.

Rules:
- Only block harmful or illegal questions (e.g., hacking, exploits, illegal content)
- If the input is unsafe, respond with:
  {"answer": "I cannot help with that.", "safe": false}
- Otherwise respond normally with:
  {"answer": "...", "safe": true}

User input:
${input}
"""

BANNED_WORDS = ["hack", "illegal", "exploit"]

def validate_input(user_input: str):
    for word in BANNED_WORDS:
        if word in user_input.lower():
            raise ValueError("Unsafe input detected")
    return user_input

def call_llm(*, prompt=None, messages=None, **kwargs):
    if messages is not None:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0
        )
    else:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

    return response.choices[0].message.content

def run_chat():
    print("Guardrails AI Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        try:
            validated = validate_input(user_input)

            formatted_prompt = prompt.replace("${input}", validated)
            result = guard(
                llm_api=call_llm,
                messages=[
                    {
                        "role": "user",
                        "content": formatted_prompt
                    }
                ]
            )

            validated_output = result.validated_output

            if not validated_output['safe']:
                print("Bot: Blocked unsafe response\n")
            else:
                print(f"Bot: {validated_output['answer']}\n")

        except Exception as e:
            print(f"Bot: {str(e)}\n")


if __name__ == "__main__":
    run_chat()