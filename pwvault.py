import cryptography
from cryptography.fernet import Fernet

# Generate a secret key
secret_key = Fernet.generate_key()

# Create an instance of the Fernet class using the secret key
fernet = Fernet(secret_key)

# Function to add a new password to the vault
def add_password(account: str, password: str):
  # Encrypt the password using the secret key
  encrypted_password = fernet.encrypt(password.encode())

  # Store the encrypted password in a file or a database
  with open("vault.txt", "a") as f:
    f.write("{},{}\n".format(account, encrypted_password))

  # Successfully added message
  print("Password has been added to the vault! :)")

# Function to retrieve a password from the vault (CANNOT FIGURE OUT DECRYPTION YET)
# def get_password(account: str):
#   # Search for the account in the vault file
#   with open("vault.txt", "r") as f:
#     for line in f:
#       parts = line.strip().split(",")
#       if parts[0] == account:
#         # Decrypt the password using the secret key
#         decrypted_password = parts[1]
#         return fernet.decrypt(decrypted_password).decode()

  # If the account is not found, return None
  return None

# Recieve input from user for encryption
platform = input("Enter Platform Name: ")
password = input("Enter Password: ")

# Test the password vault
add_password(platform, password)
# print(get_password("gmail"))
