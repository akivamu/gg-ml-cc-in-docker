# Google Machine Learning Crash Course in docker

This is guide to run tensorflow code from [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)

## Steps

### 1. Setup docker image & container

```shell
# Build docker image and run container
docker-compose -f ./docker/docker-compose.yml up -d

# Allow to run GUI in docker container
sudo apt-get install x11-xserver-utils
xhost +

# Connect to bash shell in container (to run code)
docker exec -it gg_ml_cc bash
```

### 2. Play around with code

All source code located in `src` folder, which is mapped to `/src/` in container.  
Modify code, play with it and execute in bash shell opened in container:

```shell
python /src/intro_to_pandas.py
python /src/first_steps_with_tensor_flow.py
...
```

#### Temporary stop/resume container

```shell
# Stop container
docker-compose -f ./docker/docker-compose.yml stop

# Resume learning
docker-compose -f ./docker/docker-compose.yml up -d
docker exec -it gg_ml_cc bash
```

### 3. Cleanup

```shell
# Delete container
docker-compose -f ./docker/docker-compose.yml down

# Delete image
docker rmi docker_gg_ml_cc
...
```
