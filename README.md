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
5. install ansible
```
root@control $ yum install -y epel-release
root@control $ yum install -y ansible
root@control $ ansible --version
root@control $ ansible-playbook --version
root@control $ ansible-galaxy --version
```
