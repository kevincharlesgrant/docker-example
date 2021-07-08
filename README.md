# docker-example

Brief example of serving a sine estimation model via flask and containerizing with Docker. 

Run "docker build --tag python-docker ." to build Docker image followed by "docker run --publish 5000:5000 python-docker" to run container. 

Enter inputs into HTML interface at localhost:5000 or via API call using request.py.
