# 🌾 Yield Prediction Using Machine Learning

Прогноз урожайности на основе климатических данных и агрономических факторов с помощью машинного обучения.

## 📁 Состав проекта

- `crop_yield_dataset.csv` — обучающий датасет (температура, осадки, удобрения, тип почвы, культура)
- `train_model_corrected.py` — скрипт для обучения модели
- `app_bilingual.py` — веб-приложение с поддержкой русского 🇷🇺 и английского 🇬🇧 языков
- `requirements.txt` — список необходимых библиотек
- `README_INSTRUCTION.txt` — краткая инструкция по запуску

---

## 🔧 Установка

1. Установите Python 3.9+ с официального сайта: [https://python.org](https://python.org)  
   ⚠️ Обязательно включите опцию **"Add to PATH"** при установке!

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Обучение модели

1. Запустите обучение модели:
   ```bash
   python train_model_corrected.py
   ```
2. В результате будет создан файл `model.pkl` — сериализованная модель для предсказаний.

---

## 🌍 Запуск веб-приложения

1. Запустите приложение:
   ```bash
   python app_bilingual.py
   ```

2. Откройте в браузере:

- 🌐 Русская версия: [http://127.0.0.1:5050](http://127.0.0.1:5050)  
- 🌐 English version: [http://127.0.0.1:5050/en](http://127.0.0.1:5050/en)

---

## 🖼️ Интерфейс приложения

### 🔹 Ввод параметров (русская версия)


<p align="center">
  <img src="https://github.com/user-attachments/assets/2aa297db-0e52-4503-af57-2fc2db896d74" alt="Форма ввода - Русский">
</p>

---

### 🔹 Ввод параметров (английская версия)


<p align="center">
  <img src="https://github.com/user-attachments/assets/fdafb6cf-3d22-4988-bc60-86a1e54f1a02" alt="Форма ввода - English">
</p>

---

### 🔹 Результат предсказания + экспорт в PDF


<p align="center">
  <img src="https://github.com/user-attachments/assets/78e36e52-afe6-461c-8bda-9b68cef79a3e" alt="Результат прогноза урожайности">
</p>

---

## 📄 Возможности

- Двуязычный интерфейс 🇷🇺 / 🇬🇧
- Прогноз урожайности по введённым параметрам (температура, осадки, удобрения, тип почвы, культура)
- Поддержка экспорта результата в PDF
- Простота запуска и установки

---

## 🎓 Руководитель проекта

Научный руководитель: **Гончаров Роман Дмитриевич**
