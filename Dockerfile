FROM python:3.7.1-alpine3.8

LABEL maintainer Aleksandr.Makhinov <monaxgt@gmail.com>
ENV GOOGLE_MAP_API_KEY='YOUR_GOOGLE_MAP_API_KEY'

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apk --no-cache --update-cache add gcc gfortran build-base freetype-dev libpng-dev py3-qt5 libxml2-dev libxslt-dev python-dev \
    && pip install --no-cache-dir setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

VOLUME ./TweetAnalysis.db


ENTRYPOINT ["/bin/sh"]
