FROM python:3.9
WORKDIR /app
COPY Text_Date_Time.py /app/Text_Date_Time.py
CMD ["python", "/app/Text_Date_Time.py"]
