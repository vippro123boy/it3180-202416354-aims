LAB 02 ANSWERS - Phạm Ngọc Thành - 202416354

## 1. Vì sao phải đồng bộ nhánh với `master` trước khi gửi hoặc merge Pull Request?

1. **Tích hợp sớm để phát hiện xung đột (Early Integration & Conflict Detection)**:
   - Trong quá trình lập trình viên phát triển tính năng trên nhánh riêng, nhánh `master` có thể đã nhận thêm các commit/tính năng mới từ các thành viên khác.
   - Bằng cách đồng bộ (`git merge origin/master` hoặc `git rebase origin/master`), lập trình viên sẽ phát hiện và giải quyết xung đột cục bộ ngay tại máy mình thay vì đẩy gánh nặng xử lý xung đột lên reviewer hoặc làm hỏng quá trình tích hợp.
2. **Kiểm tra tính tương thích và hồi quy (Regression Testing)**:
   - Sau khi đồng bộ, lập trình viên có thể chạy lại bộ kiểm thử (`python -m unittest discover -s tests -v`) và chương trình chính (`python main.py`) để chắc chắn rằng code mới không làm hỏng tính năng sẵn có trên master.
3. **Đảm bảo PR ở trạng thái sẵn sàng tích hợp (Clean Mergeable State)**:
   - Giúp GitHub hiển thị trạng thái "Able to merge" màu xanh lá, reviewer có thể tự tin phê duyệt và bấm merge mà không gặp thông báo "This branch has conflicts".

---

## 2. Khi nào không được dùng rebase? Giải thích quy tắc vàng của Rebase

### Quy tắc vàng của Rebase (The Golden Rule of Rebasing)
> **"Không bao giờ rebase một nhánh công khai (public branch) đã được push lên remote hoặc có người khác cùng tham gia phát triển."**

### Chi tiết và Hậu quả:
- **Cơ chế rebase**: `git rebase` tua lại các commit trên nhánh hiện tại và tạo ra các commit hoàn toàn mới (cùng nội dung thay đổi nhưng mang **mã băm SHA mới** và mốc thời gian mới) đặt tiếp nối vào đỉnh nhánh gốc.
- **Hậu quả nếu vi phạm**:
  - Khi một nhánh đã chia sẻ bị rebase và `push --force`, toàn bộ các lập trình viên khác đang theo dõi nhánh đó sẽ bị phân kỳ lịch sử (diverged branch).
  - Khi họ thực hiện `git pull`, Git sẽ hiểu nhầm các commit cũ là commit mới cần gộp, tạo ra vô số commit trùng lặp, xung đột phức tạp ("Merge Hell") và phá hủy tính toàn vẹn của lịch sử dự án.
- **Khi nào NÊN dùng rebase**:
  - Chỉ dùng trên các nhánh cá nhân riêng biệt (private feature branch) tại máy local trước khi tạo PR, nhằm làm sạch và tuyến tính hóa lịch sử commit cá nhân.

---

## 3. Nhánh `feature/*` khác `topic/*` ra sao?

feature/* dành cho hành vi/chức năng mới của sản phẩm (ví dụ feature/search-by-title). topic/* dành cho thay đổi theo một chủ đề khác như tài liệu, quy trình hoặc CI (topic/pr-template). Cả hai là nhánh sống ngắn, tạo từ master, qua PR rồi hợp nhất vào master; tên nhánh giúp người xem hiểu mục đích, không làm thay đổi cơ chế Git.

---

## 4. So sánh 3 kiểu merge trên GitHub

Merge commit giữ các commit và điểm hội tụ. Squash and merge gộp thay đổi thành một commit mới, mất chi tiết commit trên nhánh. Rebase and merge tạo lại các commit với SHA mới trên đầu nhánh đích, cho lịch sử tuyến tính. Chọn theo nhu cầu truy vết và độ gọn của lịch sử; không dùng rebase để viết lại lịch sử nhánh đã chia sẻ.
