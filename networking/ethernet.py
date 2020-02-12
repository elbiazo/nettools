import struct
import socket

class Ethernet:
  def __init__(self, raw_data):
    # Unpack 6 bytes, 6 bytes, and 2 bytes as big endian.
    self.dest_byte_addr, self.src_byte_addr, self.ether_type = struct.unpack('! 6s 6s H', raw_data[:14])
    self.raw_data = raw_data[14:]

  # Formats adress that is in byte fromat into mac format. XX:XX:XX:XX:XX:XX.
  def __format_mac_addr(self, byte_addr):
    byte_addr_hex = map('{:02x}'.format, byte_addr)
    return ':'.join(byte_addr_hex)

  # Get mac addr formatted destination.
  def get_dest_mac_addr(self):
    return self.__format_mac_addr(self.dest_byte_addr)

  # Get mac addr formatted source. 
  def get_src_mac_addr(self):
    return self.__format_mac_addr(self.src_byte_addr)

  # Get formatted ether type.
  def get_ether_type(self):
    return '0x{:04x}'.format(self.ether_type)

  # Print out the ethernet.
  def print_ethernet_frame(self):
    print('Ethernet Frame:')
    print('Destination: {}, Source: {}, EtherType: {}\n'.format(self.get_dest_mac_addr(), self.get_src_mac_addr(), self.get_ether_type()))