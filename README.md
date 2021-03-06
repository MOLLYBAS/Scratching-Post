# Team Danger Noodles | Minnehack 2020 
![scratching post logo](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/logo1.png)

## Inspiration
**Prompt:**  *develop a solution for local communities to help them foster social good*

There are many local animal adoption shelters in Minneapolis and other cities.  Shown below are a small selection (image from [Google Maps](https://www.google.com/permissions/geoguidelines/))

![map of local shelters](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/map.png)

- These places provide **social good** by taking care of animals and providing a companion to people who adopt these pets.  Pets can provide [health benefits](https://www.cdc.gov/healthypets/health-benefits/index.html).

- The local **communities of volunteers** often create social media posts to advertise pets avaliable for adoption.  However, shelters are consistently [short on volunteers](https://www.wiscnews.com/wisconsindellsevents/news/local/volunteers-make-the-difference-animal-shelters-rely-on-support/article_3189845b-04ea-57cf-90df-2a48b279ddae.html).

- By helping automate content creation, posting can be done more frequently, which means that volunteers will have more time to spend taking care of animals, and more animals will be seen and have a chance at finding a new home.  This helps **foster social good and foster animals**.

## What it Does
Transforms images into posts, with [automatic Tweeting](https://twitter.com/AnimalExample), tagging, and captioning


## How it Works
![infographic](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/infographic1.png)
For use with a [low cost IoT device](https://www.adafruit.com/product/3414?gclid=EAIaIQobChMI2piJ2eWL3AIVlIWzCh0E-gACEAQYASABEgKhn_D_BwE), or any shelter photos.
Data is stored online using mongoDB, so trends can be seen
![catdogpiechart](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/pie.png)
![posts](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/posts.png)

## What's next for Scratching Post
- Build and test the hardware for a IoT Scratching Post Device
- Species specific post text
- Specific animal identification for including names in posts
- Testing at a local shelter

## Challenges we ran into
- The dataset used for animal pictures had varying image sizes, which led captions to sometimes be cut off.  The font size was decreased to mitigate this issue.  With an IoT device the camera resolution would be fixed and this would not be an issue, so it was left for now.

## What we learned
- We had never used Google cloud services, mongoDB,  or the Twitter API before.  We also learned/practiced some graphic design.

## Accomplishments that we're proud of
- We were really excited when we were able to see the photos correctly classified, and are proud of how much our small and somewhat new team was able to accomplish in the time given.

## How we Built it |  Technologies Used

 - Google Cloud Vision API label detection: to determine if a photo contains a dog or cat, get relevant hashtags
- [Oxford-IIIT pet dataset](https://www.tensorflow.org/datasets/catalog/oxford_iiit_pet):  for testing
- UiPath Data Scraping: to gather cat and dog puns from these websites:
	- https://www.rover.com/blog/cat-puns/
	- https://www.mydogsname.com/dog-puns/
- mongoDB to store tweet data, and supply data shown using Plotly
- Python Libraries/APIs
	- PyGame
	- Pymongo
	- Plotly
	- Twython
	- os, random, csv, datetime
- Icons free from Iconfinder
- Dog icon by [Icons8](https://icons8.com/icons/set/dog)
- Domain.com used to register scratchingpost.tech for future use

## Example Post
![tweet](https://github.com/MOLLYBAS/Scratching-Post/blob/master/assets/tweet.png)
## Captioned Images
### Cat
![cat_image](https://github.com/MOLLYBAS/Scratching-Post/blob/master/generated/2020-01-25%2023%3A07%3A08.558913.png)
## Doggo
![dog_image](https://github.com/MOLLYBAS/Scratching-Post/blob/master/generated/2020-01-26%2000:10:27.830547.png)
