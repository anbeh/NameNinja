import sys
import string
import itertools
import requests
import threading
from threading import Lock
import os
import signal

OUTPUT_FILE_404 = 'good.txt'
OUTPUT_FILE_CHECKED = 'checked.txt'
lock = Lock()
stop_event = threading.Event()

counter = 0 

def script_banner():
    os.system('cls || clear')
    print("""
⠀⠀⠀⠀⠀⣀⠠⠄⠒⠒⠒⠠⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢆⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀
⠀⠀⢸⠀⢀⢴⡂⠉⠁⠀⠈⠉⠐⠢⡀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⢸⠀⡇⠀⢻⣿⠂⠀⠐⣿⣿⠁⠈⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠣⡱⣀⠈⠉⠀⠀⠀⠈⠁⣀⠜⡘⠀⠀⡠⡞⣍⡂
⠀⠀⠀⠀⠀⢢⡥⠐⣒⣒⣒⡒⢬⡔⠊⢰⣶⡮⡱⡬⠚⠁
⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠈⠲⡊⣑⢵⠏⠀⠀⠀
⠀⠀⡠⠃⠀⢠⠀⠀⠀⠀⠀⠀⠀⣄⠀⠈⢇⠀⠀
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉
""")

def load_processed_usernames(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_username(username, file_path):
    with lock:
        with open(file_path, 'a') as f:
            f.write(f"{username}\n")

def check_username(username, total):
    global counter
    try:
        response = requests.get(f"https://github.com/{username}")
        if response.status_code == 404:
            print(f"\rChecking: {counter}/{total} | Current: {username}", end="")
            save_username(username, OUTPUT_FILE_404)
        else:
            print(f"\rChecking: {counter}/{total} | Current: {username}", end="")
            save_username(username, OUTPUT_FILE_CHECKED)
        with lock:
            counter += 1
    except requests.ConnectionError:
        pass
    except requests.RequestException as e:
        print(f"\rError checking {username}: {e}", end="")

def worker(username_list, total):
    for username in username_list:
        if stop_event.is_set():
            break
        check_username(username, total)

def signal_handler(signal_received, frame):
    print("\nCTRL+C detected, stopping...")
    stop_event.set()

def generate_custom_words(length, use_letters=True, use_digits=True):
    letters = string.ascii_lowercase
    digits = string.digits
    valid_words = set()

    char_pool = ""
    if use_letters:
        char_pool += letters
    if use_digits:
        char_pool += digits

    if not char_pool:
        raise ValueError("Must include letters or digits in the character pool.")

    all_usernames = [''.join(i) for i in itertools.product(char_pool, repeat=length)]
    valid_words.update(all_usernames)

    return list(valid_words)

def main(username_list, num_threads=10):
    processed_404 = load_processed_usernames(OUTPUT_FILE_404)
    processed_checked = load_processed_usernames(OUTPUT_FILE_CHECKED)
    processed_usernames = processed_404.union(processed_checked)
    remaining_usernames = [username for username in username_list if username not in processed_usernames]

    print(f"Total usernames to check: {len(remaining_usernames)}")

    chunk_size = len(remaining_usernames) // num_threads + 1
    chunks = [remaining_usernames[i:i + chunk_size] for i in range(0, len(remaining_usernames), chunk_size)]

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=worker, args=(chunk, len(remaining_usernames)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\nProcessing completed!")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 3 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
            raise ValueError("Usage: python script.py <username_length> <num_threads> [-l] [-d]")

        username_length = int(sys.argv[1])
        num_threads = int(sys.argv[2])
        use_letters = '-l' in sys.argv
        use_digits = '-d' in sys.argv

        if username_length < 1 or username_length > 39:
            raise ValueError("Username length must be between 1 and 39.")

        if num_threads < 1:
            raise ValueError("Number of threads must be a positive integer.")

        signal.signal(signal.SIGINT, signal_handler)
        
        script_banner()
        words = generate_custom_words(username_length, use_letters, use_digits)
        print(f"Generated {len(words)} usernames.")
        main(words, num_threads=num_threads)

    except Exception as e:
        print(f"Error: {e}")