# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/3/13 15:19
@description
"""

from kubernetes import client, config
from urllib3.exceptions import InsecureRequestWarning

# 禁用 SSL 校验警告
client.configuration.verify_ssl = False
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)

# 使用 kubeconfig 文件加载 Kubernetes 配置
config.load_kube_config()

# 创建 Kubernetes API 的核心 V1Api 对象
v1 = client.CoreV1Api()

# 列出集群中的所有命名空间
print("命名空间列表:")
namespace_list = v1.list_namespace()
for namespace in namespace_list.items:
    print(namespace.metadata.name)
