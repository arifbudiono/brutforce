# Program sederhana untuk mengetahui Password yang anda ketikan
# Gunakan 3 kata untuk uji coba

import random
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)
password = input("Masukan Password : ")
guess = ""
while (guess !=password):
    guess = random.choices(character_list, k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
print("Password anda adalah : " + guess)
