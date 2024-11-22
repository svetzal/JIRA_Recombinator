import os

from jira.jira_gateway import JiraGateway
from llm_augmenter import LlmAugmentor

jira = JiraGateway("stacey@vetzal.com", os.environ['JIRA_API_KEY'])
augmentor = LlmAugmentor()

issues = jira.search_issues('project = SCRUM')

for issue in issues:
    augmented_issue = augmentor.augment(issue)
    print(augmented_issue)