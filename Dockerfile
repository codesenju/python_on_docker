FROM python:3
MAINTAINER codesenju "codesenju@gmail.com"

RUN apt-get update \
  && apt-get install -y python-pip python-dev \
  && cd /usr/local/bin \
  && pip install --upgrade pip
  
COPY . /usr/src/app

# Create app directory
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

#COPY IBM_XL_C_CPP_V1.2.0.0_LINUX_390_RUNTIME.tar.gz /usr/src/app
COPY libibmc++.so.1 /usr/src/app
RUN cd /usr/src/app
RUN tar -zxvf IBM_XL_C_CPP_V1.2.0.0_LINUX_390_RUNTIME.tar.gz
RUN ./install
#RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/ibm/lib64/
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/src/app
RUN export FLASK_APP=app.py

ENTRYPOINT ["python"]

CMD ["app.py"]

