# Use an official Python runtime as a parent image
FROM python:3.7

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

EXPOSE 8000
CMD ["/bin/bash", "entrypoint.sh"]
