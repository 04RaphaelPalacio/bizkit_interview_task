import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    for number in fave_numbers_2:
        if number not in fave_numbers_1:
            return False
    for number in fave_numbers_2:
        if number in fave_numbers_2 == fave_numbers_1:
            return True
is_match()       
        

#Pseudo_code 
#(Match endpoint for Matching Algorithm is not found: http://127.0.0.1:5000/match/%7Bmatch_id%7D and {match id} to test takes too long to respond: 127.0.0.1:5000/match/3 )

'''
list1 = [1,2,3,4,5,6,7]    
list2 = [1,2,3,4,5,6,8]
    
for number in list2:
    if number not in list1:
        print('false')
for number in list2:
    if number in list2 == list1:
        print('true')
'''
