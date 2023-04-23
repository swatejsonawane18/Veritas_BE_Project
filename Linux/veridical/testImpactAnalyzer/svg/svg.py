import xml.etree.ElementTree as ET
import glob
import json
from collections import defaultdict

answer = {}
def parser(filename):
	tree = ET.parse(filename)
	#print(tree)
	root = tree.getroot()
	#print(root.tag)
	#print(root.attrib)
	#for child in root:
	#	print(child.tag, child.attrib)
	#	
	childGraph=root[0]

	'''
	for child in childGraph:
		print("PARENT:")
		print("TAG: ", child.tag)
		print("ATTRIBUTES: ", child.attrib)
		print("TEXT: ", child.text)
		#print(child.tag, child.attrib, child.text)
		#if child.find("text") != None:
		#print(child.find("text").text)
		print("CHILD:")
		for c in child:
			#print(c.tag, c.attrib, c.text)
			print("TAG: ", c.tag)
			print("ATTRIBUTES: ", c.attrib)
			print("TEXT: ", c.text)
		print("\n\n")
		'''
	'''
	for child in root[0].iter("node"):
		print("LOL\n")
		typee=child.find("title").text
		name=child.find("text").text
		print(typee, name)
		
	'''
	nodeMap = {}
	edgeMap = {}
	for child in childGraph:
		if "class" in child.attrib.keys():
			if(child.attrib["class"]=="node"):
				print("NODE:")
				print("Node Type: ", child[0].text)
				print("Node Text: ", child[1][0][1].text)
				nodeMap[child[0].text]=child[1][0][1].text
				print("\n")
			if(child.attrib["class"]=="edge"):
				print("EDGE:")
				#print(child[0].text)
				temp=child[0].text.split("->")
				print("Edge From: ", temp[0])
				print("Edge To: ", temp[1])
				if temp[1] in edgeMap.keys():
					if temp[0] not in edgeMap[temp[1]]:
						edgeMap[temp[1]].append(temp[0])
				else:
					edgeMap.setdefault(temp[1],[]).append(temp[0])
				#edgeMap[temp[1]].append(temp[0])
				#print(temp[0], temp[1])
				print("\n")
	print(nodeMap)
	print(edgeMap)
	for edge in edgeMap:
		for x in edgeMap[edge]:
			if nodeMap[edge] in answer.keys():
				if nodeMap[x] not in answer[nodeMap[edge]]:
					answer[nodeMap[edge]].append(nodeMap[x])
			else:
				answer.setdefault(nodeMap[edge], []).append(nodeMap[x])
			#answer[nodeMap[edge]].append(nodeMap[x])
		
			
root_dir='/home/jineshparakh/Documents/Github/veridical/testImpactAnalyzer/op/html/'

for filename in glob.iglob(root_dir + '**/**', recursive=True):
	if filename.endswith('_cgraph.svg'):
		print("FILENAME: ", filename)
		parser(filename)
		#print(filename)
print("\n\nFunction dependency: ")
print(json.dumps(answer, indent=4))
