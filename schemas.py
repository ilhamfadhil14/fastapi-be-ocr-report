from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OCRReportCreate(BaseModel):
    file_name: Optional[str]
    total_page: Optional[str]
    model_name: Optional[str]
    temperature: Optional[float]
    date_time: Optional[datetime]
    running_time: Optional[float]
    input_token: Optional[int]
    output_token: Optional[int]
    total_token: Optional[int]
    report_batch: Optional[str]
    total_corrent: Optional[int]
    total_predicted: Optional[int]
    number_pages: Optional[int]
    page_success: Optional[int]
