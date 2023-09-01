from tkinter import ttk
import tkinter as tk


class Element:
    def __init__(self, **props):
        self._observers = []
        self.props = props
        self.children = props.get('children', [])

    def _observe(self, observer):
        observer.observe(self.render)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

        # ============ immediate text in container =============
        if type(value) is int:
            container = self.render()
            for child in container.children:
                if child.__class__ is Text and child.rx is True:
                    child = Text(text=value) # paints update
            lfr = container.render() # next tick
            print(type(container), type(lfr))
            for wgt in lfr.winfo_children():
                print(wgt)
                wgt.destroy()
            lfr.pack()

    def render(self):
        raise NotImplementedError(
            "Subclasses must implement the 'render' method.")


class Window:
    def __init__(self, title, width, height, children):
        self.title = title
        self.width = width
        self.height = height
        self.children = children

    def render(self):
        root = tk.Tk()
        root.title(self.title)

        root.geometry(f"{self.width}x{self.height}")

        app = self.children.render()
        app.pack(fill=tk.BOTH, expand=False)

        root.mainloop()


class Text(Element):
    def render(self):
        return tk.Label(text=self.props.get('text', ''))
    @staticmethod # triggers fine-grained rx-only updates
    def rx(text=""):
        instance = Text(text=text)
        instance.rx = True
        return instance


class Button(Element):
    def render(self):
        text = self.props.get('text', 'Button')
        command = self.props.get('command', None)

        style = ttk.Style()

        padding = self.props.get('padding', (2, 5))
        font_size = self.props.get('font_size', 10)
        foreground = self.props.get('foreground', 'black')
        background = self.props.get('background', 'lightgray')
        relief = self.props.get('relief', 'solid')

        style.configure(
            'Custom.TButton',
            padding=padding,
            font=('Helvetica', font_size),
            relief=relief,
            foreground=foreground,
            background=background,
        )

        button = ttk.Button(
            text=text,
            command=command,
            style='Custom.TButton'
        )

        return button


class Container(Element):
    def render(self):
        container = tk.Frame()
        for child in self.children:
            child_widget = child.render()
            child_widget.pack()
            container.pack()
        return container
