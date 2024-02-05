# project-template
A template repository for quick starting a new project.

## Windows environment
#### Prepare environment (run on PowerShell 7)
```bash
cd <project_dir>
$env:PYTHONPATH="$env:PYTHONPATH;${pwd}"
conda create --prefix ${pwd}\conda-env python=3.11.2
conda config --set env_prompt '({name}) '
conda activate ${pwd}\conda-env
pip install -U wheel ipykernel
pip install -r requirements.txt
```

#### Running locally (run on PowerShell 7)
```bash
cd <project_dir>
$env:PYTHONPATH="$env:PYTHONPATH;${pwd}"
conda activate ${pwd}\conda-env
python -m project_template
```
<br/>

## Linux environment
TBD
<br/><br/>

## Database configurations

**Redshift**
> <br/>
>
> 1. Specify database configuration in "project_template/config.py"
> ```
> REDSHIFT_CONFIG = {
>      'host': os.getenv('REDSHIFT_HOST', 'redshift-cluster-1.the1data.studio'),
>      'port': os.getenv('REDSHIFT_PORT', '5439'),
>      'user': os.getenv('REDSHIFT_USER', '<user>'),              # config here or in environment variables
>      'password': os.getenv('REDSHIFT_PASS', '<password>'),      # config here or in environment variables
>      'dbname': 'the1'
> }
> ```
> 2. Connect VPN before query
> <br/><br/>

**Google BigQuery**
> <br/>
>
> 1. Download gcp_service_account.json from https://centralgroup.sharepoint.com/sites/DSDataManagementBigDataAnalytics/_layouts/15/download.aspx?UniqueId=d883ff226fa14cfe9b56ba49b4be8c01&e=Ssj30X
> 2. Paste in project root directory
> <br/><br/>

<br/><br/>
## Contributing
Pull requests are welcome. For major changes, discuss with the codeowners.
