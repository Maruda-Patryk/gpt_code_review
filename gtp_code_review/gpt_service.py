import os
import openai
from .git_service import GitService


class GptService:
    def __init__(self, gpt_model="gpt-3.5-turbo", token=os.getenv('GPT_KEY')):
        self.openai = openai
        self.openai.api_key = token
        self.gpt_model = gpt_model
        self.git_service = GitService(main_branch='main')

    def send_message(self):
        return openai.ChatCompletion.create(model=self.gpt_model,messages=[{"role": "user", "content": self.git_service.preper_message_for_chat()}])
