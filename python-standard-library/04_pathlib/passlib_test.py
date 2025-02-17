#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/10/22 17:46
# @Author : limber
# @desc :

#
# 导入 CryptContext 类，用于处理所有哈希...
#
from passlib.context import CryptContext

#
# 为您的应用程序创建单个全局实例...
#
pwd_context = CryptContext(
    #将此列表替换为您希望支持的哈希值。
    # 此示例将 pbkdf2_sha256 设置为默认值，
    # 额外支持读取遗留des_crypt哈希值。
    schemes=["pbkdf2_sha256", "des_crypt"],

    # 自动将列表中除第一个哈希器之外的所有哈希器标记为已弃用。
    # （这将是 Passlib 2.0 中的默认值）
    deprecated="auto",

    # （可选）设置应使用的轮数。
    # 不同的方案的适当值可能会有所不同，
    # 以及您希望它花费的时间。
    # 不管它通常是安全的，并且会使用 passlib 的默认值。
    ## pbkdf2_sha256__rounds = 29000，
    )