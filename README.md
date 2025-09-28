# califirnia_regretion

### neaded pograms:
1. [python](https://www.python.org/downloads/)
2. [vscode](https://code.visualstudio.com/)
3. [git](https://git-scm.com/downloads)
4. [docker](https://www.docker.com/products/docker-desktop/)

### create virtual enviorment......

     python -m venv venv_name --system-site-pacakages
    .\venv_name\Scripts\activate

### this is partialy enloseed to save space...recomend creating fully enclosed venv enviorment

### needed libs inside venv...
   1. Flask
   2. numpy
   3. pandas
   4. sklearn
   5. matplotlib <br>
if shared resorces is used no need to import, but if fully enclosed venv used ,pip insatll is needed

### needed libs in ipynp....
      1. numpy
      2. pandas
      3. matplotlib.pyplot
      4. seaborn
      5. sklearn.model_selection.train_test_split
      6. sklearn.preprocessing.StandardScaler
      7. sklearn.linear_model.LinearRegression
      8. sklearn.metrics.
            1. R2_score
            2. mean_squred_eror
            3. mean_absolute_eror
      9. pickle

### docor commands
    after installing docker-can run useing
      docker build -t <app_name> .
      docker run -p 8080:8080 <app_name>
### why docker needed
    docker creates images of the web app beacus its created in windows if someone downloads it and tries to run it locally in diffrent os it might not exicute sometimes,,and if pogram is more complex then it will be hard to find and locate "main.py"
### running in localhost without docker
    if you dont want to download docker and run locally you can just locate the "app.py/main.py"
    and run in vnev useing command
    -> python <filename>.py