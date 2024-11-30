class TV:

    def __init__(self, brand, price, inches, false ):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.channel = 1
        self.volume = 50
        self.is_on = false

    def system_power(self):
        self.is_on = not self.is_on

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    # status tv_system
    def system_status(self):
        def system_power(self):
            if (self.is_on):
                "ON"
            else:
                "OFF"
                return f"self.brand : {system_power}, channel : {self.channel}, volume : {self.volume}"


class led_TV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        self.brand =brand
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def diapaly_TV(self):
        return (
            f" screen_thickness : {self.screen_thickness} , energy_usage : {self.energy_usage}, lifespan {self.lifespan}, refresh_rate {self.refresh_rate}")










