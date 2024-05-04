# COMP40660 Assignment 2

This container is only used for the purpose of the assignment.
It is a simple container that runs a nginx server on port 80.
The web server serves a static HTML page that displays the message containing our group info.

## Usage

To run the container, use the following command:

```bash
docker run --rm -p 80:80 --name muzhou233-comp40660 muzhou233/comp40660
```

Then, open your browser and go to `http://127.0.0.1` to see the message.

For using the container command line, open a new terminal and run the following command:

```bash
docker exec -it muzhou233-comp40660 bash
```

The custom file required for the assignment is located at `/opt/task1`.

```bash
cat /opt/task1/annotation.txt
```