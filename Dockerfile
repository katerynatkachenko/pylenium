FROM selenium/standalone-chrome-debug

COPY . /tmp

RUN sudo apt update && \
    sudo apt install -y python3-pip

USER seluser

RUN sudo mkdir app && \
    sudo chown seluser:seluser /app

RUN cd /tmp && sudo chmod +x setup.sh && ./setup.sh