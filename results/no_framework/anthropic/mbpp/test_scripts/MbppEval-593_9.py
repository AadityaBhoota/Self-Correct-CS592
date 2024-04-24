import re

def removezero_ip(ip):
    """
    Write a function to remove leading zeroes from an IP address.

    Examples:
    removezero_ip("216.08.094.196") == "216.8.94.196"
    removezero_ip("12.01.024") == "12.1.24"
    removezero_ip("216.08.094.0196") == "216.8.94.196"
    """
    # Split the IP address into its component octets
    octets = ip.split('.')

    # Remove leading zeroes from each octet
    cleaned_octets = [str(int(octet)) for octet in octets]

    # Join the cleaned octets back into a string
    cleaned_ip = '.'.join(cleaned_octets)

    return cleaned_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)