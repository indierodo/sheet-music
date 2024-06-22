import jinja2
import os

TEMPLATE_LOADER = jinja2.FileSystemLoader( searchpath="./templates" )
TEMPLATE_ENV = jinja2.Environment( loader=TEMPLATE_LOADER )

def create_english_webpage(scores):
    template_file = "en.jinja"
    template = TEMPLATE_ENV.get_template( template_file )
    template_vars = {
        "language": "en",
        "title": "indierodo's sheet music",
        "fork_me": "Fork me on GitHub",
        "scores": scores
    }
    with open("./site/index.html", mode="w", encoding="utf-8") as file:
        file.write(template.render(template_vars))

def create_spanish_webpage(scores):
    template_file = "es.jinja"
    template = TEMPLATE_ENV.get_template( template_file )
    template_vars = {
        "language": "es",
        "title": "partituras de indierodo",
        "fork_me": "Haz un fork en GitHub",
        "scores": scores
    }
    with open("./site/es.html", mode="w", encoding="utf-8") as file:
        file.write(template.render(template_vars))

def create_privacy_webpage():
    template_file = "privacy.jinja"
    template = TEMPLATE_ENV.get_template( template_file )
    template_vars = {
        "language": "en",
        "title": "indierodo's sheet music",
        "fork_me": "Fork me on GitHub"
    }
    with open("./site/privacy.html", mode="w", encoding="utf-8") as file:
        file.write(template.render(template_vars))

def title_case(s):
    return ' '.join([
        word.replace(word[1], word[1].upper(), 1) if word[0] == '(' else word.replace(word[0], word[0].upper(), 1)
        for word in s.split(' ')
])

def format_name(file):
    name = file.replace('.mscz', '').replace('_', ' ')
    return title_case(name)

def get_scores():
    scores = []
    for _, _, files in os.walk('./scores'):
        for file in files:
            if file.endswith('.mscz'):
                scores.append({'mscz': file,
                               'pdf': file.replace('.mscz', '.pdf'),
                               'name': format_name(file)})
    
    return scores

def main():
    scores = get_scores()
    create_english_webpage(scores)
    create_spanish_webpage(scores)
    create_privacy_webpage()

if __name__ == "__main__":
    main()