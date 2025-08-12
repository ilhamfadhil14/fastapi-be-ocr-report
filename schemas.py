from pydantic import BaseModel
from typing import Optional
from datetime import date

class OCRReportCreate(BaseModel):
    file_name: Optional[str]
    total_page: Optional[str]
    model_name: Optional[str]
    temperature: Optional[float]
    date_time: Optional[date]
    running_time: Optional[date]
    input_token: Optional[int]
    output_token: Optional[int]
    total_token: Optional[int]
    report_batch: Optional[str]
    total_corrent: Optional[int]
    total_predicted: Optional[int]
    number_pages: Optional[int]
    page_success: Optional[int]
