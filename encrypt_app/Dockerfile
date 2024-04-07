# Sử dụng image chính thức của Python
FROM python:3.11
# Thiết lập thư mục làm việc
WORKDIR /usr/src/app

# Sao chép mã và tệp yêu cầu vào thư mục làm việc trong image Docker
COPY . .

# Cài đặt các gói phụ thuộc
RUN pip install Flask cryptography

# Mở cổng mặc định cho ứng dụng Flask
EXPOSE 5000

# Chạy ứng dụng khi container được khởi chạy
CMD ["python", "app.py"]
