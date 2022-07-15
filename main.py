from website import create_app

app = create_app()

if __name__ == '__main__': # only if we run this file will the line below execute
    app.run(debug=True) # runs flask app, starts web server, automatically reruns webserver if changes are made


#https://www.youtube.com/watch?v=dam0GPOAvVI
