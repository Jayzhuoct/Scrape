import requests
from bs4 import BeautifulSoup


def scrape_interview_questions():
    base_url = 'https://woaijava.cc/mianshi/list/page?categoryId=1&page={}&flag=0'
    counter = 1  # 用于记录序号的计数器

    for page in range(0, 7):  # 循环遍历1到6的page值
        url = base_url.format(page)  # 格式化网址，将page值插入到占位符{}
        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        # 找到table标签
        table = soup.find('table')

        # 找到所有的tr标签
        rows = table.find_all('tr')

        # 遍历每个tr标签，获取第二个td标签的内容并输出
        for row in rows:
            cell = row.find_all('td')[1]  # 获取第二个td标签
            if cell.text != "题目":
                result = '# ' + str(counter) + '、' + cell.text + "\n" + '```' + "\n" + '```'  # 在结果前面拼接#、序号和题目内容
                print(result)  # 打印结果
                counter += 1  # 序号计数器递增


if __name__ == '__main__':
    scrape_interview_questions()
