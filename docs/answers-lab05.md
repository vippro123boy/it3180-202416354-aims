# Lab 05 — Hotfix và bảo trì nhiều phiên bản

## Ưu, nhược điểm của upstream first và release first

**Upstream first** sửa trên dòng phát triển chính trước, chạy kiểm thử đầy đủ rồi chuyển bản sửa vào các nhánh phát hành. Ưu điểm: giảm nguy cơ quên sửa trên `master`, mã mới nhất có bản sửa ngay, và thường hợp với sản phẩm lớn có dòng phát triển mạnh. Nhược điểm: khi lỗi chỉ xuất hiện trên bản cũ, môi trường hoặc mã trên `master` có thể khác, khiến khó tái hiện và backport.

**Release first** sửa từ đúng baseline đang gặp lỗi rồi chuyển riêng commit sửa hành vi sang các dòng khác. Ưu điểm: tái hiện và kiểm thử trực tiếp trên bản người dùng đang chạy, phát hành bản vá nhanh. Nhược điểm: phải theo dõi cẩn thận mọi dòng phiên bản chịu ảnh hưởng, tránh quên backport/cherry-pick; không được chuyển nhầm commit nâng số phiên bản cũ sang `master`.

Trong bài này chọn release first vì lỗi tìm kiếm xuất hiện trên `v1.0.0`. Commit sửa lỗi và test riêng được chuyển bằng `git cherry-pick -x`; commit nâng `1.0.1` chỉ ở `release/lab04`.

## Nếu quên đưa bản sửa vào `release/lab05`, phát hiện bằng lệnh nào?

`git cherry -v release/lab05 release/lab04` so sánh các patch trên `release/lab04` với `release/lab05`. Dòng `+` trước commit sửa lỗi nghĩa là chưa có patch tương đương trên `release/lab05`; dòng `-` nghĩa là đã có bản tương đương dù SHA khác do cherry-pick. Cần đọc đúng thứ tự tham số vì đối số thứ nhất là nhánh nhận để đối chiếu. Ngoài ra chạy kiểm thử hành vi trên `v1.0.1`, `v1.1.0` và `master` để kiểm tra kết quả thực tế.

## Vì sao tách commit sửa lỗi và nâng số phiên bản?

Sửa hành vi cần có mặt ở cả `release/lab04`, `release/lab05` và `master`, nhưng số `1.0.1` chỉ thuộc dòng 1.0.x. Tách commit giúp cherry-pick đúng phần cần thiết và giữ truy vết bằng dòng `(cherry picked from commit ...)`.
