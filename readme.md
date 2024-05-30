A client-server networked docker example, using Flask RESTful API to deliver a randomly generated file + checksum to a client. Client will download the file only if checksums match. 


Run instructions:

**Using Docker Compose**
Using docker compose is very simple! Simply use the command *docker-compose up --build*

**Building Manually**
step 1: build the docker images from the docker files
- in the server directory:
    - docker build -t server .
- in the client directory:
    - docker build -t client .

step 2: create a docker network
- in my example, i created a network called "assignment3"
    - docker network create assignment3

step 3: create individual docker volumes to persist data
- docker volume create servervol
- docker volume create clientvol

step 4: run the docker containers, connecting them to the network and mounting the volumes
- server:
    - docker run -v servervol:/serverdata -d --name server --network clientserv -p {port}:5000 server
        - the -p flag will allow you to bind any port of your specification to the exposed port on the container
- client:
    - docker run -v clientvol:/clientdata -d --name client --network clientserv client


if you want to shell in to either container and check the contents of /serverdata or /client data:
- docker exec -it {containername} /bin/bash
    - /{container}data directories are located in the root directory of the container, NOT the working directory.