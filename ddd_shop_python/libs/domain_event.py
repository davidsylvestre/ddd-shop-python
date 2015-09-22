class DomainEvents(object):

    def __init__(self):
        pass

    @classmethod
    def trigger(cls, event):

        handlers = set()
        for child in event.__class__.__subclasses__():
            if child not in handlers:
                handlers.add(child)

        for handler in handlers:
            handler_instance = handler()
            handler_instance.run()
