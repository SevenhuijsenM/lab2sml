# lab2sml
Laboratory 2 for ID2223 HT23 Scalable Machine Learning and Deep Learning (50935) : Made by Merlijn Sevenhuijsen and Alessandro Meroli
Language: Dutch

After researching online about improvement techinques for Recurrent Neural Networks and different Data/model centric approaches we focused on two main proposal:

Data centric:
- Have more data based on music. As we want to use the model to listen to radio and what is being said, it should know how to recognize music. For this we should have popular music that is being played on the radio and the transcription of it, luckily there is a lot of available music along with the lyrics which can be used. This also requires tuning of parameters towards this data.

Model centric:
- To improve the accuracy of our radio recognition model we can train a seperate model that tells whether music is being played, news is being given or advertisements are being played. This can then be used to get more accurate results for the radio recognition model as the functionality may differ. Moreover we can finetune the hyperparameters of the current model. At the beginning we trained the model on a very small data set and in time we increased it to get the best results. We can also apply a model to first seperate the vocals from the music and then use the speech recognition on this, basically chaining AI  models.

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
