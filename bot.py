from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from predictor import predict_next
from ocr_utils import extract_numbers_from_image

BOT_TOKEN = 'ISI_TOKEN_BOT_KAMU'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Halo! Kirim angka seperti ini:\n`1,5,10,1`\nAtau kirim screenshot Mega Wheel!",
        parse_mode='Markdown'
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        numbers = list(map(int, update.message.text.strip().split(',')))
        pred = predict_next(numbers)
        await update.message.reply_text(f"🎯 Prediksi dari teks: {pred}")
    except:
        await update.message.reply_text("⚠️ Format salah. Kirim angka dipisah koma, contoh: 1,5,10")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    path = "screenshot.jpg"
    await photo_file.download_to_drive(path)

    numbers = extract_numbers_from_image(path)
    if not numbers:
        await update.message.reply_text("⚠️ Gagal membaca angka dari gambar.")
        return

    pred = predict_next(numbers)
    await update.message.reply_text(
        f"📸 Angka dari gambar: {numbers[:20]}...\n🎯 Prediksi: {pred}"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot berjalan...")
    app.run_polling()
