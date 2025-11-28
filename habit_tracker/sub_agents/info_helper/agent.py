from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


def info_crud_updated(user_info : dict, tool_context : ToolContext) -> dict :
    """
    This method updates the state value of {user_info} in a single fashion
    """

    print("Updating user information _updated")

    tool_context.state["user_info"] = user_info

    return {
        "action" : "Add user_info",
        "user_info" : user_info,
        "message" : "Successfully added user information"
    }


def info_update(info_key:str, usr_inp:str, tool_context: ToolContext) -> dict:
    """
    Updates the user information, based on the keys provided
    """
    user_info = tool_context.state.get("user_info", {})

    if info_key not in user_info:
        return {
            "action" : "invalid",
            "user_info" : user_info,
            "message" : "Invalid operation, the provided key does not exist"
        }
    
    user_info[info_key] = usr_inp

    tool_context.state["user_info"] = user_info

    return {
        "action" : "Success",
        "user_info" : user_info,
        "message" : "Successfully updated the user information"
    }



def info_crud(usr_input :str, option: str, tool_context : ToolContext) -> dict :
    """
    This method logs the personal information of the user.
    """

    print("This is from the function call")
    
    user_info = tool_context.state.get("user_info", {})


    base_stats = ["user_name", "user_age", "user_weight", "user_fitness_goal", "user_diet_restrictions"]

    for i in base_stats:
        if option.lower() == i:
            user_info[i] = usr_input
    
    print(user_info.keys())

    tool_context.state["user_info"] = user_info

    
    return {
        "action" : "Add user information",
        "user_info" : tool_context.state.get("user_info"),
        "message" : "user information added"
    }




    

info_tracker = Agent(
    name="info_tracker",
    description="This agent is capable of maintaining the personal bio-data of the user",
    instruction="""
        You are a friendly information assistant, that manages the user information.

        <FUNCTION SIGNATURE TEMPLATE (info_crud_updated)>
            user_info = {
                "user_name" : "...",
                "user_age" : "...",
                "user_weight" : "...",
                "user_fitness_goal" : "...",
                "user_diet_restriction" : "..."
            }
        </FUNCTION SIGNATURE TEMPLATE (info_crud_updated)>
        
        
        <FUNCTION SIGNATURE KEYWORDS (info_update)>
            * Queries related to user age : user_age
            * Queries related to user name : user_name
            * Queries related to user weight : user_weight
            * Queries related to user diet restrictions : user_diet_restrictions
            * Queries related to user fitness goal : user_fitness_goal
        </FUNCTION SIGNATURE KEYWORDS (info_update)>
        
        <PRE-REQUSITE>
            1. Check if the {user_info} is valid.
                1.a. If no proceed to section <USER-INPUT>
            2. If the information on the user is available, Ask if they would like to make any modifications. 
                2.a. Based on the input, use the tool (info_crud) and perform the function call with the correct keywords from <FUNCTION SIGNATURE KEYWORDS>
        </PRE-REQUSITE>

        <USER-INPUT>
            1. Ask the user their name, age, weight, fitness goal, diet restrictions
                Once provided you will construct a valid JSON based on <FUNCTION SIGNATURE(info_crud_updated)>
                This valid JSON will then be passed to the tool (info_crud_updated)
                example : {
                    "user_name" : "surya",
                    "user_age" : "25",
                    "user_weight" : "85",
                    "user_fitness_goal" : "Lean Bulk",
                    "user_diet_restriction" : "No restrictions"
                }
        </USER-INPUT>

        <INFO-UPDATE>
            1. If the user wants to update any information, the following tool (info_update), with the function signature <FUNCTION SIGNATURE KEYWORDS (info_update)>
                example : info_update("<FUNCTION SIGNATURE KEYWORDS (info_update)>", user_input, tool_context)
        </INFO-UPDATE>


        <FINALLY>
            Once all the information is processed and the user is satisfied, please transfer the control back to the main agent (habit_tracker)
        </FINALLY>
""",
    tools=[info_crud_updated, info_update],
)