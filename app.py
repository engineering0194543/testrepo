from flask import Flask, render_template
import random
app=Flask(__name__)

# list of birds
images=[
"https://raw.githubusercontent.com/engineering0194543/testrepo/main/1.jpg", 
 "https://raw.githubusercontent.com/engineering0194543/testrepo/main/2.jpg", 
 "https://raw.githubusercontent.com/engineering0194543/testrepo/main/3.jpg", 
 "https://raw.githubusercontent.com/engineering0194543/testrepo/main/4.jpg",
 "https://raw.githubusercontent.com/engineering0194543/testrepo/main/5.jpg" 
]

@app.route('/')
def index():
url=random.choice(images)
return render_template('index.html', url=url)

if __name__ == "__main__":
app.run(host="0.0.0.0")