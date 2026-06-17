# 🤖 Kiểm Thử Tự Động với Selenium

> **Môn học:** Kiểm thử phần mềm  
> **Sinh viên:** [Họ và tên của bạn]  
> **MSSV:** [Mã số sinh viên]  
> **Nhóm:** Nhóm 6 – COUR01.LT2  
> **Trường:** Đại học Phenikaa  

---

## 📌 Mục tiêu

- Học cách sử dụng **Selenium WebDriver** để kiểm thử tự động
- Xây dựng 3 test case tự động cho website thực tế
- Chạy và xác nhận kết quả kiểm thử

---

## 🌐 Website được kiểm thử

**DemoQA** – `https://demoqa.com`

DemoQA là website thực hành kiểm thử tự động, cung cấp các thành phần UI phổ biến như form, bảng, checkbox, dialog... Rất phù hợp để học Selenium.

---

## ⚙️ Cài đặt môi trường

### Yêu cầu
- Python 3.8+
- Google Chrome (phiên bản mới nhất)
- ChromeDriver (tương ứng với phiên bản Chrome)

### Bước 1: Cài đặt Python
Tải tại [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Kiểm tra: mở CMD → `python --version`

### Bước 2: Cài đặt thư viện Selenium
```bash
pip install selenium
pip install webdriver-manager
```

### Bước 3: Cài ChromeDriver tự động (khuyên dùng)
Thêm vào đầu file Python:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

### Bước 4: Chạy test
```bash
python -m pytest test_selenium.py -v
# hoặc
python test_selenium.py
```

---

## 📋 Các Test Case Thực Hiện

---

### Test Case 1 – Kiểm thử điền Form (Text Box)

| Thông tin | Chi tiết |
|-----------|---------|
| **Mã TC** | TC1 |
| **Tên** | Kiểm thử điền thông tin vào Text Box Form |
| **URL** | `https://demoqa.com/text-box` |
| **Mục tiêu** | Xác nhận form nhận đúng dữ liệu và hiển thị kết quả |

**Các bước thực hiện:**
1. Mở trình duyệt, truy cập `https://demoqa.com/text-box`
2. Nhập **Full Name:** `Nguyen Van A`
3. Nhập **Email:** `nguyenvana@phenikaa.edu.vn`
4. Nhập **Current Address:** `Ha Noi, Viet Nam`
5. Nhập **Permanent Address:** `Ho Chi Minh, Viet Nam`
6. Click nút **Submit**
7. Kiểm tra kết quả hiển thị bên dưới

**Kết quả mong đợi:**
- Phần output hiển thị đúng tên và email vừa nhập
- Không có thông báo lỗi

**Kết quả thực tế:** ✅ PASS

**📸 Ảnh minh hoạ:**

![TC1 - Text Box Form](./screenshots/tc1_textbox.png)

---

### Test Case 2 – Kiểm thử Check Box

| Thông tin | Chi tiết |
|-----------|---------|
| **Mã TC** | TC2 |
| **Tên** | Kiểm thử chức năng tích chọn Check Box |
| **URL** | `https://demoqa.com/checkbox` |
| **Mục tiêu** | Xác nhận việc chọn checkbox cập nhật đúng kết quả |

**Các bước thực hiện:**
1. Mở trình duyệt, truy cập `https://demoqa.com/checkbox`
2. Click nút **Expand All** (mở rộng toàn bộ cây thư mục)
3. Tích chọn checkbox **"Documents"**
4. Kiểm tra phần kết quả bên dưới

**Kết quả mong đợi:**
- Phần kết quả hiển thị: `You have selected: documents`
- Các mục con của Documents cũng được chọn theo

**Kết quả thực tế:** ✅ PASS

**📸 Ảnh minh hoạ:**

![TC2 - Check Box](./screenshots/tc2_checkbox.png)

---

### Test Case 3 – Kiểm thử Web Tables (Thêm bản ghi)

| Thông tin | Chi tiết |
|-----------|---------|
| **Mã TC** | TC3 |
| **Tên** | Kiểm thử thêm bản ghi mới vào bảng dữ liệu |
| **URL** | `https://demoqa.com/webtables` |
| **Mục tiêu** | Xác nhận thêm dữ liệu mới hiển thị đúng trong bảng |

**Các bước thực hiện:**
1. Mở trình duyệt, truy cập `https://demoqa.com/webtables`
2. Click nút **"Add"**
3. Điền thông tin vào form:
   - First Name: `Tran`
   - Last Name: `Thi B`
   - Email: `tranthib@test.com`
   - Age: `22`
   - Salary: `5000`
   - Department: `QA Testing`
4. Click nút **Submit**
5. Kiểm tra bảng hiển thị bản ghi mới

**Kết quả mong đợi:**
- Bảng xuất hiện hàng mới với tên `Tran Thi B`
- Cột Department hiển thị `QA Testing`

**Kết quả thực tế:** ✅ PASS

**📸 Ảnh minh hoạ:**

![TC3 - Web Tables](./screenshots/tc3_webtables.png)

---

## 📊 Tổng Hợp Kết Quả

| STT | Mã TC | Tên Test Case | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
|-----|-------|---------------|------------------|-----------------|------------|
| 1 | TC1 | Điền Text Box Form | Hiển thị đúng dữ liệu nhập | Hiển thị đúng | ✅ PASS |
| 2 | TC2 | Tích chọn Check Box | Kết quả cập nhật đúng | Cập nhật đúng | ✅ PASS |
| 3 | TC3 | Thêm bản ghi Web Table | Bản ghi mới xuất hiện | Xuất hiện đúng | ✅ PASS |

**📸 Ảnh kết quả chạy pytest:**

![Kết quả pytest](./screenshots/pytest_result.png)

---

## 📁 Cấu trúc Repository

```
selenium-testing/
│
├── README.md               # Báo cáo chính (file này)
├── test_selenium.py        # File code Selenium
├── requirements.txt        # Danh sách thư viện
└── screenshots/
    ├── tc1_textbox.png
    ├── tc2_checkbox.png
    ├── tc3_webtables.png
    └── pytest_result.png
```

**File requirements.txt:**
```
selenium==4.18.1
webdriver-manager==4.0.1
pytest==8.0.0
```

---

## 🚀 Hướng Dẫn Chạy Lại

```bash
# 1. Clone repo
git clone https://github.com/[username]/selenium-testing.git
cd selenium-testing

# 2. Cài thư viện
pip install -r requirements.txt

# 3. Chạy toàn bộ test
python -m pytest test_selenium.py -v

# 4. Chạy 1 test cụ thể
python -m pytest test_selenium.py::DemoQATests::test_TC1_text_box_form -v
```

---

## 📚 Tài Liệu Tham Khảo

- 📖 [Tài liệu chính thức Selenium](https://www.selenium.dev/documentation/)
- 🌐 [DemoQA – Website thực hành](https://demoqa.com/)
- 📘 [Selenium với Python](https://selenium-python.readthedocs.io/)
- 🎬 [Video hướng dẫn Selenium](https://www.youtube.com/results?search_query=selenium+python+tutorial+tieng+viet)

---

*Báo cáo được thực hiện bởi Nhóm 6 – COUR01.LT2 – Đại học Phenikaa*
