# Mai Thị Thảo Vy - Bảo mật MQTT bằng Mosquitto và Paho Python

## 1. Giới thiệu đề tài

Đề tài triển khai hệ thống MQTT bảo mật sử dụng Eclipse Mosquitto làm MQTT Broker và Eclipse Paho MQTT Python để xây dựng chương trình Publisher/Subscriber.

Mục tiêu của hệ thống:
- Triển khai MQTT Broker cục bộ bằng Mosquitto.
- Xây dựng MQTT Publisher và Subscriber bằng Python.
- Thiết lập xác thực Username/Password.
- Cấu hình phân quyền truy cập Topic bằng ACL.
- Kiểm thử kết nối hợp lệ và không hợp lệ.


## 2. Kiến trúc hệ thống

Mô hình gồm 3 thành phần:

- Publisher (`mqtt_pub.py`)
  - User: sensor
  - Chức năng: gửi dữ liệu cảm biến
  - Quyền: Publish Topic

- MQTT Broker (Mosquitto)
  - Host: localhost
  - Port: 1883
  - Chức năng: xác thực, kiểm tra ACL và chuyển tiếp dữ liệu

- Subscriber (`mqtt_sub.py`)
  - User: dashboard
  - Chức năng: nhận dữ liệu cảm biến
  - Quyền: Subscribe Topic


## 3. Cấu hình bảo mật MQTT

Hệ thống sử dụng hai cơ chế bảo mật:

### Authentication

Xác thực người dùng bằng Username/Password thông qua Mosquitto Broker.

### Authorization

Phân quyền truy cập bằng ACL (Access Control List).

Quyền truy cập:

| User | Topic | Quyền |
|---|---|---|
| sensor | iot/sensor/temp | Publish |
| dashboard | iot/sensor/temp | Subscribe |


## 4. Cấu trúc thư mục
MaiThiThaoVy_BaomatMQTTbangMosquittovaPahoPython

├── configs
│ ├── mosquitto.conf
│ ├── aclfile.txt
│ └── password.txt.example
│
├── data
│ └── payload_sample.json
│
├── results
│ ├── logs
│ └── screenshots
│
├── src
│ ├── mqtt_pub.py
│ └── mqtt_sub.py
│
├── references
│ └── link_nguon.md
│
└── requirements.txt


## 5. Cài đặt môi trường

Cài đặt thư viện Python:

```bash
pip install -r requirements.txt

Yêu cầu môi trường:
Windows 11
Eclipse Mosquitto 2.1.2
Python 3.x
Eclipse Paho MQTT Python

## 6. Chạy thử hệ thống
 ```bash
Bước 1: Khởi động MQTT Broker

Di chuyển đến thư mục cấu hình:


cd configs

Khởi động Mosquitto:

mosquitto -c mosquitto.conf -v

Broker chạy tại:

localhost:1883
Bước 2: Chạy Publisher

Mở terminal mới:

python src/mqtt_pub.py

Publisher gửi dữ liệu lên Topic:

iot/sensor/temp
Bước 3: Chạy Subscriber

Mở terminal mới:

python src/mqtt_sub.py

Subscriber nhận dữ liệu từ Topic:

iot/sensor/temp

## 7. Kiểm thử bảo mật

###Các trường hợp kiểm thử:
 ```bash
Trường hợp 1: Người dùng hợp lệ

Điều kiện:

Username/Password đúng.
Có quyền truy cập Topic.

Kết quả mong đợi:

Client kết nối thành công.
Publisher gửi dữ liệu.
Subscriber nhận dữ liệu.
Trường hợp 2: Sai Username/Password

Điều kiện:

Sử dụng tài khoản không tồn tại hoặc sai mật khẩu.

Kết quả mong đợi:

Mosquitto Broker từ chối kết nối.
Client không thể truy cập hệ thống.
Trường hợp 3: Sai quyền ACL

Điều kiện:

Người dùng không có quyền Publish hoặc Subscribe Topic.

Kết quả mong đợi:

Broker từ chối thao tác không đúng quyền.
Dữ liệu MQTT được bảo vệ theo chính sách ACL.

## 8. Lưu ý bảo mật
 ```bash
Không đưa file chứa mật khẩu thật (password.txt) lên GitHub.
File password.txt.example chỉ chứa dữ liệu mẫu.
Password thật chỉ sử dụng trong môi trường thử nghiệm cục bộ.
Dữ liệu MQTT sử dụng trong đề tài là dữ liệu cảm biến giả lập.
Hệ thống chỉ triển khai trên localhost phục vụ mục đích học tập.
Không thử nghiệm trên hệ thống IoT bên ngoài khi chưa được phép.

## 9. Tài liệu tham khảo
 ```bash
Danh sách tài liệu tham khảo được lưu tại:
references/link_nguon.md
