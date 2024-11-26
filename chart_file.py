import matplotlib.pyplot as plt

product = ['panadol','brufen','diasar','disprine','paracetamol','arinac']
units_sold = [10,12,30,10,34,56]

plt.bar(product,units_sold)
plt.title("Product Sale Chart")
plt.show()