import requests
import json


class SearchForFaceClient:
    def __init__(self, host: str, token: str):
        self.host = host
        self.headers = {
            "Content-Type": "application/json",
            "x-authorization-token": token
        }

    def __make_request(self, method: str, params: dict) -> requests.models.Response:
        try:
            res = requests.request(method, self.host,
                                   json=params, headers=self.headers)
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception(e)
        return res

    def rate_limit(self):
        params = {
            "jsonrpc": "2.0",
            "method": "rateLimit",
            "id": "some-id",
            "params": {}
        }
        res = self.__make_request('POST', params)
        return res

    def detected_face(self, byte_image: str):
        params = {
            "jsonrpc": "2.0",
            "method": "detectFaces",
            "id": "some-id",
            "params": {
                "image": byte_image
            }
        }
        res = self.__make_request('POST', params)
        return res

    def search_face(self, image: str, face: dict, source: str, results: int, hidden: bool, lang: str = "ru"):
        params = {
            "jsonrpc": "2.0",
            "method": "searchFace",
            "id": "some-id",
            "params": {
                "image": image,
                "face": face,
                "source": source,
                "hidden": hidden,
                "results": results,
                "lang": lang
            }
        }
        res = self.__make_request('POST', params)
        return res
