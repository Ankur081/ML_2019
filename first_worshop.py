#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello poornima university student in python AI')


# In[2]:


print('hello python')
print('i am a ankur jain')


# In[3]:


myint =10
mystring ='hello'
mystring1 ='Aj is back'
print(myint)
print(mystring)
print(mystring1)


# In[4]:


demo1 =10
print(id(demo1))


# In[6]:


demo2 =10
print(id(demo2))


# In[7]:


num1 = 10
num2 = 20
print(num1 + num2)


# In[8]:


num1 = input("enter the number")
num2 = input("enter the number")
print(num1 + num2)


# In[10]:


def show(var1,var2):
    print('hello from show')
    return(var1+var2)
print('welcome')
print(show(20,30))


# In[13]:


var1 =4
if var1 > 5:
    print('value is greater')
else:
    print('value is less')


# In[14]:


mylist =[1,2,3,45]
print(mylist)
print(type(mylist))
print(mylist[1:2])


# In[17]:


myset ={2,3,45}
print(myset)
print(type(myset))
#print(mylist[1:2])


# In[18]:


mydict={1:"one",2:"two",3:"three"}
print(mydict)
print(type(mydict))


# In[21]:


print(dir(__builtins__))


# In[29]:


mydict={1:"one",2:"two",3:"three"}
for x in mydict.items():
    print(x)


# In[27]:


def shopping(item,price):
    print("item is",item)
    print("price is" ,price)
    
shopping(10,200)
shopping(price=200,item=10)


# In[28]:


class demo:
    def show(self):
        print("hello i am ankur jain")
d =demo()
d.show()


# In[30]:


x =[10,20,30,40]
print(x[ : : -1])
print(x[ 1:3:2])
print(x[2:3])


# In[37]:


class demo1:
    def show1(self):
        a=100
        b=200
        self.a=10
        self.b=20
        self._b=20
        print('sum krlo yar')
        print(a+b)
d = demo1()
d.show1()
print(d.a)
print(d.b)
print(d._b)


# In[41]:


class student:
    def show4(self,name,clas,*marks):
        print("name",name)
        print("clas",clas)
        print("marks",marks)
d =student()
d.show4("arun",10,20,30,40,50)


# In[ ]:




