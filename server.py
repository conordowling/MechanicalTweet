from flask import Flask, render_template,redirect
from db_config import *
app = Flask(__name__)

@app.route('/')
def random_tweet():
	random_topic = list(db.topics.aggregate(
		[{
			"$sample": { "size": 1 }		
		}]
	)[0]["name"]
    return redirect("/" + name) 

@app.route('/<topic>')
def topic_tweet(topic):
	tweet = list(db[topic].aggregate(
		[{
			"$sample": { "size": 1 }		
		}]
	))[0]
	return render_template(
		"tweet_classifier.html", 
		tweet = tweet,
		user="admin",
		topic = topic
	)


@app.route("/<topic>/label/<user>/<tweet>/<label>")
def label_tweet(topic, user, tweet, label):
	# maybe consider verifying inputs
	# create new label record
	label = {
		"user":user,
		"tweet":tweet,
		"label":label,
		"topic":topic
	}
	label_id = label_db.insert(label)
	# update user
	user_db.update({ "_id": user}, {"$push": { "labels": label_id }})
	# update tweet
	db.topic.update({ "_id": tweet}, {"$push": { "labels": label_id }})

	return redirect("/" + topic)