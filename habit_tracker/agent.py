from typing import Optional
from google.adk.agents.llm_agent import Agent
from google.genai import types
from google.adk.agents.callback_context import CallbackContext

from .sub_agents.calorie_tracker.agent import calorie_tracker
from .sub_agents.info_helper.agent import info_tracker
from .sub_agents.tracker_agent.agent import tracker_agent



def before_agent_callback(callback_context : CallbackContext) -> Optional[types.Content] :
    """
    Simple callback that logs when the agent is processing the request

    Args : 
        callback_context: Contains the state and context information
    
    Returns:
        None to continue with normal execution
    """

    state = callback_context.state

    # Set initial state values if not present

    # user information
    if "user_info" not in state:
        state["user_info"] = {
            "user_name" : "",
            "user_age" : "",
            "user_fitness_goal" : "",
            "user_diet_restrictions" : "",
            "user_diet_plan" : {}
        }
    
    # habits to track
    if "habits_to_track" not in state:
        state["habits_to_track"] = {}
    
    # reminders to track
    if "reminders_to_track" not in state:
        state["reminders_to_track"] = {}
    

    return None

root_agent = Agent(
    model='gemini-2.5-flash',
    name='habit_tracker',
    description='A helpful assistant to help the user maintain and track habits',
    instruction="""
        You are a helpful assistant with the main goal of improving the lifestyle of the user.
        you are available to use the following tools for the defined operations.

        <PRE-REQUSITE>
            1. Check if you know the {user_info.user_name} and their valid information under {user_info}
                1.a. If no transfer the control to sub_agent (info_tracker) and proceed to ask the relevant questions
            2. Check if you know the habits of the user under {habits_to_track}
                2.a. If empty transfer the control to the sub_agent (tracker_agent) and proceed to ask the relevant questions
        <PRE-REQUSITE>

        <AGENT ROUTING>
            1. Any inputs regarding CRUD operation on personal information should be routed to
                - info_tracker
            2. Any inputs regarding CRUD operation on reminders / habits should be routed to
                - tracker_agent
        </AGENT ROUTING>

        <ACTIONS>
            1. If the user asks for a cumulative report, show the complete values of {user_info}, {habits_to_track}, {reminders_to_track} all neatly formatted.
        </ACTIONS>

    """,
    sub_agents=[calorie_tracker, info_tracker, tracker_agent],
    before_agent_callback=before_agent_callback
)
