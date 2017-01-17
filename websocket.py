import sublime
import sublime_plugin
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "websocket_client-0.40.0"))
print(os.path.join(os.path.dirname(__file__), "websocket_client-0.40.0"))
import websocket
import _thread
import time
#Create websocket and connect to server
#

class WebsocketCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        def on_message(ws, message):
            print (message)

        def on_error(ws, error):
            print (error)

        def on_close(ws):
            print ("### closed ###")

        def on_open(ws):
            ws.send("Hello!")
            ws.close()      

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://localhost:9001/",
                                  on_message = on_message,
                                  on_error = on_error,
                                  on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
