# Image
FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Add files
COPY . /desafio_hyperativa

# Go to working directory
WORKDIR /desafio_hyperativa

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
