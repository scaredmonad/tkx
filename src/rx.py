class Observer:
    def __init__(self, value=None):
        self._value = value
        self._callbacks = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            for callback in self._callbacks:
                callback()

    def observe(self, callback):
        self._callbacks.append(callback)

    def bind(self, prop):
        prop.value = self._value
        self.observe(lambda: setattr(prop, "value", self.value))


class PropertyObserver:
    def __init__(self, initial_value=None):
        self._observer = Observer(initial_value)

    def __get__(self, instance, owner):
        return self._observer.value

    def __set__(self, instance, value):
        self._observer.value = value
