#/bin/bash

TAG="latest"
PUSH=0
case $# in
    0)
        echo "tag is $TAG"
        ;;
    1)
        echo "tag is $1"
        TAG=$1
        PUSH=1
        ;;
    *)
        echo "Multiple arguments provided: $@"
        echo "tag is $TAG"
        ;;
esac

docker build -t pytorch211:${TAG} .

# if [[ $PUSH -eq 1 && $? -eq 0 ]]; then
#     docker push specialhwang/cuda113-pytorch:${TAG}
# fi