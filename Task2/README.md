# COMP40660 Assignment 2 - Task 2

This task contains two containers that communicate by IPC.

To run the containers, use the following command:

```bash
# Build and run the server
docker build -t muzhou233/comp40660-task2-server server
docker run --rm --name muzhou233-comp40660-task2-server muzhou233/comp40660-task2-server

# Open a new terminal and run the client
docker build -t muzhou233/comp40660-task2-client client
docker run --rm --name muzhou233-comp40660-task2-client muzhou233/comp40660-task2-client
```

Both server and client containers will exit after the communication is done.
Check the logs of the server container to see the communication.

```bash
docker logs muzhou233-comp40660-task2-server
docker logs muzhou233-comp40660-task2-client
```
