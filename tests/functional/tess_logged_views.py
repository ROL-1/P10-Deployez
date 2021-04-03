"""Test views for webapp app."""

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase, Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class FirefoxFunctionalTestCases(LiveServerTestCase):
    """Functional tests using the Firefox web browser."""

    @classmethod
    def setUpClass(cls):
        """Create webdriver."""
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Leave driver."""
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        """Load user model."""
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user1", password="mdp123mdp"
        )

    def test_user_can_connect_and_disconnect_without_error(self):
        """User can connect and disconnect without error."""
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector("#button-login").click()
        self.driver.find_element_by_css_selector("#id_username").send_keys(
            "user1"
        )
        self.driver.find_element_by_css_selector("#id_password").send_keys(
            "mdp123mdp"
        )
        self.driver.find_element_by_css_selector("#button-submit").click()
        self.driver.find_element_by_css_selector("#button-logout").click()
        self.assertEqual(
            self.driver.current_url, "{}/".format(self.live_server_url)
        )
