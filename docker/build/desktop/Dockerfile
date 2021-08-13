FROM opendatacam/base-desktop-nvidia-cuda-opencv-gstreamer:1.0

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y jq wget

# Start Darknet Install
RUN git clone --depth 1 -b traffic-project https://github.com/jlo-le/darknet /var/local/darknet

WORKDIR /var/local/darknet

RUN sed -i -e s/GPU=0/GPU=1/ Makefile;
RUN sed -i -e s/CUDNN=0/CUDNN=1/ Makefile;
RUN sed -i -e s/OPENCV=0/OPENCV=1/ Makefile;

RUN make

# COPY weights, get them localy in the Dockerfile folder previously as they are slow to download each time
# Links: https://github.com/AlexeyAB/darknet#pre-trained-models
COPY yolov4.weights yolov4.weights

# Include demo.mp4 file
RUN mkdir opendatacam_videos && cd opendatacam_videos && wget https://github.com/jlo-le/opendatacam/raw/development/public/static/demo/demo.mp4

# Install node.js
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs

# CUSTOM
RUN apt-get install -y python3-venv python3-pip 
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install opencv-python==4.3.0.38

RUN git clone --depth 1 -b traffic-project https://github.com/jlo-le/opendatacam /var/local/opendatacam

WORKDIR /var/local/opendatacam

RUN npm install

RUN git pull
RUN npm run build

# UPDATES
WORKDIR /var/local/darknet
RUN git pull && make

# Set default settings for Desktop run
RUN sed -i -e 's+TO_REPLACE_PATH_TO_DARKNET+/var/local/darknet+g' config.json;
RUN sed -i -e 's+TO_REPLACE_VIDEO_INPUT+file+g' config.json;
RUN sed -i -e 's+TO_REPLACE_NEURAL_NETWORK+yolov4+g' config.json;


RUN git pull npm run build

EXPOSE 8080 8070 8090

COPY launch.sh launch.sh
RUN chmod 777 launch.sh
CMD ["./launch.sh"]
