# dockerisilonsdk8

## Overview
Docker file and test script for Isilon SDK 8.0

## Getting Started
Ensure that you have a working docker setup available or follow this link to get started with docker: https://www.docker.com/products/overview

For most modern Linux Distros the following command will install docker for you:

<code>
curl -sSL https://get.docker.com/ | sh
</code>

## Clone the Repo
On the docker host begin by cloning this repo:

<code>git clone https://github.com/j-sims/dockerisilonsdk8.git</code>

## Build the image
<code>cd dockerisilonsdk8</code>

<code>docker build -t dockerisilonsdk8 .</code>

## Run the image Interactively
<code>docker run --rm -ti dockerisilonsdk8 -e USERNAME=<USERNAME> -e PASSWORD=<PASSWORD> URL=<URL> /bin/bash
</code>

<b>Example:</b>
<code>docker run --rm -ti  -e USERNAME=root -e PASSWORD=a -e URL=https://172.16.10.10:8080 dockerisilonsdk8 /bin/bash
</code>

# Run your own code silently
You can create and mount your own code in place of the provide example run.py by replacing run.py with the -v option at runtime
<code>docker run -e USERNAME=root -e PASSWORD=a -e URL=https://172.16.10.10:8080 -v /path/to/myrun.py:/app/run.py dockerisilonsdk8</code>
