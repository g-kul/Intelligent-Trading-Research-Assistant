from abc import ABC, abstractmethod
import asyncio
import aiohttp


class Basescraper(ABC):
    def __init__(self, delay=1.0):
        self._delay = delay

    async def fetch(self, url, session):
        try:
            await asyncio.sleep(self._delay)

            async with session.get(url) as response:
                if response.status == 200:
                    html_body = await response.text()
                    return html_body
                else:
                    print(f"Error: {url} returned status {response.status}")

        except Exception as e:
            print(f"Exception fetching {url}:{e}")
            return None

    @abstractmethod
    def parse(self, html_content):
        """Input: Raw HTML string
        Output: A dictionary or object with {title,content,date}
        """
        pass
