# Tài liệu Use Case hệ thống AIMS
```mermaid
flowchart LR
    Customer(("Customer<br>(Khách hàng)"))
    PM(("Product Manager<br>(Quản lý kho)"))
    Admin(("Administrator<br>(Quản trị)"))
    VNPay(("VNPay Subsystem"))

    subgraph AIMS["Hệ thống AIMS"]
        UC01(["UC01: Xem danh mục sản phẩm"])
        UC02(["UC02: Tìm kiếm sản phẩm"])
        UC03(["UC03: Xem chi tiết sản phẩm"])
        UC04(["UC04: Quản lý giỏ hàng"])
        UC05(["UC05: Đặt hàng"])
        UC06(["UC06: Thanh toán"])
        UC07(["UC07: Đặt giao nhanh"])

        UC08(["UC08: Quản lý Media"])
        UC09(["UC09: Cập nhật tồn kho"])

        UC10(["UC10: Quản lý người dùng"])
        UC11(["UC11: Báo cáo đơn hàng"])
    end

    Customer --> UC01
    Customer --> UC02
    Customer --> UC03
    Customer --> UC04
    Customer --> UC05

    UC05 -. include .-> UC06
    UC07 -. extend .-> UC05
    UC06 --- VNPay

    PM --> UC08
    PM --> UC09

    Admin --> UC10
    Admin --> UC11
```
