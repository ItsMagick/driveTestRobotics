#!/bin/bash
/bin/sleep 5
docker run -d --net=host --gpus all roboflow/inference-server:jetson
/bin/sleep 3
