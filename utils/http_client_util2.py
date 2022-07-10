# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/22 16:41
@description  HTTP 请求工具类 注：未调试成功
"""

import http.client


class HttpClient:
    def __init__(self, host):
        self.host = host
        self.cookie = None

    def request(self, method, path, body=None, headers=None):
        conn = http.client.HTTPConnection(self.host)
        headers = headers or {}
        if self.cookie:
            headers['Cookie'] = self.cookie

        # 添加Content-Type到请求标头
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        conn.request(method, path, body, headers)
        response = conn.getresponse()

        # 保存返回的Cookie
        if 'Set-Cookie' in response.headers:
            self.cookie = response.headers['Set-Cookie']

        return response

    def get(self, path, headers=None):
        response = self.request('GET', path, headers=headers)
        return response

    def post(self, path, body=None, headers=None):
        response = self.request('POST', path, body, headers)
        return response

    def put(self, path, body=None, headers=None):
        response = self.request('PUT', path, body, headers)
        return response

    def delete(self, path, headers=None):
        response = self.request('DELETE', path, headers=headers)
        return response


if __name__ == '__main__':
    client = HttpClient("www.demo.com")

    client.cookie = "sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; oschina_new_user=false; remote_way=http; user_locale=zh-CN; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2258836%22%2C%22first_id%22%3A%2218abaa7d1f29a3-00b1523e3a033b1-18525634-3686400-18abaa7d1f310bc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhNmQ4OTI1NmJkYTItMDQyZTM2YTQzNDg4ZDA4LTE5NTI1NjM0LTIwNzM2MDAtMThhNmQ4OTI1NmMxZTg4IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiNTg4MzYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2258836%22%7D%2C%22%24device_id%22%3A%22189f6fdbf86f18-0ab090f618dcd-1a525634-2073600-189f6fdbf871c5f%22%7D; gitee-session-n=cWMzUk5FdS8zNElTWGNYMEFjMXlvSFMzY2cvTE5UTGFNdHU2ZEtZMlFhandoaDFoejFQY1R3ZlVlVHhlK0VJQjl5K2tIcWU0ZXBCN1JmaWhaZTFMN2V4MlpOWmhxczArQUxFQitNTnhCWUpybzVxenVsOUtvSFd0M3lFRWxBcW0vcDBwcldlRUwxMExQQ3haWVZiYVFXUUZqZXpwS1lYTjY0UzAvVmxORHdFNUpodkNJcWpoSmlGNkFnMVZtMkhHSy9Ib1RvNllydURLcWFzcTJIdzNneElQZGN4S1o1cEorMXlNVXozUHovRXdiYmRTU1ZvMmRyNUpLZlhzejEyako3dzV0bk5iNVFzTW41cEdMUGlZR1ZObEs0Sll0ZC9zRU9ycGgwQUZtc3B0K1lacTEvbS8xZEV0K1oyL2RnbVNDdEl4bkNad1gvQ0ZCTzRCenkySkwxeC9KbHVTdEduZmFhcWR5M0lzWUNnbCtYVWx1eE13OEp0OGdrSUNKZ1JWTkdjMEVlOFVINXdTYit2UXZlR3hVeHEvWEk2VGNxSWY0bWszUE5GU2lNRy9ncGJuNU85ektKanIyUjE5OExvSkhacUpzSFh3Z2MwblY1MkZZUzZLOHl2K0xuS1FOYWsyVmVmNzlsb25nbzl2Nnp5SGNwUzVHZHY4R2QvM3JNZTE5dTlYaWpDQ21XNEdweFVQWVlkU2l5eThxMzZsSm95cC9TdkNPOVFYV3RzZ2dTSVFYMVA2Zk9xMThOcUhCSXZZSDZOdXRmT2p6bWNDTmdFM2tadE5CTzRkSy9ZS1JGV2EvR1FpNjUwZi9uZXphcjQxT1Avd0xaMUtsZ3MzdkF6Ry0tQXFUS0M1UGNIS1JqL3o5enhjb2hvZz09--2df6d61912241219c4f6ecf193823a8ac7c5fcdd"

    """获取仓库列表"""
    path = '/enterprises/2110017/projects?page=1&per_page=20&offset=0'
    response_data = client.get(path).read().decode('utf-8')
    print(response_data)
