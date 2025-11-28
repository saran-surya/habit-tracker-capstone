from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def user_workout_update(usr_workout : dict, tool_context : ToolContext) -> dict:
    """
    Updates the user workouts under the user_info
    """

    user_info = tool_context.state.get("user_info", {})
    user_info["user_workout_plan"] = usr_workout

    tool_context.state["user_info"] = user_info

    return {
        "action" : "Added workouts for user",
        "user_workout_plan" : user_info["user_workout_plan"],
        "message" : "Successfully added user workouts"
    }

def user_injury_update(usr_inp:str, tool_context : ToolContext) -> dict:
    """
    Updates the user injuries under the user_info.
    """

    user_info = tool_context.state.get("user_info", {})
    user_info["user_injuries"] = usr_inp

    tool_context.state["user_info"] = user_info

    return {
        "action" : "Added user injuries",
        "user_injuries" : user_info["user_injuries"],
        "message" : "Added user injuries"
    }
    

gym_tracker = Agent(
    name = "gym_tracker",
    description = "This agent is capable of guiding the user with gym workouts, based on their fitness goals",
    instruction = """
        You are a friendly agent that suggests the user with workout schedule based on their fitness goal

        <FUNCTION SIGNATURE TEMPLATE (user_workout_update)>
            user_info = {
                "user_name" : "...",
                "user_age" : "...",
                "user_weight" : "...",
                "user_fitness_goal" : "...",
                "user_diet_restriction" : "...",
                "user_workout_plan" : "..."
            }
        </FUNCTION SIGNATURE TEMPLATE (user_workout_update)>

        <PRE-REQUSITE>
            1. Check if you have a valid {user_info}, 
                If no transfer the control to (info_tracker) agent
            2. Ask the user for their Injuries, 
                2.a. If the user has injuries, Proceed to add them using the tool (user_injury_update) 
        </PRE-REQUSITE>

        <USER-INPUT>
            1. when the user asks for a workout plan, check if a workout plan already exists under {user_info.user_workout_plan}
                1.a. If exists a user plan, ask the user if they would like to tweak the plan, and make the modifications as needed.
            
            2. when the user asks for a workout plan, add the workouts in the following manner.
                {
                    "Monday" : {
                        "Workout" : "..."
                    },
                    "Tuesday" : {
                        "Workout" : "..."
                    },
                    "Wednesday" : {
                        "Workout" : "..."
                    },
                    "Thursday" : {
                        "Workout" : "..."
                    },
                    "Friday" : {
                        "Workout" : "..."
                    }
                }
                After the valid JSON is formed, then call the tool (user_workout_update)
        </USER-INPUT>

        Please be polite to the user, and allow tweaks to the workouts as necessary
    """,

    tools = [user_injury_update, user_workout_update]
)