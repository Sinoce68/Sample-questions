from bs4 import BeautifulSoup as soup
from requests import get
from googlesearch import search


def main(lesson,type_lesson):
    term = "نمونه سوالات " + lesson + " " + type_lesson
    result = {}
    class_link = "season-box sp-bg-white sp-pointer sp-rp-4 sp-center sp-mt-4 sp-transition"
    res = search(term,num_results=2,sleep_interval=2)

    for l in res:
        if l.startswith("https://paadars.com/"):
            html_site = get(l).text
            app = soup(html_site, "html.parser")
            a_tags = app.find_all("li",attrs={"class":class_link})
            for tag in a_tags:
                link_download = tag.a.get("href")
                description = tag.a.getText().strip()
                result[description] = link_download
            for key in result:
                print(key)
                print(result[key])
                print("="*20)
                print()

if __name__ == "__main__":
    main(input("Example: ریاضی نهم,علوم هفتم\nEnter Lesson:"), input("Example: ترم اول,درس دو,...\nEnter TypeLesson:"))