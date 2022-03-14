import awesome_python_app

def test_main_fail():
    """Checks main function.
    """
    value = 2
    assert value == awesome_python_app.main()

def test_main_pass():
    """Checks main function.
    """
    value = 1
    assert value == awesome_python_app.main()
