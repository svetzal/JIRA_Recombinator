import os

from openai import OpenAI

import instructor

from augmented_issue import AugmentedIssue
from jira.jira_issue import JiraIssue


class LlmAugmentor:
    def __init__(self):
        self.client = instructor.from_openai(
            OpenAI(
                # base_url="http://localhost:11434/v1",
                # api_key="ollama",  # required, but unused
                api_key=os.environ["OPENAI_API_KEY"],
            ),
            mode=instructor.Mode.JSON,
        )

    def augment(self, issue: JiraIssue) -> AugmentedIssue:
        response = self.client.chat.completions.create(
            # model="llama3.1:8b",
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Augment the following Jira issue:\n{issue.model_dump_json(indent=2)}"
                    ),
                }
            ],
            response_model=AugmentedIssue,
        )
        return response
