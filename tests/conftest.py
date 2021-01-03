import pytest, json
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()



def outputSort (e):
    return e['delivery_partner_id']
    
def execute_test(client, input, expected_output):
    res = client.get('/api/v1/delivery/assign', data=json.dumps(input), headers={'Content-Type': 'application/json'})
    assert res.status_code == 200

    output = json.loads(res.get_data(as_text=True))
    output.sort(key=outputSort)   
    for out in output:
        out['list_order_ids_assigned'].sort() 
    assert expected_output == output
    