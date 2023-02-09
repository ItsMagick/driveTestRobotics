#!/bin/bash
/bin/sleep 10
docker run -d --net=host --gpus all roboflow/inference-server:jetson
/bin/sleep 10