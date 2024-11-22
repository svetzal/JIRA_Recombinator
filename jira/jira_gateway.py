import os

import requests
from requests.auth import HTTPBasicAuth

from jira_issue_mapper import map_dict_to_jira_issue


class JiraGateway:
    def __init__(self, username, auth_token):
        self.auth = HTTPBasicAuth(username, auth_token)

    @property
    def headers(self):
        return {
            "Accept": "application/json"
        }

    @property
    def server(self):
        return "https://svetzal.atlassian.net"

    def get(self, path, params):
        return requests.request(
            "GET",
            f"{self.server}{path}",
            headers=self.headers,
            params=params,
            auth=self.auth
        ).json()

    def search_issues(self, query):
        response = self.get("/rest/api/3/search", {'jql': query})
        return [map_dict_to_jira_issue(issue_dict) for issue_dict in response['issues']]
