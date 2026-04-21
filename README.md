# Phân loại Ngôn ngữ Ký hiệu Việt Nam (Vietnamese Sign Language Classification)

Dự án phân loại 25 ký hiệu chữ cái trong ngôn ngữ ký hiệu Việt Nam sử dụng Deep Learning và Transfer Learning với các kiến trúc CNN tiên tiến (VGG16, ResNet50, MobileNet).

<div align="center">
  <img src="reports/figures/samples_data.png" width="90%">
  <p><i>Mẫu ảnh trong bộ dữ liệu Vietnamese Sign Language</i></p>
</div>

## 🎯 Tổng quan

Dự án này xây dựng và so sánh 3 mô hình phân loại ký hiệu ngôn ngữ ký hiệu Việt Nam sử dụng kỹ thuật Transfer Learning, đạt độ chính xác lên đến **99.00%** trên tập test. Ngoài ra, dự án còn bao gồm ứng dụng demo web sử dụng Gradio để triển khai mô hình.

## 📊 Bộ dữ liệu

- **Nguồn**: [Kaggle - Vietnamese Sign Language Dataset](https://www.kaggle.com/datasets/mcphngnga/dataset-vsl/data)
- **Tổng số ảnh**: 25,000 ảnh (sau khi xử lý trùng lặp)
- **Số lớp**: 25 ký hiệu (A, AA, B, C, D, DD, E, G, H, I, K, L, M, N, O, OOO, P, Q, R, S, T, U, V, X, Y)
- **Kích thước ảnh**: 224x224 pixels
- **Định dạng**: PNG

**Phân chia dữ liệu:**
- Train: 20,000 ảnh (80%)
- Validation: 2,496 ảnh (10%)
- Test: 2,504 ảnh (10%)

**Xử lý dữ liệu:**
- Loại bỏ class AAA do trùng lặp với class AA
- Lưu trữ dưới dạng TFRecord với nén GZIP (tiết kiệm ~97.8% dung lượng: 14GB → 313MB)

## 🏆 Kết quả các mô hình

| Mô hình       | Test Accuracy | Test Loss | Val Accuracy | Số Parameters | Kích thước | Thời gian huấn luyện |
| ------------- | ------------- | --------- | ------------ | ------------- | ---------- | -------------------- |
| **VGG16**     | **99.00%**    | 0.0678    | 99.00%       | 27.6M         | 105 MB     | ~60 phút             |
| **ResNet50**  | **98.96%**    | 0.0402    | 98.48%       | ~25M          | ~98 MB     | ~35 phút             |
| **MobileNet** | **98.80%**    | 0.0519    | 98.68%       | ~4.2M         | ~16 MB     | ~15 phút             |

**Phân tích:**
- **VGG16**: Độ chính xác cao nhất (99.00%) nhưng tốn nhiều tài nguyên
- **ResNet50**: Loss thấp nhất (0.0402), cân bằng tốt giữa hiệu suất và tốc độ
- **MobileNet**: Nhẹ nhất (4.2M params), phù hợp cho triển khai trên thiết bị di động và web

## 🚀 Demo ứng dụng

### Web Demo với Gradio

Dự án bao gồm ứng dụng web demo sử dụng Gradio để phân loại ký hiệu ngôn ngữ ký hiệu Việt Nam trong thời gian thực.

**Chạy demo trên local:**

```bash
cd huggingface-demo
pip install -r requirements.txt
python app.py
```

Truy cập `http://localhost:7860` để sử dụng demo.

**Tính năng:**
- Upload ảnh hoặc chọn từ ảnh mẫu
- Dự đoán ký hiệu với confidence score
- Hiển thị top 5 dự đoán có xác suất cao nhất
- Sử dụng mô hình MobileNet để inference nhanh

Xem thêm hướng dẫn chi tiết tại [huggingface-demo/LOCAL_SETUP.md](huggingface-demo/LOCAL_SETUP.md) và [huggingface-demo/DEPLOY.md](huggingface-demo/DEPLOY.md).

## 📁 Cấu trúc thư mục

```
Classification-of-Vietnamese-Sign-Language/
├── notebooks/                  # Jupyter notebooks
│   ├── VLS_preprocessing.ipynb            # Tiền xử lý và chia dữ liệu
│   ├── VLS_EDA.ipynb                      # Khám phá và trực quan hóa dữ liệu
│   ├── data_visualization.ipynb           # Trực quan hóa dữ liệu
│   ├── transfer_learning_resnet50.ipynb   # Huấn luyện ResNet50
│   ├── transfer_learning_vgg16.ipynb      # Huấn luyện VGG16
│   └── transfer_learning_mobilenet.ipynb  # Huấn luyện MobileNet
├── huggingface-demo/           # Ứng dụng demo web với Gradio
│   ├── app.py                 # Gradio app chính
│   ├── model/                 # Thư mục chứa model MobileNet
│   ├── examples/              # Ảnh mẫu để test
│   ├── requirements.txt       # Dependencies cho demo
│   ├── LOCAL_SETUP.md         # Hướng dẫn chạy local
│   └── DEPLOY.md              # Hướng dẫn deploy lên Hugging Face
├── models/                     # Mô hình đã huấn luyện (lưu trên Drive)
│   └── Link (do cac files kha nang).txt
├── reports/                    # Báo cáo và tài liệu
│   └── figures/               # Hình ảnh và biểu đồ
└── README.md
```

## 🛠️ Phương pháp huấn luyện

### Chiến lược 2 giai đoạn

Tất cả các mô hình đều sử dụng chiến lược huấn luyện 2 giai đoạn:

**Giai đoạn 1 - Warmup (5 epochs):**
- Đóng băng base model (pretrained trên ImageNet)
- Chỉ huấn luyện lớp phân loại
- Adam optimizer với learning rate warmup (0.0003 → 0.001)

**Giai đoạn 2 - Fine-tuning (10 epochs):**
- Mở băng toàn bộ mô hình
- SGD optimizer với momentum 0.9
- Learning rate: 1e-5
- Callbacks: EarlyStopping, ReduceLROnPlateau

### Kỹ thuật được sử dụng

- **Transfer Learning**: Sử dụng mô hình pretrained trên ImageNet
- **Data Augmentation**: 
  - Random horizontal flip
  - Random brightness adjustment (±20%)
  - Random contrast adjustment (0.8-1.2)
- **Callbacks**:
  - Learning Rate Scheduler (Warmup)
  - Early Stopping (patience=3)
  - ReduceLROnPlateau (factor=0.5, patience=2)
- **Optimization**:
  - Adam optimizer (giai đoạn warmup)
  - SGD với momentum (giai đoạn fine-tuning)

## 📈 Kết quả chi tiết

### Biểu đồ huấn luyện

#### VGG16 - Accuracy: 99.00%

<div align="center">
  <img src="reports/figures/vgg16_acc_loss.png" width="90%">
  <p><i>Quá trình huấn luyện VGG16: Đạt validation accuracy 99.00% sau 15 epochs</i></p>
</div>

#### ResNet50 - Accuracy: 98.96%

<div align="center">
  <img src="reports/figures/resnet50_acc_loss.png" width="90%">
  <p><i>Quá trình huấn luyện ResNet50: Loss thấp nhất (0.0402) với huấn luyện ổn định</i></p>
</div>

#### MobileNet - Accuracy: 98.80%

<div align="center">
  <img src="reports/figures/mobilenet_acc_loss.png" width="90%">
  <p><i>Quá trình huấn luyện MobileNet: Nhanh nhất với 4.2M parameters</i></p>
</div>

### Chi tiết từng mô hình

#### 1. VGG16
- **Test Accuracy**: 99.00%
- **Test Loss**: 0.0678
- **Kiến trúc**: VGG16 pretrained trên ImageNet
- **Đặc điểm**: Kiến trúc đơn giản, nhiều tham số, độ chính xác cao nhất

#### 2. ResNet50
- **Test Accuracy**: 98.96%
- **Test Loss**: 0.0402
- **Kiến trúc**: ResNet50 pretrained trên ImageNet với skip connections
- **Đặc điểm**: Loss thấp nhất, huấn luyện ổn định nhờ residual connections

#### 3. MobileNet
- **Test Accuracy**: 98.80%
- **Test Loss**: 0.0519
- **Kiến trúc**: MobileNetV1 với depthwise separable convolutions
- **Đặc điểm**: Nhẹ nhất (4.2M params), tốc độ inference nhanh, được sử dụng trong demo app

## 💻 Yêu cầu hệ thống

### Thư viện Python

```
tensorflow>=2.10.0
numpy>=1.21.0
matplotlib>=3.5.0
pandas>=1.3.0
scikit-learn>=1.0.0
gradio  # Cho demo app
pillow  # Cho xử lý ảnh
```

### Môi trường

- Python 3.8+
- Google Colab (khuyến nghị cho GPU khi huấn luyện)
- Google Drive (để lưu trữ dữ liệu và mô hình)

## 📖 Hướng dẫn sử dụng

### 1. Chuẩn bị dữ liệu

```python
# Chạy notebook VLS_preprocessing.ipynb
# Notebook này sẽ:
# - Tải dữ liệu từ Kaggle
# - Xử lý dữ liệu trùng lặp (loại bỏ class AAA)
# - Chia dữ liệu thành train/val/test (80/10/10)
# - Lưu dữ liệu dưới dạng TFRecord (nén GZIP)
```

### 2. Khám phá dữ liệu (EDA)

```python
# Chạy notebook VLS_EDA.ipynb hoặc data_visualization.ipynb
# Xem phân bố dữ liệu, kích thước ảnh, và mẫu ảnh
```

### 3. Huấn luyện mô hình

Chọn một trong các notebook tùy theo mô hình muốn huấn luyện:

```python
# VGG16 - Độ chính xác cao nhất (99.00%)
# Chạy notebook: transfer_learning_vgg16.ipynb

# ResNet50 - Cân bằng tốt (98.96%)
# Chạy notebook: transfer_learning_resnet50.ipynb

# MobileNet - Nhẹ nhất cho mobile (98.80%)
# Chạy notebook: transfer_learning_mobilenet.ipynb
```

### 4. Chạy Demo App

```bash
# Di chuyển vào thư mục demo
cd huggingface-demo

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python app.py

# Truy cập http://localhost:7860
```

### 5. Đánh giá và dự đoán

```python
import tensorflow as tf
import numpy as np

# Load mô hình (chọn một trong ba)
model = tf.keras.models.load_model('path/to/model.keras')

# Dự đoán
predictions = model.predict(preprocessed_images)
predicted_class = class_names[np.argmax(predictions[0])]
```

## 🔧 Tiền xử lý dữ liệu

### Xử lý dữ liệu trùng lặp

- Loại bỏ class **AAA** do trùng lặp với class **AA**
- Giảm từ 26 classes xuống 25 classes
- Đảm bảo tính nhất quán của dữ liệu

### Lưu trữ tối ưu

Dữ liệu được lưu dưới dạng **TFRecord** với nén GZIP:

- Dung lượng gốc (dataset.save()): ~14 GB
- Dung lượng sau nén (TFRecord + GZIP): ~313 MB
- **Tiết kiệm**: ~97.8%

### Data Augmentation

- Random horizontal flip
- Random brightness adjustment (±20%)
- Random contrast adjustment (0.8-1.2)

## 🌐 Triển khai

### Deploy lên Hugging Face Spaces

Dự án có thể được deploy lên Hugging Face Spaces để tạo demo công khai:

```bash
# Clone space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-sign-language
cd vietnamese-sign-language

# Copy files
cp -r huggingface-demo/* .

# Push to Hugging Face
git add .
git commit -m "Deploy Vietnamese Sign Language Classification"
git push
```

Xem hướng dẫn chi tiết tại [huggingface-demo/DEPLOY.md](huggingface-demo/DEPLOY.md).

## 📊 So sánh và lựa chọn mô hình

| Tiêu chí                  | VGG16      | ResNet50   | MobileNet  |
| ------------------------- | ---------- | ---------- | ---------- |
| **Độ chính xác**          | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐   |
| **Tốc độ inference**      | ⭐⭐       | ⭐⭐⭐     | ⭐⭐⭐⭐⭐ |
| **Kích thước mô hình**    | ⭐⭐       | ⭐⭐⭐     | ⭐⭐⭐⭐⭐ |
| **Phù hợp cho mobile**    | ❌         | ⚠️         | ✅         |
| **Phù hợp cho production**| ⚠️         | ✅         | ✅         |

**Khuyến nghị:**
- **VGG16**: Sử dụng khi cần độ chính xác tối đa và có đủ tài nguyên
- **ResNet50**: Lựa chọn cân bằng cho hầu hết các ứng dụng
- **MobileNet**: Tốt nhất cho ứng dụng mobile, web, và edge devices

## 👥 Tác giả

**NTTU - Nguyễn Xuân Tiến & Đồng Nguyễn Xuân An**

Trường Đại học Nguyễn Tất Thành  
Học kỳ 2 - Năm học 2025-2026  
Môn: Trí tuệ nhân tạo 2

## 📚 Tài liệu tham khảo

1. He, K., Zhang, X., Ren, S., & Sun, J. (2016). **Deep residual learning for image recognition**. CVPR.
2. Simonyan, K., & Zisserman, A. (2014). **Very deep convolutional networks for large-scale image recognition**. ICLR.
3. Howard, A. G., et al. (2017). **MobileNets: Efficient convolutional neural networks for mobile vision applications**. arXiv.
4. [Vietnamese Sign Language Dataset - Kaggle](https://www.kaggle.com/datasets/mcphngnga/dataset-vsl/data)
5. TensorFlow Documentation - Transfer Learning Guide
6. Gradio Documentation - Building ML Web Apps

## 📝 License

Dự án này được sử dụng cho mục đích học tập và nghiên cứu.

## 🔗 Liên kết hữu ích

- **Dataset**: [Kaggle - Vietnamese Sign Language](https://www.kaggle.com/datasets/mcphngnga/dataset-vsl/data)
- **Models**: [Google Drive](https://drive.google.com/drive/folders/1EAddrr6MtpKt4HXUfzcsBy4Sh8uj3wHb) (VGG16, ResNet50, MobileNet)
- **Demo App**: Xem thư mục [huggingface-demo/](huggingface-demo/)

---

**Lưu ý**: Các mô hình đã huấn luyện được lưu trữ trên Google Drive do kích thước lớn. Xem file [models/Link (do cac files kha nang).txt](models/Link%20(do%20cac%20files%20kha%20nang).txt) để truy cập.
