import os

import pytest
import requests
from requests.exceptions import ConnectionError

from load_environment import load_environment


# Подгружаем окружение и вытягиваем логин/пароль для авторизации.
load_environment()
LOGIN = os.getenv('login')
PASSWORD = os.getenv('password')


class TestStoriesApi:
    """Тестирование API сайта 'interligo.pythonanywhere.com'"""

    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36'
    }
    API_URL = 'https://interligo.pythonanywhere.com/api/v1/stories/'

    def get_all_data_from_api(self) -> list:
        """Метод для получение всей информации, предоставляемой API"""
        response = requests.get(self.API_URL, headers=self.HEADERS)
        return response.json()

    @pytest.fixture(scope='function')
    def try_to_get_content_count(self):
        """Метод для получения информации о количестве контента"""
        try:
            response = requests.get(self.API_URL, headers=self.HEADERS)
            result = len(response.json())
        except ConnectionError:
            result = 0
        return result

    def test_url_to_get_status_code_equals_200(self):
        """Тест с корректным URL API"""
        response = requests.get(self.API_URL, headers=self.HEADERS)
        assert response.status_code == 200

    def test_wrong_url_to_get_status_code_equals_404(self):
        """Тест с некорректным URL API"""
        wrong_url = self.API_URL + 'test'
        response = requests.get(wrong_url, headers=self.HEADERS)
        assert response.status_code == 404

    def test_get_content_type_equals_json(self):
        """Тест с проверкой типа контента, возвращаемого API"""
        response = requests.get(self.API_URL, headers=self.HEADERS)
        assert response.headers['Content-Type'] == 'application/json'

    def test_get_content_count_equals_3(self):
        """Тест с проверкой количества элементов контента"""
        response = requests.get(self.API_URL, headers=self.HEADERS)
        assert len(response.json()) == 3

    def test_get_content_count_with_fixture(self, try_to_get_content_count):
        """Тест с проверкой количества элементов контента, получаемый из фикстуры"""
        response = requests.get(self.API_URL, headers=self.HEADERS)
        assert len(response.json()) == try_to_get_content_count

    @pytest.mark.parametrize('story_id', ('1', '2', '3'))
    def test_get_story_detail_without_auth_to_get_status_code_equals_403(self, story_id: str):
        """Тест с проверкой доступа без авторизации"""
        story_detail_url = self.API_URL + story_id
        response = requests.get(story_detail_url, headers=self.HEADERS)
        assert response.status_code == 403

    @pytest.mark.parametrize('story_id', ('1', '2', '3'))
    def test_get_story_detail_with_auth_to_get_status_code_equals_200(self, story_id: str):
        """Тест с проверкой доступа с авторизацией"""
        story_detail_url = self.API_URL + story_id
        response = requests.get(story_detail_url, headers=self.HEADERS, auth=(LOGIN, PASSWORD))
        assert response.status_code == 200

    @pytest.mark.parametrize('story_id', ('1', '2', '3'))
    def test_get_story_detail_with_auth_to_get_story_ids(self, story_id: str):
        """Тест с проверкой соответствия ID рассказа"""
        story_detail_url = self.API_URL + story_id
        response = requests.get(story_detail_url, headers=self.HEADERS, auth=(LOGIN, PASSWORD))
        story_detail = response.json()
        assert story_detail['id'] == int(story_id)
