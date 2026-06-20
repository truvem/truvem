import requests

class Client:
    def __init__(self, api_key: str, base_url: str = "https://truvem-production.up.railway.app"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def remember(self, agent_id: str, content: str) -> dict:
        resp = requests.post(
            f"{self.base_url}/v1/memory/write",
            json={"agent_id": agent_id, "content": content},
