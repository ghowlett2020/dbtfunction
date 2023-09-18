import azure.functions as func
import logging
import os, sys
import dbt_runner

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!!")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        
@app.route(route="HttpDBTTrigger")
def HttpDBTTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cwd = os.getcwd()
    ncwd = os.path.join(cwd,"demo")
        
    result = dbt_runner.DBTRunner().exec_dbt(ncwd)
  
    logging.info(result)
  
    return func.HttpResponse(f"It Run")