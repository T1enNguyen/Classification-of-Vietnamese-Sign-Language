## 1. Giới thiệu

- **Mục tiêu:** Xây dựng mô hình phân loại 25 lớp ký hiệu ngôn ngữ ký hiệu Việt Nam sử dụng kỹ thuật Transfer Learning với mô hình ResNet50 đã được huấn luyện trên ImageNet.

- **Kiến trúc:** ResNet50 (Residual Network 50 layers) - một trong những kiến trúc CNN mạnh mẽ nhất cho bài toán phân loại ảnh.

## 2. Chuẩn bị dữ liệu

- **Nguồn dữ liệu:** Sử dụng các tập dữ liệu đã được chia sẵn từ bước trước:
	- Train: 20,000 mẫu (625 batches)
	- Validation: 2,496 mẫu (78 batches)
	- Test: 2,504 mẫu (79 batches)

- **Tiền xử lý:**
	- Chuẩn hóa ảnh theo chuẩn ImageNet sử dụng `preprocess_input` của ResNet50
	- Kích thước ảnh: 224×224 pixels
	- Batch size: 32

- **Tăng cường dữ liệu (Data Augmentation):**
	- Random horizontal flip (lật ngang ngẫu nhiên)
	- Random brightness adjustment (điều chỉnh độ sáng, max_delta=0.2)
	- Random contrast adjustment (điều chỉnh độ tương phản, 0.8-1.2)
	- Chỉ áp dụng cho tập Train, không áp dụng cho Val và Test

## 3. Kiến trúc mô hình

- **Base Model:** ResNet50 với trọng số ImageNet (không bao gồm lớp phân loại đầu ra)

- **Custom Head:**
	- GlobalAveragePooling2D: Giảm chiều từ feature maps
	- Dropout(0.4): Giảm overfitting
	- Dense(25, activation='softmax'): Lớp đầu ra cho 25 lớp

- **Tổng số layers:** 178 layers (ResNet50 base + custom head)

## 4. Chiến lược huấn luyện 2 giai đoạn

### **Giai đoạn 1: Warmup (5 epochs)**

- **Mục đích:** Huấn luyện lớp đầu (head) mới trong khi giữ nguyên trọng số của ResNet50 base.

- **Cấu hình:**
	- Đóng băng toàn bộ base model (`base_model.trainable = False`)
	- Optimizer: Adam
	- Learning Rate: Tăng dần từ 0 đến 1e-3 trong 3 epochs đầu (warmup), sau đó giữ ổn định
	- Loss function: Sparse Categorical Crossentropy
	- Metric: Accuracy

- **Lý do:** Cho phép lớp đầu mới học cách ánh xạ features từ ResNet50 sang 25 lớp của bộ dữ liệu mà không làm hỏng trọng số đã học của base model.

### **Giai đoạn 2: Fine-tuning (10 epochs)**

- **Mục đích:** Tinh chỉnh toàn bộ mô hình để tối ưu hóa cho bộ dữ liệu cụ thể.

- **Cấu hình:**
	- Rã đông toàn bộ mô hình (`base_model.trainable = True`)
	- Optimizer: SGD với momentum=0.9
	- Learning Rate: 1e-5 (rất nhỏ để tránh phá hủy trọng số đã học)
	- Callbacks:
		- **EarlyStopping:** Dừng huấn luyện nếu val_loss không cải thiện sau 5 epochs, khôi phục trọng số tốt nhất
		- **ReduceLROnPlateau:** Giảm learning rate xuống 20% nếu val_loss không cải thiện sau 3 epochs (min_lr=1e-7)

- **Lý do:** Learning rate rất nhỏ giúp tinh chỉnh từ từ các trọng số của ResNet50 để phù hợp với đặc điểm của ngôn ngữ ký hiệu Việt Nam mà không làm mất đi kiến thức đã học từ ImageNet.

## 5. Đánh giá mô hình

- **Phương pháp:** Đánh giá trên tập Test (2,504 mẫu chưa từng thấy trong quá trình huấn luyện)

- **Metrics:**
	- Test Loss
	- Test Accuracy

- **Trực quan hóa:**
	- Biểu đồ Accuracy và Loss qua các epochs cho cả Train và Validation
	- Đường phân cách đỏ tại epoch 5 đánh dấu thời điểm chuyển từ Warmup sang Fine-tuning
	- Hiển thị dự đoán trên 9 mẫu ngẫu nhiên với nhãn thực tế, nhãn dự đoán và độ tin cậy

## 6. Lưu trữ mô hình

- **Định dạng:** HDF5 (.h5)
- **Vị trí:** `/content/drive/MyDrive/NTTU_Chuyen de AI_2/resnet50_vsl_25_classes.h5`
- **Nội dung:** Toàn bộ kiến trúc mô hình và trọng số đã được huấn luyện

## 7. Ưu điểm của phương pháp

- **Transfer Learning:** Tận dụng kiến thức đã học từ ImageNet (1.4 triệu ảnh, 1000 lớp) để cải thiện hiệu suất trên bộ dữ liệu nhỏ hơn (25,000 ảnh, 25 lớp)

- **Huấn luyện 2 giai đoạn:** Tránh catastrophic forgetting (quên kiến thức cũ) bằng cách huấn luyện head trước, sau đó mới fine-tune toàn bộ

- **Data Augmentation:** Tăng tính đa dạng của dữ liệu huấn luyện, giảm overfitting

- **Callbacks thông minh:** EarlyStopping và ReduceLROnPlateau giúp tối ưu hóa quá trình huấn luyện và tránh overfitting

## 8. Kết luận

Notebook này triển khai một pipeline hoàn chỉnh cho bài toán phân loại ngôn ngữ ký hiệu Việt Nam sử dụng Transfer Learning. Phương pháp này đặc biệt hiệu quả khi làm việc với bộ dữ liệu có kích thước vừa phải và muốn đạt được độ chính xác cao trong thời gian huấn luyện hợp lý.
