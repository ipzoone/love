import time
from random import randint

def love_animation():
    heart = [
        "   ♥♥♥     ♥♥♥   ",
        " ♥     ♥ ♥     ♥",
        "♥       ♥       ♥",
        " ♥     LOVE    ♥ ",
        "  ♥♥♥       ♥♥♥   ",
        "    ♥♥  ♥  ♥♥     ",
        "      ♥   ♥       ",
        "        ♥        "
    ]
    
    colors = ['\033[95m', '\033[91m', '\033[93m', '\033[92m']
    
    for _ in range(8):
        print("\033[H\033[J")  
        for line in heart:
            print(colors[randint(0,3)] + line)
            time.sleep(0.1)
        time.sleep(0.5)

print("Initializing Boyfriend.exe...")
time.sleep(1)
print("\nScanning universe...")
time.sleep(1)
print("Found been HACKED by IPZONEX!!")
time.sleep(1)
print("Found been HACKED by IPZONEX!!.")
time.sleep(1)
print("Found been HACKED by IPZONEX!!..")
time.sleep(3)
print("Target acquired: ❤️ YOU ❤️\n")
time.sleep(2)

love_animation()

print("\n\033[93m⚠️  WARNING ⚠️")
print("\033[96mSystem overload detected!")
print(f"Cause: Terlalu banyak memikirkan kamu\n")

input("Press ENTER untuk buktikan kamu nyata...")
print("\n\033[92mVerification successful!")
print("Kamu adalah manusia tercantik di alam semesta!\n")

time.sleep(1)
print("Menghitung alasan aku sayang kamu...")
for i in range(101):
    print(f"\r{i}% completed: {'♥'*(i//2)}", end='')
    time.sleep(0.05)
    
print("\n\n\033[91mERROR 1001:")
print("System crash...")
print("Penyebab: Kelebihan kebahagiaan saat bersamamu")
print("Solusi: Pelukan darurat segera diperlukan! 🫂\n")

jawaban = input("Apakah kamu mau menerima cintaku? (ya/tentu saja): ").lower()
while jawaban not in ["ya", "tentu saja"]:
    print("\033[91mInvalid response! Coba lagi 😘")
    jawaban = input("Apakah kamu mau menerima cintaku? (ya/tentu saja): ").lower()

print("\n\033[92m❤️❤️❤️ SELAMAT! ❤️❤️❤️")
print("Kamu berhasil mendapatkan:")
print("- Pacar terbaik")
print("- Teman hidup")
print("- Partner Nonton")
print("- Dan... ERROR! ❤️ Terlalu banyak keuntungan untuk disebutkan!")