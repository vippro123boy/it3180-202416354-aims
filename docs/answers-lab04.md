# Lab 04 — Release flow và phiên bản

## Vì sao `release/*` không merge ngược vào `master`?

Trong Release Flow rút gọn của học phần, `release/*` là dòng bảo trì của một baseline đã nộp, còn phát triển mới tiếp tục trên `master`. Merge cả nhánh release ngược lại có thể đưa số phiên bản, CHANGELOG hoặc thay đổi chỉ dành cho bản cũ vào dòng phát triển mới. Với hotfix, tách commit sửa hành vi rồi `cherry-pick -x` vào các dòng chịu ảnh hưởng; mỗi dòng giữ số phiên bản riêng. Đây là quy ước của bài thực hành, không phải giới hạn kỹ thuật của Git.

## So sánh với GitFlow

GitFlow có `main` để phát hành, `develop` để tích hợp công việc mới, nhánh `release/*` để chuẩn bị một bản phát hành và `hotfix/*` thường tách từ `main`; thay đổi được đưa trở lại các nhánh dài hạn. Bài thực hành dùng `master` làm dòng phát triển và giữ `release/labXX` như các dòng nộp bài/bảo trì song song; không có `develop`, và không merge ngược release. Mô hình này phù hợp việc kiểm tra các baseline theo tuần, nhưng cần chủ động lan truyền hotfix.

## Vì sao lên `1.0.0`, không phải `0.4.0`?

Theo SemVer, `0.y.z` báo API còn trong giai đoạn phát triển, có thể thay đổi không tương thích bất kỳ lúc nào. Bản `1.0.0` đánh dấu giao diện/hành vi được xem là ổn định để phát hành và bảo trì theo MAJOR.MINOR.PATCH. Trong bài, giảng viên chọn Lab 04 làm mốc phát hành ổn định. Số phiên bản là quyết định về cam kết tương thích, không suy ra tự động từ số lab.

## Tag và nhánh release

Tag annotated `v1.0.0` định danh chính xác một commit và không được di chuyển sau khi công bố. `release/lab04` là nhánh có thể tiến lên khi có bản vá. `git diff --stat v0.3.0 v1.0.0` ghi nhận thay đổi giữa baseline; `git switch --detach v1.0.0` hoặc `git worktree add` tái tạo phiên bản đó để kiểm toán.
