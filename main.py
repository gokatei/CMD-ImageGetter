import argparse
import re
import os
import datetime
from icrawler.builtin import BingImageCrawler

def checkPathText(path):
    pattern = r'[\\/:*?"<>|\s]'
    sanitized_path = re.sub(pattern, '-', path)
    return sanitized_path

def main(args):
    dtNOW = datetime.datetime.now()
    os.makedirs(os.path.join(args.output, dtNOW.strftime('%Y-%m-%d_%H-%M-%S') + '-' + checkPathText(args.keyWord)))

    print(os.path.join(args.output, dtNOW.strftime('%Y-%m-%d_%H-%M-%S') + '-' + checkPathText(args.keyWord)))
    crawler = BingImageCrawler(storage = {'root_dir' : os.path.join(args.output, dtNOW.strftime('%Y-%m-%d_%H-%M-%S') + "-" + checkPathText(args.keyWord))})
    crawler.crawl(keyword = args.keyWord, max_num = int(args.length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CMD-ImageGetter')
    parser.add_argument('keyWord', help='search key words')
    parser.add_argument('-l', '--length', help='search volume', default=100)
    parser.add_argument('-o', '--output', help='set output directory', default='./output')
    args = parser.parse_args()

    print(args)
    main(args)