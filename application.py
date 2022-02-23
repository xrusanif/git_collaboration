from flask import Flask, request, render_template
from recommender import recommend_random, recommend_neighbors
from utils import movies, movie_title_search

# we instanciate the flask oject, (__name__) used to declare this file as the home script 
app = Flask(__name__)

# each view (or webpage) is defined by a function and app.route tells flask at which URL to render it
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/recommendations/')
def give_me_recommendations():
    # request gives us access to the URL arguments
    # print(request.args)
   
    # access each with different key variables
    # recs = request.args['movies']
    # dd1 = request.args['t']
    # dd2 = request.args['ia']
    # this method used for more than one movie with all the smae key varibale
    user_movies = request.args.getlist('movies')

    #uses our movie title search function from utils to match the exact title
    all_titles = movies.set_index('movieId')['title']
    matched_titles = [movie_title_search(user_movie, all_titles) for user_movie in user_movies]
    
    #get the movieIds to make user_dict and eventually user_vec
    matched_ids = [matched_title[0][2] for matched_title in matched_titles]
    
    #create user_dict to be used to make the uservector for our recommendations
    # user_query = dict(zip(matched_ids, len(user_movies)*[5]))
    
    # to do: create uservec with the user_dict data
    # make recommendation
    #recs = recommend_random(user_movies, movies)
    #pass recs to html and render
    return render_template('recommender_frontpage.html', matched_titles=matched_titles)



# ensures the code below is only executed when this file is directly run
if __name__=='__main__':
    # runs app and sets debug level on so that the errors are shows in the terminal
    # and the server restarts when any changes are made to this file!
    app.run(debug=True)
