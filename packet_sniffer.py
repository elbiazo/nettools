import socket
from networking.ethernet import Ethernet
from networking.ipv4 import IPV4

conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
while True:
  raw_data, addr = conn.recvfrom(65536)
  eth = Ethernet(raw_data)
 #eth.print_ethernet_frame()
  
  ipv4 = IPV4(eth.raw_data)
  ipv4.print_ipv4() 
