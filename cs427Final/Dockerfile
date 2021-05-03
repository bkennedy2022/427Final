# use alpine linux container
FROM alpine:3.7

# as per prof's suggestions via slack to install pandas early
RUN apk add python3 py3-pip python3-dev alpine-sdk

# make local directory
RUN mkdir /final427
WORKDIR /final427

# install requirements listed for app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy entire project over to docker
COPY . .

# adjust permissions to the start_script (ran into 127 error before adding this)
RUN ["chmod", "+x", "./startup.sh"]

# run start_script to run all necessary migrations/collections/deployments for django
CMD ./startup.sh 