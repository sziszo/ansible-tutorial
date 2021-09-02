# Ansible tutorial

1. create docker image
```
docker build -t ansible_base:latest docker
```
2. start containers
```
docker-compose up -d
```
3. connect to the control container
```
docker-compose exec control bash
```
4. ensure ssh service
```
service ssh status
```
5. ssh from control to other container eg.: lb1
```
root@control $ ssh lb1   
```
6. install ansible on control container
```
work/ansible/install-ansible.sh
```
