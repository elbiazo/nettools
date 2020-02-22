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
  
  if segment.src_port == 80:
    print("\nIP: {}, Dest Port: {}, Data: {}\n".format(packet.get_src_ip_addr(), segment.dest_port, segment.data))
