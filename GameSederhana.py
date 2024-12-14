class Hero:
    def __init__(self, nama, health, attackPower, armorNumber, specialAttack, namaKekuatan):
        self.nama = nama
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
        self.specialAttack = specialAttack
        self.namaKekuatan = namaKekuatan

    def menyerang(self, lawan):
        if self.health > 0:
            print(f"{self.nama} menyerang {lawan.nama} dengan {self.namaKekuatan}")
            lawan.bertahan(self, self.attackPower)
        else:
            print(f"{self.nama} sudah kalah dan tidak bisa menyerang.")

    def bertahan(self, lawan, attackPower_lawan):
        if self.health <= 0:
            return
        print(f"{self.nama} bertahan dari serangan {lawan.nama}")
        damage = attackPower_lawan / (self.armorNumber if self.armorNumber > 0 else 1)
        self.health -= damage
        print(f"Serangan berdampak {damage:.1f}")
        if self.health <= 0:
            self.health = 0
            print(f"{self.nama} telah kalah!")
        else:
            print(f"Darah {self.nama} tersisa {self.health:.1f}")

hero1 = Hero("Ariff", 42, 80, 99, 42, "Semekdwon")
hero2 = Hero("Ulpia", 42, 85, 120, 42, "Kekuatan Tendangan Maut")
hero3 = Hero("Wafiqq", 42, 99, 135, 42, "Kamehameha")
hero4 = Hero("Serlia", 42, 999, 199, 42, "Rasengan")

heroes = [hero1, hero2, hero3, hero4]

turns = 8
for i in range(turns):
    print(f"\n==== Turn {i+1} ====")
    attacker = heroes[i % 4]
    defender = heroes[(i + 1) % 4]
    attacker.menyerang(defender)

    hidup = [hero for hero in heroes if hero.health > 0]
    if len(hidup) == 1:
        print(f"\nPermainan selesai! Pemenangnya adalah {hidup[0].nama}")
        break

hidup = [hero for hero in heroes if hero.health > 0]
if len(hidup) > 1:
    pemenang = max(hidup, key=lambda hero: hero.health)
    print(f"\nPermainan selesai! Pemenangnya adalah {pemenang.nama} dengan health {pemenang.health:.1f}.")
elif len(hidup) == 0:
    print("\nPermainan selesai! Tidak ada pemenang, semua hero telah kalah.")

