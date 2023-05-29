# -*-coding:utf-8-*-
import json
import paho.mqtt.client as mqtt

from app.config.conf import conf
from app.config.setupsetting import sysuuid
from app.core.clip import Clipboard


class ClipSync:
    def __init__(self):
        # 创建 MQTT 客户端
        self.client = mqtt.Client()

        # 为客户端分配回调函数
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

        self.unacked_sub = []  # 未获得服务器响应的订阅消息 id 列表
        self.setup()
        self.reduplicates = {}
        self.clip = Clipboard()

    def setup(self):
        # 连接到 MQTT 服务器
        # connect() 函数是阻塞的，在连接成功或失败后返回。如果想使用异步非阻塞方式，可以使用 connect_async() 函数。
        config = conf.get_config().config
        self.client.username_pw_set(config.get("MQTT", "username"), config.get("MQTT", "password"))
        self.client.connect(config.get("MQTT", "ip"), config.getint("MQTT", "port"), config.getint("MQTT", "keepalive"))
        # 开始客户端循环
        self.client.loop_start()
        # client.loop_forever()

    # 用于响应服务器端 CONNACK 的 callback，如果连接正常建立，rc 值为 0
    def on_connect(self, client, userdata, flags, rc):
        print(f"MQTT连接结果: {'正常' if rc == 0 else '异常'}")
        # 订阅主题
        config = conf.get_config().config
        self.client.subscribe(config.get("MQTT_CLIENT", "subscribe"), qos=config.getint("MQTT_CLIENT", "qos"))

    # 在连接断开时的 callback，打印 result code
    def on_disconnect(self, client, userdata, rc):
        print(f"断开连接返回结果: {rc}")
        self.client.loop_stop()

    # 用于响应服务器端 PUBLISH 消息的 callback，打印消息主题和内容
    def on_message(self, client, userdata, msg):
        data = json.loads(msg.payload)
        if data["id"] != sysuuid:
            # 在这里处理接收到的消息，例如：过滤、分发、回调、确认、加密、解密、签名等
            print(f"收到 【{data['name']}】 的信息 <<< {data['value']}")
            self.reduplicates[data["id"]] = data["value"]
            self.clip.copy(data["value"])

    # 在订阅获得服务器响应后，从为响应列表中删除该消息 id
    def on_subscribe(self, client, userdata, mid, granted_qos):
        try:
            self.unacked_sub.remove(mid)
        except ValueError as e:
            # print(e)
            pass

    # 订阅单个主题
    def publish(self, topic, payload, qos=0, retain=False, properties=None):
        if self.reduplicates.get(payload["id"]) == payload["value"]:
            return None
        # 在这里发送消息，例如：消息队列、消息持久化、消息发布、消息推送等
        print(f"【{payload['name']}】发送信息 >>> {payload['value']}")
        self.reduplicates[payload["id"]] = payload["value"]
        result, mid = self.client.publish(topic, json.dumps(payload), qos, retain, properties)
        self.unacked_sub.append(mid)

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()


client = ClipSync()
