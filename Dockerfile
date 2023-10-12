FROM python:3.8.16

WORKDIR /app/

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 8080

ENTRYPOINT ["python", "app.py", "8080"]


# docker build -t harbor.cloud.netease.com/qztest/nsf-poc-api:v1.2.0 .
# docker push harbor.cloud.netease.com/qztest/nsf-poc-api:v1.2.0