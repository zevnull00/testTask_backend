# test_api.py

import requests
import threading
from app import create_app
import time


TEST_PORT = 5000
BASE_URL = "http://127.0.0.1:" + str(TEST_PORT)

def run_server():
    app = create_app()
    app.run(host="127.0.0.1", port=TEST_PORT, debug=False)

# если запускать сервер 'на боевом' -> поток сервера заблочит выполнение
# поэтому, поток сервера в отдельный - в виде демона, который прибьется
# по окончанию теста
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# на всякий случай
time.sleep(1)

# проверка, что сервак вообще живой
def test_api_alive():
    url = BASE_URL + "/gross_violations/2/objects_gv"
    response = requests.get(url)
    print('Response: ' + response.text)
    assert response.status_code == 200

# проверка, что корректно обрабатывается другой вид данных
def test_api_uncorrect_str():
    url = BASE_URL + "/gross_violations/fdfdadsfs/objects_gv"
    response = requests.get(url)
    print('Response: ' + response.text)
    assert response.status_code == 404

# проверка, что корректно обрабатывается несуществующий uid
def test_api_uncorrect_uid():
    url = BASE_URL + "/gross_violations/9999999/objects_gv"
    response = requests.get(url)
    print('Response: ' + response.text)
    assert response.status_code == 200