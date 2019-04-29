# CNN-MNIST-digit-recognition
handwritting recognition using mnist dataset

## To create a CNN model:-
1. Use Conda to load all the dependencies using this command 
```conda env create -f enviornment.yml``` 
This will load all the dependencies that are needed
2. Now do ```conda activate mnist-recognition```
3. Now run the minst-digit-recognition-github.py file to generate the model to detect images using this command ```python minst-digit-recognition-github.py```
4. Now you will see a model file named "finalized_model.sav"

## To use the model generated above to detect images:-
1. We are using the MINST database to get the test files. Open the "import-pickle-digitrecognition.py" file and look at line 30. You can edit image_index to any number between 1 to 10000 (which refers to the image file stored in the database)
2. Now run the file using ```python import-pickle-digitrecognition.py```

