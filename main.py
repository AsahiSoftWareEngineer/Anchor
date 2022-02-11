from bottle import route, template, run, static_file
import os
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

JSON_DIR =  os.path.join(BASE_DIR, "Controller")

@route('/static/css/<filename:path>')
def send_static(filename):
    """静的ファイルを返す
    """
    return static_file(filename, root=f'{STATIC_DIR}/css')



@route('/<url>')
def Main(url):
    routingData = []
    viewData = []
    viewName = ""
    templateName = ""
    contentFile = ""
    with open(f'{JSON_DIR}/routing.json', mode='r', encoding='utf-8') as routefile:
       data = json.load(routefile)
       routingData = data["route"]
    
    with open(f'{JSON_DIR}/views.json', mode='r', encoding='utf-8') as viewfile:
       data = json.load(viewfile)
       viewData = data["views"]
       
    for i in routingData:
        if (url == i["url"]):
            viewName = i["view"]
    
    for i in viewData:
        if (str(viewName) == str(i["name"])):
            templateName = i["template"]
            print("------------")
            contentFile = i["content_file"]
            

            
    fileUrl = str(JSON_DIR) + "/" + str(contentFile)
    print("=======here=http")
    print(fileUrl+"44")
    with open (fileUrl, 'r') as file:
        data = json.load(file)
        print(data)
        backData = data["content"]
    return template(templateName, backData)

run(host='localhost', port=8000, debug=True)


