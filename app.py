from app import create_app

#Creating the app instance
app = create_app('development')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9050)