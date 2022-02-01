from channels.consumer import SyncConsumer

class EchoConsumer(SyncConsumer):
    def websocket_connect(self , event):
        print("connect event is called")

    def websocket_recieve(self,event):
        print("new event is recieved")
        print(event)