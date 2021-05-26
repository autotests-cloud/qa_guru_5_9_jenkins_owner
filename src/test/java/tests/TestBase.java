package tests;

import com.codeborne.selenide.Configuration;
import com.codeborne.selenide.Selenide;
import com.codeborne.selenide.logevents.SelenideLogger;
import config.ProjectConfig;
import helpers.AttachmentHelper;
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

        Configuration.browser = ProjectConfig.driver.browser();
        System.out.println("remoteWebDriver: " + ProjectConfig.driver.remoteUrl());

        if(ProjectConfig.driver.remoteUrl() != null) {
            String user = ProjectConfig.driver.remoteUser();
            String password = ProjectConfig.driver.remotePassword();
            Configuration.remote = String.format(ProjectConfig.driver.remoteUrl(), user, password);

            System.out.println("Running on a remote hub with...");
            System.out.println("user: " + user);
            System.out.println("password: " + password);
            System.out.println("remote url: " + ProjectConfig.driver.remoteUrl());
            System.out.println("formatted url: " + String.format(ProjectConfig.driver.remoteUrl(), user, password));
        }
    }

    @AfterEach
    void afterEach() {
        AttachmentHelper.attachScreenshot("Last screenshot");
        AttachmentHelper.attachPageSource();
        AttachmentHelper.attachAsText("Browser console logs", AttachmentHelper.getConsoleLogs());

        if(ProjectConfig.driver.videoStorage() != null) {
            AttachmentHelper.attachVideo();
        }
        
        Selenide.closeWebDriver();
    }
}
