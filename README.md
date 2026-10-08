# Khởi Hướng — Website lập kế hoạch kinh doanh

Website tĩnh nhiều trang, HTML/CSS/JavaScript, phù hợp đường dẫn GitHub Pages `/Spoon-Knife/`. Không framework, không backend, không khóa API. Giai đoạn 2 chưa kích hoạt Pages hoặc workflow xuất bản.

## Tạo website

Cần Python 3, không cần cài thêm thư viện:

```bash
python3 scripts/build.py
```

Đầu ra trong `site/`. Đây là thư mục được sinh lại hoàn toàn: không chỉnh tay hoặc đặt file cá nhân trong `site/`. Chỉnh nguồn rồi chạy build. Đầu ra được commit để xem xét; chỉ đầu ra này được đề xuất sử dụng khi triển khai được duyệt riêng. Triển khai GitHub Pages từ artifact `site/` cần cấu hình trong giai đoạn sau, không chọn nhầm thư mục nguồn làm website.

## Cấu trúc

- `content/pages.json`: URL, title, description của 9 trang.
- `content/pages/`: nội dung riêng của từng trang.
- `content/packages.json`: nguồn giá duy nhất — Cơ bản 3.000.000đ, Tiêu chuẩn 9.000.000đ, Chuyên sâu 18.000.000đ, Toàn diện 30.000.000đ.
- `content/comparison.json`: danh mục so sánh. Chưa có phân bổ theo gói, mọi ô ghi Chờ phê duyệt.
- `content/cases/`: chỉ nội dung đã được duyệt công bố, không nguyên bản/nháp nội bộ.
- `templates/layout.html`: header, footer, breadcrumb, CTA và SEO chung.
- `assets/`: CSS và JavaScript chung, không phụ thuộc bên ngoài.
- `scripts/build.py`: sinh trang HTML và tài nguyên, không đọc hồ sơ tài chính trong workspace.
- `site/`: đầu ra sẵn để kiểm tra; có `.nojekyll` và `404.html`.

Trang chính: `/`, `/gioi-thieu/`, `/dich-vu/`, `/bang-gia/`, `/du-an/`, `/du-an/cau-truc-phan-tich/`, `/kien-thuc/`, `/cong-cu/`, `/lien-he/`. Trang cấu trúc chi tiết dự án không phải Case Study thực tế.

## Nội dung đã xác nhận và đang chờ

Giá/tên bốn gói là chính thức theo xác nhận của người dùng. Phạm vi theo gói, tiến độ, số vòng điều chỉnh, thuế, thanh toán và cam kết đều Chờ phê duyệt; chưa tự chuyển điều khoản từ hợp đồng mẫu thành lời chào dịch vụ. Gói Tiêu chuẩn được nhấn mạnh bằng thiết kế, không có tuyên bố bán chạy hoặc phổ biến nhất.

Case Study thực tế, chuỗi tài chính/biểu đồ, bài viết đầy đủ và máy tính tương tác dành cho Giai đoạn 3. Chưa có Case Study được duyệt nên trang dự án hiển thị trạng thái rỗng và bộ lọc. Hồ sơ chuyên gia, email/điện thoại: Chờ phê duyệt. Không sử dụng tên, giá vốn hoặc số liệu tài chính của các dự án chưa duyệt.

## Liên hệ

Nút Đăng ký tư vấn dẫn đến trang liên hệ và tự chọn gói qua tham số `goi`. Form kiểm tra trường bắt buộc/email, sau đó tạo tệp UTF-8 để tải về. Không gửi lên máy chủ, không lưu dữ liệu hoặc giả báo gửi thành công. Kênh tiếp nhận/backend cần được duyệt riêng.

## Xem thử và kiểm tra base path

Trên máy thực thi, chạy `python3 -m http.server 8000 --bind 127.0.0.1 --directory site`. Máy chủ chỉ hoạt động trên máy chạy lệnh. Môi trường onboarding hiện không cung cấp URL Preview/chuyển tiếp cổng để truy cập từ Mac; không coi địa chỉ loopback trong cloud là URL dùng từ máy cá nhân.

Để kiểm tra đúng `/Spoon-Knife/`, tạo thư mục kiểm thử ngoài repository, đặt symlink `Spoon-Knife` trỏ đến thư mục `site` rồi phục vụ thư mục kiểm thử bằng Python. Dùng trình duyệt/request trong cùng môi trường để kiểm tra đường dẫn trang, URL lồng hai cấp, query chọn gói, liên kết và assets. Không xuất bản để kiểm tra.

Kiểm tra JavaScript: `node --check assets/js/script.js` nếu có Node. Kiểm tra build lặp lại, responsive 4 cột từ 1101px, 2 cột từ 761–1100px, 1 cột đến 760px; bảng so sánh cuộn trong khung trên màn hình nhỏ. Kiểm tra menu, bàn phím, chọn gói, lỗi input, tải yêu cầu, console/network và danh sách rỗng. Canonical/sitemap sẽ hoàn thiện khi domain xuất bản được xác nhận.
