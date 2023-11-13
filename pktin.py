import math
import re
import asyncio
import random
import random
from gevent import monkey;monkey.patch_all()
from gevent import spawn
from scapy.all import *
import time
import sys
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether, ARP

import settings
import threading
from threading import currentThread
import subprocess

'''def ping_host(host):

    ping_cmd = f"hping3 -c {settings.HPING3_NUM_ONCE_TIME} {host}"

    result = subprocess.getstatusoutput(ping_cmd)

    print(result)

def ping(mode):
    prefix = settings.BLACKHOLE_PKTIN_IP_STYLE #192.168.100

    hosts = []

    if mode == 0:
        # 正常测试

        hosts.extend([prefix +'.'+ str(i) for i in range(1, numpy.random.randint(5, settings.NORMAL_PKTIN_RANGE))])

    if mode == 1:
        # 压力测试

        hosts.extend([prefix +'.'+str(i) for i in range(10, 250)])  # 开启多个250+个协程

    greenlets = [gevent.spawn(ping_host, host) for host in hosts]

    gevent.joinall(greenlets)


if __name__ == '__main__':

    mode=None

    try:
        if sys.argv[1]:
            mode = 1
    except IndexError as e:

        mode = 0

    thread_num=settings.PKTIN_THREAD_NUM

    for _ in range(thread_num):

        t = threading.Thread(target=ping, args=(mode,))

        t.start()'''

'''async def ping_host(host):
    process = await asyncio.create_subprocess_shell(
        f'hping3 -c 10 {host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # stdout, stderr = await process.communicate()
    # print(f'Ping result for {host}:')
    # print(stdout.decode())

async def run_ping_tasks(index,mode):
    PREFIXS = settings.BLACKHOLE_PKTIN_IP_STYLE  # 192.168.xxx

    hosts = []

    if mode == 0:
        # 正常测试

        hosts.extend([PREFIXS[index] + '.' + str(i) for i in range(1, numpy.random.randint(5, settings.NORMAL_PKTIN_RANGE))])

    if mode == 1:
        # 压力测试

        hosts.extend([PREFIXS[index] + '.' + str(i) for i in range(1, 250)])
        #hosts.extend([PREFIXS[index+1] + '.' + str(i) for i in range(1, 250)])# 开启多个250+个协程

    tasks = [asyncio.create_task(ping_host(host)) for host in hosts]

    await asyncio.wait(tasks)

def run(index,mode):

    print(currentThread().ident)
    asyncio.run(run_ping_tasks(index,mode))

if __name__ == '__main__':

    mode = None

    try:

        if sys.argv[1]:

            mode = 1

    except IndexError as e:

        mode = 0

    thread_num = settings.PKTIN_THREAD_NUM

    threads = []

    for thread_index in range(thread_num):

        thread = threading.Thread(target=run,args=(thread_index,mode,))

        thread.start()

        threads.append(thread)

    for thread in threads:

        thread.join()#阻塞主进程
'''

# 构造IP请求包
f=sys.argv[1] # 1101... 1203...1602...
# def run(id):
#
#     while 1:
#         # 发送ARP请求包
#         ip_request = IP(dst=f'192.168.{int(list(f)[0])-1}.4')
#
#         sendp(ip_request, iface=f"h{f}-eth0")
#
# if __name__ == '__main__':
#     #ping单个地址： 1 30pkts/s  5 130pkts/s  10 = 250 pkts/s  15 350pkts/s
#     threads=[]
#     thread_num=math.ceil(pkts_speed/TRANSFORM_FACTOR)
#     id = random.randint(1, EACH_SW_HOSTS_NUM + 1)
#     if thread_num==0:
#         sys.exit(0)
#     for i in range(thread_num):
#         t=threading.Thread(target=run,args=(id,))
#         t.start()
#         threads.append(t)
#     for th in threads:
#         th.join()

async def send_arp_request():
    while True:
        ip_request = [IP(dst=f'192.168.{int(list(f)[0])-1}.4') for _ in range(10)]
        sendp(ip_request, iface=f"h{f}-eth0")
        await asyncio.sleep(0)  # 控制发送速率，可根据实际需求调整

async def main():
    tasks = []
    tasks.append(asyncio.create_task(send_arp_request()))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
