sudo docker build . -t recognition_api:latest
sudo docker run -p 8080:80 recognition_api