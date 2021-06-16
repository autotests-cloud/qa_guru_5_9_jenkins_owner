from allure import step as Step


def step(title):
    if callable(title):
        fn = title
        fn_with_logging_to_allure = Step(fn)
        fn_with_logging_to_allure()
    else:
        def decorator(fn):
            fn_with_logging_to_allure = Step(title)(fn)
            fn_with_logging_to_allure()
        return decorator
