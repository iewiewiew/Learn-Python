# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/5 13:44
@description  数据库备份 注：未实践成功
"""

import os
import datetime
import subprocess

# 数据库备份目录
BACKUP_DIR = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/'
# 备份文件保留周期（天）
RETENTION_PERIOD = 7


# 备份数据库
def backup_database():
    current_time = datetime.datetime.now()
    backup_file = f"backup_{current_time.strftime('%Y%m%d%H%M%S')}.sql"
    backup_path = os.path.join(BACKUP_DIR, backup_file)

    # 使用 subprocess 模块执行数据库备份命令：mysqldump -uroot -proot --all-databases > backup_20230921182716.sql
    backup_command = [
        'mysqldump',
        '-u',
        'root',
        '-p',
        'root',
        '--all-databases',
        "--result-file=" + backup_path
    ]

    subprocess.run(backup_command, check=True)

    # with open(backup_path, 'w') as backup_file:
    #     subprocess.run(backup_command, stdout=backup_file, check=True)

    print(f"数据库备份已完成，备份文件保存为: {backup_path}")


# 清理过期备份文件
def cleanup_backup():
    current_time = datetime.datetime.now()
    cutoff_time = current_time - datetime.timedelta(days=RETENTION_PERIOD)

    for file in os.listdir(BACKUP_DIR):
        file_path = os.path.join(BACKUP_DIR, file)
        if os.path.isfile(file_path):
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_time < cutoff_time:
                os.remove(file_path)
                print(f"过期备份文件已删除: {file_path}")


# 恢复数据库
def restore_database(backup_file, restore_time):
    backup_path = os.path.join(BACKUP_DIR, backup_file)

    # 使用 subprocess 模块执行数据库恢复命令
    restore_command = [
        'mysql',
        '-u',
        'username',
        '-p',
        'password'
    ]
    with open(backup_path, 'r') as backup_file:
        subprocess.run(restore_command, stdin=backup_file)

    print(f"数据库已成功恢复到时间点: {restore_time}")


# 主函数
def main():
    # 执行数据库备份
    backup_database()

    # 清理过期备份文件
    # cleanup_backup()

    # 恢复数据库到指定时间点
    # restore_database('backup_20220101120000.sql', '2022-01-01 12:00:00')


if __name__ == '__main__':
    main()
