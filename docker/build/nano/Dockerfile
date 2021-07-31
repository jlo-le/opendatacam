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

# CUSTOM
RUN apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
RUN apt-get install -y python3-pip

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip3 install -U pip
RUN pip3 install -U cython numpy grpcio absl-py py-cpuinfo psutil portpicker six mock requests gast h5py astor termcolor protobuf keras-applications keras-preprocessing wrapt google-pasta

RUN pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v43 tensorflow==1.15.2+nv20.3

# RUN apt-get install -y python3-apt python3-dev && \
#     apt-get install -y python3-scipy python3-pandas python3-sklearn && \

#     RUN python3 -m pip install --upgrade pip && \
#     python3 -m pip install scikit-image h5py imgaug IPython "keras>=2.0.8"

# RUN apt-get install -y python3-venv python3-pip && \
#     python3 -m pip install --upgrade pip && \
#     python3 -m pip install opencv-python


# RUN mkdir /var/local/tensorflow
# WORKDIR /var/local/tensorflow
# RUN wget "https://developer.download.nvidia.com/compute/redist/jp/v41/tensorflow-gpu/tensorflow_gpu-1.10.0+nv18.10-cp36-cp36m-linux_aarch64.whl" && \
#     python3 -m pip install tensorflow_gpu-1.10.0+nv18.10-cp36-cp36m-linux_aarch64.whl

# WORKDIR /var/local/opendatacam

# Set default settings for Desktop run
RUN sed -i -e 's+TO_REPLACE_PATH_TO_DARKNET+/var/local/darknet+g' config.json;
RUN sed -i -e 's+TO_REPLACE_VIDEO_INPUT+file+g' config.json;
RUN sed -i -e 's+TO_REPLACE_NEURAL_NETWORK+yolov4-tiny+g' config.json;

EXPOSE 8080 8070 8090

COPY launch.sh launch.sh
RUN chmod 777 launch.sh
CMD ["./launch.sh"]