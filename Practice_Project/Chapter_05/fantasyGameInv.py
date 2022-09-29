def dis_inv(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def add_inv(inv, add_itt):
    for k in add_itt:
        inv[k] = inv.get(k,0) + 1
    return inv
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = add_inv(stuff, dragonLoot)

dis_inv(stuff)
