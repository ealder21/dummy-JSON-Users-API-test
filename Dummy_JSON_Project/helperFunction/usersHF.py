
import config as config #Import config file as it contains the baseURL and endpoints


#---------------------------------------------------------------------------------------------------------------------
#Get authenticated user
def get_current_authenticated_uer():
    return config.baseURL + config.auth_user

#Login to platform
def login_page():
    return config.baseURL +config.user_login

# Get all users
def get_users(): #Name method
    return config.baseURL + config.users #Create method

