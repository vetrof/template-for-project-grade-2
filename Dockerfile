FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY ./req.txt .
RUN pip install -r req.txt

#EXPOSE 8000

COPY . .

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
