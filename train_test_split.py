
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree


# In[3]:


iris=load_iris()


# In[6]:


#now spliting trainning and testing dataset testing data 10%
split_data=train_test_split(iris.data,iris.target,test_size=0.1)


# In[7]:


train_data,test_data,train_target,test_target=split_data


# In[9]:


features=train_data
label=train_target


# In[13]:


#calling clf
dsc_clf=tree.DecisiontTreeClassifier()
trained=dsc_clf.fit(train_data,train_target)


# In[12]:


test_target

