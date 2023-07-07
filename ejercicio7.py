import requests
import unittest

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 3
B = 2


class TestRequest(unittest.TestCase):

    def test_request_get(self):
        parametros = {
            "a": A,
            "b": B
        }

        response1 = requests.get(URL, params=parametros)
        self.assertEqual(float(response1.text), 5)

    def test_request_post(self):
        data = {
            "a": A,
            "b": B
        }

        response2 = requests.post(URL, json=data)
        self.assertEqual(float(response2.json()["result"]), 5)


if __name__ == '__main__':
    unittest.main()
