# !/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import download_file
from jmeter_report import json_to_excel, extract_data_from_jmx, save_report, merge_excel_files, merge_report

"""
@author       weimenghua
@time         2024/1/12 10:20
@description
"""

if __name__ == '__main__':
    # array = ["Conda", "Nuget", "Dart", "Golang", "Maven", "Npm", "Packagist", "Pypi", "RubyGems", "Rust", "SBT", "system", "file", 'email']
    array = ["Conda"]
    # array = ["aa", "bb"]

    base_path = '/Users/menghuawei/PycharmProjects/Learn-Python/.gitee/tmp/'  # 本地环境
    # base_path = '/root/gitee-pref-mirrors/'                        # 服务器
    # base_path = '/home/git/gitee-pref-mirrors/'                    # 服务器

    try:
        """statistics.json 转换成 statistics.xlsx"""
        json_to_excel(base_path, array)

        """读取 JMX 获取交易和 URL 写入 CSV"""
        extract_data_from_jmx(base_path, array)

        """合并 Excel 和 CSV 生成单个报告"""
        save_report(base_path, array)

        """合并多个 Execl 生成最终测试报告"""
        merge_excel_files(base_path, array)

        """合并两个报告"""
        command = f'python generate_mirrors_report.py --template result/镜像统计周报模板.xlsx'
        subprocess.call(command, shell=True)
        merge_report(base_path)
    except Exception as e:
        print('发生异常: ', str(e))
    download_file.app.run(host='0.0.0.0', port=8888)
