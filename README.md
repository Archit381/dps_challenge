# **Folder Structure**

├── DPS_CHALLENGE  
│   ├── lib                             # Contains the encoder & model files in pkl format
│   ├── routers      
│   │   ├── Prediction
│   │       ├── prediction_route.py     # Contains the code for api route '/predict'. Defines a post method which accepts 4 values and returns predicted value
│   ├── utils
│   │   ├── ProcessingClass.py          # Contains the class for pre processing functions. Involves changing 'MONAT' to extract month name & one hot encoding for categorical columns 
│   ├── api.py                          # API
│   └── dps_challenge_notebook.ipynb    # Main notebook for pre-processing & training of the model. Contains the complete approach regarding this problem                 
├


