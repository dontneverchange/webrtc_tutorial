# WebRTC Tutorial

WebRTC - python=3.8 - anaconda

javascript - web
Unity 3d c#
Android Studio kotlin

Linux - you don't have to


sadda - our

----------------------------------------------
webrtc -> NAT Traversal

Components of WebRTC
1 - python client (peer) - behind NAT

2 - signaling server - AWS - (python)

3 - turn/stun server - (without it, works locally, not acorss internet) AWS

------------------------------------
process to create peer to peer connection

1 - Client 1(Offerer) - creates an offer, sends to signaling server

	1-Creates offer
	
	2-Sets Local Description
	
2 - Client 2(Answerer) - Requests for an offer, create an Answer

	1-Sets Remote Description
	
	2-Creates Answer
	
	3-Sets Local Description
	
3 - Client 2(Answerer) - Sends the Answer to signaling server

4 - Client 1(Offerer) - Receives the Answer

	3-Sets Remote Description
	





