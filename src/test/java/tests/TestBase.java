package tests;

import com.codeborne.selenide.Configuration;
import com.codeborne.selenide.Selenide;
import com.codeborne.selenide.logevents.SelenideLogger;
import config.Project;
import helpers.Attach;
import io.qameta.allure.selenide.AllureSelenide;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.openqa.selenium.remote.DesiredCapabilities;

import static helpers.Attach.*;

public class TestBase {

    @BeforeAll
    static void setup() {
        SelenideLogger.addListener("AllureSelenide", new AllureSelenide());

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("enableVNC", true);
        capabilities.setCapability("enableVideo", true);
        Configuration.browserCapabilities = capabilities;

        Configuration.browser = Project.config.browser();

        if(Project.config.remoteWebDriver() != null) {
            String user = Project.config.remoteWebDriverUser();
            String password = Project.config.remoteWebDriverPassword();
            Configuration.remote = String.format(Project.config.remoteWebDriver(), user, password);

            System.out.println(user);
            System.out.println(password);
            System.out.println(Project.config.remoteWebDriver());
            System.out.println(String.format(Project.config.remoteWebDriver(), user, password));
        }
    }

    @AfterEach
    void afterEach() {
        Attach.screenshotAs("Last screenshot");
        Attach.pageSource();
        Attach.browserConsoleLogs();
        if(Project.config.videoStorage() != null) {
            Attach.attachVideo();
        }

        Selenide.closeWebDriver();
    }
}
