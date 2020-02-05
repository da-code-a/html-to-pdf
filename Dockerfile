FROM ubuntu
RUN apt update
RUN apt install -y chromium-browser python3 python3-pip wget unzip
RUN mkdir -p /builds/pdf_app/
COPY . /builds/pdf_app/
WORKDIR /builds/pdf_app/
RUN wget https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/ -o driver.zip
RUN unzip driver.zip
ENV PATH /builds/pdf_app:$PATH
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 app.py