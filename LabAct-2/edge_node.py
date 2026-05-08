import uuid
import time
import random
import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_URL = os.getenv("SUPABASE_URL") + "/functions/v1/vote-api"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('SUPABASE_ANON_KEY')}"
}

def generate_vote(node_id):
    return {
        "user_id": str(uuid.uuid4()),
        "poll_id": "poll_1",
        "choice": random.choice(["A", "B", "C"]),
        "node_id": node_id,
        "timestamp": time.time()
    }

def send_vote(vote):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, json=vote, headers=HEADERS, timeout=5)

            if response.status_code in [200, 202]:
                print(f"Success: Vote sent (Attempt {attempt + 1})")
                return True
            else:
                print(f"Server returned error {response.status_code}: {response.text}")

        except Exception as e:
            print(f"Transmission failed on attempt {attempt + 1}: {e}")

        time.sleep(2 ** attempt)

    return False

def run_edge_node(node_id):
    print(f"Starting Edge Node: {node_id}...")
    while True:
        vote = generate_vote(node_id)
        send_vote(vote)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    MY_NODE_ID = "Student_Name_Node_1"
    run_edge_node(MY_NODE_ID)