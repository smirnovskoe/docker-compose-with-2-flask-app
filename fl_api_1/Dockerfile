FROM python:3.6

LABEL user="yanix"
LABEL email="smirnovskoe@gmail.com"

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]