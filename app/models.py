from pydantic import BaseModel
from typing import Dict

class Telemetry(BaseModel):
    device_id : str
    timestamp : str
    sensor_values : Dict

