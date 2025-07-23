#FROM cddlyf/pytorch1.0.0-tensorflow-py36-cuda10.0:latest
#FROM nvcr.io/nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04
#FROM nvcr.io/nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
FROM nvcr.io/nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    openjdk-11-jdk \
    apt-utils \
    curl \
    software-properties-common\
    && rm -rf /var/lib/apt/lists/*

    # 2. JAVA_HOME 명시적으로 설정
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"
ENV LD_LIBRARY_PATH=$JAVA_HOME/lib/server

RUN  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa


# #python3.8 is installed
RUN apt update
RUN apt install -y python3 
RUN apt-get install -y build-essential gdb
RUN apt-get install -y python3-pip

# update pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel
RUN pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu121
RUN pip install jupyter
#RUN pip install PyQt5==5.15.5
RUN pip install tensorboard
RUN pip install torchmetrics
RUN pip install tqdm==4.59.0
RUN pip install matplotlib
RUN pip install nltk
RUN pip install torchtext==0.17.2
RUN pip install seaborn

RUN apt-get install -y git cmake
RUN apt-get update && apt-get install wget sudo -y
RUN apt-get update &&apt-get install -y libgl1-mesa-glx ibglib2.0-0 libxcb-xinerama0-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev

#install qt5-defulat 
# RUN apt-get update && apt-get install -y \
#     qtbase5-dev \
#     qttools5-dev-tools \
#     qtchooser

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
    dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
    tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt-get update && apt-get install -y gh

RUN apt install -y gdb

RUN pip install jpype1

# KoNLPy 설치 (Okt 포함)
RUN pip install konlpy
RUN pip install nltk
RUN pip install spacy==3.4.3
RUN python3 -m spacy download en_core_web_sm 

RUN useradd -m -s /bin/bash developer && echo "developer:1234" | chpasswd

# Add the user to the sudoers file
RUN usermod -aG sudo developer
# Optionally, allow sudo without a password (less secure)
RUN echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER developer

WORKDIR /home/developer
RUN echo "PS1=\"torch21# \"" >> /home/developer/.bashrc 

ENTRYPOINT ["bash"]
#CMD qlua -lenv main.lua