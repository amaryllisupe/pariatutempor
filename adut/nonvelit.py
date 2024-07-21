class ViewConfig:
    def __init__(self, labels, other_setting):
        self.labels = labels
        self.other_setting = other_setting

    def display_config(self):
        print(f"Labels: {self.labels}, Other Setting: {self.other_setting}")

config = ViewConfig(labels='main', other_setting='value')
config.display_config()
