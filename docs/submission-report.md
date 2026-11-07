# BÁO CÁO TỔNG KẾT BÀI TẬP THỰC HÀNH SCM (IT3180)
## QUẢN LÝ CẤU HÌNH PHẦN MỀM VỚI GIT & GITHUB

---

### THÔNG TIN SINH VIÊN
- **Họ và tên**: Phạm Ngọc Thanh
- **Mã số sinh viên (MSSV)**: *202416354*
- **Email sinh viên**: *Thanh.PN2416354@sis.hust.edu.vn*
- **Tài khoản GitHub**: vippro123boy
- **Repository chính thức**: [https://github.com/vippro123boy/it3180-aims](https://github.com/vippro123boy/it3180-aims)

---

### 1. TỔNG QUAN HỆ THỐNG & QUY TRÌNH ÁP DỤNG
Bài thực hành triển khai toàn diện quy trình **Release Flow** của học phần IT3180 cho ứng dụng **AIMS-mini**, đáp ứng chuẩn mực 5 hoạt động SCM (Software Configuration Management):
- **Identification (Định danh cấu hình)**: Quản lý cấu hình thông qua commit SHA, quy ước Conventional Commits (`feat`, `fix`, `refactor`, `chore`, `docs`), tệp `.gitignore` loại bỏ file rác (`__pycache__`, `.vscode`), `.gitattributes` đồng bộ ngắt dòng LF.
- **Change Control (Kiểm soát thay đổi)**: Kiểm soát qua nhánh riêng biệt (`refactor/*`, `feature/*`, `bugfix/*`, `topic/*`, `hotfix/*`), Pull Request có mô tả chuẩn template, áp dụng Branch Protection trên `master` và `release/*` (bắt buộc review & approve).
- **Status Accounting (Ghi nhận trạng thái)**: Sử dụng chuẩn Semantic Versioning (`1.0.0`, `1.0.1`, `1.1.0`), tệp `CHANGELOG.md` theo định dạng Keep a Changelog, theo dõi tiến trình qua `git log A..B`, `git describe`.
- **Configuration Audit (Kiểm toán cấu hình)**: Đóng băng baseline với Annotated Tags (`v0.1.0` đến `v1.1.0`), kiểm thử đa phiên bản tự động bằng script matrix testing và `git worktree` / `git switch --detach`.
- **Release Management (Quản lý phát hành)**: Duy trì các baseline nộp bài qua các nhánh `release/labXX`, đóng băng phát hành, xử lý lỗi trên sản phẩm bằng `hotfix/*` kết hợp `git cherry-pick -x`, tích hợp pipeline CI với GitHub Actions.

---

### 2. BẢNG TỔNG HỢP CÁC NHÁNH VÀ TAGS

#### Danh sách nhánh (Branches)
| Tên nhánh | Mục đích | Base từ |
| :--- | :--- | :--- |
| `master` | Nhánh tích hợp chính (Main development line) của toàn bộ dự án | - |
| `release/lab01` | Baseline nộp bài Lab 01 (Tái cấu trúc mã nguồn vào package `aims/`) | `master` |
| `release/lab02` | Baseline nộp bài Lab 02 (Hoàn thiện `print_cart`, `search_by_title`, 3 kiểu merge) | `master` |
| `release/lab03` | Baseline nộp bài Lab 03 (Sửa lỗi giới hạn giỏ hàng, giải quyết conflict, hoàn tác) | `master` |
| `release/lab04` | Dòng bảo trì phiên bản phát hành `1.0.x` (tiếp nhận bản vá `1.0.1`) | `master` |
| `release/lab05` | Dòng phát hành phiên bản `1.1.0` (tiếp nhận tính năng mới và đồng bộ bản vá) | `master` |

#### Danh sách Thẻ phiên bản (Annotated Tags)
| Thẻ (Tag) | Trỏ tới nhánh | Phiên bản | Nội dung đánh dấu |
| :--- | :--- | :--- | :--- |
| `v0.1.0` | `release/lab01` | 0.1.0 | Bản phát hành hoàn thành Lab 01 (Refactor flow) |
| `v0.2.0` | `release/lab02` | 0.2.0 | Bản phát hành hoàn thành Lab 02 (Feature flow & Code Review) |
| `v0.3.0` | `release/lab03` | 0.3.0 | Bản phát hành hoàn thành Lab 03 (Bugfix & Conflict flow) |
| `v1.0.0` | `release/lab04` | 1.0.0 | Bản phát hành chính thức đầu tiên (Production Baseline) |
| `v1.0.1` | `release/lab04` | 1.0.1 | Bản vá lỗi tìm kiếm không phân biệt hoa thường trên dòng 1.0.x |
| `v1.1.0` | `release/lab05` | 1.1.0 | Bản phát hành nâng cấp tính năng mới và đồng bộ bản vá |

---

### 3. MINH CHỨNG CHECKLIST ĐẠT ĐƯỢC THEO 5 BÀI LAB

#### Lab 01 – Thiết lập môi trường & Refactor flow
- [x] Khởi tạo kho chứa Git với các cấu hình `.gitignore`, `.gitattributes`, `README.md`.
- [x] Tái cấu trúc mã nguồn: Dùng `git mv` chuyển `dvd.py`, `cart.py` vào package `aims/`, tạo `aims/__init__.py`.
- [x] Cập nhật lại import chuẩn xác trong `main.py` (`from aims.dvd...`, `from aims.cart...`).
- [x] Tạo Pull Request #1 từ nhánh `refactor/apply-release-flow` vào `master`, merge thành công và xóa nhánh làm việc.
- [x] Tạo nhánh nộp bài `release/lab01` đóng băng baseline đầu tiên.
- [x] Báo cáo trả lời câu hỏi thảo luận: `docs/answers-lab01.md`.
- [x] Kiểm tra thực thi: `python main.py` chạy ổn định, in ra `Total cost: 63.89 $`.

#### Lab 02 – Feature/Topic flow & Pull Request
- [x] Cấu hình Branch Protection cho `master` (bắt buộc PR, không cho push trực tiếp).
- [x] Thiết lập mẫu PR Template tại `.github/pull_request_template.md` thông qua nhánh `topic/pr-template`.
- [x] Thực hiện luồng Code Review nghiêm ngặt: Nhánh `feature/cart-print` nhận phản hồi review xử lý giỏ hàng trống, sửa đổi và được phê duyệt.
- [x] Minh chứng đầy đủ 3 kiểu tích hợp merge:
  - **Merge commit** (`--no-ff`): Dành cho tính năng `feature/cart-print`.
  - **Squash and merge**: Dành cho tính năng tìm kiếm `feature/search-by-title`.
  - **Rebase and merge**: Dành cho tài liệu ca sử dụng `topic/use-case-diagram`.
- [x] Đồng bộ nhánh cá nhân với `origin/master` trước khi gửi PR.
- [x] Tạo nhánh nộp bài `release/lab02`, gắn tag `v0.2.0`, hoàn thành `docs/answers-lab02.md`.

#### Lab 03 – Bugfix flow, xung đột & hoàn tác
- [x] Tạo Issue #6 ghi nhận lỗi giỏ hàng chấp nhận đĩa thứ 21 vượt quá sức chứa.
- [x] Thực hành TDD (Test-Driven Development): Viết test tái hiện lỗi trong `tests/test_cart.py` và chạy FAIL trước khi sửa mã nguồn.
- [x] Sửa toán tử so sánh `len(self.items) >= MAX_NUMBERS_ORDERED` và commit kèm thông điệp đóng Issue: `Fixes #6`.
- [x] Tạo và xử lý thành công xung đột hợp nhất (Merge Conflict) giữa hai nhánh sửa cùng thông báo thêm đĩa trong `aims/cart.py`.
- [x] Thực hành các kỹ thuật hoàn tác an toàn: Phân biệt `git reset` (commit cục bộ) và `git revert` (commit đã chia sẻ).
- [x] Tạo nhánh nộp bài `release/lab03`, gắn tag `v0.3.0`, hoàn thành `docs/answers-lab03.md`.

#### Lab 04 – Release flow & Phiên bản phát hành
- [x] Chuẩn bị phát hành đúng quy trình trên `master` (`topic/prepare-release-1.0.0`): bump version `1.0.0` trong `aims/__init__.py` và cập nhật `CHANGELOG.md`.
- [x] Tách nhánh `release/lab04`, thiết lập bảo vệ nhánh và gắn Annotated Tag `v1.0.0`.
- [x] Tuân thủ quy tắc Release Flow: Nhánh `release/lab04` tuyệt đối không merge ngược vào `master`.
- [x] Tiếp tục phát triển tính năng mới trên `master` mà không làm ảnh hưởng bản phát hành `1.0.0`.
- [x] Đánh dấu hồi quy Annotated Tags `v0.1.0`, `v0.2.0`, `v0.3.0` cho các bài lab trước.
- [x] Xuất bản GitHub Release chính thức cho phiên bản `v1.0.0`.
- [x] Hoàn thành tệp trả lời thảo luận: `docs/answers-lab04.md`.

#### Lab 05 – Hotfix flow & Bảo trì nhiều phiên bản
- [x] Tạo nhánh `release/lab05` chuẩn bị cho phiên bản `1.1.0`.
- [x] Tiếp nhận báo cáo lỗi tìm kiếm phân biệt hoa thường (Issue #20).
- [x] Tách nhánh `hotfix/search-case-insensitive` trực tiếp từ nhánh phát hành lỗi `release/lab04`:
  - Tách commit 1 chứa mã sửa lỗi và unit test để lấy mã `<FIX_SHA>`.
  - Tách commit 2 nâng phiên bản bản vá lên `1.0.1` cho dòng 1.0.x.
  - Hợp nhất vào `release/lab04` và gắn tag `v1.0.1`.
- [x] Sử dụng `git cherry-pick -x <FIX_SHA>` lan truyền chính xác bản sửa lỗi sang nhánh `master` và `release/lab05`.
- [x] Gắn tag `v1.1.0` trên nhánh `release/lab05`.
- [x] Tích hợp tự động hóa CI qua GitHub Actions tại `.github/workflows/ci.yml`.
- [x] Thực hiện kiểm toán cấu hình đa phiên bản (Configuration Audit), xác nhận 100% các dòng (`v1.0.1`, `v1.1.0`, `master`) hoạt động đúng đắn.
- [x] Hoàn thành tệp trả lời thảo luận: `docs/answers-lab05.md`.

---

### 4. KẾT QUẢ KIỂM THỬ HỆ THỐNG
1. **Kiểm thử đơn vị tự động (Unit Tests)**:
   ```bash
   python -m unittest discover -s tests -v
   ```
   *Kết quả*: **Ran 7 tests in 0.003s - OK** (Tất cả test cases đều vượt qua).
2. **Kiểm toán đa phiên bản (Matrix Execution Audit)**:
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
     git switch --detach -q $ref; printf "%-8s " $ref
     python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
   print(len(search_by_title([D('The Lion King')], 'lion')))"
   done; git switch -q master
   ```
   *Kết quả*:
   ```text
   v1.0.1   1
   v1.1.0   1
   master   1
   ```
3. **Thực thi chương trình ứng dụng**:
   ```bash
   python main.py
   ```
   *Kết quả in ra chuẩn*:
   ```text
   AIMS-mini v1.1.0
   Đã thêm đĩa 'The Lion King' vào giỏ hàng
   Đã thêm đĩa 'Star Wars' vào giỏ hàng
   Đã thêm đĩa 'Aladdin' vào giỏ hàng
   Total cost: 63.89 $

   ***********************CART***********************
   Ordered Items:
   1. DVD - The Lion King - Animation - Roger Allers - 87: 19.95 $
   2. DVD - Star Wars - Science Fiction - George Lucas - 124: 24.95 $
   3. DVD - Aladdin - Animation - John Musker - 90: 18.99 $
   Total cost: 63.89 $
   ***************************************************
   ```