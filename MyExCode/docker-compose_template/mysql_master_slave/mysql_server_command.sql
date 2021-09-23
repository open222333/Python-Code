-- master server
-- 確認mysql-master server_id和log_bin變數
SHOW VARIABLES LIKE 'server_id%';
SHOW VARIABLES LIKE 'log_bin%';

-- master server
-- 該File列顯示日誌文件的名稱並Position顯示文件中的位置。在這個例子中，二進制日誌文件是 mysql-bin.000003，位置是 73。記錄這些值。稍後在設置副本時需要它們。它們表示副本應開始處理來自源的新更新的複制坐標。
SHOW MASTER STATUS;

-- master server
-- 建立master-slave使用者
-- 要創建新帳戶，請使用CREATE USER。要授予此帳戶複製所需的權限，請使用該GRANT 語句。如果您僅為複制目的創建帳戶，則該帳戶只需要 REPLICATION SLAVE權限。例如，要設置一個repl可以從example.com域內的任何主機連接以進行複制 的新用戶
CREATE USER 'user'@'host' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'user'@'host';

-- 查看 ‘dbuser’@’localhost’ 所擁有的權限
SHOW GRANTS FOR 'user'@'host';
-- 移除權限
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user'@'host';
--  刪除使用者
DROP USER 'user'@'host';
-- 檢查使用者
-- 列出所有使用者帳號
SELECT User,Host FROM mysql.user;

-- slave server
-- 檢查mysql-slave server_id和read_only變數
SHOW VARIABLES LIKE 'server_id%';
SHOW VARIABLES LIKE 'read_only%';
-- slave server
-- 新增mysql-slave設定master資料 綁定到master
CHANGE MASTER TO MASTER_HOST = 'master ip',
MASTER_PORT = 3306,
MASTER_USER = 'user',
MASTER_PASSWORD = 'password',
-- master server 輸入 SHOW MASTER STATUS 找出資訊;
MASTER_LOG_FILE = 'master bin_log filename',
MASTER_LOG_POS = 'log position';

-- 確認 slave狀態 SHOW SLAVE STATUS; 會很醜
-- Slave_IO_Running: Yes
-- Slave_SQL_Running: Yes
SHOW SLAVE STATUS\G
-- 執行slave
START SLAVE;