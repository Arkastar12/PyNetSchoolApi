# PyNetSchoolApi
Текущая версия: 0.1.1

# Установка
Для установки используйте

    python -m pip install pyNetSchoolApi

# Примеры

    import pyNetSchoolApi

    school = pyNetSchoolApi.school('AT', 'Cookie', 'host', 'User Agent')
    print(school.getSettings())