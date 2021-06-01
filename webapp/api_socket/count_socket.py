import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.urls import re_path

urls = [] 
class CountConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # subscript own channel name to group
        await self.channel_layer.group_add("grp", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("grp", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        counter = text_data_json['counter']
        #raise group event
        await self.channel_layer.group_send("grp", {
            "type": "grp.count",
            "counter": counter
        })
    async def grp_count(self, event):
        # Send a group event down to the client
        await self.send(text_data=json.dumps({'counter':event["counter"]}))


urls+=[re_path(r'socket/count', CountConsumer.as_asgi())]