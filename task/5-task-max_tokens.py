from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_QUESTION = "Give me a mac and cheese recipe."
DEPLOYMENT_NAME = "gpt-4o"
MAX_TOKENS = 10

client = DialClient(
    endpoint=DIAL_ENDPOINT,
    deployment_name=DEPLOYMENT_NAME,
)
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

client.get_completion(
    messages=conversation.get_messages(),
    print_request=False,
    print_only_content=False,
    max_tokens=MAX_TOKENS,
)
