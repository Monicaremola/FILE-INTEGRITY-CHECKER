import os
import hashlib
import json

HASH_FILE = 'hashes.json'


def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def scan_folder(folder_path):
    file_hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, folder_path)
            file_hashes[rel_path] = calculate_hash(file_path)
    return file_hashes


def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)


def compare_hashes(old_hashes, new_hashes):
    added = [f for f in new_hashes if f not in old_hashes]
    deleted = [f for f in old_hashes if f not in new_hashes]
    modified = [f for f in new_hashes if f in old_hashes and new_hashes[f] != old_hashes[f]]
    return added, deleted, modified


def main():
    folder = input('Enter the folder path to check: ').strip()
    if not os.path.isdir(folder):
        print('Invalid folder path.')
        return

    print('Scanning files...')
    new_hashes = scan_folder(folder)
    old_hashes = load_hashes()

    if not old_hashes:
        print('No previous hash record found. Saving current hashes as baseline.')
        save_hashes(new_hashes)
        print('Baseline hashes saved. Run the script again to check for changes.')
        return

    added, deleted, modified = compare_hashes(old_hashes, new_hashes)

    if not (added or deleted or modified):
        print('No changes detected. All files are intact.')
    else:
        if added:
            print('Added files:')
            for f in added:
                print('  +', f)
        if deleted:
            print('Deleted files:')
            for f in deleted:
                print('  -', f)
        if modified:
            print('Modified files:')
            for f in modified:
                print('  *', f)
    # Optionally update the hash file after reporting
    save_hashes(new_hashes)


if __name__ == '__main__':
    main() 
