#!/usr/bin/env python
# coding: utf-8

# In[2]:


3,.05+5


# In[4]:


100*(1.1**7)


# In[1]:


savings = 100


# In[2]:


print(savings)


# In[4]:


print(savings*1.1**7)


# In[8]:


saving = 100
pct = 1.1
year = 7
print(saving*pct**year)


# In[9]:


saving*pct**year


# In[13]:


saving = 100
growth_multiplier = 1.1
year = 7
money = saving*growth_multiplier**year
print(money)


# In[14]:


'hello'


# In[15]:


desc = 'compound interest'
print(desc)


# In[16]:


profitable = True


# In[17]:


print(profitable)


# In[19]:


saving = 100
growth_multiplier = 1.1
year1 = saving*growth_multiplier
print(year1)
type(year1)


# In[2]:


desc = 'compound interest'
doubledesc = desc+' '+ desc
print(doubledesc)


# In[5]:


saving = 100
growth_multiplier = 1.1
year = 7
money = saving*growth_multiplier**year
print('I started with $' + str(saving) + ' and now I have $' +str(money) + '.' + ' Awesome!!!')


# In[6]:


pi_string = float()'3.1415926'
type(pi_string)


# In[2]:


hall=11.25
kit=18.0
liv=20.0
bed=10.75
bath=9.50
areas = [['hallway', hall], ['kicthen', kit], ['living room', liv], ['bedroom', bed], ['bathroom', bath]]
print(areas)
type(areas)


# In[5]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
print(areas[5])


# In[1]:


x=['a','b','c','d']
print(x[1] + x[3])


# In[1]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
eat_sleep_area=areas[3]+areas[9]
print(eat_sleep_area)


# In[3]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
downstairs=areas[0:6]
print(downstairs)


# In[3]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
downstairs=areas[-4:]
print(downstairs)


# In[2]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
downstairs=areas[-3:]
print(downstairs)


# In[5]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
areas[4]='chill zone'
print(areas)


# In[6]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
area_1=areas+['poolhouse',24.5]
print(area_1)


# In[7]:


areas=["hallway",11.25,"kitchen",18.0,"living Room",20.0,"bedroom",10.75,"bathroom",9.50]
area_1=areas+['poolhouse',24.5]
area_2=area_1+['garage']
print(area_2)


# In[9]:


areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]
del(areas[-2:])
print(areas)


# In[1]:


var1=[1,2,3,4]
var2=True
print(type(var1),type(var2))


# In[2]:


var1=[1,2,3,4]
print(len(var1))


# In[4]:


var2=56.87
var3=int(var2)
print(var3,type(var3))


# In[9]:


place='poolhouse'
print(place.count('o'))


# In[11]:


areas=[11.25,18.0,20.0,10.75,9.50]
position=areas.count(9.50)
print(position)


# In[2]:


fruits = ['apple']
fruits.append('cherry')
print(fruits)


# In[3]:


areas=[11.25,18.0,20.0,10.75,9.50]
areas.append(24.5)
areas.append(15.45)
print(areas)


# In[4]:


areas=[11.25,18.0,20.0,10.75,9.50]
areas.reverse()
print(areas)


# In[5]:


areas = [11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
areas.reverse()
print(areas)


# In[6]:


areas = [11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
areas.insert(2, 15.45)
print(areas)


# In[2]:


import math
r = 0.43
A = math.pi * r ** 2
print(A)


# In[2]:


import numpy as np
baseball=[180,215,210,210,188,176,209,200]
baseballnp = np.array(baseball)
print(baseballnp)
print(type(baseballnp))


# In[5]:


a = [1,2,3,5]
p=a*2
p


# In[27]:


import numpy as np
print(np_weight_lb[50])


# In[28]:


import numpy as np
print(np_height_in[100:111])


# In[29]:


import numpy as np
baseball= [[180,    78.4],[215,   102.7],[210,    98.5],[188,    75.2]]
np_baseball=np.array(baseball)
print(np_baseball.shape)


# In[38]:


import numpy as np
baseball =[[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180], [73, 188], [73, 180], [74, 185], [74, 160], [69, 180], [70, 185], [73, 189], [75, 185], [78, 219], [79, 230], [76, 205], [74, 230], [76, 195], [72, 180], [71, 192], [75, 225], [77, 203], [74, 195], [73, 182], [74, 188], [78, 200], [73, 180], [75, 200], [73, 200], [75, 245], [75, 240], [74, 215], [69, 185], [71, 175], [74, 199], [73, 200], [73, 215], [76, 200], [74, 205], [74, 206], [70, 186], [72, 188], [77, 220], [74, 210], [70, 195], [73, 200], [75, 200], [76, 212], [76, 224], [78, 210], [74, 205], [74, 220], [76, 195], [77, 200], [81, 260], [78, 228], [75, 270], [77, 200], [75, 210], [76, 190], [74, 220], [72, 180], [72, 205], [75, 210], [73, 220], [73, 211], [73, 200], [70, 180], [70, 190], [70, 170], [76, 230], [68, 155], [71, 185], [72, 185], [75, 200], [75, 225], [75, 225], [75, 220], [68, 160], [74, 205], [78, 235], [71, 250], [73, 210], [76, 190], [74, 160], [74, 200], [79, 205], [75, 222], [73, 195], [76, 205], [74, 220], [74, 220], [73, 170], [72, 185], [74, 195], [73, 220], [74, 230], [72, 180], [73, 220], [69, 180], [72, 180], [73, 170], [75, 210], [75, 215], [73, 200], [72, 213], [72, 180], [76, 192], [74, 235], [72, 185], [77, 235], [74, 210], [77, 222], [75, 210], [76, 230], [80, 220], [74, 180], [74, 190], [75, 200], [78, 210], [73, 194], [73, 180], [74, 190], [75, 240], [76, 200], [71, 198], [73, 200], [74, 195], [76, 210], [76, 220], [74, 190], [73, 210], [74, 225], [70, 180], [72, 185], [73, 170], [73, 185], [73, 185], [73, 180], [71, 178], [74, 175], [74, 200], [72, 204], [74, 211], [71, 190], [74, 210], [73, 190], [75, 190], [75, 185], [79, 290], [73, 175], [75, 185], [76, 200], [74, 220], [76, 170], [78, 220], [74, 190], [76, 220], [72, 205], [74, 200], [76, 250], [74, 225], [75, 215], [78, 210], [75, 215], [72, 195], [74, 200], [72, 194], [74, 220], [70, 180], [71, 180], [70, 170], [75, 195], [71, 180], [71, 170], [73, 206], [72, 205], [71, 200], [73, 225], [72, 201], [75, 225], [74, 233], [74, 180], [75, 225], [73, 180], [77, 220], [73, 180], [76, 237], [75, 215], [74, 190], [76, 235], [75, 190], [73, 180], [71, 165], [76, 195], [75, 200], [72, 190], [71, 190], [77, 185], [73, 185], [74, 205], [71, 190], [72, 205], [74, 206], [75, 220], [73, 208], [72, 170], [75, 195], [75, 210], [74, 190], [72, 211], [74, 230], [71, 170], [70, 185], [74, 185], [77, 241], [77, 225], [75, 210], [75, 175], [78, 230], [75, 200], [76, 215], [73, 198], [75, 226], [75, 278], [79, 215], [77, 230], [76, 240], [71, 184], [75, 219], [74, 170], [69, 218], [71, 190], [76, 225], [72, 220], [72, 176], [70, 190], [72, 197], [73, 204], [71, 167], [72, 180], [71, 195], [73, 220], [72, 215], [73, 185], [74, 190], [74, 205], [72, 205], [75, 200], [74, 210], [74, 215], [77, 200], [75, 205], [73, 211], [72, 190], [71, 208], [74, 200], [77, 210], [75, 232], [75, 230], [75, 210], [78, 220], [78, 210], [74, 202], [76, 212], [78, 225], [76, 170], [70, 190], [72, 200], [80, 237], [74, 220], [74, 170], [71, 193], [70, 190], [72, 150], [71, 220], [74, 200], [71, 190], [72, 185], [71, 185], [74, 200], [69, 172], [76, 220], [75, 225], [75, 190], [76, 195], [73, 219], [76, 190], [73, 197], [77, 200], [73, 195], [72, 210], [72, 177], [77, 220], [77, 235], [71, 180], [74, 195], [74, 195], [73, 190], [78, 230], [75, 190], [73, 200], [70, 190], [74, 190], [72, 200], [73, 200], [73, 184], [75, 200], [75, 180], [74, 219], [76, 187], [73, 200], [74, 220], [75, 205], [75, 190], [72, 170], [73, 160], [73, 215], [72, 175], [74, 205], [78, 200], [76, 214], [73, 200], [74, 190], [75, 180], [70, 205], [75, 220], [71, 190], [72, 215], [78, 235], [75, 191], [73, 200], [73, 181], [71, 200], [75, 210], [77, 240], [72, 185], [69, 165], [73, 190], [74, 185], [72, 175], [70, 155], [75, 210], [70, 170], [72, 175], [72, 220], [74, 210], [73, 205], [74, 200], [76, 205], [75, 195], [80, 240], [72, 150], [75, 200], [73, 215], [74, 202], [74, 200], [73, 190], [75, 205], [75, 190], [71, 160], [73, 215], [75, 185], [74, 200], [74, 190], [72, 210], [74, 185], [74, 220], [74, 190], [73, 202], [76, 205], [75, 220], [72, 175], [73, 160], [73, 190], [73, 200], [72, 229], [72, 206], [72, 220], [72, 180], [71, 195], [75, 175], [75, 188], [74, 230], [73, 190], [75, 200], [79, 190], [74, 219], [76, 235], [73, 180], [74, 180], [74, 180], [72, 200], [74, 234], [74, 185], [75, 220], [78, 223], [74, 200], [74, 210], [74, 200], [77, 210], [70, 190], [73, 177], [74, 227], [73, 180], [71, 195], [75, 199], [71, 175], [72, 185], [77, 240], [74, 210], [70, 180], [77, 194], [73, 225], [72, 180], [76, 205], [71, 193], [76, 230], [78, 230], [75, 220], [73, 200], [78, 249], [74, 190], [79, 208], [75, 245], [76, 250], [72, 160], [75, 192], [75, 220], [70, 170], [72, 197], [70, 155], [74, 190], [71, 200], [76, 220], [73, 210], [76, 228], [71, 190], [69, 160], [72, 184], [72, 180], [69, 180], [73, 200], [69, 176], [73, 160], [74, 222], [74, 211], [72, 195], [71, 200], [72, 175], [72, 206], [76, 240], [76, 185], [76, 260], [74, 185], [76, 221], [75, 205], [71, 200], [72, 170], [71, 201], [73, 205], [75, 185], [76, 205], [75, 245], [71, 220], [75, 210], [74, 220], [72, 185], [73, 175], [73, 170], [73, 180], [73, 200], [76, 210], [72, 175], [76, 220], [73, 206], [73, 180], [73, 210], [75, 195], [75, 200], [77, 200], [73, 164], [72, 180], [75, 220], [70, 195], [74, 205], [72, 170], [80, 240], [71, 210], [71, 195], [74, 200], [74, 205], [73, 192], [75, 190], [76, 170], [73, 240], [77, 200], [72, 205], [73, 175], [77, 250], [76, 220], [71, 224], [75, 210], [73, 195], [74, 180], [77, 245], [71, 175], [72, 180], [73, 215], [69, 175], [73, 180], [70, 195], [74, 230], [76, 230], [73, 205], [73, 215], [75, 195], [73, 180], [79, 205], [74, 180], [73, 190], [74, 180], [77, 190], [75, 190], [74, 220], [73, 210], [77, 255], [73, 190], [77, 230], [74, 200], [74, 205], [73, 210], [77, 225], [74, 215], [77, 220], [75, 205], [77, 200], [75, 220], [71, 197], [74, 225], [70, 187], [79, 245], [72, 185], [72, 185], [70, 175], [74, 200], [74, 180], [72, 188], [73, 225], [72, 200], [74, 210], [74, 245], [76, 213], [82, 231], [74, 165], [74, 228], [70, 210], [73, 250], [73, 191], [74, 190], [77, 200], [72, 215], [76, 254], [73, 232], [73, 180], [72, 215], [74, 220], [74, 180], [71, 200], [72, 170], [75, 195], [74, 210], [74, 200], [77, 220], [70, 165], [71, 180], [73, 200], [76, 200], [71, 170], [75, 224], [74, 220], [72, 180], [76, 198], [79, 240], [76, 239], [73, 185], [76, 210], [78, 220], [75, 200], [76, 195], [72, 220], [72, 230], [73, 170], [73, 220], [75, 230], [71, 165], [76, 205], [70, 192], [75, 210], [74, 205], [75, 200], [73, 210], [71, 185], [71, 195], [72, 202], [73, 205], [73, 195], [72, 180], [69, 200], [73, 185], [78, 240], [71, 185], [73, 220], [75, 205], [76, 205], [70, 180], [74, 201], [77, 190], [75, 208], [79, 240], [72, 180], [77, 230], [73, 195], [75, 215], [75, 190], [75, 195], [73, 215], [73, 215], [76, 220], [77, 220], [75, 230], [70, 195], [71, 190], [71, 195], [75, 209], [74, 204], [69, 170], [70, 185], [75, 205], [72, 175], [75, 210], [73, 190], [72, 180], [72, 180], [72, 160], [76, 235], [75, 200], [74, 210], [69, 180], [73, 190], [72, 197], [72, 203], [75, 205], [77, 170], [76, 200], [80, 250], [77, 200], [76, 220], [79, 200], [71, 190], [75, 170], [73, 190], [76, 220], [77, 215], [73, 206], [76, 215], [70, 185], [75, 235], [73, 188], [75, 230], [70, 195], [69, 168], [71, 190], [72, 160], [72, 200], [73, 200], [70, 189], [70, 180], [73, 190], [76, 200], [75, 220], [72, 187], [73, 240], [79, 190], [71, 180], [72, 185], [74, 210], [74, 220], [74, 219], [72, 190], [76, 193], [76, 175], [72, 180], [72, 215], [71, 210], [72, 200], [72, 190], [70, 185], [77, 220], [74, 170], [72, 195], [76, 205], [71, 195], [76, 210], [71, 190], [73, 190], [70, 180], [73, 220], [73, 190], [72, 186], [71, 185], [71, 190], [71, 180], [72, 190], [72, 170], [74, 210], [74, 240], [74, 220], [71, 180], [72, 210], [75, 210], [72, 195], [71, 160], [72, 180], [72, 205], [72, 200], [72, 185], [74, 245], [74, 190], [77, 210], [75, 200], [73, 200], [75, 222], [73, 215], [76, 240], [72, 170], [77, 220], [75, 156], [72, 190], [71, 202], [71, 221], [75, 200], [72, 190], [73, 210], [73, 190], [71, 200], [70, 165], [75, 190], [71, 185], [76, 230], [73, 208], [68, 209], [71, 175], [72, 180], [74, 200], [77, 205], [72, 200], [76, 250], [78, 210], [81, 230], [72, 244], [73, 202], [76, 240], [72, 200], [72, 215], [74, 177], [76, 210], [73, 170], [76, 215], [75, 217], [70, 198], [71, 200], [74, 220], [72, 170], [73, 200], [76, 230], [76, 231], [73, 183], [71, 192], [68, 167], [71, 190], [71, 180], [74, 180], [77, 215], [69, 160], [72, 205], [76, 223], [75, 175], [76, 170], [75, 190], [76, 240], [72, 175], [74, 230], [76, 223], [74, 196], [72, 167], [75, 195], [78, 190], [77, 250], [70, 190], [72, 190], [79, 190], [74, 170], [71, 160], [68, 150], [77, 225], [75, 220], [71, 209], [72, 210], [70, 176], [72, 260], [72, 195], [73, 190], [72, 184], [74, 180], [72, 195], [72, 195], [75, 219], [72, 225], [73, 212], [74, 202], [72, 185], [78, 200], [75, 209], [72, 200], [74, 195], [75, 228], [75, 210], [76, 190], [74, 212], [74, 190], [73, 218], [74, 220], [71, 190], [74, 235], [75, 210], [76, 200], [74, 188], [76, 210], [76, 235], [73, 188], [75, 215], [75, 216], [74, 220], [68, 180], [72, 185], [75, 200], [71, 210], [70, 220], [72, 185], [73, 231], [72, 210], [75, 195], [74, 200], [70, 205], [76, 200], [71, 190], [82, 250], [72, 185], [73, 180], [74, 170], [71, 180], [75, 208], [77, 235], [72, 215], [74, 244], [72, 220], [73, 185], [78, 230], [77, 190], [73, 200], [73, 180], [73, 190], [73, 196], [73, 180], [76, 230], [75, 224], [70, 160], [73, 178], [72, 205], [73, 185], [75, 210], [74, 180], [73, 190], [73, 200], [76, 257], [73, 190], [75, 220], [70, 165], [77, 205], [72, 200], [77, 208], [74, 185], [75, 215], [75, 170], [75, 235], [75, 210], [72, 170], [74, 180], [71, 170], [76, 190], [71, 150], [75, 230], [76, 203], [83, 260], [75, 246], [74, 186], [76, 210], [72, 198], [72, 210], [75, 215], [75, 180], [72, 200], [77, 245], [73, 200], [72, 192], [70, 192], [74, 200], [72, 192], [74, 205], [72, 190], [71, 186], [70, 170], [71, 197], [76, 219], [74, 200], [76, 220], [74, 207], [74, 225], [74, 207], [75, 212], [75, 225], [71, 170], [71, 190], [74, 210], [77, 230], [71, 210], [74, 200], [75, 238], [77, 234], [76, 222], [74, 200], [76, 190], [72, 170], [71, 220], [72, 223], [75, 210], [73, 215], [68, 196], [72, 175], [69, 175], [73, 189], [73, 205], [75, 210], [70, 180], [70, 180], [74, 197], [75, 220], [74, 228], [74, 190], [73, 204], [74, 165], [75, 216], [77, 220], [73, 208], [74, 210], [76, 215], [74, 195], [75, 200], [73, 215], [76, 229], [78, 240], [75, 207], [73, 205], [77, 208], [74, 185], [72, 190], [74, 170], [72, 208], [71, 225], [73, 190], [75, 225], [73, 185], [67, 180], [67, 165], [76, 240], [74, 220], [73, 212], [70, 163], [75, 215], [70, 175], [72, 205], [77, 210], [79, 205], [78, 208]]
np_baseball = np.array(baseball)
print(np_baseball[49])


# In[43]:


import numpy as np
height=np_baseball[123,0]
print(height)


# In[5]:


import numpy as np
price_2020x = [[690,199.00],[199,192.00],[959,913.00],[683,129.00],[188,510.00],[592,207.00],[245,507.00]]
np_price_2020x = np.array(price_2020x)
np_price_2020x = np_price_2020x + 100
print(np_price_2020x)


# In[3]:


import pandas as pd
import numpy as np

baseball = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/mlbData.csv')
np_baseball = np.array(baseball)
print(np.std(np_baseball[:,0]))


# In[6]:


import pandas as pd
import numpy as np

baseball = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/mlbData.csv')
np_baseball = np.array(baseball)
np_height = np_baseball[:,0]
np_weight = np_baseball[:,1]
corr = np.corrcoef(np_height,np_weight)
print(corr[0,1])


# In[14]:


import pandas as pd
import numpy as np
fifa = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/fifapos.csv')
np_fifa = np.array(fifa)
np_position = np_fifa[:,0]
np_height = np_fifa[:,1]
gk = np_height[np_position != ' GK']
print(np.median(gk))


# In[21]:


import numpy as np
neg_list = list(range(-100, 0))
print(neg_list)


# In[12]:


import matplotlib.pyplot as plt
pop=[2.53,2.57,2.62,2.67,2.71,2.76,2.81,2.86,2.92,2.97,3.03,3.08,3.14,3.2,3.26,3.33,3.4,3.47,3.54,3.62,3.69,3.77,3.84,3.92,4.,4.07,4.15,4.22,4.3,4.37,4.45,4.53,4.61,4.69,4.78,4.86,4.95,5.05,5.14,5.23,5.32,5.41,5.49,5.58,5.66,5.74,5.82,5.9,5.98,6.05,6.13,6.2,6.28,6.36,6.44,6.51,6.59,6.67,6.75,6.83,6.92,7.,7.08,7.16,7.24,7.32,7.4,7.48,7.56,7.64,7.72,7.79,7.87,7.94,8.01,8.08,8.15,8.22,8.29,8.36,8.42,8.49,8.56,8.62,8.68,8.74,8.8,8.86,8.92,8.98,9.04,9.09,9.15,9.2,9.26,9.31,9.36,9.41,9.46,9.5,9.55,9.6,9.64,9.68,9.73,9.77,9.81,9.85,9.88,9.92,9.96,9.99,10.03,10.06,10.09,10.13,10.16,10.19,10.22,10.25,10.28,10.31,10.33,10.36,10.38,10.41,10.43,10.46,10.48,10.5,10.52,10.55,10.57,10.59,10.61,10.63,10.65,10.66,10.68,10.7,10.72,10.73,10.75,10.77,10.78,10.79,10.81,10.82,10.83,10.84,10.85]
year_list = list(range(1950,2101))
plt.plot(np_year,np_pop)
plt.show()



# In[19]:


import matplotlib.pyplot as plt
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
savings = [209,250,209,297,356,388,305,397,362,237,282,238]
plt.scatter(month,savings)
plt.show


# In[15]:


import pandas as pd
import numpy as np
country_Data = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv')
np_country_Data=np.array(country_Data)
gdp_cap=np_country_Data[:,6]
life_exp = np_country_Data[:,5]
print(gdp_cap[-1], life_exp[-1])


# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
country_Data = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv')
np_country_Data=np.array(country_Data)
gdp_cap=np_country_Data[:,6]
life_exp = np_country_Data[:,5]
plt.scatter(gdp_cap,life_exp)
plt.xscale('log')
plt.show


# In[36]:



import matplotlib.pyplot as plt
life_exp1950 = [28.8,55.23,43.08,30.02,62.48,69.12,66.8,50.94,37.48,68.0,38.22,40.41,53.82,47.62,50.92,59.6,31.98,39.03,39.42,38.52,68.75,35.46,38.09,54.74,44.0,50.64,40.72,39.14,42.11,57.21,40.48,61.21,59.42,66.87,70.78,34.81,45.93,48.36,41.89,45.26,34.48,35.93,34.08,66.55,67.41,37.0,30.0,67.5,43.15,65.86,42.02,33.61,32.5,37.58,41.91,60.96,64.03,72.49,37.37,37.47,44.87,45.32,66.91,65.39,65.94,58.53,63.03,43.16,42.27,50.06,47.45,55.56,55.93,42.14,38.48,42.72,36.68,36.26,48.46,33.68,40.54,50.99,50.79,42.24,59.16,42.87,31.29,36.32,41.72,36.16,72.13,69.39,42.31,37.44,36.32,72.67,37.58,43.44,55.19,62.65,43.9,47.75,61.31,59.82,64.28,52.72,61.05,40.0,46.47,39.88,37.28,58.0,30.33,60.4,64.36,65.57,32.98,45.01,64.94,57.59,38.64,41.41,71.86,69.62,45.88,58.5,41.22,50.85,38.6,59.1,44.6,43.58,39.98,69.18,68.44,66.07,55.09,40.41,43.16,32.55,42.04,48.45
bin=15
plt.hist(life_exp1950,bin)
plt.show()


# In[37]:


import matplotlib.pyplot as plt
life_exp1950 = [28.8,55.23,43.08,30.02,62.48,69.12,66.8,50.94,37.48,68.0,38.22,40.41,53.82,47.62,50.92,59.6,31.98,39.03,39.42,38.52,68.75,35.46,38.09,54.74,44.0,50.64,40.72,39.14,42.11,57.21,40.48,61.21,59.42,66.87,70.78,34.81,45.93,48.36,41.89,45.26,34.48,35.93,34.08,66.55,67.41,37.0,30.0,67.5,43.15,65.86,42.02,33.61,32.5,37.58,41.91,60.96,64.03,72.49,37.37,37.47,44.87,45.32,66.91,65.39,65.94,58.53,63.03,43.16,42.27,50.06,47.45,55.56,55.93,42.14,38.48,42.72,36.68,36.26,48.46,33.68,40.54,50.99,50.79,42.24,59.16,42.87,31.29,36.32,41.72,36.16,72.13,69.39,42.31,37.44,36.32,72.67,37.58,43.44,55.19,62.65,43.9,47.75,61.31,59.82,64.28,52.72,61.05,40.0,46.47,39.88,37.28,58.0,30.33,60.4,64.36,65.57,32.98,45.01,64.94,57.59,38.64,41.41,71.86,69.62,45.88,58.5,41.22,50.85,38.6,59.1,44.6,43.58,39.98,69.18,68.44,66.07,55.09,40.41,43.16,32.55,42.04,48.45]
bin=15
plt.hist(life_exp1950,bin)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
savings = [209,250,209,297,356,388,305,397,362,237,282,238]
plt.scatter(month,savings)
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('world Development')
plt.show


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
country_Data = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv')
population=np.array(country_Data)
pop=(population[:,3])
life_exp =(population[:,5])
plt.scatter()
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('world Development')
plt.show()


# In[10]:


import pandas as pd
import numpy as np
country_Data=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv')
np_country_Data=np.array(country_Data)
gdp_cap=np_country_Data[:,6]
life_exp = np_country_Data[:,5]
plt.scatter(gdp_cap, life_exp)
x=[1000,10000,100000]
plt.xticks([1000,10000,100000],['1k','10k','100k'])
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development')
plt.show()


# In[12]:


import matplotlib.pyplot as plt
x=[10,20,30,40]
y=[5,10,15,20]
plt.scatter(x,y)
plt.xticks([10,20,30,40],['ten','twenty','thirty','fourty'])
plt.yticks([5,10,15,20],['five','ten','fifteen','twenty'])
plt.show()


# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pop=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/popdata.csv')
np_country_Data=np.array(country_Data)
gdp_cap=np_country_Data[:,6]
np_pop=np.array(pop)
np_pop=np_pop*2


# In[8]:


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
country_Data=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/gapminder.csv')
#gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.
np_country_Data=np.array(country_Data)
gdp_cap=np_country_Data[:,6]
#life_exp which contains the life expectancy for each country
life_exp = np_country_Data[:,5]
population_Data =pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/popdata.csv')
pop=np.array(population_Data)
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop=np.array(pop)
# Double np_pop
np_pop=np_pop*2
# Update: set s argument to np_pop
col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']
plt.scatter(gdp_cap, life_exp, s=np_pop, c=col, alpha=0.8)
plt.grid(True)
plt.text(5300,80,'India')
plt.text(58700,80,'China')
# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
# Display the plot
plt.show()


# In[9]:


countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
ind_ger=countries.index("germany")
print(ind_ger)
print(capitals[ind_ger])


# In[15]:


countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
europe ={'spain': 'madrid', 'germany': 'berlin', 'france':'paris', 'norway': 'oslo'}

europe['italy']='rome'
europe['poland']='warsaw'
europe['iceland']='reykjavik'
europe['australia']='vienna'
europe['germany']='bonn'
print(europe)


# In[14]:


europe['germany']='berlin'
print(europe)


# In[16]:


del(europe['australia'])
print(europe)


# In[17]:


print(europe)


# In[18]:


europe['germany']='berlin'


# In[19]:


print(europe)


# In[27]:


spain={ 'capital':'madrid', 'population':46.77 }
france= { 'capital':'paris', 'population':66.03 }
germany= { 'capital':'berlin', 'population':80.62 }
norway ={ 'capital':'oslo', 'population':5.084 }

europe={'spain':{'spain'}, 'france':{'capital':'paris', 'population':66.03}, 'germany':{'capital':'berlin', 'population':80.62}, 'norway':{'capital':'oslo', 'population':5.084}}
print(europe)


# In[23]:


print(europe['france']['capital'])


# In[26]:


data={'capital':'rome', 'population':59.83}

europe['italy']=data
print(europe)


# In[40]:


import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}
my_dict=pd.DataFrame(my_dict)
print(my_dict)


# In[41]:


import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}
my_dict=pd.DataFrame(my_dict)
print(my_dict)


# In[4]:


import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}
my_dict=pd.DataFrame(my_dict)
row_labels=['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
my_dict.index=row_labels
print(my_dict)


# In[8]:


import pandas as pd
cars=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv')
cars[3:6]


# In[10]:


cars[['country','drives_right']]


# In[13]:


cars[3:6]


# In[53]:


import pandas as pd
cars=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv', index_col=0)
print(cars)
cars.loc[:,['cars_per_cap']]


# In[3]:


print(True==1)


# In[11]:


import numpy as np
np_my_house = np.array([18.0, 20.0, 10.75, 9.50])
np_your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(np.less(np_my_house,np_your_house))


# In[17]:


import numpy as np
my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen*2<your_kitchen*3)


# In[20]:


import numpy as np
np_my_house = np.array([18.0, 20.0, 10.75, 9.50])
np_your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(np.logical_and(np_my_house<11,np_your_house<11))


# In[31]:


room = 'kit'
area = 14.0
if(area>15):
 print('Big place')
elif(area>10):
    print('Medium size, nice!')
else:
    print('Pretty small')


# In[37]:


import pandas as pd
import numpy as np
ser=['g','e','e','k','s','f','o','r','g','e','e','k','s']
ser_ser=pd.Series(ser)
print(ser_ser)
print(type(ser_ser))


# In[44]:


import pandas as pd
cars = pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv', index_col = 0)
dr = pd.Series(cars['drives_right'])
sel=cars[dr]
print(sel)


# In[ ]:


offset = 10
while offset!=0:
    print('correcting...')
    offset=offset-1


# In[3]:


offset = 10
while offset!=0:
    print('correcting...')
    offset=offset-1
    


# In[7]:


offset=10
while offset!=0:
    if(offset==5):
        print('Five is the best!')
        break
    else:
        print('I am not five')
    offset=offset-1


# In[1]:


areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for number in areas:
    print(number)


# In[2]:


areas1 = [11.25, 18.0, 20.0, 10.75, 9.50]
areas2 = [10.50, 17.25, 30.0, 23.75, 5.0]
for number in areas2:
    areas1.append(number)
print(areas1)


# In[4]:


area = [11.25, 18.0, 20.0, 10.75, 9.50]
for i, h in enumerate(area):
 print('room '+str(i) +':'+' '+str(h))


# In[8]:


student_info = {'firstname': 'Richard', 
                'lastname':'Branson', 
                'age': 24, 
                'email':'rbranson@gmail.com'}
for a,b in student_info:
    print(student_info[a])


# In[10]:


europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna'}
for a,b in europe.items():
    print('The capital of '+a+' is '+b)


# In[34]:


import numpy as np
import pandas as pd
cars=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv', index_col=0)
# print(cars)
for index, row in cars.iterrows():
    print(str(index)+': ' +str(row['cars_per_cap']))


# In[31]:


import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/nba.csv', index_col=0)
for index, rows in data.iterrows():
    print(str(index) + ": "+ str(rows["Age"]))


# In[64]:


import numpy as np
import pandas as pd
cars=pd.read_csv('https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/cars.csv', index_col=0)
# print(cars)
for x, y in cars.iterrows():
     if y['drives_right'] == True:
        cars.loc[x, 'Drives'] = 'right'
     else:
        cars.loc[x, 'Drives'] = 'left'
print(cars)


# In[59]:


for x, y in cars.iterrows():
    if y['drives_right'] == True:
        cars.loc[x, 'Drives'] = 'Right'
    else:
        cars.loc[x, 'Drives'] = 'Left'
print(cars)


# In[1]:


import pandas as pd
players_df = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
players_df
# players_df_group=players_df.groupby(['teamid', 'bats'])['salary'].describe()
# players_df_group


# In[7]:


import pandas as pd
players_df = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
# players_df
Major=players_df.groupby(['teamid'])['salary'].min()
print(Major)


# In[12]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")

year=data[data['yearid']>2000]
mean=year.groupby(['teamid'])['salary'].mean()
print(mean)


# In[13]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
non_duplicate=data.drop_duplicates(['namefirst'], ['yearid'])
pivottable=non_duplicate.pivot(index='namefirst', columns='yearid', values='salary')
print(pivottable)


# In[ ]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
non_duplicate=data.drop_duplicates(['playerid', 'yearid'])
pivottable=non_duplicate.pivot(index='playerid', columns='yearid', values='salary').reset_index()
pivottablemelt=pd.melt(frame=pivottable,id_vars='player_id', var_name='yearid', value_name='salary')
print(pivottablemelt)


# In[22]:


import pandas as pd
import numpy as np
# Import pandas
import pandas as pd
# Read the file into a DataFrame: df
players_df = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
players_df
#getting rid of duplicates

years = players_df.drop_duplicates(['playerid', 'yearid'])
#creating the pivot table
years_pivot = years.pivot(index='playerid', columns='yearid', values='salary').reset_index()
#print
years_pivot
melt = pd.melt(frame=years_pivot, id_vars = ['playerid'], var_name='yearid', value_name='salary')
melt


# In[4]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
non_duplicate=data.drop_duplicates(['playerid', 'yearid'])
pivottable=non_duplicate.pivot(index='playerid', columns='yearid', values='salary').reset_index()
pivottablemelt=pd.melt(frame=pivottable,id_vars='playerid', var_name='yearid', value_name='salary')
pivottablemelt


# In[2]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/salaries.csv")
data2 = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/people.csv")
mergeddata = pd.merge(data, data2)
mergeddata


# In[18]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
data
# data.loc[(data['weight'].between(210,230))]
# cond1 = data['weight']>=210
# cond2 = data['weight']<=230
# fullcond=cond1&cond2
# data[fullcond]

# years=data[(data['yearid'].between(2011,2016))]
# years


# In[34]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
# cond1=data['weight']>200
# cond2=data['height']>50
# fullcond=cond1&cond2
# data[fullcond]

cond=data[(data['yearid']>2007)|(data['birthyear']>1990)]
cond


# In[40]:


import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/players.csv")
data['BMI']= (data['weight'] * 703) / (data['height'] * data['height'] )
cond=data[(data['BMI'].between(20,27))|(data['birthcountry'].between('USA','Venezuela'))]
cond


# In[2]:


def sum_of_two_numbers(x,y):
    print((x+y)**2)

sum_of_two_numbers(5,9)


# In[4]:


def my_phrase(x,y):
    return x+', '+y

a=my_phrase('Hello','World')
a


# In[11]:




def show_list(my_list):
    for value in my_list:
        print(value)

show_list([1,2,3,4,5])
   
    


# In[18]:


import datetime as dt
print(dt.datetime.now().strftime('%B-%d-%Y'+', '+'%I:%M %p'))


# In[23]:


import datetime as dt
birthday = dt.date(1995,2,13)
print('My month of birth is:',birthday.strftime('%B'))


# In[28]:


slice = 'Python slice string'
print(slice[0:5])
print(slice[-5:])
print(slice[1:7])
print(slice[0:10:2])


# In[8]:


split ='split() function is used to split a string into the list of strings based on a delimiter.'
split=split.split(sep=(' '),maxsplit=2)
split


# In[12]:


split1String='split()|function|is|used|to|plit|a|string|into|the|list|of|strings|based|on|a|delimiter.'
split1String=split1String.split('|',maxsplit=3)
split1String


# In[13]:


#string
string= 'Data is the new oil for the 21st century'
# substring
substring ='new oil'
print(string.find(substring))
if string.find(substring) != 0:
    print("Found")
else:
    print("Not Found")


# In[8]:


#string
string= 'Data is the new oil for the 21st century'
# substring
print(string.replace('century','century!'))


# In[4]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv ")

print(students_df.head(5))
print(students_df.tail(5))
students_df.info()


# In[8]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")
students_df[['math score','writing score','reading score']].describe()


# In[3]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")

sns.distplot(students_df['math score'], kde=False)


# In[4]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")
sns.distplot(students_df['math score'])


# In[18]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")
sns.scatterplot(x='writing score', y='reading score', hue='race/ethnicity', size='test preparation course', data=students_df)


# In[21]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")
sns.jointplot(x='reading score',y='writing score', data=students_df )


# In[23]:


import pandas as pd
import matplotlib as plt
import seaborn as sns

students_df=pd.read_csv("https://raw.githubusercontent.com/Masadn/PythonCourse/master/dataset/StudentsPerformance.csv")
sns.boxplot(y='math score', data=students_df)


# In[1]:


import mysql.connector
#Connect Database
mydb = mysql.connector.connect(
  host="cassendra.cdjflmucstpo.us-east-1.rds.amazonaws.com",
  user="datawiz",
  passwd="datawiz123",
  database="cassendra" )
print(mydb)
# Get data from database and storing it in a dataframe
import pandas as pd
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM reviews")
data=list(mycursor)
data_df = pd.DataFrame([[x[0] for x in mycursor.description]] + data, dtype='object')
new_header = data_df.iloc[0] #grab the first row for the header
data_df = data_df[1:] #take the data less the header row
data_df.columns = new_header
data_df


# In[1]:


name = "Guido"
cost = 3
demand = "Bring me {} shrubberies, {}!"
print(demand.format(cost, name))


# In[2]:


line = "He said, \"Sure, let's rock!\"";
print(line)


# In[9]:


import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv')
data


# In[2]:


import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv')
x=data.drop(['Description','Temperature'], axis=1)
x.shape
x


# In[3]:


y=data['Temperature']
y.head(10)


# In[4]:


y.shape


# In[5]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[7]:


print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[9]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
tmodel = model.fit(x_train, y_train)
tmodel.score(x_test,y_test )


# In[10]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Data.csv')
df.dtypes
df.isna().sum()
df=df.dropna()
df.isna().sum()


# In[6]:


import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Data.csv')
df.dtypes
df.isna().sum()
mean_age=df.Age.mean()
df=df.Age.fillna(mean_age)
df.isna().sum()


# In[7]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Data.csv')
df.dtypes
df.isna().sum()
df=df.dropna()
df.isna().sum()


# In[6]:


import pandas as pd
df1=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/state-abbrevs')
df2=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/state_areas')
# df1[0:6]
# df2[0:8]
fulldata=pd.merge(df1,df2,on='state')
fulldata[:10]


# In[2]:


import numpy as np
import seaborn as sbn
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/german_credit_data.csv')
df
sbn.boxplot(df['Age'])


# In[10]:


import numpy as np
import seaborn as sbn
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Mall_Customers.csv')
# df
Q1=df['Annual Income'].quantile(0.25)
Q3=df['Annual Income'].quantile(0.75)
IQR=Q3-Q1

minimum=Q1-(1.5*IQR)
maximum=Q3+(1.5*IQR)

df=df[~((df['Annual Income']<minimum)|(df['Annual Income']>maximum))]
df
    
QQ1=df['Spending Score'].quantile(0.25)
QQ3=df['Spending Score'].quantile(0.75)
IQQR=QQ3-QQ1

minimumscore=QQ1-(1.5*IQQR)
maximumscore=QQ3+(1.5*IQQR)

print(minimumscore)
print(maximumscore)
df=df[~((df['Spending Score']<minimumscore)|(df['Spending Score']>maximumscore))]
df


# In[17]:


import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/student.csv")

df_cat=df.select_dtypes(exclude=[np.number])
df = df.drop(['Gender', 'Grade', 'Employed'], axis=1)

# df_cat

# df_cat.Gender.unique()

df_cat.Gender.replace({"Male": 0,"Female": 1},inplace=True)
df_cat.Grade.replace({'1st Class':1,'2nd Class':2,'3rd Class':3}, inplace=True)
df_cat.Employed.replace({'yes':1,'no':0}, inplace=True)
df_cat

data=pd.concat([df, df_cat],axis=1)
data


# In[5]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/student.csv')
df.dropna()
df_categ=df.select_dtypes(exclude=[np.number])
label_encoder=LabelEncoder()
for i in df_categ:
    df[i]=label_encoder.fit_transform(df[i])
df


# In[6]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
dataset = 'https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Banking_Marketing.csv'

#reading the data into the dataframe into the object data
df = pd.read_csv(dataset, header=0)
df = df.dropna()

data_column_category = df.select_dtypes(exclude = [np.number]).columns
data_column_category

label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])

onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoder = onehot_encoder.fit_transform(df[data_column_category])
df
onehot_encoder_frame = pd.DataFrame(onehot_encoder, columns=onehot_encoder.get_feature_names(data_column_category))
onehot_encoder_frame


# In[7]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

dataset = 'https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Banking_Marketing.csv'
df = pd.read_csv(dataset, header=0)

df = df.dropna()

data_column_category = df.select_dtypes(exclude = [np.number]).columns
data_column_category

label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])

onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category])

df

onehot_encoded_frame = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names(data_column_category))
onehot_encoded_frame


# In[9]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

dataset = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Banking_Marketing.csv"
df = pd.read_csv(dataset, header = 0)

df = df.dropna() #drop null values

data_column_category = df.select_dtypes(exclude=[np.number]).columns
data_column_category

label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])

onehot_encoder = OneHotEncoder(sparse = False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category])
df

onehot_encoded_frame = pd.DataFrame(onehot_encoded, columns = onehot_encoder.get_feature_names(data_column_category))
onehot_encoded_frame.columns

df_onehot_getdummies = pd.get_dummies(df[data_column_category], prefix=data_column_category[0])
data_onehot_encoded_data = pd.concat([df_onehot_getdummies, df[data_column_category]], axis = 1)
data_onehot_encoded_data


# In[16]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/student.csv')
df=df.dropna()

data_cat = df.select_dtypes(exclude=[np.number]).columns
data_cat

label_encoder = LabelEncoder()
for i in data_cat:
    df[i] = label_encoder.fit_transform(df[i])
    
onehot_encoder = OneHotEncoder(sparse = False)
onehot_encoded = onehot_encoder.fit_transform(df[data_cat])

onehot_encoded_frame = pd.DataFrame(onehot_encoded, columns = onehot_encoder.get_feature_names(data_cat))
onehot_encoded_frame.columns


# In[18]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

dataset = 'https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Banking_Marketing.csv'
df = pd.read_csv(dataset, header=0)

df = df.dropna()

data_column_category = df.select_dtypes(exclude=[np.number]).columns
data_column_category

df[data_column_category].head()

df_onehot_getdummies = pd.get_dummies(df[data_column_category], prefix=data_column_category)
data_onehot_encoded_data = pd.concat([df_onehot_getdummies,df[data_column_category]],axis = 1)
data_onehot_encoded_data


# In[20]:


import pandas as pd
from sklearn import preprocessing
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/scale.csv')
std_scale=preprocessing.StandardScaler().fit_transform(df)
scale_frame=pd.DataFrame(std_scale, columns=df.columns)
scale_frame


# In[2]:


import pandas as pd
from sklearn import preprocessing

data=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/scale.csv')
# data

minmax_scale=preprocessing.MinMaxScaler().fit_transform(data)
scaled_frame=pd.DataFrame(minmax_scale, columns=data.columns)
scaled_frame.head()


# In[3]:


import pandas as pd
data=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/discretization.csv')

label=['Silver','Gold','Platinum','Diamond']
label_range=[0,70000,100000,130000,200000]

data['cut_ex1']=pd.cut(data['ext_price'],bins=label_range,labels=label)
data


# In[3]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
#Loading th dataset
x = load_boston()
#Changing datatype tp a Pandas DataFrame
df = pd.DataFrame(x.data, columns = x.feature_names)
df["MEDV"] = x.target
#Features and Target
X = df.drop("MEDV", 1) #Feature Matrix
Y = df["MEDV"] #Target variable
df.head()
#Using pearson Correlation
plt.figure(figsize = (12,10))
cor = df.corr()
sns.heatmap(cor, annot = True, cmap = plt.cm.Greens)
plt.show()


# In[13]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
#Loading the dataset
x = load_boston()
#Changing data type to a Pandas DataFrame
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/pearson.csv')
df = pd.DataFrame(x.data, columns = x.feature_names)
df["Price"] = x.target
#Features and Target
X = df.drop("Price",1) #Feature Matrix
y = df["Price"] #Target Variable
df.head()
#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
#Correlation with output variable
cor_target = abs(cor["Price"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.5]
relevant_features
print(df[["LSTAT","PTRATIO"]].corr())
print(df[["RM","LSTAT"]].corr())


# In[12]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso

#Loading the dataset
df = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/pearson.csv')
X = df.drop('Price',1) #Feature Matrix
y = df['Price'] #Target Variable

#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
cor_target = abs(cor['Price'])

#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.5]
relevant_features


# In[5]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm


###########################################
# Wrapper Method - Backward Eliminiation  #
###########################################

#Loading the dataset
x = load_boston()
df = pd.DataFrame(x.data, columns = x.feature_names)
df["MEDV"] = x.target

#Features and Target
X = df.drop("MEDV",1) #Feature Matrix
y = df["MEDV"] #Target Variable
df.head()





####################################
#Backward Eliminatio Without a Loop#
####################################

#Adding constant column of ones, mandatory for sm.OLS model
#Fitting sm.OLS model
X_1 = sm.add_constant(X)
X_1
model = sm.OLS(y,X_1).fit()
model.pvalues




####################################
#Backward Elimination With a Loop   #
####################################
cols = list(X.columns) #13 Columns
pmax = 1
while(len(cols)>0):
    p = []
    X_1 = X[cols]
    X_1 = sm.add_constant(X_1)
    model = sm.OLS(y,X_1).fit()
    p = pd.Series(model.pvalues.values[1:],index = cols)
    pmax = max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)


# In[8]:


from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm


###########################################
# Wrapper Method - Backward Eliminiation  #
###########################################

#Loading the dataset
df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/pearson.csv')

#Features and Target
X = df.drop("Price",1) #Feature Matrix
y = df["Price"] #Target Variable
df.head()





####################################
#Backward Eliminatio Without a Loop#
####################################

#Adding constant column of ones, mandatory for sm.OLS model
#Fitting sm.OLS model
X_1 = sm.add_constant(X)
X_1
model = sm.OLS(y,X_1).fit()
model.pvalues




####################################
#Backward Elimination With a Loop   #
####################################
cols = list(X.columns) #13 Columns
pmax = 1
while(len(cols)>0):
    p = []
    X_1 = X[cols]
    X_1 = sm.add_constant(X_1)
    model = sm.OLS(y,X_1).fit()
    p = pd.Series(model.pvalues.values[1:],index = cols)
    pmax = max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)


# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


url = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/iris.csv"
dataset = pd.read_csv(url, header=0)
print(dataset)


#Features and Target
X = dataset.drop('Class', 1)
y = dataset['Class']


#Splitting into training/testing sets and scaling data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Applying Principal Component Analysis
pca = PCA() #can input the number of components
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_
explained_variance


# In[4]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


url = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/pima-indians-diabetes.data.csv"
dataset = pd.read_csv(url, header=0)
print(dataset)


#Features and Target
X = dataset.drop('Outcome', 1)
y = dataset['Outcome']


#Splitting into training/testing sets and scaling data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Applying Principal Component Analysis
pca = PCA() #can input the number of components
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_
explained_variance


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')


#Bringing In The Data
dataset = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/USA_Housing.csv"
df = pd.read_csv(dataset, header = 0)
# plt.xlabel('Avg. Area Income')
# plt.ylabel('Price')
# plt.scatter(df['Avg. Area Income'], df['Price'], color='red', marker='+')


#Divide into features and target
X = df.drop('Price', axis=1)
y = df['Price']


#Split My Data Into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X[['Avg. Area Income']], y, test_size=0.2, random_state=0)


#Building a Machine Learning Model
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test) #Can also enter individual values
# print(X_test)
predictions

#Visual
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, model.predict(X_train), color = "green")
plt.title('Price vs Avg. Area Income (Training set)')
plt.xlabel('Avg. Area Income')
plt.ylabel('Price')
plt.show()

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, model.predict(X_train), color = "green")
plt.title('Price vs Avg. Area Income (Testing set)')
plt.xlabel('Avg. Area Income')
plt.ylabel('Price')
plt.show()

# #Evaluate My ML Model Using R-Sqaured Statistical Measure
# model.score(X_test,y_test)
# metrics.mean_absolute_error(y_test, predictions)


# In[3]:


all_the_things = ['cats', 'dogs', 42, ['pizza', 'beer'], True] 
first_item = all_the_things[0] 
print("The first thing is" + " " + all_the_things[0])


# In[4]:


to_do = ["Conquer world", "Install Linux", "Change light bulb"]
current_task = to_do.pop()

print(to_do)


# In[2]:


values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
import matplotlib.pyplot as plt
ax = plt.axes()
ax.set_xlim([0, 11])
ax.set_ylim([1, 11])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.plot(range(1,11), values)
plt.show()


# In[4]:


values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
import matplotlib.pyplot as plt
ax = plt.axes()
ax.set_xlim([0, 11])
ax.set_ylim([1, 11])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.grid()
plt.plot(range(1,11), values)
plt.show()


# In[8]:


values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
import matplotlib.pyplot as plt
plt.plot(range(1,11), values, '?')
plt.plot(range(1,11), values2, ':')
plt.show()


# In[9]:


values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
import matplotlib.pyplot as plt
plt.plot(range(1,11), values, 'r')
plt.plot(range(1,11), values2, 'm')
plt.show()


# In[11]:


values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
import matplotlib.pyplot as plt
plt.plot(range(1,11), values, 'o')
plt.plot(range(1,11), values2, 'v:')
plt.show()


# In[14]:


values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
import matplotlib.pyplot as plt
line1 = plt.plot(range(1,11), values)
line2 = plt.plot(range(1,11), values2)
plt.legend(['First', 'Second'], loc=4)
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')


#Bringing In The Data
dataset = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv"
df = pd.read_csv(dataset, header = 0)
# plt.xlabel('Avg. Area Income')
# plt.ylabel('Price')
# plt.scatter(df['Avg. Area Income'], df['Price'], color='red', marker='+')


#Divide into features and target
X = df.drop('Temperature', axis=1)
y = df['Temperature']


#Split My Data Into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X[['Humidity']], y, test_size=0.2, random_state=0)


#Building a Machine Learning Model
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test) #Can also enter individual values
# print(X_test)
print(predictions)

#Visual
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, model.predict(X_train), color = "green")
plt.title('Temperature vs Humidity (Training set)')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_train, model.predict(X_train), color = "green")
plt.title('Temperature vs Humidity (Testing set)')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()

# #Evaluate My ML Model Using R-Sqaured Statistical Measure
print(model.score(X_test,y_test))
metrics.mean_absolute_error(y_test, predictions)


# In[10]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


dataset = "https://raw.githubusercontent.com/datawizardsai/Data-Science/master/weather.csv"
df = pd.read_csv(dataset, header = 0)


X = df.drop('Temperature', axis = 1) #features
y = df['Temperature'] #target


X_train, X_test, y_train, y_test = train_test_split(X[['Humidity','Wind_Speed_kmh','Wind_Bearing_degrees', 'Visibility_km', 'Pressure_millibars']], y, test_size=0.2, random_state=0)


model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test) #can also enter individual values
print(predictions)

print(model.score(X_test, y_test))
metrics.mean_absolute_error(y_test, predictions)


# In[5]:


#Predicts whether it will rain or not. 1 means yes, 0 means no.
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LogisticRegression #scikit-learn
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix


#Bring in the dataset
df = pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/iris.csv')
df


# Divide in features and target
X = df.drop('Class', axis=1) #features
y = df['Class'] #target


#Split in training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


#Build the ML Model - Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)


#Evaluate The ML Model Performance
model.score(X_test,y_test)
print(model.score(X_test,y_test))
cm = confusion_matrix(y_test, y_predicted)

#Vizualisation
sns.heatmap(cm, cmap="Reds", annot=True)


# In[3]:


# Predicts whether a patient has Diabetes or not.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn  import metrics
from sklearn.metrics import confusion_matrix


df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/cancer.csv")


X = df.drop('diagnosis',axis=1)
y = df['diagnosis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)


print(model.score(X_test,y_test))
confusion_matrix(y_test, y_predicted)


# In[3]:


# Predicts the specie of flower
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn  import metrics
from sklearn.metrics import confusion_matrix


df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Development%20Index.csv")
df


X = df.drop('Development Index',axis=1)
y = df['Development Index']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


model = RandomForestClassifier() #n_estimators=10 # 10 forests by default
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)


print(model.score(X_test,y_test))
confusion_matrix(y_test, y_predicted)


# In[4]:


#Predict the specie of flower
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd


#Bring in the dataset
df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/cancer.csv")


#Divide features and target
X = df.drop('diagnosis',axis=1)
y = df['diagnosis']


#Training and Testing Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Data Preprocessing
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# Building the model
classifier = KNeighborsClassifier(n_neighbors=7)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


#Evaluation
print(classifier.score(X_test,y_test))
confusion_matrix(y_test, y_pred)


# In[19]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df=pd.read_csv('https://raw.githubusercontent.com/datawizardsai/Data-Science/master/USA_Housing.csv')
df

X=df[['Avg. Area Income','Avg. Area House Age','Area Population']] #features
y=df['Price'] #target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=0)

clf=KNeighborsRegressor(20) #Number of K
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

print(mean_squared_error(y_test,y_pred))
print(mean_absolute_error(y_test,y_pred))
clf.score(X_test, y_test)


# In[20]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


#Bring in the dataset
df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/income.csv")
df


#Data Preprocessing
scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])
scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])


# #Visualizing the data 2-D
# plt.scatter(df.Age,df['Income($)'])
# plt.xlabel('Age')
# plt.ylabel('Income($)')


#Decide the features from which we want to find out the clusters
x = df[['Age','Income($)']] #features


#KMeans Clustering
km = KMeans(n_clusters=3) #K=3
y_predicted = km.fit_predict(x)
y_predicted


#Create a new columns in my dataset which will contain information about the clusters that are assigned
df['cluster']=y_predicted
df


#Visualizing the clustering result
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')
plt.xlabel('Age')
plt.ylabel('Income ($)')
plt.show()


# In[35]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
get_ipython().run_line_magic('matplotlib', 'inline')


df = pd.read_csv("https://raw.githubusercontent.com/datawizardsai/Data-Science/master/Mall_Customers.csv")


#Data Preprocessing
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])


#Specify features
x = df[['Age','Annual Income','Spending Score','Gender']] #features


#Elbow Method
sse = []
k_range = range(1,10)
for k in k_range:
    km = KMeans(n_clusters=k)
    km.fit(x)
    sse.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_range,sse)
plt.show()


# #Clustering
km = KMeans(n_clusters=5)
y_predicted = km.fit_predict(x)
y_predicted


# #Creating a new columns with clusters
df['cluster']=y_predicted
df


# #Visualize my clustering results
df.cluster.unique()
df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]
plt.scatter(df1['Annual Income'],df1['Spending Score'],color='blue')
plt.scatter(df2['Annual Income'],df2['Spending Score'],color='green')
plt.scatter(df3['Annual Income'],df3['Spending Score'],color='yellow')
plt.scatter(df4['Annual Income'],df4['Spending Score'],color='red')
plt.scatter(df5['Annual Income'],df5['Spending Score'],color='black')


# In[ ]:




