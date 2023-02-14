# eyes
定时提示保护眼睛
机制如下:

1. 如果用户正在敲击键盘或点击鼠标，那么提示会被延缓一段时间。（防止打扰到用户的使用，比如打游戏）
2. 用户进入锁屏状态则停止记录时间
3. 支持开机自启

以下命令适用于windows powershell
安装(开机自启)
```
git clone https://github.com/zrr12138/eyes.git
cd .\eyes\
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
python .\eyes.py install
```
卸载
```
python .\eyes.py uninstall
```
更新
```
cd .\eyes\
python .\eyes.py uninstall
cd ..
rm .\eyes\
https://github.com/zrr12138/eyes.git
cd .\eyes\
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
python .\eyes.py install
```

## 参数配置
参数配置在eyes.py的开头部分，参数用全大写的变量表示

SLEEP_TIME  提醒间隔，单位秒

REMIND_TITLE 提醒窗口的标题

REMIND_STRING 提醒文字

ANSWER_STRING  回答按钮上的文字

DELAY_TIME  可以简单理解为鼠标或者键盘在2倍的DELAY_TIME之间没有点击，就会弹出提醒（距离上一次提醒至少过了SLEEP_TIME）

CHECK_TEST_INTERVAL 检测是否锁屏的间隔

LOG_FILE_PATH 日志文件的路径，必须使用绝对路径，默认是在eyes.py同目录下

MAX_LOG_FILE_SIZE = 1024 * 1024 * 1024  日志文件的最大的大小，单位字节
