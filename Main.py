import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.environ.get("BOT_TOKEN")

# Başlangıç mesajı
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📿 Günlük Dua", callback_data='daily_prayer')],
        [InlineKeyboardButton("📖 Günlük Söz", callback_data='daily_quote')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📜 Sırlar Kapısı'na hoş geldiniz.\nBir seçim yapınız:", reply_markup=reply_markup)

# Buton seçimlerini yakalama
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "daily_prayer":
        text = generate_prayer()
    elif query.data == "daily_quote":
        text = generate_quote()
    else:
        text = "❓ Geçersiz seçim."

    await query.edit_message_text(text=text)

# Günlük dua örneği
def generate_prayer():
    return (
        "🕊️ **Günün Hurûf-u Mukattaa Duası**\n\n"
        "📿 Ya Allah, Ya Hafîz, Ya Nur...\n"
        "Bu harflerin sırrıyla kalplerimize ferahlık, sözlerimize hikmet ver.\n\n"
        "📅 Tarih: 01.06.2025"
    )

# Günlük söz örneği
def generate_quote():
    return (
        "🗝️ **Günün Sözü**\n\n"
        "Her harf bir sırdır; bazen dua, bazen anahtar.\n"
        "Every letter is a secret; sometimes a prayer, sometimes a key.\n\n"
        "📅 Tarih: 01.06.2025"
    )
