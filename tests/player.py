from requests import post, get, put, delete
import unittest

class PlayerTest(unittest.TestCase):

    def setUp(self):
        r = post(
            "http://127.0.0.1:5000/login",
            json={
                "username": "test",
                "password": "test"
            })
        resp = r.json()
        # print(resp['access_token'])
        self.token = resp['access_token']
        self.headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

    def test_create_player(self):
        r = post(
            "http://127.0.0.1:5000/api/v1/players",
            headers=self.headers,
            json={
                "Team": "sicks",
                "First Name": "one",
                "Last Name": "1",
                "Image URI": "http://karsas"
            }
        )
        response = r.json()
        assert r.status_code == 201
        assert response['message'] == 'New Player Created'

    def test_update_player(self):
        r = put(
            "http://127.0.0.1:5000/api/v1/players/1",
            headers=self.headers,
            json={
                # "Team": "sicks",
                "First Name": "updated name",
                "Last Name": "hjhhj",
                "Image URI": "http://karsas_updated"
            }
        )
        assert r.status_code == 200

    def test_delete_player(self):
        r = delete(
            "http://127.0.0.1:5000/api/v1/players/8",
            headers=self.headers
        )
        assert r.status_code == 200


if __name__ == "__main__":
    unittest.main()


