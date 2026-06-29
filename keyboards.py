from telegram import ReplyKeyboardMarkup

def main_menu():
    keyboard = [
        ["💰 Watch Ads"],
        ["👥 Referral", "💳 Withdraw"],
        ["🏆 Leaderboard", "👛 Wallet"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
