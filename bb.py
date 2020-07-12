def remove_item(item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price):
    while True:
        show_basket(item_bought, item_bought_quantity, item_quantity_price_list)

        remove_choice = input(
            '\n''Select the remove mode: ''\n''1. Remove Item Completely ''\n'
            "2. Remove Item Partially (Edit Quantity) "'\n''\n''0. Return to Shopping Menu''\n')
        while remove_choice != '1' and remove_choice != '2' and remove_choice != '0':
            print('Invalid Option')
            remove_choice = input('\n''Select the remove mode: ''\n''1. Remove Item Completely ''\n'
                                  "2. Remove Item Partially (Edit Quantity)  "'\n''\n''0. Return to Shopping Menu''\n')

        if remove_choice == '0':
            print('Returning to Main Menu''\n')
            return item_bought, item_bought_quantity, item_quantity_price_list, item_bought_unit_price
            # break

        if remove_choice == '1':
            while True:
                delete_item = input(
                    'Select the item you want to completely remove it from the Basket ? for e.g 1,2,3..... ')

                while not delete_item.isdigit() or delete_item.isspace() or int(delete_item) > len(item_bought) or delete_item == '0':
                    print('No item found , Please Enter from 1 to', len(item_bought))
                    delete_item = input(
                        'Select the item you want to completely remove it from the Basket ? for e.g 1,2,3..... ')
                delete_item = int(delete_item)
                print('Your selected item', item_bought[delete_item - 1], 'has been completely removed')

                del item_bought[delete_item - 1]
                del item_bought_quantity[delete_item - 1]
                del item_quantity_price_list[delete_item - 1]
                del item_bought_unit_price[delete_item - 1]