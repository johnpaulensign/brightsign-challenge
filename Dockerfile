FROM python:3

# get build args
ARG IP
ARG IPSTACK_KEY

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY queryip.py ./

# set environment variables
ENV IPSTACK_KEY=$IPSTACK_KEY
ENV IP=$IP
CMD [ "sh", "-c", "python ./queryip.py $IP" ]