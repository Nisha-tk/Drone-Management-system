
from src.routers.auth_router import auth_router
from src.routers.drone_router import drone_router
from src.routers.survey_area import survey_area_router
from src.routers.mission_router import mission_router
from src.routers.flight_path import flight_router
from src.routers.mission_report import report_router
from fastapi import FastAPI
from src.exceptions.register import register_exception_handlers
app = FastAPI(title="drone-Management-system")

app.include_router(auth_router)
app.include_router(survey_area_router)
app.include_router(drone_router)
app.include_router(flight_router)
app.include_router(report_router)
app.include_router(mission_router)
register_exception_handlers(app)




