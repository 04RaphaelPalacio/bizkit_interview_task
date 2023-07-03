from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    users_dict =  { 0: {"age": "29", "id": "1", "name": "John Doe", "occupation": "Developer"}, 1: {"age": "30", "id": "2", "name": "John Doe", "occupation": "Engineer"}, 2: {"age": "25", "id": "3", "name": "John Doe", "occupation": "Designer"}, 3: {"age": "28", "id": "4", "name": "John Smith", "occupation": "Architect"}, 4: {"age": "31", "id": "5", "name": "Jane Smith", "occupation": "Manager"}, 5: {"age": "24", "id": "6", "name": "Joe Smith", "occupation": "Designer"}} 

    for i in range(users_dict):
        user_input_key = input("Search User:")
        users_dict[user_input_key] = user_input_key
        if  user_input_key not in users_dict:
            return False
        else: return USERS
search_users()