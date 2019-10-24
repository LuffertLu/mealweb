@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search/')
def search():
    n=request.args.get('user')
    dic=recommend.recommend(n)
    return render_template('search.html',Data=dic)
