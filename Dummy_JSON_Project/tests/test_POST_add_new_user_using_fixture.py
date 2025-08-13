
# Import libraries and packages
import pytest
import requests
import json


# Import helper functions
from Dummy_JSON_Project.helperFunction.headersHF import header_data_for_login #Import helper function
from Dummy_JSON_Project.helperFunction.addNewUsersHF import new_user_details_payload #Import helper function
from Dummy_JSON_Project.helperFunction.usersHF import add_a_new_user #Import helper function


"""Test case: 1. Add a new user, 2. Get user_id """

# Add a new user
@pytest.mark.tc1 #Add test marker
def test_POST_add_new_user(POST_add_new_user_fixture): #Pass fixture as an argument
    add_new_user_response, result_add_new_user_response =POST_add_new_user_fixture #assign return data to fixture
    """in the fixture we need to add the data we are returning and assign it to the fixture"""


    # Verify data in response back, first name
    """Assert name in firstname dictionary. As we know the name to expect, we can check the firstname field will 
    return the exact name we want"""

    verify_data_in_response = result_add_new_user_response  # Store response in a variable
    assert verify_data_in_response["firstName"] == "Muhammad"
    print(verify_data_in_response["firstName"])  # Print verified data


    #Verify data in response back, last name
    """Assert name in lastname dictionary. Lets say we don't know what the value is, but we are expecting a 
    value, we can verify the response has a lastName and corresponding data"""

    verify_data_in_response = result_add_new_user_response #Store response in a variable
    assert verify_data_in_response["lastName"] == verify_data_in_response["lastName"] #Assrt content matches what's in response
    print(verify_data_in_response["lastName"]) #Print verified data


    """Get id of newly created user"""

    user_id = result_add_new_user_response["id"] #Get user ID
    assert user_id # Assert user ID
    print(user_id) #Print user ID