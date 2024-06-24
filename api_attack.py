import requests
from colorama import Fore

def launch_attack_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(Fore.GREEN, "[System] API Launch Attack", Fore.RESET)
        else:
            print(Fore.RED, f"API gagal dijalankan. Kode status: {response.status_code}", Fore.RESET)
    except requests.ConnectionError as e:
        print(Fore.RED, "[System] Api Connection Error", Fore.RESET)
    except requests.Timeout as e:
        print(Fore.RED, "[System] Api Timeout Error", Fore.RESET)
    except requests.RequestException as e:
        print(Fore.RED, "[System] Api General Error", Fore.RESET)