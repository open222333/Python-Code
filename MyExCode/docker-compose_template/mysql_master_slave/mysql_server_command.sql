-- master server
-- 確認mysql-master server_id和log_bin變數
show variables like 'server_id%';
show variables like 'log_bin%';

-- master server
-- 該File列顯示日誌文件的名稱並Position顯示文件中的位置。在這個例子中，二進制日誌文件是 mysql-bin.000003，位置是 73。記錄這些值。稍後在設置副本時需要它們。它們表示副本應開始處理來自源的新更新的複制坐標。
SHOW MASTER STATUS;

-- master server
-- 建立master-slave使用者
-- CREATE USER 'replication'@'192.168%' IDENTIFIED BY '.wFb9A?$9*WN';
-- GRANT REPLICATION SLAVE ON *.* TO 'replication'@'192.168%';
-- 要創建新帳戶，請使用CREATE USER。要授予此帳戶複製所需的權限，請使用該GRANT 語句。如果您僅為複制目的創建帳戶，則該帳戶只需要 REPLICATION SLAVE權限。例如，要設置一個repl可以從example.com域內的任何主機連接以進行複制 的新用戶
CREATE USER 'repl'@'%.example.com' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%.example.com';
-- ＃檢查使用者
select User, Host From mysql.user;


CREATE USER 'repl'@'172.105.39.26' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'172.105.39.26';

-- slave server
-- 檢查mysql-slave server_id和read_only變數
show variables like 'server_id%';
show variables like 'read_only%';
-- slave server
-- 新增mysql-slave設定master資料
CHANGE MASTER TO MASTER_HOST = '{$master ip}',
MASTER_PORT = 3306,
MASTER_USER = 'replication',
MASTER_PASSWORD = '.wFb9A?$9*WN',
-- master server 輸入 SHOW MASTER STATUS 找出資訊;
MASTER_LOG_FILE = '{$master bin_log filename}',
MASTER_LOG_POS = { $log position };
-- 確認 slave狀態 SHOW SLAVE STATUS; 會很醜
SHOW SLAVE STATUS\G
-- 執行slave
start slave;


CHANGE MASTER TO MASTER_HOST = '172.105.39.26',
MASTER_PORT = 31216,
MASTER_USER = 'repl',
MASTER_PASSWORD = 'password',
MASTER_LOG_FILE = 'mysql-bin.000003',
MASTER_LOG_POS = 12345;
SHOW SLAVE STATUS\G
