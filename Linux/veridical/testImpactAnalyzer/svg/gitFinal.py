import os
import sys
import pydriller
import csv
from pydriller import Repository
import json
import sys

#path_to_repo="https://github.com/mantriaditi10/bookMyMovieTia"
path_to_repo=sys.argv[1]
print(path_to_repo)
ans=[]
functionDependency = {}
with open(sys.argv[2], 'r') as f:
  functionDependency = json.load(f)
print(functionDependency)

def findDependendantMethods(functionDependency, methodName):
	for name,dependents in functionDependency.items():
		methodName=methodName.replace("::",".")
		if methodName in name:
			return dependents
	return []
	
for commit in Repository(path_to_repo).traverse_commits():
	singleCommit={}	
	singleCommit['commitHash'] = commit.hash
	singleCommit['authorName'] = commit.author.name
	singleCommit['commiterName'] = commit.committer.name
	files = []
	for f in commit.modified_files:
		singleFile = {}
		singleFile['fileName'] = f.filename
		singleFile['oldPath'] = f.old_path
		singleFile['newPath'] = f.new_path
		singleFile['changeType'] = f.change_type.name
		#singleFile['codeAdded'] = f.diff_parsed['added']
		#singleFile['codeDeleted'] = f.diff_parsed['deleted']
		changedMethods = []
		for method in f.changed_methods:
			singleMethod = {}
			singleMethod['methodName'] = method.name
			singleMethod['dependentMethods'] = findDependendantMethods(functionDependency, method.name)
			changedMethods.append(singleMethod)
		singleFile['changedMethods'] = changedMethods
		files.append(singleFile)
	singleCommit['changedFiles'] = files
	ans.append(singleCommit)
	
	
for commit in ans:
	print(json.dumps(commit, indent=4,default=str))

with open(sys.argv[3], 'w', encoding='utf-8') as f:
    json.dump(ans, f, ensure_ascii=False, indent=4)
