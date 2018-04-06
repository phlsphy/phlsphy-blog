---
category: ''
date: 2018-04-06 12:00:00 UTC
description: ''
link: ''
slug: the-estate-got-real
tags: ''
title: The Estate got Real
type: text
---

# Pictures this...
A representative from a real estate company approaches us with this business case:
> Find me houses that we can buy on the cheap, renovate it, and then sell it for a profit.

"Ok. Do you have data?"

"Yes, we do. Here's the CSV file."

Let's break down what we have to do in order to fulfill our client's needs.
1. Find houses.
2. Find their worth.
3. Find out what we need to renovate to make the house a better sale.
4. Find out how much the real estate company can make from any renovation.

## Find them houses

We have a dataset of houses, their condition, their quality, their features (like how many bathrooms or kitchens they have), and the price that they were sold for. Thank the stars for the comprehansive data dictionary that details each and every column (all 80 of them) and what all the abbreviations mean. We'll go through it all and divide the features into two categories:
1. What can be renovated
2. What can't be renovated

The reason for this is two folds. We want to account for things that are not renovate-able. Things like neighbourhood, how big the houses are, how many bathrooms/kitchens it has, ceiling height, the shape of the house, the house type, etc. Once we have something that modelled these aspects of the houses, we can then look at stuff that can be renovated and then see what effects they had on the final sale price.

In all fairness, these things _can_ be renovated but it will cost an arm and a leg and the client specifically said "profit". We need to keep that in mind. 

## Straight as an arrow

A picture says a thousand words. So, here's a visual representation of the first part:
![](/assets/linear_regression.png)

The red line represents our linear model. It generalises the sale price from all of the historical data that we threw at it. 

The blue dots are the actual sale prices that the houses were sold for. Frankly, this is not predictive analysis, we are not exactly predicting anything. We are not predicting future sales prices. We just want to divide our data into two sides. We want to _model_ the ups and downs of house prices based on things that the real estate company cannot renovate. 

We can read it this way: For a house of N shape, N size, in N neighbourhood, the price of the house should be somewhere along the red line. But in reality, there are houses that sold for more and houses that sold for less.

![](/assets/two_sets.png)

Once we have accounted for things that we cannot renovate, we need to account for those that can. The difference between the red line and the blue dots would be due to features that _are_ renovate-able. Things like kitchen quality, bathroom condition, basement finish, type of roof, electricity supply, exterior wall material etc. 

![](/assets/price_difference.png)

Which makes sense in real life. A house might not be in the best neighbourhood, might be smaller than others, might be in an odd shape, but if the inside is top-notch, with a beautiful kitchen, lovely bathrooms, spacious configuration, modern heating and plumbing...it would sell better than if we take just neighbourhood, shape and size to value a property.

In mathematical terms, the difference is called the residual. The residuals will help us work on finding out what needs to renovate to make the house a better sale and to find out how much the real estate company can make from any renovation.

## 'Yes' and 'No'

If the first part used a linear regression model, the second part can be solved with a classification model. I'd say 'can' here because we can also use another linear regression model to do this part. But:
1. that would be boring
2. the classification model would give the client a simple "yes" or "no" output at the end
3. a linear regression model would rely on things like coefficients and short of giving our client a lesson on statistics and then ask for an invoice for our hardwork, they will fire us before we get to '...and this table here will show the coeff--" "No."

## Tale of two residuals

The residuals form a normal distribution. It is one of those mathematical magic that happens with residuals, so just take it that it this lovely bell curve occurs as is does. If we plot this and it doesn't make this shape, that probably means that a linear model is not the best choice to model the spread and scatter of the sales prices. With our residuals from all of our sales data, we can split the houses into two sets (yes, again). 

![](/assets/dividing_the_residuals.png)

For the Ames housing data, the median (the middle point of the sale prices) is $760. This comes from our linear model in part 1. We split the data right down the middle into the right hand side where the residual is positive (there's a potential for profit; "yes") and the left hand side where the residuals are negative values (total loss; "no"). From there, we have our "yes" and "no" labels. 

We swap over to our renovate-able features and we label each house as a "yes" or a "no". From there, we will use a classification model, using our renovate-able features, to produce an output of "yes" or "no" for an future houses that are introduced to the model. We will know then, what are the renovations that the client needs to do in order to produce a "yes" and which renovation does not have an effect. 

## Coeff--

We still rely on the coefficients of each feature in a classification model to tell us which feature to renovate and which not to. But instead of just a table containing a bunch of numbers, and letting the client figure it out, a classification model value adds in the output ("yes, this house might make monies", "no, don't even bother").

How we can further refine the product that we're gonna hand over to the client (and then collect our dues) is to divide the residuals in a more realistic manner.

![](/assets/dividing_residuals_irl.png)

The second cut off point of $10,000 can be any value, it need not be $10,000. It becomes a business decision, on the part of the real estate company, to decide the values of the other cut off points. This is also where we have to make sure that as data scientists/analysts/consultants, we don't get into a rabbit hole chasing after accuracy, precision, f1-score, and all these various out metrics for our model that we forget about the metrics of our clients. 

## Profit

In the real world out there, there will be times that the renovation cost will be higher than normal. If there was a sand shortage or cement shortage in the area, anything to do with cement or sand will cost waaaay more than normal. Glass and alternative materials like synthetic ceramics might be the better choice in those times. If we had gone with the regression model, it would be able to directly quantify the affects of...say, renovating the garage and putting in another roof type. Let's take an arbitrary number of $1,000 for the garage and $5,000 for the roof. In 6 months, there's no gurantee that $1,000 and $5,000 still hold true. Providing a budget and a list of features to renovate (provided by the classification model), the real estate company can make a decision if they can renovate whatever that needs renovating to the optimum quality and condition, _within_ the budget determined by the cut off points. 

Also, much of the modern payment schemes means that the real estate agent has to fork out upfront -- the cost of renovation (gotta pay the construction company)-- and then put the house up for sale. By keeping to a budget, it would take into account a housing downturn. If we had relied on the regression model, and it told us that the garage will net us $1,000 if we renovate it, but the cost of renovation is $500 and there was a housing downturn so we are definitely not getting the $1,000 that was expected, the model's prediction of $1,000 in sales would not hold true.

Using the classification model, we set a cut off point at $5,000. We had a budget of $2,500 (half of the cut off point), and we come under budget at $2,000, we are slightly better off even with a slight housing downturn. 

## 

Once we have both our models running and we have piped it into a lovely dashboard (I haven't learnt that much from the data science course yet, but I'll get there) for our client, we hand it over, give them one day of training, present the models that got us our numbers and output, we collect our ~cheque or~ bank transfer. 

If you reall want to dig into the data munging, cleaning, machine learning model tuning and are comfortable with .ipynb, you can go [here](https://github.com/phlsphy/GA-Projects/tree/master/project03). 

I wanted to give a high level overview of how I would approach such a business case. It was also Project 3 of the data science course that I am taking so please ignore the boring file names.

----
The housing data is the [Ames housing data](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) from Ames, Iowa. The dataset originally came from Dean De Cock (2011), "Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project", _Journal of Statistics Education_, 19(3), [available here](www.amstat.org/publications/jse/v19n3/decock.pdf). It is now currently widely used along with the Boston Housing dataset. The dataset comes with a comprehansive [data dictionary](https://ww2.amstat.org/publications/jse/v19n3/decock/datadocumentation.txt).