

# Klaidas Wikar


class PacketGen:
    #initializes
    def __init__(self):
        self.Packet_t = 0
    
    #creates a packet via the given information
    def generate_packet(self, pid, dst, src, data):
        # converts the data to a binary string
        binary_string = ''.join(format(ord(x), '08b') for x in data)
        #calcuates the parity
        parity_bit = str(binary_string.count('1') % 2)
        
        #assigns the new packet
        packet = (pid, dst, src, data, parity_bit)
        self.Packet_t = packet
        return self.Packet_t



class PacketRecv:
    #intializes 
    def __init__(self, packet_t): 
        self.ParityValid = -1   
        self.pid = packet_t[0]
        self.dst = packet_t[1]
        self.src = packet_t[2]
        self.data = packet_t[3]
        self.rcvd_parity = packet_t[4]
        
	
    # returns a boolean value that checks if the parity of the packet is correct
    def check_parity(self):
        #converts the data to a binary string
        binary_string = ''.join(format(ord(char), '08b') for char in self.data)
        #calcualtes the parity
        computed_parity = str(binary_string.count('1') % 2)
        #checks to see if the parity is valid or not
        self.ParityValid = (computed_parity == self.rcvd_parity)
    # returns info about the packet
    def parsed_packet(self):
            return f"Packet Number {self.pid} with the message {self.data}, is received from node {self.src}. Parity Check returns {self.ParityValid}"

    
 
#takes in various values related to packets
#intializes the class 
#returns what generate_packet should
def test1(pid, dst, src, data):
    p_i = PacketGen()
    return p_i.generate_packet(pid, dst, src, data)

#takes in a packet
#intializes the class with the packet as the input
#checks the parity
# then returns what the parsed_packed method should return
def test2( packet_t ):
    pkt_o = PacketRecv(packet_t)
    pkt_o.check_parity()
    return pkt_o.parsed_packet()
