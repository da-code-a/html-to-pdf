FROM selenium/standalone-chrome
USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN mkdir -p /builds/pdf_app/
COPY . /builds/pdf_app/
WORKDIR /builds/pdf_app/
RUN python3 -m pip install -r requirements.txt
EXPOSE 8080
CMD python3 app.py
