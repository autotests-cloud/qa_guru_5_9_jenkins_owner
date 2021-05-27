package tests;

import com.codeborne.selenide.Configuration;
import com.codeborne.selenide.Selenide;
import com.codeborne.selenide.logevents.SelenideLogger;
import config.Project;
import helpers.Attachments;
import io.qameta.allure.selenide.AllureSelenide;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.openqa.selenium.remote.DesiredCapabilities;


public class TestBase {

    @BeforeAll
    static void setup() {
        SelenideLogger.addListener("AllureSelenide", new AllureSelenide());

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("enableVNC", true);
        capabilities.setCapability("enableVideo", true);
        Configuration.browserCapabilities = capabilities;

        Configuration.browser = Project.config.browser();
        System.out.println("remoteWebDriver: " + Project.config.remoteWebDriverUrl());

        if(Project.config.remoteWebDriverUrl() != null) {
            String user = Project.config.remoteWebDriverUser();
            String password = Project.config.remoteWebDriverPassword();
            Configuration.remote = String.format(Project.config.remoteWebDriverUrl(), user, password);

            System.out.println("Running on a remote hub with...");
            System.out.println("user: " + user);
            System.out.println("password: " + password);
            System.out.println("remote url: " + Project.config.remoteWebDriverUrl());
            System.out.println("formatted url: " + String.format(Project.config.remoteWebDriverUrl(), user, password));
        }
    }

    @AfterEach
    void afterEach() {
        Attachments.addScreenshotAs("Last screenshot");
        Attachments.addPageSource();
        Attachments.addBrowserConsoleLogs();

        if(Project.config.videoStorage() != null) {
            Attachments.addVideo();
        }
        
        Selenide.closeWebDriver();
    }
}
