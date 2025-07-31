
# Import libraries and packages
import pytest
import requests
import json


# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login
from Dummy_JSON_Project.helperFunction.addNewUsersHF import new_user_details_payload
from Dummy_JSON_Project.helperFunction.usersHF import add_a_new_user


"""Test case: Add a new user """

# Add a new user
@pytest.mark.tc1 #Add test marker
def test_POST_add_new_user(): #Name function
    create_new_user = new_user_details_payload() #Call new user payload helper function
    headers = header_data_for_login() #Call header helper function

    add_new_user_response = requests.post(add_a_new_user(),headers=headers,json=create_new_user) #Send request
    result_add_new_user_response = add_new_user_response.json() #Get response back as json
    pretty_print = json.dumps(result_add_new_user_response, indent=4)
    assert add_new_user_response.status_code == 201
    print(pretty_print, add_new_user_response.status_code)

    #Verify data in response back, first name
    """Assert name in firstname dictionary. As we know the name to expect, we can check the firstname field will 
    return the exact name we want"""

    verify_data_in_response = result_add_new_user_response #Store response in a variable
    assert verify_data_in_response["firstName"] == "Muhammad" #Assrt content matches what's in response
    print(verify_data_in_response["firstName"]) #Print verified data


    #Verify data in response back, last name
    """Assert name in lastname dictionary. Lets say we don't know what the value is, but we are expecting a 
    value, we can verify the response has a lastName and corresponding data"""

    verify_data_in_response = result_add_new_user_response #Store response in a variable
    assert verify_data_in_response["lastName"] == verify_data_in_response["lastName"] #Assrt content matches what's in response
    print(verify_data_in_response["lastName"]) #Print verified data




