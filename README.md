# Folder Structure

.
├── ...
├── vecto_search   
│   ├── chroma_db                   # Contains the indexed data
│   ├── routers      
│   │   ├── Search
│   │       ├── search.py           # Contains the code for api route /search and uses the SearchClass from the utils folder pass user query and fetch results from the index'ed database
│   ├── utils
│   │   ├── SearchClass.py          # Contains the class for retreiving the stored index from chroma_db and constructing a retriever for future retreival based on user query
│   ├── search_api.py               # API
│   └── update_chroma_script.py     # Update script when the csv gets updated in Dataset folder                
└── ...


