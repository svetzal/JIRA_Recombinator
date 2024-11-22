from jira.jira_issue import JiraIssue


def map_dict_to_jira_issue(data: dict) -> JiraIssue:
    return JiraIssue(
        key=data['key'],
        summary=data['fields']['summary'],
        description=data['fields']['description']
    )