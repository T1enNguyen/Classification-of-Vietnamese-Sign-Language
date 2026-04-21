# Hướng dẫn Deploy lên Hugging Face Spaces

## Cách 1: Qua Web UI (Đơn giản nhất)

1. Truy cập https://huggingface.co/spaces
2. Click "Create new Space"
3. Điền thông tin:
   - Space name: `vietnamese-sign-language`
   - License: `mit`
   - SDK: `Gradio`
   - Hardware: `CPU basic` (miễn phí)
4. Click "Create Space"
5. Upload các files:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitattributes`
   - Thư mục `model/` (chứa file mobilenet_vsl.keras)
   - Thư mục `examples/` (chứa các ảnh mẫu)

**Lưu ý**: File model (221MB) cần dùng Git LFS. Hugging Face sẽ tự động xử lý khi bạn upload qua web.

## Cách 2: Qua Git (Nâng cao)

```bash
# 1. Cài đặt Git LFS
git lfs install

# 2. Clone space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-sign-language
cd vietnamese-sign-language

# 3. Copy files vào
cp ../huggingface-demo/* .

# 4. Add và commit
git add .
git commit -m "Initial commit: Vietnamese Sign Language Classification"

# 5. Push lên Hugging Face
git push
```

## Sau khi deploy

- Space sẽ tự động build (mất 2-5 phút)
- Bạn sẽ có URL dạng: `https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-sign-language`
- Demo sẽ chạy 24/7 miễn phí trên CPU của Hugging Face

## Troubleshooting

Nếu gặp lỗi khi upload file model lớn:
1. Đảm bảo file `.gitattributes` có dòng: `*.keras filter=lfs diff=lfs merge=lfs -text`
2. Hoặc upload qua web UI thay vì Git CLI
