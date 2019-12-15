from Flask import Flask, jsonify, redirect, render_template
import pymongo
import scrape_mars

client = pymongo.MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)

db = client.mars_data_DB
mars_data = db.mars_data = mars_data['news_data']['paragraph_text_1']

@app.route("/")
def render_index():
    try:
        mars_find = mars_data.find_one()
        news_title = mars_data['news_data']['news_title']
        paragraph_text_1 = mars_data['news_data']['paragraph_text_1']
        paragraph_text_2 = mars_data['news_data']['paragraph_text_2']
        featured_image_url = mars_data['featured_image_url']
        mars_weather = mars_data ['mars_weather']
        mars_facts = mars_data ['factstable']
        hemi_title_1 = mars_data['mars_hemispheres'][0]['title']
        hemi_img_1 = mars_data['mars_hemispheres'][0]['img_url']
        hemi_title_2 = mars_data['mars_hemispheres'][1]['title']
        hemi_img_2 = mars_data['mars_hemispheres'][1]['img_url']
        hemi_title_3 = mars_data['mars_hemispheres'][2]['title']
        hemi_img_3 = mars_data['mars_hemispheres'][2]['img_url']
        hemi_title_4 = mars_data['mars_hemispheres'][3]['title']
        hemi_img_4 = mars_data['mars_hemispheres'][3]['img_url']

    except (IndexError, TypeError) as error_handler:

        news_title = ""
        paragraph_text_1 = ""
        paragraph_text_2 = ""
        featured_image_url = ""
        mars_weather = ""
        mars_facts = ""
        hemi_title_1 = ""
        hemi_img_1 = ""
        hemi_title_2 = ""
        hemi_img_2 = ""
        hemi_title_3 = ""
        hemi_img_3 = ""
        hemi_title_4 = ""
        hemi_img_4 = ""


return render_template("index.html", news_title = news_title,\
paragraph_text_1 = paragraph_text_1, paragraph_text_2 = paragraph_text_2,\
featured_image_url = featured_image_url, mars_weather = mars_weather,\
mars_facts = mars_facts, hemi_title_1 = hemi_title_1, hemi_img_1 = hemi_img_1,\
hemi_title_2 = hemi_title_2, hemi_img_2 = hemi_img_2, hemi_title_3 = hemi_title_3,\
hemi_img_3 = hemi_img_3, hemi_title_4 = hemi_title_4, hemi_img_4 = hemi_img_4)


@app.route('/scrape')
def scrape_mars_data():
    scrape_results = scrape_mars.scrape()
    mars_data.replace_one({}, scrape_results, upsert=True)
    return redirect('http://localhost:5000/', code=302)

if __name__=='__main__':
    app.run()