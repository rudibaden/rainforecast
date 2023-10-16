import hassapi as hass
import datetime

class Get_Accu_ForeCast(hass.Hass):
    def initialize(self):
        self.run_in(self.callback, 20)

    def callback(self, cb_args):
        sensorId = 'sensor.acc_rain_prob'
        txt = datetime.time.second
        friendlyName = 'AccuWeather Rain Probability'
        self.set_state(sensorId, state=txt, replace=True, attributes={"friendly_name": friendlyName})