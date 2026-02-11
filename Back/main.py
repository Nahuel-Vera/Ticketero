# from src.utils.excel_generator import generar_excel_prueba

# if __name__ == "__main__":
#     generar_excel_prueba()


import time
from fastapi import FastAPI, Response
from Back.src.utils.config_chrome import selenium_config, run_browser

app = FastAPI()


@app.get("/test")
def test():
    driver = selenium_config()
    run_browser(driver)
    return {"status": "ok - navigated to Google successfully"}



@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)