import json
import asyncio
import websockets
import execjs
cxt=execjs.compile(open("adapter/pako.min.js").read())
async def huobi_websocket():
    async with websockets.connect("ws://cex.plus/ws/huobipro") as websocket:
        await websocket.send(json.dumps({'sub': "market.dashusdt.depth.step0", 'id': "detpth1526651678686"}))
        while 1:
            rep=await websocket.recv()
            rep=cxt.call('cex_parse',str(rep)[1:]);
            print(rep)
asyncio.get_event_loop().run_until_complete(huobi_websocket())
