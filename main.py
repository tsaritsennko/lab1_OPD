import Parser
import openpyxl # импортируем библиотеку openpyxl

if __name__ == '__main__':
    wb = openpyxl.load_workbook(filename='results.xlsx')  # открываем файл
    worksheet = wb['Result']  # открываем нужную страницу

    worksheet['A1'] = "Название вакансии"
    for item in Parser.parse():
        worksheet.append([item])

    wb.save('results.xlsx')
