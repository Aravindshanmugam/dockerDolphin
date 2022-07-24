#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="aravind"

COPY ./requirement.txt /app/requirement.txt
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /app
RUN pip install -r requirement.txt
#to COPY the remote file at working directory in container
COPY test.py ./
# Now the structure looks like this '/usr/app/src/test.py'

EXPOSE 5000

ENTRYPOINT FLASK_APP=test.py flask run --host=0.0.0.0 --port=5000

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

# CMD [ "FLASK_APP", "test.py"]
