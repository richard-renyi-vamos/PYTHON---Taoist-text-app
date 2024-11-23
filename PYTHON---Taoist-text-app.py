import json

def load_tao_te_ching(file_path="tao_te_ching.json"):
    """Loads the Tao Te Ching text from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def display_menu():
    """Displays the main menu."""
    print("\nWelcome to the Tao Te Ching Reader 📖")
    print("1. Read a specific chapter")
    print("2. Read the entire text")
    print("3. Exit")

def display_chapter(tao, chapter_number):
    """Displays a specific chapter."""
    chapter = tao.get(str(chapter_number))
    if chapter:
        print(f"\nChapter {chapter_number}")
        print("-" * 30)
        print(chapter)
    else:
        print("\nInvalid chapter number! Please try again.")

def display_all(tao):
    """Displays the entire Tao Te Ching."""
    print("\nThe Tao Te Ching 📜")
    print("=" * 30)
    for chapter, text in tao.items():
        print(f"\nChapter {chapter}")
        print("-" * 30)
        print(text)

def main():
    tao_te_ching = load_tao_te_ching()
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            chapter = input("Enter chapter number: ").strip()
            if chapter.isdigit():
                display_chapter(tao_te_ching, int(chapter))
            else:
                print("\nInvalid input! Please enter a number.")
        elif choice == "2":
            display_all(tao_te_ching)
        elif choice == "3":
            print("\nThank you for reading the Tao Te Ching! 🙏")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
