ARG venv_python
ARG alpine_version
FROM python:${venv_python}-alpine${alpine_version}

LABEL Maintainer="CanDIG Team"

USER root

RUN apk update

RUN apk add --no-cache \
	autoconf \
	automake \
	bash \
	build-base \
	bzip2-dev \
	cargo \
	curl \
	curl-dev \
	gcc \
	git \
	libcurl \
	libffi-dev \
	libressl-dev \
	linux-headers \
	make \
	musl-dev \
	perl \
	postgresql-dev \
	postgresql-libs \
	xz-dev \
	yaml-dev \
	zlib-dev

RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app
ADD ./requirements-dev.txt /app
RUN pip install -r requirements-dev.txt

COPY . /app/katsu_service

WORKDIR /app/katsu_service


ENTRYPOINT ["python", "manage.py", "runserver"]
