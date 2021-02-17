FROM python:3.6-slim

MAINTAINER Kunal PATIL

# Update and Install git
RUN apt-get update && apt-get install git -y

# Install Twint package from official git version
RUN pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

# Install PySpark
RUN pip3 install --user pyspark