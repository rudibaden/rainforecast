import hassapi as hass
import time
import datetime

class Get_Accu_RainForeCast(hass.Hass):
    def initialize(self):
        
        self.log("accu_rainforecast initializing...")
        self.set_state( "sensor.acc_rain_prob", state=str(datetime.time.second), replace=True, attributes={"friendly_name": "AccuWeather Rain Probability"})

        self.get_state('sensor.acc_rain_prob');
        # Run every two minutes  
        self.run_every(self.callback, time, 2 * 60)

    def callback(self, cb_args):
        newState = str(datetime.time.second)
        self.log("accu_rainforecast: setting state " + newState)
        self.set_state( "sensor.acc_rain_prob", state=newState, replace=True, attributes={"friendly_name": "AccuWeather Rain Probability"})