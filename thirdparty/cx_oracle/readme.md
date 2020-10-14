# download
https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

# install
rpm -ivh oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm
rpm -ivh oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm

# view install directory
rpm -qpl oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm

# vim ~/.bash_profile
export ORACLE_HOME=/usr/lib/oracle/12.2/client64
export TNS_ADMIN=$ORACLE_HOME/network/admin
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$PATH:ORACLE_HOME/bin
-----------
$ source .bash_profile

#sqlplus
sqlplus64 ebaotech_oa/ebaotech_oapwd@172.16.7.232:1522/o232g4

# install cx_Oracle
pip3 install cx-Oracle

# solve DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory
sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf"
sudo ldconfig