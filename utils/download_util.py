# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/8 11:32
@description
"""

import requests


def download_file(url, save_path):
    response = requests.get(url, stream=True)  # 指定 stream=True 参数来启用流式传输模式
    response.raise_for_status()  # 用于检查发送的 HTTP 请求的响应状态码，并在出现错误时引发相应的异常

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):  # chunk_size 参数指定每个数据块的大小（以字节为单位）
            file.write(chunk)


def download_file2(url, save_path):
    headers = {
        "Content-Type": "application/json",
        "Cookie": "alpha-enable=5; close_wechat_tour=true; oschina_new_user=false; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; Hm_lvt_24f17767262929947cc3631f99bfd274=1693448762,1695034941,1695612484; user_locale=zh-CN; remember_user_token=BAhbCFsGaQPaWiNJIiIkMmEkMTAkVVR1N0tiS1g4TTNLOXNVdXpBYzdEZQY6BkVUSSIXMTY5NjY0NDEwNS44MTk3OTUxBjsARg%3D%3D--b5075d1f70119e16b7e82ad8f86ccf6e2565a5a9; BEC=1f1759df3ccd099821dcf0da6feb0357; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222317018%22%2C%22first_id%22%3A%2218b07de78e7104d-062ef7ec55af3b4-18525634-1484784-18b07de78e829b7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22sem%22%2C%22%24latest_utm_campaign%22%3A%22enterprise%22%2C%22%24latest_utm_content%22%3A%22competition%22%2C%22%24latest_utm_term%22%3A%22%25D7%25D4%25B6%25AF%25B6%25A8%25CF%25F2%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3ZWYyZGVkYzUzMDYtMDFmNTY1MTBjOTI1ZGIxLTFkNTI1NjM0LTE0ODQ3ODQtMTg3ZWYyZGVkYzYxZmI5IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjMxNzAxOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222317018%22%7D%2C%22%24device_id%22%3A%22187ef2dedc5306-01f56510c925db1-1d525634-1484784-187ef2dedc61fb9%22%7D; csrf_token=JqT9nDyhg30TvIAEtmUs%2Frncjq7VYY8EbgAVs8FGJJ%2BU3Rt95gcWKt5%2BSuc81AUHo9BsR7nG108JE%2FnYW9d6CA%3D%3D; gitee-session-n=N254QjcvVDNlMjFhVUpiYStVVnpkMk41c2RWZnBHOUhjUm1pUFhYSHB1aDNqVXJiMDlEaVo2dGphcGpPUXN4dHgybk1DV2IvdnFRMGhITkU0ckFrNThYdUdiRHpqUHZvaTFJOUd4VWxwQWd1WUxUYzU1a1ZTcFJOYzlzSmZpRm1wVnlLWVRhNHpQbWhPNHJySHlIWWxRbjJDcTJYYlJXWjdrcU9ocXdkMmRxVTF5VXNkbGNMQW1CQmRURGtMV2VGdlFQMkNaYkRxcmhsN2NrQXg3YXJla2twSytrM3JDaytYUWZ3Ty9BQTdiTldqZVlwRVVmTXZhdEJ2VlcxdW0rbUZWWnMyTCtpOUVhS0gvS3h6WXlqaTZ6VGdxVnIvKzQwKzM1cFdtcndPSEQzRndScFVwUlNiTmtNUjNLZThYaVdtVWoyNUo3bXl1d0ZjUm85bDRiQ0V3VHFJTDJFSG9xcE92bTFDMUZYZmJiLzFwSWQ4U1A0cEI2YkFVZ21nOXRUVWoyOEVyaUNVV1dKYlUyVytxdm5OcUVFa2grTDJSWjNuYk1YWTFBQllTTHdUSGk0NEpzd0JLazRyU2lKS09oVjMyVGF4ZTlRYUc2YUJld3Q2QUpndFR4dWptUXFVOHlOUmdqNFZiWUJIcVdSeWd3N3hob2t2a3BCV3hNeUNxd09QZlFVZlFncTg4ckVVMDFXUmxGSS9xaUNsbWErV2U3KzVxTzNiRzBIQXE2NG92Y1pwTkY0ai90OWtFUE5NWnhvZVhHV2gwb3dUUkUwV1NxeHBybmthTWtGZ0VoMnBDSXRsanAvKzBlbHFEbmt1MWN3d0JVbDd1WDRDSVF3QTQxRkxXOGlKVzdGYktPOXo0clpTRlgwMDZqOEhwdjdkS1ZHcjJQYnlBMnovM0U9LS15cStBSWlaWkp6cE41bmRDL09Xa0tRPT0%3D--d5b30b9fe05b36cb658002b81f858fdcbd6769ed"
    }
    data = '''{"ref": "master", "file_format": "zip"}'''  # JSON 数据需要加 '''

    response = requests.post(url, headers=headers, data=data, stream=True)

    if response.status_code == 201:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)  # 下载地址重定向了
        print("文件下载完成")
    else:
        print("文件下载失败")


if __name__ == '__main__':
    # url = 'http://gitee.com/api/v5/repos/hightest/wei-demo-001/tarball?access_token=99d49b62b4f51c39b4bd65be3f22d52f'  # 文件的 URL
    save_path = '../.tmp/gitee/repo/master.zip'  # 要保存的文件路径
    # save_path = '../.tmp/gitee/repo/master.tar.gz'  # 要保存的文件路径
    url = "https://api.gitee.com/enterprises/2095951/projects/29714570/repository/download"  # 替换为实际的下载链接

    # download_file(url, save_path)
    download_file2(url, save_path)
