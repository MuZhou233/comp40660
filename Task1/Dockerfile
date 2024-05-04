# This file is used to build the docker image for COMP40660 Assignment 2

# Group Members:
# Hang Li
# Yaning Li

# Use the official nginx image as the base image

FROM nginx:stable-bookworm

# Replace the index.html file in the default nginx directory with the index.html file in the current directory

COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 to the host machine

EXPOSE 80

# Additional packages required for the assignment

ARG DEB_PKGS="curl vim iputils-ping net-tools"

# Install the required packages

RUN apt-get update && apt-get install -y $DEB_PKGS
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Copy the annotation file to opt directory

RUN mkdir -p /opt/task1
COPY annotation.txt /opt/task1/annotation.txt

# Add print script to entrypoint

COPY print.sh /docker-entrypoint.d/90-print.sh
