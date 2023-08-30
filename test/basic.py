import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from src.lib import *


def main():
    app = Window(
        title="Basic Test",
        width=800,
        height=600,
        children=Container(
            children=[
                Text(text="Text 1"),
                Button(text="Click me", command=lambda: print("Button clicked")),
                Container(
                    children=[
                        Text(text="Nested Container"),
                        Button(text="Nested Button", command=lambda: print(
                            "Nested Button clicked")),
                    ]
                ),
            ]
        )
    )

    app.render()


if __name__ == "__main__":
    main()
