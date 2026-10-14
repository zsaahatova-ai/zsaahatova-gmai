import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    name = event.get("name", "Жалгас")
    result = {
        "message": f"Сәлем, {name}! Код AWS Lambda арқылы іске қосылды.",
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "function": context.function_name if context else "local",
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result, ensure_ascii=False),
    }
