# 指令说明

- 创建虚拟环境：`python -m venv venv`
- 进入虚拟环境：`call activate.bat`
- 安装项目依赖：`pip install -r requirements.txt`
- 重新生成依赖：`pipreqs ./ --encoding=utf8`
- 转换.qrc为.py：`pyside6-rcc resources.qrc -o ../../helper/resources.py`
- 打包： `pyinstaller ./src/*.py -D -w -n Fnt工具箱 --clean -y -i app.ico --upx-dir=./upx`