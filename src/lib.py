import tkinter as tk

class Element:
    def __init__(self, **props):
        self.props = props
        self.children = props.get('children', [])
        
    def render(self):
        raise NotImplementedError("Subclasses must implement the 'render' method.")

class Text(Element):
    def render(self):
        return tk.Label(text=self.props.get('text', ''))

class Button(Element):
    def render(self):
        text = self.props.get('text', 'Button')
        command = self.props.get('command', None)
        return tk.Button(text=text, command=command)

class Container(Element):
    def render(self):
        container = tk.Frame()
        for child in self.children:
            child_widget = child.render()
            child_widget.pack()
            container.pack()
        return container
