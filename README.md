# Welcome to our [Housing Predictor Application](https://atlanta-housing.herokuapp.com/).

In this app, we will be building a simple machine learning model using the Metro Atlanta dataset.
![image](https://user-images.githubusercontent.com/70181086/110031592-1bd22f00-7d05-11eb-92f8-0b218aafdb02.png)

## Introduction

For our final project, we decided to do an analysis and run machine learning models on Atlanta real estate data. The data we used was the Zillow Real Estate Data on Quandl.com. We ran API calls to pull all available Zillow real estate data for all metro Atlanta zip codes. We created an app where users can enter the listing price of a house, the number of bedrooms, and the zip code the house is located in, and it would determine and show the estimated monthly rental price of the house.

## Cleaning Process

We then proceeded to clean the data using Python within Jupyter Notebooks. Cleaning involved removing rows with null values, changing column names, and merging the Zillow data with other datasets including Atlanta census data and Atlanta crime data.

## Questions Asked 

After cleaning, we analyzed the data to answer various questions. The questions we attempted to answer and visualize were:

1) What are the median sales prices and median rental prices for each county, city, and zip code in the Atlanta metro area? Which are the highest? Which are the lowest?
2) What is the correlation between the percentages of minorities in a zip code and home sales prices and rental prices?
3) What is the correlation between crime in a zip code and home sales prices and rental prices?
4) What effect does an event like Turner Field closing and SunTrust Park opening have on home prices in those areas?
5) How do things like square footage and number of bedrooms correlate with the rental prices?

## Machine Learning Model

For our project we decided to use Linear Regression. We chose this model because it was the most accurate model with our data with the highest r2 score.

## Findings

1) We used Tableau to visualize median house sales prices and rental prices for each zip code in the Atlanta metro area. We found that the city is basically split in half in terms of housing prices with most of the northern metro having above-average house sales and rental prices and most of the southern metro having below-average house sales and rental prices. 

![image](https://user-images.githubusercontent.com/70181086/110032222-e37f2080-7d05-11eb-878f-c301b0ca51a3.png)

![image](https://user-images.githubusercontent.com/70181086/110032307-fd206800-7d05-11eb-9da3-d530c0dbb08f.png)

The county with the highest median sales price is Fayette county at $266,663. The county with the lowest median sales price is Clayton county at $74,763. 

![image](https://user-images.githubusercontent.com/70181086/110032463-2a6d1600-7d06-11eb-891d-bf1899c545e5.png)


The cities with the highest median sales prices are Alpharetta, Roswell, and Peachtree City at $345,890, $335,513, and $325,960 respectively. 

![image](https://user-images.githubusercontent.com/70181086/110032537-3f49a980-7d06-11eb-93d0-eea76950c028.png)


The cities with the lowest median sales prices are all in Clayton county - Riverdale, Forest Park, and Conley at $72,858, $47,050, and $27,000 respectively. 

![image](https://user-images.githubusercontent.com/70181086/110032614-55f00080-7d06-11eb-860d-59323281d783.png)


The zip code with by far the highest median sales price is 30327 which covers West Buckhead at $709,450. The zip code with the lowest median sales price is 30288 which covers the city of Conley at $27,000.

2) We found that there is a moderate negative correlation between the percentage of minorities in a given zip code and the median sales prices and rental prices of houses in the zip code, meaning the higher the percentage of minorities in the zip code, the lower the median sales price or rental price of houses in the zip code on average. In addition, we found that zip codes that are majority minorities median sales price was over $110,000 less than zip codes that are majority whites - $151,775 majority minorities vs. $264,000 for majority whites. Similarly, zip codes that are majority minorities have median rental prices much lower on average than zip codes that are majority white - $1,395 and $1,800 respectively.

![image](https://user-images.githubusercontent.com/70181086/110032748-833cae80-7d06-11eb-9fc3-34d7e317caf1.png)

![image](https://user-images.githubusercontent.com/70181086/110032769-8899f900-7d06-11eb-84b4-2b766606045d.png)

![Correlation_Between_%_Minority_and_Median_Sales_Price](https://user-images.githubusercontent.com/70181086/110036393-edefe900-7d0a-11eb-83bb-9ad0cde6a34b.png)


![image](https://user-images.githubusercontent.com/70181086/110033263-2d1c3b00-7d07-11eb-8349-20b01653b865.png)

3) We found that there is a moderate negative correlation between the level of crime in a given zip code and the median listing price in the zip codes. This cause of this could either be due to less demand in higher crime areas, or due to the fact that zip codes with lower priced houses have fewer gated communities and less house security. 

![image](https://user-images.githubusercontent.com/70181086/110034987-1676e380-7d09-11eb-9ce4-6765cb869610.png)

![image](https://user-images.githubusercontent.com/70181086/110035033-255d9600-7d09-11eb-8d78-409cdc850469.png)

![image](https://user-images.githubusercontent.com/70181086/110035158-4aea9f80-7d09-11eb-81e9-ad4658a28483.png)

![image](https://user-images.githubusercontent.com/70181086/110035096-37d7cf80-7d09-11eb-8a11-0d7e7052d27b.png)

4) We found that there was not much of a change in the number of houses listed and the price-to-rent ratio in the zip codes where Turner Field and SunTrust are located during their closings and openings respectively.



5) We found that number of bedrooms strongly correlated with the Rent Price. Square footage had a small correlation, and Days on Zillow did not correlate very much at all with the rent price.

![image](https://user-images.githubusercontent.com/70181086/110033328-40c7a180-7d07-11eb-9519-fa8e1fafb78b.png)

![image](https://user-images.githubusercontent.com/70181086/110033384-4fae5400-7d07-11eb-9f57-d5f977f3dddc.png)

![image](https://user-images.githubusercontent.com/70181086/110033411-576df880-7d07-11eb-91d4-1e47e19623a0.png)


## Conclusions & Challenges

* As much data as Zillow has, when you zoom in past region, it shows gaps. Some features don’t return any results when searched by zip code, like foreclosures per 10,000 homes, or days on ZIllow. Other features are present for some zip codes but not others, like number of monthly listings. When viewing features by zip code and date, some return lots of relevant data (2003 - 2020), while other zip codes only return one year (2018-2019) or much older dates (1984-1997).

* The Zillow data was only available on a county or zip code level, so trying to combine that with data on a latitude/longitude level became a challenge. We were able to work around this using proxy map layers for now.

## The Team
* [Greg Atkinson](https://www.linkedin.com/in/atkingn67/) - Turner vs Suntrust Tableau visualizations
* [Kim Crine](https://www.linkedin.com/in/kim-crine-2701a386/) - Atlanta Crime Tableau visualizations, Github controller, Heroku deployment
* [Grant Hicks](https://www.linkedin.com/in/grant-hicks-58807383/) - Minorities vs Sale/Rental Price Tableau visualizations
* [Jessica Layne](https://www.linkedin.com/in/jessica-layne/) - Data Insights with Matplotlib and sklearn models
* [Richard Philipose](https://www.linkedin.com/in/richard-phillips-b48716ba/) - Web app development and ML integration
* [Cory Russell](https://www.linkedin.com/in/cory-a-russell-9503481b5/) - Machine learning model to predict rental prices
