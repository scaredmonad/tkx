import tkinter as tk
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from src.rx import Observer
from src.lib import *

class Counter(Element):
    def __init__(self):
        super().__init__()
        self.count = Observer(0)

    def increment(self):
        self.count.value += 1

    def decrement(self):
        self.count.value -= 1

    def render(self):
        return Container(
            children=[
                Text(text="Counter Value:"),
                Text(text=str(self.count.value)),
                Button(text="Increment", command=self.increment),
                Button(text="Decrement", command=self.decrement),
            ]
        )


def main():
    app = Window(
        title="Basic Test",
        width=800,
        height=600,
        children=Counter().render()
    )

    app.render()


if __name__ == "__main__":
    main()
