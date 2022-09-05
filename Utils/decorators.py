def async_caller(function):
    def wrapper_function():
        try:
            function()

        except Exception as err:
            print(err)
            return err
