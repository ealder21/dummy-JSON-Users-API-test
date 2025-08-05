
# Update a user record

"""If you want to generate faker data use the faker library. In this example, the endpoint
is very specific,as it is expecting a particular name in the data field. We need to update
the user's last name from Williams to Owais"""

# Example of using faker

# from faker import Faker #Import faker library to generate random data
#
# #fake = Faker() #Create faker object
#
# # Update a task by ID helper function
# def updated_create_task_payload(task_id=None):
#     update_task_payload = {
#         "task_id": task_id,
#         "content": fake.word(),
#         "is_done": True
#     }
#     return update_task_payload

#--------------------------------------------------------------------------------------------------------

# Update a user record
def update_a_user_record(): #Name function. ID=None as we don't want to update ID
    update_user_payload = {
        "id": 2,
        "firstName": "Michael",
        "lastName": "Owais",
        "gender": "male"
    }
    return update_user_payload
