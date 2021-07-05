FROM python:3.9-alpine
ENV PYTHONUNBUFERED=1
WORKDIR /code

RUN pip install pip -U
COPY requirements.txt /code/requirements.txt
RUN \
    apk add --no-cache postgresql-libs && \
    apk add gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    apk add --no-cache --virtual .build-deps musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . /code/
RUN ["chmod", "+x", "docker-entrypoint.sh"]
ENTRYPOINT ["/bin/sh" , "docker-entrypoint.sh"]
