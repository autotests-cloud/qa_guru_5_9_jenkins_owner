from allure import step as allure_step


def step(title):
    if callable(title):
        fn = title
        fn_with_reporting_to_allure = allure_step(title)(fn)
        fn_with_reporting_to_allure()
    else:
        def decorator(fn):
            fn_with_reporting_to_allure = allure_step(title)(fn)
            fn_with_reporting_to_allure()
        return decorator