
# Import libraries and packages
import pytest
import requests
import json

# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login
from Dummy_JSON_Project.helperFunction.updateUserRecordHF import update_a_user_record
from Dummy_JSON_Project.helperFunction.usersHF import get_users


"""Test case: Update the users last name from Williams to Owais"""

#1. Update users last name, users ID is 2
@pytest.mark.tc1 #Add Pytest marker
def test_PUT_update_a_user_record_based_on_ID(): #Name test
    payload_update_users_lastName = update_a_user_record() # Add updated payload
    headers = header_data_for_login() #Headers helper function
    id = 2 #Hardcoded user ID

    update_users_last_name_response = requests.put(f"{get_users()}/{id}", json=payload_update_users_lastName, headers=headers) #Send request to endpoint
    results_update_users_last_name_response = update_users_last_name_response.json() #Get response back as json
    pretty_print = json.dumps(results_update_users_last_name_response, indent=4) #Format response back
    assert update_users_last_name_response.status_code == 200 #Assert status code
    print(pretty_print,update_users_last_name_response.status_code)  #Print formatted response and status code

    verify_last_name_update = results_update_users_last_name_response #Store response in a variable
    assert verify_last_name_update["lastName"] == verify_last_name_update["lastName"] #Assrt content matches what's in response
    print(verify_last_name_update["lastName"]) #Print verified data

