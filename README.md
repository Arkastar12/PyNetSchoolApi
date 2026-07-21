# PyNetSchoolApi
Текущая версия: 0.1.3

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
1. Зайдите в свой аккаунт в сетевом городе
2. Откройте "инспектор" в браузере
3. Перейдите во вкладку "Сеть"
4. Совершите любое действие (например зайдите в обьявления, или в свой дневник)
5. Найдите любой запрос к серверу (если вы зашли в обьявления, то он должен выглядеть так: "https://(адрес)/webapi/announcements?take=-1")
6. В заголовках вы найдете все данные