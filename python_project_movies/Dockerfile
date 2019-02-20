FROM alpine

# set environment variables
ENV FLASK_APP=server.py


# set czech mirrors, thx cvut
RUN printf "https://mirror.fit.cvut.cz/alpine/v3.9/main/\nhttps://mirror.fit.cvut.cz/alpine/v3.9/community/" > /etc/apk/repositories

# update repos
RUN apk update
# upgrade
RUN apk upgrade
# install base python
RUN apk add python3
# install flask
RUN apk add py3-flask

# create user uwsgi, no password, nologin shell, workdir as home
WORKDIR /var/www
RUN adduser -D -s /sbin/nologin -h /var/www uwsgi
# switch to user
USER uwsgi

# add project files to WORKDIR
COPY moviedb moviedb
COPY server.py server.py
COPY films.json films.json

# expose internal port 5000 to external port 5000, both tcp and udp
EXPOSE 5000 5000
# set ip a (to show ip) && flask run as entrypoint (when image is run)
# --host 0.0.0.0 is for whole network, note this is for DEBUG only
ENTRYPOINT ip a && flask run --host=0.0.0.0
