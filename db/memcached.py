from pymemcache.client import base
import json

client = base.Client(('localhost', 5000))

def addItem(user, item, price):
    try:
        price = int(price)
    except Exception as e:
        print(e)
        return
    items = getItem(user)
    if items is False:
        data = '{"%s":{"count":1}, "all_price":%d}' % (item, price)
        client.set(user, data)
        return

    items["all_price"] += price
    if item in items.keys():
        items[item]["count"] += 1        
        client.set(user, str(items).replace("'", '"'))
        return

    items.update({item:{"count":1}})
    client.set(user, str(items).replace("'", '"'))
    return

def delItem(user, item, price):
    try:
        price = int(price)
    except Exception as e:
        print(e)
    items = getItem(user)
    if items is False:
        return False

    if item in items.keys():
        items["all_price"] -= price
        if items[item]["count"] > 1:
            items[item]["count"] -= 1
            client.set(user, str(items).replace("'", '"'))
            return
        del items[item]        
        client.set(user, str(items).replace("'", '"'))
        return

    return False

def getItem(user):
    items = client.get(user)
    if items is None:
        return False
    data = json.loads(items.decode("utf-8"))
    return data
