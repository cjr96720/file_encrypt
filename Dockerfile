FROM python:3.9

ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ /etc/Timezone

RUN apt-get update \
    && apt-get upgrade -y

RUN useradd -m -d /home/devuser -s /bin/bash devuser
USER devuser
WORKDIR /home/devuser/app

COPY . .

RUN pip3 install -r requirements.txt