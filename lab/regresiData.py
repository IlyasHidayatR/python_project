import pandas as pd
import matplotlib.pyplot as plt

pizza = {'diameter': [7, 6, 8, 6, 10], 'price': [5, 6, 7, 8, 9]}

pizza_df = pd.DataFrame(pizza)
pizza_df.plot.scatter(x='diameter', y='price')
plt.title('Pizza')
plt.xlabel('Diameter')
plt.ylabel('Price')
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.grid(True)
plt.show()

