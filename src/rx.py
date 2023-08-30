class Observer:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            for callback in self._callbacks:
                callback(new_value)

    def subscribe(self, callback):
        self._callbacks.append(callback)

    def unsubscribe(self, callback):
        self._callbacks.remove(callback)
