from .app import create_app
app = create_app('dev')
@app.route("/")
def welcome(): 
    print("welcoming")
    return "welcome"
if __name__ == '__main__': 
    app.run()