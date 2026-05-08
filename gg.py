import os
import re
import random

def sanitize_filename(s: str) -> str:

    return re.sub(r'[\\/:\*\?"<>\|]', '-', s).strip()

songs = [
    # ==== The Weeknd — Dawn FM (2022) ====
    ("The Weeknd", "Dawn FM", "2022", "01", "Dawn FM"),
    ("The Weeknd", "Dawn FM", "2022", "02", "Gasoline"),
    ("The Weeknd", "Dawn FM", "2022", "03", "How Do I Make You Love Me?"),
    ("The Weeknd", "Dawn FM", "2022", "04", "Take My Breath"),
    ("The Weeknd", "Dawn FM", "2022", "05", "Sacrifice"),
    ("The Weeknd", "Dawn FM", "2022", "06", "Out of Time"),
    ("The Weeknd", "Dawn FM", "2022", "07", "Here We Go... Again"),
    ("The Weeknd", "Dawn FM", "2022", "08", "Best Friends"),
    ("The Weeknd", "Dawn FM", "2022", "09", "Is There Someone Else?"),
    ("The Weeknd", "Dawn FM", "2022", "10", "Starry Eyes"),
    ("The Weeknd", "Dawn FM", "2022", "11", "Every Angel is Terrifying"),
    ("The Weeknd", "Dawn FM", "2022", "12", "Don't Break My Heart"),
    ("The Weeknd", "Dawn FM", "2022", "13", "I Heard You’re Married"),
    ("The Weeknd", "Dawn FM", "2022", "14", "Less Than Zero"),
    ("The Weeknd", "Dawn FM", "2022", "15", "Phantom Regret by Jim"),

    # ==== Drake — Scorpion (2018) ====
    ("Drake", "Scorpion", "2018", "01", "Survival"),
    ("Drake", "Scorpion", "2018", "02", "Nonstop"),
    ("Drake", "Scorpion", "2018", "03", "Elevate"),
    ("Drake", "Scorpion", "2018", "04", "Emotionless"),
    ("Drake", "Scorpion", "2018", "05", "God’s Plan"),
    ("Drake", "Scorpion", "2018", "06", "I’m Upset"),
    ("Drake", "Scorpion", "2018", "07", "8 Out of 10"),
    ("Drake", "Scorpion", "2018", "08", "Mob Ties"),
    ("Drake", "Scorpion", "2018", "09", "Can’t Take a Joke"),
    ("Drake", "Scorpion", "2018", "10", "Sandra’s Rose"),
    ("Drake", "Scorpion", "2018", "11", "Talk Up"),
    ("Drake", "Scorpion", "2018", "12", "Is There More"),
    ("Drake", "Scorpion", "2018", "13", "Peak"),
    ("Drake", "Scorpion", "2018", "14", "Summer Games"),
    ("Drake", "Scorpion", "2018", "15", "Jaded"),
    ("Drake", "Scorpion", "2018", "16", "Nice for What"),
    ("Drake", "Scorpion", "2018", "17", "Finesse"),
    ("Drake", "Scorpion", "2018", "18", "Ratchet Happy Birthday"),
    ("Drake", "Scorpion", "2018", "19", "That’s How You Feel"),
    ("Drake", "Scorpion", "2018", "20", "Blue Tint"),
    ("Drake", "Scorpion", "2018", "21", "In My Feelings"),
    ("Drake", "Scorpion", "2018", "22", "Don’t Matter to Me"),
    ("Drake", "Scorpion", "2018", "23", "After Dark"),
    ("Drake", "Scorpion", "2018", "24", "Final Fantasy"),
    ("Drake", "Scorpion", "2018", "25", "March 14"),
]

out_dir = os.path.abspath("test_audio")  # folder to create files
make_mp3 = True
make_flac = True

os.makedirs(out_dir, exist_ok=True)

created = []

for artist, album, year, track, title in songs:
    minutes = random.randint(2, 5)
    seconds = random.randint(0, 59)
    duration = f"{minutes}:{seconds:02d}"

    base = f"{artist} - {alb
print("\nNow point your GUI's 'Load album' to that folder to test filename parsing.")um} - {year} - {track} - {title}"
    safe_base = sanitize_filename(base)

    extension = random.choice([".mp3", ".flac"]) if make_mp3 and make_flac else ".mp3"
    fname = os.path.join(out_dir, safe_base + extension)

    with open(fname, "wb") as f:
        f.write(b"\x00" * 1024)

    created.append((fname, duration))

print(f"Created {len(created)} fake songs in {out_dir}:\n")
for path, dur in created:
    print(f" - {os.path.basename(path)}  ({dur})")
