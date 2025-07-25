

#Needed headers to login. Once logged in we need the access token to access the API
"""In the function name, we need to pass the variable that stores the access token. This can be found in the test
 case. From the response body, we can get the token. The variable we used is called accessToken"""


def header_for_auth_accessToken(accessToken): #As an argument, pass the variable that holds the access token
    header_authorization_accessToken = {
        "Authorization": f"Bearer {accessToken}" #Pass access token
    }
    return header_authorization_accessToken


