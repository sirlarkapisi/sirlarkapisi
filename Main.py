from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Kullanıcı bilgileri (sadece bu kullanıcı erişebilecek)
AUTHORIZED_USER = {
    "username": "imdat",
    "password": "1i2m3d4a5t",
    "id": 16321123
}

# Kullanıcı durumunu takip etmek için hafıza (basit)
user_sessions = {}

# Menü butonları
main_menu = [["🎴 Dua Kartları", "📜 Kutsal Kitaplar"], ["🌍 Uygarlıklar", "🔮 Astroloji & Kabala"]]

# Kullanıcı doğrulama komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.username != AUTHORIZED_USER["username"]:
        await update.message.reply_text("Erişim reddedildi! Kullanıcı adı hatalı.")
        return
    user_sessions[user.id] = {"authenticated": False}
    await update.message.reply_text(
        "Hoşgeldin İmdat! Lütfen şifreni gönder.",
    )

# Şifre doğrulama
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.strip()

    if user.id not in user_sessions:
        await update.message.reply_text("Lütfen önce /start komutunu kullan.")
        return

    session = user_sessions[user.id]

    if not session["authenticated"]:
        if text == AUTHORIZED_USER["password"]:
            session["authenticated"] = True
            await update.message.reply_text(
                "Başarıyla giriş yaptınız.\nMenüden bir seçenek seçin:",
                reply_markup=ReplyKeyboardMarkup(main_menu, one_time_keyboard=True, resize_keyboard=True)
            )
        else:
            await update.message.reply_text("Şifre yanlış, tekrar deneyin.")
        return

    # Kullanıcı menü seçimi
    if text == "🎴 Dua Kartları":
        await update.message.reply_text("Dua Kartları modülüne hoşgeldiniz! Kodu kopyala:\n<DUA KODU>")
    elif text == "📜 Kutsal Kitaplar":
        await update.message.reply_text("Kutsal Kitaplar modülüne hoşgeldiniz! Kodu kopyala:\n<KUTSAL KİTAP KODU>")
    elif text == "🌍 Uygarlıklar":
        await update.message.reply_text("Uygarlıklar modülüne hoşgeldiniz! Kodu kopyala:\n<UYGARLIK KODU>")
    elif text == "🔮 Astroloji & Kabala":
        await update.message.reply_text("Astroloji ve Kabala modülüne hoşgeldiniz! Kodu kopyala:\n<ASTROLOJİ KODU>")
    else:
        await update.message.reply_text("Lütfen menüden geçerli bir seçenek seçin.")

# Ana fonksiyon
def main():
    application = ApplicationBuilder().token("BOT_TOKENINIZI_BURAYA_YERLEŞTİRİN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
