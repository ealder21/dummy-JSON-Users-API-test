
# Import libraries and packages
import pytest
import requests
import json

from Dummy_JSON_Project.helperFunction.usersHF import get_users

"""Test case: Delete a users base on ID"""

#1. Delete the user with ID 1
@pytest.mark.tc1 #Add Pytest marker
def test_DELETE_a_user_record_based_on_ID(): #Name test
    id = 1 #Hardcoded user ID
    delete_a_user_response = requests.delete(f"{get_users()}/{id})") #Send request to endpoint
    results_delete_a_user_response = delete_a_user_response.json() #Get response back as json
    pretty_print = json.dumps(results_delete_a_user_response, indent=4) #Format response back
    assert delete_a_user_response.status_code == 400 #Assert status code
    print(pretty_print, delete_a_user_response.status_code) #Print formatted response and status code

    #Verify data in the response
    response_message = results_delete_a_user_response #Store response in a variable
    assert response_message["message"] == response_message["message"] #Assrt content matches what's in response
    print(response_message["message"]) #Print verified data