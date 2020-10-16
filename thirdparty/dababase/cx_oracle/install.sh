#!/usr/bin/env bash
rpm -ivh oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm
rpm -ivh oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm

rpm -qpl oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm

sudo tee >> ~/.bash_profile <<-'EOF'
export ORACLE_HOME=/usr/lib/oracle/12.2/client64
export TNS_ADMIN=$ORACLE_HOME/network/admin
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$PATH:ORACLE_HOME/bin
EOF

source ~/.bash_profile

# solve DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory
sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf"
ldconfig
