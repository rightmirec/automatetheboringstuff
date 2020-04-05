# Write your code here :-)
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    count = {}
    for k, v in inventory.items():
        item_total = item_total + inventory.get(k,0)
        print(f'{k} {v}')
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1
    return(inventory)


inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dager', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
