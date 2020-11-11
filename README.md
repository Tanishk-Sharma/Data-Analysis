# Data Preparation

Data Peparation is an important step of any Data Science project life cycle.
It acts as a precursor to the Model Planning step. 
<p align="center"><img src="https://user-images.githubusercontent.com/32167236/98797542-b7782080-2432-11eb-9c34-c44e74f19022.png"></p>
Since in the model planning step we explore relationships in the dataset, we need a good dataset to begin with.

So, in the Data Preparation step, we perform different operations on the data so that our model can easily learn from it.

Even in my work life, I always catch data feeds having problems that need to be cleared in this step before moving on like:

* NULL values
* Misspelled headers
* Unreal values (out of bounds, for example, 500 m cannot be the height of a person :laughing:)
* Leading/Trailing whitespace
* Invalid values ("Random String" cannot be the price of a product.)

So. in this repo, we will deal with these issues and at the end of it we should have a good, clean dataset to build our model on! :)
