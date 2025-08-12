from sqlalchemy import Column, Integer, Text, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OCRReport(Base):
    __tablename__ = 'ocr_report'

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(Text)
    total_page = Column(Text)
    model_name = Column(Text)
    temperature = Column(Float)
    date_time = Column(Date)
    running_time = Column(Date)
    input_token = Column(Integer)
    output_token = Column(Integer)
    total_token = Column(Integer)
    report_batch = Column(Text)
    total_corrent = Column(Integer)
    total_predicted = Column(Integer)
    number_pages = Column(Integer)
    page_success = Column(Integer)
