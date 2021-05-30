from lib.mongodb import APARTMENTS


def address1s():
    return APARTMENTS.find({}).distinct('address_1')


def address2s(address1):
    return APARTMENTS.find({'address_1': address1}).distinct('address_2')


def address3s(address1, address2):
    return APARTMENTS.find({'address_1': address1, 'address_2': address2}).distinct(
        'address_3'
    )
