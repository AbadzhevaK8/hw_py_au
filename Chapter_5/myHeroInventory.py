#! /usr/bin/python3
#! python3

def displayInventory(inventory):
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for j in addedItems:
        inventory.setdefault(j, 0)
        inventory[j] += 1
    displayInventory(inventory)
    return(inventory)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("Inventory:")
displayInventory(inv)
print('')
inv = addToInventory(inv, dragonLoot)
print('')
print(inv)

input()
