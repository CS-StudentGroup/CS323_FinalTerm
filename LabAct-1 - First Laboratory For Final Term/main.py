
from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:

    item_names = [
        "Burger",
        "Pizza",
        "Fries",
        "Coffee",
        "Pasta",
        "Milk Tea",
        "Sandwich",
        "Donut"
    ]

    num_orders = random.randint(5, 8)

    orders = []

    for i in range(num_orders):
        orders.append({
            "order_id": i + 1,
            "item": random.choice(item_names)
        })

    print("\nMASTER: Generated Orders")

    for order in orders:
        print(order)

    workers = size - 1

    if workers <= 0:
        print("Run with at least 2 processes.")
        exit()


    chunks = [[] for _ in range(workers)]

    for i, order in enumerate(orders):
        chunks[i % workers].append(order)

    for worker_rank in range(1, size):
        comm.send(chunks[worker_rank - 1], dest=worker_rank)


    completed_orders = []

    for worker_rank in range(1, size):
        results = comm.recv(source=worker_rank)
        completed_orders.extend(results)


    print("\nMASTER: Completed Orders")

    for result in completed_orders:
        print(result)

else:

    assigned_orders = comm.recv(source=0)

    processed = []

    for order in assigned_orders:

        print(
            f"Worker {rank} processing "
            f"Order {order['order_id']} ({order['item']})"
        )

        delay = random.uniform(1, 3)
        time.sleep(delay)

        completed = {
            "worker": rank,
            "order_id": order["order_id"],
            "item": order["item"],
            "status": "Completed",
            "time": round(delay, 2)
        }

        print(
            f"Worker {rank} completed "
            f"Order {order['order_id']}"
        )

        processed.append(completed)

    comm.send(processed, dest=0)