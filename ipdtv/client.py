import http.client
import json

API_BASE_PATH = "ipd-tv:8001"
APPLICATION_ID = "python-demo-client"
APPLICATION_SECRET = "*****"


def push_data(data_source_uid, values):
    post_data = {
        "data_source_uid": data_source_uid,
        "values": values
    }

    headers = {}
    payload = json.dumps(post_data)
    conn = http.client.HTTPConnection(API_BASE_PATH)
    conn.request("POST", "/api/v1/data_source/push", payload, headers)
    response = conn.getresponse()

    print(response.read().decode())
