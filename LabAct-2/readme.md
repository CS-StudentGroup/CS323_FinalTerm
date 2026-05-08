REFLECTIONS

Member 1: Tion, James Dominic P.

Implementing this voting system provided a clear contrast between sequential and distributed execution. In a sequential program, a failure in the database would immediately crash the client. However, in our distributed setup, I observed Fault Isolation in action: when I intentionally disabled the worker (simulating a backend failure by toggling the Supabase Webhook), the edge_node.py continued to receive successful 200 OK responses. This highlighted the power of Temporal Decoupling, the system didn't stop, it simply buffered the data in the vote_queue. This experience solidified my understanding that availability and processing can be separated to create a more resilient architecture.

Member 2: [Name Here]

(Reflection Here)

Member 3: [Name Here]

(Reflection Here)

Member 4: [Name Here]

(Reflection Here)

Member 5: [Name Here]

(Reflection Here)
