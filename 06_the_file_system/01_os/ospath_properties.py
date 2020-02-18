import os.path
import time

'''获取文件信息
'''

print(f"File          : {__file__}")
print(f"Access time   : {time.ctime(os.path.getatime(__file__))}")
print(f"Modified time : {time.ctime(os.path.getmtime(__file__))}")
print(f"Change time   : {time.ctime(os.path.getctime(__file__))}")
print(f"Size          : {os.path.getsize(__file__)}")