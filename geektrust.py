# TSHIRT 	Clothing 	1000 	10%
# JACKET 	Clothing 	2000 	5%
# CAP 	    Clothing 	500 	20%
# NOTEBOOK 	Stationery 	200 	20%
# PENS 	    Stationery 	300 	10%
# MARKERS 	Stationery 	500 	5%

# For each clothing item, the maximum quantity that can be purchased is 2.
# For each stationery item, the maximum quantity that can be purchased is 3.
# Discounts can be applied only if the total purchase amount is 1000 rupees or more.
# An additional discount of 5% can be applied if the total amount to pay is 3000 rupees or more.
# There is a 10% sales tax on total bill. The tax is calculated after all the discounts are applied.

products ={"TSHIRT": 	{"category":"Clothing","cost":1000,"discount": 	10},
"JACKET": 	{"category":"Clothing","cost":2000,"discount": 	5},
"CAP": 	    {"category":"Clothing","cost":500, "discount":	20},
"NOTEBOOK": 	{"category":"Stationery","cost":200, "discount":	20},
"PENS": 	    {"category":"Stationery","cost":300, "discount":	10},
"MARKERS": 	{"category":"Stationery","cost":500, "discount":	5},}
# print(products)

quantities={"TSHIRT":0,
"JACKET":0,
"CAP":0,
"NOTEBOOK":0,
"PENS":0,
"MARKERS":0}

shopping = True


def add_item(item,quantitiy):
    cur_counts = quantities[item]+quantitiy
    if(cur_counts>2 and products[item]["category"]=="Clothing"):
        print("ERROR_QUANTITY_EXCEEDED")
        return
    elif(cur_counts>3 and products[item]["category"]=="Stationery"):
        print("ERROR_QUANTITY_EXCEEDED")
        return
    quantities[item]+=quantitiy
    print("ITEM_ADDED")

def print_bill():
    # print(quantities)
    cost_total=0
    discount_total=0
    for item in quantities:
        cost_total+=quantities[item]*products[item]["cost"]
        discount_total+=quantities[item]*products[item]["cost"]*products[item]["discount"]/100
        # print(item,cost_total,discount_total)
    if(cost_total>3000):
        # cost_total-=discount_total
        discount_total+=cost_total*5/100
    if(cost_total>=1000):
        cost_total-=discount_total
    else:
        discount_total=0.00
    tax=cost_total*0.1
    # print(cost_total,discount_total,tax)
    print("TOTAL_DISCOUNT",discount_total)
    print("TOTAL_AMOUNT_TO_PAY",round(cost_total+tax,2))


while(shopping):
    event = input().strip()
    if(event.startswith("ADD_ITEM")):
        item,quantitiy=event.split()[1:]
        add_item(item=item,quantitiy=int(quantitiy))
    elif(event.startswith("PRINT_BILL")):
        print_bill()
        shopping=False