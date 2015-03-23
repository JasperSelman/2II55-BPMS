import re
import sys

data = ""
with open (sys.argv[1], "r") as myfile:
    data = myfile.read()

reRef = re.compile('<decomposesTo id="([^"]*)" />', re.DOTALL)
reDef = re.compile('<decomposition id="([^"]*)" xsi:type="([^"]*)">', re.DOTALL)

listRefs = set()
listDefs = set()
mapDefs = dict()

for match in reRef.finditer(data):
    listRefs.add(match.group(1))
    
for match in reDef.finditer(data):
    listDefs.add(match.group(1))
    mapDefs[match.group(1)] = match.group(2)
    
print("Results:")
for match in (listRefs - listDefs):
    print(" * Undefined :", match)