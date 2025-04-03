from voice_input import get_voice_input
from reddit_search import search_reddit
from twitter_search import search_twitter
from csv_writer import write_to_csv  # Updated import
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    while True:
        choice = input("Choose input method:\n1: Voice Input\n2: Text Input\nEnter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")

    if choice == '1':
        print("🔊 Please speak your query...")
        query = get_voice_input()
    else:
        query = input("🖊️ Please type your query: ").strip()

    if not query:
        print("No input received. Exiting...")
        return

    print(f"🔍 Searching for: {query}\n")

    reddit_results = search_reddit(query)
    twitter_results = search_twitter(query)
    combined = reddit_results + twitter_results

    write_to_csv(combined)  # Updated function call
    print("✅ Done! Results written to CSV file.")

if __name__ == "__main__":
    main()
