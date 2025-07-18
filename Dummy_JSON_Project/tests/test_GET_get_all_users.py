
# Import libraries and packages
import pytest
import requests
import json


# Import helper functions
from Dummy_JSON_Project.helperFunction.usersHF import get_users


#Tests
"""Get list of all users"""


@pytest.mark.tco1 #Create test tag
def test_GET_get_all_users(): #Name function
    get_all_the_users_response = requests.get(get_users()) #Send request
    result_get_all_the_users_response = get_all_the_users_response.json() #Get response back as json
    pretty_print = json.dumps(result_get_all_the_users_response, indent=4) #Format response
    assert get_all_the_users_response.status_code == 200 #Assert status code
    print(pretty_print, get_all_the_users_response) #Print results