import os
from telegram import Update
from telegram.ext import ContextTypes
from bot import application

async def handle_webhook(request):
    """Handle incoming Telegram updates"""
    if request.method == "POST":
        update = Update.de_json(await request.json(), application.bot)
        await application.process_update(update)
        return {"status": "ok"}
    return {"status": "method not allowed"}, 405

async def set_webhook(request):
    """Programmatically set webhook URL"""
    webhook_url = os.environ.get("WEBHOOK_URL")
    if not webhook_url:
        return {"error": "WEBHOOK_URL not set"}, 400
    
    await application.bot.set_webhook(webhook_url)
    return {"status": f"Webhook set to {webhook_url}"}, 200