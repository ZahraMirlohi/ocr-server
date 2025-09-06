# پایه: Python 3.10 slim
FROM python:3.10-slim

# نصب Tesseract و زبان فارسی + کتابخانه‌های مورد نیاز
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-fas \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# تعیین مسیر کاری
WORKDIR /app

# کپی کل پروژه به داخل کانتینر
COPY . /app

# ارتقای pip و نصب پکیج‌ها
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# اجرای سرور با gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "ocr_server:app"]
