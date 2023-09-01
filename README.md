### tkx

**tkx** is a utility for declarative rendering with Tkinter.

_Please only use if necessary, I intend to add (based on my other projects) what I need when I get free time._

#### Overview

There is no need to use a virtual env since only the standard lib is used.

```py
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
```

#### Creating windows

```py
Window(
    title="Title",
    width=500,
    height=300,
    children=Text(text="Hello, World!")
).render()
```

#### Scoped state (getter/setters)

For non-iterables (currently int) and only `Text`, overloaded as `Text.rx` as a runtime specifier. `PropertyObserver` is thin and can only work when scoped/defined in a class declaration. Unpainting the frame is shitty right now, will likely not give this attention as it involves clearing `Frame` instances with `winfo_children` which doesn't work (YMMV).

```py
from tkx.rx import PropertyObserver
from tkx.lib import *

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
```

#### License

MIT © 2023.
