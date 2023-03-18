## Steps 1-2: Runs the Python Script and asks for input  
py .\3x_plus_1.py
## Step 3: Runs the R Script
## You May have to edit the version of R
&"C:\Program Files\R\R-4.2.3\bin\Rscript.exe" .\3x_plus_1.R
## Step 4: Opens PDF in a browser
Start-Process ((Resolve-Path ".\rplot.pdf").Path)