# kamu sedang membuat permainan sederhana.
# seorang pemain memula dengan 100 poin kesehatan.
# mereka meminum ramuan yang menambah 25 poin kesehatan
# lalu diserang oleh monster yang menyebabkan 40 kerusakan

health = 100
potion = 25
damage = -40

hp_potion = health + potion
hp_damage = hp_potion + damage

print(hp_damage)