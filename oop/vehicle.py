class Vehicle:
    def __init__(self, starting_top_speed = 100):
        self.top_speed = starting_top_speed
        self.__warnings = []

    def drive(self):
        print("I am driving but notfadter than {}".format(self.top_speed))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnigs(self):
        return self.__warnings

