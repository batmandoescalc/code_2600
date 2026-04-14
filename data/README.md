This file serves a placeholder for where data will be stored for labs and other demos.

Note that the `.gitignore` file contains "data/*.csv" as one of the items, which means that all csv files stored in the data folder will **not** be shared in Github. This is for two reasons:
1.  Datasets tend to be large in size, so it's a bad habit to store multiple copies in different places. 
2.  Often data is stored in entirely separate location from code, for a variety of reasons (data is often shared across projects, data may have different security/permissions than code, data size might require a separate server/host, etc.). It's a good practice to keep code and data in _separate places_ so that you become comfortable calling data from other directories inside your code.

All csv files stored in this location will be called the same way in the code for your labs:
`sample = pd.read_csv('data/sample.csv')`
This is because your code is stored in the same directory as the `data` folder.

If you need to run code from the `demos` folder, then you will need to access the data as:
`sample = pd.read_csv('../data/sample.csv')`
This is because you first must exit the `demos` folder using `..`, and then you must enter the `data` folder to locate the csv file.