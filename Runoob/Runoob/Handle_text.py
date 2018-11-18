import hashlib

from scrapy.utils.python import to_bytes
from w3lib.html import remove_tags, remove_tags_with_content
import re
from html.parser import unescape
from lxml import etree


def deal_html(html):
    # 处理菜鸟代码pre标签
    html = re.sub('<pre.*?>', '<code>', html).replace('</pre>', '</code>')
    HTML = etree.HTML(html)
    img_list = HTML.xpath('//img/@src')

    temp = remove_tags_with_content(html, ('script', 'iframe'))
    temp = remove_tags(temp, keep=('img', 'p', 'br', 'div', 'h1', 'h2', 'h3', 'code'))
    temp = re.sub('<p.*?>', '<br>', temp).replace('</p>', '<br>')
    temp = re.sub('<div.*?>', '<br>', temp).replace('</div>', '<br>')
    temp = re.sub('<h1.*?>', '<br>', temp).replace('</h1>', '<br>')
    temp = re.sub('<h2.*?>', '<br>', temp).replace('</h2>', '<br>')
    temp = re.sub('<h3.*?>', '<br>', temp).replace('</h3>', '<br>')
    temp = re.sub('<br.*?>', '<br>', temp)
    temp = unescape(temp)
    temp = temp.replace(u'\xa0', u'').replace(u'\ufeff', u'').replace('　', '')

    html_list = temp.split('<br>')
    html_list = [html for html in html_list if html]
    new_html = []
    for html in html_list:
        if '<code>' not in html and '<img' not in html:
            h = '<p>{}</p>'.format(html)
            new_html.append(h)

        else:
            new_html.append(html)

    new = ''.join(new_html)
    # for img in img_list:
    #     img_md5 = hashlib.sha1(to_bytes(img)).hexdigest()
    #     new = new.replace(img, img_md5)

    return new, img_list
