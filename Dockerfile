FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app.yaml /code
COPY ./main.py /code
COPY ./txt_file.txt /code

#
CMD ["python", "main.py"]