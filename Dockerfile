FROM python:3.9-alpine
LABEL maintainer="yuhr123@gmail.com"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U && \
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple && \
pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

EXPOSE 8000
CMD exec gunicorn tarot.wsgi:app --bind 0.0.0.0:8000