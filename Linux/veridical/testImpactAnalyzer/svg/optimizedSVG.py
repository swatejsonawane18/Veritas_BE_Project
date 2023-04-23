import xml.etree.ElementTree as ET
import glob
import json
from collections import defaultdict
import sys

answer = {}
def parser(filename):
	#print(filename)
	tree = ET.parse(filename)

	root = tree.getroot()
	childGraph=root[0]
	nodeMap = {}
	edgeMap = {}
	for child in childGraph:
		if "class" in child.attrib.keys():
			if(child.attrib["class"]=="node"):
				length = len(child[1][0])
				t=""
				for i in range(1,length):
					t=t+child[1][0][i].text
				#print(t)
				nodeMap[child[0].text]=t
			if(child.attrib["class"]=="edge"):
				temp=child[0].text.split("->")
				if temp[1] in edgeMap.keys():
					if temp[0] not in edgeMap[temp[1]]:
						edgeMap[temp[1]].append(temp[0])
				else:
					edgeMap.setdefault(temp[1],[]).append(temp[0])
	#print(nodeMap)
	#print(edgeMap)				
	for edge in edgeMap:
		for x in edgeMap[edge]:
			if nodeMap[edge] in answer.keys():
				if nodeMap[x] not in answer[nodeMap[edge]]:
					answer[nodeMap[edge]].append(nodeMap[x])
			else:
				answer.setdefault(nodeMap[edge], []).append(nodeMap[x])
		
			
#root_dir='/home/jineshparakh/Documents/Github/veridical/testImpactAnalyzer/op/html/'

for filename in glob.iglob(sys.argv[1] + '**/**', recursive=True):
	if filename.endswith('_cgraph.svg'):
		parser(filename)

print("Function dependency: ")
print(json.dumps(answer, indent=4))
with open(sys.argv[2], 'w', encoding='utf-8') as f:
    json.dump(answer, f, ensure_ascii=False, indent=4)
