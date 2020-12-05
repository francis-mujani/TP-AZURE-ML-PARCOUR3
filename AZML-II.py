from azureml.core import Workspace
from azureml.core import Workspace, Datastore, Dataset


# Get the workspace
ws = Workspace.from_config()

# Get the datastore
# blob_store = Datastore.get(ws, datastore_name='az_my_datastorage')
datastore = Datastore.get(ws, 'workspaceblobstore')



# create a TabularDataset from 1 file paths in datastore
datastore_paths = [(datastore, 'datasets/fairness_data.csv')] # get the path in datastore


#  Récupérer une référence vers ce dataset avec la classe Dataset.Tabular
data_objet = Dataset.Tabular.from_delimited_files(path=datastore_paths)

# Get a dataset from the workspace datasets collection
ds1 = ws.datasets['csv_test'] # On peut aussi récupèrer directement le dataset avec le workplace ws.datasets 

# convert objet in pandas dataframe
df_ = data_objet.to_pandas_dataframe()
# code to work with dataframe goes here, for example:
print(df_.head())