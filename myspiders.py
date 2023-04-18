import copy
import scrapy


class BlogSpider(scrapy.Spider):

    name = 'blogspider'
    start_urls = ['https://www.freshersworld.com/jobs']
    def parse(self, response):
        jobArray = []

        jobData = {
            'jobTitle': '',
            'jobDescription': '',
            'postedDate': '',
            'companyName': '',
            'location': '',
        }

        for quote in response.css('.job-container'):
            jobData["jobTitle"] = quote.css(".seo_title::text").get()
            jobData["jobDescription"] = quote.css(".desc::text").get()
            jobData["postedDate"] = quote.css(".ago-text::text").get()
            jobData["companyName"] = quote.css(".latest-jobs-title::text").get()
            jobData["location"] = quote.css(".job-location::text").get()
            jobArray.append(copy.deepcopy(jobData))

        print(jobArray)