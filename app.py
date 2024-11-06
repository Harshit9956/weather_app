from flask import Flask,render_template
# import requests

# city_name = 'Pune'
# API_key=
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

# response= requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     print(data['weather'][0]['description'])
#     print('current temperature is',data['main']['temp'])
#     print('current temperature Feels like  is ',data['main']['feels_like'])
#     print('Humidity is',data['main']['humidity'])


    


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
