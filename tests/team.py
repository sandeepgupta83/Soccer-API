from requests import post, get, put, delete
import unittest

class TeamTest(unittest.TestCase):

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

    def test_create_team(self):
        r = post(
            "http://127.0.0.1:5000/api/v1/teams",
            headers=self.headers,
            json={
                "Team Name": "team one one",
                "Logo URI": "http://ontene"
            }
        )
        response = r.json()
        assert r.status_code == 201
        assert response['message'] == "New Team Created"

    def test_update_team(self):
        r = put(
            "http://127.0.0.1:5000/api/v1/teams/2",
            headers=self.headers,
            json={
                "Team Name": "new team"
            }
        )
        assert r.status_code == 200


if __name__ == "__main__":
    unittest.main()


