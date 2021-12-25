

class TestMainRouter:

    def test_get(self, client):
        res = client.get("/")

        assert res.status_code == 200

    def test_get_fail_notanymore(self, client):
        res = client.get("/")

        assert res.status_code == 200

    def test_posts(self, client):
        res = client.get("/posts")

        res_json = res.json()

        assert res.status_code == 200
        assert len(res_json) == 2
