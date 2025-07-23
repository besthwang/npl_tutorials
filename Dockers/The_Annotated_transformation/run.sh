#/bin/bash

#WORK_PATH="FloorplanTransformation"

# if [ ! -d $WORK_PATH ]; then
#     git clone "https://github.com/besthwang/FloorplanTransformation.git"
# else
#     echo "The folder exists: $WORK_PATH"
# fi

docker run --gpus all \
--volume=$PWD/npl_tutorials:/home/developer/npl_tutorials \
-e PYTHONPATH="/home/developer/FloorplanTransformation" \
-e DISPLAY=$DISPLAY  -v /tmp/.X11-unix:/tmp/.X11-unix \
-p 8888:8888 -p 6006:6006 -p 8080:8080 \
--rm -it \
--env="QT_X11_NO_MITSHM=1"  \
--name pytorch211 pytorch211:latest

#-e PYTHONPATH="/home/developer/FloorplanTransformation/visualplan"
#e PYTHONPATH="/home/developer/FloorplanTransformation/visualplan" \