import requests

def main():
    other = input("Second Currency: ")
    res = requests.get("http://data.fixer.io/api/latest",
                        params={"access_key":"1436e01b81b4ba6a72e1fa931e67c82c", "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    data = res.json()
    rate = data["rates"][other]
    date = data["date"]
    print(f"1 EUR is equal to {rate} {other}")
    print(f"Date: {date}")


if __name__ == "__main__":
    main()