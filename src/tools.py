"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Đã được định nghĩa mẫu sẵn cho Học viên tham khảo
    {
        "name": "vehicle_query",
        "description": "Tra cứu hồ sơ xe, số km đã đi (ODO), tình trạng pin (SoH), cảnh báo lỗi và lịch sử bảo dưỡng bằng số VIN.",
        "parameters": {
            "type": "object",
            "properties": {
                "vin": {
                    "type": "string",
                    "description": "Số khung xe (VIN) cần tra cứu (ví dụ: 'VF8-VN202601')"
                }
            },
            "required": ["vin"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - student_id (string): Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')
    #    - datetime_str (string): Thời gian hẹn (ví dụ: '14:00 15/09/2026')
    #    - advisor_name (string): Tên cố vấn học tập
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
         "name": "schedule_service",
        "description": "Đặt lịch hẹn bảo dưỡng hoặc sửa chữa xe điện tại các Xưởng dịch vụ VinFast.",
        "parameters": {
            "type": "object",
            "properties": {
                "vin": {
                    "type": "string",
                    "description": "Số khung xe (VIN) cần đặt lịch (ví dụ: 'VF8-VN202601')"
                },
                "service_center": {
                    "type": "string",
                    "description": "Tên Xưởng dịch vụ VinFast (ví dụ: 'VinFast Smart City', 'VinFast Ocean Park')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn dịch vụ (ví dụ: '09:00 20/09/2026')"
                },
                "service_type": {
                    "type": "string",
                    "description": "Loại dịch vụ yêu cầu (ví dụ: 'Bảo dưỡng định kỳ', 'Kiểm tra pin', 'Sửa chữa cảnh báo lỗi')"
                }
            },
            "required": ["vin", "service_center", "datetime_str"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "VF8-VN202601": {
        "model": "VinFast VF8 Plus",
        "owner": "Trần Van Bình",
        "plate_number": "30K-882.49",
        "odo_km": 12500,
        "battery_soh": "96%",
        "warning_lights": "Không có cảnh báo lỗi (Hệ thống bình thường)",
        "maintenance_status": "Đã đến hạn bảo dưỡng cấp 1 (mốc 12.000 km)",
        "preferred_service_center": "VinFast Smart City"
    },
    "VF9-VN202602": {
        "model": "VinFast VF9 Eco",
        "owner": "Nguyễn Văn An",
        "plate_number": "30L-123.45",
        "odo_km": 24200,
        "battery_soh": "94%",
        "warning_lights": "Cảnh báo áp suất lốp trước bên phải (TPMS)",
        "maintenance_status": "Đã đến hạn bảo dưỡng cấp 2 (mốc 24.000 km)",
        "preferred_service_center": "VinFast Ocean Park"
    }
}


def execute_vehicle_query(vin: str) -> str:
    """Thực thi tra cứu thông tin xe điện theo số VIN"""
    vehicle = MOCK_DATABASE.get(vin.strip().upper())
    if vehicle:
        return json.dumps({
            "status": "SUCCESS",
            "vin": vin,
            "data": vehicle
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu xe có số VIN '{vin}' trong hệ thống VinFast."
        }, ensure_ascii=False)
def execute_schedule_service(vin: str, service_center: str, datetime_str: str, service_type: str = "Bảo dưỡng định kỳ") -> str:
    """Thực thi đặt lịch bảo dưỡng xe điện"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-VF-{vin}-2026",
        "vin": vin,
        "service_center": service_center,
        "datetime": datetime_str,
        "service_type": service_type,
        "message": f"Đặt lịch thành công cho xe {vin} ({service_type}) tại {service_center} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "vehicle_query": execute_vehicle_query,
    "schedule_service": execute_schedule_service
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
