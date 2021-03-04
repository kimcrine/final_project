# Welcome to our [Housing Predictor Application](https://atlanta-housing.herokuapp.com/).

In this app, we will be building a simple machine learning model using the Metro Atlanta dataset.
![image](https://user-images.githubusercontent.com/70181086/110031592-1bd22f00-7d05-11eb-92f8-0b218aafdb02.png)

## Introduction

For our final project, we decided to do an analysis and run machine learning models on Atlanta real estate data. The data we used was the Zillow Real Estate Data on Quandl.com. We ran API calls to pull all available Zillow real estate data for all metro Atlanta zip codes. We created an app where users can enter the listing price of a house, the number of bedrooms, and the county the house is located in, and it will determine and show the estimated monthly rental price of the house.

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

For our project we decided to use Linear Regression. We wanted to make a useful tool for calculating possible rental income that took into account the initial cost of the property (in addition to location). Due to the relationship between purchase price and rent, we decided a Linear Regression would be an effective tool for predictions.

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

![image](https://user-images.githubusercontent.com/70181086/110039803-c51e2280-7d0f-11eb-9e92-0c8113f62033.png)

![image](https://user-images.githubusercontent.com/70181086/110039823-ccddc700-7d0f-11eb-833e-173a94f1a5bd.png)

![image](https://user-images.githubusercontent.com/70181086/110038684-11686300-7d0e-11eb-9858-717617f0fdbe.png)

![image](https://user-images.githubusercontent.com/70181086/110038702-188f7100-7d0e-11eb-8f7e-7d3c0abb41c1.png)


3) We found that there is a moderate negative correlation between the level of crime in a given zip code and the median listing price in the zip codes. This cause of this could either be due to less demand in higher crime areas, or due to the fact that zip codes with lower priced houses have fewer gated communities and less house security. 

![image](https://user-images.githubusercontent.com/70181086/110034987-1676e380-7d09-11eb-9ce4-6765cb869610.png)

![image](https://user-images.githubusercontent.com/70181086/110035033-255d9600-7d09-11eb-8d78-409cdc850469.png)

![image](https://user-images.githubusercontent.com/70181086/110038603-f138a400-7d0d-11eb-943b-d19d1ee44423.png)

![image](https://user-images.githubusercontent.com/70181086/110038620-f990df00-7d0d-11eb-8249-991dbaac5acc.png)


4) We found that there was not much of a change in the number of houses listed and the price-to-rent ratio in the zip codes where Turner Field and SunTrust are located during their closings and openings respectively.

![image](https://user-images.githubusercontent.com/70181086/110038751-2f35c800-7d0e-11eb-8f80-d9fc95ec066d.png)

![image](https://user-images.githubusercontent.com/70181086/110038771-365cd600-7d0e-11eb-859b-92cb4e2a7aea.png)

Suprisingly, we found that the median listing price in the zip code where Turner Field was located increased significantly from the time it closed to the most recent data point we had - from September 2016 to March 2018, the median listing price increased from $305,000 to $388,000. That is likely due to the overall growth of Atlanta and revitalization efforts of the area around Turner Field. During the same timeframe, the median listing price of the zip code where SunTrust park is located grew by a slightly less amount of $1,249,000 to $1,296,500, likely because it is already a highly developed area with some of the most lavish homes in Atlanta.

![image](https://user-images.githubusercontent.com/70181086/110039415-2e516600-7d0f-11eb-9de9-c192dc0f1030.png)

The number of listings with price cuts near SunTrust park showed a significant dip in the months before it opened. However, they showed a similar drop one year later. This indicates that the price cuts are likely seasonal rather than having anything due to the opening of the new stadium.

![image](https://user-images.githubusercontent.com/70181086/110039619-7ff9f080-7d0f-11eb-9684-19beb29c9baa.png)

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
