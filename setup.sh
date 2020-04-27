
docker build -t def_image .

docker run  -dit --name=def_container -e FLASK_APP=assignment1.py -p 5000:5000 def_image

docker logs -f def_container
