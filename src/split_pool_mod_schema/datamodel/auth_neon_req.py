import pprint
from typing import Dict, Any

import requests


# # Replace TOKEN_VALUE with your API Token
# # X-API-Token header
# curl --verbose -H "X-API-Token: TOKEN_VALUE" \
#   -X GET https://data.neonscience.org/api/v0/products/DP1.00001.001 \
#   >> neon-data-products-DP1.00001.001.json

# # apiToken query parameter
# curl --verbose \
#   -X GET https://data.neonscience.org/api/v0/products/DP1.00001.001?apiToken=TOKEN_VALUE \
#   >> neon-data-products-DP1.00001.001.json


def get_raw_result(sample_uuid: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                   param_name="sampleUuid") -> Dict[str, Any]:
    assembled_url = f"{base_url}?{param_name}={sample_uuid}"
    header = {
        "X-API-Token":
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJNQU1AbGJsLmdvdiIsInNjb3BlIjoicmF0ZTpwdWJsaWMiLCJpc3MiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnLyIsImV4cCI6MTg0MDYzMTY3MywiaWF0IjoxNjgyOTUxNjczLCJlbWFpbCI6Ik1BTUBsYmwuZ292In0.H0P7ke_WL7syECGAA4khEddZ8f6sR__vA3TFherLVt8I1omtYNjspqwWZh42ZkoCbCmRTIr4b4OG8uqPhICv8g"}
    return requests.get(assembled_url, headers=header)


result = get_raw_result('ba5a86ba-767d-4434-94c1-b57acdcfbba9')
headers = result.headers

# print(type(headers))
# <class 'requests.structures.CaseInsensitiveDict'>
# pprint.pprint(headers['content-encoding'])

pprint.pprint(dict(headers))

pprint.pprint(result.json())

# {'access-control-allow-origin': '*',
#  'content-encoding': 'gzip',
#  'content-type': 'application/json;charset=UTF-8',
#  'date': 'Mon, 01 May 2023 15:08:28 GMT',
#  'strict-transport-security': 'max-age=31536000; includeSubdomains; preload;',
#  'transfer-encoding': 'chunked',
#  'vary': 'Accept-Encoding',
#  'x-content-type-options': 'nosniff',
#  'x-forwarded-proto': 'https',
#  'x-frame-options': 'SAMEORIGIN',
#  'x-ratelimit-limit': '200',
#  'x-ratelimit-remaining': '200',
#  'x-xss-protection': '1'}

# If you exceed the rate limit, you will receive the following response:
# HTTP/1.1 429 Too Many Requests
# Status: 429 Too Many Requests
# X-RateLimit-Limit: 200
# X-RateLimit-Remaining: 0
# X-RateLimit-Reset: 100
# RetryAfter: 1
