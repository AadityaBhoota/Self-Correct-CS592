import re

def removezero_ip(ip):
    octets = ip.split('.')
    cleaned_octets = [str(int(octet)) for octet in octets]
    cleaned_ip = '.'.join(cleaned_octets)
    return cleaned_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)