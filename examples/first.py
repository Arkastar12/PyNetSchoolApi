import pyNetSchoolApi

school = pyNetSchoolApi.school('AT', 'Cookie', 'host', 'User Agent')

print(school.getSettings()) # Получить настройки текущего пользователя (ФИО, дата рождения, роль, телефон и тд.)

print(school.getAnnouncements()) # Получить обьявления

school.downloadFileById(123) # Получить содержимое файла по ID

# Скачать файл с сервера
with open('file.txt', 'wb') as f:
    f.write(school.downloadFileById(123)) 

#Расписание
print(school.getDiary('schoolId', 'studentId', 'vers', 'weekStart', 'weekEnd', 'withLaAssigns', 'yearId'))

#Проверка живой ли токен
print(school.checkTokenExpired()) # возвращает True или False

#Получение информации (новые сообщения, уведомления, активные сессии)
print(school.getState())