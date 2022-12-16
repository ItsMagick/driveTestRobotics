cd librealsense-2.51.1
ls
./scripts/patch-realsense-ubuntu-L4T.sh
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev -y
reboot now
sudo reboot now
ls
cd /usr/local/cuda-10.2/bin
ls
cd nvcc
cd librealsense-2.51.1/
ls
./scripts/setup_udev_rules.sh
mkdir build && cd build
cmake .. -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true && make -j$(($(nproc)-1)) && sudo make install
sudo apt-get update
sudo apt-get install cuda
uname -m
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/aarch64/cuda-keyring_1.0-1_all.deb
cd ~/Downloads/
ls
tar xpf Tegra186_Linux_R32.4.3_aarch64.tbz2 
sl
ls
cd ../librealsense-2.51.1/
cd build
cmake .. -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true && make -j$(($(nproc)-1)) && sudo make install
realsense-viewer
sudo nano /etc/environment 
sudo apt-get install nano
nano
sudo nano /etc/environment 
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build && cd build
cmake ../
make -j$(nproc)
sudo make install
sudo ldconfig
cd ..
ls
ls python/
ls python/python/
ls python/python/jetson_inference/
ls python/python/jetson
ls python/python/Jetson
ls
ls build
ls build/examples/
cd build/examples/
ls
cd detectnet/
ls
cd ~
ls
cd jetson-inference/python/examples/
ls
./detectnet.py /dev/video0
cd jetson-inference/python/examples/
./detectnet.py /dev/video0 display://0
v4l2
v4l2-ctl
ffplay
sudo apt-get install ffmpeg
ffplay /dev/video0
ffplay /dev/video1
ffplay /dev/video2
sudo apt-get install v4l-utils
v4l2-ctl --list-devices
cd jetson-inference/python/examples/
./detectnet.py /dev/video2 display://0
cd Desktop/
touch test_pwm.py
nano test_pwm.py 
git -v
git
git --version
cd Documents/
git clone https://github.com/JetsonHacksNano/ServoKit
ls
cd ServoKit/
./install
./installServoKit.sh 
pip --version
python -m pip --version
python3 -m pip --version
cd
python3 -m pip adafruit-circuitpython-servokit
python3 -m pip install adafruit-circuitpython-servokit
sudo apt update
sudo apt upgrade 
python3 -m pip install adafruit-circuitpython-servokit
python3 -m pip update wheel
python3 -m pip -h
python3 -m pip --version
python3 -m pip install adafruit-circuitpython-servokit
python3 -m pip install Adafruit-Blinka
python3 -m pip install adafruit-circuitpython-servokit
pyhton3 -m pip install --upgrade pip
python3 -m pip install --upgrade pip
python3 -m pip install Adafruit-Blinka
python3 -m pip install adafruit-circuitpython-servokit
ls
cd Desktop/
ls
nano test_pwm.py 
setxkbmap de_macintosh
nano test_pwm.py 
python3 test_pwm
python3 test_pwm.py 
python3 --version
nano test_pwm.py 
apt-list | grep python3.10
apt list | grep python3.10
sudo apt install python3.10
python3 --version
sudo nano /usr/bin/gnome-terminal
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --config python3
where python3
whereis python3
whereis python3.10
sudo apt install python3.10
cd
ls -la
nano .bashrc
source ~/.bashrc 
nano .bashrc 
source ~/.bashrc 
cd Desktop/
python3 test_pwm.py 
cd
cd /usr/bin
ls
cd ../local/bin
sl
ls
cd
whereis python
python3 test
ls
cd Desktop/
sl
ls
python test_pwm.py 
cd
nano .bashrc
cd Desktop/
python3 test_pwm.py +
python3 test_pwm.py 
source ~/.bashrc
python3 test_pwm.py 
cd
source ~/.bashrc
cd Desktop/
ls
python3 test_pwm.py 
cd
nano .bash
nano .bashrc
sudo add-apt-repository ppa:deadsnake/ppa
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
top
sudo apt upgrade
apt list | grep python3.10
sudo apt-get install python3.10
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
sudo update-alternatives --config python3
python3 --version
cd Desktop/
python3 test_pwm.py 
python3 -m pip install adafruit-circuitpython-servokit
python3 -m pip3 install adafruit-circuitpython-servokit
nano test_pwm.py 
python3 -m pip install adafruit-circuitpython-servokit
sudo apt-get install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 3
sudo update-alternatives --config python3
python3 -m pip install adafruit-circuitpython-servokit
python --version 
python3 --version 
sudo update-alternatives --config python3
python3 --version
cd Desktop/
python3 --version
python3 test_pwm.py 
python3 -m pip install adafruit-circuitpython-servokit
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
sudo reboot
cd Desktop/
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 -m pip install adafruit-circuitpython-motor
nano test_pwm.py 
python3 -m pip install adafruit-circuitpython-motorkit
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 -m pip install Jetson.GPIO
touch test_motor.py
nano test_pwm.py 
python3 test_pwm.py 
nano test_motor.py 
touch busio_motor.py
nano busio_motor.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
nano busio_motor.py 
python 3 busio_motor.py 
nano busio_motor.py 
python3 busio_motor.py 
ss: 0x%x" % self.device_address)
ValueError: No I2C device at address: 0x60
Exiting... 
exit()
cd ../Documents/
ls
git clone http://github.com/ItsMagick/driveTestRobotics.git
ls
mv ../Desktop/test_pwm.py driveTestRobotics/
mv ../Desktop/test_motor.py driveTestRobotics/
cd driveTestRobotics/
ls
git push
mv test_motor.py ../../Desktop/
mv test_pwm.py ../../Desktop/
ls
man snap
ls
git pull
sl
ls
cd venv
ls
cd ../..
cd ../Desktop/
ls
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
nano test_pwm.py 
python3 test_pwm.py 
cd Desktop/
touch motor_test_2.py
nano motor_test_2.py 
python3 motor_test_2.py 
nano motor_test_2.py 
python3 motor_test_2.py 
/usr/bin/python3.10 /home/herbie/Documents/driveTestRobotics/venv/test_pwm.py
history
history | grep adafruit
workon py3_venv
ls
python3 ./venv/test_pwm.py 
git config --global user.name "ItsMagick" 
git config --global user.email "magick930@googlemail.com" 
python3 ./venv/jetson_motor_servo_control.py 
python3 -m pip install smbus
sudo python3 -m pip install smbus
python3 -m pip install smbus2
python3 ./venv/jetson_motor_servo_control.py 
/usr/bin/python3.10 /home/herbie/Documents/driveTestRobotics/venv/jetson_motor_servo_control.py
python3 ./venv/jetson_motor_servo_control.py
python3 ./venv/test_pwm.py 
python3 ./venv/jetson_motor_servo_control.py
python3 ./venv/test_pwm.py 
/usr/bin/python3 /home/herbie/Documents/driveTestRobotics/venv/test_pwm.py
/usr/bin/python3 /home/herbie/Documents/driveTestRobotics/venv/motor_test_2.py
/usr/bin/python3 /home/herbie/Documents/driveTestRobotics/venv/test_pwm.py
whereis snap
snap install intelliJ
snap install intellij-idea-community --classic
sudo apt install sl
sl
uname -m
cd Downloads/
ls
sudo dpkg -i code_1.73.1-1667967334_amd64.deb 
ls
rm code_1.73.1-1667967334_amd64.deb 
ls
sudo dpkg -i code_1.73.1-1667966450_arm64.deb 
/usr/bin/python3 /home/herbie/Documents/realSense/main.py
python3 -m pip install pyrealsense2
export PYTHONPATH=$PYTHONPATH:/usr/local/lib
history | grep cmake
history | grep python3-dev
sudo apt-get install python3-dev
ls
cd librealsense-2.51.1/
ls
cmake .. -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3.8 && make -j$(($(nproc)-1)) && sudo make install
cmake ./ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3.8 && make -j$(($(nproc)-1)) && sudo make install
python3.6 -m pip install pyrealsense2
cd librealsense-2.51.1/
cmake ./ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3.6 && make -j$(($(nproc)-1)) && sudo make install
cd Documents/driveTestRobotics/
cd venv/
cd ..
git pull
python3 venv/motorControl/init.py
git pull
python3 venv/motorControl/init.py
d
git pull
python3 venv/motorControl/init.py
git pull
python3 venv/motorControl/init.py
git pull
python3 venv/motorControl/init.py
git pull
python3 venv/motorControl/init.py
docker run 
docker ps
ls
cd Documents/
ls
cd driveTestRobotics/venv/camera/
ls
docker build -t cameraTest .
docker build -t camera-test .
docker images
docker container stop python
docker container stop hello-world
docker images
docker stop python
docker stop 8c1c1d9c1f70
docker images rm 8c1c1d9c1f70
docker images rm python
docker rmi python
docker rmi 8c1c1d9c1f70
docker images
docker run python
docker run camer-test
docker run camera-test
docker ps -a
docker ps 
cd Documents/librealsense2/
ls
cd ..
ls
cd ..
cd librealsense-2.51.1/
ls
cd examples/
ls
cd ../wrappers/python/
cd examples/
ls
python3 opencv_viewer_example.py 
cd ../../..
cd build/
ls
cd ..
./scripts/setup_udev_rules.sh 
rm -r ./build/
ls
mkdir build && cd build
cmake ../ -DBUILD_EXAMPLES=true -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB_BACKEND=false -DBUILD_WITH_CUDA=true -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3.6
sudo make uninstall && sudo make clean && sudo make -j4 && sudo make install
sudo make clean && sudo make -j4 && sudo make install
sudo make -j4 && sudo make install
cd ..
sudo make uninstall && sudo make clean && sudo make -j4 && sudo make install
whereis pyrealsense.so
whereis pyrealsense
cd /usr/local/lib/python3.6
ls
cd dist-packages/
ls
cd ../../python3.8
ls
ls ./pyrealsense2/
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.8/pyrealsense2
ls
cd pyrealsense2/
ls
cp pyrealsense2.cpython-36m-aarch64-linux-gnu.so ~/Documents/driveTestRobotics/venv/camera/pyrealsense2.so
cd ../..
ls
cp librealsense2.so ~/Documents/driveTestRobotics/venv/camera/librealsense2.so
sudo apt-get install docker
docker run hello-world
sudo docker run hello-world
cowsay
sudo apt-get install cowsay
sl
cowsay
sudo apt-get install portai
docker volume create portainer_data
sudo docker volume create portainer_data
docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.9.3
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.9.3
sudo -s
/usr/bin/python3 /home/herbie/Documents/driveTestRobotics/venv/pyrealsenseTest.py
/usr/bin/python3 /home/herbie/Documents/driveTestRobotics/venv/camera/pyrealsenseTest.py
git rm --cached venv/camera/*realsense.so
git rm --cached venv/camera/*realsense2.so
git commit --amend -CHEAD
git push
git rm --cached venv/camera/*realsense2.so
git commit --amend -CHEAD
git push
cd Documents/
ls
cd driveTestRobotics/
git pull
cd venv/camera/
ls
docker build -t realcamera
docker build -t realcamera .
sudo docker build -t realcamera .
git pull
sudo docker build -t realcamera .
git pull
sudo docker build -t realcamera .
git pull
sudo docker build -t realcamera .
git pull
sudo docker build -t realcamera .
git pull
sudo docker build -t realcamera .
git pull
cd Documents/
cd driveTestRobotics/
cd venv/camera/
git pull
sudo docker build -t realcamera .
realsense-viewer
cd Documents/driveTestRobotics/venv/
ls
cd camera/
python 3.6 pyrealsenseTest.py 
python 3 pyrealsenseTest.py 
python3.6 pyrealsenseTest.py 
python3 pyrealsenseTest.py 
./pyrealsenseTest.py
sudo ./pyrealsenseTest.py
chmod +x pyrealsenseTest.py
./pyrealsenseTest.py 
git pull
./pyrealsenseTest.py 
cd Documents/driveTestRobotics/venv/camera/
git pull
sudo docker build -t realcamera .
cd ..
git clone https://github.com/JetsonHacksNano/installLibrealsense
cd installLibrealsense
./installLibrealsense.sh
./buildLibrealsense.sh
cd ..
cd /home/herbie/librealsense/build/CMakeFiles/
nano CMakeError.log 
cd
realsense-viewer
virtualenv -p /usr/bin/python3.6
cd Documents/driveTestRobotics/venv/camera/
python36 pyrealsenseTest.py 
git add venv/camera/pyrealsenseTest.py 
