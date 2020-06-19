# pip install requests
import requests
from lxml import etree
import re


text = requests.get("http://172.25.16.9/downloads/op_tools/cloud_info/cloud_info").text
list01 = text.split("\n")
list02 = []
for line in list01:
    if line.find(",") != -1:
        lineList = line.split(",")
        for item in lineList:
            if item == "null":
                continue
            list02.append(item)
'''
<entry name="test tag">
    <ip-netmask>172.18.5.55/32</ip-netmask>
    <tag>
      <member>outsideIP</member>
    </tag>
  </entry>
'''
# pan_head = 'panxapi.py '
# pan_cmd_merge = '-S '

def commit():
    return "panxapi.py -C \'\' --sync"

# def mergeAddress(cmd, name, netmask):
#     #print("\nname: %s \nip: %s \nnetmask: %s\n" %(name, ip, netmask))
#     return pan_head + cmd + '\"<entry name=\'' +name+ '\'><ip-netmask>'+netmask+'</ip-netmask></entry>\" ' + pan_body_address +"\""

pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

once = [True, True]

for address in list02:
    entry = etree.Element("entry", name=address)
    tag = etree.SubElement(entry, "tag")
    member = etree.SubElement(tag, "member")
    member.text = "outsideIP"
    if re.match(pattern, address):
        if once[0]:
            once[0] = False
        else:
            continue
        ip_netmask = etree.SubElement(entry, "ip-netmask")
        ip_netmask.text = address
    else:
        if once[1]:
            once[1] = False
        else:
            continue
        ip_netmask = etree.SubElement(entry, "fqdn")
        ip_netmask.text = address

    xml = etree.tostring(entry).decode("UTF-8")
    print(xml)

    cmd = "panxapi.py -S \'" + xml + "\' \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address\""
    print(cmd)