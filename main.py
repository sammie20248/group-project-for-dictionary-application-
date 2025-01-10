from japanese import japanese_dictionary_app
def main():
    while True:
        print("\nWelcome to this Multi_lingual Dictionary!")
        print("Select a dictionary:")
        print("1. japanese")
        print("2. spanish (coming soon)")
        print("3. french (coming soon)")
        print("4. italian (coming soon)")
        print("5. german (coming soon)")
        print("6. Exit")

        choice = input("Enter your choice from (1-6): ")

        if choice == "1":
            japanese_dictionary_app()
        elif choice == "2":
            print("sorry,The spanish dictionary is not available yet.")
        elif choice == "3":
            print("sorry,The french dictionary is not available yet.")
        elif choice == "4":
            print("sorry,The italian dictionary is not available yet.")
        elif choice == "5":
            print(" sorry,The german dictionary is not available yet.")
        elif choice == "6":
            print("you are Exiting the program now!")
            break
        else:
            print("Invalid ,Please try again.")
# main program
if __name__ == "__main_":
    main()