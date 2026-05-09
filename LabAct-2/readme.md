REFLECTIONS

Member 1: Tion, James Dominic P.

Implementing this voting system provided a clear contrast between sequential and distributed execution. In a sequential program, a failure in the database would immediately crash the client. However, in our distributed setup, I observed Fault Isolation in action: when I intentionally disabled the worker (simulating a backend failure by toggling the Supabase Webhook), the edge_node.py continued to receive successful 200 OK responses. This highlighted the power of Temporal Decoupling, the system didn't stop, it simply buffered the data in the vote_queue. This experience solidified my understanding that availability and processing can be separated to create a more resilient architecture.

Member 2: Olaer, Kurt Andre L.

Our Supabase setup made the lab’s architecture feel real: edge nodes send votes over HTTP, vote-api enqueues them in vote_queue, and vote-worker processes them asynchronously. That separation showed me why distributed systems use buffers—ingestion can stay available even when processing lags. Sending duplicate votes highlighted idempotency: the final votes rows should stay consistent and not multiply when the same payload is delivered more than once. Temporarily disabling the webhook simulated a failed worker; the queue backed up while edges kept sending, and turning the worker back on drained pending work. Compared to a single-threaded program, debugging was harder because I had to correlate logs and table state, but I also saw clearer fault isolation and recovery behavior.

Member 3: [Name Here]

(Reflection Here)

Member 4: [Name Here]

(Reflection Here)

Member 5: [Name Here]

(Reflection Here)
