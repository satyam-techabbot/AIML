from typing import Annotated, List, Tuple, TypedDict
import operator

class PlanExecuteState(TypedDict):
    input: str # prompt
    plan: List[str] # list of steps
    past_steps: Annotated[List[Tuple], operator.add] # completed steps and its answer
    response: str # final o/p
    tone: str