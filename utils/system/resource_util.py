# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/22 08:29
@description  检测当前环境CPU和内存、磁盘等信息状态
"""

import psutil


def check_cpu_memory():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    print("当前CUP使用率：{}  内存使用率：{}".format(cpu_usage, memory_usage))

    if cpu_usage > 90 or memory_usage > 90:
        print("CPU或内存使用率过高:")
        for process in psutil.process_iter(['pid', 'name']):
            process_info = process.as_dict(attrs=['pid', 'name', 'cpu_percent'])
            if process_info['cpu_percent'] > 0:
                print(f"进程ID: {process_info['pid']}, 进程名称: {process_info['name']}")
    else:
        print("CPU和内存使用率正常.")


def check_disk_usage():
    partitions = psutil.disk_partitions()
    print("当前磁盘使用率：{}".format(partitions))

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        if usage.percent > 90:
            print(f"磁盘使用率过高: {partition.device}")
        else:
            print(f"磁盘使用率正常: {partition.device}")


def check_disk_io():
    disk_io = psutil.disk_io_counters()

    if disk_io.read_count > 0 or disk_io.write_count > 0:
        print("磁盘IO活动已检测到.")
        print(f"读取次数: {disk_io.read_count}, 写入次数: {disk_io.write_count}")
    else:
        print("没有磁盘IO活动.")


def check_process_count():
    process_count = len(psutil.pids())

    if process_count > 1000:
        print(f"进程数量过高: {process_count}")
    else:
        print(f"进程数量正常: {process_count}")


def print_top_like():
    # 获取系统的 CPU 核心数
    cpu_count = psutil.cpu_count()

    while True:
        # 获取所有进程的 CPU 使用率
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                cpu_percent = proc.info['cpu_percent']
                if cpu_percent is not None:
                    processes.append((proc.pid, proc.info['name'], proc.info['cpu_percent']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # 按 CPU 使用率进行排序
        processes.sort(key=lambda x: x[2], reverse=True)

        # 清空控制台
        print("\033c", end="")

        # 打印进程信息
        print(f"{'PID':<10s} {'NAME':<30s} {'CPU %':<10s}")
        print("-" * 50)
        for pid, name, cpu_percent in processes[:10]:
            print(f"{pid:<10d} {name:<30s} {cpu_percent:<10.2f}%")

        # 打印 CPU 核心数
        print("\n" + "-" * 50)
        print(f"CPU Cores: {cpu_count}\n")

        # 等待一段时间后再刷新信息
        psutil.cpu_percent(interval=10)


if __name__ == "__main__":
    # check_cpu_memory()
    # check_disk_usage()
    # check_disk_io()
    # check_process_count()
    print_top_like()
