FROM nvcr.io/nvidia/dli/dli-nano-ai:v2.0.2-r32.7.1

# 1. Install tools to manage GPG keys without running apt-get update yet
RUN mkdir -p /usr/share/keyrings && \
    curl -fsSL https://apt.kitware.com/keys/kitware-archive-latest.asc \
    | gpg --dearmor -o /usr/share/keyrings/kitware-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ bionic main" > /etc/apt/sources.list.d/kitware.list

# 2. Now it's safe to update
RUN apt-get update && apt-get install -y \
    curl gnupg lsb-release \
    python3 python3-pip \
    libopencv-dev python3-opencv

# 3. Python packages
RUN pip3 install pyzmq numpy

# 4. Copy and run your camera script
COPY cam_pub.py /cam_pub.py
CMD ["python3", "/cam_pub.py"]

