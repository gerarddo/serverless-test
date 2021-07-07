# This is a Proof of concept repository

It features the serverless framework with use of python and flask for the implementation of two endpoints, one to be used without authorization headers and another with authorization headers.

## Public endpoint:
```
/api/public
```
It will always return the same information no matter what.

## Private endpoint
```
/api/private
```
It will return different messages depending on the authorization headers value being sent. Relevant information will only be revealed if auth headers are valid. Scheme is BASIC with user and password string ``` gmijares@lapsusdev.com:ThisIsASecurePassword ```

## Directory structure

Important files are:

- api.py
- authorizer.py
- myPermissions.json
- serverless.yml

Implementation logic for endpoints is found in ```api.py``` and authorization logic in ```authorizer.py``` . The other two files are mainly configuration settings.