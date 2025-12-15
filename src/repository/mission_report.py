from sqlalchemy.orm import Session
from src.models.mission_report import MissionReports

class MissionReportRepository:

    @staticmethod
    def create(db: Session, report: MissionReports) -> MissionReports:
        db.add(report)
        db.commit()
        db.refresh(report)
        return report

    @staticmethod
    def get_by_mission(db: Session, mission_id):
        return (
            db.query(MissionReports)
            .filter(MissionReports.mission_id == mission_id)
            .first()
        )
