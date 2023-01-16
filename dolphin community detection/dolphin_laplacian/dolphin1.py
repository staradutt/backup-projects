import pandas as pd 
import numpy as np 
import scipy 
import math
import networkx as nx 
import matplotlib.pyplot as plt
from numpy import linalg as LA 

#reading the graph xml file
DG=nx.read_gml('dolphins.gml')
#listing nodes
nodelist=list(DG.nodes())
edgelist=list(DG.edges())
#drawing the graph for visualisation
#nx.draw(DG,with_labels=True)


#creating the adjacency matrix
ad=nx.adjacency_matrix(DG).todense()
 

#Creating the degree matrix 
#degree=[]
degree_root=[]
for i in range(len(ad)):
#	degree.append(np.sum(ad[i,:]))
	degree_root.append(1/math.sqrt(np.sum(ad[i,:])))
#deg_mat=np.diagflat(degree)
deg_root_mat=np.diagflat(degree_root)


    

#normalised laplacian
nlm=np.eye(len(ad))-np.matmul(deg_root_mat,np.matmul(ad,deg_root_mat ) ) #Normalised lap=I-D^(-0.5)*A*D^(-0.5)
nlm1=nx.normalized_laplacian_matrix(DG).todense()#just to be safe


#eig vec ang aig val

arr,v=LA.eig(nlm)

#to find second smallest 
temp=1000000000000
pos=-1
for i in range(len(arr)):
	if arr[i]<temp:
		pos=i
		temp=arr[i]
temp2=1000000000000
pos2=-1
for i in range(len(arr)):
	if arr[i]>=temp and arr[i]<temp2 and i!=pos:
		pos2=i
		temp2=arr[i]

eigv2=v[:,pos2]
fiedler_v=np.transpose(np.sign(eigv2))

cl_1=[]
cl_2=[]

cluster_1=[]
cluster_2=[]
for i in range(len(nlm1)):
	if fiedler_v[0,i]==1:
		cluster_1.append(nodelist[i])
		cl_1.append(i)
	if fiedler_v[0,i]==-1:
		cluster_2.append(nodelist[i])
		cl_2.append(i)
#print fiedler_v,cluster_1,cluster_2
#creating table
c=pd.DataFrame({'dol_#':cl_1,'name':cluster_1}) 
d=pd.DataFrame({'dol_#':cl_2,'name':cluster_2})


#visualisation
pos=nx.spring_layout(DG)
nx.draw_networkx_nodes(DG,pos,nodelist=cluster_1,node_color='c',figsize=(10,10))
nx.draw_networkx_nodes(DG,pos,nodelist=cluster_2,node_color='y')


nx.draw_networkx_edges(DG,pos,edgelist=edgelist)
labels={}
for i in range(len(nodelist)):
	u=nodelist[i]
	labels[u]=u

nx.draw_networkx_labels(DG,pos,labels,font_size=8)


plt.axis('off')
plt.savefig('fig.png',figsize=(20,20))
plt.show()
f=open("Output.txt", "w") 
f.write('\n\ncluster1\n\n')
f.write(c.to_string(index=False))
f.write('\n\ncluster2\n\n')
f.write(d.to_string(index=False))
f.close()

#print pos

#print list(DG)
#print eigv2
#print eigv2[0,0]
#print eigv2[0,3]









#drawing the graph for visualisation
#nx.draw(DG,with_labels=True)
#plt.show()




#bullshit
#a=DG.number_of_nodes()
#DG.number_of_edges()
#print(a)