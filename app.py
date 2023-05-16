from flask import Flask, render_template, request
import csv
app = Flask(__name__)

def checker(movie_name):
    with open('new_ratings.csv', 'r') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
        # Check if this is the row you're looking for
            if row[0] == movie_name:
                break
        return index

def change(genres, genre_ratings, movie_name):
    with open('new_ratings.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == movie_name:
                old_lst = row[0:]
        print(old_lst)
        rate = [int(r) for r in genre_ratings if r]
        dic = {'Action':2, 'Adventure':3, 'Sci-Fi':4, 'Drama':5, 'Comedy':6, 'Romance':7, 'Musical':8, 'War':9, 'Horror':10, 'History':11, 'Mystery':12, 'Thriller':13, 'Crime':14, 'Sport':15, 'Biography':16, 'Fantasy':17, 'Family':18, 'Documentary':19, 'Music':20, 'Animation':21, 'News':22, 'Western':23}
        dis = {}
        for c in range(len(genres)):
            dis[genres[c]] =format(float(old_lst[dic[genres[c]]])+ rate[c] / int(old_lst[25]),'.1g')
        new_lst = []
        print(dis)
        common_keys = set(dis.keys()) & set(dic.keys())  
        result = [dic[key] for key in common_keys] 
        print(result)
        for x in range(len(old_lst)):
            rx = old_lst[x]
            if x in result:
                r = result.index(x)
                print(r)
                rx = dis[list(dis.keys())[r]]
                print(rx)
            new_lst.append(rx)
        new_lst[25] = int(new_lst[25]) + 1
    return new_lst
def replacing(new_lst,movie_name):
    with open('new_ratings.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    y=checker(movie_name)
    rows.pop(y)
    rows.append(new_lst)
    with open('new_ratings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def Submit():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        overall_rating = request.form['overall_rating']
        genres = request.form.getlist('genres[]')
        genre_ratings = request.form.getlist('genre_ratings[]')
        new_lst=change(genres,genre_ratings,movie_name)
        replacing(new_lst,movie_name)
    return render_template('rated.html')

if __name__ == '__main__':
    app.run(debug=True,port=8900)
