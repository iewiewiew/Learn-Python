# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/4/5 22:36
@description  处理 JMeter 测试报告
"""

import json
import os
import time
from typing import Union, Any
import pandas as pd
from pandas import Series, DataFrame
from pandas._typing import NDFrameT


def json_to_excel(base_path, threads, jmxs):
    """statistics.json 转换成 statistics.xlsx"""

    for thread in threads:
        try:
            for jmx_path in jmxs:
                file_path = base_path + thread + "/" + jmx_path + "/"
                with open(file_path + "statistics.json", "r") as file:
                    json_data = json.load(file)
                    # index = list(json_data.keys()).index("Total")

                # 转换为 DataFrame
                df = pd.DataFrame.from_dict(json_data, orient="index")

                # 将小数四舍五入
                df = df.round(2)

                custom_header = ["事务", "并发数", "样本计数", "错误计数", "错误百分比", "平均响应时间", "最小响应时间", "最大响应时间", "中位数响应时间", "百分之九十响应时间", "百分之九十五响应时间", "百分九十九响应时间", "吞吐量", "接收字节速率", "发送字节速率"]

                # 指定字段顺序
                desired_columns = ["transaction", "并发数", "sampleCount", "errorCount", "errorPct", "meanResTime", "minResTime", "maxResTime", "medianResTime", "pct1ResTime", "pct2ResTime", "pct3ResTime", "throughput", "receivedKBytesPerSec", "sentKBytesPerSec"]

                # 重新排序列顺序
                df = df.reindex(columns=desired_columns)

                # 将 "Total" 移动到第二行
                df = df.reindex(["Total"] + [col for col in df.index if col != "Total"])

                # 设置新列的值为 40/5min 60/5min 80/5min
                if thread == "40load":
                    df["并发数"] = "40/5min"
                elif thread == "60load":
                    df["并发数"] = "60/5min"
                elif thread == "80load":
                    df["并发数"] = "80/5min"
                else:
                    df["并发数"] = thread

                file_path = base_path + thread + "/" + jmx_path + "/statistics.xlsx"
                # 将 DataFrame 写入 Excel 文件
                df.to_excel(file_path, index=False, header=custom_header)
                print("生成 statistics.xlsx: " + file_path)
        except Exception as e:
            print("生成 statistics.xlsx: ", e)


def merge_excel_files(base_path, threads, jmxs):
    for thread in threads:
        """合并多个 statistics.xlsx 为 merged_report.xlsx"""
        merged_data = pd.DataFrame()

        try:
            for jmx_path in jmxs:
                file_path = base_path + thread + "/" + jmx_path + "/"
                data = pd.read_excel(file_path + "/statistics.xlsx")
                merged_data = merged_data.append(data, ignore_index=True)
        except Exception as e:
            print("读取 statistics.xlsx：", e)

        try:
            merged_data: Union[Union[Series, DataFrame, NDFrameT, None], Any] = merged_data[~merged_data.iloc[:, 0].astype(str).str.startswith(("Total", "cp", "add", "rm", "commit", "1", "文", "根据"))]
        except Exception as e:
            print(e)

        output_file_path = base_path + thread + "/merged_report.xlsx"

        try:
            merged_data.to_excel(output_file_path, index=False)
            print("生成 merged_report.xlsx：", output_file_path)
        except Exception as e:
            print("生成 merged_report.xlsx：", output_file_path, e)


def final_report(base_path, threads, jmxs, directory_name):
    """合并多个 merged_report.xlsx 为 final_merged_report.xlsx"""

    threads.sort()
    jmxs_index = {value: index for index, value in enumerate(jmxs)}  # 创建一个字典，用于存储事务在jmxs中的索引

    merged_data = pd.DataFrame()
    try:
        for thread in threads:
            file_path = base_path + thread + "/merged_report.xlsx"
            data = pd.read_excel(file_path)
            merged_data = merged_data.append(data, ignore_index=True)
    except Exception as e:
        print("读取 merged_report.xlsx：", e)

    output_file_path = base_path + "负载测试报告" + '_{}'.format(time.strftime("%Y%m%d", time.localtime())) + '_' + directory_name + '.xlsx'

    try:
        merged_data["事务索引"] = merged_data["事务"].map(jmxs_index)     # 添加一个辅助列，存储事务在jmxs中的索引
        merged_data.sort_values(by=["事务索引", "并发数"], inplace=True)  # 根据事务索引和并发数进行排序
        merged_data.drop(columns="事务索引", inplace=True)               # 删除辅助列

        merged_data.to_excel(output_file_path, index=False)
        print("生成 final_merged_report.xlsx：", output_file_path)
    except Exception as e:
        print("生成 final_merged_report.xlsx：", e)


if __name__ == "__main__":
    base_path = "/Users/menghuawei/PycharmProjects/my-project/Learn-Python/.gitee/tmp/20240408090003/"

    # threads = ["base"]
    threads = ["40load", "60load", "80load"]

    # jmxs = ["ssh_push_new_10", "企业代码仓库列表"]

    # 单交易基准
    # jmxs = ["http_clone_100m", "http_clone_300m", "http_clone_900m", "ssh_clone_100m", "ssh_clone_300m", "ssh_clone_900m", "http_pull_single_10", "http_pull_single_50", "http_pull_single_100", "ssh_pull_single_10", "ssh_pull_single_50", "ssh_pull_single_100", "http_push_new_10", "http_push_new_50", "http_push_new_100", "ssh_push_new_10", "ssh_push_new_50", "ssh_push_new_100", "企业代码仓库列表", "企业工作项列表", "企业工作项详情", "企业项目列表", "企业成员列表", "企业仓库_仓库分支列表", "企业仓库_仓库标签列表", "企业仓库_仓库发行版列表", "企业仓库_commit列表", "企业仓库_单个commit差异文件", "企业仓库_基于master分支下新建仓库文件", "代码评审_新建代码评审", "代码评审_开启状态列表", "代码评审_详情页", "代码评审_commits列表", "代码评审_diff文件列表", "代码评审_评论列表", "代码评审_新建评论"]

    # 单交易负载
    jmxs = ["http_clone_100m", "http_clone_300m", "ssh_clone_100m", "ssh_clone_300m", "http_pull_single_10", "http_pull_single_50", "ssh_pull_single_10", "ssh_pull_single_50", "http_push_new_10", "http_push_new_50", "ssh_push_new_10", "ssh_push_new_50", "企业代码仓库列表", "企业工作项列表", "企业工作项详情", "企业项目列表", "企业仓库_仓库分支列表", "企业仓库_仓库标签列表", "企业仓库_commit列表", "企业仓库_单个commit差异文件", "代码评审_开启状态列表", "代码评审_详情页", "代码评审_commits列表", "代码评审_diff文件列表", "代码评审_评论列表"]

    directory_name = os.path.basename(os.path.normpath(base_path))

    json_to_excel(base_path, threads, jmxs)
    merge_excel_files(base_path, threads, jmxs)
    final_report(base_path, threads, jmxs, directory_name)
