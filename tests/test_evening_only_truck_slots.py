import json

def outputSort (e):
    return e['delivery_partner_id']

def test_index(app, client):


    order = {
        'slot_number' : 4,
        'order_list' : [
            {
                'order_id':1,
                'order_weight':30
            }, 
            {
                'order_id':2,
                'order_weight':10
            },
            {
                'order_id':3,
                'order_weight':20    
            }
        ]
    }
    
    print(json.dumps(order))
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    res = client.get('/api/v1/delivery/assign', data=json.dumps(order), headers=headers)
    assert res.status_code == 200
    expected =   [
        {
            "capacity_left": 40, 
            "delivery_partner_id": 6, 
            "list_order_ids_assigned": [
                    1,
                    2,
                    3
            ], 
            "vehicle_type": "Truck"
        }
    ]

    output = json.loads(res.get_data(as_text=True))
    output.sort(key=outputSort)   
    for out in output:
        out['list_order_ids_assigned'].sort() 
    assert expected == output