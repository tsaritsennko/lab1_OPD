from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests
import openpyxl # импортируем библиотеку openpyxl

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://omsk.hh.ru/search/vacancy?text=Python&from=suggest_post&salary=&ored_clusters=true'  # передаем необходимый URL адрес
page = requests.get(url, headers=headers)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
block = soup.findAll('h3', class_='bloko-header-section-3')  # находим контейнер с нужным классом

wb = openpyxl.load_workbook(filename='results.xlsx') # открываем файл
worksheet = wb['Result'] # открываем нужную страницу

vacancy = []

for data in block:  # проходим циклом по содержимому контейнера
    if data.find('a', class_='serp-item__title') is not None:  # находим тег <a>
        vacancy.append(data.text)

worksheet['A1'] = "Название вакансии"
for item in vacancy:
    worksheet.append([item])

print('Successful!')
wb.save('results.xlsx')
