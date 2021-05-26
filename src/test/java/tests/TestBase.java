package tests;

import com.codeborne.selenide.Configuration;
import com.codeborne.selenide.Selenide;
import com.codeborne.selenide.logevents.SelenideLogger;
import config.DriverConfig;
import helpers.AttachmentHelper;
import io.qameta.allure.selenide.AllureSelenide;
import org.aeonbits.owner.ConfigFactory;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.openqa.selenium.remote.DesiredCapabilities;


public class TestBase {

    public static DriverConfig driverConfig = ConfigFactory.create(DriverConfig.class);

    @BeforeAll
    static void setup() {
        SelenideLogger.addListener("AllureSelenide", new AllureSelenide());

        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("enableVNC", true);
        capabilities.setCapability("enableVideo", true);
        Configuration.browserCapabilities = capabilities;

        Configuration.browser = driverConfig.webBrowser();
        System.out.println("remoteWebDriver: " + driverConfig.remoteWebDriver());

        if(driverConfig.remoteWebDriver() != null) {
            String user = driverConfig.remoteWebUser();
            String password = driverConfig.remoteWebPassword();
            Configuration.remote = String.format(driverConfig.remoteWebDriver(), user, password);

            System.out.println("Running on a remote hub with...");
            System.out.println("user: " + user);
            System.out.println("password: " + password);
            System.out.println("remote url: " + driverConfig.remoteWebDriver());
            System.out.println("formatted url: " + String.format(driverConfig.remoteWebDriver(), user, password));
        }
    }

    @AfterEach
    void afterEach() {
        AttachmentHelper.attachScreenshot("Last screenshot");
        AttachmentHelper.attachPageSource();
        AttachmentHelper.attachAsText("Browser console logs", AttachmentHelper.getConsoleLogs());

        if(driverConfig.videoStorage() != null) {
            AttachmentHelper.attachVideo();
        }
        
        Selenide.closeWebDriver();
    }
}
