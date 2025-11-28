from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext



def info_crud(usr_input :str, option: str, tool_context : ToolContext) -> dict :
    """
    This method logs the personal information of the user.
    """

    print("This is from the function call")
    
    user_info = tool_context.state.get("user_info", {})


    base_stats = ["user_name", "user_age", "user_fitness_goal", "user_diet_restrictions", "user_diet_plan"]

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

        <FUNCTION SIGNATURE KEYWORDS>
            * Queries related to user age : user_age
            * Queries related to user name : user_name
            * Queries related to user diet restrictions : user_diet_restrictions
            * Queries related to user fitness goal : user_fitness_goal
        </FUNCTION SIGNATURE KEYWORDS>
        
        <PRE-REQUSITE>
            1. Check if there is any available information on the user in the session state / tool_context
                1.a. If no proceed to section <USER-INPUT>
            2. If the information on the user is available, Ask if they would like to make any modifications. 
                2.a. Based on the input, use the tool (info_crud) and perform the function call with the correct keywords from <FUNCTION SIGNATURE KEYWORDS>
        </PRE-REQUSITE>

        <USER-INPUT>
            1. Ask the user their name.
                Once provided use the tool (info_crud) with the parameters (usr_input, "user_name", tool_context). example : ("surya", "user_name", tool_context)
            2. Ask the user their age.
                Once provided use the tool (info_crud) with the parameters (usr_input, "user_age", tool_context). example : ("20", "user_age", tool_context)
            3. Ask the user their fitness goal
                Once provided use the tool (info_crud) with the parameters (usr_input, "user_fitness_goal", tool_context). example : ("Atheletic", "user_fitness_goal", tool_context)
            4. Ask the user their diet restrictions
                Once provided use the tool (info_crud) with the parameters (usr_input, "user_diet_restrictions", tool_context). example : ("Allergic to shell fish", "user_diet_restrictions", tool_context)
        </USER-INPUT>

        <FINALLY>
            Once all the information is processed and the user is satisfied, please transfer the control back to the main agent (habit_tracker)
        </FINALLY>
""",
    tools=[info_crud],
)