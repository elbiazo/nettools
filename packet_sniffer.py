import socket
from net.parser.frame import Frame
from net.parser.packet import Packet
from net.parser.segment import Segment 

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
while True:
  raw_data, addr = conn.recvfrom(65536)
  frame = Frame(raw_data)
 
  packet = Packet(frame.raw_data)

  segment = Segment(packet.raw_data, packet.protocol)

  segment.print_tcp()
