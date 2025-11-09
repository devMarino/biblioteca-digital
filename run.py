from app import create_app #import create app in folder app

app = create_app() #calling create_app function in folder app

if __name__ == '__main__':
    app.run(debug=True) #start app