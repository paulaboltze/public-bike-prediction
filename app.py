from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np
import datetime
from datetime import datetime
import sklearn



app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

wc_dict = {
            'Clear':[1,0,0,0,0,0,0,0,0,0,0,0,0], 
            'Cloudy':[0,1,0,0,0,0,0,0,0,0,0,0,0],
            'Fair': [0,0,1,0,0,0,0,0,0,0,0,0,0], 
            'Fog':[0,0,0,1,0,0,0,0,0,0,0,0,0],
            'Heavy Rain':[0,0,0,0,1,0,0,0,0,0,0,0,0], 
            'Heavy Rain Shower':[0,0,0,0,0,1,0,0,0,0,0,0,0],
            'Light Rain': [0,0,0,0,0,0,1,0,0,0,0,0,0],
            'Light Snowfall': [0,0,0,0,0,0,0,1,0,0,0,0,0],
            'Overcast': [0,0,0,0,0,0,0,0,1,0,0,0,0],
            'Rain': [0,0,0,0,0,0,0,0,0,1,0,0,0],
            'Rain Shower': [0,0,0,0,0,0,0,0,0,0,1,0,0],
            'Sleet': [0,0,0,0,0,0,0,0,0,0,0,1,0],
            'Thunderstorm': [0,0,0,0,0,0,0,0,0,0,0,0,1]
            }



day_dict = {'Friday':[1,0,0,0,0,0,0], 'Monday':[0,1,0,0,0,0,0],
           'Saturday': [0,0,1,0,0,0,0], 'Sunday':[0,0,0,1,0,0,0],
          'Thursday':[0,0,0,0,1,0,0], 'Tuesday':[0,0,0,0,0,1,0],
          'Wednesday': [0,0,0,0,0,0,1]}

# cols = ['hour', 'is_holiday', 'day_of_week']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    item = [x for x in request.form.values()]

    print(item)
    # hour, is_weekends, temp, rhum, wc, weekday 
    data = []
    data.append(int(item[0]))

    # calculate weekday and is_weekends

    day = datetime.today().strftime("%A")

    if (day == 'Sunday') or (day == 'Saturday'):
        is_weekends = True
    else:
        is_weekends = False


    data.append(is_weekends)

    temp = int(item[1])
    data.append(temp)

    rhum = int(item[2])
    data.append(rhum)

    data.extend(wc_dict[item[3]])

    data.extend(day_dict[day])


    print(data)



        
    # fri, mon, sat , sun, thu, tue, wed
    # data.extend(day_dict[item[2]])
    
   
    prediction = int(model.predict([data])[0])
    
    # postman begin

    # return 'the predicted total bike count :' + str(prediction) 

    # postman end
   


    return render_template('index.html',pred='Total Bike ride counts on at {}:00 Hrs will be {}'.format(item[0], prediction))



#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


if __name__ == "__main__":
    app.run(debug=True)