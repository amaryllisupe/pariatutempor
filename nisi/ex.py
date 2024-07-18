class SmartHome:
    def __init__(self, location, temperature, lights, security):
        self.location = location
        self.temperature = temperature
        self.lights = lights
        self.security = security

    def display_status(self):
        print(f"Location: {self.location}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Lights: {self.lights}")
        print(f"Security: {self.security}")

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

    def turn_on_lights(self):
        self.lights = "On"

    def turn_off_lights(self):
        self.lights = "Off"

    def enable_security(self):
        self.security = "Enabled"

    def disable_security(self):
        self.security = "Disabled"


# Create a SmartHome object
my_home = SmartHome("Living Room", 22, "Off", "Enabled")

# Display the initial status
my_home.display_status()

# Change the temperature and display the updated status
my_home.set_temperature(24)
my_home.display_status()

# Turn on the lights and display the updated status
my_home.turn_on_lights()
my_home.display_status()

# Disable security and display the updated status
my_home.disable_security()
my_home.display_status()
