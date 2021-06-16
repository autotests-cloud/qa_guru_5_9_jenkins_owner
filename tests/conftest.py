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
# public class ConfTest {
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
#     @AfterEach                      /* <<< LET'S TRANSLATE ONLY THIS SO FAR */
#     void afterEach() {              /* <<< LET'S TRANSLATE ONLY THIS SO FAR */
#         AllureAttachments.addScreenshotAs("Last screenshot");
#         AllureAttachments.addPageSource();
#         AllureAttachments.addBrowserConsoleLogs();
#
#         if(Project.config.videoStorage() != null) {
#             AllureAttachments.addVideo();
#         }
#
#         Selenide.closeWebDriver();  /* <<< LET'S TRANSLATE ONLY THIS SO FAR */
#     }
# }
import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def quite_browser():

    yield

    browser.quit()
