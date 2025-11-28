from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from typing import Literal


def habit_insert(usr_inp:str, tool_context : ToolContext) -> dict :
     """
     Inserts a new habit to the state "habits_to_track"
     """

     habits_to_track = tool_context.state.get("habits_to_track", [])
     habits_to_track.append(usr_inp)

     tool_context.state["habits_to_track"] = habits_to_track

     return {
        "action" : "Added new habit",
        "habits_to_track" : habits_to_track,
        "message" : "Habit added"
    }

def reminder_insert(usr_input:str, tool_context: ToolContext) -> dict:
     """
     Insert a new reminder to the state "reminders_to_track"
     """

     reminders_to_track = tool_context.state.get("reminders_to_track", [])

     reminders_to_track.append(usr_input)

     tool_context.state["reminders_to_track"] = reminders_to_track

     return {
          "action" : "Add new reminder",
          "reminders_to_track" : reminders_to_track,
          "message" : "Reminder Added"
     }

tracker_agent = Agent(
    name="tracker_agent",
    description="The agent capable of tracking the user habits / reminders",
    instruction="""
        You are a friendly agent that helps the user in tracking their habits and reminders.

        <PRE-REQUSITE>
            1. Check if you have access to the user habits {habits_to_track}
                1.a. If no proceed to ask the user on what habits they would like to track
                1.b. Once the user provides the habits use the tool (habit_insert) to insert a new habit
            2. Check if you have access to the user reminder {reminders_to_track}
                2.a. This is optional (do not ask explicitly if they have a reminder)
        </PRE-REQUSITE>

        <USER INPUT ANALYSIS>
            1. On every input the user provides regarding a habit they would like to track, or a reminder they would like to add,
                you will determine whether the input will be classified under "Reminders" or "Habits"
                1.a. If the input is classified as a habit, use the tool (habit_insert)
                1.b. If the input is classified as a reminder, use the tool (reminder_insert)
        </USER INPUT ANALYSIS>

        <FINALLY>
            Once all the information is processed and the user is satisfied, please transfer the control back to the main agent (habit_tracker)
        </FINALLY>
    """,
    tools=[habit_insert, reminder_insert]
)