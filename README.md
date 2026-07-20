# PyNetSchoolApi
Текущая версия: 0.1.2

# Установка
Для установки используйте

    python3 -m pip install pyNetSchoolApi

# Примеры

    import pyNetSchoolApi

    school = pyNetSchoolApi.school('AT', 'Cookie', 'host', 'User Agent')
    print(school.getSettings()) # Получить настройки текущего пользователя (ФИО, дата рождения, роль, телефон и тд.)
    print(school.getAnnouncements()) # Получить обьявления
    school.downloadFileById(123) # Получить содержимое файла по ID

Больше примеров ищите в папке examples