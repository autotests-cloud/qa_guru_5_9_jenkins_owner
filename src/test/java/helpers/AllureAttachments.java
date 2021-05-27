package helpers;

import com.codeborne.selenide.Selenide;
import config.Project;
import io.qameta.allure.Attachment;

import static org.openqa.selenium.logging.LogType.BROWSER;

public class AllureAttachments {
    @Attachment(value = "{attachName}", type = "text/plain")
    public static String addMessage(String attachName, String text) {
        return text;
    }

    @Attachment(value = "Page source", type = "text/plain")
    public static byte[] addPageSource() {
        return DriverUtils.getPageSourceAsBytes();
    }

    @Attachment(value = "{attachName}", type = "image/png")
    public static byte[] addScreenshotAs(String attachName) {
        return DriverUtils.getScreenshotAsBytes();
    }

    @Attachment(value = "Video", type = "text/html", fileExtension = ".html")
    public static String addVideo() {
        return "<html><body><video width='100%' height='100%' controls autoplay><source src='"
                + Project.config.videoStorage()
                + DriverUtils.getRemoteSessionId()
                + ".mp4"
                + "' type='video/mp4'></video></body></html>";
    }

    public static void addBrowserConsoleLogs() {
        AllureAttachments.addMessage("Browser console logs", String.join("\n", Selenide.getWebDriverLogs(BROWSER)));
    }
}
