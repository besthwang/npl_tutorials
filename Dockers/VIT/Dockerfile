#FROM cddlyf/pytorch1.0.0-tensorflow-py36-cuda10.0:latest
#FROM nvcr.io/nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04
#FROM nvcr.io/nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
#FROM nvcr.io/nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu20.04
FROM nvcr.io/nvidia/cuda:12.4.0-runtime-ubuntu22.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    apt-utils \
    curl \
    software-properties-common\
    && rm -rf /var/lib/apt/lists/*


RUN  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa

RUN apt-get install -y git cmake
RUN apt-get update && apt-get install wget sudo -y
RUN apt-get update &&apt-get install -y libgl1-mesa-glx ibglib2.0-0 libxcb-xinerama0-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev

# # #python3.10.12 is installed
RUN apt-get install -y build-essential gdb
RUN apt-get install -y python3-pip

# # update pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel
RUN pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu124
RUN pip install jupyter
# #RUN pip install PyQt5==5.15.5
RUN pip install tensorboard
# RUN pip install torchmetrics
# RUN pip install tqdm==4.59.0
RUN pip install matplotlib
# RUN pip install nltk
# RUN pip install torchtext==0.17.2
# RUN pip install seaborn



# #install qt5-defulat 
# # RUN apt-get update && apt-get install -y \
# #     qtbase5-dev \
# #     qttools5-dev-tools \
# #     qtchooser

# RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
#     dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
#     echo "deb [signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
#     tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
#     apt-get update && apt-get install -y gh

# RUN apt install -y gdb

# RUN pip install jpype1

# # KoNLPy 설치 (Okt 포함)
# RUN pip install konlpy
# RUN pip install nltk
# RUN pip install spacy==3.4.3
# RUN python3 -m spacy download en_core_web_sm 

RUN apt-get update && apt-get install -y \
    wget tar openjdk-17-jdk \
    libxtst6 libxext6 libxrender1 libxi6 libfreetype6 libxrandr2 libgtk-3-0 libasound2 \
    && rm -rf /var/lib/apt/lists/*

# PyCharm 설치
RUN wget https://download.jetbrains.com/python/pycharm-community-2023.3.7.tar.gz -O /tmp/pycharm.tar.gz \
    && tar -xzf /tmp/pycharm.tar.gz -C /opt \
    && rm /tmp/pycharm.tar.gz

ENV PATH="/opt/pycharm-community-2023.3.7/bin:${PATH}"
RUN useradd -m -s /bin/bash developer && echo "developer:1234" | chpasswd

# Add the user to the sudoers file
RUN usermod -aG sudo developer
# Optionally, allow sudo without a password (less secure)
RUN echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER developer

WORKDIR /home/developer

RUN echo "PS1=\"torch25# \"" >> /home/developer/.bashrc 

ENTRYPOINT ["bash"]
#CMD qlua -lenv main.lua