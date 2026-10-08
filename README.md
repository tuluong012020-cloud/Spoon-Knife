# Khởi Hướng — Website dịch vụ lập kế hoạch kinh doanh

Website tiếng Việt dùng HTML, CSS và JavaScript thuần, không cần framework, cài dependencies hay build.

## Xem trước trên máy của bạn

Trong thư mục repository, chạy:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Mở trình duyệt tại `http://127.0.0.1:8000`. Nếu máy sử dụng lệnh `python` thay vì `python3`, thay tên lệnh tương ứng. Nhấn Ctrl+C để dừng. Máy chủ chỉ phục vụ trên máy đang chạy lệnh; địa chỉ này không mở website trên một máy khác. Trong môi trường cloud, kiểm tra bằng HTTP cục bộ hoặc tải repository về máy cá nhân để xem trong trình duyệt. Không có bước triển khai công khai.

## Các tệp

- `index.html`: nội dung dịch vụ, quy trình, bảng giá và hộp thoại tư vấn.
- `styles.css`: màu navy, trắng, gold; bố cục responsive và trạng thái tương tác.
- `script.js`: menu điện thoại, hộp thoại, chọn gói và tải yêu cầu tư vấn bằng tệp văn bản UTF-8.

## Biểu mẫu tư vấn

Chưa cấu hình email, số điện thoại hay backend tiếp nhận. Biểu mẫu tạo tệp `yeu-cau-tu-van.txt` để người dùng tải về; không gửi yêu cầu và không lưu dữ liệu lên máy chủ. Cần cung cấp kênh liên hệ thực trước khi đưa website vào sử dụng thương mại. Tên thương hiệu Khởi Hướng và phạm vi các gói là nội dung mẫu có thể tùy chỉnh; biểu đồ trên banner chỉ mang tính minh họa.

## Kiểm tra

Kiểm tra cú pháp: `node --check script.js` (nếu có Node.js). Chạy máy chủ như trên, kiểm tra trang, CSS và JS đều trả HTTP 200. Kiểm tra bố cục ở 320px, 390px, 768px và 1440px; menu trên điện thoại; nút chọn gói; trường bắt buộc và email; tải tệp yêu cầu; đóng hộp thoại bằng Escape. Không có test suite hoặc build tool riêng của dự án.

---

## README gốc của Spoon-Knife

### Well hello there!

This repository is meant to provide an example for *forking* a repository on GitHub.

Creating a *fork* is producing a personal copy of someone else's project. Forks act as a sort of bridge between the original repository and your personal copy. You can submit *Pull Requests* to help make other people's projects better by offering your changes up to the original project. Forking is at the core of social coding at GitHub.

After forking this repository, you can make some changes to the project, and submit [a Pull Request](https://github.com/octocat/Spoon-Knife/pulls) as practice.

For some more information on how to fork a repository, [check out our guide, "Forking Projects""](http://guides.github.com/overviews/forking/). Thanks! :sparkling_heart:
