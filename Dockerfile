FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY . usr/src/webapp
WORKDIR usr/src/webapp
RUN pip install -r requirements.txt