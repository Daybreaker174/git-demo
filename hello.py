# -*- coding: utf-8 -*-
"""Git 环境自检脚本：验证中文、编码与基础运行。"""


def greet(name: str = "DIO") -> str:
    return f"你好，{name}！Git 环境配置成功。"


def main() -> None:
    print(greet())
    print("中文输出正常 ✅")


if __name__ == "__main__":
    main()

# 第二个提交：验证中文提交说明
