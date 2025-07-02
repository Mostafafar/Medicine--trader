import os
from fastapi import FastAPI
from webhook import handle_webhook, set_webhook
from bot import create_application

app = FastAPI()

# Initialize Telegram application
application = create_application()

# Add webhook routes
app.add_api_route("/webhook", handle_webhook, methods=["POST"])
app.add_api_route("/set_webhook", set_webhook, methods=["GET"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))