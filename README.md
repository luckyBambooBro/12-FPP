# My School Finder (Beta)

A simple program that contains a pre-loaded database (although very limited at the moment) of schools. The program allows the user to select their desired filters to search through a database of schools. Providing an address also sorts the list of schools according to the distance from the address

## Requirements
Python 3.10 or higher

## Git Branches

This repo contains 2 branches:
- cli_UI: contains the program which was initially developed for the user to interact via the CLI. Contains more backend coding, and the UX is less than impressive
- main: UX is now run via the Streamlit module and displayed via a browser. This version is much more user friendly

**Recommended branch**: main

## How to Use My School Finder
1. From the command line, cd to your desired directory
2. Type `git clone https://github.com/luckyBambooBro/My_School_Finder_Beta.git`
3. There are 3 steps for setup. You will need to setup a venv and activate it, then install the modules in the requirements text file. Enter the 3 following commands
    - venv setup: `python3 -m venv venv`
    - activate venv: `source venv/bin/activate`
    - install requirements: `pip install -r requirements.txt`
4. As mentioned above, there are 2 main branches. Ensure you are on the main branch. The recommended branch for optimal UX is "main". Ensure you are on main by typing the following into your CLI 
`git switch main`
5. Start the program by typing into terminal: `streamlit run app.py`
Your terminal will notify you of a localhost address e.g. `http://localhost:8501`
6. If streamlit does not open the program in your browser automatically, copy and paste this localhost address into your browser to use the program