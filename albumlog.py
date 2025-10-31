# Author: Sam Perez-Tamayo
# Course: CS361
# Date: 10/30/2025

import os
import json

DATA_FILE = 'album_log.json'            # stores album data

def display_menu():
    """Provides user with menu of actions to choose from"""
    print("Make a selection from the list below:")
    print("[1] Add Album to Queue")
    print("[2] View Queue")
    print("[3] Get Album Recommendation")
    print("[4] Help/Info")
    print("[5] Exit")


def load_from_file():
    """Get all album data from queue"""
    # file doesn't exist
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_to_file(queue):
    """Save album data to JSON log file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(queue, f)


def add_album_helper(queue):
    """Handle adding an album (title and artist) to queue"""
    artist_name = input('Enter artist name: ')
    album_title = input('Enter album title: ')

    choice = input(f"Enter 1 if this looks correct below. This will be added to your queue and cannot be reversed:\n *** {album_title} - {artist_name} ***\n")

    # if choice != "1":
    #     add_album()

    new_album = {
        "artist": artist_name,
        "album": album_title
    }

    queue.append(new_album)
    save_to_file(queue)

    print("Album added!")

def view_queue_helper(queue):
    """Handle displaying full queue of albums to user"""



def main():

    album_queue = load_from_file()

    while True:
        display_menu()
        choice = input('Enter the index of your choice: ')

        if choice == "1":
            add_album_helper(album_queue)
        elif choice == "2":
            view_queue_helper(album_queue)
        elif choice == "3":
            print('GET RECOMMENDATION')
        elif choice == "4":
            print('GET RECOMMENDATION')
        elif choice == "5":
            print('Goodbye!')
            break
        else:
            print('Invalid choice - try again: ')



if __name__ == "__main__":
    main()