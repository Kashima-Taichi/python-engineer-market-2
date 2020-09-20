from bs4 import BeautifulSoup
import requests
import datetime

# variables
greenJobsPage = 'https://www.green-japan.com/search_key/01?keyword=PHP'

dt = datetime.datetime.now()
formatDate = dt.strftime('%Y%m')

html = requests.get(greenJobsPage)
soup = BeautifulSoup(html.text, 'lxml')

positionTitle = soup.find_all('h3', {'class': 'card-info__heading-area__title'})
positionSalary = soup.select('div.card-info__detail-area > ul > li:nth-child(1)')
positionArea = soup.select('div.card-info__detail-area > ul > li:nth-child(2)')

fileName = formatDate + "PHPJobs.txt"

with open(fileName, 'w') as f:
    for i in range(10):
        print(str(positionTitle[i].text), end=',', file=f)
        print(str(positionSalary[i].text.replace('\n', '').replace(' ', '')), end=',', file=f)
        print(str(positionArea[i].text), file=f)
