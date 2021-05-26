package config;

import org.aeonbits.owner.Config;

@Config.LoadPolicy(Config.LoadType.MERGE)
@Config.Sources({
        "system:properties",
        "classpath:config/driver.properties",
})
public interface DriverConfig extends Config {
    @DefaultValue("chrome")
    @Key("web.browser")
    String webBrowser();

    @Key("remote.web.driver")
    String remoteWebDriver();

    @Key("remote.web.user")
    String remoteWebUser();

    @Key("remote.web.password")
    String remoteWebPassword();

    @Key("video.storage")
    String videoStorage();
}
