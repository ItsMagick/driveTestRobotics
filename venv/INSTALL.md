Es wird vorausgesetzt, dass das Repo driveTestsRobotics im Dokumente Ordner liegt.

sudo apt install nano
sudo apt install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo apt install python3-pip
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
User=herbie
[Install]
WantedBy = multi-user.target

sudo systemctl enable herbieStartup.service
sudo systemctl daemon-reload
sudo systemctl restart herbieStartup.service


python3 -m pip install pvporcupine

sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
sudo apt-get install python3-pyaudio
