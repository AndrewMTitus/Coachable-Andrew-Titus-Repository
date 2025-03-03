class Thermostat:
    def __init__(self, temperature: float=72.0):
        self.temperature = temperature 
    def get_temperature(self):
        return self.temperature
    def set_temperature(self, new_temp):
        if new_temp < 50.0 or new_temp > 90.0:
            raise ValueError("Temperature must be between 50°F and 90°F")
        self.temperature = new_temp
    def __str__(self):
        return f"Temperature set to {self.temperature}°F"

class SmartThermostat(Thermostat):
    def __init__(self, temperature: float=72.0, eco_mode: bool=False):
        super().__init__(temperature)
        self.eco_mode = eco_mode
    
    def set_temperature(self, new_temp: float):
        if self.eco_mode:
            if new_temp < 60.0 or new_temp > 78.0:
                raise ValueError("In eco mode, temperature must be between 60°F and 78°F.")
            else:
                if new_temp < 50.0 or new_temp > 90.0:
                    raise ValueError("Temperature must be between 50°F and 90°F.")
        self.temperature = new_temp
    
    def toggle_eco_mode(self):
        self.eco_mode = not self.eco_mode
    
    def __str__(self):
        mode_status = "on" if self.eco_mode else "off"
        return f"Thermostat set to {self.temperature}°F, eco mode is {mode_status}"

#Test Cases
smart_thermo = SmartThermostat(temperature=70.0, eco_mode=True)

print(smart_thermo)  # Output: Thermostat set to 70.0°F, eco mode is on

try:
    smart_thermo.set_temperature(55.0)  # This will raise an error
except ValueError as e:
    print(e)  # Output: In eco mode, temperature must be between 60°F and 78°F.

# Toggle eco mode
smart_thermo.toggle_eco_mode()
print(smart_thermo)  # Output: Thermostat set to 70.0°F, eco mode is off

# Set a valid temperature
smart_thermo.set_temperature(55.0)
print(smart_thermo)  # Output: Thermostat set to 55.0°F, eco mode is off
