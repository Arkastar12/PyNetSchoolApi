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

# Помощь
## Получение At, Cookie, host и user-agent
 • Зайдите в свой аккаунт в сетевом городе
 • Откройте "инспектор" в браузере
 • Перейдите во вкладку "Сеть"
 • Совершите любое действие (например зайдите в обьявления, или в свой дневник)
 • Найдите любой запрос к серверу (если вы зашли в обьявления, то он должен выглядеть так: "https://(адрес)/webapi/announcements?take=-1")
 • В заголовках вы найдете все данные