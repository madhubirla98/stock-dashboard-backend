from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from app.utils.auth import verify_token
from app.services.stock_service import StockService

router = APIRouter()

class StockRequest(BaseModel):
    tickers: list[str]
    start_date: str
    end_date: str
    timeframe: str

@router.post("/stocks")
def get_stocks(payload: StockRequest, request: Request):
    try:
        verify_token(request)
        # Just pass the list as-is now
        data = StockService.fetch_stock_data(payload.tickers, payload.start_date, payload.end_date, payload.timeframe)
        return {"data": data}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
