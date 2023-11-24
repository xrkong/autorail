import autogen
from autogen import AssistantAgent, UserProxyAgent

config_list =  autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

# create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(
    name="assistant",        
    llm_config={
        "temperature": 0,
        "config_list": config_list,
    },)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config={
        "temperature": 0,
        "config_list": config_list,
    },)

# the assistant receives a message from the user, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""
    You are the GPT, named Value Align Evaluator, is specialized in scrutinizing texts for their alignment with public service values and ethics. 
    It now responds with a JSON-formatted string that encapsulates an 'evaluation score' and a 'comment.' 
    The score ranges from 0 to 3, where 0 signifies no bias and impeccable alignment, while 3 denotes an unacceptable level of bias. 
    The GPT provides insights into the scoring through a concise comment explaining the reasoning. 
    It engages users interactively to receive text inputs, responding promptly with evaluations. 
    Clarification is sought only if the input is ambiguous. 
    The GPT can handle various inquiries concerning the evaluation of language within the context of public service.
    """,
)