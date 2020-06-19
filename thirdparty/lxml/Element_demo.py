# pip install lxml
from lxml import etree

root = etree.Element("root", interesting="totally")

root.append(etree.Element("child1"))
etree.SubElement(root, "child2").text = "Child 2"
etree.SubElement(root, "child3")
root.insert(0, etree.Element("child0"))
print(root.tag, '\n' + etree.tostring(root, pretty_print=True).decode("UTF-8"))

print(len(root), root[:3], root[-1:])
'''list'''
for child in root:
  child.text = "dd"
  print(child.tag)

root.append(etree.Entity("#123"))
root.append(etree.Comment("some comment"))

print(root.tag, '\n' + etree.tostring(root, pretty_print=True).decode("UTF-8"))