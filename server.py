from flask import Flask

app = Flask(__name__)
task = "tesyt"

@app.route("/submit")
def submit():
    #convert task to string
    task2 = str(task)
    #write string to txt
    text_file = open("Output.txt", "w")

    text_file.write( task2)

    text_file.close()
    
    return "<p>Hello, World!</p>"

if __name__ == "__main__":

    app.run(host="127.0.0.1",port="5000",debug = True)