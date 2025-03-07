FROM alpine:3.8

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk --no-cache add \
        python3 \
        postgresql-libs \
        libstdc++ \
        lapack \
        libxml2 \
        libxslt \
        libffi \
        && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    apk add --no-cache --virtual .build-deps \
        build-base \
        postgresql-dev \
        python3-dev \
        lapack-dev \
        gfortran \
        libxml2-dev \
        libxslt-dev \
        libffi-dev \
         && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm -fr /root/.cache && \
    rm /usr/include/xlocale.h && \
    apk del .build-deps

COPY . .
ENV PYTHONPATH `pwd`/..

EXPOSE 5000

CMD [ "python3", "Webservice/Tower_Webservice.py" ]
