import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from model.state import PlanExecuteState

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

class Plan(BaseModel):
    """A list of steps to achieve an objective."""
    steps: List[str] = Field(description="Steps to follow, in order.")

planner_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert planner. Break the user's request into a concise, logical list of steps."),
    ("user", "{input}")
])
planner = planner_prompt | llm.with_structured_output(Plan)

def plan_node(state: PlanExecuteState):
    """Creates the initial plan."""
    plan = planner.invoke({"input": state["input"]})
    return {"plan": plan.steps}

def execute_node(state: PlanExecuteState):
    """Executes the FIRST step in the current plan."""
    plan = state["plan"]
    current_step = plan[0]
    tone = state.get("tone", "Normal")
    
    tone_instructions = {
        "Normal": "Be professional, clear, and factual.",
        "Funny": "Use puns, lighthearted jokes, and a playful tone.",
        "Sarcastic": "Be witty, cynical, and use heavy irony. Act like you're slightly annoyed to be helping."
    }

    system_msg = f"You are an assistant who speaks in a {tone} tone. {tone_instructions[tone]}"
    user_msg = f"Objective: {state['input']}\nTask: {current_step}\nContext: {state['past_steps']}"
    
    response = llm.invoke([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return {
        "past_steps": [(current_step, response.content)],
        "plan": plan[1:]
    }

def replan_node(state: PlanExecuteState):
    """Decides if the task is done or if the plan needs updating."""
    if not state["plan"]:
        return {"response": state["past_steps"][-1][1]}
    return {
        "plan": state["plan"]
    }