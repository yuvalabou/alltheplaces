from json import loads

from scrapy.http import Response

from locations.spiders.hyundai_gb import HyundaiGBSpider


class HyundaiPLSpider(HyundaiGBSpider):
    name = "hyundai_pl"
    allowed_domains = ["www.hyundai.com"]
    start_urls = ["https://www.hyundai.com/pl/pl/znajdz-dealera.html"]

    def extract_json(self, response: Response) -> list:
        js_blob = response.xpath('//div[@data-js-module="dealer-locator"]/@data-js-content').get()
        json_dict = loads(js_blob)
        return json_dict["dealers"]["pl"]