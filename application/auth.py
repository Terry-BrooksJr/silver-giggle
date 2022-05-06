# import argon2


# class PasswordValidationError(Exception):
#     '''Generic Password Error'''


# class PasswordManager:
#     def __init__(self,P_Hasher):
#         self.P_Hasher = argon2.PasswordHasher()

#     def set_password(self, password):
#         return self.P_Hasher.hash(password)

#     def verify_password(self, hashed, password):
#         try:
#             self.P_Hasher.verify(hashed, password)
#         except:
#             argon2.exceptions.VerificationError("Incorrect Password")
