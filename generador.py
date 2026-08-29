import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Ingresa la longitud de la contraseña: "))

password = ""
for i in range(longitud):
    password += random.choice(caracteres)

print("La contraseña generada es:", password)
