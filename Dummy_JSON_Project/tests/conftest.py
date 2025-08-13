
# Import libraries and packages
import pytest
import requests
import json


# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login #Import helper function
from Dummy_JSON_Project.helperFunction.addNewUsersHF import new_user_details_payload #Import helper function
from Dummy_JSON_Project.helperFunction.usersHF import add_a_new_user #Import helper function


"""Test case: Add a new user """

# Add a new user
@pytest.fixture()
def POST_add_new_user_fixture(): #Name function
    create_new_user = new_user_details_payload() #Call new user payload helper function
    headers = header_data_for_login() #Call header helper function

    add_new_user_response = requests.post(add_a_new_user(),headers=headers,json=create_new_user) #Send request
    result_add_new_user_response = add_new_user_response.json() #Get response back as json
    if add_new_user_response.status_code != 201: #If statement to assert status code
        pytest.fail(f"user creation failed with status {add_new_user_response.status_code}:" 
                    f"{result_add_new_user_response}")
    pretty_print = json.dumps(result_add_new_user_response, indent=4) #Format json response
    print(pretty_print, add_new_user_response.status_code) #Print response and status code
    return add_new_user_response, result_add_new_user_response #Return request and response to use fixture

