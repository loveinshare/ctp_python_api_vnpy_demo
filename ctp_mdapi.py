from vnpy_envi import *
from  datetime import datetime
import threading
# def produce_data(db,data):
#     table_name = "tick"
#     sql = """
#     insert into table %s(




#     )


#     """%(table_name)
#     pass


class CtpMdApi(MdApi):
    """"""

    def __init__(self):
        """Constructor"""
        super(CtpMdApi, self).__init__()
        self.reqid = 0
        self.connect_status = False
        self.login_status = False
        self.userid = ""
        self.password = ""
        self.brokerid = 0
    
    
    
    
    
    def onFrontConnected(self):
        """
        Callback when front server is connected.
        """
        self.connect_status = True
        print("行情服务器连接成功")
        self.login()

    def onFrontDisconnected(self, reason: int):
        """
        Callback when front server is disconnected.
        """
        self.connect_status = False
        self.login_status = False
        print(f"行情连接断开，原因{reason}")

    def onRspUserLogin(self, data: dict, error: dict, reqid: int, last: bool):
        """
        Callback when user is logged in.
        """
        if not error["ErrorID"]:
            self.login_status = True
            print("行情服务器登录成功")
            
            
            # for symbol in self.subscribed:
            #     print(symbol)
            #     self.subscribeMarketData(symbol)
            #     print("已订阅")
        else:
            print("行情登录失败", error)
    
    def onRspError(self, error: dict, reqid: int, last: bool):
        """
        Callback when error occured.
        """
        print("行情接口报错", error)
    
    def onRspSubMarketData(self, data: dict, error: dict, reqid: int, last: bool):
        """"""
        if not error or not error["ErrorID"]:
            print("onRspSubMarketData",data)
            return
        
        print("行情订阅失败", error)

    def onRtnDepthMarketData(self, data: dict):
        """
        Callback of tick data update.
        """
        """
        {'TradingDay': '20190305', 'InstrumentID': 'j1905', 'ExchangeID': '', 'ExchangeInstID': '', 'LastPrice': 2089.0, 'PreSet
        tlementPrice': 2140.5, 'PreClosePrice': 2107.5, 'PreOpenInterest': 306956.0, 'OpenPrice': 2105.0, 'HighestPrice': 2106.0
        , 'LowestPrice': 2071.0, 'Volume': 363622, 'Turnover': 75893641300.0, 'OpenInterest': 277642.0, 'ClosePrice': 1.79769313
        48623157e+308, 'SettlementPrice': 1.7976931348623157e+308, 'UpperLimitPrice': 2290.0, 'LowerLimitPrice': 1991.0, 'PreDel
        ta': 0.0, 'CurrDelta': 1.7976931348623157e+308, 'UpdateTime': '13:49:13', 'UpdateMillisec': 0, 'BidPrice1': 2088.5, 'Bid
        Volume1': 26, 'AskPrice1': 2089.0, 'AskVolume1': 29, 'BidPrice2': 1.7976931348623157e+308, 'BidVolume2': 0, 'AskPrice2':
        1.7976931348623157e+308, 'AskVolume2': 0, 'BidPrice3': 1.7976931348623157e+308, 'BidVolume3': 0, 'AskPrice3': 1.7976931
        348623157e+308, 'AskVolume3': 0, 'BidPrice4': 1.7976931348623157e+308, 'BidVolume4': 0, 'AskPrice4': 1.7976931348623157e
        +308, 'AskVolume4': 0, 'BidPrice5': 1.7976931348623157e+308, 'BidVolume5': 0, 'AskPrice5': 1.7976931348623157e+308, 'Ask
        Volume5': 0, 'AveragePrice': 208715.757847435, 'ActionDay': '20190305'}
        """
        pass
    


    def connect(self, address: str, userid: str, password: str, brokerid: int):
        """
        Start connection to server.
        """
        self.userid = userid
        self.password = password
        self.brokerid = brokerid
        
        # If not connected, then start connection first.
        if not self.connect_status:
            #path = get_folder_path(self.gateway_name.lower())
            self.createFtdcMdApi("tempPath" + "\\Md")
            self.registerFront(address)
            self.init()
        # If already connected, then login immediately.
        elif not self.login_status:
            self.login()
    
    def login(self):
        """
        Login onto server.
        """
        req = {
            "UserID": self.userid,
            "Password": self.password,
            "BrokerID": self.brokerid
        }
        
        self.reqid += 1
        self.reqUserLogin(req, self.reqid)
        
    def close(self):
        """
        Close the connection.
        """
        if self.connect_status:
            self.exit()

if __name__ == "__main__":
    class app_ctp_mdapi2(CtpMdApi):
        def __init__(self,db=None):
            """Constructor"""
            super(app_ctp_mdapi2, self).__init__()
        def onRtnDepthMarketData(self, data: dict):
            print(data)
            # print("app_api",data["InstrumentID"]," ",data["BidPrice1"],data["BidVolume1"],data["LastPrice"],data["AskPrice1"],data["AskVolume1"],"              ",data["UpdateTime"],data["UpdateMillisec"])   
    
    print("ctp_mdapi")
    userid=""
    password=""
    md_address="tcp://180.168.146.187:10010"
    
    brokerid="9999"
    mymd= app_ctp_mdapi2()   
    mymd.connect(md_address, userid, password, brokerid)
    import time
    time.sleep(5)
    mymd.subscribeMarketData("i1905")

    while 1:
        time.sleep(1)
    