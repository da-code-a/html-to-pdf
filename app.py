from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64

def send_devtools(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if 'status' in response:
     raise Exception(response.get('value'))
    return response.get('value')

def get_pdf_from_html(content, print_options = {}):
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument('--no-sandbox')
    webdriver_options.add_argument('--disable-dev-shm-usage')
    webdriver_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome("chromedriver", options=webdriver_options)

    driver.get("data:text/html;charset=utf-8," + content)

    calculated_print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
    }
    calculated_print_options.update(print_options)
    result = send_devtools(driver, "Page.printToPDF", calculated_print_options)
    driver.quit()
    return base64.b64decode(result['data'])

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/pdf', methods=['POST'])
def return_pdf():
    html_content = request.data or b''
    html_content = html_content.decode()
    response = get_pdf_from_html(html_content)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)