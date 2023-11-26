import autogen
#from autogen.agentchat import UserProxyAgent
#from autogen.oai.completion import Completion

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
evaluator = autogen.UserProxyAgent(
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
reviser = autogen.UserProxyAgent(
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

# get the messages from the groupchat
print(groupchat.messages)

# https://github.com/openai/openai-cookbook/blob/feef1bf3982e15ad180e17732525ddbadaf2b670/examples/How_to_count_tokens_with_tiktoken.ipynb#L8

import token_count  

for model in [
    "gpt-3.5-turbo",
    "gpt-4",
    ]:
    print(model)
    # example token count from the function defined above
    print(f"{token_count.num_tokens_from_messages(groupchat.messages, model)} prompt tokens counted by num_tokens_from_messages().")
    # example token count from the OpenAI API
    # import openai
    # response = openai.ChatCompletion.create(
    #     model=model,
    #     messages=groupchat.messages,
    #     temperature=0,
    #     max_tokens=1,  # we're only counting input tokens here, so let's not waste tokens on the output
    # )
    # print(f'{response["usage"]["prompt_tokens"]} prompt tokens counted by the OpenAI API.')
    # print()



