import time
import random
from edge_node import send_vote, generate_vote


def run_step_1_duplication():
    print("\n--- STARTING STEP 1: DUPLICATION TEST ---")
    vote = generate_vote("Test")
    print(f"Targeting User: {vote['user_id']}")

    for i in range(3):
        print(f"Transmission Attempt {i + 1}...")
        send_vote(vote)

    print("\nStep 1 Complete.")
    print("Check Supabase: 'vote_queue' should have 3 rows, 'votes' should have 1.")


def run_step_2_continuous():
    print("\n--- STARTING STEP 2: CONTINUOUS FLOW ---")
    print("ACTION REQUIRED: Disable the Webhook in Supabase Dashboard now!")
    print("Press Ctrl+C to stop when you are ready to restore the service.")

    try:
        while True:
            vote = generate_vote("Test")
            send_vote(vote)
            wait_time = random.uniform(1, 3)
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print("\nStopping continuous flow. Now re-enable the Webhook to observe recovery.")


if __name__ == "__main__":
    print("Select Demo Phase:")
    print("1. Step 1: Duplicate/Idempotency Test")
    print("2. Step 2: Continuous Flow (Fault Simulation)")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_step_1_duplication()
    elif choice == "2":
        run_step_2_continuous()
    else:
        print("Invalid choice.")