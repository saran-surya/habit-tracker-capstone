from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def diet_update(dietPlan : dict, tool_context : ToolContext) -> dict :
    """
    Update the diet plan of the user,
    Args : 
        a completely valid json
    """

    user_info = tool_context.state.get("user_info", {})

    user_info["user_diet_plan"] = dietPlan

    tool_context.state["user_info"] = user_info

    return {
        "action" : "Added meal plan",
        "user_diet_plan" : dietPlan,
        "message" : "Successfully added meal plan"
    }


calorie_tracker = Agent(
    name="calorie_tracker",
    description="This agent is capable of suggesting diet plans to users based on their goal",
    instruction="""
        You are a helpful agent that can help with carefully curating the meal plan for the users
        based on their dietary restrictions and help them achieve their {user_info.fitness_goal} by tracking their regular meal inputs
        and adjusting them to help them maintain the goal, Please do not be extreme with the user, but curate their meals in a gentle manner
        and help them in a more polite way.

        <PRE-REQUSITE>
            * Check if the context variable {user_info} is populated
                - If valid continue
                - Else 
                    -> Turn control to (info_helper)
        </PRE-REQUSITE>

        <USER-INFORMATION>
            {user_info}
        </USER-INFORMATION>

        <INSTRUCTIONS>
            * When the user asks for a meal prep,
                - Carefully curate the meal considering both {user_info.user_diet_restrictions} and {user_info.user_fitness_goal}, Each meal should be properly propotioned to match the {user_info.fitness_goal} including protein, fiber, and healthy fats.
                  you will have to determine whether the meal is going to be protein rich, based on the inputs of the fitness goal {user_info.user_fitness_goal}
                - The meal plan should be carefully curated for all seven days in a valid JSON
                    * the json should be represented in the following template
                        - {
                            "MON" : {
                                "breakfast" : {
                                    "Macros" : "...",
                                    "Micros" : "...",
                                    "food" : "..."
                                },
                                "lunch" : {
                                    "Macros" : "...",
                                    "Micros" : "...",
                                    "food" : "..."
                                },
                                "dinner" : {
                                    "Macros" : "...",
                                    "Micros" : "...",
                                    "food" : "..."
                                },
                            }
                        }
                This JSON should be then processed with the tool (diet_update)
        </INSTRUCTIONS>

        <FINALLY>
            Once all the information is processed and the user is satisfied, please transfer the control back to the main agent (habit_tracker)
        </FINALLY>
       
    """,

    tools=[diet_update]
)