from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)

BANNED_WORDS = ["hack", "illegal", "exploit"]

def validate_input(user_input: str):
    for word in BANNED_WORDS:
        if word in user_input.lower():
            raise ValueError("Unsafe input detected")
    return user_input

class ResponseSchema(BaseModel):
    answer: str = Field(...)
    safe: bool = Field(...)

parser = PydanticOutputParser(pydantic_object=ResponseSchema)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a safe assistant.

Rules:
- Do NOT answer harmful or illegal questions
- If unsafe, respond with:
  {{"answer": "I cannot help with that.", "safe": false}}
- Always respond in JSON format:
  {{"answer": "...", "safe": true/false}}
"""),
    ("human", "{input}")
])

chain = prompt | llm | parser

def run_chat():
    print("Guardrails Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        try:
            validated = validate_input(user_input)

            result = chain.invoke({"input": validated})

            if not result.safe:
                print("Bot: Blocked unsafe response\n")
            else:
                print(f"Bot: {result.answer}\n")

        except Exception as e:
            print(f"Bot: {str(e)}\n")

if __name__ == "__main__":
    run_chat()