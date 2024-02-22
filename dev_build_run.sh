sudo docker build . -t recognition_api:latest
sudo docker run -p 8080:8080 recognition_api