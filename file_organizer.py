import os
import shutil
from datetime import datetime


class FileOrganizer:

    def location(self):
        """Show current folder location"""
        current = os.getcwd()
        print(f"You are in: {current}")

    def list_files(self):
        """Show all files in current folder"""
        print("\nFiles in this folder:")
        items = os.listdir(".")
        for item in items:
            print(f"  {item}")

    def organize_by_type(self):
        """Sort files into folders by their type"""
        categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
            'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md', '.doc'],
            'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.php'],
            'Others': []
        }

        items = os.listdir(".")
        files = []
        for item in items:
            if os.path.isfile(item):
                files.append(item)

        for folder in categories.keys():
            if not os.path.exists(folder):
                os.mkdir(folder)
                print(f"Created folder: {folder}")

        moved = 0

        for file in files:
            extension = os.path.splitext(file)[1].lower()
            moved_to = None

            for folder, extensions in categories.items():
                if extension in extensions:
                    source = file
                    destination = os.path.join(folder, file)
                    os.rename(source, destination)
                    print(f"Moved: {file} -> {folder}")
                    moved += 1
                    moved_to = folder
                    break

            if moved_to is None:
                source = file
                destination = os.path.join("Others", file)
                os.rename(source, destination)
                print(f"Moved: {file} -> Others")
                moved += 1

        print(f"\nOrganized {moved} files")

    def undo_organize(self):
        """Move all files back from organized folders"""
        folders = ['Images', 'Documents', 'Music', 'Videos', 'Archives', 'Code', 'Others']
        moved_back = 0

        for folder in folders:
            if os.path.exists(folder):
                files = os.listdir(folder)
                for file in files:
                    file_path = os.path.join(folder, file)
                    if os.path.isfile(file_path):
                        destination = os.path.join('.', file)
                        os.rename(file_path, destination)
                        print(f"Moved back: {file} from {folder}")
                        moved_back += 1

        for folder in folders:
            if os.path.exists(folder):
                try:
                    os.rmdir(folder)
                    print(f"Removed empty folder: {folder}")
                except:
                    pass

        print(f"\nMoved back {moved_back} files")

_organizer = FileOrganizer()

def location():
    return _organizer.location()

def list_files():
    return _organizer.list_files()

def organize_by_type():
    return _organizer.organize_by_type()

def undo_organize():
    return _organizer.undo_organize()