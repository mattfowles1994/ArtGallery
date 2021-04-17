from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        path = reverse('art:artwork', kwargs={'id': 1})
        assert resolve(path).view_name == 'art:artwork'