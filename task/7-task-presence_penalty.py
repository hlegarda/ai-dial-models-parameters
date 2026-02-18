from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

# Try `presence_penalty`: positive values encourage new topics; higher == more topic diversity.
# Range: -2.0 to 2.0, Default: 0.0.

USER_QUESTION = "What games have been made by Blizzard?"
DEPLOYMENT_NAME = "gpt-4o"
PRESENCE_PENALTY = -2.0 

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
    print_only_content=True,
    presence_penalty=PRESENCE_PENALTY,
)
