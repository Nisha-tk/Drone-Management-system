import enum

class DroneStatus(enum.Enum):
    AVAILABLE = "AVAILABLE"
    IN_MISSION = "IN_MISSION"
    MAINTENANCE = "MAINTENANCE"