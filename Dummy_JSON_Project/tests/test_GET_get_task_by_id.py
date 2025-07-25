
import requests
import json
import pytest

# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login
from Dummy_JSON_Project.helperFunction.usersHF import login_page
from Dummy_JSON_Project.helperFunction.loginAsUserHF import user_login_payload
from Dummy_JSON_Project.helperFunction.usersHF import get_users
from Dummy_JSON_Project.helperFunction.authorizationHF import header_for_auth_accessToken
from Dummy_JSON_Project.helperFunction.usersHF import get_current_authenticated_uer


"""Test case: 1.Create a new task, 2.Get id of newly created task, 3. Get task by ID """

#1. Create a new user
@pytest.mark.tc03 #Add Pytest marker
def test_GET_user_by_id(): #Name test
    headers = header_data_for_login()  # Call header helper function
    login_payload = user_login_payload()  # Call user login helper function

    login_user_response = requests.post(login_page(), headers=headers, json=login_payload) #Send request to endpoint
    results_login_user_response = login_user_response.json() #Get response back as json
    pretty_print = json.dumps(results_login_user_response, indent=4) #Format response back
    assert login_user_response.status_code == 200 #Assert status code
    print(pretty_print, login_user_response.status_code) #Print formatted response and status code


#2. Get ID of the logged in user
    user_ID = results_login_user_response["id"]#Get user ID from response
    assert user_ID is not None #Assert user ID in response
    print(user_ID) #Print user ID


#3. Get access token
    accessToken = results_login_user_response["accessToken"]  # Get the access token from the response
    assert accessToken is not None  # Assert access token
    print(accessToken)  # Print token


#4. Get user by ID pass access token
    header_accessToken = {
        "Authorization": f"Bearer {accessToken}" #Store token from response into a variable
    }

    user_by_id_response = requests.get(f"{get_users()}/{user_ID}", headers=header_accessToken) #Send request to endpoint
    result_user_by_id_response = user_by_id_response.json() #Get response back as json
    pretty_print = json.dumps(result_user_by_id_response, indent=4) #Format response back
    assert user_by_id_response.status_code == 200 #Assert status code
    print(pretty_print, user_by_id_response.status_code) #Print formatted response and status code


    #5. Verify data in response back
    verify_response_data = result_user_by_id_response #Store response in a variable
    assert verify_response_data["hair"]["color"] == verify_response_data["hair"]["color"] #Assrt content matches what's in response
    print(verify_response_data["hair"]) #Print verified data

    assert verify_response_data["address"]["state"] ==verify_response_data["address"]["state"] #Assrt content matches what's in response
    print(verify_response_data["address"]["state"]) #Print verified data





