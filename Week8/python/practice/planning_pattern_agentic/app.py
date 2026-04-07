import streamlit as st
from langgraph.graph import StateGraph, START, END
from model.state import PlanExecuteState
from graph.nodes import plan_node, execute_node, replan_node
from fpdf import FPDF

def should_continue(state: PlanExecuteState):
    if state.get("response"):
        return END
    return "execute"

workflow = StateGraph(PlanExecuteState)
workflow.add_node("planner", plan_node)
workflow.add_node("execute", execute_node)
workflow.add_node("replan", replan_node)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "execute")
workflow.add_edge("execute", "replan")
workflow.add_conditional_edges("replan", should_continue, {"execute": "execute", END: END})

app = workflow.compile()

st.title("Planning Agent")

selected_tone = st.sidebar.selectbox(
    "Choose Agent Personality:",
    ["Normal", "Funny", "Sarcastic"],
    index=0 
)

query = st.text_input("How can I help you?", "Research and summarize the impact of AI on the 2026 job market in 3 distinct paragraphs.")

if st.button("Start Planning & Execution"):
    with st.spinner("Executing plan..."):
        config = {
            "input": query,
            "plan": [],
            "past_steps": [],
            "response": "",
            "tone": selected_tone
        }
        print(config)
        final_state = app.invoke(config)
        
        st.subheader("Final Result")
        st.write(final_state["response"])
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=final_state["response"].encode('latin-1', 'ignore').decode('latin-1'))
        st.download_button("Download PDF", pdf.output(dest='S').encode('latin-1'), "plan_output.pdf")

        with st.expander("Show Plan History"):
            for step, result in final_state["past_steps"]:
                st.info(f"**Step:** {step}")
                st.write(result)