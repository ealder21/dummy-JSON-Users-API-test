
# Import libraries and packages
import json
from os import access

import requests
import pytest


# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login
from Dummy_JSON_Project.helperFunction.usersHF import login_page
from Dummy_JSON_Project.helperFunction.loginAsUserHF import user_login_payload
from Dummy_JSON_Project.helperFunction.authorizationHF import header_for_auth_accessToken
from Dummy_JSON_Project.helperFunction.usersHF import get_current_authenticated_uer


"""Test case: Login with a user, then verify the user is logged in by accessing the token"""

    #1. Login as a user
@pytest.mark.tc02 #Add test marker
def test_POST_login_and_get_token(): #Name function
    headers = header_data_for_login() #Call header helper function
    login_payload = user_login_payload() #Call user login helper function

    login_user_response = requests.post(login_page(),headers=headers,json=login_payload) #Send request
    result_login_user_response = login_user_response.json() #Get response back as json
    pretty_print = json.dumps(result_login_user_response, indent=4) #Format response
    assert login_user_response.status_code == 200 #Assert status code
    print(pretty_print,login_user_response.status_code) #Print formatted response


    #2. Get access token from response
    accessToken = result_login_user_response["accessToken"] #Get the access token from the response
    assert accessToken #Assert access token
    print(accessToken) #Print token


    #3. Set up access token header
    #Create access token header helper function
    authorisation_header = header_for_auth_accessToken(accessToken) #Get authorization data from HF


    #4. Get the details of the authenticated user
    current_authenticated_user_response = requests.get(get_current_authenticated_uer(),headers=authorisation_header) #Send request
    result_current_authenticated_user_response = current_authenticated_user_response.json() #Get response back as json
    pretty_print =json.dumps(result_current_authenticated_user_response, indent=4)
    assert current_authenticated_user_response.status_code == 200 #Assert status code
    print(pretty_print, current_authenticated_user_response.status_code) #Print formatted response back


    #5. Verify data in the response of the current authenticated user
    #In this example, we are checking the firstname in the response
    verify_name = result_current_authenticated_user_response
    assert verify_name["firstName"] == "Emily" # Verify first name in response





