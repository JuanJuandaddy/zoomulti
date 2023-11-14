
import math
import asyncio
import re

from gevent import monkey;monkey.patch_all()
from gevent import spawn
from scapy.all import *
from multiprocessing import  Process
import sys
from scapy.layers.inet import IP
# 构造IP请求包
factor=50
f=re.search(r'\d+',get_if_list()[1]).group()
speed=math.ceil(int(sys.argv[1])/factor)
packet=IP(dst=f'192.168.{int(list(f)[0])-1}.4')

async def send_arp_request():
    while True:
        ip_request = [packet for _ in range(speed)]
        sendp(ip_request, iface=f"h{f}-eth0")
        await asyncio.sleep(0)  # 控制发送速率，可根据实际需求调整

async def main():
    tasks = [asyncio.create_task(send_arp_request()) for _ in range(3)]

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
