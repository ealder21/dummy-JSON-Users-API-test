
import config as config #Import config file as it contains the baseURL and endpoints


#---------------------------------------------------------------------------------------------------------------------
#Get authenticated user
def get_current_authenticated_uer(): #Name function
    return config.baseURL + config.auth_user

#Login to platform
def login_page(): #Name function
    return config.baseURL +config.user_login

# Get all users
def get_users(): #Name function
    return config.baseURL + config.users #Create method

# Add a new users
def add_a_new_user(): #Name function
    return config.baseURL + config.add_new_user

