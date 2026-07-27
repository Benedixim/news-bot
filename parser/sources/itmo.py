from parser.base import BaseParser


class ITMOParser(BaseParser):

    URL = "https://news.itmo.ru/ru/"

    def parse(self):

        soup = self.get_soup(self.URL)

        news = []

        # ---------- Главная новость ----------
        accent = soup.select_one("div.accent")

        if accent:

            link = accent.select_one("h3 a")

            if link:

                href = link.get("href")

                if href.startswith("/"):
                    href = "https://news.itmo.ru" + href

                news.append(
                    {
                        "title": link.text.strip(),
                        "text": self.parse_article(href),
                        "url": href,
                        "published_at": ""
                    }
                )

        # ---------- Остальные новости ----------

        cards = soup.select("ul.triplet li")

        print(f"Найдено карточек: {len(cards)}")

        for card in cards:

            link = card.select_one("h4 a")

            if link is None:
                continue

            href = link.get("href")

            if href.startswith("/"):
                href = "https://news.itmo.ru" + href

            time = card.select_one("time")

            published = ""

            if time:
                published = time.get("datetime", "")

            print("Скачиваю:", href)

            text = self.parse_article(href)

            news.append(
                {
                    "title": link.text.strip(),
                    "text": text,
                    "url": href,
                    "published_at": published
                }
            )

        return news
    
    def parse_article(self, url):

        soup = self.get_soup(url)

        article = soup.select_one("article")

        if article is None:
            return ""

        paragraphs = article.select("p")

        text = []

        for p in paragraphs:

            value = p.get_text(" ", strip=True)

            if value:
                text.append(value)

        return "\n".join(text)