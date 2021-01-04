# app.py

import json
from flask import Flask  
from flask import request, jsonify
import sqlite3
from best_fit import bestFitDecreasing

app = Flask(__name__) # name for the Flask app (refer to output)

# Create some test data for our catalog in the form of a list of dictionaries.
conn = sqlite3.connect('database.db', check_same_thread=False)
print ("Opened database successfully")

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/delivery/assign', methods=['GET'])
def deliveryAssign():
    content = request.json
    # conn = sqlite3.connect('database.db', check_same_thread=False)
    # print ("Opened database successfully")

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

    available_delivery_partners = cur.fetchall()

    result = bestFitDecreasing (content['order_list'], available_delivery_partners)
    #customSolveHardCoded(content['slot_number'], content['order_list'], delivery_map)
    
   
            
    return jsonify(result)




if __name__ == "__main__":
    app.run(debug = True) 

# to allow for debugging and auto-reload

# curl --header "Content-Type: application/json" \
#   --request GET \
#   --data '{"slot_number": 1, "order_list" : [{"order_id": 1, "order_weight": 10},{"order_id": 2, "order_weight": 40},{"order_id": 3, "order_weight": 10},{"order_id": 4, "order_weight": 20}]}' \
#   http://localhost:5000/api/v1/delivery/assign