from fastapi import APIRouter
from services.market import get_market_insights

router = APIRouter(prefix="/insights", tags=["Insights"])

@router.get("/")
def insights():
    return get_market_insights()
