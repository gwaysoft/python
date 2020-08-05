from gspackage import paloauto


def getAddressListByTag(command):
    output = paloauto.executeCommand(command)
    outList = output.split("\n")
    print(outList[:10:])
    print(outList[len(outList) - 10::])
    print("-----------start--------------")
    tagList = []
    for item in outList:
        print(item)
        if item.find("(O)") == -1:
            continue
        tagList.append(item.strip().replace(" (O)", ""))
    print("-----------end--------------")
    print(len(tagList))
    return tagList


# testList = getAddressListByTag('show object dynamic-address-group name awsprod')
testList = getAddressListByTag('show object dynamic-address-group name cloud-env')
print(len(testList), testList)
