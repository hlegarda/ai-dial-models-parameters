import requests

from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

USER_QUESTION = "Is GTA 4 better than GTA 5?"
DEPLOYMENT_NAME = "gpt-4o"
TEMPERATURE = 1.4  # in range 0.0 to 2.0 (0.0 = deterministic, higher = more creative).

client = DialClient(
    endpoint=DIAL_ENDPOINT,
    deployment_name=DEPLOYMENT_NAME,
)
conversation = Conversation()
conversation.add_message(Message(Role.SYSTEM, DEFAULT_SYSTEM_PROMPT))
conversation.add_message(Message(Role.USER, USER_QUESTION))

try:
    client.get_completion(
        messages=conversation.get_messages(),
        print_request=False,
        print_only_content=True,
        temperature=TEMPERATURE,
    )
except requests.exceptions.ReadTimeout:
    print("Request timed out. High temperature can make the API slower; try again or use a lower value.")
except requests.exceptions.Timeout:
    print("Request timed out. The server took too long to respond; try again.")
