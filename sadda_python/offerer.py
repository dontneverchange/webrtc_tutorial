from aiortc import RTCIceCandidate, RTCPeerConnection, RTCSessionDescription, RTCConfiguration, RTCIceServer
import json
import asyncio
import requests


SIGNALING_SERVER_URL = 'http://0.0.0.0:6969'
ID = "offerer01"




async def main():
    print("Starting")
    peer_connection = RTCPeerConnection()
    channel = peer_connection.createDataChannel("chat")


    async def send_pings(channel):
        num = 0
        while True:
            msg = "From Offerer: {}".format(num)
            print("Sending via RTC Datachannel: ", msg)
            channel.send(msg)
            num+=1
            await asyncio.sleep(1)

    @channel.on("open")
    def on_open():
        print("channel openned")
        channel.send("Hello from Offerer via Datachannel")
        asyncio.ensure_future(send_pings(channel))

    @channel.on("message")
    def on_message(message):
        print("Received via RTC Datachannel", message)



    # send offer
    await peer_connection.setLocalDescription(await peer_connection.createOffer())
    message = {"id": ID, "sdp": peer_connection.localDescription.sdp, "type": peer_connection.localDescription.type}
    r = requests.post(SIGNALING_SERVER_URL + '/offer', data=message)
    print(r.status_code)
    
    #POLL FOR ANSWER
    while True:
        resp = requests.get(SIGNALING_SERVER_URL + "/get_answer")
        if resp.status_code == 503:
            print("Answer not ready, trying again")
            await asyncio.sleep(1)
        elif resp.status_code == 200:
            data = resp.json()
            if data["type"] == "answer":
                rd = RTCSessionDescription(sdp=data["sdp"], type=data["type"])
                await peer_connection.setRemoteDescription(rd)
                print(peer_connection.remoteDescription)
                while True:
                    #print("Ready for Stuff")
                    await asyncio.sleep(1)
            else:
                print("Wrong type")
            break

        print(resp.status_code)



asyncio.run(main())