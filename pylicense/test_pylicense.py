from unittest import TestCase

from pylicense import pylicense


class TestPylicense(TestCase):
    def test_get_license_from_url(self):
        license_str = pylicense.get_license_from_url("https://github.com/AtsushiSakai/pylicense")
        self.assertIn("MIT", license_str)

        license_str = pylicense.get_license_from_url("https://github.com/furo-org/LittleSLAM")
        self.assertIn("Mozilla Public License 2.0", license_str)

        license_str = pylicense.get_license_from_url("https://github.com/at-wat/neonavigation")
        self.assertIn("Other", license_str)
