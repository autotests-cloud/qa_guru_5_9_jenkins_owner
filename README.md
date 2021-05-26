
# USAGE examples

Run in local chrome:

```bash
gradle clean test
```

Run in local opera:

```bash
gradle clean test -Dweb.browser=opera
```

Run on remote hub without auth:

```bash
gradle clean test -Dremote.web.driver="https://selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with explicit auth:

```bash
gradle clean test -Dremote.web.driver="https://user1:1234@selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with implicit auth credentials (read from properties if set, otherwise failed):

```bash
gradle clean test -Dremote.web.driver="https://%s:%s@selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with implicit auth credentials + attach videos to report:

```bash
gradle clean test -Dremote.web.driver="https://%s:%s@selenoid.autotests.cloud/wd/hub/" -Dvideo.storage="https://selenoid.autotests.cloud/video/"
```

Serve report:

```bash
allure serve build/allure-results
```