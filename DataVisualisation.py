import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))

a=["India","USA","Uk","China"]
b=[70,50,15,43]

plt.pie(b,labels=a)

plt.show()