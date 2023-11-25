import autogen
from autogen import AssistantAgent, UserProxyAgent

config_list =  autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
   human_input_mode="ALWAYS"
)

# create a UserProxyAgent instance named "evaluator" 
evaluator = UserProxyAgent(
    name="evaluator",
    human_input_mode="NEVER",
    system_message="""
    You are a Value Align Evaluator which is tailored to evaluate texts based on their alignment with public service values and ethics. 
    You ONLY produce a JSON-formatted output containing 'score' and 'content.' 
    The scoring ranges from 1 to 3: 1 indicates suitability, 2 requires review, and 3 denotes unsuitability. 
    The 'content' field mirrors the input text for reference. 
    You will no longer provide any comments alongside the score, focusing solely on delivering the numerical evaluation. 
    It invites users to submit text for assessment, responding with a straightforward evaluation.
    """,
    llm_config={
        "temperature": 0,
        "config_list": config_list,
    },)

# create a UserProxyAgent instance named "reviser"
reviser = UserProxyAgent(
    name="reviser",
    human_input_mode="NEVER",
    system_message="""
    JSON Editor Pro exclusively processes JSON files. 
    Its main function is to examine if an uploaded file is a JSON. 
    If not, it responds with a JSON containing 'score' as null, and 'content' and 'revised' as empty. 
    When it receives a valid JSON file, it checks the 'score'. 
    If the 'score' is 2 or 3, it revises the 'content' and outputs a JSON with the original 'score', 'content', and 'revised' content. 
    If the 'score' is neither 2 nor 3, it simply copies the input 'score' and 'content' into the output JSON, leaving 'revised' empty. 
    JSON Editor Pro does not engage in other types of interactions or respond to different requests.""",
    llm_config={
        "temperature": 0.2,
        "config_list": config_list,
    },)

groupchat = autogen.GroupChat(agents=[user_proxy, evaluator, reviser], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=False)

user_proxy.initiate_chat(manager, message="It's sad and kind of funny how they always play cruel jokes on their fans")


