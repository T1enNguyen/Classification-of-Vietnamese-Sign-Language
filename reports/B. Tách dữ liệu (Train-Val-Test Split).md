## 1. Xử lý dữ liệu trùng lặp

- **Vấn đề:** Lớp `AA` và lớp `AAA` cùng biểu thị cho chữ cái Â, gây trùng lặp dữ liệu.

- **Giải pháp:** Xóa thư mục lớp `AAA` để tránh nhầm lẫn trong quá trình huấn luyện.

- **Kết quả:** 
	- Số lượng lớp giảm từ 26 xuống còn 25 lớp.
	- Tổng số mẫu còn lại: 25,000 ảnh (1,000 ảnh mỗi lớp).

## 2. Phân chia tập dữ liệu

- **Mục tiêu:** Chia dữ liệu thành 3 tập: Train, Validation, Test để huấn luyện và đánh giá mô hình.

- **Phương pháp:** Sử dụng TensorFlow `image_dataset_from_directory` với tỷ lệ phân chia:
	- **Train:** 80% (20,000 mẫu)
	- **Validation:** 10% (2,496 mẫu)
	- **Test:** 10% (2,504 mẫu)

- **Cấu hình:**
	- Kích thước ảnh: 224×224 pixels
	- Batch size: 32
	- Seed: 42 (để đảm bảo tính tái lập)

- **Kết quả:**
	- Train: 625 batches
	- Validation: 78 batches
	- Test: 79 batches

## 3. Lưu trữ dữ liệu

- **Mục tiêu:** Lưu các tập dữ liệu đã chia để sử dụng lại trong các lần huấn luyện sau.

- **Phương pháp:** Sử dụng `tf.data.Dataset.save()` để lưu trữ dưới dạng TensorFlow Dataset.

- **Vị trí lưu trữ:** Google Drive tại `/content/drive/MyDrive/NTTU_Chuyen de AI_2/`
	- `train_ds/`
	- `val_ds/`
	- `test_ds/`

## 4. Kiểm tra tính toàn vẹn

- **Mục tiêu:** Xác minh dữ liệu đã được lưu và tải lại đúng cách.

- **Kết quả kiểm tra:**
	- Cấu trúc ảnh trong 1 batch: (32, 224, 224, 3)
	- Cấu trúc nhãn trong 1 batch: (32,)
	- Tất cả 25 lớp đều có mặt trong cả 3 tập dữ liệu

- **Phân bố mẫu:**
	- Tập Train: Mỗi lớp có khoảng 770-820 mẫu
	- Tập Validation: Mỗi lớp có khoảng 75-115 mẫu
	- Tập Test: Mỗi lớp có khoảng 82-122 mẫu

- **Nhận xét:** Dữ liệu được phân chia tương đối cân bằng giữa các lớp, phù hợp cho việc huấn luyện mô hình phân loại.
