from parser.base import BaseParser


class OpportunitiesCornersParser(BaseParser):

    URL = "https://opportunitiescorners.com/"

    def parse(self):

        soup = self.get_soup(self.URL)

        cards = soup.find_all("div", class_="td_module_6")

        print(f"Найдено карточек Opportunities Corners: {len(cards)}")

        news = []

        for card in cards:

            link = card.find("h3", class_="entry-title").find("a")

            title = link.get_text(strip=True)
            url = link["href"]

            time_tag = card.find("time")
            published_at = (
                time_tag["datetime"]
                if time_tag
                else None
            )

            article = self.get_soup(url)

            paragraphs = article.find_all("p")

            text = "\n".join(
                p.get_text(" ", strip=True)
                for p in paragraphs
            )

            news.append({
                "title": title,
                "text": text,
                "url": url,
                "published_at": published_at
            })

        return news