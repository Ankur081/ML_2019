
# coding: utf-8

# In[1]:


#  analysis iris flower data sets with decisionTreeClassifier 

#import  sklearn.datasets
# import all datasets 
#dir(sklearn.datasets)
from sklearn.datasets  import  load_iris
from  sklearn import  tree
import numpy as np
iris=load_iris()

dir(iris)   # printing  all function 



#print(iris.data)  #  data of features 

#print(iris.target_names) #  output as  name of flowers
#print(iris.target)  #  target output in number format as per feautres names
#  here 0 means setosa  1  means versicolor and 2 means virginica


# In[3]:


print(iris.feature_names)


# In[4]:


print(iris.data[0])


# In[5]:


print(iris.target_names)


# In[8]:


print(iris.target[0])


# In[9]:


print(iris.filename)


# In[11]:


print(iris.DESCR)


# In[13]:


# now time for testing data

training_target1=iris.target[0]
training_target2=iris.target[50]
training_target3=iris.target[100]
print(training_target1,training_target2,training_target3)

# rather than doing this we can use numpy 
#target_output=np.delete(iris.target,[0,50,100])  #  we have removed one data for each flower output
#target_output


# In[14]:


#  testing data
training_data=np.delete(iris.data,[0,50,100],axis=0) # removed one set of each for featues
training_data


# In[15]:


#testing
test_data=iris.data[[0,50,100]]
test_data


# In[16]:


clf=tree.DecisionTreeClassifier()
clf=clf.fit(training_data,target_output)
#  testing  target by printing
#print(test_output)
print(clf.predict(test_data))


# In[17]:


#  time for visual
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names,  
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data) 
graph

