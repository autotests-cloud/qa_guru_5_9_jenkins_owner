# Initial Project Setup

## Prerequisites
* pyenv
  ** python 3.8.2
* poetry

## Setup

Open terminal in your project folder and do:

```bash
poetry install
```

Set a project interpreter in your editor to: `"$(poetry env info -p)/bin/python"`, and you should be ready to go;)

# USAGE examples

Run in local chrome:

```bash
gradle clean test
```

Run in local opera:

```bash
gradle clean test -Dbrowser=opera
```

Run on remote hub without auth:

```bash
gradle clean test -DremoteWebDriverUrl="https://selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with explicit auth:

```bash
gradle clean test -DremoteWebDriverUrl="https://user1:1234@selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with implicit auth credentials (read from properties if set, otherwise failed):

```bash
gradle clean test -DremoteWebDriverUrl="https://%s:%s@selenoid.autotests.cloud/wd/hub/"
```

Run on remote hub with implicit auth credentials + attach videos to report:

```bash
gradle clean test -DremoteWebDriverUrl="https://%s:%s@selenoid.autotests.cloud/wd/hub/" -DvideoStorage="https://selenoid.autotests.cloud/video/"
```

Serve report:

```bash
allure serve build/allure-results
```