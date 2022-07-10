# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/3 9:54
@description  Faker模块：生成测试数据

pip install Faker -i https://pypi.tuna.tsinghua.edu.cn/simple/

批量生成数据
https://gongchuangcloud.com/home/gene
https://tools.kalvinbg.cn/dev/randomdata
"""

from faker import Faker
import pandas as pd

fake = Faker(["zh_CN"])
Faker.seed(0)


def phone_number():
    phone_number = fake.phone_number()  # 手机号码
    id_card = fake.ssn()  # 随机生成身份证号(18位)
    print(phone_number, id_card)


def get_data():
    key_list = ["姓名", "详细地址", "所在省份", "手机号", "身份证号", "出生年月", "邮箱"]
    name = fake.name()
    address = fake.address()
    province = address[:3]
    number = fake.phone_number()
    id_card = fake.ssn()
    birth_date = id_card[6:14]
    email = fake.email()
    info_list = [name, address, province, number, id_card, birth_date, email]
    person_info = dict(zip(key_list, info_list))
    return person_info


def to_excel():
    df = pd.DataFrame(columns=["姓名", "详细地址", "所在省份", "手机号", "身份证号", "出生年月", "邮箱"])
    for i in range(5):
        person_info = [get_data()]
        df1 = pd.DataFrame(person_info)
        df = pd.concat([df, df1])
    df.to_excel("../../../../file/xlsx/模拟数据.xlsx", index=None)


def save_to_excel(file_path, n):
    fake = Faker(locale='zh_CN')
    res = []
    for i in range(n):
        name = fake.name()
        phone = fake.phone_number()
        id_card = fake.ssn()

        res.append(
            [name, phone, id_card, fake.company(), fake.address(), fake.credit_card_number(), fake.job(), fake.email()])

    # list转dataFrame
    df = pd.DataFrame(data=res, columns=['name', 'phone', 'id_card', 'comp', 'addr', 'bank_card', 'title', 'email'])
    print(df)
    # 保存到本地excel
    df.to_excel(file_path, index=False)


def save_to_excel2(file_path):
    from faker import Faker
    from faker_pandas import PandasProvider

    fake = Faker()
    fake.add_provider(PandasProvider)

    colgen = fake.pandas_column_generator()

    df2 = fake.pandas_dataframe(
        colgen.first_name('First Name', empty_value='', empty_ratio=.5),
        colgen.last_name('Last Name'),
        colgen.pandas_int('Age', 18, 80, empty_ratio=.2),
        rows=7
    )

    print(df2)
    df2.to_excel(file_path, index=False)


if __name__ == '__main__':
    # phone_number()
    # to_excel()
    # save_to_excel("../../../../file/xlsx/模拟数据.xlsx", 5)
    save_to_excel2("../../../../file/xlsx/模拟数据.xlsx")

