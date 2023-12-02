from data import data
from pprint import pprint
from copy import deepcopy


def clean_data(lst: list) -> list:
    """
        Cleans and transforms a list of dictionaries representing user data.

        This function takes a list of dictionaries, where each dictionary contains
        user information. It performs several transformations:
        - Splits the 'name' field into 'firstname' and 'lastname'.
        - Converts the 'id' field to an integer.
        - Converts the 'admin' field to a boolean.
        - Removes the original 'name' field from each dictionary.

        The function operates on a copy of the input list to avoid modifying
        the original data.

        Parameters:
        lst (list): A list of dictionaries to be cleaned. Each dictionary should have
                    the keys 'name', 'id', and 'admin'.

        Returns:
        list: A new list of dictionaries with the cleaned and transformed data.

        Example:
        >>> data = [
        ...     {'name': 'John Doe', 'id': '123', 'admin': 'False'},
        ...     {'name': 'Jane Smith', 'id': '456', 'admin': 'True'}
        ... ]
        >>> clean_data(data)
        [{'firstname': 'John', 'lastname': 'Doe', 'id': 123, 'admin': False},
         {'firstname': 'Jane', 'lastname': 'Smith', 'id': 456, 'admin': True}]
        """
    lst_to_be_cleaned = deepcopy(lst)
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
    pprint(data)
