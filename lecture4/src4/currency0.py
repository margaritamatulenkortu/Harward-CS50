import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=059112a81343782ef028c7ba0d5d1ce9&format=1")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
