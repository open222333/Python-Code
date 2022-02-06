workers = 5  # 定義同時間開啟的處理請求的程序數量，根據網站流量調整
worker_class = "gevent"  # 採用gevent庫，支援非同步處理請求
bind = "0.0.0.0:5000"
