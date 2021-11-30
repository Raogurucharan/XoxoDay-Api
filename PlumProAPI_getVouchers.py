import requests

url = "https://stagingaccount.xoxoday.com/chef/v1/oauth/api"

payload = {
	"query": "plumProAPI.mutation.getVouchers",
	"tag": "plumProAPI",
	"variables": {
		"data":{
			"limit": 10,
        	"page": 1,
        	"includeProducts": "<product Id>", #eg: 9080
        	"excludeProducts": "<Product id to be excluded>",
        	"sort": {
        		"field":"name",
        		"order":"ASC"
        	},
        	"filters":[
        		{
        			"key": "productName",
        			"value": "Myntra"
        		}
    		]
		}
	}
}
headers = {
  'Authorization': 'Bearer eyJ0b2tlbkNvbnRlbnQiOnsiaXNzdWVkRm9yIjoiUGx1bSBQcm8iLCJzY29wZSI6IiIsImlzc3VlZEF0IjoxNTg5OTYyMTg4ODg1LCJleHBpcmVzQXQiOiIyMDIwLTA2LTA0VDA4OjA5OjQ4Ljg4NVoiLCJ0b2tlbl90eXBlIjoiVVNFUiJ9LCJhX3QiOiJleUpsYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySWl3aVlXeG5Jam9pUlVORVNDMUZVeUlzSW10cFpDSTZJbVZ1WXlJc0ltVndheUk2ZXlKcmRIa2lPaUpGUXlJc0ltTnlkaUk2SWxBdE1qVTJJaXdpZUNJNklqRlVkazVvWmxWU1pITjBNMXBqWmxadVQyOTFSWEpCVERSaWJtZGtTMVZLTVhobWMwcHdORFppTUc4aUxDSjVJam9pT0ZaMWJYTjZVbU50WDNKQk16WlVUVFpVYUZGNVIwY3lVa1ZxTFV0b1JtNDJXbHBXWDNOdFExWm5ZeUo5ZlEuLjN1emtMcXBUUlhDOHFzVmpmMnpoX1EuSU9YeTRidEVqTTRhXzM0YkcxOEF2MmhJWUxnUnUwVy1vZ2Vva2pwRFE4QnlMV0l2dXpLV3dDdi02eFJYSlBXbnBGQ2d4TlFRZDJVUDVDaWJvc2prSU9Mc28wOW9qelBPd2ZWaFp3UDc2UkJ0djVoTThGVU0tWkphZEJCSmkwRVdPQmNBb3RIQnpwT2FfVzE2LVJZOFl3MGhTUExyNnJnWmhXN1A1TUtpZ1A5S3pMTlBubTdjZVVQRjNYLWlOR0M1aVkwSFhTVEZLSmpzVENtYjFjQkVmSDNsaGtfWmozbEdHZHJlb0RMNEJfdWFEUUZHNXFFRUNmaWE5QXFDenNXTVR2ZjNJR3d5ZVNsSmdKa1pKUkhlbnNSdHpzZTBvOS1YVTByX2pUdVlhcFNZSzlRSE9iQm9kVFNNMHRVWUxJYUJvQTl2NTZXVXhwNkVrWFJoVE9FSmFlOXlTNU1QQTRUODdUTkcyWk8xelVfRXZHYXhNaUtWSGpjalFPVFctYjhmLXREV1F0YzROblBjTnFHY3J2NWYxbFZkZ0llNFJOOGRTWTFPdVM4ODBiYWpCY0pMY0ZlQ1dtTXJHSXgtaWRtNVdaNnFzOXVxa2VzbmRhS2gweEdLdGRTMTU5ZlRXRkxFTnl2ZFVUWjhFWmd0QmU3eVNmOUhqV0ctQTc4ejExdDdNRnJ3RFl0cFRUV2pwUGxoUDEwRWNOd0hJRDd6djVjLXRVcWUxdXc2TjhqNEFrQ1lld3kza1V5SlJWbVNzNllJcFI2MVItbXBKVktSdVBzSG16ZmxfMGE0VVBnLWlWMmlxYXdOUEtkY1I1U1BLclI3U0FRTE5JT0FXY2ZRREpZSVgtTWVJRXhNM20xRWZ6aGdtLUFnbDV4cElUM3Z2NWtwdTQzY29VN2JOLU10M0VTQjFOZld6MW5TMnhBTDZFemx0bkkzeGFQOFNxZmRtZDJjWWRmNWJXSEJRNXdEWXBxMGNVVzVidlNyYzRad3VCNS1HdUpEbG5RLVFHYnhGZUs3Lk1TQ0I1bVUxUTlESmdESGQtRkNxM3cifQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)