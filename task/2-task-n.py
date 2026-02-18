from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_QUESTION = "What's the best faction in StarCraft 2?"
DEPLOYMENT_NAME = "gpt-4o"
N_CHOICES = 3  # n in range 1–5: number of alternative responses to generate

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
    print_only_content=False,  # show full response so you see all choices
    n=N_CHOICES,
)
