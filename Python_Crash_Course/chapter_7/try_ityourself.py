# Try It Yourself
# 7.8 Deli

sandwich_orders = ['pastrami','chicken sw','buff sw','veg sw','pastrami','light salad sw','sw with no bread','mitho sw','pastrami','i dont like sw']

finished_sandwiches = []

def prep_sw():
    print('Sandwitch that have been preped: ')
    # not_finito = False
    while sandwich_orders:
        current_item = sandwich_orders.pop()
        print(f'Preparing {current_item}')
        print('...\n...\n...')
        # print(f'{current_item} is Done')
        print(f'Your {current_item} is Ready!\n')
        finished_sandwiches.append(current_item)
    return finished_sandwiches

# prep_sw()
finished_sandwiches = []
def check_sw_availability():
    print(f'Here is the list of sandwithces available in the shop today')
    print(f'But due to some indgridient error pastrami is not available today')
    print(list(set(sandwich_orders)))
    #or you can call above funtion with some adjustment
    while 'pastrami sw' in sandwich_orders:
        sandwich_orders.remove('pastrami sw')

    while sandwich_orders:
        current_item = sandwich_orders.pop()
        if 'pastrami' in current_item.lower():
            print("Please read the notice carefully.")
        else:
            # print(current_item)
            finished_sandwiches.append(current_item)
check_sw_availability()
print("Finished sandwiches:", finished_sandwiches)