package helpers;

import com.codeborne.selenide.Selenide;
import config.ProjectConfig;
import io.qameta.allure.Attachment;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import java.nio.charset.StandardCharsets;

import static com.codeborne.selenide.WebDriverRunner.getWebDriver;
import static org.openqa.selenium.logging.LogType.BROWSER;

public class AttachmentHelper {
    @Attachment(value = "{attachName}", type = "text/plain")
    public static String attachAsText(String attachName, String message) {
        return message;
    }

    @Attachment(value = "Page source", type = "text/plain")
    public static byte[] attachPageSource() {
        return DriverUtils.getPageSourceAsBytes();
    }

    @Attachment(value = "{attachName}", type = "image/png")
    public static byte[] attachScreenshot(String attachName) {
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
        AttachmentHelper.attachAsText("Browser console logs", String.join("\n", Selenide.getWebDriverLogs(BROWSER)));
    }
}
