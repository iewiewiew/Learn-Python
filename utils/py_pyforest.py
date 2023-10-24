# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/27 17:32
@description  自动导入代码中使用到的Python库

pip install pyforest -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

import pyforest


def demo():
    list_ = [n for n in dir(pyforest)]

    print(f'python内置库的总数是：{str(len(list_))}')
    # python内置库的总数是：105

    print(list_)


if __name__ == '__main__':
    demo()
    """
    ['ARIMA', 'CountVectorizer', 'ElasticNet', 'ElasticNetCV', 'GradientBoostingClassifier', 'GradientBoostingRegressor', 'GridSearchCV', 'Image', 'KFold', 'KMeans', 'LabelEncoder', 'Lasso', 'LassoCV', 'LazyImport', 'LinearRegression', 'LogisticRegression', 'MinMaxScaler', 'OneHotEncoder', 'PCA', 'Path', 'PolynomialFeatures', 'Prophet', 'RandomForestClassifier', 'RandomForestRegressor', 'RandomizedSearchCV', 'Ridge', 'RidgeCV', 'RobustScaler', 'SimpleImputer', 'SparkContext', 'StandardScaler', 'StratifiedKFold', 'TSNE', 'TfidfVectorizer', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_importable', '_imports', '_jupyter_labextension_paths', '_jupyter_nbextension_paths', 'active_imports', 'alt', 'bokeh', 'cross_val_score', 'cv2', 'dash', 'dd', 'dt', 'fastai', 'fbprophet', 'gensim', 'get_user_symbols', 'glob', 'go', 'import_symbol', 'imutils', 'install_extensions', 'install_labextension', 'install_nbextension', 'keras', 'lazy_imports', 'lgb', 'load_workbook', 'metrics', 'mpl', 'nltk', 'np', 'open_workbook', 'os', 'pd', 'pickle', 'plt', 'px', 'py', 'pydot', 'pyforest_imports', 're', 'sg', 'skimage', 'sklearn', 'sm', 'sns', 'spacy', 'statistics', 'stats', 'svm', 'sys', 'textblob', 'tf', 'torch', 'tqdm', 'train_test_split', 'user_specific_imports', 'user_symbols', 'utils', 'wr', 'xgb']
    """
