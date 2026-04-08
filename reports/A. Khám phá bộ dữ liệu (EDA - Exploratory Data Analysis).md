## 1. Kiểm tra tính toàn vẹn của dữ liệu
- **Mục tiêu:** Phát hiện tình trạng Data Imbalance. Điều này sẽ khiến mô hình bị thiên kiến.
	1. Xác định số lượng ảnh và lớp.
	2. Xác định số lượng ảnh trong mỗi lớp.
	3. Kiểm tra định dạng của ảnh.

- **Kết quả:**
	- Bộ dữ liệu có tổng số lượng ảnh là 26000 và 26 lớp.
	- Trong đó mỗi lớp chứa 1000 ảnh.
	- Tất cả ảnh đều có định dạng là .pnj

<div align="center">
  <img src="figures/1.png" width="90%">
  <p><i>Hình 1: Số lượng ảnh trên mỗi lớp</i></p>
</div>

- Đặc tả về các lớp đặc biệt: 

| AA  | ==AAA== | DD  | OOO |
| --- | --- | --- | --- |
| Â   | ==Â==   | Đ   | Ơ   |

- **Vấn đề:** 
	- Bảng chữ cái tiếng việt gồm có 29 chữ nhưng bộ dữ liệu này chỉ có 26. Thiếu 3 chữ là `Ê`,`Ô`,`Ư` 
	- Bên cạnh đó lớp `AA` và lớp `AAA` cùng biểu thị cho chữ cái Â.

## 2. Phân tích kích thước và tỉ lệ

- **Mục tiêu:** Xác định kích thước ban đầu của ảnh.  Vì các mô hình cần đầu vào là 224×224.

- **Kết quả:** Phần lớn dataset đã được chuẩn hóa về kích thước 224x224.

<div align="center">
  <img src="figures/2.png" width="90%">
  <p><i>Hình 2: Phân bố chiều cao và chiều rộng của ảnh</i></p>
</div>

## 3. **Kiểm tra trực quan**
- **Mục tiêu:** Xác định ảnh thuộc các lớp có khác nhau không.

- **Kết quả:** Các lớp có ảnh khác nhau trừ lớp `AA` và lớp `AAA`  đang sử dụng cùng trạng thái để biểu thị cho chữ cái `Â`. 

![[3.png]]


