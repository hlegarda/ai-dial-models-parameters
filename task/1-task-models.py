from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

USER_QUESTION = "What LLMs can do?"
MODELS = [
    "gpt-4o",
    "claude-3-7-sonnet@20250219",
    "gemini-2.5-pro",
]

for deployment_name in MODELS:
    print(f"\n--- Model: {deployment_name} ---")
    client = DialClient(
        endpoint=DIAL_ENDPOINT,
        deployment_name=deployment_name,
    )
    conversation = Conversation()
    conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
    conversation.add_message(Message(Role.USER, USER_QUESTION))

    try:
        client.get_completion(
            messages=conversation.get_messages(),
            print_request=False,
            print_only_content=True,
        )
    except Exception as e:
        err = str(e)
        if "403" in err and "Access denied" in err:
            print("Access denied for this model. Your API key may not have permission for it.")
        else:
            print(f"Error: {e}")
