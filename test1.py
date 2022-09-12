import requests
from lxml import html

response = requests.get("https://docs.oracle.com/en-us/iaas/Content/Events/Reference/eventsproducers.htm")
tree = html.fromstring(response.text)

#services_with_events = tree.xpath('//div[@class="vl-content vl-content-max-width"]/article/article[@id="Services_that_Produce_Events"]/div//ul/li/a/span/text()')
services_with_events = tree.xpath('//div[@class="vl-content vl-content-max-width"]/article/article[@id="Services_that_Produce_Events"]/div//ul/li')

for service in services_with_events:
    serviceList = service.xpath('./a/@href')
    if len(serviceList) > 0:
        service = serviceList[0].split("#")
        if (len(service) > 1): 
            print(service[1])

            path = '//div[@class="vl-content vl-content-max-width"]/article/article[@id="Services_that_Produce_Events"]/article[@id="%s"]'%(service[1])
            events = tree.xpath(path)

            print(events[0].xpath('./h2/text()'))
            sections = events[0].xpath('./div/section')

            for section in sections:
                print(section.xpath('./@id'))
                table_rows = section.xpath('./div/table/tbody/tr')
                for row in table_rows:
                    name = row.xpath('./th/text()')
                    event = row.xpath('./td/div/pre/code/text()')
                    n = ""
                    e = ""
                    if len(name) > 0:
                        n = name[0]
                    if len(event) > 0:
                        e = event[0]
                    print(n + ": " +e)
