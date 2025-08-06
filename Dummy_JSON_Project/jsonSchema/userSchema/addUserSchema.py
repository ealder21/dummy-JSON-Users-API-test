
#Define add user schema helper function

def add_new_user_schema():
    add_user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["id", "firstName", "lastName", "age"],
        "additionalProperties": True
    }
    return add_user_schema
