
def order_sort(e):
    return e['order_weight']


###
#   As this problem is a version of "Bin packing problem" which is NP-Hard
#   I am going to use Approximation algorithm that in known as Best fit algorithm.
#   As this is an offline problem (all the orders are upfront given to us)
#   We will be using the modified version Bestfit decreasing algorithm.
###
def bestFitDecreasing(order_list, delivery_partner_list):
    result = []

    # Sort the input order_weights in DESC order
    order_list.sort(reverse=True, key=order_sort)

    # As the delivery_partner_list is actually a tuple DS, it is not modifiable
    # we need a set to track which delivery_partner is already in-use
    assigned_partners_set = set()
    
    for order in order_list:
        assigned = False
        min = 101
        best_fit_index = -1

        # Find the best fit delivery_partner from list of already assigned partners
        for idx, partner in enumerate(result):
            if partner['capacity_left'] >= order['order_weight'] and min > partner['capacity_left'] - order['order_weight']:
                best_fit_index = idx
                min = partner['capacity_left'] - order['order_weight']

        # Add the order to already assigned selected partner's list 
        if best_fit_index > -1:
            partner = result[best_fit_index]
            partner['capacity_left'] -= order['order_weight']
            partner['list_order_ids_assigned'].append(order['order_id'])
            assigned = True

        # if we were not able to assign the order to any of already selected delivery_partners
        # we will select a new partner for this order
        if not assigned:
            for delivery_partner in delivery_partner_list:
                if delivery_partner[0] not in assigned_partners_set and delivery_partner[1] >= order['order_weight']:
                    
                    partner = {
                        'delivery_partner_id' : delivery_partner[0],
                        'capacity_left' : delivery_partner[1] - order['order_weight'],
                        'vehicle_type' : delivery_partner[2],
                        'list_order_ids_assigned' : [order['order_id']]
                    }
                    result.append(partner)
                    assigned_partners_set.add(delivery_partner[0])
                    break
    
    return result
    
    
