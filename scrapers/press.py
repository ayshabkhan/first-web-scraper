import csv
import requests #requests info from website

from BeautifulSoup import BeautifulSoup #html parser

url = 'https://www.oag.state.md.us/Press/index.htm'

response = requests.get(url)
html = response.content 

soup = BeautifulSoup(html) #you can use any variable, but soup is the convention

#print soup.findAll('table') <-that would isolate and print all tables
#print soup.findAll('table') [2] # prints only the third table (uses zero indexing, so third=2)

table = soup.findAll('table') [2]

#use python to loop over each row and extract certain information, not by number, so that it works even if new data is added
#for loop goes through each row

#COLLECT ALL THE ROWS!!!

list_of_rows = [] #empty list to structure each row

for row in table.findAll('tr')[1:]: #calling everything between tr tags a row, tells it to ignore the first row with the extra head text
	list_of_cells = [] #reset to an empty list of cells for every row
	for cell in row.findAll('td'): #within that, calling everything between td tags a cell
		list_of_cells.append(cell.text) #prints all text in the cell -- BUT it ignores the markup, like the links
		if cell.find('a'):
			list_of_cells.append("https://www.oag.state.md.us/Press/" + cell.find('a')['href'])
			#navigates inside a tag to extract the href value.
			#but this prints out relative (internal site) url, so we add the rest of the url in separately        
	list_of_rows.append(list_of_cells)

#write the data to a csv file
outfile = open("./releases.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(['date', 'title', 'url']) #adds header row before wrting data
writer.writerows(list_of_rows)