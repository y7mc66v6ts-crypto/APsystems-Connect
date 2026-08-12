from apsystems_connect_core.config import APP_ID, APP_SECRET, SID
from apsystems_connect_core.auth import build_headers

request_path = f"/user/api/v2/systems/details/{SID}"

headers = build_headers(
    APP_ID,
    APP_SECRET,
    request_path,
)

print("=== Headers ===")

for key, value in headers.items():
    print(f"{key}: {value}")