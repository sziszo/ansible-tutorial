# Ansible tutorial

## Setting up the environment

1. generate an ssh key
```
ssh-keygen -q -t rsa -N '' -f docker/ansible_key
```
2. create docker image
```
docker build -t ansible_base:latest docker
```
3. start containers
```
docker-compose up -d
```
4. connect to the control container
```
docker-compose exec control bash
```
5. ensure ssh service
```
service ssh status
```
6. ssh from control to other container eg.: lb1
```
root@control $ ssh lb1   
```
7. install ansible on control container
```
work/ansible/install-ansible.sh
```
