import requests

url = "https://stagingaccount.xoxoday.com/chef/v1/oauth/api"

payload = {
	"query": "plumProAPI.mutation.getOrderDetails",
	"tag": "plumProAPI",
	"variables": {
		"data":{
			"poNumber": "",
			"orderId": 1316578
		}
	}
}
headers = {
  'Authorization': '<Bearer token here>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)