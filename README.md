
# USAGE examples

Run in local chrome:

```bash

```

Run in local firefox:

```bash
env -S "browser=firefox" pytest tests/
```

Run on remote hub without auth:

```bash
env -S "remote_webdriver_url=https://selenoid.autotests.cloud/wd/hub/" pytest tests/
```

Run on remote hub with explicit auth:

```bash
env -S "remote_webdriver_url=https://user:pswd@selenoid.autotests.cloud/wd/hub/" pytest tests/
```

Run on remote hub with implicit auth credentials (read from properties set in config.env, otherwise failed):

```bash
env -S "remote_webdriver_url=https://%:%@selenoid.autotests.cloud/wd/hub/" pytest tests/
```

Run parallelized (`-n auto`) with report (`--alluredir=reports`) on remote hub with implicit auth credentials + attach videos to report:

```bash
env -S "remote_webdriver_url=https://%:%@selenoid.autotests.cloud/wd/hub/ video_storage=https://selenoid.autotests.cloud/video/" pytest tests/ -n auto --alluredir=reports
```

Serve report:

```bash
allure serve build/allure-results
```