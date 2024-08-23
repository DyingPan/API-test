import os

os.chdir(os.path.join(os.getcwd(), 'api_test_env'))
os.system("streamlit run st_scripts.py")
