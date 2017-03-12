from app import app

if os.environ.get('APP_LOCATION') == 'heroku':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    app.run(debug=True, host='0.0.0.0')
