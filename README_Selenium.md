# Selenium Testing Assignment

## 1. Thông tin sinh viên

* Họ tên: Dương Trung Kiên
* MSSV: 22010037

---

## 2. Mục tiêu

Tìm hiểu công cụ kiểm thử tự động Selenium và xây dựng các test case kiểm thử website.

Website được chọn:

https://demoqa.com

Ngôn ngữ sử dụng:

* Python
* Selenium WebDriver
* Pytest

---

## 3. Cài đặt môi trường

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

Chạy kiểm thử:

```bash
python -m pytest test_selenium.py -v
```

---

## 4. Các Test Case

### TC1 – Text Box

Mục tiêu:

* Kiểm tra chức năng nhập dữ liệu biểu mẫu.

Các bước:

1. Truy cập Text Box.
2. Nhập họ tên.
3. Nhập email.
4. Nhập địa chỉ.
5. Nhấn Submit.
6. Kiểm tra kết quả hiển thị.

Kết quả mong đợi:

* Dữ liệu hiển thị chính xác sau khi Submit.

---

### TC2 – Check Box

Mục tiêu:

* Kiểm tra chức năng chọn Check Box.

Các bước:

1. Truy cập Check Box.
2. Chọn Home.
3. Kiểm tra vùng Result.

Kết quả mong đợi:

* Hệ thống hiển thị kết quả tương ứng với lựa chọn.

---

### TC3 – Web Tables

Mục tiêu:

* Kiểm tra chức năng thêm dữ liệu vào bảng.

Các bước:

1. Truy cập Web Tables.
2. Chọn Add.
3. Nhập thông tin nhân viên.
4. Submit.

Kết quả mong đợi:

* Bản ghi mới xuất hiện trong bảng.

---

## 5. Kết quả thực hiện

| Test Case | Trạng thái |
| --------- | ---------- |
| TC1       | PASS       |
| TC2       | PASS       |
| TC3       | PASS       |
<img width="1797" height="907" alt="Screenshot 2026-06-17 174346" src="https://github.com/user-attachments/assets/fa73ce54-cba3-4399-8c12-71fe4fa64ffd" />



## 6. Kết luận

Selenium hỗ trợ tự động hóa thao tác trên trình duyệt hiệu quả. Qua bài thực hành đã xây dựng được ba test case cơ bản gồm nhập biểu mẫu, chọn checkbox và thao tác với bảng dữ liệu.
