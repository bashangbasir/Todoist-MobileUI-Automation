# Setel-MobileAutomation
## Setel Mobile Automatio Task 

### Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipenv
```bash
pip install pipenv
```
1. Run the command in cmd to install the dependencies
```bash
python -m pipenv install
```
2. Start the virtual env 
```bash
python -m pipenv shell
```
3. Create api_config.json in project directory
```bash
{
    "token" = "your token"
    "base_url": "https://api.todoist.com/rest/v1"
{
```
4. Run test 
```bash
python -m pytest
```
### Sample Result
![alt-text](https://github.com/bashangbasir/Setel-MobileAutomation/blob/master/result.gif)


### Notes
- Start the test on empty project Todoist App 
