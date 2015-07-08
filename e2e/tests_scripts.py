from django.test import TestCase
from scripts import load_bootswatch_themes
from authenticating.models import Theme


class LoadBootswatchTests(TestCase):
    def tearDown(self):
        Theme.objects.all().delete()

    def _assert_count(self):
        self.assertEqual(
            len(Theme.objects.all()),
            len(load_bootswatch_themes.theme_list)
        )

    def test_load(self):
        """
        should load themes
        """
        load_bootswatch_themes.run()
        self._assert_count()

    def test_purge(self):
        """
        should purge themes if 'purge' in args
        """
        load_bootswatch_themes.run()
        load_bootswatch_themes.run('purge')
        self._assert_count()
