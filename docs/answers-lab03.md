LAB 03 ANSWERS - Phạm Ngọc Thành - 202416354

## Merge base là gì?

Merge base: Là tổ tiên chung gần nhất (lowest common ancestor) của hai nhánh chuẩn bị merge. Git dựa vào merge base để thực hiện phép so sánh 3 chiều (3-way merge) và tìm ra những thay đổi khác biệt.

## Vì sao `master` và `release/*` phải dùng `revert`?

Lệnh reset dời con trỏ và xóa bỏ commit khỏi lịch sử, buộc phải dùng push --force làm rối loạn kho lưu trữ của nhóm. Lệnh revert tạo ra một commit mới đảo ngược các thay đổi trước đó, giữ nguyên tính bất biến và an toàn cho lịch sử công khai.

## Chứng cứ trong lịch sử repo

Nhánh `bugfix/cart-limit-off-by-one` ghi test lỗi trước khi sửa mã. Nhánh `bugfix/discount-calculation` bắt đầu từ `feature/discount`, với test và bản sửa trước khi tính năng vào `master`. Hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` tạo xung đột thật trên cùng dòng; commit giải quyết giữ thông điệp tiếng Việt có tên DVD. Sau đó nhánh `bugfix/revert-show-added-title` đảo merge bằng `revert -m 1`.
