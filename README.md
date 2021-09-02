# Ansible tutorial

1. create docker image
```
docker build -t ansible_base:latest .
```
2. start containers
```
docker-compose up -d
```
3. connect to the control container
```
docker-compose exec control bash
```
4. ssh from control to other container eg.: lb1
```
root@control $ ssh lb1   
```
