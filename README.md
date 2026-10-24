# Ao Sen Food ML — Mini Project

## Mục tiêu
Phân tích sơ bộ mối liên hệ giữa giá món ăn và số suất bán/ngày ước lượng của 7 nhóm món quanh Ao Sen, Hà Đông. Dùng Linear Regression để minh họa quy trình ML cơ bản.

## Lưu ý về dữ liệu
**Toàn bộ `sales_min`, `sales_max` và `sales_avg` trong dataset hiện tại là ước lượng do người dùng cung cấp trong quá trình xây dựng project, không phải số liệu bán hàng đã được xác minh độc lập.** Vì vậy kết quả chỉ dùng cho demo học tập, không đại diện cho doanh số thật của toàn bộ khu vực Ao Sen.

`price_avg` được tính bằng trung điểm của khoảng giá. `sales_avg` là trung điểm của khoảng lượt bán nếu có khoảng; riêng các giá trị được cung cấp dưới dạng một con số thì giữ nguyên con số đó.

## Cấu trúc repository
```text
AoSen_Food_ML/
├── data/
│   └── food_data.csv
├── notebooks/
│   └── AoSen_Food_ML.ipynb
├── src/
│   └── preprocessing.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Cách chạy
1. Cài Python 3.10+.
2. Tạo môi trường ảo (không bắt buộc nhưng khuyến nghị).
3. Cài thư viện:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Mở `notebooks/AoSen_Food_ML.ipynb` trong VS Code (cài extension Python và Jupyter) hoặc Jupyter Notebook.
5. Chạy các cell từ trên xuống.

## Phương pháp
- Khám phá dữ liệu và thống kê mô tả.
- Trực quan hóa giá và số suất bán ước lượng.
- Fit Linear Regression với `price_avg` là biến đầu vào và `sales_avg` là biến mục tiêu.
- So sánh với baseline dự đoán bằng trung bình.
- Báo cáo MAE, RMSE, R² và residual trên chính 7 dòng demo.

## Hạn chế
- Chỉ có 7 điểm tổng hợp theo nhóm món.
- Các số suất bán là ước lượng, không phải quan sát bán hàng được xác minh.
- Đánh giá trên tập huấn luyện không chứng minh khả năng dự đoán dữ liệu mới.
- Không thể kết luận giá gây ra thay đổi doanh số từ dữ liệu này.
- Muốn dự báo thực tế cần thu thập số suất bán theo cùng khoảng thời gian, tốt nhất theo món/quán/ngày, và lưu URL + ngày thu thập cho từng bản ghi.

## GitHub
Tạo repository GitHub mới, rồi đẩy toàn bộ thư mục này lên. Không đưa thư mục `.venv/` hoặc file cache vào Git.
