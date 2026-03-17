## Docker:
1. Dockerfile
2. docker build -t fastapi-app .
3. docker run -p 8000:8000 fastapi-app
4. docker run -d -p 8000:8000 fastapi-app (runs in bg so u can check it in docker ps)
5. docker ps
6. docker logs -f [image-name]
7. docker stop 3d0ff26d07a2 #image id
8. docker rm my-fastapi # removes image

## Push Docker Image to Docker Hub
1. docker login
2. docker tag fastapi-app satyamy21/fastapi-app:latest
3. docker push satyamy21/fastapi-app:latest
### pull and run anywhere
4. docker pull satyamy21/fastapi-app:latest
5. docker run -d -p 8000:8000 satyamy21/fastapi-app:latest