from bs4 import BeautifulSoup
import csv
import requests

r = requests.post("https://api.winebuff.com.hk/product")

if r.status_code != 200:
    raise Exception("Not success status code")

data = r.json()

soup = BeautifulSoup("""<table>
    <tr>
        <th>Name</th>
        <th>Colour</th>
        <th>Region</th>
        <th>Price</th>
        <th>Description</th>
    </tr>
</table>""", "html.parser")

for product in data['data']['products']:
    product_row = soup.new_tag("tr")

    name_tag = soup.new_tag('td')
    colour_tag = soup.new_tag('td')
    region_tag = soup.new_tag('td')
    price_tag = soup.new_tag('td')
    desc_tag = soup.new_tag('td')

    name_tag.string = product["name_en"]
    colour_tag.string = product["category_label"]
    region_tag.string = product["region"]
    price_tag.string = product["bprice"]
    desc_tag.string = product["description"]

    product_row.append(name_tag)
    product_row.append(colour_tag)
    product_row.append(region_tag)
    product_row.append(price_tag)
    product_row.append(desc_tag)

    soup.table.append(product_row)

    with open('r_text_6.html', 'w') as result:
        result.write(soup.prettify())