
### `scripts/hello.py`

"""简单的示例脚本 - Hello World"""

import sys
from datetime import datetime


def greet(name: str = "World") -> str:
    """向某人打招呼"""
    return f"Hello, {name}! 欢迎学习 Python。"


def show_info() -> None:
    """打印运行时信息"""
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    print(greet("tanjinshe"))
    print()
    show_info()