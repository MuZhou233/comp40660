# https://medium.com/techanic/docker-containers-ipc-using-sockets-part-1-2ee90885602c
# Get the latest base image for python
FROM python:latest
# Put files at the image '/client/' folder.
ADD ipc_client.py /client/
# '/server/' is base directory
WORKDIR /client/
# execute the command
CMD [ "python3", "/client/ipc_client.py" ]
