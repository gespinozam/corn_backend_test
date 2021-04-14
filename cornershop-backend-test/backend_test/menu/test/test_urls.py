from django.urls import reverse, resolve


class TestUrls:
    def test_detail_url(self):
        path = reverse("details", kwargs={"pk": "d9fb40d8-bd09-4b30-b782-347828cb25ca"})
        assert resolve(path).view_name == "details"

    def test_update_url(self):
        path = reverse("update", kwargs={"pk": "5abf161a-4dae-43f9-a369-6543c37a7fd6"})
        assert resolve(path).view_name == "update"

    def test_delete_url(self):
        path = reverse("delete", kwargs={"pk": "a6c0dc09-9a55-482b-a698-ed087b93b748"})
        assert resolve(path).view_name == "delete"
