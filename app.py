
from flask import Flask,render_template,request
import requests
import pickle

with open('model.pkl','rb') as f:
    model=pickle.load(f)

    


app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    try:
        city_name = 'Mumbai'
        API_key=''
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

        response= requests.get(url)
        if response.status_code == 200:
            data = response.json()
            wethr={
                'humidity':data['main']['humidity'],
                'temp':data['main']['temp'],
                'wind':data['wind']['speed']
            }
        return render_template('home.html',data=wethr)
    except: 
        return render_template('form.html')




@app.route('/form')
def form():
    return render_template('form.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch the input values from the form
        temp = float(request.form['Temp (C)'])
        dew_point_temp = float(request.form['Dew Point Temp (C)'])
        rel_hum = float(request.form['Rel Hum (%)'])
        wind_spd = float(request.form['Wind Spd (km/h)'])
        visibility = float(request.form['Visibility (km)'])
        stn_press = float(request.form['Stn Press (kPa)'])
    # Prepare the data for prediction
        input_data = [[temp, dew_point_temp, rel_hum, wind_spd, visibility, stn_press]]
        
        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Return result page with the prediction
        return render_template('result.html', predict=prediction)
    except ValueError:
        return "Invalid input. Please enter numeric values only."


@app.route('/weather')
def index():
    
    return render_template('weather.html')

@app.route('/weather_result', methods=['POST'])
def weather():
    city = request.form['city']
    
    API_KEY=''
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        weather_info = {
            "city": city,
            "temperature": data['main']['temp'],
            'feels_like':data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max':data['main']['temp_max'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed'],
            "description": data['weather'][0]['description'].capitalize(),
            'clouds_all': data['clouds']['all']

        }
        return render_template('weather_result.html', weather=weather_info)
    
    else:
        error_message = f"City '{city}' not found!"
        return render_template('weather.html', error=error_message)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
