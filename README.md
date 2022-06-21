# Steak Doneness Classifier using AI
# Introduction
Hello, everyone! My name is Pattanun Wattanacheevakosol and I am a Thai student studying in 11th Grade from the AI Builders community, a community where people who are interested in AI share ideas, knowledge, and code. I have been granted access to join the community and as an assignment, I decided to deploy a model where it can determine the doneness of a steak (via an image) using AI. This is my first ever AI model and I have no experience in machine learning beforehand. So without further ado, here is the model!
# Drawing Board + Inspiration
So of course before deploying the model, I have to think of what kind of model should I do and what topic should it be. I thought about everything from video games to science, then I have an idea! I noticed that my parents especially my mom are really wary on the cook and doneness of their meat when they order a dish. My mom likes her steak well done and if there is a little pink inside the steak, she sends it back to the chef immediately. I said to myself, why not do a model which can determine the doneness or cook on the steak? With inspiration from my parents, I decided to start coding the steak doneness classifier AI.
# Failing the Initial Project
Before coming up with the steak project. I decided to do a results prediction model from a video game tournament called Minecraft Championship. Unfortunately, the data size was way too small containing only a few thousand scores for every tournament participator. I tried to bring up the model accuracy but my attempts were futile. Thus, I decided to change my project from Minecraft Championship to steak doneness classifier with only 2 weeks til due date.
# Steak Doneness Scale
- rare (125 degrees Fahrenheit)
- medium rare (135 degrees Fahrenheit)
- medium (145 degrees Fahrenheit)
- medium well (150 degrees Fahrenheit)
- well done (160 degrees Fahrenheit)

# Collecting and Cleaning Dataset
Before we can train our model, we need to have a train/test dataset first. I proceeded to research and find websites where there are many food images. Here are some good websites that I found out
- Yelp
- TripAdvisor
- Freepik
- Dreamstime
- iStock 

Yelp and TripAdvisor are restaurant reviews websites and the rest are stock images websites without watermarks obstructing the image. I manually collected and stored the data in my computer during my time doing the project which resulted in some ambiguous images. This results in me constantly cleaning the data multiple times and doing so every time I modify the dataset.
Uploading Data on Kaggle
Kaggle is one of the world's best platforms for storing datasets. Most datasets there are science datasets and there is no steak dataset yet, so then I decided to upload the dataset that I made on Kaggle so that I can use it in Google Colab while I'm coding. Machine Learning with FastAI FastAI is a library for machine learning and AI in Python made by Jeremy Howard. FastAI makes tasks like image classification as in the case of my project easier. All you have to do is import fastbook and fastai in the colab notebook.
#The Code
Now is the time to start coding!
## Step 1: Install and import libraries.
If we are going to use FastAI, we have to install and import the libraries first.
## Step 2: Upload the dataset from Kaggle.
After making the dataset manually in Kaggle, we will have to use it in our model. The most important part in this step is to not forget to unzip the data after uploading although you only have to do it once.
## Step 3: Create a DataBlock.
Thanks to FastAI, we can go ahead and create a DataBlock. In our DataBlock, we will use aug_transforms() for image augmentation as it will automatically augment images inside the data.
## Step 4: Use DataLoader on our DataBlock.
We then use DataLoaders to load our DataBlock which contains data that has been uploaded from Kaggle. At this point, we are now ready to train and fine tune our data.
## Step 5: Training time!
First, we will use our visual learner so that our data will train and we will be using resnet152 the latest version of resnet. Next, we will use lr_find() function to determine the optimal rate during fine tuning. For fine tuning, we will use epoch to fine tune our data. During coding, I have adjusted the number of epochs multiple times including freeze_epoch which pre calculates highest epochs before fine tuning with the main epochs. After countless hours of fine tuning, the optimal epoch number is 20 with 3 freeze_epochs as well.
## Step 6: Confusion Matrix
After fine tuning the data, we then line out a confusion matrix. A confusion matrix is a table that compares predicted value (or data) to actual value (or data) in the form of a matrix. This helps us determine our accuracy which can be calculated with the formula (sum of predicted==actual values)/(number of values). My model has an accuracy of 60%, which is not bad for a first timer!
## Step 7: Display the results.
Let's display the results of the prediction versus actual results of the images. This helps me visualize on what area or class of the data is most inaccurate. And that's the code! :)
Purpose of Steak Doneness Classifier
The main purpose for this AI model is to determine the doneness of the steak which helps people who are wary on the cook on their steak (rare steak can be dangerous if not handled properly). The model can correctly determine the doneness of steak with a 60% chance (most inaccurate predictions are one off the correct predictions on the steak doneness scale). The model can also help chefs who are training or in culinary school to use this classifier to determine the doneness of steak as well. All you need to do is take a photo of said steak and upload it on my application.
# Conclusion + Special Thanks
In conclusion, I programmed and trained an AI model using FastAI which can predict the doneness of a steak image (ranging from rare to well done) which has a 60% accuracy and this model will help people who are concerned on the doneness of the steak and training chefs as well. Finally, I would like to thank my mentors from the AI Builders Community especially P Mick, my family, my friends, and Stack Overflow! Without the aforementioned, I would not have succeeded in making this project. Thank you for reading this article!
# Links
Steak Doneness Classifier:

Google Colab: https://colab.research.google.com/drive/10Ou7pwsSA-b71ho2SntqZy840U7j4qCJ#scrollTo=6PzW7SktOcP_

GitHub: https://github.com/TheTrapperXD/steakdonenessclassifier

Streamlit:

Social Media Contacts

Email: satangpattanun@hotmail.com

Reddit (active): u/TheTrapperBeingXD

Instagram (inactive): satangpattanun

Facebook (inactive): Satang Pattanun

AI Builders Contacts

Facebook: AI Builders

YouTube: AI Builders
