# lab2sml
Laboratory 2 for ID2223 HT23 Scalable Machine Learning and Deep Learning (50935) : Made by Merlijn Sevenhuijsen and Alessandro Meroli
Language: Dutch

After researching online about improvement techinques for Recurrent Neural Networks and different Data/model centric approaches we focused on two main proposal:
- tune a smaller set of hyperparameters, especially the learning rate
- at the beginnin we trained the model on a very small data set and in time we increased it.

# We have three different files for training the data
For feature engineering we have the whisper_dutch_feature_engineering.ipynb which takes the pretrained model and data for the dutch language and creates the features for the training and test set. The audio sampling rate is reduced to 16000hz. The features are then stored in the google drive.

For creating the model the model by openai is used. The model is trained on the data created by the feature engineering file. The model is then stored on huggingface "dussen/whisper-small-nl-hc"

For training the model we have the file whisper_dutch_training.ipynb which takes the model and the features and trains the model. The model is then stored on huggingface "dussen/whisper-small-nl-hc"


# For the extra tasks we have added a huggingface link
https://huggingface.co/spaces/dussen/Whisper_dutch

It has three pages, one where a person can speak dutch and it is then transcribed.
The second page uses a video as an input and then transcribes the audio.
The third page takes as input a link to a radio link that creates mp3 files, and this is then transcribed and put into chatGPT to define what is being played on the radio station. Examples for radio station links are:
Music -> https://25343.live.streamtheworld.com/WEB10_MP3_SC
News -> https://icecast.omroep.nl/radio1-bb-mp3 
