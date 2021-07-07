import base64 

# Define user and password for Basic auth scheme
myPersistentAuth = 'gmijares@lapsusdev.com:ThisIsASecurePassword'
authInBytes = myPersistentAuth.encode('ascii')
base64Bytes = base64.b64encode(authInBytes)

# Get the Base64 string representation of our defined Auth
base64Auth = base64Bytes.decode('ascii')

# Function to be used in other modules to verify authentication header validity
def main(auth):
    return auth == base64Auth