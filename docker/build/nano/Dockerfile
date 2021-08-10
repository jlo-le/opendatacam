FROM resinplayground/jetson-nano-cuda-cudnn-opencv:v0.2-full

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y jq wget

# Start Darknet Install
RUN git clone --depth 1 -b traffic-project https://github.com/jlo-le/darknet /var/local/darknet

WORKDIR /var/local/darknet

# COPY Makefile
COPY Makefile Makefile

RUN make

# COPY weights, get them localy in the Dockerfile folder previously as they are slow to download each time
# Links: https://github.com/AlexeyAB/darknet#pre-trained-models
COPY yolov4-tiny.weights yolov4-tiny.weights

# Include demo.mp4 file
RUN mkdir opendatacam_videos && cd opendatacam_videos && wget https://github.com/jlo-le/opendatacam/raw/development/public/static/demo/demo.mp4

# Install node.js
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs

ENV CACHE_BREAKER 1
RUN git clone --depth 1 -b traffic-project https://github.com/jlo-le/opendatacam /var/local/opendatacam

WORKDIR /var/local/opendatacam

RUN npm install
RUN npm run build

# Set default settings for Desktop run
RUN sed -i -e 's+TO_REPLACE_PATH_TO_DARKNET+/var/local/darknet+g' config.json;
RUN sed -i -e 's+TO_REPLACE_VIDEO_INPUT+file+g' config.json;
RUN sed -i -e 's+TO_REPLACE_NEURAL_NETWORK+yolov4-tiny+g' config.json;

RUN wget -P /var/local/darknet/opendatacam_videos "http://nl.jeanlouisle.com/downloads/B.mov"
RUN sed -i -e 's+demo.mp4+B.mov+g' config.json;

EXPOSE 8080 8070 8090

COPY launch.sh launch.sh
RUN chmod 777 launch.sh
CMD ["./launch.sh"]