from fastapi.testclient import TestClient
from main import app

# Создаем тестового клиента
client = TestClient(app)

# 1. Простой тест для главной страницы
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет от Docker и CI/CD!"}

# 2. Простой тест для проверки статуса сервера
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}