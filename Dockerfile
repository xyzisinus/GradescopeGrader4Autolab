FROM ubuntu:xenial

# The purpose of this container:
# Mimick the grader execution environment in a Gradescope container

# Install ssh (and vim for debugging)
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    openssh-server \
    vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# build the directory structure for a Gradescope grader
RUN mkdir /autograder
RUN mkdir /autograder/results
WORKDIR /autograder

COPY ./source source
COPY ./submission submission
COPY ./source/run_autograder .

# in submission_metadata.json we want to use the submission id
RUN echo \{\"id\":123456\} > submission_metadata.json

# setup.sh installs stuff needed by grader.py
# it's used by Gradescope to build its container, too.
RUN chmod +x source/setup.sh
RUN source/setup.sh

# Set the locale to UTF-8 to ensure that Unicode output is encoded correctly
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# debugging
# CMD /autograder/run_autograder; sleep 10000

# normal exec
CMD /autograder/run_autograder
