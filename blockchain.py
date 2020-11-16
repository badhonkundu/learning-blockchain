# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """returns the last value of the current clockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_lockchain_elements():
    for block in blockchain:
        print("Outputting block")
        print(block)


while True:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_lockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid. Please pick a value from the list')

print("Done!")
