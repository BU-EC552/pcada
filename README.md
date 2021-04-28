# PCADA

## Installation

First, navigate to https://github.com/Lattice-Automation/repp and follow the instructions for installing Repp on your
system.  We recommend Linux systems, as all of the development took place in this environment.

Second, make sure the following Python packages are installed.  If they are not installed, you can install them using
the python package manager, pip install [package_name]:

flask 
flask_restful
pandas
requests
primer3-py (https://pypi.org/project/primer3-py/)
dna_features_viewer (https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer)

Third, make sure you install SFML correctly.  If you are using a Linux system (recommended), 
then (https://www.sfml-dev.org/tutorials/2.5/start-linux.php):

```
sudo apt-get install libsfml-dev
```

## Test Case

Once all of the preliminaries are installed, move all of the CSV files in the company_files directory into the same
directory level as the pcada_gui.cpp application.  Make sure the target input sequence (in the example, As0.input.fa) 
is also at the same directory level as the pcada_gui.cpp application.  This is just to simplify pathing requirements.
Once all of the files are in the proper location, execute the following compile command:

```
g++ pcada_gui.cpp -o app -lsfml-graphics -lsfml-window -lsfml-system
```

And the application "app" should compile correctly.  Then, just run:

```
./app
```

And proceed with the rest of the test case.  Select the desired database and enter the name of the input file.  There
is no need to interact with Repp from the user's perspective - as long as you followed the steps above and installed
Repp, everything should run correctly.  It should take about 2.5 minutes for all of the different configurations to be
run through the Repp tool.  You may notice many "Error" messages in the terminal; they do not seem to impact the output,
and seem to occur due to the setting of unused configurations.  Just look for the output JSONs and the output PNGs to
see the result of the PCADA application.
