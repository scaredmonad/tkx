import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from src.rx import PropertyObserver
from src.lib import *


class Counter(Element):
    count = PropertyObserver(0)

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def render(self):
        return Container(
            children=[
                Text(text="Counter Value:"),
                Text.rx(text=str(self.count)),
                Button(text="Increment", command=self.increment),
                Button(text="Decrement", command=self.decrement),
            ]
        )


Window(
    title="Counter Test",
    width=500,
    height=300,
    children=Counter().render()
).render()
