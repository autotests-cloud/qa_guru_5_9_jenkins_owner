package config;

import org.aeonbits.owner.ConfigFactory;

public class ProjectConfig {
    public static DriverConfig driver = ConfigFactory.create(DriverConfig.class);
}
