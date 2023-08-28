#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt


# In[16]:


# selecting the equation type
type=int(input("""Select the type of equation 
for LINEAR type 1
for QUADRATIC type 2
for CUBIC type 3"""))


# In[17]:


#taking the equation as input
if type==1:
    print("in the form of aX+b=0")
    a=input("coefficient of x:")
    b=input("constant")
elif type==2:
    print("in the form of aX^2+bx+c=0")
    a=input("coefficient of x^2:")
    b=input("coefficient of x:")
    c=input("constant:")
else:
    print("in the form of aX^3+bx^2+cx+d=0")
    a=input("coefficient of x^3:")
    b=input("coefficient of x^2:")
    c=input("coefficient of x:")
    d=input("constant:")


# In[18]:


# Get user input for coefficients
a = float(a)
b = float(b)
c = float(c)
d = float(d)
# Generate x values
x = np.linspace(-10, 10, 400)  # Adjust the range and granularity as needed

# Calculate corresponding y values
if type==1:
    y = a * x + b
elif type==2:
    y = a * x**2 + b * x + c
else:
     y = a * x**3 + b * x**2 + c * x + d
# Create the plot
plt.figure(figsize=(8, 6))
if type==1:
    plt.plot(x, y, label=f'{a}x + {b}')
    plt.title('Linear Equation Plot')
elif type==2:
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Quadratic Equation Plot')
else:
    plt.plot(x, y, label=f'{a}x^3 + {b}x^2 + {c}x + {d}')
    plt.title('Cubic Equation Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




