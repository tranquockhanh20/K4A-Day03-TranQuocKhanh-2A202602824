# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Trần Quốc Khánh  
> **Mã Sinh Viên / Mã Học viên:** 2A202602824  
> **Chủ đề Lựa chọn:** Trợ lý Bảo dưỡng & Dịch vụ Xe điện VinFast (After-Sales EV Assistant)

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 3/ 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5/ 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 5/ 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4/ 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "mã số xe VF9-VN202602 hãy kiểm tra tình trạng của xe để xem đến lúc đi bảo hành chưa, nếu đã đến lúc nên đi bảo hành thì đặt lịch cho tôi lúc 17h ngày 14/09/2026 ở vinhomes ocean park",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "vehicle_query",
    "arguments": {
      "vin": "VF9-VN202602"
    },
    "observation": {
      "status": "SUCCESS",
      "vin": "VF9-VN202602",
      "data": {
        "model": "VinFast VF9 Eco",
        "owner": "Nguyễn Văn An",
        "plate_number": "30L-123.45",
        "odo_km": 24200,
        "battery_soh": "94%",
        "warning_lights": "Cảnh báo áp suất lốp trước bên phải (TPMS)",
        "maintenance_status": "Đã đến hạn bảo dưỡng cấp 2 (mốc 24.000 km)",
        "preferred_service_center": "VinFast Ocean Park"
      }
    },
    "latency_ms": 2331.52
  },
  {
    "step": 2,
    "query": "mã số xe VF9-VN202602 hãy kiểm tra tình trạng của xe để xem đến lúc đi bảo hành chưa, nếu đã đến lúc nên đi bảo hành thì đặt lịch cho tôi lúc 17h ngày 14/09/2026 ở vinhomes ocean park",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả tra cứu cho xe VinFast VF9-VN202602 (VinFast VF9 Eco): Chủ sở hữu: Nguyễn Văn An, Biển số: 30L-123.45, Odo: 24200, SOH: 94%, Cảnh báo: Cảnh báo áp suất lốp trước bên phải (TPMS), Bảo dưỡng: Đã đến hạn bảo dưỡng cấp 2 (mốc 24.000 km), Xưởng dịch vụ ưu tiên: VinFast Ocean Park.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 / 4 lượt (TC02, TC03, TC04, TC05 đều gọi tool chính xác 100%).
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
