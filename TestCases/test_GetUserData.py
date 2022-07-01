import requests
import json
import jsonpath
import pytest

#API URL
url = "https://reqres.in/api/users"
a = 10

@pytest.fixture
def start_exec():
    global file
    file = open("C:\\Users\\tibi\\Documents\\API\\CreateUser.json",'r')

def test_create_new_user(start_exec):
    json_input = file.read()
    x = json.loads(json_input)
    pst = requests.post(url,x)
    assert pst.status_code == 201
    a = json.loads(pst.text)
    id = jsonpath.jsonpath(a,'id')
    print(id)

def test_create1_new_user(start_exec):
    json_input = file.read()
    x = json.loads(json_input)
    pst = requests.post(url,x)
    assert pst.status_code == 201
    a = json.loads(pst.text)
    id = jsonpath.jsonpath(a,'id')
    print(id)

def test_create2_new_user(start_exec):
    json_input = file.read()
    x = json.loads(json_input)
    pst = requests.post(url,x)
    assert pst.status_code == 201
    a = json.loads(pst.text)
    id = jsonpath.jsonpath(a,'id')
    print(id)

def test_create3_new_user(start_exec):
    json_input = file.read()
    x = json.loads(json_input)
    pst = requests.post(url,x)
    assert pst.status_code == 201
    a = json.loads(pst.text)
    id = jsonpath.jsonpath(a,'id')
    print(id)