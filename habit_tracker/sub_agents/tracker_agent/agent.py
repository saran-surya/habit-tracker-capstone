from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def habit_insert(usr_inp:str, tool_context : ToolContext) -> dict :
     """
     Inserts a new habit to the state "habits_to_track"
     """

     habits_to_track = tool_context.state.get("habits_to_track", {})

     habits_to_track[usr_inp] = {
          "habit_name" : usr_inp,
          "habit_completion_days" : 0
     }

     tool_context.state["habits_to_track"] = habits_to_track

     return {
        "action" : "Added new habit",
        "habits_to_track" : habits_to_track,
        "message" : "Habit added"
    }

def habit_update(habit_key:str, tool_context: ToolContext) -> dict :
    """
    Updates the habit completion days, if the habit is not present, the habit is added to the context, 
    And the habit_completion_day is updated to +1
    """
    habits_to_track = tool_context.state.get("habits_to_track", {})

    if habit_key not in habits_to_track:
        habits_to_track = habit_insert(habit_key, tool_context)["habits_to_track"]
    
    habits_to_track[habit_key]["habit_completion_days"] += 1

    tool_context.state["habits_to_track"] = habits_to_track

    return {
         "action" : "Updated habit completion days",
         "habits_to_track" : habits_to_track,
         "message" : "Successfully added a day to completion of habit"
    }



def reminder_insert(usr_input:str, tool_context: ToolContext) -> dict:
     """
     Insert a new reminder to the state "reminders_to_track"
     """

     reminders_to_track = tool_context.state.get("reminders_to_track", {})

     reminders_to_track[usr_input] = {
          "reminder_name" : usr_input,
          "completion" : False
     }

     tool_context.state["reminders_to_track"] = reminders_to_track

     return {
          "action" : "Add new reminder",
          "reminders_to_track" : reminders_to_track,
          "message" : "Reminder Added"
     }

def reminder_update(reminder_key: str, tool_context: ToolContext) -> dict:
    """
    Update the reminders to complete state, If the reminder does not exist, add them and change the state to comeplted
    """
    reminders_to_track = tool_context.state.get("reminders_to_track", {})

    if reminder_key not in reminders_to_track:
        reminders_to_track = reminder_insert(reminder_key, tool_context)["reminders_to_track"]
    
    reminders_to_track[reminder_key]["completion"] = True

    tool_context.state["reminders_to_track"] = reminders_to_track

    return {
        "action" : "Updated reminder",
        "reminders_to_track" : reminders_to_track,
        "message" : "Successfully updated the reminder"
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
            
            2. When the user states they have completed a habit today, you will use the following tool (habit_update)
            3. When the user states they have completed a reminder today, you will use the follwoing tool (reminder_update)
        </USER INPUT ANALYSIS>

        <FINALLY>
            Once all the information is processed and the user is satisfied, please transfer the control back to the main agent (habit_tracker)
        </FINALLY>
    """,
    tools=[habit_insert, habit_update, reminder_insert, reminder_update]
)