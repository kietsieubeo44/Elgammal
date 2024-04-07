# Sử dụng image python làm base
FROM python:3.9

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy các file requirements.txt vào container
COPY requirements.txt /app/

# Cài đặt các dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . /app/

# Mở cổng 5000 để truy cập ứng dụng
EXPOSE 5000

# Khởi chạy ứng dụng Flask
CMD ["python", "app.py"]
