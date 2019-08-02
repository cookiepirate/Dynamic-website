from flask import Flask, render_template, request


app = Flask(__name__)


 


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-asset', methods =['GET', 'POST'])
def asset():
    if request.method == "GET":
        return render_template('asset.html')
    else:
        print(request.form)
        return "Asset added Successfully"
        # return render_template('index.html')
        




@app.route('/add-task', methods = ['GET', 'POST'])   
def task():
    if request.method == "GET":
        return render_template('task.html')
    else:
        print(request.form)
        return "POST"




@app.route('/assets/all', methods = ['GET', 'POST'])
def allassets():
    if request.method == "GET":
        return render_template('')  ####
    else:
        return "GET"



@app.route('/add-worker', methods = ['GET', 'POST'])
def workers():   
    if request.method == "GET":
        return render_template('workers.html')
    else :
        print(request.form)
        return "POST"    

@app.route('/admin' )
def admin():
    return render_template('admin.html')



@app.route('/allocate-task')
def allocate():
    return render_template('')

@app.route('/get-tasks-for-worker')
def getask():
    return render_template('')    


if __name__ == "__main__":
    app.run(port=8000, debug=True)
