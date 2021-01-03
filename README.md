# Grofers Assignment

This repository contains a Flask REST-API backend application, that aims to solve the [problem statement](https://github.com/tanushree27/Grofers_app/blob/main/Grofers%20-%20Problem%20Statement.pdf).





## Summary

The application exposes a REST-API that takes in list of orders and slot number and returns the assigned delivery details that utilizes the vehicle space efficiently.

Database tables creation and data insertion queries are available in [db directory](https://github.com/tanushree27/Grofers_app/tree/main/db).

### Constraits

**Vehicle Capacity:**
- Bike : 30kg
- Scooter : 50kg
- Truck : 100kg

**Slots:**
- 6 - 9
- 9 - 13
- 16 - 19
- 19 - 23

**Available Vehicles:**
- 1 Truck
- 3 Bikes
- 2 Scooters

**Note:**
- Trucks are not available in the (6 - 9) slot.
- Bikes and Scooters are not available in the (19-23) slot.
- 100kg max weight per slot

### Algorithm

This problem is a modified version of [Bin Packing Problem](https://en.wikipedia.org/wiki/Bin_packing_problem), our problem modifies the constraint of fixed bin size to variable sized bin, rest all is the same. This problem is a well known NP-Hard problem with no polynomial time solution.

**Approach:** To tackle this problem I am going to use approximation algorithm called _"Best Fit Decreasing"_.

**Steps:**
1) Sort the orders by weights in decreasing order.
2) Get the first/next order from the list.
3) Search the assigned delivery partners list for _best fit_*. 
4) If nothing found in step 3, find in unassigned delivery partners list for _best fit_*.
5) add the order to that delivery partner update its capacity_left and if needed add the partner to assigned delivery_partners list.
6) repeat from step 2 until no orders remain.

*best fit = min(capacity_left - order_weight)




## Getting started

### Prerequisites

- python3
- pip

### Steps

- Clone the repository and cd into it.

- Setup and activate a virtualenv for the project.
```
$ python3 -m venv myenv
$ source myenv/bin/activate
```

- Install required packages
```
$ pip3 install -r requirements.txt
```

- You are all setup now.

- To run our pytests
```
$ python3 -m pytest -v
```

- To start the server
```
$ python3 app.py
```

Your server should be up and running on localhost:5000




## APIs

Here we outline the usage of our API
### Input

###### URL: GET http://localhost:5000/api/v1/delivery/assign

###### Header
```
{
    'Content-Type': 'application/json'
}
```

###### Body
```
{
    "slot_number" : 4,
    "order_list" : [
        {
            "order_id":1,
            "order_weight":30
        }, 
        {
            "order_id":2,
            "order_weight":10
        },
        {
            "order_id":3,
            "order_weight":20    
        }
    ]
}
```

###### EXAMPLE

cURL request:
```
curl \
    --header "Content-Type: application/json"   \
    --request GET   \
    --data '{"slot_number": 1, "order_list" : [{"order_id": 1, "order_weight": 10},{"order_id": 2, "order_weight": 40},{"order_id": 3, "order_weight": 10},{"order_id": 4, "order_weight": 20}]}'   \
    http://localhost:5000/api/v1/delivery/assign
```


### Output

```
[
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
```

---
By Tanushree Tumane