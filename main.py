import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
from banner import print_banner

SOCIAL_MEDIA_PLATFORMS = {
    "Instagram": "https://www.instagram.com/{username}",
    "Twitter": "https://www.x.com/{username}",
    "Facebook": "https://www.facebook.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "VSCO": "https://vsco.co/{username}/gallery",
    "Threads": "https://www.threads.net/@{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Wattpad": "https://www.wattpad.com/user/{username}",
    "LINE": "https://line.me/R/ti/p/@{username}",
    "Telegram": "https://t.me/{username}",
    "GitHub": "https://github.com/{username}",
    "Ask.fm": "https://ask.fm/{username}",
    "YouTube": "https://www.youtube.com/{username}",
    "Discord": "https://discord.com/users/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Tumblr": "https://{username}.tumblr.com"
}

# Fungsi untuk memeriksa username di berbagai platform sosial media
def check_username(platform, url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"{Fore.GREEN}[FOUND]{Style.RESET_ALL}\t\t\t{platform}: {url}"
        else:
            return f"{Fore.YELLOW}[NOT FOUND]{Style.RESET_ALL}\t\t{platform}: {url}"
    except requests.RequestException:
        return f"{Fore.RED}[ERROR]{Style.RESET_ALL}\t\t\t {platform}: {url}"

# Fungsi untuk melakukan pencarian username di berbagai platform sosial media
def search_social_media(username):
    results = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for platform, url_template in SOCIAL_MEDIA_PLATFORMS.items():
            url = url_template.format(username=username)
            futures.append(executor.submit(check_username, platform, url))

        for future in futures:
            results.append(future.result())

    return results

# Fungsi untuk pencarian menggunakan Brave
def brave_search(fullname):
    query = fullname.replace(" ", "+")
    url = f"https://search.brave.com/search?q={query}&source=web"

    try:
        print(Fore.BLUE + f"Searching for '{fullname}' on Brave Search..." + Style.RESET_ALL)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("http"):
                results.append(href)

        if results:
            print(Fore.BLUE + "[RESULTS FOUND]" + Style.RESET_ALL + " Results from Brave Search:")
            for idx, result in enumerate(results, start=1):
                print(f"{Fore.GREEN}{idx}. {result}{Style.RESET_ALL}")
        else:
            print(Fore.YELLOW + "[NOT FOUND]" + Style.RESET_ALL + " No results found.")
        return results

    except requests.RequestException as e:
        print(Fore.RED + f"[ERROR] Error occurred: {e}" + Style.RESET_ALL)
        return []

# Fungsi utama
def main():
    print("Options:")
    print("1. Search Social Media with username")
    print("2. Search Brave Search with full name")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        username = input("Enter the username to search: ")
        print(f"Searching for '{username}' in social media platforms...\n")
        results = search_social_media(username)
        for result in results:
            print(result)
    elif choice == '2':
        fullname = input("Enter the full name to search in Brave Search: ")
        print(f"\nSearching for '{fullname}' on Brave Search...\n")
        results = brave_search(fullname)
        if results:
            print(Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL + f" Search completed for '{fullname}'.")
        else:
            print(Fore.YELLOW + "[NOT FOUND]" + Style.RESET_ALL + " No results found or an error occurred.")
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("\n\n")
    print_banner("YUD'S TRACKER")
    print("\n\n")
    main()
