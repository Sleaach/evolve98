from scapy.all import sniff
import time
def net(packet):
    try:
        if packet.haslayer("IP"):
            ip_src = packet["IP"].src
            ip_dst = packet["IP"].dst
            if packet.haslayer("TCP"):
                tcp_sport = packet["TCP"].sport
                tcp_dport = packet["TCP"].dport
                print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: TCP, Source Port: {tcp_sport}, Destination Port: {tcp_dport}, Domain: {packet['DNSQR'].qname if packet.haslayer('DNSQR') else 'N/A'}")
                time.sleep(1)
            elif packet.haslayer("UDP"):
                udp_sport = packet["UDP"].sport
                udp_dport = packet["UDP"].dport
                print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: UDP, Source Port: {udp_sport}, Destination Port: {udp_dport}, Domain: {packet['DNSQR'].qname if packet.haslayer('DNSQR') else 'N/A'}")
                time.sleep(1)
    except Exception as e:
        print(e)

def main():
    sniff(prn=net, store=0)
