# Google Machine Learning Crash Course in docker  
This is guide to run tensorflow code from [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)

## Steps

### 1. Build and run docker container

```
docker-compose -f ./docker/docker-compose.yml up -d
```

### 2. Connect to bash shell in container

```
docker exec -it gg_ml_cc bash
```

### 3. Allow to run GUI in docker container

```
sudo apt-get install x11-xserver-utils
xhost +
```

### 4. Execute lesson scripts

All source code located in `/src/` in container.

```
cd /src
python first_steps_with_tensor_flow.py
```
