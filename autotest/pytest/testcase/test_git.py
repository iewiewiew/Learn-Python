# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/3/25 17:08
@description  Git + Gitee 测试用例
"""


import os
import shutil
import allure
import pytest
import logging
from autotest.pytest.utils.randomutil import RandomGenerator
from autotest.pytest.utils.config_util import read_yaml

# 随机数
rg = RandomGenerator()
# 读取配置
data = read_yaml('../config/config-git.yml')


@allure.feature('Git 操作')
class TestGit:
    # @pytest.mark.skip(reason='跳过此条用例，暂未解决公私密钥问题')
    @pytest.mark.parametrize('clone_repo', ['ssh'], indirect=True)
    @allure.story('仓库操作')
    @allure.testcase('SSH 克隆仓库')
    def test_clone_ssh_repo(self, clone_repo):
        assert os.path.exists(clone_repo.working_tree_dir)
        shutil.rmtree(clone_repo.working_tree_dir)

    @pytest.mark.parametrize('clone_repo', ['https'], indirect=True)
    @allure.story('仓库操作')
    @allure.testcase('HTTPS 克隆仓库')
    def test_clone_https_repo(self, clone_repo):
        assert os.path.exists(clone_repo.working_tree_dir)
        shutil.rmtree(clone_repo.working_tree_dir)

    @pytest.mark.parametrize('clone_repo', ['depth_https'], indirect=True)
    @allure.story('仓库操作')
    @allure.testcase('HTTPS 浅克隆仓库')
    def test_clone_depth_repo(self, clone_repo):
        assert os.path.exists(clone_repo.working_tree_dir)
        shutil.rmtree(clone_repo.working_tree_dir)

    @allure.story('分支操作')
    @allure.testcase('查看远程分支')
    def test_show_remote_branch(self, init_repo):
        remote_branches = [ref.name for ref in init_repo.remote().refs]
        assert 'origin/master' in remote_branches

    @allure.story('分支操作')
    @allure.testcase('推送分支')
    def test_push_branch(self, init_repo, commit_file):
        init_repo.remote('origin').push()
        assert 'README.md' in init_repo.head.commit.tree or len(init_repo.index.diff(None)) == 0

    @allure.story('分支操作')
    @allure.testcase('推送所有分支')
    def test_push_branchs(self, init_repo, commit_file):
        # 创建新分支
        new_branch = 'new_branch_' + rg.formatted_time()
        init_repo.create_head(new_branch)
        init_repo.git.push('--all')
        # 查看远程分支
        remote_branches = [ref.name for ref in init_repo.remote().refs]
        assert 'origin/' + new_branch in remote_branches

    @allure.story('分支操作')
    @allure.testcase('强制推送分支')
    def test_enforce_push_branch(self, test_pre_push_branch, init_repo, commit_file):
        # 调用 test_pre_push_branch 先在远程做一次提交
        init_repo.remote('origin').push(force=True)
        assert 'README.md' in init_repo.head.commit.tree or len(init_repo.index.diff(None)) == 0

    @allure.story('分支操作')
    @allure.testcase('推送新分支')
    def test_push_new_branch(self, init_repo):
        # 创建新分支
        new_branch = init_repo.create_head('new_branch_' + rg.formatted_time())
        new_branch.commit = init_repo.head.commit
        # 推送新分支
        init_repo.remotes.origin.push(new_branch)
        assert new_branch in init_repo.branches

    @allure.story('分支操作')
    @allure.testcase('删除远程分支')
    def test_delete_remote_branch(self, init_repo):
        # 创建新分支并推送到远程仓库
        branch_name = 'remote_branch_to_delete'
        new_branch = init_repo.create_head(branch_name)
        new_branch.commit = init_repo.head.commit
        init_repo.remotes.origin.push(new_branch)
        # 删除远程分支
        init_repo.git.branch('-D', branch_name)
        remote_branch = init_repo.remote().refs[branch_name]
        init_repo.git.push('--delete', 'origin', branch_name)
        assert branch_name not in [b.name for b in init_repo.branches]
        assert remote_branch not in [b for b in init_repo.remote().refs]

    @allure.story('分支操作')
    @allure.testcase('fetch拉取分支')
    def test_fetch_branch(self, init_repo):
        init_repo.remote('origin').fetch()
        assert 'origin/master' in init_repo.refs

    @allure.story('分支操作')
    @allure.testcase('pull拉取分支')
    def test_pull_branch(self, test_pre_push_branch, init_repo):
        # 调用 test_pre_push_branch 先在远程做一次提交
        result = init_repo.remote('origin').pull()
        assert 'origin/master' in str(result[0])

    @allure.story('标签操作')
    @allure.testcase('查看远程标签')
    def test_show_remote_tag(self, init_repo, test_pre_push_branch):
        tags = init_repo.remote('origin').repo.tags
        remote_tags = [tag.name for tag in tags]
        logging.info(remote_tags)
        assert 'v1.0.0' in remote_tags

    # @allure.story('标签操作')
    # @allure.testcase('推送标签')
    def test_push_tag(self, init_repo):
        # 创建标签
        tag = init_repo.create_tag('v' + rg.formatted_time(), message='test push tag')
        # 推送标签
        init_repo.remote('origin').push(tag)
        assert init_repo.git.ls_remote('--tags', init_repo.remote().name, tag)

    @pytest.mark.skip(reason='跳过此条用例，没调试成功')
    @allure.story('标签操作')
    @allure.testcase('推送所有标签')
    def test_push_all_tags(self, init_repo):
        # init_repo.create_tag('v' + rg.formatted_time(), message='test push tag')
        init_repo.remotes.origin.push('--tags')

    @allure.story('标签操作')
    @allure.testcase('删除远程标签')
    def test_delete_remote_tag(self, init_repo):
        # 先创建标签并推送到远程
        remote_tag = 'remote_tag_to_delete'
        tag = init_repo.create_tag(remote_tag, message='test push tag')
        init_repo.remote('origin').push(tag)
        # 删除本地标签
        init_repo.delete_tag(remote_tag)
        # 删除远程标签
        init_repo.remote('origin').push(':refs/tags/' + remote_tag, force=True)
        assert ':refs/tags/' + remote_tag not in [tag.name for tag in init_repo.remote().refs]

    @allure.story('标签操作')
    @allure.testcase('fetch拉取标签')
    def test_fetch_tags(self, init_repo):
        # 获取所有远程标签的最新更改
        init_repo.remotes.origin.fetch(tags=True)
        assert len(init_repo.tags) > 0, "No tags found"

    @allure.story('其它操作')
    @allure.testcase('本地是否连通Gitee')
    def test_git_connection(self, init_repo):
        assert init_repo.remotes.origin.fetch(), 'Failed to fetch from remote origin'

    @pytest.mark.skip(reason='跳过此条用例，待解决没有在protected_branch进行commit的问题')
    @allure.story('其它操作')
    @allure.testcase('自动创建 PR')
    def test_auto_create_pr(self, init_repo, commit_file):
        # 前提：在远程创建 protected_branch 分支，并设置为保护分支
        if 'protected_branch' not in init_repo.branches:
            init_repo.create_head('protected_branch', f'origin/protected_branch')

        # 切换到 protected_branch 分支
        # init_repo.heads['protected_branch'].checkout()
        init_repo.head.reference = init_repo.heads.protected_branch

        init_repo.remote('origin').push()

        # 切换回 master 分支
        init_repo.head.reference = init_repo.heads.master


if __name__ == '__main__':
    # pytest.main(['-v', '-s'])
    pytest.main(['--alluredir', '../report/allure'])
    os.system(r"allure generate ../report/allure -o ../report/allure --clean")
    os.system(f"allure serve ../report/allure -p 8899")

    # 命令行生成测试报告
    # 生成测试报告: pytest test_git.py --alluredir ../report/allure
    # 清除测试报告：pytest --alluredir ../report/allure --clean-alluredir
    # 打开测试报告: allure serve ../report/allure
