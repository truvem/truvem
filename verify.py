import hashlib
import sys
import requests

BASE_URL = "https://truvem.onrender.com"
API_KEY = "YOUR_TRUVEM_KEY"

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def verify(action_id: str):
    r = requests.get(
        f"{BASE_URL}/v1/action/proof/{action_id}",
        headers={"x-api-key": API_KEY}
    )
    if r.status_code != 200:
        print("❌ Unable to retrieve proof.")
        return

    proof = r.json()

    # Recalculate proof_hash from stored prompt_hash + result_hash
    recalculated = sha256(
        proof["prompt_hash"] + proof["result_hash"]
    )

    stored = proof["proof_hash"]

    print(f"\nAction ID      : {proof['id']}")
    print(f"Agent          : {proof['agent_id']}")
    print(f"Model          : {proof['model']}")
    print(f"Authorized by  : {proof['authorized_by']}")
    print(f"Created at     : {proof['created_at']}")
    print(f"\nStored hash    : {stored}")
    print(f"Recalculated   : {recalculated}")
    print()

    if recalculated == stored:
        print("✅ VALID — proof is intact and untampered.")
    else:
        print("❌ INVALID — proof has been tampered with.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify.py ACTION_ID")
        sys.exit(1)
    verify(sys.argv[1])
