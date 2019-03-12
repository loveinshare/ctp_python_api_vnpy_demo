从vnpy中抽出了ctp的python api 
去除了原vnpy的gateway

python使用vnpy的vncoda 
{
其实只要下载vncoda把他的python.exe改一下名比如vpy.exe
运行的时候用 vpy.exe ctp_mdapi.py之类的就可以
}

#测试行情API
python ctp_mdapi.py 可以订阅合约(写的是i1905，如果失效请自行修改)并print Tick的data


#测试交易API
python ctp_tdapi.py 可以获取当日可订阅合约，并尝试挂单（如失效请自行修改）
需要自行编辑ctp_tdapi.py输入账户和密码（siminow）


#进一步使用
在自己的main.py中 import ctp_tdapi ctp_mdapi模块，继承api函数并重写相应函数
可以自己写一些tick接受储存的功能或者小的实时策略




#联系方式
如需期货开户和技术支持
微信：17615876246
QQ：657688572




