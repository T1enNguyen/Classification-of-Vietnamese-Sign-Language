# Dự án phân loại ký hiệu ngôn ngữ ký hiệu Việt Nam

Dự án phân loại ký hiệu ngôn ngữ ký hiệu Việt Nam (Vietnamese Sign Language) sử dụng Deep Learning và Transfer Learning.


<div align="center">
  <img src="reports/figures/samples_data.png" width="90%">
  <p><i>Vài mẫu trong bộ dữ liệu VSL</i></p>
</div>

## Tổng quan

Dự án này xây dựng mô hình phân loại 25 ký hiệu chữ cái trong ngôn ngữ ký hiệu Việt Nam sử dụng các kiến trúc mạng nơ-ron tích chập (CNN) tiên tiến thông qua kỹ thuật Transfer Learning.

### Bộ dữ liệu

- **Nguồn**: [Kaggle - Vietnamese Sign Language Dataset](https://www.kaggle.com/datasets/mcphngnga/dataset-vsl/data)
- **Tổng số ảnh**: 25,000 ảnh (sau khi xử lý trùng lặp)
- **Số lớp**: 25 ký hiệu (A, AA, B, C, D, DD, E, G, H, I, K, L, M, N, O, OOO, P, Q, R, S, T, U, V, X, Y)
- **Kích thước ảnh**: 224x224 pixels
- **Định dạng**: PNG

**Phân chia dữ liệu:**

- Train: 20,000 ảnh (80%)
- Validation: 2,496 ảnh (10%)
- Test: 2,504 ảnh (10%)

### Các mô hình được triển khai

1. **ResNet50** - Đạt độ chính xác cao nhất: **98.96%**
2. **VGG16** - Mô hình baseline
3. **MobileNet** - Mô hình nhẹ cho triển khai mobile

## Cấu trúc thư mục

```
Classification-of-Vietnamese-Sign-Language/
├── notebooks/              # Jupyter notebooks
│   ├── VLS_train_val_test.ipynb           # Tiền xử lý và chia dữ liệu
│   ├── data_visualization.ipynb           # Khám phá và trực quan hóa dữ liệu
│   ├── transfer_learning_resnet50.ipynb   # Huấn luyện ResNet50
│   ├── transfer_learning_vgg16.ipynb      # Huấn luyện VGG16
│   └── transfer_learning_mobilenet.ipynb  # Huấn luyện MobileNet
├── models/                 # Mô hình đã huấn luyện (lưu trên Drive)
├── reports/                # Báo cáo và tài liệu
│   ├── figures/           # Hình ảnh và biểu đồ
│   ├── 1. Phần tổng quan về dữ liệu.md
│   ├── 2. Tiền xử lý dữ liệu.md
│   └── 3. Lý thuyết mạng ResNet50.md
└── README.md
```

## Kết quả

### ResNet50 (Mô hình tốt nhất)

- **Test Accuracy**: 98.96%
- **Test Loss**: 0.0402
- **Kiến trúc**: ResNet50 pretrained trên ImageNet
- **Phương pháp huấn luyện**: 2 giai đoạn
  - Giai đoạn 1 (Warmup): Huấn luyện lớp phân loại (5 epochs)
  - Giai đoạn 2 (Fine-tuning): Tinh chỉnh toàn bộ mô hình (10 epochs)

### Kỹ thuật được sử dụng

- **Transfer Learning**: Sử dụng mô hình pretrained trên ImageNet
- **Data Augmentation**: Random flip, brightness, contrast
- **Callbacks**:
  - Learning Rate Scheduler (Warmup)
  - Early Stopping
  - ReduceLROnPlateau
- **Optimization**:
  - Adam optimizer (giai đoạn warmup)
  - SGD với momentum (giai đoạn fine-tuning)

## Yêu cầu hệ thống

### Thư viện Python

```
tensorflow>=2.10.0
numpy>=1.21.0
matplotlib>=3.5.0
pandas>=1.3.0
scikit-learn>=1.0.0
```

### Môi trường

- Python 3.8+
- Google Colab (khuyến nghị cho GPU)
- Google Drive (để lưu trữ dữ liệu và mô hình)

## Hướng dẫn sử dụng

### 1. Chuẩn bị dữ liệu

```python
# Chạy notebook VLS_train_val_test.ipynb
# Notebook này sẽ:
# - Tải dữ liệu từ Kaggle
# - Xử lý dữ liệu trùng lặp (loại bỏ class AAA)
# - Chia dữ liệu thành train/val/test
# - Lưu dữ liệu dưới dạng TFRecord (nén GZIP)
```

### 2. Khám phá dữ liệu

```python
# Chạy notebook data_visualization.ipynb
# Xem phân bố dữ liệu, kích thước ảnh, và mẫu ảnh
```

### 3. Huấn luyện mô hình

```python
# Chạy notebook transfer_learning_resnet50.ipynb
# Hoặc các notebook khác tùy theo mô hình muốn huấn luyện
```

### 4. Đánh giá và dự đoán

Mô hình đã được đánh giá trên tập test và có thể sử dụng để dự đoán:

```python
import tensorflow as tf

# Load mô hình
model = tf.keras.models.load_model('path/to/resnet50_vsl.keras')

# Dự đoán
predictions = model.predict(preprocessed_images)
```

## Tiền xử lý dữ liệu

### Xử lý dữ liệu trùng lặp

- Loại bỏ class **AAA** do trùng lặp với class **AA**
- Giảm từ 26 classes xuống 25 classes

### Lưu trữ tối ưu

Dữ liệu được lưu dưới dạng **TFRecord** với nén GZIP:

- Dung lượng gốc (dataset.save()): ~14 GB
- Dung lượng sau nén (TFRecord + GZIP): ~313 MB
- **Tiết kiệm**: ~97.8%

### Data Augmentation

- Random horizontal flip
- Random brightness adjustment (±20%)
- Random contrast adjustment (0.8-1.2)

## Kết quả chi tiết

### Quá trình huấn luyện VGG16

![[vgg16_acc_loss.png]]

### Quá trình huấn luyện ResNet50

![[reports/figures/resnet50_acc_loss.png]]


### Quá trình huấn luyện MobileNetV1

![[resnet50_acc_loss 1.png]]

## Tác giả

NTTU - Nguyễn Xuân Tiến & Đồng Nguyễn Xuân An

## Tài liệu tham khảo

1. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. CVPR.
2. Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. ICLR.
3. Howard, A. G., et al. (2017). MobileNets: Efficient convolutional neural networks for mobile vision applications. arXiv.
4. Vietnamese Sign Language Dataset - Kaggle

## License

Dự án này được sử dụng cho mục đích học tập và nghiên cứu.

---

**Lưu ý**: Các mô hình đã huấn luyện được lưu trữ trên Google Drive do kích thước lớn. Xem file `models/Link (do cac files kha nang).txt` để biết thêm chi tiết.
