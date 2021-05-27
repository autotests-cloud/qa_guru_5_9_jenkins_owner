package config;

import org.aeonbits.owner.Config;
import org.aeonbits.owner.ConfigFactory;

@Config.LoadPolicy(Config.LoadType.MERGE)
@Config.Sources({
        "system:properties",
        "classpath:config/driver.properties"
})
public interface ProjectConfig extends Config {
    String remoteWebDriver();

    String remoteWebDriverUser();

    @DefaultValue("chrome")
    String browser();

    String remoteWebDriverPassword();

    String videoStorage();
}
