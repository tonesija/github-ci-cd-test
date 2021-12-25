

class TestMainRouter:

    def test_get(self, client):
        res = client.get("/")

        assert res.status_code == 200
