# pip install lxml
from lxml import etree

text='''
<address-group>
  <entry name="test1">
    <dynamic>
      <filter>'paupdate' or 'paupdate' </filter>
    </dynamic>
    <tag>
      <member>paupdate</member>
    </tag>
  </entry>
  <entry name="tagTestGroup">
    <dynamic>
      <filter>'insideIP'</filter>
    </dynamic>
    <tag>
      <member>insideIP</member>
    </tag>
    <description>test Tag</description>
  </entry>
  <entry name="outsideTag">
    <static>
      <member>192.16.3.5</member>
    </static>
    <tag>
      <member>outsideIP</member>
      <member>insideIP</member>
    </tag>
  </entry>
</address-group>

'''
xml=etree.XML(text, etree.XMLParser(remove_blank_text=True)) #初始化生成一个XPath解析对象



# print(xml.tag)
# print(etree.tostring(xml))
# print(etree.tostring(xml).decode('utf-8'))

for entry in xml:
  print(etree.tostring(entry))