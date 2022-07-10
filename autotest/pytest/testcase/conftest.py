# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/7 16:41
@description  Git + Gitee 通用操作
"""

import os
import git
import pytest
import shutil
from autotest.pytest.utils.config_util import read_yaml
from autotest.pytest.utils.randomutil import RandomGenerator


# 随机数
rg = RandomGenerator()
# 读取配置
data = read_yaml('../config/config-git.yml')


@pytest.fixture
def clone_repo(request):
    """ 克隆仓库 """

    if not os.path.exists(data['param']['repo_dir']):
        os.makedirs(data['param']['repo_dir'])

    global new_repo_dir
    new_repo_dir = data['param']['repo_dir'] + data['param']['repo_name'] + rg.formatted_time()
    if request.param == 'ssh':
        # SSH 克隆仓库
        repo = git.Repo.clone_from(data['param']['git_repo_url'], new_repo_dir)
    elif request.param == 'https':
        # HTTPS 克隆仓库
        repo = git.Repo.clone_from(data['param']['https_repo_url'], new_repo_dir)
    elif request.param == 'depth_https':
        # HTTPS 浅克隆仓库
        repo = git.Repo.clone_from(data['param']['https_repo_url'], new_repo_dir, depth=1)
    else:
        # HTTPS 克隆仓库(默认)
        repo = git.Repo.clone_from(data['param']['https_repo_url'], new_repo_dir)
    return repo


@pytest.fixture
def init_repo():
    """ 创建本地仓库对象 """
    # 判断本地仓库是否存在，如不存在则克隆仓库，并创建本地仓库对象
    if os.path.exists(data['param']['repo_dir'] + data['param']['repo_name']):
        return git.Repo(data['param']['repo_dir'] + data['param']['repo_name'])
    else:
        # os.makedirs(data['param']['repo_dir'])
        git.Repo.clone_from(data['param']['https_repo_url'], data['param']['repo_dir'] + data['param']['repo_name'])
    return git.Repo(data['param']['repo_dir'] + data['param']['repo_name'])


@pytest.fixture()
def commit_file(init_repo):
    """ 修改文件并 commit """
    # 覆盖写入 README.md 并 commit
    with open(init_repo.working_dir + '/README.md', 'w') as f:
        f.write('Hello Git ' + rg.formatted_time() + '\n')
    init_repo.index.add(['README.md'])
    init_repo.index.commit('Hello Git ' + rg.formatted_time())


@pytest.fixture()
def test_pre_push_branch(env):
    """ 前置数据准备操作 todo：待调整 """
    repo_path = data['param']['repo_dir'] + rg.formatted_time()
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)

    """ 创建本地仓库对象 """
    init_repo = git.Repo.clone_from(data['param']['https_repo_url'], data['param']['repo_dir'] + rg.formatted_time())

    """ 修改文件并 commit """
    with open(init_repo.working_dir + '/README.md', 'w') as f:
        f.write('Hello Git ' + rg.formatted_time() + '\n')
    init_repo.index.add(['README.md'])
    init_repo.index.commit('Hello Git ' + rg.formatted_time())
    init_repo.remote('origin').push()
    assert 'README.md' in init_repo.head.commit.tree or len(init_repo.index.diff(None)) == 0

    # 推送标签 v1.0.0 到远程
    if 'v1.0.0' not in init_repo.remote('origin').repo.tags:
        init_repo.remote('origin').push(init_repo.create_tag('v1.0.0', message='test push tag'))

    """ 清理数据 """
    shutil.rmtree(repo_path)
