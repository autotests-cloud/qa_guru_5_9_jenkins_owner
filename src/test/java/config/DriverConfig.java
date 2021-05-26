package config;

import org.aeonbits.owner.Config;

@Config.LoadPolicy(Config.LoadType.MERGE)
@Config.Sources({
        "system:properties",
        "classpath:config/driver.properties",
})
public interface DriverConfig extends Config {
    @DefaultValue("chrome")
    @Key("driver.browser")
    String browser();

    @Key("driver.remoteUrl")
    String remoteUrl();

    @Key("driver.remoteUser")
    String remoteUser();

    @Key("driver.remotePassword")
    String remotePassword();

    @Key("driver.videoStorage")
    String videoStorage();
}
