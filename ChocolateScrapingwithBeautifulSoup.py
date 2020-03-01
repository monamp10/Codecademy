import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup=BeautifulSoup(url.content , 'html.parser')
# print(soup)
# print(soup.select('.Rating'))
ratings = []
rate=soup.select('.Rating')
for i in rate[1:]:
  ratings.append(float(i.string))
# print(ratings)

plt.hist(ratings)
plt.show()

company = soup.select('.Company')
companies = []
for i in company[1:]:
  companies.append(i.string)

# print(companies)

data={"Company":companies , "Rating":ratings}
cocoa_df=pd.DataFrame.from_dict(data)

# print(bestCompany.head())

rate_mean = cocoa_df.groupby('Company').Rating.mean()
top_ten = rate_mean.nlargest(10)

# print(top_ten)

cocoa_percent = soup.select('.CocoaPercent')
cocoaPC = []
for i in cocoa_percent[1:]:
  percent = i.get_text().strip('%')
  cocoaPC.append(float(percent))

# print(cocoaPC)

cocoa_df['CocoaPercentage']=cocoaPC
# print(cocoa_df.head())
plt.scatter(cocoa_df.CocoaPercentage, cocoa_df.Rating)
z = np.polyfit(cocoa_df.CocoaPercentage, cocoa_df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(cocoa_df.CocoaPercentage, line_function(cocoa_df.CocoaPercentage), "r--")
plt.show()