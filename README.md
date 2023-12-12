cmd:
set BROWSER=ch

set RESULTS_DIR=E:\Py_project\ssqatest\reports  

set RESULTS_DIR=E:\Py_project\DATN_vMinh_181403383\Tests_with_Pytest_Framework\reports

pytest -m tcid1 --html=reports/testcae_id1_report.html --self-contained-html

pytest -m tcid1 --html=testcae_id1_report.html --self-contained-html
