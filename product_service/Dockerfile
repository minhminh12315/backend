# Sử dụng image Python 3.12 slim
FROM python:3.12-slim

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt system dependencies cho PostgreSQL và MySQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
        libmariadb-dev \
        pkg-config \
        netcat-traditional \
        libffi-dev \
        libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt phụ thuộc Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary gunicorn

# Sao chép dự án
COPY . /app/

# Thu thập static files
RUN python manage.py collectstatic --noinput --clear || true

# Tạo thư mục media
RUN mkdir -p /app/media/variant_images

# Tạo người dùng non-root
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Mở port
EXPOSE 8001
