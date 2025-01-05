from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import asyncio
import os

words_list = [
    "abandon - يتخلى عن",
    "ability - قدرة",
    "abnormal - غير طبيعي",
    "abolish - يلغي",
    "abrupt - مفاجئ",
    "absorb - يمتص",
    "abstract - مجرد",
    "abundant - وفير",
    "academy - أكاديمية",
    "access - وصول",
    "accompany - يرافق",
    "accomplish - ينجز",
    "account - حساب",
    "accumulate - يتراكم",
    "accurate - دقيق",
    "achieve - يحقق",
    "acknowledge - يعترف",
    "acquire - يكتسب",
    "adapt - يتكيف",
    "adequate - كافٍ",
    "adjacent - مجاور",
    "adjust - يضبط",
    "administer - يدير",
    "advantage - ميزة",
    "adventure - مغامرة",
    "advocate - يدافع عن",
    "affect - يؤثر على",
    "afford - يتمكن من تحمل",
    "agency - وكالة",
    "agenda - جدول أعمال",
    "aggressive - عدواني",
    "allocate - يخصص",
    "alter - يغير",
    "alternative - بديل",
    "ambition - طموح"
]


# معرف الشات (تأكد من تخصيصه)
CHAT_ID = "1721817711"

# دالة إرسال الكلمات اليومية
async def send_daily_words(application: Application):
    daily_words = random.sample(words_list, 10)
    message = "الكلمات اليومية:\n" + "\n".join(daily_words)
    await application.bot.send_message(chat_id=CHAT_ID, text=message)

# دالة إرسال الكلمات عند الطلب
async def send_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    daily_words = random.sample(words_list, 10)
    message = "الكلمات اليومية:\n" + "\n".join(daily_words)
    await update.message.reply_text(message)

# دالة البدء
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! سأرسل لك كلمات يومية. استخدم الأمر /words للحصول على الكلمات.")

# جدولة المهمة اليومية
async def schedule_task(application: Application):
    while True:
        now = asyncio.get_event_loop().time()
        next_run = now + 60  # تشغيل كل دقيقة
        asyncio.create_task(send_daily_words(application))
        await asyncio.sleep(next_run - now)

# الدالة الرئيسية
def main():
    # ضع التوكن الخاص بك هنا أو قم بتحميله من متغيرات البيئة
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7908394892:AAFJ3NHsVlQlqb-aZnT86zAJMXzZW3nVqSc")

    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إعداد الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("words", send_words))

    # تشغيل الجدولة في الخلفية
    asyncio.get_event_loop().create_task(schedule_task(application))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()
