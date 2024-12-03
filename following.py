import json
import os

# Dapatkan path folder saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Followers
f = open(os.path.join(current_dir, 'followers_1.json'))
data = json.load(f)

follower = []
for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])
f.close()

# Following
f = open(os.path.join(current_dir, 'following.json'))
data = json.load(f)

following = []
for i in data["relationships_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])
f.close()

# Main
good_people = []
for i in following:
    if i in follower:
        good_people.append(i)

# Hitung jumlah data
total_followers = len(follower)
total_following = len(following)
total_mutual = len(good_people)
total_not_followback = total_following - total_mutual

# Print ringkasan data
print("\n=== RINGKASAN DATA ===")
print(f"Total Followers: {total_followers}")
print(f"Total Following: {total_following}")
print(f"Total Mutual Follow: {total_mutual}")
print(f"Total Tidak Follow Back: {total_not_followback}")

# Print yang tidak follow back
print("\n=== DAFTAR YANG TIDAK FOLLOW BACK ===")
for i in following:
    if i not in good_people:
        print("https://www.instagram.com/" + i)