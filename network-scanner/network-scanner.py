import scapy.all as scapy

# using arping function:
# def scanner(ip):
#     scapy.arping(ip)

# scanner("192.168.0.1/24")

def scanner(ip):
    arp_request = scapy.ARP(pdst=ip) # create ARP packet
    broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # create broadcast frame
    arp_request_broadcast = broadcast_frame/arp_request # combine ARP packet with broadcast frame
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1) # send'n'receive packets
    print(answered.summary())


    #get help from scapy
    #print(arp_request.summary()) # print summary of the ARP packet
    #scapy.ls(scapy.Ether())
    #arp_request_broadcast.show()

scanner("192.168.0.1/24")