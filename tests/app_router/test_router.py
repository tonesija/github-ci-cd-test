

class TestMainRouter:

    def test_get(self, client):
        res = client.get("/")

        assert res.status_code == 200

    def test_get_fail_notanymore(self, client):
        res = client.get("/")

        assert res.status_code == 200

    def another_test(self):
        assert 3 == 1 + 2
