import secrets
 
def generate_api_key():
    return secrets.token_urlsafe(32)
 
print(generate_api_key())