from flask import Flask, jsonify
from playwright.sync_api import sync_playwright
from utils import filter_laptops_by_description

app = Flask(__name__)

@app.route('/laptops', methods=['GET'])
def get_laptops():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
        page.wait_for_load_state()
        laptops = page.query_selector_all('.col-sm-4.col-lg-4.col-md-4')
        laptop_data = []

        for laptop in laptops:
            name = laptop.query_selector('h4').text_content()
            description = laptop.query_selector('p.description').text_content()
            price = laptop.query_selector('h4.price').text_content().split()[0]
            price = price.replace('$', '')
            laptop_data.append({"name": name, "description": description, "price": price})

        browser.close()
        sorted_laptops = sorted(laptop_data, key=lambda x: float(x['price']))

        filtered_laptops = filter_laptops_by_description(sorted_laptops, 'Lenovo')
        return jsonify(filtered_laptops)


if __name__ == '__main__':
    app.run()
