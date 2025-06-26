from flask import Flask, request, render_template_string, redirect, url_for
import pandas as pd
import pickle

app = Flask(__name__)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

TEMPLATES = {
    "ru": {
        "title": "Прогноз урожайности | Саратовский ГАУ",
        "form_title": "Прогноз урожайности",
        "student_label": "ФИО студента:",
        "temp_label": "Температура (°C):",
        "rain_label": "Осадки (мм):",
        "fert_label": "Удобрения (кг/га):",
        "soil_label": "Тип почвы:",
        "crop_label": "Культура:",
        "submit": "Предсказать",
        "result": "Прогноз урожайности: {} т/га",
        "supervisor": "Научный руководитель: Гончаров Роман Дмитриевич",
        "switch": "English version",
        "route": "/en"
    },
    "en": {
        "title": "Crop Yield Prediction | Vavilov Agricultural University",
        "form_title": "Crop Yield Prediction",
        "student_label": "Student name:",
        "temp_label": "Temperature (°C):",
        "rain_label": "Rainfall (mm):",
        "fert_label": "Fertilizer (kg/ha):",
        "soil_label": "Soil type:",
        "crop_label": "Crop:",
        "submit": "Predict",
        "result": "Predicted yield: {} t/ha",
        "supervisor": "Supervisor: Goncharov Roman Dmitrievich",
        "switch": "Русская версия",
        "route": "/"
    }
}

def render_interface(lang="ru", prediction=None):
    t = TEMPLATES[lang]
    html = f"""
<!doctype html>
<html lang='{lang}'>
<head>
  <meta charset='UTF-8'>
  <title>{t["title"]}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: url('https://www.vavilovsar.ru/images/slide/1.jpg') no-repeat center center fixed;
      background-size: cover;
      margin: 0;
    }}
    .overlay {{
      background-color: rgba(255, 255, 255, 0.95);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }}
    .form-container {{
      background: #ffffff;
      padding: 30px;
      border: 2px solid #003366;
      border-radius: 12px;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
      width: 460px;
      text-align: center;
    }}
    h2 {{
      color: #003366;
      margin-bottom: 10px;
    }}
    label {{
      display: block;
      margin-top: 10px;
      margin-bottom: 5px;
      font-weight: bold;
      text-align: left;
    }}
    input[type=text], select {{
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 6px;
      box-sizing: border-box;
    }}
    input[type=submit], button {{
      background-color: #003366;
      color: white;
      padding: 10px;
      margin-top: 15px;
      border: none;
      border-radius: 6px;
      width: 100%;
      cursor: pointer;
      font-size: 16px;
    }}
    input[type=submit]:hover, button:hover {{
      background-color: #002244;
    }}
    .result {{
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      color: #333;
    }}
    .footer {{
      font-size: 13px;
      margin-top: 15px;
      color: #555;
      text-align: left;
    }}
    img.logo {{
      max-width: 100px;
      margin-bottom: 10px;
    }}
    .lang {{
      margin-top: 10px;
      font-size: 14px;
    }}
  </style>
  <script>
    function downloadPDF() {{
      window.print();
    }}
  </script>
</head>
<body>
  <div class="overlay">
    <div class='form-container'>
      <h2>{t["form_title"]}</h2>
      <form method='post'>
        <label>{t["student_label"]}</label>
        <input type='text' name='student_name' required>

        <label>{t["temp_label"]}</label>
        <input type='text' name='temperature' required>

        <label>{t["rain_label"]}</label>
        <input type='text' name='rainfall' required>

        <label>{t["fert_label"]}</label>
        <input type='text' name='fertilizer_amount' required>

        <label>{t["soil_label"]}</label>
        <select name='soil_type'>
          <option value='Чернозем'>Чернозем / Chernozem</option>
          <option value='Суглинок'>Суглинок / Loam</option>
          <option value='Песчаная'>Песчаная / Sandy</option>
        </select>

        <label>{t["crop_label"]}</label>
        <select name='crop'>
          <option value='Пшеница'>Пшеница / Wheat</option>
          <option value='Кукуруза'>Кукуруза / Corn</option>
          <option value='Подсолнечник'>Подсолнечник / Sunflower</option>
        </select>

        <input type='submit' value='{t["submit"]}'>
      </form>
      {f"<div class='result'>{t['result'].format(prediction)}</div>" if prediction else ""}
      {f"<button onclick='downloadPDF()'>Export to PDF</button>" if prediction else ""}
      <div class='footer'>{t["supervisor"]}</div>
      <div class='lang'><a href='{t["route"]}'>{t["switch"]}</a></div>
    </div>
  </div>
</body>
</html>
"""
    return html

@app.route("/", methods=["GET", "POST"])
def index_ru():
    prediction = None
    if request.method == "POST":
        prediction = handle_prediction()
    return render_template_string(render_interface("ru", prediction))

@app.route("/en", methods=["GET", "POST"])
def index_en():
    prediction = None
    if request.method == "POST":
        prediction = handle_prediction()
    return render_template_string(render_interface("en", prediction))

def handle_prediction():
    temp = float(request.form["temperature"])
    rain = float(request.form["rainfall"])
    fert = float(request.form["fertilizer_amount"])
    soil = request.form["soil_type"]
    crop = request.form["crop"]
    input_df = pd.DataFrame([{
        "temperature": temp, "rainfall": rain, "fertilizer_amount": fert,
        "soil_type": soil, "crop": crop
    }])
    input_encoded = pd.get_dummies(input_df)
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_features]
    pred = model.predict(input_encoded)[0]
    return round(pred, 2)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
