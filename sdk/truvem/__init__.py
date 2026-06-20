import requests

class Client:
    def __init__(self, api_key: str = None, base_url: str = "https://truvem.onrender.com"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"x-api-key": api_key} if api_key else {}

    def register(self, email: str) -> dict:
        resp = requests.post(
            f"{self.base_url}/v1/register",
            json={"email": email}
        )
        data = resp.json()
        if "api_key" in data:
            self.api_key = data["api_key"]
            self.headers = {"x-api-key": self.api_key}
        return data

    def remember(self, agent_id: str, content: str) -> dict:
        resp = requests.post(
            f"{self.base_url}/v1/memory/write",
            json={"agent_id": agent_id, "content": content},
            headers=self.headers
        )
        return resp.json()

    def recall(self, agent_id: str) -> dict:
        resp = requests.post(
            f"{self.base_url}/v1/memory/read",
            json={"agent_id": agent_id},
            headers=self.headers
        )
        return resp.json()

Truvem = Client
