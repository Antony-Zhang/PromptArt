import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    # 生成url [host主机 + date时间戳(RFC1123格式) + authorization认证信息]
    def create_url(self):
        # (可对参数进行逐步打印确认)
        # 生成参数:时间戳date(RFC1123格式)
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 生成参数:认证信息authorization(base64编码)
        # 拼接字符串,得到初始签名signature_origin
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256算法进行加密; 得到签名的摘要signature_sha
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        # 进行base64编码生成签名signature_sha_base64
        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        # 将字符串拼接成原始认证
        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", ' \
                               f'signature="{signature_sha_base64}"'

        # 进行base64编码生成最终认证信息authorization
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.gpt_url + '?' + urlencode(v)
        return url


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### closed ###")


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    data = json.loads(message)  # 将JSON字符串转化为Python对象
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        print(content, end='')
        if status == 2:
            ws.close()


def gen_params(appid, question):
    """
    通过appid和用户的提问, 生成请求参数
    """
    data = {
        "header": {
            "app_id": appid,    # AppID
            "uid": "1234"       # 用于区分不同的用户
        },
        "parameter": {
            "chat": {
                "domain": "general",        # (必)指定访问的领域
                "random_threshold": 0.5,    # 温度系数temperature
                "max_tokens": 2048,         # 模型回答的tokens的最大长度,范围为[1,4096]
                "auditing": "default"
                # "top_k": 4                # 从k个候选中随机选择⼀个（⾮等概率）,范围为[1,6]
                # "chat_id": "1234"         # 用于关联用户会话,需要保障用户对话的唯一性
            }
        },
        "payload": {
            "message": {
                "text": [
                    {
                        "role": "user",         # 对话角色,范围为[user,assistant]
                        "content": question     # 用户和AI的对话内容,text下所有content累计tokens需要控制在8192内
                     }
                ]
            }
        }
    }
    return data


def main(appid, api_key, api_secret, gpt_url, question):
    wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == "__main__":
    # 测试时候在此处正确填写相关信息即可运行
    main(appid="5e683bc7",
         api_key="850c8c6af18250377f05ba90bd0c7dc9",
         api_secret="NmQzZGJjOWEwYmM2MTgxZjM3NzI5MzA2",
         gpt_url="wss://spark-api.xf-yun.com/v1.1/chat",
         question="你是谁？你能做什么？")
