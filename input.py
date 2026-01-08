# Berlatih Input

username = input("Masukan Username: ")
age = input("Masukan Umur Kamu: ")

print("Hallo,")
print(username, age)

# Menggabung

# Cara Lama
salam = "Halo, " + username + ", Umur Kamu " + age

print(salam)

# Cara Modern
salam2 = print(f"Halo, {username}, Umur Kamu {age}")

print(salam2)