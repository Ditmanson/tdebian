FROM python:3.13-alpine3.22

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

COPY . /app
COPY .pg_service.conf /
COPY .my_pgpass /
RUN ls -a
RUN chown root:root /.pg_service.conf /.my_pgpass \
  && chmod 600 /.pg_service.conf /.my_pgpass


WORKDIR /app

ENV PGSERVICEFILE=/.pg_service.conf
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "tdebian.wsgi"]
