# -*- coding: utf-8 -*-
# @Author : QSheng
# @File   : os_env.py
# @Time   : 2026/9/29 10:21

import os

if __name__ == '__main__':
    print(os.environ.get("TAVILY_API_KEY"))
    print(os.environ.get("CHAT_DEEPSEEK_API_KEY"))