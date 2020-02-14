import struct

class Packet:
  def __init__(self, raw_data):
    version_and_ihl = raw_data[0]
    self.version = version_and_ihl >> 4
  
    # ihl holds how many 4 bytes you need for whole IP Header
    self.ihl = (version_and_ihl & 0b1111) * 4

    self.ttl, self.protocol, self.src_ip, self.dest_ip = struct.unpack("! B B 2x 4s 4s", raw_data[8:20])
    self.raw_data = raw_data[20:]
    
  def __format_ip_addr(self, raw_ip):
    formatted_ip = '.'.join(map('{:d}'.format, raw_ip))
    return formatted_ip

  def get_src_ip_addr(self):
    return self.__format_ip_addr(self.src_ip)

  def get_dest_ip_addr(self):
    return self.__format_ip_addr(self.dest_ip)

  def print_packet(self):
    print('IPV4:')
    print('SRC IP: {}, DEST IP:{}\n'.format(self.get_src_ip_addr(), self.get_dest_ip_addr()))
