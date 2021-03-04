"""Test views for webapp app."""


from django.test import LiveServerTestCase, Client
from django.contrib.auth import get_user_model
from selenium import webdriver
from django.contrib import auth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class FirefoxFunctionalTestCases(LiveServerTestCase):
    """Functional tests using the Firefox web browser."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user1", password="mdp123mdp"
        )

    def test_user_can_connect_and_disconnect_without_error(self):
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

    # def test_user_can_search_in_nav_search_field(self):
    #     self.driver.get(self.live_server_url)
    #     self.driver.find_element_by_css_selector(
    #         "#search-nav-input"
    #     ).send_keys("pizza")
    #     self.driver.find_element_by_css_selector(
    #         "#search-nav-input"
    #     ).send_keys(Keys.ENTER)
    #     self.assertEqual(
    #         self.driver.current_url,
    #         "{}/webapp/results?query=pizza".format(self.live_server_url),
    #     )