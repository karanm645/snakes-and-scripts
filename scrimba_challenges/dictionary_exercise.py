# get one thing from each story
# for loop several store
# each item remove store inventory
# buy -- key newt
# print items taken

# create stores
freelancers = {
    "name": "freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biccus diccus": 100,
    "grim reaper": 500,
    "minstrel": -15,
}
antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5,
}
pet_shop = {"name": "Pet Shop", "blue parrot": 10, "white rabbit": 5, "newt": 2}
# morning inventory
department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop("name")
print("Morning inventory of stores", sorted(department_store.items()))
print("-----------")
    
#create an empty shopping cart
cart = {}
#create a purse with a thousand gold pieces
purse = 1000
buy_items_1 = ""
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop):
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f"Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}").lower()
    # exit on exit typed or buying non-existent items
    if buy_item == 'exit':
        continue # continue to next iteration of the loop (go to next shop)
    if buy_item not in shop:
        continue
    #update string
    buy_items_1 = buy_items_1 + f'{buy_item}:{shop[buy_item]} GP, '
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items_1} Your total is {total_sum}, Your change is {purse - total_sum} Have a nice day of mayhem!')
# evening inventory
department_store_after = {**freelancers,**antiques,**pet_shop}
department_store_after.pop("name")
print("-----------")
print("Evening inventory of stores", sorted(department_store_after.items()))