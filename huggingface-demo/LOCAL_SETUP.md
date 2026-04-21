# Hướng dẫn chạy Demo trên Local

## Yêu cầu hệ thống

- Python 3.8 trở lên
- pip (Python package manager)
- Git (để clone repository)

## Các bước thực hiện

### 1. Clone repository (nếu chưa có)

```bash
git clone <repository-url>
cd huggingface-demo
```

### 2. Tạo môi trường ảo (khuyến nghị)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Kiểm tra cấu trúc thư mục

Đảm bảo các thư mục sau tồn tại:
- `model/` - chứa file model đã train
- `examples/` - chứa ảnh mẫu để test

### 5. Chạy ứng dụng

```bash
python app.py
```

### 6. Truy cập ứng dụng

Sau khi chạy thành công, mở trình duyệt và truy cập:
```
http://localhost:7860
```

Gradio sẽ tự động mở trình duyệt với giao diện demo.

## Sử dụng

1. Upload ảnh ngôn ngữ ký hiệu hoặc chọn từ examples
2. Nhấn Submit để phân loại
3. Xem kết quả dự đoán với confidence score

## Xử lý lỗi thường gặp

### Lỗi: Module not found
```bash
pip install --upgrade -r requirements.txt
```

### Lỗi: Port 7860 đã được sử dụng
Thay đổi port trong file `app.py`:
```python
demo.launch(server_port=7861)
```

### Lỗi: Model không tìm thấy
Kiểm tra đường dẫn model trong `app.py` và đảm bảo file model tồn tại trong thư mục `model/`

## Tắt ứng dụng

Nhấn `Ctrl + C` trong terminal để dừng server.
