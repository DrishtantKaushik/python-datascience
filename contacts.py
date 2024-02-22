contacts = {
    'police': '112',
    'ambulance': '102',
}
while True:
    print('search a contact:')
    q = input(">>>")
    if len(q) == 0:
        print('closing down...')
        break
    if q in contacts:
        print(f'{q}:{contacts[q]}')
    elif q =='all':
        print('All contacs:')
        for k, v in contacts.items():
            print(f'{k}: {v}')
    else:        
         print(f"{q} not found")
         print('add a new contact?')
         new_contact = input(">>>")
         if len(new_contact) == 0:
            print('skipping')
            contacts[q] = new_contact
            print(f'{q}: {contacts[q]} added')