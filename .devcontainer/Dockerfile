# Start from the NVIDIA PyTorch image
# FROM unifyai/ivy:latest-gpu
FROM nvcr.io/nvidia/pytorch:23.10-py3

# Update libstdc++.so.6 for this image
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common && \
    DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y libstdc++6

# Install btop
RUN wget "https://github.com/aristocratos/btop/releases/latest/download/btop-x86_64-linux-musl.tbz" && \
    tar xvjf btop-x86_64-linux-musl.tbz -C /usr/local/bin && \
    rm btop-x86_64-linux-musl.tbz

# Install necessary tools and libraries to parse toml and manage Python venv
RUN apt-get update && apt-get install -y python3-venv

# Set work directory
WORKDIR /workspaces

RUN pip install toml

# Copy over the training.toml
COPY training.toml .

COPY scripts/parse_toml.py /parse_toml.py

RUN python3 /parse_toml.py

RUN python3 -m venv venv --system-site-packages && \
    venv/bin/pip install -r requirements.txt