if __name__ == "__main__":
    print("Do NOT execute this script directly. Execute the acrpy.py at the parent directory.")

import requests

url = "https://api.thegraph.com/subgraphs/name/traderjoe-xyz/exchange"

# Todo: trim unnec fields.
query = '''query pairDetailQuery($first: Int! = 1, $orderBy: String! = "trackedReserveAVAX", $orderDirection: String! = "desc", $dateAfter: Int! = 1629056839) {{
  pairs(
    first: $first
    orderBy: $orderBy
    orderDirection: $orderDirection
    where: {{token0_in: ["{contract}", "0xc7198437980c041c805a1edcba50c1ce5db95118"], token1_in: ["{contract}", "0xc7198437980c041c805a1edcba50c1ce5db95118"]}}
  ) {{
    id
    name
    token0Price
    token1Price
    token0 {{
      id
      symbol
      name
      decimals
      derivedAVAX
    }}
    token1 {{
      id
      symbol
      name
      decimals
      derivedAVAX
    }}
    reserve0
    reserve1
    reserveUSD
    volumeUSD
    timestamp
  }}
}}'''

# Set the request headers
headers = {
    "Content-Type": "application/json"
}

# Set the request payload
def getPayload() -> str:
    global contractaddress
    global query
    payload = {
    "query": query.format(contract= contractaddress),
    "variables": {
        "first": 1,
        "orderBy": "trackedReserveAVAX",
        "orderDirection": "desc",
        "dateAfter": 1629056839
    },
        "operationName": "pairDetailQuery"
    }
    return payload


contractaddress = ""

def setContractAddress(addr: str) -> str:
    global contractaddress
    contractaddress = addr
    return requestSymbol()

def performRequest():
    try:
        pay = getPayload()
        response = requests.post(url, headers=headers, json=getPayload())
        return response
    except Exception as ex:
        print(f'Error while fetching the price: {ex}')
        return None
def requestSymbol() -> str:
    res = performRequest()
    if res is None:
        return res
    try:
        return res.json()["data"]["pairs"][0]["token0"]["symbol"]
    except:
        print(res.content)
        return None

def requestPrice() -> float:
    res = performRequest()
    if res is None:
        return res
    return float(res.json()["data"]["pairs"][0]["token1Price"])
