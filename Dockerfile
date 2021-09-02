FROM centos:latest

RUN yum install -y openssh-server openssh-clients

EXPOSE 22
RUN mkdir -p /root/.ssh && ln -s /run/secrets/user_ssh_key /root/.ssh/id_rsa
RUN ln -s /run/secrets/user_ssh_key_pub /root/.ssh/authorized_keys
RUN chown -R root:root /root/.ssh
COPY ssh-config /root/.ssh/config

RUN rm /run/nologin #https://unix.stackexchange.com/questions/487742/system-is-booting-up-unprivileged-users-are-not-permitted-to-log-in-yet

RUN /usr/bin/ssh-keygen -A

CMD /usr/sbin/sshd -D
