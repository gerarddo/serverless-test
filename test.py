import base64


myPersistentAuth = 'gmijares@lapsusdev.com:ThisIsASecurePassword'
authInBytes = myPersistentAuth.encode('ascii')
base64Bytes = base64.b64encode(authInBytes)
base64Auth = base64Bytes.decode('ascii')

print(base64Auth)