import psutil
from libqtile.widget import base

class BatteryWidget(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__("BatteryWidget", **config)
        self.add_defaults(BatteryWidget.defaults)

    defaults = [
        ("update_interval", 10, "Update interval in seconds."),
    ]

    def poll(self):
        battery = psutil.sensors_battery()
        if battery is not None:
            plugged = battery.power_plugged
            percent = battery.percent
            if plugged:
                return f"Battery: {int(percent)}% (Charging)"
            else:
                return f"Battery: {int(percent)}%"
        else:
            return "Battery: N/A"
