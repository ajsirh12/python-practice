from d04.ex1 import *
from d04.ex2 import ManageFIle

create_table()

itemroute = 'd:/python/data/item.txt'
salesroute = 'd:/python/data/sales.txt'

item = readfile(itemroute)
sales = readfile(salesroute)

insertDBData('item', item)
insertDBData('sales', sales)

print('DB Complete')