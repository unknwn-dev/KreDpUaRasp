import urllib.request
from bs4 import BeautifulSoup
import csv

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html,'html.parser')

    raspisaniye = []

    predm = soup.find_all('td',id='predm')

    rowInt=0

    for row in soup.find_all('td',id='group')[7:]:
        group = row.text
        pr1 = predm[rowInt].text
        pr2 = predm[rowInt+1].text
        pr3 = predm[rowInt+2].text
        pr4 = predm[rowInt+3].text
        pr5 = predm[rowInt+4].text

        raspisaniye.append ({
            'group':"Группа:"+group+"|",
            'pr1':"0. "+pr1+"|",
            'pr2':"1. "+pr2+"|",
            'pr3':"2. "+pr3+"|",
            'pr4':"3. "+pr4+"|",
            'pr5':"4. "+pr5
        })

        rowInt += 5

    return raspisaniye

def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for project in projects:
            writer.writerow((project['group'],project['pr1'],project['pr2'],project['pr3'],project['pr4'],project['pr5']))

def main():
    save(parse(get_html("https://www.kre.dp.ua/education-process/timetable")),'rasp.csv')

if __name__ == "__main__":
    main()
