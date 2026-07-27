# Bảo mật MQTT bằng Mosquitto và Paho Python (Đề tài 12 - Hướng B)

* **Học phần:** Bảo mật IoT (INT4410)
* **Sinh viên thực hiện:** Mai Thị Thảo Vy
* **Mã số sinh viên:** 231A010112
* **Giảng viên hướng dẫn:** Hồ Nhựt Minh

---

## 1. Giới thiệu đề tài
Đề tài tập trung nghiên cứu, xây dựng và triển khai các cơ chế bảo mật cốt lõi cho giao thức truyền thông MQTT trong hệ thống Internet of Things (IoT). Hệ thống sử dụng phần mềm mã nguồn mở **Eclipse Mosquitto Broker** kết hợp với thư viện lập trình **Eclipse Paho MQTT Python** nhằm thiết lập lớp bảo mật xác thực danh tính (Authentication bằng Username/Password) và kiểm soát quyền hạn truy cập Topic nghiêm ngặt theo nguyên tắc đặc quyền tối thiểu (Authorization bằng ACL).

---

## 2. Cấu trúc Thư mục Kho lưu trữ (Repository)
Kho lưu trữ được tổ chức theo đúng chuẩn cấu trúc phục vụ nghiên cứu và kiểm thử thực nghiệm:

```text
MaiThiThaoVy_BaomatMQTTbangMosquittovaPahoPython/
│
├── README.md               # Hướng dẫn cài đặt, cấu trúc và cách sử dụng hệ thống
├── report/                 # Thư mục chứa báo cáo tiểu luận (.docx và .pdf)
├── slides/                 # Thư mục chứa file slide thuyết trình bảo vệ đề tài
├── src/                    # Thư mục mã nguồn Python
│   ├── mqtt_pub.py         # Script Publisher giả lập cảm biến phát gói tin JSON
│   └── mqtt_sub.py         # Script Subscriber lắng nghe thông điệp và tự động ghi log
├── configs/                # Thư mục chứa các tệp cấu hình bảo mật hệ thống
│   ├── mosquitto.conf      # Tệp cấu hình chính của Mosquitto Broker
│   ├── aclfile.txt         # Tệp danh sách điều khiển truy cập (ACL)
│   └── password.txt.example# Mẫu định dạng tệp mật khẩu tài khoản đã mã hóa hash
├── data/                   # Thư mục dữ liệu mẫu
│   └── payload_sample.json # Tệp cấu trúc JSON mẫu truyền nhận dữ liệu cảm biến
└── results/                # Thư mục kết quả thực nghiệm và minh chứng
    ├── logs/               # Tệp nhật ký hoạt động (mqtt_log.txt)
    └── screenshots/        # Thư mục chứa ảnh chụp màn hình kiểm thử kịch bản TC-01 đến TC-06
```
---
## 3. Hướng dẫn Cài đặt và Triển khai Hệ thống

Bước 1: Cài đặt và cấu hình Mosquitto Broker
Cài đặt Eclipse Mosquitto trên hệ điều hành Windows.
Cấu hình tệp mosquitto.conf (đặt tại thư mục cài đặt Mosquitto hoặc sử dụng từ thư mục configs/):
      listener 1883
      allow_anonymous false
      password_file "C:\Program Files\Mosquitto\password.txt"
      acl_file "C:\Program Files\Mosquitto\aclfile.txt"
Khởi động Mosquitto Broker kèm tệp cấu hình ở chế độ dòng lệnh:
      cd "C:\Program Files\Mosquitto"
      mosquitto -c mosquitto.conf -v
Bước 2: Cài đặt thư viện Python
Đảm bảo máy tính đã cài đặt Python, sau đó cài đặt thư viện Paho MQTT chính thức:
    pip install paho-mqtt
Bước 3: Chạy chương trình kiểm thử
Khởi chạy Subscriber (Lắng nghe dữ liệu và ghi log):
    python src/mqtt_sub.py
    
---
## 4. Kết quả và Minh chứng Kiểm thử

Hệ thống đã vượt qua thành công toàn bộ các kịch bản kiểm thử bảo mật (TC-01 đến TC-06):

Xác thực hợp lệ/không hợp lệ: Chặn tuyệt đối các kết nối ẩn danh hoặc sai thông tin đăng nhập.
Phân quyền ACL: Ngăn chặn các hành vi cố tình Publish hoặc Subscribe trái phép trên kênh định danh iot/sensor/temp.
Ghi log tự động: Lưu trữ toàn bộ thông điệp dữ liệu cảm biến định dạng JSON vào tệp nhật ký results/logs/mqtt_log.txt.

---
