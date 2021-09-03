FROM ubuntu:20.04

RUN apt update && apt install -y openssh-server openssh-client
RUN apt install -y less vim net-tools iproute2

EXPOSE 22
RUN mkdir -p /root/.ssh
COPY ansible_key /root/.ssh/id_rsa
COPY ansible_key.pub /root/.ssh/authorized_keys
#RUN mkdir -p /root/.ssh && ln -s /run/secrets/user_ssh_key /root/.ssh/id_rsa
#RUN ln -s /run/secrets/user_ssh_key_pub /root/.ssh/authorized_keys
RUN chown -R root:root /root/.ssh
RUN chmod -R 600 /root/.ssh
COPY ssh-config /root/.ssh/config

RUN /usr/bin/ssh-keygen -A
RUN service ssh start

CMD /usr/sbin/sshd -D
