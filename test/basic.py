import tkinter as tk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.lib import *

def main():
    root = tk.Tk()

    app = Container(
        children=[
            Text(text="Text 1"),
            Button(text="Click me", command=lambda: print("Button clicked")),
            Container(
                children=[
                    Text(text="Nested Container"),
                    Button(text="Nested Button", command=lambda: print("Nested Button clicked")),
                ]
            ),
        ]
    )
    
    app.render().pack()

    root.mainloop()

if __name__ == "__main__":
    main()
