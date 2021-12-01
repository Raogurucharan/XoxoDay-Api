import requests

url = "https://stagingaccount.xoxoday.com/chef/v1/oauth/api"

payload = {
    "query": "plumProAPI.mutation.placeOrder",
    "tag": "plumProAPI",
    "variables": {
      "data":{
        "productId":"<productId>",
        "quantity": "1",
        "denomination": "<price of voucher>",
        "email": "<enter the email>",
        "contact":"+91-<enter the phone number>",
        "tag":"",
        "poNumber":"qwerytuiop"
      }
    }
  }
  
headers = {
  'Authorization': 'Bearer eyJ0b2tlbkNvbnRlbnQiOnsiaXNzdWVkRm9yIjoicGx1bVByb1Rlc3QiLCJzY29wZSI6IiIsImlzc3VlZEF0IjoxNTg5OTY0OTU3OTk3LCJleHBpcmVzQXQiOiIyMDIwLTA2LTA0VDA4OjU1OjU3Ljk5N1oiLCJ0b2tlbl90eXBlIjoiVVNFUiJ9LCJhX3QiOiJleUpsYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySWl3aVlXeG5Jam9pUlVORVNDMUZVeUlzSW10cFpDSTZJbVZ1WXlJc0ltVndheUk2ZXlKcmRIa2lPaUpGUXlJc0ltTnlkaUk2SWxBdE1qVTJJaXdpZUNJNklteDJhRk0xTWw5ZmFHVXhVRkEyUTBOUGJIVmlSMnh1TVY4MGF6QjZjak5pU21OTk0xaGlYMDgwWDFFaUxDSjVJam9pZEVJelpFRnNVVmRVTFRKWVRVVnBWRzFIYUZVdFRWa3RVMEl6YzJ0eGNFODFOa1ZDUkd0dk1rVmFWU0o5ZlEuLkQ3UTZBMzJ1Z25RTHlkM0kyS3lFc0EuYVRNUWtraU9YaGRVeUVoeUlsODhuMFo2SnRzWDhmM05Ud1pHNFhGN25qMU9lbTlmLXltZWNsSnJHQUppS0hReTFrekFNTGE3ekZaRDFjMlM2dXFVckxqYlUtQXRnbWVxaFJKb0lrYnhHOEdFSDdEdGxreXhMa05iaFZfM0MwcC04aVlneTMyTHlvRE1xbUd1LXhZdEdleG10UDh1Y3ZSRzA5QWVxa3JsVzgtTEFoUjZjVE0tOWZybXNsRHhoZHFHWkVwMHJ1Nlh0N0Q4NlNXWHQ3QUItTTdCUl8xNUxDOTRCNjhOcjFPSnBZYmI5dkhlcVJpUWxfNG1wR3JaNFNfOVlkenFKS0R5WEdGLUdkVk40cWFZRy1Oc3RJTXFORUdEeWY1WEtYeGhDczhVYkktQ2J6YlRZbDVlajRITTRzVWdTVjAyT25xRjJqbzM1ME9LQVRuTWl0MWJMRmVzRy1HSDdrU09TY05LckpNZ1A2ZmdZcnlPMS1FNm1mT3hHc0xCYnRmc3VyNHoyOEJ4bk5GSC1NZUpNQWljdUtrYTQ1X2hTZ0tjclMxQU9NRTh2b1Fud0dBUDVyTlZxZUFWeUlSUW5sbHU1MUJ0TVJDdTNadWd0c0JDb1pscEJBVTlhTENTazlfOURTNTJ4a0NUQndmRWhPTjZ0aWxMcVdwb29nSWliazhBQ0xzWVMyUDJTajh2ZzdlUXB1TkRLU3VzNjJnOEI3WHBwUkh6NnNXb2tKUlhZU3RtUUxlZWNNYjNxTUVtb044Y1p1WmRvN0JsV3BGUVZRLUkzRnJ1MEJLeVVJbHFqazlxZFlCZmNsSkF5LWhjZXd3Z09SSEJyQ2hCNDB2SEV1cDZES0RiSTlYVGlfZ3lQZnYwc2x6SWVhYWZ3ZURfSUMtZUhIQ0hNWm5NWkV5emxRZ3BNWktnb1BXSm9MWnl0MWdVbll2cTl4Y1RBdG40b2NXZmFaOVVhTWpNZzdqZDc1dVczRF9jRmYwUjZjOTVDMElaUlN0QzdJZDMyZ1BsLmV0cXZOcTFUNmVIWnY2N0VleGg4Y3cifQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)