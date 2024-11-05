FROM ubuntu:22.04
LABEL maintainer="languageplanet.com"

# Basic Environment Varibles
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ America/Denver

# Add user
RUN adduser lang --disabled-login --gecos ""

#Packages Repos
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y curl

#install node
RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    NODE_MAJOR=20 && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install nodejs -y

#install server packs
RUN apt-get install -y \
    libssl-dev \
    libpq-dev \
    locales \
    vim \
    wget \
    python3 \
    python3-pip \
    gettext

# Install yarn
RUN mkdir /etc/apt/keyrings/debian
RUN wget -O- https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /etc/apt/keyrings/debian/pubkey.gpg > /dev/null
RUN echo "deb [signed-by=/etc/apt/keyrings/debian/pubkey.gpg] https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

# Python
RUN pip3 install --upgrade pip
RUN mkdir -p /home/lang/djangotemplate/
COPY ./requirements /home/lang/djangotemplate/requirements
RUN pip3 install -r /home/lang/djangotemplate/requirements/requirements.txt

#Copy in main project
COPY . /home/lang/djangotemplate

# Static and Media
RUN mkdir -p /var/lib/static/ && \
    mkdir -p /var/lib/media/ && \
    chown -R lang:lang /var/lib/static && \
    chown -R lang:lang /var/lib/media && \
    chmod -R 755 /var/lib/static && \
    chmod -R 755 /var/lib/media && \
    chown -R lang:lang /home/lang/djangotemplate/mysite/static

#Setup Work Directory
WORKDIR /home/lang/djangotemplate/

RUN chmod -R +x ./scripts

#Setup Env
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

USER lang
