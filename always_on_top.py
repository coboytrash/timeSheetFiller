class AlwaysOnTop:
    def __init__(self):
        self.always_on_top = not self.always_on_top
        self.attributes("-topmost", self.always_on_top)
        status = "ON" if self.always_on_top else "OFF"
        self.toggle_button.config(text=f"AOT: {status}")