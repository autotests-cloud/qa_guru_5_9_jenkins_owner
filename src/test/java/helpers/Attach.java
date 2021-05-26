package helpers;

import com.codeborne.selenide.Selenide;
import config.ProjectConfig;
import io.qameta.allure.Attachment;

import static org.openqa.selenium.logging.LogType.BROWSER;

public class Attach {
    @Attachment(value = "{attachName}", type = "text/plain")
    public static String message(String attachName, String text) {
        return text;
    }

    @Attachment(value = "Page source", type = "text/plain")
    public static byte[] pageSource() {
        return DriverUtils.getPageSourceAsBytes();
    }

    @Attachment(value = "{attachName}", type = "image/png")
    public static byte[] screenshotAs(String attachName) {
        return DriverUtils.getScreenshotAsBytes();
    }

    @Attachment(value = "Video", type = "text/html", fileExtension = ".html")
    public static String attachVideo() {
        return "<html><body><video width='100%' height='100%' controls autoplay><source src='"
                + ProjectConfig.driver.videoStorage()
                + DriverUtils.getRemoteSessionId()
                + ".mp4"
                + "' type='video/mp4'></video></body></html>";
    }

    public static void attachBrowserConsoleLogs() {
        Attach.message("Browser console logs", String.join("\n", Selenide.getWebDriverLogs(BROWSER)));
    }
}
