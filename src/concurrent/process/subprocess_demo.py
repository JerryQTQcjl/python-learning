#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/10/31 00:16"

import subprocess

if __name__ == '__main__':
    print('ls -l .')
    subprocess.call(['ls', '-l', '.'])

    # 创建子进程
    # subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
    # args: 子进程执行的命令，可以是字符串或列表
    # bufsize: 缓冲区大小，0表示无缓冲，1表示行缓冲，其他值表示缓冲区大小
    # executable: 子进程执行的程序路径
    # stdin: 子进程的标准输入
    # stdout: 子进程的标准输出
    # stderr: 子进程的标准错误
    print('nslookup www.baidu.com')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 向子进程发送数据
    output, err = p.communicate(b'www.baidu.com')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)
