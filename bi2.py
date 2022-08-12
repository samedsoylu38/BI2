from bs4 import BeautifulSoup
import requests
import pandas as pd

city_1 = 'Berlin'
city_2 = 'Hamburg'
city_3 = 'Cologne'
city_4 = 'Frankfurt'
city_5 = 'Munich'
city_6 = 'Leipzig'

url1 = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'
url2 = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_3}&city2={city_4}&tracking=getDispatchComparison'
url3 = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_5}&city2={city_6}&tracking=getDispatchComparison'

page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.content, 'html.parser')

page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, 'html.parser')

page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.content, 'html.parser')

table1 = soup1.find('table', attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
table2 = soup2.find('table', attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
table3 = soup3.find('table', attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})

rows1 = table1.find_all('tr')
rows2 = table2.find_all('tr')
rows3 = table3.find_all('tr')

liste = pd.DataFrame(columns=['City', 'Lebensmittel', 'Preis'])

for element in rows1[17:22]:
    new_row1 = pd.DataFrame({'City' : [city_1], 'Lebensmittel' : [element.text.split()[0]], 'Preis' : [element.text.split()[2]]})
    new_row2 = {'City' : city_2, 'Lebensmittel' : element.text.split()[0], 'Preis' : element.text.split()[4]}
    liste = liste.append(new_row1, ignore_index =True)
    liste = liste.append(new_row2, ignore_index =True)

for element in rows2[17:22]:
    new_row1 = {'City' : city_3, 'Lebensmittel' : element.text.split()[0], 'Preis' : element.text.split()[2]}
    new_row2 = {'City' : city_4, 'Lebensmittel' : element.text.split()[0], 'Preis' : element.text.split()[4]}
    liste = liste.append(new_row1, ignore_index =True)
    liste = liste.append(new_row2, ignore_index =True)

for element in rows3[17:22]:
    new_row1 = {'City' : city_5, 'Lebensmittel' : element.text.split()[0], 'Preis' : element.text.split()[2]}
    new_row2 = {'City' : city_6, 'Lebensmittel' : element.text.split()[0], 'Preis' : element.text.split()[4]}
    liste = liste.append(new_row1, ignore_index =True)
    liste = liste.append(new_row2, ignore_index =True)

liste.to_csv("Daten.csv")

