from task.app.client import DialClient
from task.app.main import DIAL_ENDPOINT, DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role

# positive values reduce repetition; higher == less repetitive text.
# Range: -2.0 to 2.0, Default: 0.0. (With -2.0 the request can run very long and output may be repetitive.)

USER_QUESTION = "What's the best drummer in the world?"
DEPLOYMENT_NAME = "gpt-4o"
FREQUENCY_PENALTY = -1.9

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
    frequency_penalty=FREQUENCY_PENALTY,
)
