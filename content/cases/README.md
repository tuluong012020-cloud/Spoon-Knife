# Dữ liệu Case Study công khai

Hiện chưa có Case Study được duyệt. Không đưa tài liệu gốc, bản nháp chờ duyệt hoặc dữ liệu khách hàng vào thư mục này hay repository công khai.

Giai đoạn 2 hỗ trợ mỗi dự án là một file JSON với đúng các trường: `slug`, `title`, `category`, `summary`, `body`, `publication_status`. `category` dùng `food`, `retail` hoặc `services`; `publication_status` phải là `approved`. Nội dung là văn bản công khai đã được người dùng duyệt, không HTML. Bộ sinh tạo URL `du-an/<slug>/` và cập nhật danh sách/bộ lọc. Chỉ chạy sau khi có phê duyệt; nhãn approved không tự chứng minh quyền công bố.

Chuỗi tài chính, nguồn dữ liệu và biểu đồ sẽ mở rộng trong Giai đoạn 3. Không đặt số liệu nhạy cảm vào `body`, không tạo kết quả hoặc lời chứng thực thay dữ liệu thiếu.
