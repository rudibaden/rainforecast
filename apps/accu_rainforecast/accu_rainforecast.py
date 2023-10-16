import hassapi as hass
import time
import datetime

class Get_Accu_RainForeCast(hass.Hass):
    def initialize(self):

        self.set_state( 'sensor.acc_rain_prob', state=datetime.time.second, replace=True, attributes={"friendly_name": 'AccuWeather Rain Probability'})

        self.listen_state(self.set_acc_sensors)

        # Run every two minutes  
        self.run_every(self.callback, time, 2 * 60)

    def callback(self, cb_args):       
        self.set_state( 'sensor.acc_rain_prob', state=datetime.time.second, replace=True, attributes={"friendly_name": 'AccuWeather Rain Probability'})
    
    def set_acc_sensors(self, entity, attribute, old, new, kwargs):
        self.set_state( 'sensor.acc_rain_prob', state=datetime.time.second, replace=True, attributes={"friendly_name": 'AccuWeather Rain Probability'})
