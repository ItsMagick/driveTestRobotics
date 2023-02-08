Es wird vorausgesetzt, dass das Repo driveTestsRobotics im Dokumente Ordner liegt.
Libraries müssen für root installiert werden! Service ist Root

sudo apt install nano
sudo apt install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo apt install python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install adafruit-circuitpython-servokit
python3 -m pip install inputs

sudo chmod +x Documents/driveTestRobotics/venv/init.py
sudo nano /etc/systemd/system/herbieStartup.service

[Unit]
Description = Herbie Python Startup
[Service]
Type = idle
ExecStartPre = /bin/sleep 10
ExecStart = /home/herbie/Documents/driveTestRobotics/venv/init.py
User=root
[Install]
WantedBy = multi-user.target

sudo systemctl enable herbieStartup.service
sudo systemctl daemon-reload
sudo systemctl restart herbieStartup.service


sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
sudo apt-get install python3-pyaudio

sudo apt-get install libffi6 libffi-dev
sudo apt install libpython3.8-dev

python3 -m pip install sounddevice

python3 -m pip install Cython

python3 -m pip install wavio


python3 -m pip install torch==1.10.0 torchvision==0.11.1 torchaudio==0.10.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html
python3 -m pip install git+https://github.com/openai/whisper.git --ignore-installed PyYAML

sudo apt update && sudo apt install ffmpeg


For Camera COCO Test
pip instlal pycocotools

pip install imageAI

pip install tk


sudo apt install zsh -y
sudo apt install curl
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/AssemblyAI/assemblyai-cli/main/install.sh)"
