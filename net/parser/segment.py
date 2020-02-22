import struct

class Segment:
  def __init__(self, raw_data, protocol):
    self.src_port=self.dest_port=self.sequence=self.ack=self.offset=self.reserved = 0
    self.protocol = protocol
    self.data = 0
    self.raw_data = raw_data

    if self.protocol == 6:
      self.tcp(raw_data)
     
  def tcp(self, data):
    self.src_port, self.dest_port, self.sequence, self.ack, offset_reserved_flags = struct.unpack("! H H L L H", data[:14])
    
    # Header length in bytes
    self.header_length = (offset_reserved_flags >> 12) * 4
    self.reserved = (offset_reserved_flags >> 9) & 0b0000111

    # Get last 9 bits
    self.control_flags = offset_reserved_flags & 511
    self.data = self.raw_data[self.header_length:]
    
  def print_tcp(self):
    if self.protocol == 6:
      print("TCP:")
      print("SRC Port: {}, DEST Port: {}\n".format(self.src_port, self.dest_port))
