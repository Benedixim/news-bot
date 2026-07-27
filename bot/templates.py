def news_message(news):

    return (
        f"🎓 <b>{news['title']}</b>\n\n"
        f"{news['summary']}\n\n"
        f"📅 <b>Дедлайн:</b> {news['deadline']}\n\n"
        f"🔗 {news['url']}"
    )