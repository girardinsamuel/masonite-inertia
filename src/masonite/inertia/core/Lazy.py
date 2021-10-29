class LazyProp:
    def __init__(self, callable):
        self.callable = callable

    def __call__(self, *args):
        return self.callable(*args)
