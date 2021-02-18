

bind = '0.0.0.0:5000' # 可以更改server ip 跟port號
worker_class = 'sync'
workers = 4   # 調越高越多工同時處理repuest, 最高值建議    CPU核心數*2+1
timeout = 60

# gunicorn -c unicorn.py eleflask:app