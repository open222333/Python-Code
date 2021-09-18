1.mysql-master設定
＃登入mysql
mysql -u{$username} -p{$password}

＃確認mysql-master server_id和log_bin變數
show variables like 'server_id%';
show variables like 'log_bin%';

<!-- **mysql-master server_id和log_bin變數正確跳至第一步-建立master-slave使用者** -->

＃停止mysql
service mysql stop

＃mysql-master 加入下列到 my.cnf
[mysqld]
log-bin = mysql-bin
server-id = 1

＃啟動mysql
service mysql start

＃登入mysql
mysql -u{$username} -p{$password}

＃確認mysql-master server_id和log_bin變數
show variables like 'server_id%';
show variables like 'log_bin%';

＃建立master-slave使用者
CREATE USER 'replication'@'192.168%' IDENTIFIED BY '.wFb9A?$9*WN';
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'192.168%';

＃檢查使用者
select User, Host From mysql.user;


2.mysql-slave設定
＃登入mysql
mysql -u{$username} -p{$password}

＃檢查mysql-slave server_id和read_only變數
show variables like 'server_id%';
show variables like 'read_only%';

**mysql-slave server_id和read_only變數正確跳至第三步**

＃停止mysql
service mysql stop

＃mysql-master 加入下列到 my.cnf
[mysqld]
server-id = 2
read-only = ON

＃啟動mysql
service mysql start

＃登入mysql
mysql -u{$username} -p{$password}

＃確認mysql-slave server_id和read_only變數
show variables like 'server_id%';
show variables like  'read_only%';

3.備份mysql-master
＃master全表鎖定只讀
FLUSH TABLES WITH READ LOCK;

#檢查master是否lock
