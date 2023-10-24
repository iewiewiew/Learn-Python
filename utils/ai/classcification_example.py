# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/11/15 14:34
@description  图片分类

streamlit官网：https://streamlit.io/
pip install streamlit
pip install torch torchvision
streamlit run classcification_app.py
"""

import streamlit as st
import torch
import torchvision.models as models
from PIL import Image

weights = models.VGG16_Weights.DEFAULT
img_preprocess = weights.transforms()
categories = weights.meta["categories"]


@st.cache_resource
def get_model():
    model = models.vgg16(weights='IMAGENET1K_V1')
    model.eval()
    return model


model = get_model()


def make_prediction(img):
    img_processed = img_preprocess(img)
    prediction = model(img_processed.unsqueeze(0))
    index = torch.argmax(prediction, 1)
    return  categories[index]


# Dashboard
st.title("图片分类")  # 设置标题
upload = st.file_uploader(label="上传图片", type=["png", "jpg", "jpeg"])  # 上传文件
if upload:
    img = Image.open(upload)
    st.image(img)
    prediction = make_prediction(img)
    st.header("预测概率")
    st.write(prediction)  # 写入各种东西，文字、表格、图片