FROM centos:7

# Instala vsftpd y python

RUN yum -y update && \
    yum -y install vsftpd epel-release && \
    yum -y install python3 && \
    yum -y install git && \
    yum clean all

# Cambia la version de python de 2.7 a 3.6

RUN ln -sf /usr/bin/python3.6 /usr/bin/python2.7

# Copia archivo conf the vsftpd

COPY vsftpd.conf /etc/vsftpd/vsftpd.conf

# Copia archivos python

WORKDIR /usr/src/app
COPY . .

# Expone puertos

EXPOSE 5000

#Empieza el servicio de vsftpd
CMD ["/usr/sbin/vsftpd", "/etc/vsftpd/vsftpd.conf"]

