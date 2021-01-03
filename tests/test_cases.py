import json
from conftest import execute_test


def test_slot_1_with_only_bike(app, client):

    with open('tests/test_2.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_1_with_only_Scooter(app, client):

    with open('tests/test_3.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_1_with_only_BikeAndScooter(app, client):

    with open('tests/test_4.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_2_with_all_vehicles_1(app, client):

    with open('tests/test_5.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_2_with_all_vehicles_2(app, client):

    with open('tests/test_6.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_2_with_all_vehicles_3(app, client):

    with open('tests/test_7.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_2_with_all_vehicles_4(app, client):

    with open('tests/test_8.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_3_with_all_vehicles_1(app, client):

    with open('tests/test_9.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_3_with_all_vehicles_2(app, client):

    with open('tests/test_10.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_3_with_all_vehicles_3(app, client):

    with open('tests/test_11.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_3_with_all_vehicles_4(app, client):

    with open('tests/test_12.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])

def test_slot_4_with_only_trucks(app, client):

    with open('tests/test_1.json') as f:
        test = json.load(f)
   
    execute_test (client, test['input'], test['expected_output'])
