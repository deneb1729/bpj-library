FROM python:3.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV home_app /src/app

WORKDIR $home_app

COPY requirements.txt $home_app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . $home_app/

RUN mkdir $home_app/static && \
    mkdir $home_app/media

EXPOSE 8000 $PORT
RUN useradd john && \
    chown -R john:john $home_app
USER john

ENTRYPOINT [ "/src/app/entrypoint.sh" ]
CMD gunicorn library.wsgi:application --bind 0.0.0.0:$PORT --log-level info
