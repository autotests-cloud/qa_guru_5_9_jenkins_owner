package helpers;

import org.openqa.selenium.remote.RemoteWebDriver;

import static com.codeborne.selenide.WebDriverRunner.getWebDriver;

public class DriverUtils {
    public static String getRemoteSessionId(){
        return ((RemoteWebDriver) getWebDriver()).getSessionId().toString();
    }
}
