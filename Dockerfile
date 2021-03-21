# base image
FROM nginx


#install Python and pip
#RUN apk add --update py-pip

#upgrade pip
#RUN pip install --upgrade pip

# install Python modules
#COPY ./requirements.txt /usr/src/app/requirements.txt
#RUN pip install -r /usr/src/app/requirements.txt

#copy files
#COPY app.py /usr/src/app
COPY index.html /usr/share/nginx/html
RUN echo "000 App Fin 000"

#port number for container
EXPOSE 80

#run the app
#CMD ["/usr/src/app/index.html"]
