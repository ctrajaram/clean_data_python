from data import data
from pprint import pprint


# INSTRUCTIONS
# 1) Split the full name into two fields, first name and last name
# 2) Convert the admin field to a boolean value
# 3) Convert the id to an integer
# 4) Keep the rest of the info the same
# 5) Complete this in a function(s)
# 6) Save the data into a new data structure: a list of dictionaries


def clean_data(lst: list) -> list:
    lst_to_be_cleaned = lst.copy()
    new_list = list()
    for dct in lst_to_be_cleaned:
        first_name, last_name = dct.get('name').split()
        dct['firstname'] = first_name
        dct['lastname'] = last_name
        dct['id'] = int(dct.get('id'))
        dct['admin'] = bool(dct.get('admin'))
        del (dct['name'])
        new_list.append(dct)

    return new_list


if __name__ == "__main__":
    pprint(clean_data(data))
