from flask import Flask,render_template,request
import recommend
manage=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('search.html',Data=dic)

if __name__=="__main__":
    manage.run(debug=True)
