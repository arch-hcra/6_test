import pytest
from flask import Flask

# Импортируем приложение из основного файла
from app import app

@pytest.fixture
def client():
    """Создаем тестовый клиент для Flask приложения."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Тестируем маршрут домашней страницы (/)"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, World!"