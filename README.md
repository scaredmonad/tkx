### tkx

**tkx** is a utility for declarative rendering with Tkinter.

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

#### License

MIT © 2023.
