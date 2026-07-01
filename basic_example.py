from truvem import Truvem

BASE_URL = "https://truvem.onrender.com"
API_KEY = "YOUR_TRUVEM_KEY"

client = Truvem(api_key=API_KEY, base_url=BASE_URL)

def web_search(query: str) -> str:
    """Fake tool call — replace with your real tool."""
    return f"Search results for '{query}'"

# Your agent action
prompt = "What is Truvem?"
result = web_search(prompt)

# 2 lines to add cryptographic proof
response = client.log_action(
    agent_id="demo-agent",
    model="gpt-4o",
    authorized_by="user@company.com",
    prompt=prompt,
    result=result,
    scope=["web_search"]
)

print("\n✅ Action logged with cryptographic proof\n")
print("Action ID :", response["action_id"])
print("Proof Hash:", response["proof_hash"])

# Retrieve and display the proof
proof = client.get_proof(response["action_id"])
print("\n📋 Retrieved proof:")
print(f"  Agent    : {proof['agent_id']}")
print(f"  Model    : {proof['model']}")
print(f"  By       : {proof['authorized_by']}")
print(f"  Created  : {proof['created_at']}")
print(f"  Hash     : {proof['proof_hash']}")
