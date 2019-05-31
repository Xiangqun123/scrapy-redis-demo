import scrapy.cmdline

def main():
    scrapy.cmdline.execute(['scrapy','crawl','zhihu'])

if __name__ == '__main__':
    main()