#!/usr/bin/env python
# coding: utf-8

# In[122]:


import pandas as pd
import numpy as np


# In[123]:


f = open('128ipd.data','r')
data = f.readlines()


# In[124]:


#read these data manually as they are at top

first_atom_at_line_no = 32 #specific for each data file
no_of_atoms = 16884 #specific for each data file
reactive_type = 9

last_atom_at_line_no = first_atom_at_line_no + no_of_atoms


# In[126]:


atom_ID = []
mol_ID = []
atom_type = []
charge = []
x_coord = []
y_coord = []
z_coord = []
atom_type_2 = []


# In[127]:


lo = range(first_atom_at_line_no - 1, last_atom_at_line_no - 1)
for i in lo:

    splitarr = data[i].split()
    atom_ID.append(int(splitarr[0]))
    mol_ID.append(int(splitarr[1]))
    atom_type.append(int(splitarr[2]))
    charge.append(float(splitarr[3]))
    x_coord.append(float(splitarr[4]))
    y_coord.append(float(splitarr[5]))
    z_coord.append(float(splitarr[6]))
    atom_type_2.append(splitarr[8])
    
    
    


# In[128]:


dgeba_arr = [] #this array stores the atom ID of starting atom of each dgeba molecule
ipd_arr = [] #this array // //  each ipd molecule


# In[129]:


count = 1
index = 1
for i in range(len(lo)):
    if mol_ID[i] != count:
        count = count + 1
        if atom_ID[i]-index > 40:
            dgeba_arr.append(index)
        else:
            ipd_arr.append(index)
        index = atom_ID[i]
ipd_arr.append(ipd_arr[-1]+30) #the above loop misses the last molecule. This is done to correct that.


# In[130]:


#the above loops fill out the dgeba and ipd arrays


# In[131]:


reactive_id = [] #array to contain atom ids of reactive carbon atoms
for x in dgeba_arr:
    reactive_id.append(x + 21)#every 21 st atom and 42nd atom of DGEBA molecule is reactive. Seen from ovito/vmd
    reactive_id.append(x + 42)


# In[132]:


reactive_indices = [ x + (first_atom_at_line_no - 1 - 1) for x in reactive_id] #indices of reactive atoms in main data matrix


# In[133]:


print(data[31])
print(data[43])
print(atom_ID[0])
print(x_coord[0])
print(atom_ID[12])
print(x_coord[12])


# In[143]:


copy_data = [x for x in data]
for i in reactive_indices:
    temp = i-31
    r1 = str(atom_ID[temp])
    r2 = str(mol_ID[temp])
    r3 = str(reactive_type)
    r4 = str(charge[temp])
    r5 = str(x_coord[temp])
    r6 = str(y_coord[temp])
    r7 = str(z_coord[temp])
    r8 = 'cr'
    string = '      '+r1 + '       ' + r2 + '   ' + r3 + '  ' + r4 + '  ' + r5 + '  ' + r6 + '  ' + r7 + '  # ' + r8 + '\n'
    copy_data[i] = string


# In[144]:


f1 = open('128ipd_edited.data','w') #create this file from terminal first
f1.writelines(copy_data)
f.close()
f1.close()


# In[ ]:





# In[ ]:




