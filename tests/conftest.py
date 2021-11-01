# package tests;
#
# import com.codeborne.selenide.Configuration;
# import com.codeborne.selenide.Selenide;
# import com.codeborne.selenide.logevents.SelenideLogger;
# import config.Project;
# import helpers.AllureAttachments;
# import io.qameta.allure.selenide.AllureSelenide;
# import org.junit.jupiter.api.AfterEach;
# import org.junit.jupiter.api.BeforeAll;
# import org.openqa.selenium.remote.DesiredCapabilities;
#
#
# public class TestBase {
#
#     @BeforeAll
#     static void setup() {
#         SelenideLogger.addListener("AllureSelenide", new AllureSelenide());
#
#         DesiredCapabilities capabilities = new DesiredCapabilities();
#         capabilities.setCapability("enableVNC", true);
#         capabilities.setCapability("enableVideo", true);
#         Configuration.browserCapabilities = capabilities;
#
#         Configuration.browser = Project.config.browser();
#         System.out.println("remoteWebDriver: " + Project.config.remoteWebDriverUrl());
#
#         if(Project.config.remoteWebDriverUrl() != null) {
#             String user = Project.config.remoteWebDriverUser();
#             String password = Project.config.remoteWebDriverPassword();
#             Configuration.remote = String.format(Project.config.remoteWebDriverUrl(), user, password);
#
#             System.out.println("Running on a remote hub with...");
#             System.out.println("user: " + user);
#             System.out.println("password: " + password);
#             System.out.println("remote url: " + Project.config.remoteWebDriverUrl());
#             System.out.println("formatted url: " + String.format(Project.config.remoteWebDriverUrl(), user, password));
#         }
#     }
#
#     @AfterEach
#     void afterEach() {
#         AllureAttachments.addScreenshotAs("Last screenshot");
#         AllureAttachments.addPageSource();
#         AllureAttachments.addBrowserConsoleLogs();
#
#         if(Project.config.videoStorage() != null) {
#             AllureAttachments.addVideo();
#         }
#
#         Selenide.closeWebDriver();
#     }
# }
import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import config


@pytest.fixture(scope='function', autouse=True)
def manage_browser():
    browser.config.timeout = config.settings.timeout
    driver = None

    if config.settings.browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.headless = True
        if not config.settings.remote_webdriver_url:
            driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=options,
            )
    elif config.settings.browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if not config.settings.remote_webdriver_url:
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options,
            )
    else:
        raise Exception('not supported browser: ' + config.settings.browser)

    if config.settings.remote_webdriver_url:
        options.set_capability('enableVNC', True)
        options.set_capability('enableVideo', True)
        user = config.settings.remote_webdriver_user
        password = config.settings.remote_webdriver_password
        remote_webdriver_url = config.settings.remote_webdriver_url % (user, password)

        driver = webdriver.Remote(
            command_executor=remote_webdriver_url,
            options=options,
        )

    browser.config.driver = driver

    yield

    browser.quit()
