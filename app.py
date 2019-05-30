from flask import Flask
import recommend
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/search/')
def search():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('search.html',Data=dic)

if __name__=="__main__":
    app.run(debug=True)
