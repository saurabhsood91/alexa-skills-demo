from flask import Flask
from flask import jsonify
from flask_ask import Ask, statement, question, session
from flask import Flask, render_template

app = Flask(__name__)
app.config['ASK_VERIFY_REQUESTS'] = False
ask = Ask(app, '/')

WEATHER = {
    'San Francisco': '65',
    'Seattle': '80',
    'Los Angeles': '85'
}

@ask.launch
def launch():
    response = render_template('launch')
    return question(response)


@ask.intent("WeatherIntent")
def get_weather(city):

    previous_city = session.attributes.get('city', None)

    print previous_city

    if previous_city:
        difference = abs(int(WEATHER[city]) - int(WEATHER[previous_city]))

        response = render_template('weather_city_difference', city=city, previous_city=previous_city, difference=difference)

        session.attributes['city'] = city

        return question(response)

    response = render_template('weather', city=city, temperature=WEATHER[city])

    session.attributes['city'] = city

    return question(response)


if __name__ == '__main__':
    app.run(debug=True)
