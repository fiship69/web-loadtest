from locust import HttpUser, task, between
from bs4 import BeautifulSoup
import random

class PermutaUser(HttpUser):
    wait_time = between(3, 8)

    @task(3)
    def browse_home(self):
        self.client.get("/")

    @task(2)
    def browse_products(self):
        response = self.client.get("/")

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a")

            product_links = [
                link.get("href") for link in links
                if link.get("href") and "/producto/" in link.get("href")
            ]

            if product_links:
                random_link = random.choice(product_links)
                self.client.get(random_link)

    @task(1)
    def search(self):
        search_terms = ["auto", "casa", "iphone", "moto", "terreno"]
        random_search = random.choice(search_terms)

        self.client.get(f"/search?q={random_search}")
