import os

import pandas as pd

target_name = "all_users.json"

dfs = []
for dir, subdirs, files in os.walk(os.curdir):
    if "all_users.json" in files:
        df = pd.read_json(os.path.join(dir, "all_users.json"))
        try:
            df['screen_name'] = pd.Series([v['screen_name'] for v in df['user'].values])
            dfs.append(df)
            print("Worked for "+dir)
        except KeyError:
            print("Ignoring "+dir)

out = pd.concat(dfs)
out.to_csv("collection.csv",  index=False)