from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_QUESTION = "Name a random Terran character from StarCraft 2."
DEPLOYMENT_NAME = "gpt-4o"
SEED = 42  # any integer
N_CHOICES = 5

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
    seed=SEED,
    n=N_CHOICES,
)
