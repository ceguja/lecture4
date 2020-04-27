import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=1436e01b81b4ba6a72e1fa931e67c82c&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    data = res.json()
    print(data)


if __name__ == "__main__":
    main()