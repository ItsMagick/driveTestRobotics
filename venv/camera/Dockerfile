FROM python:3.6
WORKDIR /usr/scripts/herbie
RUN apt-get update

RUN sudo apt install libssl-dev
RUN wget https://github.com/IntelRealSense/librealsense/archive/refs/tags/v2.48.0.zip
RUN unzip v2.48.0.zip
RUN cd librealsense-2.48.0
RUN mkdir build && cd build

RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
RUN export PATH=$PATH:$CUDA_HOME/bin

RUN cmake ../ -DFORCE_RSUSB_BACKEND=ON -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3
RUN make -j4
RUN sudo make install
RUN export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/pyrealsense2

RUN sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
RUN sudo udevadm control --reload-rules && udevadm trigger


COPY pyrealsenseTest.py .
CMD ["python", "./pyrealsenseTest.py"]
