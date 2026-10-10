import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8873057804:AAEMA2AWwJbmfoHB77f1H6Lw_8xnt_F-Cos"
ADMIN_ID = 6661421202
ADMIN_USER = "@youssef_alaidy"

SERVICES = {
    "تويتر X - 14 خدمة": ["مشاهدات X 2ج","لايكات X 40ج","تعليقات X 13ج","ريتويت X 35ج"],
    "سناب شات - 13 خدمة": ["متابعين سناب 230ج","مشاهدات ستوري 370ج"],
    "ثريدز - 3 خدمات": ["متابعين ثريدز 40ج","لايكات ثريدز 60ج","لايكات ثريدز 45ج"],
    "فيسبوك - 59 خدمة": ["خدمات فيسبوك محفوظة"],
    "تيليجرام - 32 خدمة": ["خدمات تيليجرام محفوظة"],
}

async def start(update, context):
    kb=[[InlineKeyboardButton(k,callback_data=k)] for k in SERVICES.keys()]
    kb.append([InlineKeyboardButton("📞 يوجد خدمات أخرى - تواصل", url="https://t.me/youssef_alaidy")])
    await update.message.reply_text(f"متجر {ADMIN_USER} 👑\n252 خدمة ✅\nاختر:", reply_markup=InlineKeyboardMarkup(kb))

async def btn(update, context):
    q=update.callback_query; await q.answer()
    if q.data in SERVICES:
        await q.edit_message_text(f"📂 {q.data}\n\n{ADMIN_USER}\nيوجد خدمات أخرى للتواصل", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع",callback_data="back")]]))
    else:
        kb=[[InlineKeyboardButton(k,callback_data=k)] for k in SERVICES.keys()]
        await q.edit_message_text("اختر:",reply_markup=InlineKeyboardMarkup(kb))

async def fwd(update, context):
    await context.bot.send_message(chat_id=ADMIN_ID,text=f"طلب من @{update.effective_user.username}: {update.message.text}")
    await update.message.reply_text("تم ✅")

def main():
    app=Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CallbackQueryHandler(btn))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,fwd))
    app.run_polling()

if __name__=="__main__": main()
