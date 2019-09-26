# Ensembl Python REST API Deployment.

Deploying is one of the most important components if of an application launching process. An improper deployment can cause of the total failing of the system and low performance of the system.

### Deploying Flask REST API with Docker and nginx

To deploy a web service, the best available method is Docker as for my knowledge. It's easy to manage, scalable and has a huge supporting community. 

With a nginx reverse procy server, we can easily manage incoming traffic and redirect when necessary. 

##### Step 1:
Make a `DockerfileENV` file. This is not necessary, but without this,everytime you build this docker image, you need to reinstall all the python requirments and it will take some time.

```
FROM python:3
WORKDIR /app  --> This must be your project directory.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```
Then we cn build this script and make it active. You can mame `ensembl_env` as yout like according to your project name.
```
docker build --no-cache -t ensembl_env -f DockerfileENV .
```
##### Step 2:
Now we need to make the `Dockerfile` and copy our project into production Docker environment. 

```
FROM ensembl_env
WORKDIR /app
COPY . .
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080","wsgi:app" ]
```
In here, I'm not using Flask default built in development server. When we are production stage, we need to use much stabe and secure development server like `gunicorn`. 

##### Stage 3:

Now we need to use nginx reverse proxy and manage all the incoming trffic to default port 80 to our dockererized app port 8080. We need to create a nginx configuration file and add all the commands.

#### Stage 4:

Finally we need to create the docker-compose file in order to combine everything and deploy. This is a sample template of `docker-compose.yml` file.

```
version: '2'
services:
  app:
    restart: always
    build:
      context:  ./app
      dockerfile: Dockerfile
    expose:
      - "8080"
  proxy:
    restart: always
    build:
      context:  ./nginx
      dockerfile: Dockerfile
    ports:
      - "80:80"
    links:
      - app
```
Finally you need to use following commands in order to deploy our Ensembl REST API application properly.

```
docker build --no-cache -t ensembl_api ./app
docker-compose build
docker-compose up
```

Now we have a single docker instance running Ensembl REST API. With the nginx proxy server, it can handle reuests better than a normal docker instance with a simple Apache server.

And also we can use mirror servers according to user's location. For example, when someone trying to use an endpoint via Ensembl dashboard from asia, we can use `asia.ensembl.org/xxx/yyy`. In this way, we can give user specific service and also reduce single server bandwidth usage.

Furthermore we can use Memcached in order to speed up REST request/response data flow. Memcached is very responsive and speed processing database solution better than MySQL. 

This REST API is created using `Blueprints`. The main advantage is it's really easy to add new modules and add new features into the REST API. Flask Blueprint has awesome features to manage advanced REST applications in a easy and organized way. And also in this server, we manage all the model classes in a seperate directory and it's really easy to manage new modules and services.

And also when we have `requests-cache` used in this system, we don't need to spend more resourses for the same request over and over again. 

With all the above mentioned deployment strategies and tools,I can ensure that this REST API can handle more requests than a simple hosted API and also this system can be scaled according to the future requirments. 