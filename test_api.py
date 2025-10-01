# test_api.py

import requests
import threading
from app import create_app
import time
import pytest

TEST_PORT = 5000
BASE_URL = "http://127.0.0.1:" + str(TEST_PORT)

# если запускать сервер 'на боевом' -> поток сервера заблочит выполнение
# поэтому, поток сервера в отдельный - в виде демона, который прибьется
# по окончанию теста
@pytest.fixture(scope="session")
def server():
    def run_server():
        app = create_app()
        app.config['TESTING'] = True
        app.run(host="127.0.0.1", port=TEST_PORT, debug=False, use_reloader=False)

    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1.5)
    yield BASE_URL

def test_api_alive(server):
    """проверка, что сервак вообще живой"""
    url = server + "/gross_violations/2/objects_gv"
    response = requests.get(url)
    assert response.status_code == 200

def test_api_uncorrect_str(server):
    """проверка, что корректно обрабатывается другой вид данных"""
    url = server + "/gross_violations/fdfdadsfs/objects_gv"
    response = requests.get(url)
    assert response.status_code == 404

def test_api_uncorrect_uid(server):
    """проверка, что корректно обрабатывается несуществующий uid"""
    url = server + "/gross_violations/9999999/objects_gv"
    response = requests.get(url)
    assert response.status_code == 200

def test_api_test_data(server):
    """# проверка на основе тестовых данных"""
    url = server + "/gross_violations/4/objects_gv"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    actual_uids = {obj["uid"] for obj in data}
    assert actual_uids == {1, 2, 3}

