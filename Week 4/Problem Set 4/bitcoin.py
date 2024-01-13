import requests
import sys

if len(sys.argv) == 2:
    try:
        q = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
output = response.json()
bpi = output["bpi"]
usd = bpi["USD"]
rate = float(usd["rate_float"])
amount = rate * q
print(f"${amount:,.4f}")