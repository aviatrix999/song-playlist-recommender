import numpy as np

# Artists
artists = ["Atif Aslam", "Sunidhi Chauhan", "Sabrina Carpenter"]

# Song database
song_database = {
    "Atif Aslam": [
        "Tera Hone Laga Hoon",
        "Jeene Laga Hoon",
        "Dil Diyan Gallan",
        "Pehli Nazar Mein",
        "Tajdar-e-Haram"
    ],
    "Sunidhi Chauhan": [
        "Sheila Ki Jawani",
        "Kamli",
        "Aaja Nachle",
        "Beedi",
        "Crazy Kiya Re"
    ],
    "Sabrina Carpenter": [
        "Feather",
        "Espresso",
        "Nonsense",
        "Skin",
        "Because I Liked a Boy"
    ]
}

# Take number of friends
num_friends = int(input("Enter number of friends: "))

friends = []
preferences_matrix = []

# Input preferences
for i in range(num_friends):
    print(f"\nFriend {i + 1}")
    name = input("Enter friend's name: ")
    friends.append(name)

    scores = []
    for artist in artists:
        while True:
            try:
                score = int(input(f"Rate {artist} (0–5): "))
                if 0 <= score <= 5:
                    scores.append(score)
                    break
                else:
                    print("Please enter a value between 0 and 5.")
            except ValueError:
                print("Please enter an integer.")

    preferences_matrix.append(scores)

# Convert to NumPy matrix
preferences_matrix = np.array(preferences_matrix)

# Recommendation
print("\n================ PLAYLIST RECOMMENDATIONS ================")

for i, friend in enumerate(friends):
    user_preferences = preferences_matrix[i]
    best_artist_index = np.argmax(user_preferences)
    recommended_artist = artists[best_artist_index]

    print(f"\n🎧 {friend}'s Recommended Artist: {recommended_artist}")
    print("🎶 Playlist:")
    
    for j, song in enumerate(song_database[recommended_artist], start=1):
        print(f"{j}. {song}")
