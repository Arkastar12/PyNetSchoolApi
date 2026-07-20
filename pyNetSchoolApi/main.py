import requests
from pyNetSchoolApi import errors

class school:

    def __init__(self, At: str, Cookie: str, host: str, user_agent: str):
        self.At = At
        self.Cookie = Cookie
        self.host = host
        self.user_agent = user_agent
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'At': self.At,
            'connection': 'keep-alive',
            'Cookie': self.Cookie,
            'host': self.host,
            'user-agent': self.user_agent,
        }
    
    def getSettings(self) -> dict:
        url = f'https://{self.host}/webapi/mysettings'
        answer = requests.get(url, headers=self.headers)
        try:
            return answer.json()
        except Exception as e:
            raise errors.ReturnDataError(f'Check your AT, and Cookie! Answer text: {answer.text}')
    
    def getAnnouncements(self) -> list:
        url = f'https://{self.host}/webapi/announcements?take=-1'
        answer = requests.get(url, headers=self.headers)
        try:
            return answer.json()
        except Exception as e:
            raise errors.ReturnDataError(f'Check your AT, and Cookie! Answer text: {answer.text}')
    
    def downloadFileById(self, id):
        url = f'https://{self.host}/webapi/attachments/{id}'
        answer = requests.get(url, headers=self.headers)
        try:
            return answer.content
        except Exception as e:
            raise errors.ReturnDataError(f'Check your AT, and Cookie! Answer text: {answer.text}')