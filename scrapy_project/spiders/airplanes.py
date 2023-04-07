import scrapy


class AirplanesSpider(scrapy.Spider):
    name = "airplanes"
    
    def start_requests(self):
        url = "https://www.airliners.net/search?keywords={}&photoCategory=39&sortBy=dateAccepted&sortOrder=desc&perPage=84&display=detail&page={}"
        for manuf in ["boeing+737","airbus+a320"]:
            for i in range(1, 3):
                yield scrapy.Request(url.format(manuf, i))
                
    def parse(self, response):
        raw_image_urls = response.xpath('//img[@class="lazy-load"]/@src').getall()
        new_image_urls = []
        for img_url in raw_image_urls:
            splited_url = img_url.split("-")
            new_url = splited_url[0]+".jpg?v="+splited_url[1]
            new_image_urls.append(new_url)

        text = response.xpath('//div[contains(@class, "ps-v2-results-display-detail-col photo")]//div[@class="ps-v2-results-col ps-v2-results-col-aircraft"]//div[@class="ps-v2-results-col-content-primary"]/div[2]/a/text()').getall()
        normalized_text = [i.replace("\n","").replace(" ","").replace("/","-") for i in text]
        
        for i in zip(new_image_urls, normalized_text):
            yield {
                "image_urls" : [i[0]],
                "text" : i[1]
                }
