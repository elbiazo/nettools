import socket
from networking.ethernet import Ethernet

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
while True:
  raw_data, addr = conn.recvfrom(65536)
  eth = Ethernet(raw_data)
  eth.print_ethernet_frame()
