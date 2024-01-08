# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/4 14:59
@description  Git 相关操作
"""

import git
from git import Repo, Git
import os.path
from datetime import datetime
from utils.file.docx_demo import docx_ops
from utils.file.create_big_file import create_large_binary_file

time = datetime.now().strftime("%Y%m%d%H%M%S")


class GitUtil:
    def __init__(self, repo_url, target_path):
        self.repo_url = repo_url,
        self.target_path = target_path

    @staticmethod
    def git_clone(repo_url, target_path):
        """克隆仓库"""
        if not os.path.exists(target_path):
            print('仓库不存在, 开始下载...')
            Repo.clone_from(repo_url, target_path)
        print('仓库路径: ', repo_url)

    @staticmethod
    def git_push(repo_url, target_path):
        """推送代码"""
        repo = git.Repo(target_path)
        # 切换新分支，不用时需注释
        # new_branch = repo.create_head('new_branch')
        # repo.head.reference = new_branch
        repo.head.reset(index=True, working_tree=True)

        for i in range(1, 5):
            with open(repo.working_dir + '/README.md', 'a') as f:  # w / a
                f.write('Hello Git ' + time + '\n')
            repo.index.add(['README.md'])
            repo.index.commit('第 ' + str(i) + ' 次 Hello Git ' + time)
        # repo.index.commit('第 ' + str(i) + ' 次 Hello Git ' + time)
        repo.remote('origin').push()
        print('仓库路径: ', repo_url)

    @staticmethod
    def git_create_branch(repo_url, target_path):
        """创建分支"""
        repo = git.Repo(target_path)
        for i in range(1, 5):
            new_branch = 'test_branch_' + str(i) + '_' + time
            repo.create_head(new_branch)
            # 切换到新分支
            repo.head.reference = new_branch
            repo.head.reset(index=True, working_tree=True)
            with open(repo.working_dir + '/README.md', 'w') as f:
                f.write('Hello Git ' + time + '\n')
            repo.index.add(['README.md'])
            repo.index.commit('第 ' + str(i) + ' 次Hello Git ' + time)
        repo.git.push('--all')
        print('仓库路径: ', repo_url)

    @staticmethod
    def show_branch(repo_url, target_path):
        """查看分支"""
        repo = git.Repo(target_path)
        print('本地分支: ', repo.branches)
        remote_branches = [ref.name for ref in repo.remote().refs]
        print('远程分支: ', remote_branches)
        print('仓库路径: ', repo_url)

    @staticmethod
    def delete_branch(repo_url, target_path):
        """删除分支"""
        repo = git.Repo(target_path)
        # 创建新分支并推送到远程仓库
        branch_name = 'remote_branch_to_delete'
        new_branch = repo.create_head(branch_name)
        new_branch.commit = repo.head.commit
        repo.remotes.origin.push(new_branch)
        # 删除远程分支
        repo.git.branch('-D', branch_name)
        remote_branch = repo.remote().refs[branch_name]
        repo.git.push('--delete', 'origin', branch_name)
        assert branch_name not in [b.name for b in repo.branches]
        assert remote_branch not in [b for b in repo.remote().refs]
        print('删除分支: ', branch_name)

    @staticmethod
    def git_create_tag(repo_url, target_path):
        """创建标签"""
        repo = git.Repo(target_path)
        for i in range(101, 120):
            tag = repo.create_tag('tag_' + str(i) + '_' + time, message='test push tag')
            repo.remote('origin').push(tag)
        # repo.remotes.origin.push('--tags')  # @todo：推送所有标签未成功
        print('仓库路径: ', repo_url)

    @staticmethod
    def show_tag(repo_url, target_path):
        """查看标签"""

        """
        ['tag_1_20230918104017', 'tag_2_20230918104017', 'tag_3_20230918104017', 'tag_4_20230918104017',
         'tag_5_20230918104017', 'tag_6_20230918104017', 'tag_7_20230918104017', 'tag_8_20230918104017',
         'tag_9_20230918104017']
        """

        repo = git.Repo(target_path)
        local_tag = repo.tags
        print('本地标签: ', local_tag)

        tags = repo.remote('origin').repo.tags
        remote_tags = [tag.name for tag in tags]
        print('远程标签: ', remote_tags)

        print('仓库路径: ', repo_url)

    @staticmethod
    def delete_tag(repo_url, target_path):
        repo = git.Repo(target_path)
        # 先创建标签并推送到远程
        # remote_tag = 'remote_tag_to_delete'
        remote_tag = 'tag_2_20230918104017'
        # tag = repo.create_tag(remote_tag, message='test push tag')
        # repo.remote('origin').push(tag)
        # 删除本地标签
        repo.delete_tag(remote_tag)
        # 删除远程标签
        repo.remote('origin').push(':refs/tags/' + remote_tag, force=True)
        assert ':refs/tags/' + remote_tag not in [tag.name for tag in repo.remote().refs]
        # @todo: 删除
        GitUtil.git_ls_remote(repo_url, target_path)

    @staticmethod
    def delete_all_remote_tags(repo_url, target_path):
        """删除远程标签"""
        repo = git.Repo(target_path)

        # 获取远程仓库的标签列表
        tags = repo.git.ls_remote("--tags").splitlines()

        # 删除每个标签
        for tag in tags:
            tag_name = tag.split("refs/tags/")[-1]
            repo.git.push("--delete", "origin", tag_name)

        # 删除临时目录
        repo.git.clear()

    @staticmethod
    def git_lfs(repo_url, target_path):
        """推送 LFS"""
        repo = git.Repo(target_path)

        if not os.path.exists('.gitattributes'):
            print('.gitattributes 不存在, 开始执行 git lfs 初始化')
            git_cmd = Git(target_path)
            git_cmd.execute(['git', 'lfs', 'install'])
        print('.gitattributes 已存在')

        extensions = ['.bin', '.docx']
        # extensions = ['.bin']
        for extension in extensions:
            repo.git.execute(['git', 'lfs', 'track', '*' + extension])

        for i in range(1, 5):
            docx_ops(target_path + '/lfs00{}.docx'.format(i))
            repo.git.add('.')  # add 所有
            repo.index.add(['lfs00{}.docx'.format(i)])  # 单独 add 某个文件

        repo.index.commit('Hello Git ' + time)
        repo.remote('origin').push(force=True)
        print('仓库路径: ', repo_url)


    @staticmethod
    def push_big_file(repo_url, target_path):
        """推送大文件"""
        repo = git.Repo(target_path)
        # file_size = 1024 * 1024 * 100  # 文件大小为 100 MB
        # file_size = 1024 * 1024 * 1  # 文件大小为 1 MB
        file_size = 1024 * 1024 * 1
        if not os.path.isdir(target_path + '/testfile'):
            os.mkdir(target_path + '/testfile')
        if not os.path.isdir(os.path.join(target_path + '/testfile', 'testfile2')):
            os.mkdir(os.path.join(target_path + '/testfile', 'testfile2'))
        for i in range(1, 5):
            create_large_binary_file(target_path + '/testfile/large_file_{}.bin'.format(i), file_size)
            create_large_binary_file(target_path + '/testfile/testfile2/large_file_{}.bin'.format(i), file_size)
            repo.git.add('.')  # add 所有
            repo.index.commit('Hello Git ' + time)
        repo.remote('origin').push(force=True)
        print('仓库路径: ', repo_url)

    @staticmethod
    def git_ls_remote(repo_url, target_path):
        repo = git.Repo(target_path)

        print('ls_remote: \n', repo.git.ls_remote(target_path))

        # 存储多次执行结果的列表
        results = []
        # 执行 git ls-remote 命令并记录结果
        for i in range(1, 31):
            results.append(repo.git.ls_remote(target_path))
        # results.append(repo.git.ls_remote(target_path))
        # GitUtil.delete_branch(repo_url, target_path)
        # results.append(repo.git.ls_remote(target_path))

        # 检查结果列表中的每个元素是否相同
        if len(set(results)) == 1:
            print("All results are the same.")
        else:
            print("Results are different.")
            # 打印详细差异
            for i in range(len(results) - 1):
                if results[i] != results[i + 1]:
                    print(f"Difference between execution {i + 1} and {i + 2}:")
                    diff_lines = []
                    lines1 = results[i].splitlines()
                    lines2 = results[i + 1].splitlines()
                    for line1, line2 in zip(lines1, lines2):
                        if line1 != line2:
                            diff_lines.append(f"  {line1}\n- {line2}")
                    print('\n'.join(diff_lines))

    @staticmethod
    def gitee_test(target_path):
        repo = git.Repo(target_path)


if __name__ == '__main__':
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    # repo_url = 'https://username:password@gitee/testent001/wei-demo-001.git'
    # target_path = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/gitee/repo/wei-demo-001'

    """克隆仓库"""
    # GitUtil.git_clone(repo_url, target_path)
    """推送代码"""
    # GitUtil.git_push(repo_url, target_path)
    """推送新分支"""
    # GitUtil.git_create_branch(repo_url, target_path)
    """查看分支"""
    # GitUtil.show_branch(repo_url, target_path)
    """删除分支"""
    # GitUtil.delete_branch(repo_url, target_path)
    """创建标签"""
    # GitUtil.git_create_tag(repo_url, target_path)
    """查看标签"""
    # GitUtil.show_tag(repo_url, target_path
    """删除所有标签"""
    # GitUtil.delete_all_remote_tags(repo_url, target_path)
    """删除标签"""
    # GitUtil.delete_tag(repo_url, target_path)
    """推送 LFS 文件"""
    # GitUtil.git_lfs(repo_url, target_path)
    """创建代码评审"""
    # GitUtil.create_pr_file(repo_url, target_path)
    """推送大文件"""
    # GitUtil.push_big_file(repo_url, target_path)
    """git ls-remote"""
    # GitUtil.git_ls_remote(repo_url, target_path)
