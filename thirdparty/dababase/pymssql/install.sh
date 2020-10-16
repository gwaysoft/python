#!/usr/bin/env bash
# c
yum -y install gcc
# c++
yum -y install gcc-c++

yum -y install unixODBC unixODBC-devel

# install freedbs
# https://www.freetds.org/
curl -O ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.2.5.tar.gz
zxf freetds-0.95.91.tar.gz

cd freetds-0.95.91

./configure --prefix=/application/freetds --enable-msdblib --with-tdsver=7.3
make && make install

sudo tee >> /root/.bash_profile <-'EOF'
export FREETDS_HOME=/application/freetds
export PATH=$PATH:$FREETDS_HOME/bin
ln -sf /application/freetds/lib/* /usr/lib/
ln -sf /application/freetds/include/* /usr/include/
ldconfig
EOF

source ~/.bash_profile


