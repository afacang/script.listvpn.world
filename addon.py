import xbmcaddon
import xbmcgui
import subprocess
import os
import re
import socket
import fcntl
import struct

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Hello,"
line2 = "Your VPN Address is:"
line3 = "VPN service doesn't seem to be running"
PROCNAME = "openvpn"

def is_running(process):
  s = subprocess.Popen(["ps","axw"],stdout=subprocess.PIPE)
  for x in s.stdout:
    if re.search(process, x):
      return True
  return False

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if is_running(PROCNAME):
 xbmcgui.Dialog().ok(addonname, line1, line2, get_ip_address('tun0'))
else:
 xbmcgui.Dialog().ok(addonname, line1, line3)

