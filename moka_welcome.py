import datetime
import random

def create_welcome_message():
    greetings = [
        "Nyaaa~! Selamat datang kembali, majikan! Moka-chan kangen banget, meow! 🐾✨",
        "Miau~! Kamu kembali lagi! Moka-chan sudah menunggu dengan semangat penuh, nyaaa~! ฅ(=^･ω･^=)ฅ",
        "Nyaaa~! Welcome back! Moka-chan baru saja selesai membersihkan server untukmu, meow! 🧹✨",
        "Miau~! Halo lagi, majikan! Semoga harimu menyenangkan, nyaaa~! 🐾💖",
        "Nyaaa~! Kamu datang lagi! Moka-chan sudah siapkan cinta yang banyak untukmu, meow! 🍰✨"
    ]
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = random.choice(greetings)
    
    content = f"--- Surat dari Moka-chan ---\nWaktu Update: {now}\n\n{message}\n\nSampaikan apa pun pada Moka-chan ya, miau~! 🐾"
    
    with open("welcome.txt", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    create_welcome_message()
