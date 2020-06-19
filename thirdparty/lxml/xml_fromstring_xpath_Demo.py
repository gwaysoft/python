# pip install lxml
from lxml import etree

text='''
<response status="success"><result><address-group>
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
</result></response>
'''
xml=etree.fromstring(text, etree.XMLParser(remove_blank_text=True)) #初始化生成一个XPath解析对象

'''element'''
# get by element is static or dynamic
# b = xml.xpath('//static//text()|//dynamic//text()')

# get by element -> sub element
# b = xml.xpath('//entry/tag[member="paupdate"]/../@name')

# get by elements -> content member = insideIP or paupdate or outsideIP
# b = xml.xpath('//member[contains(text(),"insideIP") or contains(text(),"paupdate") or contains(text(),"outsideIP")]/../../@name')

'''attribute'''
# get by element is static or dynamic
b = xml.xpath("//entry[@name='test1']/./@name")
print(type(b),b,b[0])
