import streamlit as st
from typing import Annotated, List, TypedDict
from fpdf import FPDF
import os, logging, re
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

@tool
def count_words(text: str) -> int:
    """Accurately counts the number of words in a string of text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    iterations: int
    max_iterations: int

def generation_node(state: AgentState):
    """Generates content while strictly adhering to the original user prompt."""
    
    original_query = state["messages"][0].content
    last_message = state["messages"][-1].content
    
    if state["iterations"] == 0:
        system_instruction = f"User Goal: {original_query}\n\nTask: Provide the initial response."
    else:
        system_instruction = f"""
        ORIGINAL USER GOAL: {original_query}
        
        YOUR PREVIOUS ATTEMPT & FEEDBACK:
        {last_message}
        
        TASK: Improve the output based on the feedback. 
        CRITICAL: You MUST still respect the original constraints (e.g., word count, tone, format) 
        set in the ORIGINAL USER GOAL. If the feedback asks for more depth but the user 
        asked for a short summary, find a way to be concise yet deep.
        """
    
    response = llm.invoke([HumanMessage(content=system_instruction)])
    return {
        "messages": [response],
        "iterations": state["iterations"] + 1
    }

def reflection_node(state: AgentState):
    """Critiques the last AI message, reminding it of the original constraints."""
    original_query = state["messages"][0].content
    last_ai_msg = state["messages"][-1].content
    
    actual_count = count_words.run(last_ai_msg)

    reflection_prompt = f"""
    Original User Requirement: {original_query}
    Current Draft: {last_ai_msg}
    
    ACTUAL STATS:
    - Current Word Count: {actual_count}

    INSTRUCTIONS:
    1. If the draft is accurate and follows all constraints (like word count), 
       reply ONLY with the word 'FINISH'.
    2. If not, provide clear instructions to fix it.
    """
    feedback = llm.invoke([HumanMessage(content=reflection_prompt)])
    return {"messages": [HumanMessage(content=feedback.content)]}

def should_continue(state: AgentState):
    last_message = state["messages"][-1].content.upper()
    
    if "FINISH" in last_message:
        return END
    
    if state["iterations"] >= state["max_iterations"]:
        return END
    
    return "generate"

workflow = StateGraph(AgentState)
workflow.add_node("generate", generation_node)
workflow.add_node("reflect", reflection_node)

workflow.add_edge(START, "generate")
workflow.add_edge("generate", "reflect")
workflow.add_conditional_edges(
    "reflect", 
    should_continue, 
    {
        "generate": "generate", 
        END: END
    }
)

app = workflow.compile()

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    return pdf.output(dest='S').encode('latin-1')

st.set_page_config (
    page_title="Agentic Reflection AI",
    layout="centered"
)

st.title("Agentic Reflection Workflow")

query = st.text_input("What can I generate for you?", placeholder="e.g. Write a technical essay on Quantum Computing.")
max_iters = st.slider("Max Reflection Rounds", 1, 5, 3)

if st.button("Generate Accurate Output"):
    if query:
        with st.spinner("Agent is thinking and reflecting..."):
            inputs = {
                "messages": [HumanMessage(content=query)],
                "iterations": 0,
                "max_iterations": max_iters
            }
            
            final_state = app.invoke(inputs)
            
            final_content = ""
            for msg in reversed(final_state["messages"]):
                if isinstance(msg, AIMessage):
                    final_content = msg.content
                    break
            
            st.markdown("### Final Result")
            st.write(final_content)
            
            # PDF Download
            pdf_data = create_pdf(final_content)
            st.download_button("Download PDF", pdf_data, "output.pdf", "application/pdf")
            
            with st.expander("View Internal Reflection Process"):
                for msg in final_state["messages"]:
                    type_label = "🤖 AI" if isinstance(msg, AIMessage) else "👤 Instruction/Feedback"
                    st.markdown(f"**{type_label}:** {msg.content}")