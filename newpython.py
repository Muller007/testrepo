url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data = requests.get(url).text
soup = BeautifulSoup(html_data)

gme_revenue = pd.DataFrame(columns = ["Date", "Revenue"])
soup.find_all("tbody")[1]
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date =col[0].text
    revenue = col[1].text
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True) 
    
    
gme_revenue ["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")

gme_revenue = gme_revenue[gme_revenue['Revenue']!=""]
