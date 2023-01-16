import pandas as pd 
import numpy as np 
import scipy 
import math
import networkx as nx 
import matplotlib.pyplot as plt
from numpy import linalg as LA 
import community
#reading the graph xml file
DG=nx.read_gml('dolphins.gml')
#listing nodes
nodelist1=list(DG.nodes())
edgelist=list(DG.edges())
#drawing the graph for visualisation
#nx.draw(DG,with_labels=True)

partition = community.best_partition(DG)
pv= partition.values()
nodelist=partition.keys()



#print community.modularity(partition,DG)


def agglomerate(a,b):
	
	part={}
	for i in range(len(nodelist1)):
		part[nodelist[i]]=pv[i]
	
	
	if b==-1:
		for i in range(len(nodelist)):
			if part[nodelist[i]]==a:
				part[nodelist[i]]=0
			else:
				part[nodelist[i]]=1
	if b!=-1:
		for i in range(len(nodelist)):
			if part[nodelist[i]]==a or part[nodelist[i]]==b:
				part[nodelist[i]]=0
			else:
				part[nodelist[i]]=1



	return part,community.modularity(part,DG)
#now we have 4 clusters namely 0 1 2 3 , we need to merge them to get 2 clusters
#possibilities are - (0 and rest) (1 and rest) ....and similar  ...4 in #
#(1,2 and rest) and similar ...3 possibilities
#we find modularity of each partition and then select the one with highest modularity
#in agglomerate (p,a,b)
#for partitions of the type (a and rest) we use b=-1
#for partitions of the type ((a,b and rest)) we use a and b as it is

arr=[[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]



#creates array of modularity values for different clusterings
mod=[]
for i in range(len(arr)):
	part1,t=agglomerate(arr[i][0],arr[i][1])
	mod.append(t)

#finds partition with maximum modularity
t=-100
pos1=100
for i in range(len(mod)):
	if mod[i]>t:
		t=mod[i]
		pos1=i


#pos gives the position of max modularity hence position of best cluster

#best combbination:
best_part,best_mod=agglomerate(arr[pos1][0],arr[pos1][1])


bpv=best_part.values()
bpk=best_part.keys()

#creating arrays of names and indices in each cluster to be useful later
cl1=[]
cl2=[]
cl1_name=[]
cl2_name=[]
for i in range(len(best_part.values())):
	if bpv[i]==0:
		cl1.append(bpk[i])
		cl1_name.append(i)
	if bpv[i]==1:
		cl2.append(bpk[i])
		cl2_name.append(i)
c=pd.DataFrame({'dol_#':cl1,'name':cl1_name}) 
d=pd.DataFrame({'dol_#':cl2,'name':cl2_name})



pos=nx.spring_layout(DG)


nx.draw_networkx_nodes(DG,pos,nodelist=cl1,node_color='c',node_size=100)
nx.draw_networkx_nodes(DG,pos,nodelist=cl2,node_color='g',node_size=100)


nx.draw_networkx_edges(DG,pos,edgelist=edgelist)

labels={}
for i in range(len(nodelist)):
	u=nodelist[i]
	labels[u]=u

nx.draw_networkx_labels(DG,pos,labels,font_size=6)

	
plt.axis('off')
plt.savefig('fig.png',figsize=(20,20))
plt.show()

f=open("result.txt", "w") 
f.write('\n\ncluster1\n\n')
f.write(c.to_string(index=False))
f.write('\n\ncluster2\n\n')
f.write(d.to_string(index=False))
f.close()



