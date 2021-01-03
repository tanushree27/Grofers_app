# app.py

import json
from flask import Flask  
from flask import request, jsonify
import sqlite3

app = Flask(__name__) # name for the Flask app (refer to output)


conn = sqlite3.connect('database.db', check_same_thread=False)
print ("Opened database successfully")

# Create some test data for our catalog in the form of a list of dictionaries.


order = '''
{
    'slot_number' : 1,
    'order_list' : [
        {
    ​       'order_id':​ ​1​, 
        ​   "order_weight':​ ​30
        }, 
        {
    ​       "order_id":​ ​2​,
    ​       "order_weight":​ ​10 
        },
        {
    ​       "order_id":​ ​3​,
        ​   "order_weight":​ ​20    
        } 
    ]
}
'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/delivery/assign', methods=['GET'])
def deliveryAssign():
    content = request.json

    cur = conn.cursor()
    sql_q = '''
    SELECT
       a.id as delivery_partner_id,
       avail_vehicles.capacity,
       avail_vehicles.type
    FROM
        delivery_partner_table a
        JOIN
        (SELECT
            b.*
        FROM vehicle_slot_table a
                JOIN vehicle_table b
                        ON a.vehicle_type_id = b.id
        WHERE a.status = 1 AND a.slot_id = ?) avail_vehicles
            ON a.vehicle_type_id = avail_vehicles.id;
    '''
    cur.execute(sql_q, (content['slot_number'],))

    rows = cur.fetchall()

    delivery_map = dict()

    for row in rows:
        delivery_map[row[0]] = {
            "capacity_left" : row[1],
            "vehicle_type" : row[2],
            "delivery_partner_id" : row[0],
            "list_order_ids_assigned" : []
        }

    customSolveHardCoded(content['slot_number'], content['order_list'], delivery_map)

    for key, value in delivery_map.items():
        if len(value['list_order_ids_assigned']) == 0:
            del delivery_map[key]
            
    return jsonify(list(delivery_map.values()))




def customSolveHardCoded (slot_number, list_of_orders, delivery_map):
    total_weight = 0.00
    for var in list_of_orders:
        total_weight += var['order_weight']

    print(total_weight)

    if slot_number == 4:
        for order in list_of_orders:
            addList(delivery_map, delivery_map[6], order)

        return
    
    print(json.dumps(delivery_map, indent=4, sort_keys=True))

    return




if __name__ == "__main__":
    app.run(debug = True) 

# to allow for debugging and auto-reload

# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"slot_number": 1, "order_list" : [{"order_id": 1, "order_weight": 10},{"order_id": 2, "order_weight": 20},{"order_id": 3, "order_weight": 30}]}' \
#   http://localhost:5000/api/v1/delivery/assign